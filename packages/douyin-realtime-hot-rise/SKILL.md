---
name: douyin-realtime-hot-rise
description: >
  抖音上升热点选题助手。当用户询问"拍什么会有流量"、"最近哪些话题在涨"、
  "下周发什么内容"、"行业热点趋势"时激活。支持可选参数：排序方式（热度/变化）、
  热点分类、搜索关键词。即使用户没有明确说"抖音"或"热点"，只要涉及内容选题、
  流量预测、话题趋势，就应激活此技能。
  Make the description "pushy" to avoid undertriggering.
compatibility: >
  Requires AISKILLS_BASE_URL, AISKILLS_API_KEY, AISKILLS_TENANT_ID environment variables.
  Calls POST /api/v1/execute with skillId=douyin-realtime-hot-rise.
---

# 拍什么会有流量？

## Overview

抖音上升热点选题助手。当用户想知道"拍什么会有流量"、"最近哪些话题在涨"、"下周发什么内容"或"行业热点趋势"时，激活此技能。

该技能调用抖音热点榜单 API，返回上升中的热点话题列表，帮助内容创作者快速定位有流量潜力的选题方向。

## Parameters

See [references/form-schema.md](references/form-schema.md) for the full parameter schema.

| 参数 | 类型 | 说明 |
|------|------|------|
| `order` | string | 排序方式：`rank`（热度排序，默认）或 `rank_diff`（变化排序） |
| `tag` | string | 热点分类，用于筛选特定类别的热点话题（如美妆、美食、科技等） |
| `keyword` | string | 搜索关键词，在热点标题/描述中过滤匹配的内容 |

## Execution

调用 `POST /api/v1/execute` 接口，详情见 [references/api-schema.md](references/api-schema.md)。

运行时通过 `scripts/run.py` 执行：

```bash
python3 scripts/run.py --params '{"order":"rank","tag":"美妆","keyword":"春季"}'
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
| `热度排名` | 话题在抖音热榜中的排名位置 |
| `变化幅度` | 排名相比上一周期的上升/下降变化量 |
| `话题分类` | 话题所属的垂直分类 |
| `选题建议` | 针对用户场景的内容创作建议 |

## Examples

### Example 1: 美妆博主查询热点

**Input:**
> 我是做美妆的抖音博主，最近发什么话题会有流量？

**Output:**
```
结论：近期"春季护肤"和"平价替代"类话题流量显著上升，建议优先跟进。

证据：
- #春季护肤 热度排名 #12，排名上升 +8 位
- #平价替代 热度排名 #25，排名上升 +15 位
- #成分党护肤 热度排名 #38，排名上升 +22 位

建议：
1. 立即拍摄"春季护肤误区"短视频，正面切入#春季护肤
2. 制作"大牌平替"对比视频，挂载购物车引流
3. 发布"成分党必看"科普内容，建立专业人设
```

### Example 2: 按变化幅度排序查询

**Input:**
> 抖音上最近哪些话题涨得最快？按变化排序

**Output:**
```
结论：以下话题近期涨速最快，正处于流量上升期，是最佳切入时机。

证据（按变化幅度排序）：
- #露营穿搭 热度排名 #45，排名上升 +35 位
- #低成本料理 热度排名 #52，排名上升 +28 位
- #职场解压 热度排名 #61，排名上升 +21 位

建议：
1. #露营穿搭：内容饱和度低，可快速跟进
2. #低成本料理：餐饮垂类创作者偏少，先发优势明显
3. #职场解压：覆盖职场人群广，适合泛娱乐内容切入
```

### Example 3: 关键词过滤查询

**Input:**
> 帮我找找抖音上跟"减脂"相关的上升热点

**Output:**
```
结论：找到 3 个与"减脂"相关的上升热点话题，流量正在爬升。

证据：
- #减脂餐 热度排名 #8，排名上升 +5 位
- #减脂零食 热度排名 #31，排名上升 +12 位
- #减脂运动 热度排名 #19，排名上升 +3 位

建议：
1. #减脂餐：竞争激烈，建议差异化角度切入（如"宿舍减脂餐"）
2. #减脂零食：内容缺口大，可做零食测评合集
3. #减脂运动：配合健身计划类内容效果更好
```
