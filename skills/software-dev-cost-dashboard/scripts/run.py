#!/usr/bin/env python3
import json

print(json.dumps({
    "success": True,
    "data": {
        "invocationMode": "external-link",
        "externalLink": "https://soft.ai-skills.ai",
        "externalLinkLabel": "打开成本看板",
        "message": "Open this external-link target to continue."
    }
}, ensure_ascii=False))
