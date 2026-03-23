#!/usr/bin/env python3
import json

print(json.dumps({
    "success": True,
    "data": {
        "invocationMode": "external-link",
        "externalLink": "https://freessl.cn/",
        "externalLinkLabel": "网站还没 HTTPS?",
        "message": "Open this external-link target to continue."
    }
}, ensure_ascii=False))
