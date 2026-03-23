---
name: bilibili-sentiment-dashboard
description: >
  B站评论舆情分析与up主运营建议。当用户提供B站视频/直播的链接，
  需要分析评论舆情、弹幕情感、用户反馈或up主运营建议时激活。
  即使用户只说"帮我看看B站这个视频的评论"或"分析下这个视频的弹幕"，
  也应激活此技能。
  Make the description "pushy" to avoid undertriggering.
compatibility: >
  Requires AISKILLS_BASE_URL, AISKILLS_API_KEY, AISKILLS_TENANT_ID environment variables.
  Uses comment-analysis-task: parse-link -> create-task -> poll get-task (platform fixed: bilibili).
---

# B站短视频怎么运营?

## Overview

B站短视频运营增长助手。当用户提供B站分享链接，需要分析视频评论、弹幕舆情、用户反馈或up主运营建议时，激活此技能。

该技能通过 3 步异步工作流（parse-link -> create-task -> get-task）调用后端 API，获取评论情感分析、弹幕密度分析、用户画像与up主运营建议。

## Invocation Mode

本技能使用 `comment-analysis-task` 异步工作流，包含以下三个步骤：

1. **parse-link** (`POST /api/v1/comment-analysis/parse-link`): 从分享链接中提取内容 ID 和标题（平台已固定为B站）
2. **create-task** (`POST /api/v1/comment-analysis/tasks`): 提交舆情分析任务，获取任务 ID
3. **get-task** (`GET /api/v1/comment-analysis/tasks/:id`): 轮询任务状态，直至完成（最多重试 60 次，间隔 2 秒）

## Parameters

See [references/form-schema.md](references/form-schema.md) for the full parameter schema.

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | B站分享链接，格式为 URI |

## Execution

运行时通过 `scripts/run.py` 执行，内部自动完成 3 步异步工作流：

```bash
python3 scripts/run.py --params '{"link":"https://www.bilibili.com/video/BV1xx411c7mD"}'
```

### 3 步异步工作流详解

#### Step 1: parse-link

```http
POST /api/v1/comment-analysis/parse-link
Content-Type: application/json

{
  "input": "<B站分享链接>",
  "platform": "bilibili"
}
```

响应示例：

```json
{
  "success": true,
  "data": {
    "platform": "bilibili",
    "contentId": "BV1xx411c7mD",
    "contentTitle": "视频标题",
    "sourceUrl": "https://www.bilibili.com/video/BV1xx411c7mD"
  }
}
```

#### Step 2: create-task

```http
POST /api/v1/comment-analysis/tasks
Content-Type: application/json

{
  "platform": "bilibili",
  "contentId": "BV1xx411c7mD",
  "contentTitle": "视频标题",
  "options": {
    "sourceUrl": "https://www.bilibili.com/video/BV1xx411c7mD"
  }
}
```

响应示例：

```json
{
  "success": true,
  "data": {
    "task": {
      "id": "task_abc123"
    }
  }
}
```

#### Step 3: get-task (轮询)

```http
GET /api/v1/comment-analysis/tasks/:id
```

轮询逻辑（内置于 `scripts/run.py`）：
- 每 2 秒轮询一次
- 最多重试 60 次
- 状态为 `completed` 或 `failed` 时停止轮询

必需的环境变量：

| 环境变量 | 说明 |
|----------|------|
| `AISKILLS_BASE_URL` | API 基础地址（默认：`https://ai-skills.ai`） |
| `AISKILLS_API_KEY` | API 密钥（必填） |
| `AISKILLS_TENANT_ID` | 租户 ID（默认：`default`） |

## Output Format

返回结果按照 **结论 -> 证据 -> 建议** 结构组织，详情见 [references/output-format.md](references/output-format.md)。

核心返回字段：

| 字段 | 说明 |
|------|------|
| `sentiment` | 情感分析：positive / negative / neutral 及正/负/中性评论比例 |
| `弹幕分析` | 弹幕密度、情感分布（仅B站特色） |
| `userProfile` | 用户画像：年龄段、性别分布、地域分布、高热词 |
| `conversionPotential` | 转化潜力评分（0-100），重点参考三连率、投币率 |
| `engagementMetrics` | 互动指标：点赞、评论、转发、弹幕密度 |
| `suggestions` | up主运营建议列表（聚焦B站特性：三连文化、弹幕互动、系列内容） |

## Examples

### Example 1: B站视频评论洞察

**Input:**
> 帮我看看这个B站视频的评论反响：https://www.bilibili.com/video/BV1xx411c7mD

**Output:**
```
结论：该视频用户反馈整体正面（正面评论占比 71%），弹幕活跃度高，社区氛围良好。

证据：
- 情感分析：正面 71%，中性 21%，负面 8%
- 弹幕密度：平均 120 条/分钟（同类均值 85 条）
- 评论峰值：视频 5:00-8:00（干货密集区）
- 转化潜力评分：82/100（高）

用户画像：
- 主要受众：18-30 岁男性（占比 65%）
- 高热词：#硬核 #干货 #涨知识 #三连
- 互动特点：投币率 12%，三连率 18%

建议：
1. 内容系列化：拆分为"入门篇/进阶篇/实战篇"
2. 视频中植入相关课程/工具推荐，引导转化
3. 建立粉丝群维护高质量用户关系
```

### Example 2: B站视频舆情偏负面

**Input:**
> 这个B站视频的弹幕好像有点不对劲，帮我分析下：https://b23.tv/xyz789

**Output:**
```
结论：该视频舆情偏中性（中性评论占比偏高），弹幕中"阴阳怪气"和"玩梗"较多，需结合语境解读。

证据：
- 情感分析：正面 38%，中性 48%，负面 14%
- 弹幕密度：平均 95 条/分钟（中等水平）
- 评论区高热词：#离谱 #就这？ #下次还来 #经典
- 转化潜力评分：55/100（中等）

用户画像：
- 主要受众：18-25 岁男性（占比 58%）
- 互动特点：弹幕互动强，评论相对沉默

建议：
1. B站用户习惯"弹幕互动"而非"评论互动"，重视弹幕节奏把控
2. 对弹幕中的质疑声音进行正向引导，可在视频中正面回应
3. 利用"经典/名场面"弹幕文化，制作系列视频提升用户粘性
```
