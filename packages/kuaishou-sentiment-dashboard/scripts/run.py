#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

FIXED_PLATFORM = "kuaishou"
BASE_URL = "https://ai-skills.ai"
TENANT_ID = "default"
PARSE_LINK_PATH = "/api/v1/comment-analysis/parse-link"
CREATE_TASK_PATH = "/api/v1/comment-analysis/tasks"
GET_TASK_PATH_TEMPLATE = "/api/v1/comment-analysis/tasks/{task_id}"

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
    if not api_key:
        print("[CONFIG_MISSING] AISKILLS_API_KEY 未配置。\n\n请运行以下命令配置：\n\n  export AISKILLS_API_KEY='your_api_key'\n\n配置完成后重新运行即可。")
        sys.exit(1)
    return {
        "Content-Type": "application/json",
        "X-API-Key": api_key,
        "X-Tenant-Id": TENANT_ID,
    }

def request_json(method, path, payload=None):
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}{path}",
        data=body,
        method=method,
        headers=build_headers(),
    )
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
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

def format_markdown(result):
    platform_name = "快手"
    if isinstance(result, dict):
        data = result.get("data", {})
        if isinstance(data, dict) and "result" in data:
            r = data["result"]
            lines = [f"## {platform_name}评论舆情分析\n"]
            sentiment = r.get("sentiment", {})
            pos = sentiment.get("positive", 0)
            neu = sentiment.get("neutral", 0)
            neg = sentiment.get("negative", 0)
            label = sentiment.get("sentimentLabel", "neutral")
            emoji = {"positive": "正面", "neutral": "中性", "negative": "负面"}.get(label, "中性")
            lines.append(f"### 情感分析（{emoji}）\n")
            lines.append(f"| 正面 | 中性 | 负面 |")
            lines.append(f"|------|------|------|")
            lines.append(f"| {pos}% | {neu}% | {neg}% |")
            lines.append("")
            profile = r.get("userProfile", {})
            keywords = profile.get("topKeywords", [])
            if keywords:
                lines.append(f"**高热词：** {' '.join(keywords[:8])}")
                lines.append("")
            cp = r.get("conversionPotential", 0)
            if isinstance(cp, int):
                if cp >= 80: level = "极高"
                elif cp >= 60: level = "高"
                elif cp >= 40: level = "中等"
                else: level = "低"
                lines.append(f"### 转化潜力：{cp}/100（{level}）\n")
            metrics = r.get("engagementMetrics", {})
            if metrics:
                lines.append("### 互动指标\n")
                lines.append(f"- 点赞：{metrics.get('likes', '-')}  评论：{metrics.get('comments', '-')}  转发：{metrics.get('shares', '-')}  收藏：{metrics.get('collects', '-')}")
                lines.append("")
            suggestions = r.get("suggestions", [])
            if suggestions:
                lines.append("### 运营建议\n")
                for s in suggestions:
                    lines.append(f"- {s}")
            return "\n".join(lines)
    return json.dumps(result, ensure_ascii=False, indent=2)

def poll_task(task_id, max_attempts=60, interval=2):
    for _ in range(max_attempts):
        response = request_json("GET", GET_TASK_PATH_TEMPLATE.format(task_id=task_id))
        task = response.get("data", {}).get("task", {})
        status = task.get("status")
        if status == "completed":
            print(format_markdown(response))
            return
        elif status == "failed":
            fail("任务执行失败")
        time.sleep(interval)
    fail("任务超时，请稍后重试")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--params", default="{}")
    args = parser.parse_args()
    params = load_params(args.params)
    link = str(params.get("link", "")).strip()
    if not link:
        fail("link 参数必填")
    parsed = request_json("POST", PARSE_LINK_PATH, {"input": link, "platform": FIXED_PLATFORM})
    parsed_data = parsed.get("data", {})
    create_payload = {
        "platform": FIXED_PLATFORM,
        "contentId": parsed_data.get("contentId"),
        "contentTitle": parsed_data.get("contentTitle"),
        "options": {"sourceUrl": parsed_data.get("sourceUrl")},
    }
    task_resp = request_json("POST", CREATE_TASK_PATH, create_payload)
    task_id = task_resp.get("data", {}).get("task", {}).get("id")
    if not task_id:
        fail("创建任务失败")
    poll_task(task_id)

if __name__ == "__main__":
    main()
