#!/usr/bin/env python3
import argparse
import json
import math
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

SKILL_ID = "douyin-realtime-hot-rise"
EXECUTE_PATH = "/api/execute"
DEFAULT_BASE_URL = "https://ai-skills.ai"
RECHARGE_URL = "https://ai-skills.ai/user/billing"
SKILL_URL = "https://ai-skills.ai/zh/skills/douyin-realtime-hot-rise"

def fail(message):
    print(json.dumps({"success": False, "error": {"code": "RUNNER_ERROR", "message": message}}, ensure_ascii=False))
    sys.exit(1)

def load_params(raw):
    try:
        return json.loads(raw or "{}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid params JSON: {exc}")

def build_base_url():
    base_url = os.getenv("AISKILLS_BASE_URL", DEFAULT_BASE_URL).strip().rstrip("/")
    try:
        parsed = urllib.parse.urlsplit(base_url)
        port = parsed.port
    except ValueError:
        fail("AISKILLS_BASE_URL must be an HTTPS URL for ai-skills.ai")

    if (
        parsed.scheme.lower() != "https"
        or parsed.hostname is None
        or parsed.hostname.lower() != "ai-skills.ai"
        or parsed.username is not None
        or parsed.password is not None
        or port not in (None, 443)
        or parsed.query
        or parsed.fragment
    ):
        fail("AISKILLS_BASE_URL must be an HTTPS URL for ai-skills.ai")
    return base_url

def build_headers():
    api_key = os.getenv("AISKILLS_API_KEY", "").strip()
    tenant_id = os.getenv("AISKILLS_TENANT_ID", "default").strip() or "default"
    if not api_key:
        fail(
            f"未检测到 AISKILLS_API_KEY。请按以下步骤操作：1) 登录 https://ai-skills.ai；"
            f"2) 打开 API Key 页面创建或复制密钥：https://ai-skills.ai/zh/user/api-key；"
            f"3) 将密钥配置为环境变量 AISKILLS_API_KEY；4) 重新运行本技能。配置说明：{SKILL_URL}"
        )
    return {
        "Content-Type": "application/json",
        # Cloudflare blocks urllib's default Python user agent for this endpoint.
        "User-Agent": "ai-skills-runner/1.0 (+https://ai-skills.ai)",
        "Accept": "application/json",
        "X-API-Key": api_key,
        "X-Tenant-Id": tenant_id,
    }

def build_ssl_context():
    if os.getenv("SSL_CERT_FILE") or os.getenv("SSL_CERT_DIR"):
        return ssl.create_default_context()
    try:
        import certifi
    except ImportError:
        return ssl.create_default_context()
    return ssl.create_default_context(cafile=certifi.where())

SSL_CONTEXT = build_ssl_context()

class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

OPENER = urllib.request.build_opener(
    urllib.request.HTTPSHandler(context=SSL_CONTEXT),
    NoRedirectHandler(),
)

REQUEST_TIMEOUT_SECONDS = 20
MAX_POLL_ATTEMPTS = 180
MAX_POLL_INTERVAL_SECONDS = 30

def validate_params(params):
    if not isinstance(params, dict):
        fail("参数必须是 JSON 对象，例如 --params '{\"keyword\":\"奥运\"}'")

    allowed = {"tag", "order", "keyword"}
    unknown = sorted(set(params) - allowed)
    if unknown:
        fail(f"不支持的参数: {', '.join(unknown)}。可用参数为 tag、order、keyword")

    tag = params.get("tag")
    if tag is not None and not isinstance(tag, str):
        fail("tag 必须是字符串分类 ID；多个分类 ID 用英文逗号分隔")
    if isinstance(tag, str) and tag.strip():
        ids = [part.strip() for part in tag.split(",")]
        if any(not re.fullmatch(r"[0-9]+", value) for value in ids):
            fail("tag 格式错误：请输入分类接口返回的数字 ID；多个 ID 用英文逗号分隔，例如 5000,6000")

    order = params.get("order")
    if order is not None and (not isinstance(order, str) or order not in {"rank", "rank_diff"}):
        fail("order 只支持 rank（热度排序）或 rank_diff（排名变化排序）")

    keyword = params.get("keyword")
    if keyword is not None and not isinstance(keyword, str):
        fail("keyword 必须是字符串")
    if isinstance(keyword, str) and len(keyword) > 100:
        fail(f"keyword 最多 100 个字符，当前为 {len(keyword)} 个；请缩短关键词后重试")

def print_url_error(exc):
    reason = getattr(exc, "reason", exc)
    if isinstance(reason, TimeoutError):
        fail(f"请求超过 {REQUEST_TIMEOUT_SECONDS} 秒仍未完成。请检查网络后重试；若持续发生，请稍后再试")
    code = "SSL_CERTIFICATE_VERIFY_FAILED" if isinstance(reason, ssl.SSLCertVerificationError) else "NETWORK_ERROR"
    message = str(reason)
    if code == "SSL_CERTIFICATE_VERIFY_FAILED":
        message = (
            "HTTPS certificate verification failed. Install certifi or set SSL_CERT_FILE "
            f"to a valid CA bundle, then retry: {reason}"
        )
    print(json.dumps({"success": False, "error": {"code": code, "message": message}}, ensure_ascii=False))
    sys.exit(1)

def print_http_error(exc):
    payload_text = exc.read().decode("utf-8", errors="replace")
    try:
        parsed = json.loads(payload_text)
    except (json.JSONDecodeError, UnicodeDecodeError):
        parsed = {"success": False, "error": {"code": f"HTTP_{exc.code}", "message": str(exc)}}

    error = parsed.setdefault("error", {})
    code = error.get("code") or f"HTTP_{exc.code}"
    if exc.code == 402 or code == "BILLING_BALANCE_INSUFFICIENT":
        error["code"] = "BILLING_BALANCE_INSUFFICIENT"
        error["message"] = f"余额不足，请前往 {RECHARGE_URL} 充值后重试"
        meta = parsed.setdefault("meta", {})
        meta["rechargeUrl"] = RECHARGE_URL

    print(json.dumps(parsed, ensure_ascii=False))
    sys.exit(1)

def request_json(method, path, payload):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{build_base_url()}{path}",
        data=body,
        method=method,
        headers=build_headers(),
    )
    try:
        with OPENER.open(req, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print_http_error(exc)
    except urllib.error.URLError as exc:
        print_url_error(exc)
    except TimeoutError:
        fail(f"请求超过 {REQUEST_TIMEOUT_SECONDS} 秒仍未完成。请检查网络后重试；若持续发生，请稍后再试")
    except json.JSONDecodeError:
        fail("服务返回的内容不是有效 JSON。请稍后重试；若持续发生，请联系技能提供方")

def is_async_terminal(data):
    status = data.get("status")
    return status in {"completed", "failed", "needs_input", "cancelled"}

def poll_async_result(start_response, max_attempts, interval_seconds):
    data = start_response.get("data") or {}
    if data.get("mode") != "async":
        return start_response
    if is_async_terminal(data):
        return start_response

    execution_id = data.get("executionId") or data.get("turnId")
    job_id = data.get("jobId")
    if not execution_id and not job_id:
        return start_response

    if max_attempts < 1 or max_attempts > MAX_POLL_ATTEMPTS:
        fail(f"--poll-attempts 必须在 1 到 {MAX_POLL_ATTEMPTS} 之间")
    if not math.isfinite(interval_seconds) or interval_seconds <= 0 or interval_seconds > MAX_POLL_INTERVAL_SECONDS:
        fail(f"--poll-interval 必须大于 0 且不超过 {MAX_POLL_INTERVAL_SECONDS} 秒")

    for _ in range(max_attempts):
        time.sleep(interval_seconds)
        response = request_json("POST", EXECUTE_PATH, {
            "skillId": SKILL_ID,
            "params": {},
            "execution": {
                "action": "poll",
                "executionId": execution_id,
                "jobId": job_id,
            },
        })
        data = response.get("data") or {}
        if data.get("mode") == "async" and is_async_terminal(data):
            return response

    elapsed = max_attempts * interval_seconds
    fail(f"任务等待超过约 {elapsed:g} 秒仍未完成。可稍后重新查询；本次任务可能仍在服务端运行")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--params", default="{}")
    parser.add_argument("--poll-attempts", type=int, default=180)
    parser.add_argument("--poll-interval", type=float, default=2.0)
    args = parser.parse_args()
    params = load_params(args.params)
    validate_params(params)
    if args.poll_attempts < 1 or args.poll_attempts > MAX_POLL_ATTEMPTS:
        fail(f"--poll-attempts 必须在 1 到 {MAX_POLL_ATTEMPTS} 之间")
    if not math.isfinite(args.poll_interval) or args.poll_interval <= 0 or args.poll_interval > MAX_POLL_INTERVAL_SECONDS:
        fail(f"--poll-interval 必须大于 0 且不超过 {MAX_POLL_INTERVAL_SECONDS} 秒")
    response = request_json("POST", EXECUTE_PATH, {"skillId": SKILL_ID, "params": params})
    print(json.dumps(poll_async_result(response, args.poll_attempts, args.poll_interval), ensure_ascii=False))

if __name__ == "__main__":
    main()
