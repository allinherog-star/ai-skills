---
name: douyin-realtime-hot-rise
description: "抖音上升热点选题助手. Use this skill when the user asks what to post next; the user asks which topics are rising; the user wants growth-oriented topic selection. Do not use when the user wants the absolute hottest list right now; the user wants benchmark accounts or creators."
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key。运行脚本时会随请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数，不含用户对话上下文）"
    - "X-API-Key（认证密钥）"
  warning: "此技能会调用 AI Skills API。启用前请确认您信任 ai-skills.ai 的数据安全政策，并使用可随时撤销的 API Key。"
---

# douyin-realtime-hot-rise 抖音上升热点选题助手

快速开始：<https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B>
更多技能：<https://ai-skills.ai>

### 概述

抖音上升热点选题助手

### 什么时候使用

**适用场景**

- the user asks what to post next
- the user asks which topics are rising
- the user wants growth-oriented topic selection

**典型用户提问**

- 最近拍什么会有流量？
- 这周抖音有什么正在上升的热点？
- 我做母婴 / 美妆 / 职场，最近该跟哪些选题？

**不要用于**

- the user wants the absolute hottest list right now
- the user wants benchmark accounts or creators
- the user wants comment analysis

**相邻技能选择**

- use `douyin-hotlist-overall` for "what is hottest right now"
- use `douyin-traffic-dashboard` for "where traffic is flowing"

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
| `order` | string | 否 | `rank` | 排序方式；可选值：热度排序（`rank`）、变化排序（`rank_diff`） |
| `tag` | string | 否 | - | 热点分类 tag，传入数字 id 或逗号分隔的 id 组合。运行时以最新分类接口为准，当前默认映射可参考 x-direction-map；分类映射见下方「`tag` 取值参考」 |
| `keyword` | string | 否 | - | 搜索词 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

#### `tag`

字段说明：热点分类

| 标签 | 值 |
| --- | --- |
| 娱乐 | `2001,2002,2003,2004,2005,2006,2007,2008,2012` |
| 游戏 | `12000,12001` |
| 二次元 | `13000` |
| 音乐 | `29000,29001` |
| 舞蹈 | `28000,28001` |
| 剧情 | `18000` |
| 颜值 | `30000` |
| 美食 | `9000` |
| 旅行 | `10000` |
| 萌宠 | `8000` |
| 时尚 | `16000` |
| 体育 | `5000` |
| 汽车 | `11000` |
| 房产家居 | `17000,17001` |
| 母婴 | `19000` |
| 情感 | `23000` |
| 科技 | `6000` |
| 财经 | `7000` |
| 教育 | `14000,14001` |
| 健康 | `15000` |
| 人文 | `24000` |
| 法律 | `27000` |
| 职场 | `26000` |
| 社会 | `4003,4005` |
| 时政 | `3001,3002` |
| 军事 | `21000` |
| 站内玩法 | `1001,1002,1003` |
| 话题互动 | `20002,20003,20005` |
| 才艺 | `25000` |
| 三农 | `22000` |
| 户外运动 | `31000` |
| 银发生活 | `32000` |

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

### 结果重点看什么

- `data.items`：热点条目列表，重点看 `keyword`、`rankDiff`、`tagName`。
- `data.pagination`：当前返回页码、单页数量和总量信息。
- `item.trends`：热点分数的时间序列，适合判断是否继续上升。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `douyin-realtime-hot-rise` 对应的 AI Skills API/工作流。
