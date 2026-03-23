---
name: notion-workspace
description: Use when the user needs "文档和知识库太乱?" style help from AI Skills. Notion 文档管理工作台
---

# 文档和知识库太乱?

## Overview

Notion 文档管理工作台

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

Run `python3 scripts/run.py --params '{}'` for $notion-workspace.

## Notes

This package was generated from AI Skills catalog metadata and keeps AI Skills APIs as the runtime backend for `notion-workspace`.
