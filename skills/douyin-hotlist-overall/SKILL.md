---
name: douyin-hotlist-overall
description: Use when the user needs "现在最热门的是什么？" style help from AI Skills. 抖音全网实时热点
---

# 现在最热门的是什么？

## Overview

抖音全网实时热点

## Invocation Mode

This skill uses `execute` invocation.

## Authentication

Set these environment variables before running the packaged runner:

- `AISKILLS_BASE_URL` (default: `https://ai-skills.ai`)
- `AISKILLS_API_KEY` (required for authenticated API calls)
- `AISKILLS_TENANT_ID` (default: `default`)

## Parameters

Read `references/form-schema.json` for the current machine-readable input schema.

## Execution

Run `python3 scripts/run.py --params '{}'` for $douyin-hotlist-overall.

## Notes

This package was generated from AI Skills catalog metadata and keeps AI Skills APIs as the runtime backend for `douyin-hotlist-overall`.
