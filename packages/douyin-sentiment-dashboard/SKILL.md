---
name: douyin-sentiment-dashboard
description: >
  抖音评论舆情分析与运营建议。当用户提供抖音视频/笔记/直播的链接，
  需要分析评论舆情、用户反馈、情感倾向或运营建议时激活。
  即使用户只说"帮我看看抖音这个视频的评论"或"分析下这个帖子"，
  也应激活此技能。
  Make the description "pushy" to avoid undertriggering.
compatibility: >
  Requires AISKILLS_BASE_URL, AISKILLS_API_KEY, AISKILLS_TENANT_ID environment variables.
  Uses comment-analysis-task: parse-link -> create-task -> poll get-task (platform fixed: douyin).
---

# 抖音短视频怎么运营?

## Overview

抖音短视频运营增长大盘。当用户提供抖音分享链接，需要分析评论舆情、用户画像、情感倾向或运营建议时，激活此技能。

该技能通过 3 步异步工作流（parse-link -> create-task -> get-task）调用后端 API，获取评论情感分析、用户画像、转化潜力评估与运营建议。

## Invocation Mode

本技能使用 `comment-analysis-task` 异步工作流，包含以下三个步骤：

1. **parse-link** (`POST /api/v1/comment-analysis/parse-link`): 从分享链接中提取内容 ID 和标题（平台已固定为抖音）
2. **create-task** (`POST /api/v1/comment-analysis/tasks`): 提交舆情分析任务，获取任务 ID
3. **get-task** (`GET /api/v1/comment-analysis/tasks/:id`): 轮询任务状态，直至完成（最多重试 60 次，间隔 2 秒）

## Parameters

See [references/form-schema.md](references/form-schema.md) for the full parameter schema.

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | 抖音分享链接，格式为 URI |

## Execution

运行时通过 `scripts/run.py` 执行，内部自动完成 3 步异步工作流：

```bash
python3 scripts/run.py --params '{"link":"https://www.douyin.com/video/7381234567890123456"}'
```

### 3 步异步工作流详解

#### Step 1: parse-link

```http
POST /api/v1/comment-analysis/parse-link
Content-Type: application/json

{
  "input": "<抖音分享链接>",
  "platform": "douyin"
}
```

响应示例：

```json
{
  "success": true,
  "data": {
    "platform": "douyin",
    "contentId": "7381234567890123456",
    "contentTitle": "视频标题",
    "sourceUrl": "https://www.douyin.com/video/7381234567890123456"
  }
}
```

#### Step 2: create-task

```http
POST /api/v1/comment-analysis/tasks
Content-Type: application/json

{
  "platform": "douyin",
  "contentId": "7381234567890123456",
  "contentTitle": "视频标题",
  "options": {
    "sourceUrl": "https://www.douyin.com/video/7381234567890123456"
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
| `userProfile` | 用户画像：年龄段、性别分布、地域分布、高热词 |
| `conversionPotential` | 转化潜力评分（0-100） |
| `engagementMetrics` | 互动指标：点赞、评论、转发、收藏量 |
| `suggestions` | 运营建议列表（聚焦抖音平台特性：算法推荐、短视频节奏、带货转化） |

## Examples

### Example 1: 抖音视频评论分析

**Input:**
> 帮我分析下这个抖音视频的评论：https://www.douyin.com/video/7381234567890123456

**Output:**
```
结论：该视频整体舆情偏正面（正面评论占比 68%），用户互动积极，但负面评论集中在视频后半段。

证据：
- 情感分析：正面 68%，中性 22%，负面 10%
- 评论峰值出现在视频 0-30 秒，正面情绪占比高达 75%
- 负面评论多在 2:15 处（涉及争议性话题）
- 转化潜力评分：78/100（中等偏高）

用户画像：
- 主要受众：18-25 岁女性（占比 62%）
- 高热词：#春季穿搭 #平价好物 #学生党
- 地域分布：广东（18%）、浙江（14%）、江苏（11%）

建议：
1. 视频后半段加入正向引导，降低负面情绪扩散风险
2. 结合"学生党平价好物"标签制作后续内容，延续热度
3. 在评论区置顶"学生党专属优惠"引导评论互动
```

### Example 2: 抖音短视频舆情（负面）

**Input:**
> 这个抖音视频的评论怎么都是负面的？https://v.douyin.com/xyz456

**Output:**
```
结论：该视频舆情偏负面（负面评论占比 52%），需要立即进行舆情引导。

证据：
- 情感分析：正面 28%，中性 20%，负面 52%
- 负面评论集中在：产品质量（38%）、物流速度（34%）、客服态度（28%）
- 转化潜力评分：35/100（低）

用户画像：
- 主要受众：25-35 岁女性（占比 65%）
- 高热词：#失望 #退货 #质量差 #物流慢

建议：
1. 立即发布公开声明回应负面关切，展示解决问题的态度
2. 为受影响用户提供补偿方案（退款/优惠券）
3. 在评论区置顶解决方案，降低后续负面扩散
```
