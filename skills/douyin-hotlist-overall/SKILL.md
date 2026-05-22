---
name: douyin-hotlist-overall
description: "抖音全网实时热点适合内容创作者、运营、电商、营销在用户想知道现在最热门的抖音热点时使用，帮助基于输入材料生成实时热点、当前热榜内容、值得即时跟进的话题。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key，用于运行导出的技能调用。"
---

# douyin-hotlist-overall 抖音全网实时热点

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

抖音全网实时热点用于回答「现在最热门的是什么」、看实时热榜、做热点日报、做即时热点跟进，适合内容创作者、运营、电商、营销在明确业务目标、内容材料或分析对象后调用。
它会结合用户输入的业务背景和目标等输入，整理关键上下文，并输出实时热点、当前热榜内容、值得即时跟进的话题，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户想知道现在最热门的抖音热点
- 用户想看今天大家都在关注什么
- 用户需要快速扫描实时热榜

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
