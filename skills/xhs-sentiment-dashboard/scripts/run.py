#!/usr/bin/env python3
import argparse
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request

PARSE_LINK_PATH = "/api/comment-analysis/parse-link"
CREATE_TASK_PATH = "/api/comment-analysis/tasks"
GET_TASK_PATH_TEMPLATE = "/api/comment-analysis/tasks/{task_id}"
FIXED_PLATFORM = "xhs"
DEFAULT_BASE_URL = "https://ai-skills.ai"

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

def request_json(method, path, payload):
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{build_base_url()}{path}",
        data=body,
        method=method,
        headers=build_headers(),
    )
    try:
        with urllib.request.urlopen(req, context=SSL_CONTEXT) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload_text = exc.read().decode("utf-8")
        try:
            parsed = json.loads(payload_text)
        except json.JSONDecodeError:
            parsed = {"success": False, "error": {"code": f"HTTP_{exc.code}", "message": str(exc)}}
        print(json.dumps(parsed, ensure_ascii=False))
        sys.exit(1)
    except urllib.error.URLError as exc:
        print_url_error(exc)

def poll_task_until_terminal(task_id, max_attempts=60, interval_seconds=2):
    for _ in range(max_attempts):
        response = request_json("GET", GET_TASK_PATH_TEMPLATE.format(task_id=task_id), None)
        task = response.get("data", {}).get("task", {})
        status = task.get("status")
        if status in {"completed", "failed"}:
            print(json.dumps(response, ensure_ascii=False))
            return
        time.sleep(interval_seconds)
    fail("Comment analysis task did not reach a terminal state in time")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--params", default="{}")
    args = parser.parse_args()
    params = load_params(args.params)
    link = str(params.get("link", "")).strip()
    if not link:
        fail("link is required")

    parse_payload = {"input": link}
    if FIXED_PLATFORM:
        parse_payload["platform"] = FIXED_PLATFORM
    elif params.get("platform"):
        parse_payload["platform"] = params["platform"]

    parsed = request_json("POST", PARSE_LINK_PATH, parse_payload)
    parsed_data = parsed.get("data", {})
    create_payload = {
        "platform": FIXED_PLATFORM or parsed_data.get("platform"),
        "contentId": parsed_data.get("contentId"),
        "contentTitle": parsed_data.get("contentTitle"),
        "options": {
            "sourceUrl": parsed_data.get("sourceUrl"),
        },
    }
    task_response = request_json("POST", CREATE_TASK_PATH, create_payload)
    task_id = task_response.get("data", {}).get("task", {}).get("id")
    if not task_id:
        fail("Comment analysis task id missing from create-task response")
    poll_task_until_terminal(task_id)

if __name__ == "__main__":
    main()
