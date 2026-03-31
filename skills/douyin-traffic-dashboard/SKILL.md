---
name: douyin-traffic-dashboard
description: "分析抖音各类内容的播放量占比与流量分布趋势。查询抖音内容分类播放数据、流量排名、赛道流量对比、流量大盘趋势时使用此技能。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 https://ai-skills.ai 获取的 API Key，用于调用抖音流量分布数据接口。API Key 会随每次请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数如分类、页码等，不含用户对话上下文）"
    - "X-API-Key（认证密钥）"
  warning: "启用前请确认您信任 ai-skills.ai 的数据安全政策。建议使用可随时撤销的 API Key，并保留对 API 使用情况的监控可见性。"
---

# douyin-traffic-dashboard

## 概述

获取抖音平台各内容分类的实时流量占比，用于分析流量分配趋势。

## API

**执行技能** `POST /api/execute`

```bash
curl -X POST https://ai-skills.ai/api/execute \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"skillId":"douyin-traffic-dashboard","params":{}}'
```

## 响应

```json
{
  "success": true,
  "data": {
    "categories": [
      {
        "label": "娱乐",
        "value": "2001,2002,2003",
        "hotCount": 42,
        "percentage": 28.5,
        "icon": "🎭",
        "group": "entertainment"
      }
    ],
    "total": 15,
    "timeRange": "抖音平台实时流量占比",
    "updateTime": "2026-03-28T12:00:00Z"
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

- **流量分布**：`categories` → 表格列：排名 | 分类（带图标） | 热度内容数 | 流量占比%
- 按 `percentage` 从高到低排序
- 附注更新时间（`updateTime`）
- 可额外绘制文本柱状图展示占比分布（如 `[██████░░░░] 28.5%`）
