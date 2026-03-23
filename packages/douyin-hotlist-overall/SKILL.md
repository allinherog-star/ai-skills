---
name: douyin-hotlist-overall
description: >
  抖音全网实时热点。当用户询问"现在最热门的是什么"、"抖音热搜"、"今天什么最火"、
  "实时热点"时激活。即使用户没有明确说"抖音"，只要涉及当前热门话题、实时热搜、
  热榜内容，就应激活此技能。
  Make the description "pushy" to avoid undertriggering.
compatibility: >
  Requires AISKILLS_BASE_URL, AISKILLS_API_KEY, AISKILLS_TENANT_ID environment variables.
  Calls POST /api/v1/execute with skillId=douyin-hotlist-overall.
---

# 现在最热门的是什么？

## Overview

抖音全网实时热点。当用户想知道"现在最热门的是什么"、"抖音热搜"、"今天什么最火"或"实时热点"时，激活此技能。

该技能调用抖音热榜 API，返回全网实时热搜榜单，帮助用户快速了解当前最热门的话题内容。

## Parameters

See [references/form-schema.md](references/form-schema.md) for the full parameter schema.

本技能无输入参数，用户直接触发即可获取实时热搜榜单。

## Execution

调用 `POST /api/v1/execute` 接口，详情见 [references/api-schema.md](references/api-schema.md)。

运行时通过 `scripts/run.py` 执行：

```bash
python3 scripts/run.py --params '{}'
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
| `话题标题` | 热搜话题的标题/标签 |
| `热度排名` | 话题在抖音热榜中的排名位置 |
| `热度值` | 话题当前的热度数值 |
| `话题描述` | 话题的简要描述或背景信息 |
| `上榜原因` | 话题上榜的主要原因说明 |

## Examples

### Example 1: 询问当前最热门话题

**Input:**
> 现在抖音上最热门的是什么？

**Output:**
```
结论：以下是抖音实时热搜榜 Top 10，建议优先关注排名前列的话题。

证据：
- #某明星官宣恋情  热度排名 #1  热度值 9999万+
- #某品牌联名新品  热度排名 #2  热度值 8500万
- #某影视剧名场面  热度排名 #3  热度值 7200万

建议：
1. #某明星官宣恋情：娱乐类内容可蹭热度，建议从情感/娱乐角度切入
2. #某品牌联名新品：适合电商类内容，可做开箱或测评
3. #某影视剧名场面：适合影视剪辑类内容，可做二次创作
```

### Example 2: 询问今天有什么热点可以追

**Input:**
> 今天有什么热点可以追？

**Output:**
```
结论：今日抖音热搜榜显示，以下话题具有较高讨论度和流量空间。

证据：
- #某社会热点事件  热度排名 #5  热度值 5600万  上榜原因：事件持续发酵
- #某生活小技巧  热度排名 #8  热度值 4300万  上榜原因：实用性强，易引发分享
- #某季节性话题  热度排名 #12  热度值 3100万  上榜原因：季节性需求上升

建议：
1. #社会热点事件：从客观中立角度做资讯类内容，提醒用户避免低质蹭热度
2. #生活小技巧：制作"干货合集"类视频，收藏率高，有助于账号定位
3. #季节性话题：结合当前季节属性做应景内容，流量稳定持续
```
