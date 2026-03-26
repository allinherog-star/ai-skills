#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

SKILL_ID = "douyin-kol-search"
BASE_URL = "https://ai-skills.ai"
TENANT_ID = "default"
EXECUTE_PATH = "/api/v1/execute"
REQUEST_TIMEOUT_SECONDS = 15

def fail(message, code="RUNNER_ERROR"):
    print(json.dumps({"success": False, "error": {"code": code, "message": message}}, ensure_ascii=False))
    sys.exit(1)

def load_params(raw):
    try:
        return json.loads(raw or "{}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid params JSON: {exc}")

def build_api_url(path):
    if not BASE_URL.startswith("https://"):
        fail("BASE_URL must use HTTPS", "CONFIG_ERROR")
    if not path.startswith("/api/"):
        fail(f"Unsupported API path: {path}", "CONFIG_ERROR")
    return f"{BASE_URL}{path}"

def format_markdown(result):
    if isinstance(result, dict):
        data = result.get("data", {})
        if isinstance(data, dict) and "result" in data:
            items = data["result"]
            if isinstance(items, list) and len(items) > 0:
                lines = ["## 抖音 KOL 搜索结果\n"]
                lines.append("| 博主 | 粉丝 | 商业价值 | 互动率 | 内容方向 |")
                lines.append("|------|------|----------|--------|----------|")
                for item in items[:10]:
                    nickname = item.get("nickname", "-")
                    follower = item.get("follower_count", "-")
                    commercial = item.get("commercial_value", "-")
                    engagement = item.get("avg_engagement", "-")
                    style = item.get("content_style", "-")
                    lines.append(f"| {nickname} | {follower} | {commercial} | {engagement}% | {style} |")
                lines.append("")
                suggestions = data.get("suggestions", [])
                if suggestions:
                    lines.append("**建议：**")
                    for s in suggestions:
                        lines.append(f"- {s}")
                return "\n".join(lines)
    return json.dumps(result, ensure_ascii=False, indent=2)

def request_json(method, path, payload):
    api_key = os.getenv("AISKILLS_API_KEY", "").strip()
    if not api_key:
        print("[CONFIG_MISSING] AISKILLS_API_KEY 未配置。\n\n请运行以下命令配置：\n\n  export AISKILLS_API_KEY='your_api_key'\n\n配置完成后重新运行即可。")
        sys.exit(1)
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        build_api_url(path),
        data=body,
        method=method,
        headers={
            "Content-Type": "application/json",
            "X-API-Key": api_key,
            "X-Tenant-Id": TENANT_ID,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            result = json.loads(response.read().decode("utf-8"))
            if not result.get("success"):
                err = result.get("error", {})
                if err.get("code") == "QUOTA_EXCEEDED":
                    print("[QUOTA_EXCEEDED] 电量已用完。\n\n请前往以下地址购买电量包为技能充电：\n\n  https://ai-skills.ai\n")
                    sys.exit(1)
            print(format_markdown(result))
    except urllib.error.HTTPError as exc:
        payload_text = exc.read().decode("utf-8")
        try:
            parsed = json.loads(payload_text)
        except json.JSONDecodeError:
            parsed = {"success": False, "error": {"code": f"HTTP_{exc.code}", "message": str(exc)}}
        err = parsed.get("error", {})
        if err.get("code") == "QUOTA_EXCEEDED":
            print("[QUOTA_EXCEEDED] 电量已用完。\n\n请前往以下地址购买电量包为技能充电：\n\n  https://ai-skills.ai\n")
            sys.exit(1)
        print(json.dumps(parsed, ensure_ascii=False, indent=2))
        sys.exit(1)
    except urllib.error.URLError as exc:
        reason = getattr(exc, "reason", str(exc))
        fail(f"网络请求失败: {reason}", "NETWORK_ERROR")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--params", default="{}")
    args = parser.parse_args()
    params = load_params(args.params)
    request_json("POST", EXECUTE_PATH, {"skillId": SKILL_ID, "params": params})

if __name__ == "__main__":
    main()
