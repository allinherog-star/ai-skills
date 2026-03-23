#!/usr/bin/env python3
import json

print(json.dumps({
    "success": True,
    "data": {
        "invocationMode": "external-link",
        "externalLink": "https://www.dzine.ai/tools/ai-watermark-remover/",
        "externalLinkLabel": "图片有水印不好处理?",
        "message": "Open this external-link target to continue."
    }
}, ensure_ascii=False))
