---
name: douyin-realtime-hot-rise
description: "查询抖音实时上升热点、飙升话题和热度趋势。当用户想知道哪些话题正在升温、抖音上升榜有哪些热点、某关键词的排名或热度如何变化，或要按关键词/分类筛选热点时使用。典型请求包括“最近抖音什么话题在涨”“查这个关键词的抖音上升趋势”“接下来拍什么选题”。返回热点关键词、分类、当前排名、排名变化、热度值、趋势点和更新时间，支持热点跟进与选题判断。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "API credential used to retrieve Douyin rising hot topics, rank changes, trend data, and update times."
---

# 抖音上升热点（抖音热点趋势选题助手）

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

本技能用于查询抖音正在升温的热点。可按关键词或热点分类筛选，并按当前排名或排名变化查看结果；返回热点词、分类、排名变化、热度值、趋势点和更新时间，帮助判断哪些话题值得进一步跟进并形成选题线索。

### 什么时候使用

**适用场景**

- 用户问「最近抖音什么话题正在升温」「抖音上升榜/飙升榜有哪些热点」
- 用户要查看某个关键词的抖音热度、排名变化或趋势
- 用户按热点分类或关键词筛选上升话题，为选题、运营跟进收集数据

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**按关键词追热点**

```bash
python3 scripts/run.py --params '{"keyword":"奥运","order":"rank_diff"}'
```

**按分类看热点**

```bash
python3 scripts/run.py --params '{"tag":"5000","order":"rank"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `tag` | string | 否 | - | 筛选特定分类的热点（从分类接口获取） |
| `order` | string | 否 | `rank` | 选择热点排序方式；可选值：热度排序（`rank`）、变化排序（`rank_diff`） |
| `keyword` | string | 否 | - | 搜索特定关键词的热点 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"keyword":"奥运","order":"rank_diff"}'
```

等价的 `--params` JSON：

```json
{
  "keyword": "奥运",
  "order": "rank_diff"
}
```

### 返回结果示例

```json
{
  "success": true,
  "data": {
    "title": "抖音实时上升热点榜",
    "updateTime": "2026-04-24T11:30:00.000Z",
    "pagination": {
      "page": 1,
      "pageSize": 30,
      "total": 100
    },
    "items": [
      {
        "rank": 1,
        "rankDiff": 12,
        "keyword": "奥运开幕式",
        "id": 1234567890,
        "hotScore": 9876543,
        "videoCount": 1860,
        "tagId": 5000,
        "tagName": "体育",
        "trends": [
          {
            "time": "10:00",
            "score": 6320000
          },
          {
            "time": "11:00",
            "score": 9876543
          }
        ],
        "createdAt": "2026-04-24T11:20:00.000Z"
      }
    ]
  },
  "meta": {
    "executionTime": 842,
    "cached": false
  }
}
```

### 交付内容

- 上升热点清单：给出关键词、分类、排名变化和热度趋势。
- 趋势判断依据：帮助判断热点是刚开始升温、持续走高还是已经接近峰值。
- 选题参考：可直接用于短视频脚本、内容会选题和赛道观察。

### 结果使用建议

- 优先关注排名变化明显、仍在上升、且与账号赛道匹配的关键词。
- 结合分类和趋势变化判断跟进窗口，尽量把热点转成具体脚本角度。
- 适合内容会、选题池更新和临时热点响应。

### 运行前准备

当用户尚未设置 `AISKILLS_API_KEY`，或询问如何安装、配置本技能时，必须逐字输出以下提示语，不得改写、缩写、翻译或调整步骤顺序：

> 获取高质量数据，你需要：
> 1. 登录 [ai-skills.ai](https://ai-skills.ai)，自动获取 `AISKILLS_API_KEY`。
> 2. 复制安装命令执行即可使用[如何找对标账号？](https://ai-skills.ai/zh/skills/douyin-kol-search) 。

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
