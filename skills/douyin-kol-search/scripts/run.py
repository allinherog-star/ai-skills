#!/usr/bin/env python3
import argparse
import json
import os
import ssl
import sys
import urllib.error
import urllib.request

SKILL_ID = "douyin-kol-search"
EXECUTE_PATH = "/api/execute"
DEFAULT_BASE_URL = "https://ai-skills.ai"
RECHARGE_URL = "https://ai-skills.ai/user/billing"

def fail(message):
    print(json.dumps({"success": False, "error": {"code": "RUNNER_ERROR", "message": message}}, ensure_ascii=False))
    sys.exit(1)

def load_params(raw):
    try:
        return json.loads(raw or "{}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid params JSON: {exc}")

def build_base_url():
    return os.getenv("AISKILLS_BASE_URL", DEFAULT_BASE_URL).rstrip("/")

def build_headers():
    api_key = os.getenv("AISKILLS_API_KEY", "").strip()
    tenant_id = os.getenv("AISKILLS_TENANT_ID", "default").strip() or "default"
    if not api_key:
        fail("AISKILLS_API_KEY is required")
    return {
        "Content-Type": "application/json",
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

def request_text(method, path, payload):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{build_base_url()}{path}",
        data=body,
        method=method,
        headers=build_headers(),
    )
    try:
        with urllib.request.urlopen(req, context=SSL_CONTEXT) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        print_http_error(exc)
    except urllib.error.URLError as exc:
        print_url_error(exc)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--params", default="{}")
    args = parser.parse_args()
    params = load_params(args.params)
    print(request_text("POST", EXECUTE_PATH, {"skillId": SKILL_ID, "params": params}))

if __name__ == "__main__":
    main()
