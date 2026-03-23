#!/usr/bin/env python3
import json

print(json.dumps({
    "success": True,
    "data": {
        "invocationMode": "external-link",
        "externalLink": "https://ipdata.co/",
        "externalLinkLabel": "TikTok 直播 IP 合规吗?",
        "message": "Open this external-link target to continue."
    }
}, ensure_ascii=False))
