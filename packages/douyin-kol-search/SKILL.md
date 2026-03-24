---
name: douyin-kol-search
description: >
  抖音 KOL 搜索与达人合作推荐。当用户询问"找达人合作"、"搜索同赛道博主"、
  "谁是最会卖货的博主"、"抖音有哪些优质 KOL"、"达人搜索"时激活。
  即使用户没有明确说"抖音"，只要涉及博主搜索、KOL 商业价值评估、
  达人合作候选人，就应激活此技能。
compatibility: >
  需要配置 AISKILLS_API_KEY（必填）。BASE_URL 和 TENANT_ID 已内置，无需配置。
---

# 谁是最会卖货的博主？

## 概述

抖音 KOL 搜索与达人合作推荐。当用户想知道"谁是最会卖货的博主"、"搜索同赛道达人"、"有哪些优质抖音 KOL"或"达人合作候选人"时，激活此技能。

该技能调用抖音 KOL 搜索 API，根据关键词和内容分类返回优质博主列表，帮助商家快速找到合适的达人合作候选人。

## 参数说明

详细参数规范见 [references/form-schema.md](references/form-schema.md)。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `keyword` | string | 是 | 搜索词，用于匹配博主或内容关键词 |
| `category` | string | 否 | 内容分类 |

## 执行方式

运行时通过 `scripts/run.py` 执行：

```bash
python3 scripts/run.py --params '{"keyword": "美妆", "category": "美妆"}'
```

## 环境变量

| 环境变量 | 说明 |
|----------|------|
| `AISKILLS_API_KEY` | API 密钥（必填），请运行 `export AISKILLS_API_KEY='your_api_key'` 配置 |

## 输出格式

输出遵循 **结论 -> 证据 -> 建议** 三段式结构。

```
## 抖音 KOL 搜索结果

| 博主 | 粉丝 | 商业价值 | 互动率 | 内容方向 |
|------|------|----------|--------|----------|
| @零食控小美 | 120w | A | 8.5% | 零食评测 |

**建议：**
- ...
```

详细格式规范见 [references/output-format.md](references/output-format.md)。
