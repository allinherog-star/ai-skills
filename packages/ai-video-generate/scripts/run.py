#!/usr/bin/env python3
import json

print(json.dumps({
    "success": True,
    "data": {
        "invocationMode": "external-link",
        "externalLink": "https://jimeng.jianying.com/ai-tool/generate",
        "externalLinkLabel": "想直接生成 AI 视频?",
        "message": "Open this external-link target to continue."
    }
}, ensure_ascii=False))
