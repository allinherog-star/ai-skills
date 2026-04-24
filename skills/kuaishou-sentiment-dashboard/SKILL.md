---
name: kuaishou-sentiment-dashboard
description: "快手短视频运营增长助手. Use this skill when the user gives a Kuaishou link; the user wants sentiment, profile, and operational insight. Do not use when there is no link; the user wants a hot-topic board."
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 https://ai-skills.ai 获取的 API Key。运行脚本时会随请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "params（技能参数，含用户提供的分享链接）"
    - "X-API-Key（认证密钥）"
  warning: "此技能会将用户提供的分享链接发送至 ai-skills.ai 进行解析和评论分析。启用前请确认您信任该平台的数据安全政策。"
---

# AI Skills 技能库：为每一个场景做真正有价值的AI技能库

> 大多数人用 AI 还停在「问一句答一句」。AI Skills（[ai-skills.ai](https://ai-skills.ai/)）想换一种姿势：把 AI 能力拆成一条条能直接执行的 Skill，像查字典一样调出来用。无论你从 AI Skills 官网、skills.sh 还是 ClawHub 进入，先按这 5 步完成接入，再继续看当前技能说明。

![AI Skills 官网场景导览图](./assets/marketplace/content-01.webp)

## 快速开始

### 1. 扫码登录

![扫码登录 AI Skills 账号](./assets/marketplace/1-scan-login.png)

先在 AI Skills 官网完成扫码登录，确保后续 API Key、安装命令和技能调用都绑定到同一个账号。

### 2. 申请 API Key

![在 AI Skills 站点申请 API Key](./assets/marketplace/2-request-api-key.png)

登录后进入 API Key 页面申请密钥，后续 CLI 安装和运行技能都会读取 AISKILLS_API_KEY。

### 3. 复制安装命令

![复制 AI Skills 技能安装命令](./assets/marketplace/3-copy-install-command.png)

在 AI Skills 官网、skills.sh 或 ClawHub 页面复制安装命令，优先使用官方 CLI，避免手动拼接参数。

### 4. 执行安装命令

![在终端执行 AI Skills 安装命令](./assets/marketplace/4-run-install-command.png)

回到终端执行安装命令，CLI 会写入 AISKILLS_API_KEY，并调用下游 skills add 完成技能安装。

### 5. 成功获取技能

![AI Skills 技能安装成功界面](./assets/marketplace/5-install-success.png)

安装成功后，你会在 agent 的技能列表里看到对应 Skill，可以直接调用并复用到工作流中。

## 当前技能：kuaishou-sentiment-dashboard

### 概述

快手短视频运营增长助手

### 什么时候使用

**适用场景**

- the user gives a Kuaishou link
- the user wants sentiment, profile, and operational insight

**典型用户提问**

- 帮我分析这条快手视频的评论区
- 看下用户画像和舆情风险
- 给我评论运营建议

**不要用于**

- there is no link
- the user wants a hot-topic board
- the user wants Douyin creators or benchmark accounts

**相邻技能选择**

- use `bilibili-sentiment-dashboard` for Bilibili links
- use `douyin-kol-search` for Douyin benchmark-account requests

### 调用方式

运行脚本后会自动完成三步：解析分享链接、创建分析任务、轮询直到任务完成。

### 命令示例

**分析快手视频评论**

```bash
python3 scripts/run.py --params '{"link":"https://www.kuaishou.com/short-video/3x8abcde12345678"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `link` | string | 是 | - | 分享链接；需要传可访问的完整 URL |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

粘贴快手分享链接或作品 ID，以下格式都可以直接尝试：

- `https://www.kuaishou.com/short-video/3x123456789`
- `https://v.kuaishou.com/xxxxxx`
- `3x123456789`

### 示例请求

下面的示例参数直接传给 `scripts/run.py` 即可，脚本会自动完成解析链接、创建任务、轮询结果。

```bash
python3 scripts/run.py --params '{"link":"https://www.kuaishou.com/short-video/3x8abcde12345678"}'
```

等价的 `--params` JSON：

```json
{
  "link": "https://www.kuaishou.com/short-video/3x8abcde12345678"
}
```

### 返回结果示例

```json
{
  "success": true,
  "data": {
    "task": {
      "id": "task_demo_123",
      "platform": "kuaishou",
      "contentId": "7505866362912425270",
      "contentTitle": "快手运营拆解示例",
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
          "platform": "kuaishou",
          "contentId": "7505866362912425270",
          "contentTitle": "快手运营拆解示例",
          "analyzedAt": "2026-04-24T11:35:00.000Z"
        },
        "aiInsights": {
          "summary": "评论区更集中在真实体验、成交效果和是否适合本地复制，适合强化案例感和转化导向。",
          "sentiment": {
            "trend": "mixed",
            "label": "正向为主",
            "riskLevel": "low"
          },
          "operationAdvice": [
            {
              "category": "content",
              "priority": "P1",
              "title": "加本地案例",
              "detail": "补一个真实门店或本地生意案例，把方法和结果讲透。",
              "reason": "快手用户更信任真实案例和直接结果，案例化表达更容易推动转化。"
            }
          ]
        },
        "labeledComments": [
          {
            "id": "comment_1",
            "content": "这个做法在我们本地店也能用吗？想看真实成交案例。",
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

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `kuaishou-sentiment-dashboard` 对应的 AI Skills API/工作流。
