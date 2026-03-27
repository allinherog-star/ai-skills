---
name: kuaishou-sentiment-dashboard
description: Use when the user needs "快手短视频如何运营?" style help from AI Skills. 快手短视频运营增长助手
---

# 快手短视频如何运营?

## Overview

快手短视频运营增长助手

## Invocation Mode

This skill uses `comment-analysis-task` invocation.

## Authentication

Set these environment variables before running the packaged runner:

- `AISKILLS_BASE_URL` (default: `https://ai-skills.ai`)
- `AISKILLS_API_KEY` (required for authenticated API calls)
- `AISKILLS_TENANT_ID` (default: `default`)

## Parameters

Read `references/form-schema.json` for the current machine-readable input schema.

## Execution

Run `python3 scripts/run.py --params '{}'` for $kuaishou-sentiment-dashboard.

## Notes

This package was generated from AI Skills catalog metadata and keeps AI Skills APIs as the runtime backend for `kuaishou-sentiment-dashboard`.
