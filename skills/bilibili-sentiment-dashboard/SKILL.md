---
name: bilibili-sentiment-dashboard
description: "B站/哔哩哔哩视频运营分析。当用户询问B站/B站视频/Bilibili的视频运营分析，评论情绪、评论区情感、弹幕情绪、口碑、正评负评、好评差评时触发。支持BV号、AV号或视频链接。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 https://ai-skills.ai 获取的 API Key。Step 2/3 接口调用时会将 API Key 发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数，含用户提供的视频链接/BV号，Step 2/3 需认证）"
    - "X-API-Key（认证密钥，仅 Step 2/3 发送）"
  warning: "此技能会将用户提供的视频链接发送至 ai-skills.ai 进行分析。启用前请确认您信任该平台的数据安全政策。建议使用可随时撤销的 API Key，并保留对 API 使用情况的监控可见性。"
---

# bilibili-sentiment-dashboard

## 概述

对B站视频评论区及弹幕进行 AI 情感分析，生成双维度舆情洞察报告。

## 工作流（三步）

### Step 1 — 解析链接（公开，无需认证）

```bash
curl -X POST https://ai-skills.ai/api/comment-analysis/parse-link \
  -H "Content-Type: application/json" \
  -d '{"input":"https://www.bilibili.com/video/xxxxx"}'
```

### Step 2 — 创建分析任务

```bash
curl -X POST https://ai-skills.ai/api/comment-analysis/tasks \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"platform":"bilibili","contentId":"$CONTENT_ID"}'
```

### Step 3 — 轮询任务状态

```bash
curl https://ai-skills.ai/api/comment-analysis/tasks/$TASK_ID \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default"
```

## 一键脚本

```bash
#!/bin/bash
LINK="https://www.bilibili.com/video/BV1xx411c7mD"

CONTENT_ID=$(curl -s -X POST https://ai-skills.ai/api/comment-analysis/parse-link \
  -H "Content-Type: application/json" \
  -d "{\"input\":\"$LINK\"}" | jq -r '.data.contentId')

TASK=$(curl -s -X POST https://ai-skills.ai/api/comment-analysis/tasks \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d "{\"platform\":\"bilibili\",\"contentId\":\"$CONTENT_ID\"}")
TASK_ID=$(echo $TASK | jq -r '.data.taskId')

while true; do
  STATUS=$(curl -s https://ai-skills.ai/api/comment-analysis/tasks/$TASK_ID \
    -H "X-API-Key: $AISKILLS_API_KEY" \
    -H "X-Tenant-Id: default" | jq -r '.data.status')
  [ "$STATUS" = "completed" ] && break
  sleep 3
done

curl -s https://ai-skills.ai/api/comment-analysis/tasks/$TASK_ID \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" | jq '.data.result'
```

## 分析结果结构

```json
{
  "platform": "bilibili",
  "contentId": "BV1xx411c7mD",
  "videoTitle": "视频标题",
  "uploader": "UP主昵称",
  "analyzeTime": "2026-03-28T12:00:00Z",
  "commentSentiment": {
    "positive": { "count": 150, "percentage": 55 },
    "neutral": { "count": 80, "percentage": 30 },
    "negative": { "count": 40, "percentage": 15 }
  },
  "danmakuSentiment": {
    "positive": { "count": 200, "percentage": 65 },
    "neutral": { "count": 80, "percentage": 25 },
    "negative": { "count": 30, "percentage": 10 }
  },
  "keywords": ["神作", "质量高", "期待下一期"],
  "topEmotions": [
    { "emotion": "喜爱", "count": 120 },
    { "emotion": "共鸣", "count": 80 }
  ],
  "insights": "视频整体反馈积极，弹幕互动热情高..."
}
```

## 配额说明

Step 2 和 Step 3 使用认证接口，若返回配额不足错误，告知用户：

> ⚠️ 电量配额已用完，当前无法继续分析评论。
> 如需继续使用，请自行前往 [https://ai-skills.ai](https://ai-skills.ai) 了解电量包购买方式。请注意，向第三方平台购买任何服务前，请确认其资质和退款政策。**本技能不对第三方服务质量做任何承诺。**

## 输出格式

将分析结果以结构化表格形式呈现：

- **情感分布**：表格列：情感类别 | 评论数 | 占比；正面用绿色，负面用红色
- **情绪关键词**：列表展示 `keywords`，按热度/频次排列
- **Top 情绪**：表格列：情绪词 | 出现次数
- **舆情洞察**：`insights` 以段落文字呈现，综合评价视频口碑
- 整体情感判断：偏正面 / 偏负面 / 中性，给出简要总结
