---
name: douyin-hotlist-overall
description: >
  抖音全网实时热点。当用户询问"现在最热门的是什么"、"抖音热搜"、"今天什么最火"、
  "实时热点"时激活。即使用户没有明确说"抖音"，只要涉及当前热门话题、实时热搜、
  热榜内容，就应激活此技能。
compatibility: >
  需要配置 AISKILLS_API_KEY（必填）。BASE_URL 和 TENANT_ID 已内置，无需配置。
---

# 现在最热门的是什么？

## 概述

抖音全网实时热点。当用户想知道"现在最热门的是什么"、"抖音热搜"、"今天什么最火"或"实时热点"时，激活此技能。

该技能调用抖音热榜 API，返回全网实时热搜榜单，帮助用户快速了解当前最热门的话题内容。

## 参数说明

本技能无输入参数，用户直接触发即可获取实时热搜榜单。

## 执行方式

运行时通过 `scripts/run.py` 执行：

```bash
python3 scripts/run.py --params '{}'
```

## 环境变量

| 环境变量 | 说明 |
|----------|------|
| `AISKILLS_API_KEY` | API 密钥（必填），请运行 `export AISKILLS_API_KEY='your_api_key'` 配置 |

## 输出格式

输出遵循 **结论 -> 证据 -> 建议** 三段式结构。

```
## 抖音实时热搜榜

| 排名 | 话题 | 热度值 |
|------|------|--------|
| #1 | #某明星官宣恋情 | 9999万 |

**建议：**
- ...
```

详细格式规范见 [references/output-format.md](references/output-format.md)。
