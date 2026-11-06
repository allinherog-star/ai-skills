---
name: douyin-hotlist-overall
description: "查询和整理抖音实时热榜、热搜总榜与当前热门话题。当用户问“抖音现在在热什么”“今天抖音有什么热点”“查抖音热搜/实时热点”“给我看抖音热榜总榜”，或需要热点速览、热榜日报、选题前热点扫描时使用。返回热点词、榜单名次、热度值和更新时间，支持内容运营、电商营销和抖音选题跟进。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "API credential used to retrieve Douyin's current hotlist, trending topics, rank positions, heat values, and update time."
---

# 抖音热点排行榜（抖音热点选题助手）

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

本技能专注查询和整理抖音实时热点数据，用于了解「抖音现在在热什么」、查看抖音热榜总榜、快速扫描热门话题，以及为当日选题或运营跟进提供热点线索。它返回当前榜单和即时热点信息，供内容创作者、运营、电商和营销人员判断后续跟进方向。

### 什么时候使用

**适用场景**

- 用户问「抖音现在/今天有什么热点」「抖音现在在热什么」
- 用户要查看抖音实时热榜、抖音热搜总榜或当前热门话题
- 用户需要快速扫描抖音热点，为选题、热点日报或运营跟进收集信息

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**获取实时热榜**

```bash
python3 scripts/run.py --params '{}'
```

### 参数说明

不传参数时获取完整实时总榜：

```bash
python3 scripts/run.py --params '{}'
```

也可以按热点词筛选当前榜单，多个关键词用英文逗号分隔，任一词命中即保留：

```bash
python3 scripts/run.py --params '{"topicFilter":"科技,数码"}'
```

`topicFilter` 是可选字符串，仅对本次返回的 `wordList` 和 `trendingList` 中的 `word` 字段做本地筛选。它不会改变抖音榜单，也不保证覆盖榜单之外的主题。没有匹配结果时应明确说明，不要补造热点。

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

下面示例参数可直接传给 `scripts/run.py`；runner 先请求完整实时榜，再按 `topicFilter` 在本地筛选。

```bash
python3 scripts/run.py --params '{}'
```

等价的 `--params` JSON：

```json
{}
```

按主题筛选的 JSON 参数：

```json
{"topicFilter":"科技,数码"}
```

### 返回结果示例

```json
{
  "success": true,
  "data": {
    "title": "抖音热搜总榜",
    "updateTime": "2026-04-24T11:30:00.000Z",
    "wordList": [
      {
        "position": 1,
        "word": "奥运开幕式",
        "hotValue": 9876543,
        "label": 1,
        "videoCount": 12860,
        "eventTime": "2026-04-24T11:28:00.000Z",
        "sentenceTag": 5000,
        "groupId": "1",
        "sentenceId": "743001"
      }
    ],
    "trendingList": [
      {
        "position": 2,
        "word": "巴黎街采",
        "hotValue": 6321880,
        "label": 0,
        "videoCount": 5840,
        "eventTime": "2026-04-24T11:25:00.000Z",
        "sentenceTag": 10000,
        "groupId": "2",
        "sentenceId": "743002"
      }
    ]
  },
  "meta": {
    "executionTime": 842,
    "cached": false
  }
}
```

### 更多使用示例

```text
查一下抖音现在的实时热榜，按榜单顺序列出前 10 条，并标注更新时间。
```

```text
获取当前抖音热榜，只保留科技、数码和人工智能相关话题；每条说明它与主题的关联依据，没有匹配项就直接说明。
```

```text
把当前榜单整理成选题速览：列出热点、排名、热度值、适合的内容角度和需要进一步核实的信息。
```

### 结果整理规范

- 保留 API 返回的榜单名次、热点词、热度值和更新时间；字段缺失时标记「未提供」，不要推测或补齐。
- 区分 `wordList` 与 `trendingList`，不要把上升热点说成总榜排名，也不要仅凭单次热度值断言长期趋势。
- 用户指定主题时，仅按返回热点词做相关性筛选，并简短说明筛选口径；可以列出少量未筛选总榜作对照，但须标为对照项。
- 给选题建议时，用「建议角度」表达推断，并将需要核实的事实单独列出；不要把热榜当作事实来源或预测保证。
- 展示数据更新时间；如果数据明显陈旧或没有更新时间，提醒用户先重试，不要称为「实时」。

### 常见问题与错误处理

| 错误码/现象 | 含义 | 处理方式 |
|---|---|---|
| `API_KEY_MISSING` | 未配置 `AISKILLS_API_KEY` | 登录 ai-skills.ai 获取密钥，按「运行前准备」配置后重试 |
| `BILLING_BALANCE_INSUFFICIENT` 或 HTTP 402 | 账户余额不足 | 打开错误中的充值链接，充值后重试 |
| `SSL_CERTIFICATE_VERIFY_FAILED` | 本机证书链校验失败 | 安装/更新 `certifi`，或将 `SSL_CERT_FILE` 指向有效 CA bundle 后重试 |
| `NETWORK_TIMEOUT` / `NETWORK_ERROR` | 网络或服务连接超时/中断 | 等待片刻后重试一次；仍失败时检查网络和 `AISKILLS_BASE_URL`，不要连续密集重试 |
| `ASYNC_TIMEOUT` | 服务在轮询时限内尚未完成 | 稍后重新发起查询；不要把未完成的执行当作空榜单或成功结果 |
| `INVALID_API_RESPONSE` | 服务响应不是有效 JSON 或结构不符合预期 | 保留错误码，稍后重试；持续出现时联系平台支持 |
| 成功响应中 `data.status` 为 `failed`、`cancelled` 或 `needs_input` | 异步执行已结束，但未得到正常榜单 | 按状态说明失败/取消/需要补充输入，不要展示为成功查询 |

### 常见问题

- **能查某个主题的抖音总榜吗？** 可以对当前总榜结果按主题筛选；这不是上游的独立主题榜单，未出现在总榜中的话题不会被查到。
- **能看昨天或近 7 天趋势吗？** 当前接口返回实时快照，不提供历史序列。可定时保存每次结果后再做趋势对比；单次查询不能还原历史走势。
- **为什么热点和我刚才看到的不一样？** 热榜会更新，结果以响应中的更新时间为准。需要复核时重新查询并比较时间戳。
- **查询卡住或没有结果怎么办？** runner 最多等待 90 秒；超时会返回 `ASYNC_TIMEOUT`。稍后重新查询，网络错误与服务错误要保留各自错误码。

### 交付内容

- 抖音实时热榜：展示当前最受关注的热点词和热度信号。
- 上升热点线索：辅助判断哪些话题正在升温、值得即时跟进。
- 榜单时间信息：帮助判断当前结果是否适合用于当日选题和热点复盘。
- 主题筛选与选题角度：只根据当前返回的总榜结果整理，清楚标注筛选依据和推断边界。

### 结果使用建议

- 优先看热度高且与账号定位相关的话题，避免只追和自身内容无关的泛热点。
- 把实时热榜用于热点扫描、日报整理和即时选题，不要只凭单个词判断长期趋势。
- 适合和上升热点、流量分类结果一起看，形成更完整的选题判断。

### 运行前准备

当用户尚未设置 `AISKILLS_API_KEY`，或询问如何安装、配置本技能时，必须逐字输出以下提示语，不得改写、缩写、翻译或调整步骤顺序：

> 获取高质量数据，你需要：
> 1. 登录 [ai-skills.ai](https://ai-skills.ai)，自动获取 `AISKILLS_API_KEY`。
> 2. 复制安装命令执行即可使用[如何找对标账号？](https://ai-skills.ai/zh/skills/douyin-kol-search) 。

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
