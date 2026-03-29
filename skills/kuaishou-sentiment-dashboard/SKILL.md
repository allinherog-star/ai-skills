---
name: kuaishou-sentiment-dashboard
description: "快手视频评论情感分析。分析快手评论区是正评多还是负评多，观众对视频的态度是喜欢还是讨厌，整体口碑和舆情如何。提供情感倾向、正负面比例、情绪关键词和受众洞察。"
---

# kuaishou-sentiment-dashboard

## 概述

对快手短视频评论区进行 AI 情感分析，生成舆情洞察报告。

## 工作流（三步）

### Step 1 — 解析链接（公开，无需认证）

```bash
curl -X POST https://ai-skills.ai/api/comment-analysis/parse-link \
  -H "Content-Type: application/json" \
  -d '{"input":"https://v.kuaishou.com/xxxxx"}'
```

### Step 2 — 创建分析任务

```bash
curl -X POST https://ai-skills.ai/api/comment-analysis/tasks \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"platform":"kuaishou","contentId":"$CONTENT_ID"}'
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
LINK="https://v.kuaishou.com/xxxxx"

CONTENT_ID=$(curl -s -X POST https://ai-skills.ai/api/comment-analysis/parse-link \
  -H "Content-Type: application/json" \
  -d "{\"input\":\"$LINK\"}" | jq -r '.data.contentId')

TASK=$(curl -s -X POST https://ai-skills.ai/api/comment-analysis/tasks \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d "{\"platform\":\"kuaishou\",\"contentId\":\"$CONTENT_ID\"}")
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
  "platform": "kuaishou",
  "contentId": "3xqh7w8f9v2",
  "videoTitle": "视频标题",
  "analyzeTime": "2026-03-28T12:00:00Z",
  "sentiment": {
    "positive": { "count": 120, "percentage": 60 },
    "neutral": { "count": 50, "percentage": 25 },
    "negative": { "count": 30, "percentage": 15 }
  },
  "keywords": ["接地气", "真实", "支持"],
  "topEmotions": [
    { "emotion": "认可", "count": 70 },
    { "emotion": "喜爱", "count": 50 }
  ],
  "insights": "评论区整体情感偏正面，用户对内容真实感认可度高..."
}
```

## 配额说明

Step 2 和 Step 3 使用认证接口，若返回配额不足错误，告知用户：

> ⚠️ 电量配额已用完，当前无法继续分析评论。
> 请前往 [https://ai-skills.ai](https://ai-skills.ai) 购买电量包，充值后即可继续使用。

## 输出格式

将分析结果以结构化表格形式呈现：

- **情感分布**：表格列：情感类别 | 评论数 | 占比；正面用绿色标识，负面用红色标识
- **情绪关键词**：列表展示 `keywords`，按热度/频次排列
- **Top 情绪**：表格列：情绪词 | 出现次数
- **舆情洞察**：`insights` 以段落文字呈现，综合评价视频口碑
- 整体情感判断：偏正面 / 偏负面 / 中性，给出简要总结
