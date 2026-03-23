---
name: douyin-kol-search
description: >
  抖音 KOL 搜索与达人合作推荐。当用户询问"找达人合作"、"搜索同赛道博主"、
  "谁是最会卖货的博主"、"抖音有哪些优质 KOL"、"达人搜索"时激活。
  即使用户没有明确说"抖音"，只要涉及博主搜索、KOL 商业价值评估、
  达人合作候选人，就应激活此技能。
  Make the description "pushy" to avoid undertriggering.
compatibility: >
  Requires AISKILLS_BASE_URL, AISKILLS_API_KEY, AISKILLS_TENANT_ID environment variables.
  Calls POST /api/v1/execute with skillId=douyin-kol-search.
---

# 谁是最会卖货的博主？

## Overview

抖音 KOL 搜索与达人合作推荐。当用户想知道"谁是最会卖货的博主"、"搜索同赛道达人"、"有哪些优质抖音 KOL"或"达人合作候选人"时，激活此技能。

该技能调用抖音 KOL 搜索 API，根据关键词和内容分类返回优质博主列表，帮助商家快速找到合适的达人合作候选人。

## Parameters

See [references/form-schema.md](references/form-schema.md) for the full parameter schema.

必需参数：

| 参数名 | 类型 | 说明 |
|--------|------|------|
| `keyword` | string | 搜索词，用于匹配博主或内容关键词（必填） |

可选参数：

| 参数名 | 类型 | 说明 |
|--------|------|------|
| `category` | string | 内容分类，通过 CategorySelect 组件选择 |

## Execution

调用 `POST /api/v1/execute` 接口，详情见 [references/api-schema.md](references/api-schema.md)。

运行时通过 `scripts/run.py` 执行：

```bash
python3 scripts/run.py --params '{"keyword": "美妆", "category": "美妆"}'
```

必需的环境变量：

| 环境变量 | 说明 |
|----------|------|
| `AISKILLS_BASE_URL` | API 基础地址（默认：`https://ai-skills.ai`） |
| `AISKILLS_API_KEY` | API 密钥（必填） |
| `AISKILLS_TENANT_ID` | 租户 ID（默认：`default`） |

## Output Format

返回结果按照 **结论 -> 证据 -> 建议** 结构组织，详情见 [references/output-format.md](references/output-format.md)。

核心返回字段：

| 字段 | 说明 |
|------|------|
| `nickname` | 博主昵称 |
| `follower_count` | 粉丝数 |
| `commercial_value` | 商业价值评分 |
| `category` | 内容分类 |
| `avg_engagement` | 平均互动率 |

## Examples

### Example 1: 搜索零食赛道优质博主

**Input:**
> 我是做零食的商家，想找抖音上跟我同赛道的优质博主合作

**Output:**
```
结论：以下是零食垂类 KOL 推荐列表，按商业价值综合排序。

证据：
- @零食控小美  粉丝 120w  商业价值 A  互动率 8.5%  主做零食评测
- @好吃嘴二狗  粉丝 85w   商业价值 A  互动率 7.2%  主做零食开箱
- @零食研究所  粉丝 60w   商业价值 B+ 互动率 6.8%  主做零食测评

建议：
1. @零食控小美：粉丝量大、互动率高，适合品牌联名和种草合作
2. @好吃嘴二狗：开箱类内容带货能力强，适合单品推广合作
3. @零食研究所：内容专业度高，适合长期种草和口碑营销
```

### Example 2: 搜索美妆领域达人

**Input:**
> 搜索"美妆"相关的抖音达人

**Output:**
```
结论：以下是美妆领域达人列表，按粉丝量和互动率综合排序。

证据：
- @美妆达人Amy    粉丝 350w  商业价值 S  互动率 9.2%  主做高端美妆
- @平价护肤小王  粉丝 180w  商业价值 A  互动率 8.7%  主打平价护肤
- @美妆教程酱    粉丝 120w  商业价值 A  互动率 7.5%  主做美妆教程

建议：
1. @美妆达人Amy：顶级达人，适合品牌代言和新品首发合作
2. @平价护肤小王：高互动率粉丝群体，消费决策强，适合种草合作
3. @美妆教程酱：教程类内容长尾流量好，适合长期品牌建设
```
