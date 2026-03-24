---
name: unified-comment-analysis
description: >
  多平台舆情监控与运营洞察大盘。当用户提供抖音、小红书、B站、快手的分享链接，
  需要分析评论舆情、用户画像、转化潜力或运营建议时激活。
  即使用户只说"帮我分析下这个视频的评论"或"看看这个帖子反响如何"，
  也应激活此技能。支持平台：抖音、小红书、B站、快手。
compatibility: >
  需要配置 AISKILLS_API_KEY（必填）。BASE_URL 和 TENANT_ID 已内置，无需配置。
  使用三步异步工作流：parse-link -> create-task -> get-task。
---

# 多平台舆情监控与运营洞察大盘

## 概述

当用户提供抖音、小红书、B站或快手的分享链接，需要分析评论舆情、用户画像、转化潜力或运营建议时，激活此技能。

该技能通过 3 步异步工作流（parse-link -> create-task -> get-task）调用后端 API，获取评论情感分析、用户画像、转化潜力评估与运营建议。

## 调用方式

本技能使用三步异步工作流：

1. **步骤 1: parse-link** (`POST /api/v1/comment-analysis/parse-link`)：从分享链接中提取平台类型、内容 ID 和标题
2. **步骤 2: create-task** (`POST /api/v1/comment-analysis/tasks`)：提交舆情分析任务，获取任务 ID
3. **步骤 3: get-task** (`GET /api/v1/comment-analysis/tasks/:id`)：轮询任务状态，直至完成（最多重试 60 次，间隔 2 秒）

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | 分享链接，格式为 URI（抖音/小红书/B站/快手） |
| `platform` | enum | 否 | 平台类型，可选值：`douyin`（抖音）、`xhs`（小红书）、`bilibili`（B站）、`kuaishou`（快手）。若不提供，将自动从链接中识别 |

## 执行方式

运行时通过 `scripts/run.py` 执行，内部自动完成 3 步异步工作流：

```bash
python3 scripts/run.py --params '{"link":"https://www.douyin.com/video/7381234567890123456"}'
```

## 环境变量

| 环境变量 | 说明 |
|----------|------|
| `AISKILLS_API_KEY` | API 密钥（必填），请运行 `export AISKILLS_API_KEY='your_api_key'` 配置 |

## 输出格式

输出遵循 **结论 -> 证据 -> 建议** 三段式结构。

```
## 多平台舆情分析结果

### 情感分析（正面）

| 正面 | 中性 | 负面 |
|------|------|------|
| 68% | 22% | 10% |

**高热词：** #春季穿搭 #平价好物 #学生党

### 转化潜力：78/100（高）

### 运营建议
- ...
```

详细格式规范见 [references/output-format.md](references/output-format.md)。
