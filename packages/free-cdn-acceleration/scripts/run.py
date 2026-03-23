#!/usr/bin/env python3
import json

print(json.dumps({
    "success": True,
    "data": {
        "invocationMode": "external-link",
        "externalLink": "https://www.dogecloud.com/",
        "externalLinkLabel": "网站访问太慢?",
        "message": "Open this external-link target to continue."
    }
}, ensure_ascii=False))
