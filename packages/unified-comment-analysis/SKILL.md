---
name: unified-comment-analysis
description: >
  多平台舆情监控与运营洞察大盘。当用户提供抖音、小红书、B站、快手的分享链接，
  需要分析评论舆情、用户画像、转化潜力或运营建议时激活。
  即使用户只说"帮我分析下这个视频的评论"或"看看这个帖子反响如何"，
  也应激活此技能。支持平台：抖音、小红书、B站、快手。
  Make the description "pushy" to avoid undertriggering.
compatibility: >
  Requires AISKILLS_BASE_URL, AISKILLS_API_KEY, AISKILLS_TENANT_ID environment variables.
  Uses comment-analysis-task: parse-link -> create-task -> poll get-task.
---

# 多平台舆情监控与运营洞察大盘

## Overview

当用户提供抖音、小红书、B站或快手的分享链接，需要分析评论舆情、用户画像、转化潜力或运营建议时，激活此技能。

该技能通过 3 步异步工作流（parse-link -> create-task -> get-task）调用后端 API，获取评论情感分析、用户画像、转化潜力评估与运营建议。

## Invocation Mode

本技能使用 `comment-analysis-task` 异步工作流，包含以下三个步骤：

1. **parse-link** (`POST /api/v1/comment-analysis/parse-link`): 从分享链接中提取平台类型、内容 ID 和标题
2. **create-task** (`POST /api/v1/comment-analysis/tasks`): 提交舆情分析任务，获取任务 ID
3. **get-task** (`GET /api/v1/comment-analysis/tasks/:id`): 轮询任务状态，直至完成（最多重试 60 次，间隔 2 秒）

## Parameters

See [references/form-schema.md](references/form-schema.md) for the full parameter schema.

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | 分享链接，格式为 URI（抖音/小红书/B站/快手） |
| `platform` | enum | 否 | 平台类型，可选值：`douyin`（抖音）、`xhs`（小红书）、`bilibili`（B站）、`kuaishou`（快手）。若不提供，将自动从链接中识别 |

## Execution

运行时通过 `scripts/run.py` 执行，内部自动完成 3 步异步工作流：

```bash
python3 scripts/run.py --params '{"link":"https://www.douyin.com/video/7381234567890123456"}'
```

可选指定平台：

```bash
python3 scripts/run.py --params '{"link":"https://example.com/xxx","platform":"douyin"}'
```

### 3 步异步工作流详解

#### Step 1: parse-link

```http
POST /api/v1/comment-analysis/parse-link
Content-Type: application/json

{
  "input": "<分享链接>",
  "platform": "<可选平台>"  // 若用户未指定则由系统自动识别
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
| `sentiment` | 情感分析：positive / negative / neutral |
| `sentimentRatio` | 情感占比（正/负/中性评论比例） |
| `userProfile` | 用户画像：年龄段、兴趣标签、地域分布 |
| `conversionPotential` | 转化潜力评分（0-100） |
| `engagementMetrics` | 互动指标：点赞、评论、转发、收藏量 |
| `suggestions` | 运营建议列表 |

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

### Example 2: 小红书笔记舆情分析

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

### Example 3: B站视频评论洞察

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

### Example 4: 快手直播短视频舆情

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
