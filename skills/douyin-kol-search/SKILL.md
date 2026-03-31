---
name: douyin-kol-search
description: "使用此技能在抖音平台搜索和筛选 KOL、达人、博主。用户想找/搜索/推荐/筛选某个领域的达人，或想找带货博主、带货达人、找合作达人进行商业合作时，使用此技能。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 https://ai-skills.ai 获取的 API Key，用于调用抖音 KOL 搜索数据接口。API Key 会随每次请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数如搜索关键词、达人分类等，不含用户对话上下文）"
    - "X-API-Key（认证密钥）"
  warning: "启用前请确认您信任 ai-skills.ai 的数据安全政策。建议使用可随时撤销的 API Key，并保留对 API 使用情况的监控可见性。"
---

# douyin-kol-search

## 概述

搜索抖音平台最具商业价值的 KOL，用于合作筛选和达人营销，对标账号。

## API

**执行技能** `POST /api/execute`

```bash
# 关键词搜索达人
curl -X POST https://ai-skills.ai/api/execute \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"skillId":"douyin-kol-search","params":{"keyword":"美妆"}}'

# 指定分类筛选
curl -X POST https://ai-skills.ai/api/execute \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $AISKILLS_API_KEY" \
  -H "X-Tenant-Id: default" \
  -d '{"skillId":"douyin-kol-search","params":{"keyword":"美食","category":"美食"}}'
```

## 参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `keyword` | string | **是** | 搜索关键词（达人名称/领域/内容标签） |
| `category` | string | 否 | 内容分类筛选 |

## 响应

```json
{
  "success": true,
  "data": {
    "users": [
      {
        "nickname": "达人昵称",
        "uid": "123456789",
        "followersCount": 5200000,
        "category": "美食",
        "awemeCount": 328,
        "followingCount": 120
      }
    ]
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

- **达人列表**：`users` → 表格列：达人昵称 | 粉丝数 | 内容分类 | 作品数 | 关注数
- 粉丝数超过 100 万显示为「X万」或「X百万」
- 按粉丝数从高到低排序
- 带货类达人在分类列标注「带货」
