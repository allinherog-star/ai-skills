---
name: kuaishou-sentiment-dashboard
description: >
  快手评论舆情分析与运营建议。当用户提供快手视频/直播的链接，
  需要分析评论舆情、用户反馈、情感倾向或运营建议时激活。
  即使用户只说"帮我看看快手这个视频的评论"或"分析下这个直播的老铁反馈"，
  也应激活此技能。
  Make the description "pushy" to avoid undertriggering.
compatibility: >
  Requires AISKILLS_BASE_URL, AISKILLS_API_KEY, AISKILLS_TENANT_ID environment variables.
  Uses comment-analysis-task: parse-link -> create-task -> poll get-task (platform fixed: kuaishou).
---

# 快手短视频如何运营?

## Overview

快手短视频运营增长助手。当用户提供快手分享链接，需要分析视频/直播评论舆情、用户反馈、情感倾向或运营建议时，激活此技能。

该技能通过 3 步异步工作流（parse-link -> create-task -> get-task）调用后端 API，获取评论情感分析、用户画像、下沉市场特征与转化路径建议。

## Invocation Mode

本技能使用 `comment-analysis-task` 异步工作流，包含以下三个步骤：

1. **parse-link** (`POST /api/v1/comment-analysis/parse-link`): 从分享链接中提取内容 ID 和标题（平台已固定为快手）
2. **create-task** (`POST /api/v1/comment-analysis/tasks`): 提交舆情分析任务，获取任务 ID
3. **get-task** (`GET /api/v1/comment-analysis/tasks/:id`): 轮询任务状态，直至完成（最多重试 60 次，间隔 2 秒）

## Parameters

See [references/form-schema.md](references/form-schema.md) for the full parameter schema.

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | 快手分享链接，格式为 URI |

## Execution

运行时通过 `scripts/run.py` 执行，内部自动完成 3 步异步工作流：

```bash
python3 scripts/run.py --params '{"link":"https://www.kuaishou.com/video/3x4c7e9f2g1h"}'
```

### 3 步异步工作流详解

#### Step 1: parse-link

```http
POST /api/v1/comment-analysis/parse-link
Content-Type: application/json

{
  "input": "<快手分享链接>",
  "platform": "kuaishou"
}
```

响应示例：

```json
{
  "success": true,
  "data": {
    "platform": "kuaishou",
    "contentId": "3x4c7e9f2g1h",
    "contentTitle": "视频标题",
    "sourceUrl": "https://www.kuaishou.com/video/3x4c7e9f2g1h"
  }
}
```

#### Step 2: create-task

```http
POST /api/v1/comment-analysis/tasks
Content-Type: application/json

{
  "platform": "kuaishou",
  "contentId": "3x4c7e9f2g1h",
  "contentTitle": "视频标题",
  "options": {
    "sourceUrl": "https://www.kuaishou.com/video/3x4c7e9f2g1h"
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
| `userProfile` | 用户画像：年龄段、性别分布、地域分布、高热词（聚焦下沉市场） |
| `conversionPotential` | 转化潜力评分（0-100），重点参考快手老铁购买意向 |
| `engagementMetrics` | 互动指标：点赞、评论、转发、关注量 |
| `suggestions` | 运营建议列表（聚焦快手特性：老铁文化、下沉市场、私域转化） |

## Examples

### Example 1: 快手视频评论分析

**Input:**
> 这是我快手视频的链接，帮我分析下评论：https://www.kuaishou.com/video/3x4c7e9f2g1h

**Output:**
```
结论：该视频评论以正面为主（正面占比 62%），但负面反馈需关注，互动率整体中等。

证据：
- 情感分析：正面 62%，中性 24%，负面 14%
- 负面评论集中在"价格偏高"和"物流速度"方面
- 转化潜力评分：65/100（有提升空间）

用户画像：
- 主要受众：25-45 岁下沉市场用户（占比 78%）
- 价格敏感度：高
- 地域分布：山东（19%）、河南（17%）、河北（15%）

建议：
1. 针对负面反馈（价格/物流）在评论区公开回应，展示服务态度
2. 推出限时优惠券或满减活动，提升下单转化率
3. 与粉丝建立更紧密互动（如直播连麦、粉丝见面会）
```

### Example 2: 快手直播舆情分析

**Input:**
> 帮我看看这次快手直播的老铁们都说了什么：https://v.kuaishou.com/直播链接

**Output:**
```
结论：本次直播整体舆情偏正面（正面占比 71%），老铁互动积极，但中后期节奏下滑。

证据：
- 情感分析：正面 71%，中性 19%，负面 10%
- 直播峰值在线人数 3.2 万，平均在线 1.8 万
- 老铁评论高热词：#老铁666 #下单了 #快点上 #支持
- 转化潜力评分：75/100（较高）

用户画像：
- 主要受众：25-40 岁下沉市场用户（占比 82%）
- 价格敏感度：高（偏好性价比产品）
- 地域分布：河北（21%）、山东（18%）、河南（15%）

建议：
1. 直播后半段保持互动节奏，避免老铁流失
2. 推出"老铁专属价"强化情感连接，提升下单率
3. 直播后发布切片视频，延续热度并引流至下次直播
```
