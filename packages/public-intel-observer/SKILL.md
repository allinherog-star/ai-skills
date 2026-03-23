---
name: public-intel-observer
description: Use when the user needs "公共情报第一观察员" style help from AI Skills. 公共舆情与热点情报观察能力，即将上线
---

# 公共情报第一观察员

## Overview

公共舆情与热点情报观察能力，即将上线

## Invocation Mode

This skill uses `manual` invocation.

## Authentication

Set these environment variables before running the packaged runner:

- `AISKILLS_BASE_URL` (default: `https://ai-skills.ai`)
- `AISKILLS_API_KEY` (required for authenticated API calls)
- `AISKILLS_TENANT_ID` (default: `default`)

## Parameters

Read `references/form-schema.json` for the current machine-readable input schema.

## Execution

Run `python3 scripts/run.py --params '{}'` for $public-intel-observer.

## Notes

This package is currently marked as `coming-soon` and should stay discoverable without pretending it is callable.
