# AI Skills Agent Playbook

> Read this file at session start.
>
> This is not a full integration spec. This is the operating handbook for choosing and using the currently executable AI Skills.

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

Treat only these 11 skills as directly executable:

- `ai-article`
- `auto-article-images`
- `xhs-viral-copywriter`
- `douyin-realtime-hot-rise`
- `douyin-traffic-dashboard`
- `douyin-hotlist-overall`
- `douyin-kol-search`
- `douyin-sentiment-dashboard`
- `xhs-sentiment-dashboard`
- `bilibili-sentiment-dashboard`
- `kuaishou-sentiment-dashboard`

Do not treat these as directly executable:

- external-link skills
- service-delivery skills
- hidden skills
- coming-soon skills

Current non-executable public skills:

- `software-dev-cost-dashboard` (external-link)

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
- If the user asks for software project cost estimation, budget planning, or quote planning:
  - treat `software-dev-cost-dashboard` as an external handoff, not an API-executable skill

If uncertain:

1. return 1-3 candidate skills
2. explain what each is best for
3. recommend one

---

## Skill Cards

### `ai-article`

- **核心价值**
  - 自动图文助手
- **主要用途**
  - 自动图文助手
- **Use when**
  - the user asks for 自动图文助手
- **Need**
  - required `AISKILLS_API_KEY`
  - read `formSchema` before calling
- **Returns**
  - the skill-specific result described in its `SKILL.md`
- **Do not use when**
  - the user goal does not match this skill description
- **Prefer neighbor skill**
  - compare neighboring skill cards before execution

### `auto-article-images`

- **核心价值**
  - 智能配图助手
- **主要用途**
  - 智能配图助手
- **Use when**
  - the user asks for 智能配图助手
- **Need**
  - required `AISKILLS_API_KEY`
  - read `formSchema` before calling
- **Returns**
  - the skill-specific result described in its `SKILL.md`
- **Do not use when**
  - the user goal does not match this skill description
- **Prefer neighbor skill**
  - compare neighboring skill cards before execution

### `xhs-viral-copywriter`

- **核心价值**
  - 爆款文案助手
- **主要用途**
  - 爆款文案助手
- **Use when**
  - the user asks for 爆款文案助手
- **Need**
  - required `AISKILLS_API_KEY`
  - read `formSchema` before calling
- **Returns**
  - the skill-specific result described in its `SKILL.md`
- **Do not use when**
  - the user goal does not match this skill description
- **Prefer neighbor skill**
  - compare neighboring skill cards before execution

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
  - required `AISKILLS_API_KEY`
  - optional `order`
  - optional `tag`
  - optional `keyword`
- **Runtime & Privacy**
  - sends `skillId`, query params, and `X-API-Key` to `ai-skills.ai`
  - use only when the operator accepts this third-party processing
- **Current tag mapping**
  - `tag` uses numeric ids or comma-separated ids. Current default mapping, with runtime values refreshed by the latest category endpoint.
  - Entertainment: `娱乐=2001,2002,2003,2004,2005,2006,2007,2008,2012`; `游戏=12000,12001`; `二次元=13000`; `音乐=29000,29001`; `舞蹈=28000,28001`; `剧情=18000`; `颜值=30000`
  - Life: `美食=9000`; `旅行=10000`; `萌宠=8000`; `时尚=16000`; `体育=5000`; `汽车=11000`; `房产家居=17000,17001`; `母婴=19000`; `情感=23000`
  - Knowledge: `科技=6000`; `财经=7000`; `教育=14000,14001`; `健康=15000`; `人文=24000`; `法律=27000`; `职场=26000`
  - News: `社会=4003,4005`; `时政=3001,3002`; `军事=21000`
  - Creative: `站内玩法=1001,1002,1003`; `话题互动=20002,20003,20005`; `才艺=25000`
  - Emerging: `三农=22000`; `户外运动=31000`; `银发生活=32000`
- **Returns**
  - rising topics
  - rank / change-oriented views
  - topic ideas suitable for planning
- **Do not use when**
  - the user wants the absolute hottest list right now
  - the user wants benchmark accounts or creators
  - the user wants comment analysis
- **Prefer neighbor skill**
  - use `douyin-hotlist-overall` for "what is hottest right now"
  - use `douyin-traffic-dashboard` for "where traffic is flowing"

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
  - required `AISKILLS_API_KEY`
  - no skill params required
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
  - Best for "what is hot now", not "what is newly rising".
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
  - required `AISKILLS_API_KEY`
  - no skill params required
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
  - required `AISKILLS_API_KEY`
  - required at least one of `keyword` or `contentTag`
  - optional `followerRange`
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
  - required `AISKILLS_API_KEY`
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
  - required `AISKILLS_API_KEY`
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
  - required `AISKILLS_API_KEY`
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
  - required `AISKILLS_API_KEY`
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

## Non-Executable Handoffs

### `software-dev-cost-dashboard`

- **核心价值**
  - 评估软件项目开发成本、预算范围与立项报价。
  - External handoff only; this release does not provide a runnable API package for it.
- **主要用途**
  - 估算软件开发成本
  - 梳理项目预算
  - 辅助立项和报价沟通
- **Use when**
  - the user asks for software project cost estimation
  - the user wants a budget or quote planning dashboard
  - the user can continue in the external web app
- **典型用户提问**
  - 这个软件项目大概要多少钱？
  - 帮我评估一下开发成本
  - 我需要一个立项预算看板
- **Need**
  - no local runner params; open the external site
- **Returns**
  - external web-app handoff
  - cost-estimation workflow inside `https://soft.ai-skills.ai`
- **Do not use when**
  - the user expects an API-executable agent skill
  - the user wants Douyin / Xiaohongshu / Bilibili / Kuaishou content analysis
- **Prefer neighbor skill**
  - use the executable social-media skills for traffic, hot-topic, creator, and comment-analysis tasks

Handoff URL: https://soft.ai-skills.ai

---

## Operating Rules

- Always choose the closest-fit skill, not the broadest one.
- Do not use comment-analysis skills for topic discovery.
- Do not use hotlist skills for comment diagnosis.
- `douyin-kol-search` covers both collaboration discovery and Douyin benchmark-account discovery.
- If the user intent is ambiguous, summarize the intent first and then recommend the best skill.
- Output should start with conclusions, then evidence, then actionable suggestions.

---

## Minimal Appendix

Use this appendix only after you have already chosen a skill.

### Start-of-session rule

Read this `skills.md` file at session start before calling AI Skills APIs.

Suggested prompt snippet:

```text
Before using AI Skills, read skills.md and follow it.
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

1. choose a skill from this playbook
2. read `skills/<slug>/SKILL.md`
3. read `skills/<slug>/references/form-schema.json`
4. build `params`
5. run `skills/<slug>/scripts/run.py` or call the equivalent API endpoint

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
