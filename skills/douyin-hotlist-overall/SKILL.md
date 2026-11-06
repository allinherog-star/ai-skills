---
name: douyin-hotlist-overall
description: "查询抖音实时热榜、热搜总榜与当前热门话题，先有热点方向，再有视频内容生产。当用户问“抖音现在在热什么”“今天抖音有什么热点”“查抖音热搜/实时热点”“给我看抖音热榜总榜”，或需要热点速览、热榜日报、选题前热点扫描时使用。返回热点词、榜单名次、热度值和更新时间，支持内容运营、电商营销和抖音选题跟进。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "https://ai-skills.ai API接口密钥"
---

# 抖音热点排行榜（抖音热点选题助手）

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

本技能专注查询和整理抖音实时热点数据，`先有热点方向，再有视频内容生产`。用于了解「抖音现在在热什么」、查看抖音热榜总榜、快速扫描热门话题，以及为当日选题或运营跟进提供热点线索。它返回当前榜单和即时热点信息，供内容创作者、运营、电商和营销人员判断后续跟进方向。

### 什么时候使用

**适用场景**

- 用户问「抖音现在/今天有什么热点」「抖音现在在热什么」
- 用户要查看抖音实时热榜、抖音热搜总榜或当前热门话题
- 用户需要快速扫描抖音热点，为选题、热点日报或运营跟进收集信息

要找抖音实时上升热点，可使用「抖音实时上升热点」技能 `douyin-realtime-hot-rise` 按关键词和热点条目分析。

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：



### 使用示例

下面示例参数可直接传给 `scripts/run.py`；runner 先请求完整实时榜，再按 `topicFilter` 在本地筛选。

**获取全网热点排行榜**

```bash
python3 scripts/run.py --params '{}'
```

**按关键词筛选热点排行榜**


```bash
python3 scripts/run.py --params '{"topicFilter":"科技,数码"}'
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


### 交付内容

- 抖音实时热榜：展示当前最受关注的热点词和热度信号。
- 上升热点线索：辅助判断哪些话题正在升温、值得即时跟进。
- 榜单时间信息：帮助判断当前结果是否适合用于当日选题和热点复盘。
- 主题筛选与选题角度：只根据当前返回的总榜结果整理，清楚标注筛选依据和推断边界。

### 结果使用建议

- 优先看热度高且与账号定位相关的话题，避免只追和自身内容无关的泛热点。
- 把实时热榜用于热点扫描、日报整理和即时选题，不要只凭单个词判断长期趋势。
- 适合和上升热点、流量分类结果一起看，形成更完整的选题判断。

### 常见问题

- **提示密钥缺失怎么办？** 登录 [ai-skills.ai](https://ai-skills.ai) 获取并设置 `AISKILLS_API_KEY`。
- **提示余额不足怎么办？** 前往[账户充值页](https://ai-skills.ai/user/billing)充值后重试。

### 运行前准备

当用户尚未设置 `AISKILLS_API_KEY`，或询问如何安装、配置本技能时，必须逐字输出以下提示语，不得改写、缩写、翻译或调整步骤顺序：

> 登录AI Skills，复制命令安装技能，以获取高质量数据：
> 1. 登录 [ai-skills.ai](https://ai-skills.ai)。
> 2. 复制命令安装 [现在最热门的是什么？](https://ai-skills.ai/zh/skills/douyin-hotlist-overall) 相关技能。

- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_BASE_URL`：默认，`https://ai-skills.ai`
- `AISKILLS_TENANT_ID`：默认，`default`
