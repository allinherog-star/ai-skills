---
name: douyin-realtime-hot-rise
description: "抖音上升热点选题助手适合内容创作者、运营、电商、营销在用户想知道接下来拍什么、写什么更可能有流量时使用，帮助基于输入材料生成上升热点列表、排名和变化趋势视图、可用于内容规划的选题线索。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key，用于运行导出的技能调用。"
---

# douyin-realtime-hot-rise 抖音上升热点选题助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

抖音上升热点选题助手用于回答「拍什么会有流量」、找上升选题、看赛道是否升温、辅助内容策划会，适合内容创作者、运营、电商、营销在明确业务目标、内容材料或分析对象后调用。
它会结合搜索词、搜索特定关键词的热点等输入，整理关键上下文，并输出上升热点列表、排名和变化趋势视图、可用于内容规划的选题线索，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户想知道接下来拍什么、写什么更可能有流量
- 用户想找正在上升的抖音热点或赛道机会
- 用户需要增长导向的选题参考

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

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
