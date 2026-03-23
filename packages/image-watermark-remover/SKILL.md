---
name: image-watermark-remover
description: Use when the user needs "图片有水印不好处理?" style help from AI Skills. 图片去水印
---

# 图片有水印不好处理?

## Overview

图片去水印

## Invocation Mode

This skill uses `external-link` invocation.

## Authentication

Set these environment variables before running the packaged runner:

- `AISKILLS_BASE_URL` (default: `https://ai-skills.ai`)
- `AISKILLS_API_KEY` (required for authenticated API calls)
- `AISKILLS_TENANT_ID` (default: `default`)

## Parameters

Read `references/form-schema.json` for the current machine-readable input schema.

## Execution

Run `python3 scripts/run.py --params '{}'` for $image-watermark-remover.

## Notes

This package was generated from AI Skills catalog metadata and keeps AI Skills APIs as the runtime backend for `image-watermark-remover`.
