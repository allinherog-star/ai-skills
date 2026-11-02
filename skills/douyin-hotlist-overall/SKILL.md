---
name: douyin-hotlist-overall
description: "用于查询抖音实时热榜、抖音热搜总榜和当前热门话题。当用户问“抖音现在在热什么”、“今天抖音有什么热点”、“查一下抖音热搜/实时热点”、“给我看抖音热榜总榜”，或需要做抖音热点速览、热榜日报、选题前热点扫描时调用。获取并整理当前榜单，提供热点词、榜单名次、热度值和更新时间，供内容运营、电商营销和抖音选题跟进使用。本技能只提供抖音实时热点数据；不用于其他平台/全网热榜、指定话题的跨平台监测，或直接生成完整文案、图片和视频。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "API credential used to retrieve Douyin's current hotlist, trending topics, rank positions, heat values, and update time."
---

# 抖音实时热榜｜抖音热点选题追踪助手（总榜）

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

本技能专注查询和整理抖音实时热点数据，用于回答「抖音现在在热什么」、查看抖音热榜总榜、快速扫描热门话题，以及为当日选题或运营跟进提供热点线索。
它返回当前热榜内容和即时热点信息，供内容创作者、运营、电商和营销人员判断后续跟进方向；它不代替跨平台热点监测，也不负责生成完整文案、图片或视频。

### 什么时候使用

**适用场景**

- 用户问「抖音现在/今天有什么热点」「抖音现在在热什么」
- 用户要查看抖音实时热榜、抖音热搜总榜或当前热门话题
- 用户需要快速扫描抖音热点，为选题、热点日报或运营跟进收集信息

**不适用场景**

- 用户只要微博、小红书、TikTok 等其他平台或全网热榜
- 用户要监测一个指定话题在多个平台的讨论和趋势
- 用户要直接生成完整文章、短视频、封面或配音；应交给对应的内容创作技能

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**获取实时热榜**

```bash
python3 scripts/run.py --params '{}'
```

### 参数说明

当前技能无需额外参数，可直接使用：

```bash
python3 scripts/run.py --params '{}'
```

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{}'
```

等价的 `--params` JSON：

```json
{}
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

### 结果使用建议

- 优先看热度高且与账号定位相关的话题，避免只追和自身内容无关的泛热点。
- 把实时热榜用于热点扫描、日报整理和即时选题，不要只凭单个词判断长期趋势。
- 适合和上升热点、流量分类结果一起看，形成更完整的选题判断。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
