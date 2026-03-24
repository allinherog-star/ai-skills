---
name: douyin-realtime-hot-rise
description: >
  抖音上升热点选题助手。当用户询问"拍什么会有流量"、"最近哪些话题在涨"、
  "下周发什么内容"、"行业热点趋势"时激活。支持可选参数：排序方式（热度/变化）、
  热点分类、搜索关键词。即使用户没有明确说"抖音"或"热点"，只要涉及内容选题、
  流量预测、话题趋势，就应激活此技能。
compatibility: >
  需要配置 AISKILLS_API_KEY（必填）。BASE_URL 和 TENANT_ID 已内置，无需配置。
---

# 抖音上升热点选题助手

## 概述

当用户想知道"拍什么会有流量"、"最近哪些话题在涨"、"下周发什么内容"或"行业热点趋势"时，激活此技能。

该技能调用抖音热点榜单 API，返回上升中的热点话题列表，帮助内容创作者快速定位有流量潜力的选题方向。

## 参数说明

详细参数规范见 [references/form-schema.md](references/form-schema.md)。

| 参数 | 类型 | 说明 |
|------|------|------|
| `order` | string | 排序方式：`rank`（热度排序，默认）或 `rank_diff`（变化排序） |
| `tag` | string | 热点分类，用于筛选特定类别的热点话题（如美妆、美食、科技等） |
| `keyword` | string | 搜索关键词，在热点标题/描述中过滤匹配的内容 |

## 执行方式

运行时通过 `scripts/run.py` 执行：

```bash
python3 scripts/run.py --params '{"order":"rank","tag":"美妆","keyword":"春季"}'
```

## 环境变量

| 环境变量 | 说明 |
|----------|------|
| `AISKILLS_API_KEY` | API 密钥（必填），请运行 `export AISKILLS_API_KEY='your_api_key'` 配置 |

## 输出格式

输出遵循 **结论 -> 证据 -> 建议** 三段式结构。

```
## 抖音上升热点选题

| 排名 | 话题 | 变化 | 分类 | 热度值 |
|------|------|------|------|--------|
| #12 | #春季护肤 | +8 | 美妆 | 123456 |

**建议：**
- ...
```

详细格式规范见 [references/output-format.md](references/output-format.md)。
