---
name: seo-article-review
description: "SEO/AEO 诊断助手. Use this skill when the user asks for SEO/AEO 诊断助手. Do not use when the user goal does not match this skill description."
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key。运行脚本时会随请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数，不含用户对话上下文）"
    - "X-API-Key（认证密钥）"
  warning: "此技能会调用 AI Skills API。启用前请确认您信任 ai-skills.ai 的数据安全政策，并使用可随时撤销的 API Key。"
---

# seo-article-review SEO/AEO 诊断助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

SEO/AEO 诊断助手

### 什么时候使用

**适用场景**

- the user asks for SEO/AEO 诊断助手

**不要用于**

- the user goal does not match this skill description

**相邻技能选择**

- compare neighboring skill cards before execution

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**基础调用**

```bash
python3 scripts/run.py --params '{}'
```

**带常用参数调用**

```bash
python3 scripts/run.py --params '{"goal":"转化目标"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `goal` | string | 否 | - | 例如提升关键词覆盖、搜索排名、AI 摘要引用、线索转化或内容权威感 |
| `audience` | string | 否 | - | 说明搜索用户画像和意图阶段，例如新手学习、方案比较、采购决策或专家复核 |
| `materialUrl` | string | 否 | - | 填写无需登录即可访问的文章页、博客页或搜索落地页链接；需要传可访问的完整 URL |
| `reviewDepth` | string | 否 | `标准诊断` | 诊断深度；可选值：`快速体检`、`标准诊断`、`深度改稿` |
| `materialFile` | string | 否 | - | 支持 docx、pdf、md、txt 等文章稿件，适合提交 Markdown、Word 或审稿版文件 |
| `materialText` | string | 否 | - | 可粘贴待审文章正文、标题方案或搜索优化草稿；建议保留 H1/H2、关键词和内链标记 |
| `searchIntent` | string | 否 | - | 例如了解概念、比较方案、购买决策、教程操作 |
| `targetKeyword` | string | 否 | - | 希望覆盖的核心关键词或查询语句 |
| `targetPlatform` | string | 否 | `SEO/AEO` | 目标平台；可选值：`SEO/AEO`、`官网博客`、`知识库` |
| `brandRequirements` | string | 否 | - | 补充品牌语气、必须保留的事实、内部链接要求、合规边界或禁用表达 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"goal":"转化目标"}'
```

等价的 `--params` JSON：

```json
{
  "goal": "转化目标"
}
```

### 返回结果示例

```json
{
  "success": true,
  "data": {
    "message": "示例结果请以技能真实返回结构为准。"
  },
  "meta": {
    "executionTime": 842,
    "cached": false
  }
}
```

### 结构化结果约定

异步执行完成时，运行时必须在产物目录根部写出 `result.json`，并使用 `ResultEnvelope` 结构：

- `items` 是预览导航的唯一来源；默认只写一个主结果 `item`。
- `artifacts` 是可下载产物清单，不会自动变成预览 Tab。
- `item.artifactIds` 或 `item.artifacts` 只表示某个结果项需要引用这些文件进行展示。
- 多结构预览必须由技能在 `items` 中显式声明多个结果项，必要时使用 `presentation.mode: "tabs"`。

### 结果重点看什么

- `data`：技能主返回结果，先看核心业务字段是否符合预期。
- `meta.executionTime`：本次执行耗时，便于排查慢请求。
- `meta.cached`：是否命中缓存，帮助判断结果新鲜度。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `seo-article-review` 对应的 AI Skills API/工作流。
