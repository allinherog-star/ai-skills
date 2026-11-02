---
name: douyin-traffic-dashboard
description: "用于查看抖音平台整体流量和热点在各内容分类间的分布。当用户问“抖音流量现在集中在哪些赛道”、“抖音各类内容流量占比”、“哪些内容分类更热门”、“抖音平台流量大盘/分类热度排行”，或需要做平台级赛道观察时使用。返回分类名称、热点数量、热度占比和更新时间，帮助进行内容方向与赛道布局的初步判断。本技能提供平台整体分类数据；不分析单个账号的流量、单条视频表现或粉丝画像，不用于查询具体热搜词、追踪单个话题或直接生成内容。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "API credential used to retrieve Douyin platform-level content category distribution, hot-topic counts, percentages, and update time."
---

# 抖音流量分布大盘｜内容分类占比与赛道观察

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

本技能查看抖音平台整体内容分类的热点分布，返回各分类名称、热点数量、占比和数据更新时间。适合平台级赛道观察、内容方向初筛与运营复盘；结果反映分类层面的整体数据，不代表某个账号或单条视频的表现。

### 什么时候使用

**适用场景**

- 用户问「抖音流量现在集中在哪些内容赛道」「抖音各分类流量占比是多少」
- 用户要比较抖音美食、体育、娱乐等内容分类的热点数量或热度占比
- 用户需要查看抖音平台流量大盘、分类热度排行或进行赛道级内容布局

**不适用场景**

- 用户要查看具体热搜词、单个热点的排名变化；应使用热榜或上升热点技能
- 用户要分析自己的账号、单条视频、粉丝或投放表现
- 用户要查询其他平台的数据或直接生成文案、图片、视频

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**查看全站流量分布**

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
    "categories": [
      {
        "label": "美食",
        "value": "9000",
        "hotCount": 128,
        "percentage": 14,
        "icon": "utensils",
        "description": "探店、烹饪、美食测评",
        "group": "life"
      },
      {
        "label": "体育",
        "value": "5000",
        "hotCount": 96,
        "percentage": 11,
        "icon": "dumbbell",
        "description": "赛事、运动员、训练内容",
        "group": "knowledge"
      }
    ],
    "total": 32,
    "updateTime": "2026-04-24T11:30:00.000Z"
  },
  "meta": {
    "executionTime": 842,
    "cached": false
  }
}
```

### 交付内容

- 平台流量分布：展示不同内容分类的热度占比和热点数量。
- 赛道判断线索：帮助判断当前哪些内容方向更值得投入。
- 分类参考：可继续用于抖音热点筛选、内容布局和运营复盘。

### 结果使用建议

- 先看流量占比和热点数量高的分类，再结合账号能力判断是否值得投入。
- 适合做赛道层面的内容布局，不直接替代具体选题判断。
- 可把分类结果继续用于筛选上升热点或规划内容矩阵。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
