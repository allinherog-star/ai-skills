#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

SKILL_ID = "douyin-realtime-hot-rise"
EXECUTE_PATH = "/api/v1/execute"

def fail(message):
    print(json.dumps({"success": False, "error": {"code": "RUNNER_ERROR", "message": message}}, ensure_ascii=False))
    sys.exit(1)

def load_params(raw):
    try:
        return json.loads(raw or "{}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid params JSON: {exc}")

def request_json(method, path, payload):
    base_url = os.getenv("AISKILLS_BASE_URL", "https://ai-skills.ai").rstrip("/")
    api_key = os.getenv("AISKILLS_API_KEY", "").strip()
    tenant_id = os.getenv("AISKILLS_TENANT_ID", "default").strip() or "default"
    if not api_key:
        fail("AISKILLS_API_KEY is required")
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{base_url}{path}",
        data=body,
        method=method,
        headers={
            "Content-Type": "application/json",
            "X-API-Key": api_key,
            "X-Tenant-Id": tenant_id,
        },
    )
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8")
        print(payload or json.dumps({"success": False, "error": {"code": f"HTTP_{exc.code}", "message": str(exc)}}, ensure_ascii=False))
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--params", default="{}")
    args = parser.parse_args()
    params = load_params(args.params)
    request_json("POST", EXECUTE_PATH, {"skillId": SKILL_ID, "params": params})

if __name__ == "__main__":
    main()
