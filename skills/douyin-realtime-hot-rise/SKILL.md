---
name: douyin-realtime-hot-rise
description: '当用户在抖音上寻找正在走红的视频、涨粉最快的话题、实时飙升榜单、新晋爆款内容，或想了解"哪些视频在抖音火起来了"、"最近抖音流行什么"时，使用此技能。此技能专用于抖音内容热度上升趋势分析，不适用于微博热搜、快手热点、达人搜索、视频播放量统计或情感分析等其他场景。'
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 https://ai-skills.ai 获取的 API Key，用于调用抖音飙升榜单数据接口。API Key 会随每次请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数如关键词、分类、页码等，不含用户对话上下文）"
    - "X-API-Key（认证密钥）"
  warning: "启用前请确认您信任 ai-skills.ai 的数据安全政策。建议使用可随时撤销的 API Key，并保留对 API 使用情况的监控可见性。"
---

# douyin-realtime-hot-rise

## 概述

获取抖音实时热搜飙升榜单，用于热点选题和内容创作参考。

## API

**执行技能** `POST /api/execute`

```bash
# 完整热搜飙升榜（热度排序）
curl -X POST https://ai-skills.ai/api/execute \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"skillId":"douyin-realtime-hot-rise","params":{}}'

# 关键词搜索（筛选包含"奥运"的热点）
curl -X POST https://ai-skills.ai/api/execute \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"skillId":"douyin-realtime-hot-rise","params":{"keyword":"奥运"}}'

# 指定分类 + 变化排序
curl -X POST https://ai-skills.ai/api/execute \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"skillId":"douyin-realtime-hot-rise","params":{"tag":"2001,2002","order":"rank_diff","page_size":20}}'
```

## 参数

| 参数 | 类型 | 默认 | 说明 |
|------|------|------|------|
| `keyword` | string | - | 关键词模糊搜索 |
| `tag` | string | - | 分类ID，多个逗号分隔 |
| `order` | string | `rank` | `rank`=热度排序，`rank_diff`=变化排序 |
| `page` | integer | `1` | 页码 |
| `page_size` | integer | `50` | 每页数量 |

## 分类 tag

| 分类 | tag |
|------|-----|
| 娱乐 | `2001,2002,2003,2004,2005,2006,2007,2008,2012` |
| 游戏 | `12000,12001` |
| 美食 | `9000` |
| 科技 | `6000` |
| 体育 | `5000` |
| 社会 | `4003,4005` |
| 时尚 | `16000` |
| 音乐 | `29000,29001` |

## 响应

```json
{
  "success": true,
  "data": {
    "title": "抖音全网实时热点上升榜",
    "updateTime": "20260328234500",
    "pagination": { "page": 1, "pageSize": 30, "total": 4018 },
    "items": [
      {
        "rank": 53,
        "rankDiff": 3889,
        "keyword": "一起野个好身材",
        "hotScore": 6880738,
        "tagName": "话题互动"
      }
    ]
  },
  "meta": {
    "executionTime": 3743,
    "cached": false,
    "quotaRemaining": 994,
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

- **飙升榜**：`items` → 表格列：当前排名 | 排名变化(↑↓) | 热搜词/话题 | 热度指数 | 分类标签
- `rankDiff` 为正数显示「↑数值」，为负数显示「↓数值」
- 热度数值较大时使用「万」「亿」单位换算
- `rankDiff` 变化幅度大的热点用 🔥 或 ⚡ 标注
