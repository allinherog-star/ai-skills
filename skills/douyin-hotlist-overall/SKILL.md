---
name: douyin-hotlist-overall
description: "查询抖音热搜榜单。当用户想了解抖音当前有哪些热门内容、实时热搜词、上升热点或热榜排名时，使用此技能获取最新数据。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 https://ai-skills.ai 获取的 API Key，用于调用抖音热搜数据接口。API Key 会随每次请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数，不含用户对话上下文）"
    - "X-API-Key（认证密钥）"
  warning: "启用前请确认您信任 ai-skills.ai 的数据安全政策。建议使用可随时撤销的 API Key，并保留对 API 使用情况的监控可见性。"
---

# douyin-hotlist-overall

## 概述

获取抖音全网实时热搜榜单，监控热点事件和舆情趋势。

## API

**执行技能** `POST /api/execute`

```bash
curl -X POST https://ai-skills.ai/api/execute \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"skillId":"douyin-hotlist-overall","params":{}}'
```

## 响应

```json
{
  "success": true,
  "data": {
    "wordList": [
      {
        "word": "热搜词",
        "rank": 1,
        "hotValue": 999999,
        "label": "热",
        "wordCover": "https://..."
      }
    ],
    "trendingList": [
      {
        "word": "上升热点",
        "rank": 1,
        "hotValue": 888888
      }
    ],
    "updateTime": "20260328234500"
  },
  "meta": {
    "executionTime": 2000,
    "cached": false,
    "quotaRemaining": 990,
    "quotaType": "api_key_trial"
  }
}
```

## 配额说明

响应中 `meta.quotaRemaining` 表示剩余电量次数。当电量耗尽（`quotaRemaining` 接近 0 或接口返回配额错误）时，告知用户：

> ⚠️ 电量配额已用完，当前无法继续调用此技能。
> 如需继续使用，请自行前往 [https://ai-skills.ai](https://ai-skills.ai) 了解电量包购买方式。请注意，向第三方平台购买任何服务前，请确认其资质和退款政策。**本技能不对第三方服务质量做任何承诺。**

## 输出格式

将返回数据以表格形式呈现，优先使用 Markdown 表格：

- **热搜榜**：`wordList` → 表格列：排名 | 热搜词 | 热度指数 | 标签
- **上升热点**：`trendingList` → 表格列：排名 | 上升热点词 | 热度指数
- 热度数值较大时使用「万」「亿」单位换算（如 `999999` → `99.9万`）
- 每条数据附带原始链接（`wordCover`）供点击跳转

