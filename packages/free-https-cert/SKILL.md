---
name: free-https-cert
description: Use when the user needs "网站还没 HTTPS?" style help from AI Skills. 免费 HTTPS 证书
---

# 网站还没 HTTPS?

## Overview

免费 HTTPS 证书

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

Run `python3 scripts/run.py --params '{}'` for $free-https-cert.

## Notes

This package was generated from AI Skills catalog metadata and keeps AI Skills APIs as the runtime backend for `free-https-cert`.
