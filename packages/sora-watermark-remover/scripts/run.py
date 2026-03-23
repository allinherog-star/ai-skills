#!/usr/bin/env python3
import json

print(json.dumps({
    "success": True,
    "data": {
        "invocationMode": "external-link",
        "externalLink": "https://www.removesorawatermark.online/",
        "externalLinkLabel": "Sora 2 水印去不掉?",
        "message": "Open this external-link target to continue."
    }
}, ensure_ascii=False))
