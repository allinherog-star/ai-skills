#!/usr/bin/env python3
import argparse
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

SKILL_ID = "douyin-kol-search"
EXECUTE_PATH = "/api/execute"
DEFAULT_BASE_URL = "https://ai-skills.ai"
RECHARGE_URL = "https://ai-skills.ai/user/billing"
SKILL_URL = "https://ai-skills.ai/zh/skills/douyin-kol-search"
REQUEST_TIMEOUT_SECONDS = 15

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

def print_url_error(exc):
    reason = getattr(exc, "reason", exc)
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
    payload_text = exc.read().decode("utf-8")
    try:
        parsed = json.loads(payload_text)
    except json.JSONDecodeError:
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

def request_json(method, path, payload, timeout=REQUEST_TIMEOUT_SECONDS):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{build_base_url()}{path}",
        data=body,
        method=method,
        headers=build_headers(),
    )
    try:
        with OPENER.open(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print_http_error(exc)
    except urllib.error.URLError as exc:
        print_url_error(exc)

def is_async_terminal(data):
    status = data.get("status")
    return status in {"completed", "failed", "needs_input", "cancelled"}

def poll_async_result(start_response, max_attempts, interval_seconds, timeout_seconds):
    data = start_response.get("data") or {}
    if data.get("mode") != "async":
        return start_response
    if is_async_terminal(data):
        return start_response

    execution_id = data.get("executionId") or data.get("turnId")
    job_id = data.get("jobId")
    if not execution_id and not job_id:
        return start_response

    deadline = time.monotonic() + timeout_seconds
    for _ in range(max_attempts):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        time.sleep(min(interval_seconds, remaining))
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        response = request_json("POST", EXECUTE_PATH, {
            "skillId": SKILL_ID,
            "params": {},
            "execution": {
                "action": "poll",
                "executionId": execution_id,
                "jobId": job_id,
            },
        }, timeout=min(REQUEST_TIMEOUT_SECONDS, remaining))
        data = response.get("data") or {}
        if data.get("mode") == "async" and is_async_terminal(data):
            return response

    fail(f"Async skill execution did not finish within {timeout_seconds:g} seconds; increase --poll-timeout to wait longer")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--params", default="{}")
    parser.add_argument("--poll-attempts", type=int, default=60, help="maximum number of async status checks")
    parser.add_argument("--poll-interval", type=float, default=2.0, help="seconds between async status checks")
    parser.add_argument("--poll-timeout", type=float, default=120.0, help="maximum async wait in seconds")
    args = parser.parse_args()
    if args.poll_attempts < 1 or args.poll_interval <= 0 or args.poll_timeout <= 0:
        parser.error("poll attempts, interval, and timeout must be positive")
    params = load_params(args.params)
    response = request_json("POST", EXECUTE_PATH, {"skillId": SKILL_ID, "params": params})
    print(json.dumps(poll_async_result(response, args.poll_attempts, args.poll_interval, args.poll_timeout), ensure_ascii=False))

if __name__ == "__main__":
    main()
