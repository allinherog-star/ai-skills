---
name: xhs-sentiment-dashboard
description: "小红书短视频运营增长助手. Use this skill when the user gives a Xiaohongshu link; the user wants to understand sentiment, profile, and next-step operations. Do not use when there is no link; the user wants a hot list."
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key。运行脚本时会随请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "params（技能参数，含用户提供的分享链接）"
    - "X-API-Key（认证密钥）"
  warning: "此技能会将用户提供的分享链接发送至 ai-skills.ai 进行解析和评论分析。启用前请确认您信任该平台的数据安全政策。"
---

# xhs-sentiment-dashboard 小红书短视频运营增长助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

小红书短视频运营增长助手

### 什么时候使用

**适用场景**

- the user gives a Xiaohongshu link
- the user wants to understand sentiment, profile, and next-step operations

**典型用户提问**

- 帮我分析这条小红书笔记的评论
- 看看用户画像和舆情风险
- 给我一些运营建议

**不要用于**

- there is no link
- the user wants a hot list
- the user wants creator collaboration candidates

**相邻技能选择**

- use `douyin-sentiment-dashboard` for Douyin links
- use `douyin-kol-search` for Douyin creator / benchmark-account requests

### 调用方式

运行脚本后会自动完成三步：解析分享链接、创建分析任务、轮询直到任务完成。

### 命令示例

**分析小红书内容评论**

```bash
python3 scripts/run.py --params '{"link":"https://www.xiaohongshu.com/explore/66f12345000000001c023abc"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `link` | string | 是 | - | 分享链接；需要传可访问的完整 URL |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

粘贴小红书分享链接或笔记 ID，以下格式都可以直接尝试：

- `https://www.xiaohongshu.com/explore/6789abcd1234567890abcdef`
- `https://xhslink.com/xxxxxx`
- `6789abcd1234567890abcdef`

### 示例请求

下面的示例参数直接传给 `scripts/run.py` 即可，脚本会自动完成解析链接、创建任务、轮询结果。

```bash
python3 scripts/run.py --params '{"link":"https://www.xiaohongshu.com/explore/66f12345000000001c023abc"}'
```

等价的 `--params` JSON：

```json
{
  "link": "https://www.xiaohongshu.com/explore/66f12345000000001c023abc"
}
```

### 返回结果示例

```json
{
  "success": true,
  "data": {
    "task": {
      "id": "task_demo_123",
      "platform": "xhs",
      "contentId": "7505866362912425270",
      "contentTitle": "小红书运营拆解示例",
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
          "platform": "xhs",
          "contentId": "7505866362912425270",
          "contentTitle": "小红书运营拆解示例",
          "analyzedAt": "2026-04-24T11:35:00.000Z"
        },
        "aiInsights": {
          "summary": "评论区更关注清单、价格、避坑点，说明种草内容更适合做模板化和合集化输出。",
          "sentiment": {
            "trend": "mixed",
            "label": "正向为主",
            "riskLevel": "low"
          },
          "operationAdvice": [
            {
              "category": "content",
              "priority": "P1",
              "title": "补充清单版",
              "detail": "把正文里的推荐项整理成清单模板，方便用户收藏和二次传播。",
              "reason": "高赞评论集中在“求清单”“求链接”，典型是种草型内容诉求。"
            }
          ]
        },
        "labeledComments": [
          {
            "id": "comment_1",
            "content": "求一个可直接照着买的清单，收藏了。",
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

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `xhs-sentiment-dashboard` 对应的 AI Skills API/工作流。
