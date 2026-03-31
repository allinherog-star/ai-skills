---
name: xhs-sentiment-dashboard
description: "使用此技能分析小红书笔记评论区的情感倾向和用户态度。提供情感分类、正负面评论占比、情绪关键词提取和舆情洞察。当用户发送小红书笔记链接或 note ID 并要求分析评论区时使用。此技能不提供笔记内容下载或抓取。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 https://ai-skills.ai 获取的 API Key。Step 2/3 接口调用时会将 API Key 发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数，含用户提供的笔记链接，Step 2/3 需认证）"
    - "X-API-Key（认证密钥，仅 Step 2/3 发送）"
  warning: "此技能会将用户提供的笔记链接发送至 ai-skills.ai 进行分析。启用前请确认您信任该平台的数据安全政策。建议使用可随时撤销的 API Key，并保留对 API 使用情况的监控可见性。"
---

# xhs-sentiment-dashboard

## 概述

对小红书笔记评论区进行 AI 情感分析，生成舆情洞察报告。

## 工作流（三步）

### Step 1 — 解析链接（公开，无需认证）

```bash
curl -X POST https://ai-skills.ai/api/comment-analysis/parse-link \
  -H "Content-Type: application/json" \
  -d '{"input":"https://www.xiaohongshu.com/explore/xxxxx"}'
```

### Step 2 — 创建分析任务

```bash
curl -X POST https://ai-skills.ai/api/comment-analysis/tasks \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"platform":"xhs","contentId":"$CONTENT_ID"}'
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
LINK="https://www.xiaohongshu.com/explore/xxxxx"

CONTENT_ID=$(curl -s -X POST https://ai-skills.ai/api/comment-analysis/parse-link \
  -H "Content-Type: application/json" \
  -d "{\"input\":\"$LINK\"}" | jq -r '.data.contentId')

TASK=$(curl -s -X POST https://ai-skills.ai/api/comment-analysis/tasks \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d "{\"platform\":\"xhs\",\"contentId\":\"$CONTENT_ID\"}")
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
  "platform": "xhs",
  "contentId": "64f1a66e0000000039005297",
  "noteTitle": "笔记标题",
  "analyzeTime": "2026-03-28T12:00:00Z",
  "sentiment": {
    "positive": { "count": 150, "percentage": 65 },
    "neutral": { "count": 50, "percentage": 22 },
    "negative": { "count": 30, "percentage": 13 }
  },
  "keywords": ["干货", "种草", "回购"],
  "topEmotions": [
    { "emotion": "喜欢", "count": 90 },
    { "emotion": "认可", "count": 60 }
  ],
  "insights": "用户反馈积极，主要集中在产品功效和使用体验..."
}
```

## 配额说明

Step 2 和 Step 3 使用认证接口，若返回配额不足错误，告知用户：

> ⚠️ 电量配额已用完，当前无法继续分析评论。
> 如需继续使用，请自行前往 [https://ai-skills.ai](https://ai-skills.ai) 了解电量包购买方式。请注意，向第三方平台购买任何服务前，请确认其资质和退款政策。**本技能不对第三方服务质量做任何承诺。**

## 输出格式

将分析结果以结构化表格形式呈现：

- **情感分布**：表格列：情感类别 | 评论数 | 占比；正面用绿色标识，负面用红色标识
- **情绪关键词**：列表展示 `keywords`，按热度/频次排列
- **Top 情绪**：表格列：情绪词 | 出现次数
- **舆情洞察**：`insights` 以段落文字呈现，综合评价笔记口碑
- 整体情感判断：偏正面 / 偏负面 / 中性，给出简要总结
