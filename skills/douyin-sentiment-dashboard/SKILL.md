---
name: douyin-sentiment-dashboard
description: "分析抖音视频评论情绪、情感和整体口碑。当用户想了解评论是正面的还是负面的、分析评论区整体舆情、评估视频是否受欢迎，或提取评论洞察时，使用此技能。"
---

# douyin-sentiment-dashboard

## 概述

对抖音视频评论区进行 AI 情感分析，生成舆情洞察报告。

## 工作流（三步）

### Step 1 — 解析链接（公开，无需认证）

```bash
curl -X POST https://ai-skills.ai/api/comment-analysis/parse-link \
  -H "Content-Type: application/json" \
  -d '{"input":"https://v.douyin.com/xxxxx"}'
```

### Step 2 — 创建分析任务

```bash
curl -X POST https://ai-skills.ai/api/comment-analysis/tasks \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"platform":"douyin","contentId":"$CONTENT_ID"}'
# 返回: { "taskId": "xxxx", "status": "pending" }
```

### Step 3 — 轮询任务状态

```bash
curl https://ai-skills.ai/api/comment-analysis/tasks/$TASK_ID \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default"
# status=completed 时返回完整分析结果
```

## 一键脚本

```bash
#!/bin/bash
LINK="https://v.douyin.com/xxxxx"

# 1. 解析（公开接口）
CONTENT_ID=$(curl -s -X POST https://ai-skills.ai/api/comment-analysis/parse-link \
  -H "Content-Type: application/json" \
  -d "{\"input\":\"$LINK\"}" | jq -r '.data.contentId')

# 2. 创建任务
TASK=$(curl -s -X POST https://ai-skills.ai/api/comment-analysis/tasks \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d "{\"platform\":\"douyin\",\"contentId\":\"$CONTENT_ID\"}")
TASK_ID=$(echo $TASK | jq -r '.data.taskId')

# 3. 轮询直到完成
while true; do
  STATUS=$(curl -s https://ai-skills.ai/api/comment-analysis/tasks/$TASK_ID \
    -H "X-API-Key: $AISKILLS_API_KEY" \
    -H "X-Tenant-Id: default" | jq -r '.data.status')
  echo "Status: $STATUS"
  [ "$STATUS" = "completed" ] && break
  sleep 3
done

# 4. 获取结果
curl -s https://ai-skills.ai/api/comment-analysis/tasks/$TASK_ID \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" | jq '.data.result'
```

## 分析结果结构

```json
{
  "platform": "douyin",
  "contentId": "7321456789012345678",
  "videoTitle": "视频标题",
  "analyzeTime": "2026-03-28T12:00:00Z",
  "sentiment": {
    "positive": { "count": 120, "percentage": 60 },
    "neutral": { "count": 50, "percentage": 25 },
    "negative": { "count": 30, "percentage": 15 }
  },
  "keywords": ["产品好", "推荐", "物流快"],
  "topEmotions": [
    { "emotion": "满意", "count": 80 },
    { "emotion": "期待", "count": 40 }
  ],
  "insights": "评论区整体情感偏正面，用户对产品质量反馈积极..."
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
