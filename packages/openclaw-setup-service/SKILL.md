---
name: openclaw-setup-service
description: Use when the user needs "大家都在养大龙虾🦞?" style help from AI Skills. OpenClaw 装机服务
---

# 大家都在养大龙虾🦞?

## Overview

OpenClaw 装机服务

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

Run `python3 scripts/run.py --params '{}'` for $openclaw-setup-service.

## Notes

This package was generated from AI Skills catalog metadata and keeps AI Skills APIs as the runtime backend for `openclaw-setup-service`.
