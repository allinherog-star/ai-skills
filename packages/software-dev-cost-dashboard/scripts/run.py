#!/usr/bin/env python3
import json

print(json.dumps({
    "success": True,
    "data": {
        "invocationMode": "external-link",
        "externalLink": "https://soft-offer.aiskills.icu/",
        "externalLinkLabel": "软件开发成本不可控?",
        "message": "Open this external-link target to continue."
    }
}, ensure_ascii=False))
