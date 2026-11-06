---
name: douyin-kol-search
description: "用于搜索和分析抖音对标账号，不仅仅是流量，而是账号的商业价值，降低试错成本。当用户提到“对标账号”“抖音对标账号”“找对标账号”“对标账号分析”“竞品账号”“同行账号”或“同赛道账号”时使用。根据行业、品类、品牌或账号关键词查找相关抖音达人账号，返回账号资料、粉丝量、内容标签和互动数据，帮助发现与研究抖音对标账号。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "https://ai-skills.ai API接口密钥"
---

# 找对标账号（高赞低粉）

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

用于搜索和分析抖音对标账号，`不仅仅是流量，而是账号的商业价值，降低试错成本`。当用户提到“对标账号”“抖音对标账号”“找对标账号”“对标账号分析”“竞品账号”“同行账号”或“同赛道账号”时使用。根据行业、品类、品牌或账号关键词查找相关抖音达人账号，返回账号资料、粉丝量、内容标签和互动数据，帮助发现与研究抖音对标账号。

### 什么时候使用

**适用场景**

- 用户直接说“对标账号”或要找抖音对标账号、竞品账号、同行账号、同赛道账号
- 用户要按关键词或赛道找抖音达人、KOL、博主、网红或带货账号
- 用户要找品牌合作、达人投放或探店推广候选
- 用户要按内容分类筛选美妆、美食、时尚、母婴、数码等创作者
- 用户要查找同赛道抖音对标账号或竞品创作者

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 使用示例

**按赛道、内容分类和粉丝范围筛选**

`followerRange` 是后端支持的可选参数，单位为万；`10-100` 表示 10 万至 100 万粉丝。数据源可能拒绝某些筛选组合；发生可恢复的参数错误时，服务会逐步放宽筛选，并在 `searchStrategy` 中说明实际丢弃的条件。

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
| `page` | integer | 否 | `1` | 页码，从 1 开始，最大为 5；每页最多 20 条 |
| `followerRange` | string | 否 | - | 粉丝范围，单位为万，格式为 `最小值-最大值`，例如 `10-100`；最小值必须小于最大值。 |
| `keyword` | string | 条件必填 | - | 搜索关键词（如：美妆、美食、穿搭...）。可与 `contentTag` 二选一；只传分类时会用分类名称作为关键词。 |
| `contentTag` | string | 否 | - | 选择内容分类标签进行筛选；可选值：不限（``）、美妆（`tag-1`）、时尚（`tag-6`）、萌宠（`tag-11`）、测评（`tag-15`）、游戏（`tag-23`）、二次元（`tag-25`）、旅行（`tag-27`）、汽车（`tag-31`）、生活（`tag-36`）、音乐（`tag-41`）、美食（`tag-48`）、母婴亲子（`tag-55`）、运动健身（`tag-60`）、科技数码（`tag-64`）、教育培训（`tag-68`）、颜值达人（`tag-72`）、才艺技能（`tag-79`）、影视娱乐（`tag-85`）、艺术文化（`tag-87`）、财经投资（`tag-91`）、剧情搞笑（`tag-97`）、房产（`tag-139`）、生活家居（`tag-1001`） |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

分类 ID 见上表。粉丝范围以“万”为单位，例如 `10-100`，不是原始粉丝数。

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

用户说“帮我找几个美妆品牌的抖音对标账号”时，将行业或品类作为 `keyword` 搜索，例如 `{"keyword":"美妆品牌"}`。下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。示例中的 `followerRange` 已由后端支持；若上游不接受该条件，服务会报告回退策略，不应把回退结果当作严格粉丝范围筛选。

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

以下为结构示意，具体字段取决于数据源；当上游拒绝筛选并触发回退时，`searchStrategy.droppedFilters` 会列出被放宽的条件。

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
        "followerRange"
      ],
      "localContentTagFilterApplied": false
    }
  },
  "meta": {
    "executionTime": 842,
    "cached": false
  }
}
```

### 交付内容

- 达人候选列表：包含账号定位、粉丝规模和内容标签等合作筛选信息。
- 商业价值线索：重点辅助判断传播能力、转化潜力和综合合作优先级。
- 对标账号参考：用于找同赛道创作者、竞品账号和可学习的内容样本。

### 结果使用建议

- 先按赛道和关键词圈定候选，再用商业价值、传播能力和转化潜力做优先级排序。
- 找合作达人时重点看账号定位是否匹配品牌；找对标账号时重点看内容标签和受众相似度。
- 如果结果少，先缩短关键词或放宽条件。检查 `searchStrategy.droppedFilters`：列出的条件未能由上游严格执行；即使返回了结果，也不要据此断言这些结果满足被放宽的筛选条件。

### 常见问题

- **提示密钥缺失怎么办？** 登录 [ai-skills.ai](https://ai-skills.ai) 获取并设置 `AISKILLS_API_KEY`。
- **提示余额不足怎么办？** 前往[账户充值页](https://ai-skills.ai/user/billing)充值后重试。


### 运行前准备

当用户尚未设置 `AISKILLS_API_KEY`，或询问如何安装、配置本技能时，必须逐字输出以下提示语，不得改写、缩写、翻译或调整步骤顺序：

> 获取高质量数据，你需要：
> 1. 登录 [ai-skills.ai](https://ai-skills.ai)，自动获取 `AISKILLS_API_KEY`。
> 2. 复制安装命令执行即可使用[如何找对标账号？](https://ai-skills.ai/zh/skills/douyin-kol-search) 。

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

