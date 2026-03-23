#!/usr/bin/env python3
import json

print(json.dumps({
    "success": True,
    "data": {
        "invocationMode": "external-link",
        "externalLink": "https://ezremove.ai/zh/video-watermark-remover/#video-watermark-remover",
        "externalLinkLabel": "免费去水印",
        "message": "Open this external-link target to continue."
    }
}, ensure_ascii=False))
