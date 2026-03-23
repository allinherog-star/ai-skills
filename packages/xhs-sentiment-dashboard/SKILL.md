---
name: xhs-sentiment-dashboard
description: >
  小红书评论舆情分析与运营建议。当用户提供小红书笔记/视频的链接，
  需要分析评论舆情、用户反馈、情感倾向或运营建议时激活。
  即使用户只说"帮我看看小红书这个笔记的评论"或"分析下这个帖子反响如何"，
  也应激活此技能。
  Make the description "pushy" to avoid undertriggering.
compatibility: >
  Requires AISKILLS_BASE_URL, AISKILLS_API_KEY, AISKILLS_TENANT_ID environment variables.
  Uses comment-analysis-task: parse-link -> create-task -> poll get-task (platform fixed: xhs).
---

# 小红书短视频怎么运营?

## Overview

小红书短视频运营增长助手。当用户提供小红书分享链接，需要分析笔记舆情、用户反馈、情感倾向或运营建议时，激活此技能。

该技能通过 3 步异步工作流（parse-link -> create-task -> get-task）调用后端 API，获取评论情感分析、用户画像、收藏率评估与运营建议。

## Invocation Mode

本技能使用 `comment-analysis-task` 异步工作流，包含以下三个步骤：

1. **parse-link** (`POST /api/v1/comment-analysis/parse-link`): 从分享链接中提取内容 ID 和标题（平台已固定为小红书）
2. **create-task** (`POST /api/v1/comment-analysis/tasks`): 提交舆情分析任务，获取任务 ID
3. **get-task** (`GET /api/v1/comment-analysis/tasks/:id`): 轮询任务状态，直至完成（最多重试 60 次，间隔 2 秒）

## Parameters

See [references/form-schema.md](references/form-schema.md) for the full parameter schema.

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | 小红书分享链接，格式为 URI |

## Execution

运行时通过 `scripts/run.py` 执行，内部自动完成 3 步异步工作流：

```bash
python3 scripts/run.py --params '{"link":"https://www.xiaohongshu.com/explore/67890abcdef"}'
```

### 3 步异步工作流详解

#### Step 1: parse-link

```http
POST /api/v1/comment-analysis/parse-link
Content-Type: application/json

{
  "input": "<小红书分享链接>",
  "platform": "xhs"
}
```

响应示例：

```json
{
  "success": true,
  "data": {
    "platform": "xhs",
    "contentId": "67890abcdef",
    "contentTitle": "笔记标题",
    "sourceUrl": "https://www.xiaohongshu.com/explore/67890abcdef"
  }
}
```

#### Step 2: create-task

```http
POST /api/v1/comment-analysis/tasks
Content-Type: application/json

{
  "platform": "xhs",
  "contentId": "67890abcdef",
  "contentTitle": "笔记标题",
  "options": {
    "sourceUrl": "https://www.xiaohongshu.com/explore/67890abcdef"
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
| `conversionPotential` | 转化潜力评分（0-100），重点参考收藏率 |
| `engagementMetrics` | 互动指标：点赞、评论、转发、收藏量 |
| `suggestions` | 运营建议列表（聚焦小红书特性：种草氛围、KOC互动、收藏引导） |

## Examples

### Example 1: 小红书笔记舆情分析

**Input:**
> 这是我小红书笔记的链接，想看看大家的反馈怎么样：https://www.xiaohongshu.com/explore/67890abcdef

**Output:**
```
结论：该笔记整体反响良好，正面情绪占主导（正面评论占比 74%），收藏率较高，用户认可度高。

证据：
- 情感分析：正面 74%，中性 19%，负面 7%
- 收藏率 15.3%（高于同类笔记均值 8.2%）
- 评论区高热词：#干货 #种草 #已入手
- 互动率：点赞 2.3w，收藏 8,600，评论 1,200

用户画像：
- 主要受众：25-35 岁都市女性（占比 71%）
- 兴趣标签：护肤、美妆、生活方式
- 地域分布：上海（22%）、北京（18%）、成都（12%）

建议：
1. 趁热度发布笔记 Part2，延续"种草清单"系列
2. 在评论区置顶"粉丝专属折扣码"提升转化
3. 私信高互动用户建立 KOC 关系链
```

### Example 2: 小红书笔记舆情偏负面

**Input:**
> 帮我看看这篇小红书笔记的评论，最近好像有点翻车：https://xhslink.com/abc123

**Output:**
```
结论：该笔记舆情偏负面（负面评论占比 48%），负面反馈集中在产品效果和价格两个方面。

证据：
- 情感分析：正面 32%，中性 20%，负面 48%
- 负面评论集中在：产品效果（42%）、价格偏高（35%）、发货速度（23%）
- 收藏率 6.1%（低于同类均值 8.2%）
- 转化潜力评分：40/100（有提升空间）

用户画像：
- 主要受众：20-30 岁女性（占比 68%）
- 高热词：#踩雷 #性价比 #等产品 #观望

建议：
1. 在评论区主动回应负面反馈，展示解决问题的诚意
2. 推出限时折扣或赠品活动，挽回价格敏感型用户
3. 私信高互动用户了解具体不满点，进行一对一沟通
```
