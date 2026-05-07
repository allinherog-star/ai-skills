---
name: douyin-sentiment-dashboard
description: "抖音短视频运营增长大盘. Use this skill when the user gives a Douyin link; the user wants comment sentiment / profile / public opinion / operational insight; the user wants to review a published content asset. Do not use when there is no concrete content link; the user wants hot topics."
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网获取的 API Key。运行脚本时会随请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "params（技能参数，含用户提供的分享链接）"
    - "X-API-Key（认证密钥）"
  warning: "此技能会将用户提供的分享链接发送至 ai-skills.ai 进行解析和评论分析。启用前请确认您信任该平台的数据安全政策。"
---

# douyin-sentiment-dashboard 抖音短视频运营增长大盘

官网入口：<https://ai-skills.ai>

### 概述

抖音短视频运营增长大盘

### 什么时候使用

**适用场景**

- the user gives a Douyin link
- the user wants comment sentiment / profile / public opinion / operational insight
- the user wants to review a published content asset

**典型用户提问**

- 帮我分析这条抖音视频的评论区
- 看看这条视频的舆情和用户画像
- 给我一些运营建议和回复思路

**不要用于**

- there is no concrete content link
- the user wants hot topics
- the user wants creators or benchmark accounts

**相邻技能选择**

- use `xhs-sentiment-dashboard` for Xiaohongshu links
- use `douyin-realtime-hot-rise` when the user wants new topics, not comment diagnosis

### 调用方式

运行脚本后会自动完成三步：解析分享链接、创建分析任务、轮询直到任务完成。

### 命令示例

**分析抖音视频评论**

```bash
python3 scripts/run.py --params '{"link":"https://v.douyin.com/xxxxx"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `link` | string | 是 | - | 分享链接；需要传可访问的完整 URL |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

粘贴抖音分享链接或视频 ID，以下格式都可以直接尝试：

- `https://www.douyin.com/video/7462574818594200872`
- `https://v.douyin.com/iNsVxxx/`
- `7462574818594200872`

### 示例请求

下面的示例参数直接传给 `scripts/run.py` 即可，脚本会自动完成解析链接、创建任务、轮询结果。

```bash
python3 scripts/run.py --params '{"link":"https://v.douyin.com/xxxxx"}'
```

等价的 `--params` JSON：

```json
{
  "link": "https://v.douyin.com/xxxxx"
}
```

### 返回结果示例

```json
{
  "success": true,
  "data": {
    "task": {
      "id": "task_demo_123",
      "platform": "douyin",
      "contentId": "7505866362912425270",
      "contentTitle": "抖音运营拆解示例",
      "status": "completed",
      "progress": 100,
      "progressMessage": "分析完成",
      "result": {
        "summary": {
          "analyzedComments": 168,
          "timeRange": {
            "start": "2026-04-23T00:00:00.000Z",
            "end": "2026-04-24T00:00:00.000Z"
          },
          "platform": "douyin",
          "contentId": "7505866362912425270",
          "contentTitle": "抖音运营拆解示例",
          "analyzedAt": "2026-04-24T11:35:00.000Z"
        },
        "aiInsights": {
          "summary": "评论区主要在追问选题拆解、发布时间和账号定位，适合继续做系列内容。",
          "sentiment": {
            "trend": "mixed",
            "label": "正向为主",
            "riskLevel": "low"
          },
          "operationAdvice": [
            {
              "category": "content",
              "priority": "P1",
              "title": "继续做系列",
              "detail": "围绕这条内容延展 3 个具体场景，继续承接评论区追问。",
              "reason": "高频评论集中在“下一条怎么做”，说明用户有连续追更意愿。"
            }
          ]
        },
        "labeledComments": [
          {
            "id": "comment_1",
            "content": "讲得很清楚，想看你下一条怎么实操。",
            "sentiment": "positive",
            "likes": 26
          }
        ]
      }
    }
  }
}
```

### 结果重点看什么

- `task.status`：任务状态，`completed` 表示已经拿到完整分析结果。
- `task.result.summary`：评论样本量、分析时间范围、内容标题等基础信息。
- `task.result.aiInsights.summary`：对评论区的一句话总结，适合快速判断内容口碑和运营方向。
- `task.result.aiInsights.operationAdvice`：最值得优先执行的运营建议，建议先看 `priority` 和 `detail`。
- `task.result.labeledComments`：带标签的原始评论样本，可用来回看用户真实反馈。

### 运行前准备

- `AISKILLS_BASE_URL`：默认使用 AI Skills 官方服务
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `douyin-sentiment-dashboard` 对应的 AI Skills API/工作流。
