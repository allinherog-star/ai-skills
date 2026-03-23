#!/usr/bin/env python3
import json

print(json.dumps({
    "success": True,
    "data": {
        "invocationMode": "external-link",
        "externalLink": "https://www.notion.com/",
        "externalLinkLabel": "文档和知识库太乱?",
        "message": "Open this external-link target to continue."
    }
}, ensure_ascii=False))
