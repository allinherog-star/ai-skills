#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

PARSE_LINK_PATH = "/api/v1/comment-analysis/parse-link"
CREATE_TASK_PATH = "/api/v1/comment-analysis/tasks"
GET_TASK_PATH_TEMPLATE = "/api/v1/comment-analysis/tasks/{task_id}"
FIXED_PLATFORM = "xhs"

def fail(message):
    print(json.dumps({"success": False, "error": {"code": "RUNNER_ERROR", "message": message}}, ensure_ascii=False))
    sys.exit(1)

def load_params(raw):
    try:
        return json.loads(raw or "{}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid params JSON: {exc}")

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

def request_json(method, path, payload):
    base_url = os.getenv("AISKILLS_BASE_URL", "https://ai-skills.ai").rstrip("/")
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(f"{base_url}{path}", data=body, method=method, headers=build_headers())
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload_text = exc.read().decode("utf-8")
        try:
            parsed = json.loads(payload_text)
        except json.JSONDecodeError:
            parsed = {"success": False, "error": {"code": f"HTTP_{exc.code}", "message": str(exc)}}
        print(json.dumps(parsed, ensure_ascii=False))
        sys.exit(1)

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
