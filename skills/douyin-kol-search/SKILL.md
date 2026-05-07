---
name: douyin-kol-search
description: "抖音最具商业价值 KOL. Use this skill when the user asks who is worth collaborating with; the user asks who sells best; the user asks for Douyin benchmark accounts; the user asks for same-track / competitor / similar creators on Douyin. Do not use when the user wants a hot topic list; the user wants rising topic discovery."
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网获取的 API Key。运行脚本时会随请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数，不含用户对话上下文）"
    - "X-API-Key（认证密钥）"
  warning: "此技能会调用 AI Skills API。启用前请确认您信任 ai-skills.ai 的数据安全政策，并使用可随时撤销的 API Key。"
---

# douyin-kol-search 抖音最具商业价值 KOL

官网入口：<https://ai-skills.ai>

### 概述

抖音最具商业价值 KOL

### 什么时候使用

**适用场景**

- the user asks who is worth collaborating with
- the user asks who sells best
- the user asks for Douyin benchmark accounts
- the user asks for same-track / competitor / similar creators on Douyin

**典型用户提问**

- 谁值得合作？
- 谁最会带货？
- 帮我找几个抖音对标账号
- 帮我找母婴 / 美妆 / 本地探店赛道的同类达人

**不要用于**

- the user wants a hot topic list
- the user wants rising topic discovery
- the user wants comment analysis

**相邻技能选择**

- use `douyin-hotlist-overall` for hot content
- use `douyin-realtime-hot-rise` for topic opportunity discovery

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**按赛道和粉丝范围筛选**

```bash
python3 scripts/run.py --params '{"keyword":"深圳烧烤酒吧","contentTag":"tag-48","followerRange":"10-100"}'
```

**只按关键词搜达人**

```bash
python3 scripts/run.py --params '{"keyword":"深圳烧烤酒吧"}'
```

**只按分类搜达人**

```bash
python3 scripts/run.py --params '{"contentTag":"tag-48"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `contentTag` | string | 否 | - | 内容标签编码，传入 tag-{id}。可只填该字段按赛道搜索，具体映射见下方「contentTag 取值参考」；`keyword`、`contentTag` 至少填写一个 |
| `keyword` | string | 否 | - | 赛道关键词，如「深圳烧烤酒吧」。与 `contentTag` 至少填写一个 |
| `followerRange` | string | 否 | - | 格式为「最小值-最大值」，单位是万，例如 `10-100` 表示 10 万到 100 万粉丝 |

参数约束：`keyword`、`contentTag` 至少填写一个。

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

#### `contentTag`

字段说明：内容分类

| 标签 | 值 |
| --- | --- |
| 美妆 | `tag-1` |
| 时尚 | `tag-6` |
| 萌宠 | `tag-11` |
| 测评 | `tag-15` |
| 游戏 | `tag-23` |
| 二次元 | `tag-25` |
| 旅行 | `tag-27` |
| 汽车 | `tag-31` |
| 生活 | `tag-36` |
| 音乐 | `tag-41` |
| 舞蹈 | `tag-46` |
| 美食 | `tag-48` |
| 母婴亲子 | `tag-55` |
| 运动健身 | `tag-60` |
| 科技数码 | `tag-64` |
| 教育培训 | `tag-68` |
| 颜值达人 | `tag-72` |
| 才艺技能 | `tag-79` |
| 影视娱乐 | `tag-85` |
| 艺术文化 | `tag-87` |
| 财经投资 | `tag-91` |
| 三农 | `tag-95` |
| 剧情搞笑 | `tag-97` |
| 情感 | `tag-100` |
| 园艺 | `tag-102` |
| 随拍 | `tag-130` |
| 房产 | `tag-139` |
| 生活家居 | `tag-1001` |
| 媒体号 | `tag-1002` |

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"keyword":"深圳烧烤酒吧","contentTag":"tag-48","followerRange":"10-100"}'
```

等价的 `--params` JSON：

```json
{
  "keyword": "深圳烧烤酒吧",
  "contentTag": "tag-48",
  "followerRange": "10-100"
}
```

### 返回结果示例

```json
{
  "success": true,
  "data": {
    "keyword": "深圳烧烤酒吧",
    "platformSource": "_1",
    "pagination": {
      "page": 1,
      "pageSize": 20,
      "total": 1
    },
    "items": [
      {
        "uid": "kol-1",
        "nickname": "深圳烧烤王",
        "region": "广东 深圳",
        "followerCount": 560000,
        "interactionRate30d": 0.082,
        "convertIndex": 82,
        "spreadIndex": 76,
        "starIndex": 91,
        "expectedPlayCount": 320000,
        "price20_60": 180000,
        "contentTags": [
          "美食"
        ]
      }
    ],
    "searchStrategy": {
      "usedFallback": true,
      "droppedFilters": [
        "contentTag"
      ],
      "localContentTagFilterApplied": true
    }
  },
  "meta": {
    "executionTime": 842,
    "cached": false
  }
}
```

### 结果重点看什么

- `data.items`：达人列表，优先看 `starIndex`、`convertIndex`、`spreadIndex`。
- `data.searchStrategy`：是否发生了筛选回退，便于判断结果是否为宽松匹配。
- `item.contentTags`：达人赛道标签，用来核对分类筛选是否准确。

### 运行前准备

- `AISKILLS_BASE_URL`：默认使用 AI Skills 官方服务
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `douyin-kol-search` 对应的 AI Skills API/工作流。
