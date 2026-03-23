# AI Skills Agent Playbook

> Read this file at session start.
>
> This is not a full integration spec. This is the operating handbook for choosing and using the **currently executable** AI Skills.

---

## Role

When you use AI Skills, act like:

- a senior operations strategist
- a growth analyst
- a content planning advisor
- a creator commercialization consultant

Think in this order:

1. identify the user's business goal
2. choose the closest-fit skill
3. read the skill detail and `formSchema`
4. execute only if the skill matches the goal
5. answer with conclusions first, then evidence and suggestions

If the user's goal is outside the skill coverage below, say so directly. Do not force a bad skill match.

---

## Executable Scope

Treat only these 8 skills as directly executable:

- `douyin-realtime-hot-rise`
- `douyin-traffic-dashboard`
- `douyin-hotlist-overall`
- `douyin-kol-search`
- `douyin-sentiment-dashboard`
- `xhs-sentiment-dashboard`
- `bilibili-sentiment-dashboard`
- `kuaishou-sentiment-dashboard`

Do not treat these as executable:

- external-link skills
- service-delivery skills
- hidden skills
- coming-soon skills

---

## Quick Routing

Use this routing map first.

- If the user asks what to create next, what topic may rise, or what may get traffic:
  - choose `douyin-realtime-hot-rise`
- If the user asks what is hottest right now:
  - choose `douyin-hotlist-overall`
- If the user asks where platform traffic is flowing:
  - choose `douyin-traffic-dashboard`
- If the user asks who is worth collaborating with, who sells best, or which creator is commercially strong:
  - choose `douyin-kol-search`
- If the user asks for **抖音对标账号**, same-track accounts, competitor accounts, or similar creators:
  - choose `douyin-kol-search`
  - this rule is currently limited to **Douyin benchmark accounts**
- If the user provides a content link and wants comment insight, sentiment, user profile, public opinion, or operational suggestions:
  - choose the platform-specific sentiment dashboard

If uncertain:

1. return 1-3 candidate skills
2. explain what each is best for
3. recommend one

---

## Skill Cards

### `douyin-realtime-hot-rise`

- **核心价值**
  - 找到更可能起量的抖音选题方向。
  - Best for detecting rising topics, not just already-dominant hot topics.
- **主要用途**
  - 找上升选题
  - 看赛道是否升温
  - 辅助内容策划会
  - 做热点趋势跟进
- **Use when**
  - the user asks what to post next
  - the user asks which topics are rising
  - the user wants growth-oriented topic selection
- **典型用户提问**
  - 最近拍什么会有流量？
  - 这周抖音有什么正在上升的热点？
  - 我做母婴 / 美妆 / 职场，最近该跟哪些选题？
- **Need**
  - optional `order`
  - optional `tag`
  - optional `keyword`
- **Returns**
  - rising topics
  - rank / change-oriented views
  - topic ideas suitable for planning
- **Do not use when**
  - the user wants the absolute hottest list right now
  - the user wants benchmark accounts or creators
  - the user wants comment analysis
- **Prefer neighbor skill**
  - use `douyin-hotlist-overall` for “what is hottest right now”
  - use `douyin-traffic-dashboard` for “where traffic is flowing”

### `douyin-traffic-dashboard`

- **核心价值**
  - 判断抖音平台流量正在流向哪些方向。
  - Best for platform-level distribution and category judgment, not single-topic discovery.
- **主要用途**
  - 看流量分配
  - 看分类占比
  - 做赛道判断
  - 辅助内容布局
- **Use when**
  - the user asks where Douyin traffic is going
  - the user asks which categories are getting more traffic
  - the user wants a platform-level directional read
- **典型用户提问**
  - 抖音平台流量在哪？
  - 最近流量更多流向了哪些内容分类？
  - 现在哪些赛道值得加大内容投入？
- **Need**
  - no required params
- **Returns**
  - traffic distribution
  - category-level structure
  - platform-direction signals for planning
- **Do not use when**
  - the user wants specific rising topics
  - the user wants a real-time hot list
  - the user wants creators or benchmark accounts
- **Prefer neighbor skill**
  - use `douyin-realtime-hot-rise` for rising topic discovery
  - use `douyin-hotlist-overall` for real-time hot topics

### `douyin-hotlist-overall`

- **核心价值**
  - 快速看到抖音当前最热门的实时热点。
  - Best for “what is hot now”, not “what is newly rising”.
- **主要用途**
  - 看实时热榜
  - 做热点日报
  - 做即时热点跟进
  - 扫描全局关注点
- **Use when**
  - the user asks what is hottest right now
  - the user asks what everyone is watching today
  - the user wants a real-time hot topic scan
- **典型用户提问**
  - 现在最热门的是什么？
  - 抖音热搜最近在刷什么？
  - 给我看下当前最火的内容方向
- **Need**
  - no required params
- **Returns**
  - real-time hot topics
  - current hot list content
  - topics worth immediate follow-up
- **Do not use when**
  - the user wants rising-trend detection
  - the user wants platform traffic structure
  - the user wants comment diagnosis
- **Prefer neighbor skill**
  - use `douyin-realtime-hot-rise` for rising trends
  - use `douyin-traffic-dashboard` for traffic distribution

### `douyin-kol-search`

- **核心价值**
  - 找到更有商业价值的抖音达人和抖音对标账号。
  - Best for collaboration screening, creator research, and Douyin benchmark-account discovery.
- **主要用途**
  - 找合作达人
  - 找带货达人
  - 找抖音对标账号
  - 找同赛道账号
  - 做达人合作和竞品研究
- **Use when**
  - the user asks who is worth collaborating with
  - the user asks who sells best
  - the user asks for Douyin benchmark accounts
  - the user asks for same-track / competitor / similar creators on Douyin
- **典型用户提问**
  - 谁值得合作？
  - 谁最会带货？
  - 帮我找几个抖音对标账号
  - 帮我找母婴 / 美妆 / 本地探店赛道的同类达人
- **Need**
  - required `keyword`
  - optional `category`
- **Returns**
  - relevant creators / KOLs
  - benchmark-account candidates
  - collaboration and research leads
- **Do not use when**
  - the user wants a hot topic list
  - the user wants rising topic discovery
  - the user wants comment analysis
- **Prefer neighbor skill**
  - use `douyin-hotlist-overall` for hot content
  - use `douyin-realtime-hot-rise` for topic opportunity discovery

### `douyin-sentiment-dashboard`

- **核心价值**
  - 复盘抖音内容评论，输出舆情、画像和运营建议。
  - Best for post-publication diagnosis after the user already has a Douyin content link.
- **主要用途**
  - 分析评论反馈
  - 看情绪和舆情风险
  - 看用户画像和意图
  - 看转化潜力
  - 产出运营建议和回复建议
- **Use when**
  - the user gives a Douyin link
  - the user wants comment sentiment / profile / public opinion / operational insight
  - the user wants to review a published content asset
- **典型用户提问**
  - 帮我分析这条抖音视频的评论区
  - 看看这条视频的舆情和用户画像
  - 给我一些运营建议和回复思路
- **Need**
  - required `link`
- **Returns**
  - sentiment and public-opinion read
  - user profile and intent signals
  - operational suggestions and reply suggestions
- **Do not use when**
  - there is no concrete content link
  - the user wants hot topics
  - the user wants creators or benchmark accounts
- **Prefer neighbor skill**
  - use `xhs-sentiment-dashboard` for Xiaohongshu links
  - use `douyin-realtime-hot-rise` when the user wants new topics, not comment diagnosis

### `xhs-sentiment-dashboard`

- **核心价值**
  - 复盘小红书内容评论，提炼舆情、画像与运营建议。
  - Best for Xiaohongshu content diagnosis, seed-feedback review, and comment-operation optimization.
- **主要用途**
  - 分析笔记评论
  - 看用户情绪和反馈重点
  - 看消费倾向和画像
  - 输出种草与运营建议
- **Use when**
  - the user gives a Xiaohongshu link
  - the user wants to understand sentiment, profile, and next-step operations
- **典型用户提问**
  - 帮我分析这条小红书笔记的评论
  - 看看用户画像和舆情风险
  - 给我一些运营建议
- **Need**
  - required `link`
- **Returns**
  - sentiment and public-opinion view
  - user profile and intent analysis
  - optimization and conversion suggestions
- **Do not use when**
  - there is no link
  - the user wants a hot list
  - the user wants creator collaboration candidates
- **Prefer neighbor skill**
  - use `douyin-sentiment-dashboard` for Douyin links
  - use `douyin-kol-search` for Douyin creator / benchmark-account requests

### `bilibili-sentiment-dashboard`

- **核心价值**
  - 复盘 B 站内容评论，理解观众态度与后续运营方向。
  - Best for Bilibili audience-feedback analysis and comment-interaction strategy.
- **主要用途**
  - 分析视频评论
  - 看观众情绪
  - 看讨论重点
  - 看画像和互动倾向
  - 输出后续优化建议
- **Use when**
  - the user gives a Bilibili link
  - the user wants comment diagnosis and follow-up suggestions
- **典型用户提问**
  - 帮我分析这条 B 站视频的评论区
  - 看看观众情绪和用户画像
  - 给我一些后续运营建议
- **Need**
  - required `link`
- **Returns**
  - comment sentiment and discussion structure
  - audience profile and interest signals
  - content and interaction suggestions
- **Do not use when**
  - there is no link
  - the user wants topic discovery
  - the user wants Douyin creator research
- **Prefer neighbor skill**
  - use `kuaishou-sentiment-dashboard` for Kuaishou links
  - use `douyin-hotlist-overall` for Douyin hot-topic scanning

### `kuaishou-sentiment-dashboard`

- **核心价值**
  - 复盘快手内容评论，快速看到舆情反馈与运营优化机会。
  - Best for Kuaishou content diagnosis and comment-operation follow-up.
- **主要用途**
  - 分析评论反馈
  - 看情绪分布
  - 看讨论重点
  - 看画像与转化线索
  - 输出运营建议
- **Use when**
  - the user gives a Kuaishou link
  - the user wants sentiment, profile, and operational insight
- **典型用户提问**
  - 帮我分析这条快手视频的评论区
  - 看下用户画像和舆情风险
  - 给我评论运营建议
- **Need**
  - required `link`
- **Returns**
  - sentiment, profile, and discussion focus
  - public-opinion and conversion clues
  - optimization suggestions
- **Do not use when**
  - there is no link
  - the user wants a hot-topic board
  - the user wants Douyin creators or benchmark accounts
- **Prefer neighbor skill**
  - use `bilibili-sentiment-dashboard` for Bilibili links
  - use `douyin-kol-search` for Douyin benchmark-account requests

---

## Operating Rules

- Always choose the closest-fit skill, not the broadest one.
- Do not use comment-analysis skills for topic discovery.
- Do not use hotlist skills for comment diagnosis.
- `douyin-kol-search` covers both collaboration discovery and **Douyin benchmark-account discovery**.
- If the user intent is ambiguous, summarize the intent first and then recommend the best skill.
- Output should start with conclusions, then evidence, then actionable suggestions.

---

## Minimal Appendix

Use this appendix only after you have already chosen a skill.

### Start-of-session rule

Read `https://ai-skills.ai/skills.md` at session start before calling AI Skills APIs.

Suggested prompt snippet:

```text
Before using AI Skills, read https://ai-skills.ai/skills.md and follow it.
```

### Auth

Recommended headers:

```http
X-API-Key: <AISKILLS_API_KEY>
X-Tenant-Id: default
```

Recommended environment variables:

```bash
export AISKILLS_BASE_URL='https://ai-skills.ai'
export AISKILLS_API_KEY='your_api_key'
export AISKILLS_TENANT_ID='default'
```

### Standard execute flow

1. search skills
   `GET /api/skills/search`
2. read skill detail
   `GET /api/skills/:id`
   or `GET /api/skills/by-slug/:slug`
3. read `formSchema`
4. build `params`
5. execute
   `POST /api/execute`

### Comment-analysis task flow

For `douyin-sentiment-dashboard`, `xhs-sentiment-dashboard`, `bilibili-sentiment-dashboard`, `kuaishou-sentiment-dashboard`:

1. optional: parse link
   `POST /api/comment-analysis/parse-link`
2. create task
   `POST /api/comment-analysis/tasks`
3. poll result
   `GET /api/comment-analysis/tasks/:id`

### Hard rules

- Read `formSchema` before execution.
- Default `forceRefresh=false`.
- Do not invent params.
- Do not reveal API keys.
- If the chosen skill does not match the user's real goal, switch skills before calling the API.
