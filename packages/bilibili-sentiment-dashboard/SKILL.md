---
name: bilibili-sentiment-dashboard
description: >
  B站评论舆情分析与up主运营建议。当用户提供B站视频/直播的链接，
  需要分析评论舆情、弹幕情感、用户反馈或up主运营建议时激活。
  即使用户只说"帮我看看B站这个视频的评论"或"分析下这个视频的弹幕"，
  也应激活此技能。
compatibility: >
  需要配置 AISKILLS_API_KEY（必填）。BASE_URL 和 TENANT_ID 已内置，无需配置。
  使用三步异步工作流：parse-link -> create-task -> get-task（平台固定为B站）。
---

# B站评论舆情分析

## 概述

当用户提供B站分享链接，需要分析视频评论、弹幕舆情、用户反馈或up主运营建议时，激活此技能。

该技能通过 3 步异步工作流调用后端 API，获取评论情感分析、弹幕密度分析、用户画像与up主运营建议。

## 调用方式

三步异步工作流：

1. **步骤 1: parse-link** — 从分享链接中提取内容 ID 和标题（平台固定为B站）
2. **步骤 2: create-task** — 提交舆情分析任务，获取任务 ID
3. **步骤 3: get-task** — 轮询任务状态，直至完成（最多重试 60 次，间隔 2 秒）

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | B站分享链接 |

## 执行方式

运行时通过 `scripts/run.py` 执行：

```bash
python3 scripts/run.py --params '{"link":"https://www.bilibili.com/video/BV1xx411c7mD"}'
```

## 环境变量

| 环境变量 | 说明 |
|----------|------|
| `AISKILLS_API_KEY` | API 密钥（必填），请运行 `export AISKILLS_API_KEY='your_api_key'` 配置 |

## 输出格式

```
## B站评论舆情分析

### 情感分析（正面）

| 正面 | 中性 | 负面 |
|------|------|------|
| 71% | 21% | 8% |

**高热词：** #硬核 #干货 #涨知识 #三连

### 转化潜力：82/100（高）

### 运营建议
- ...
```

详细格式规范见 [references/output-format.md](references/output-format.md)。
