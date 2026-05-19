---
name: ai-humanizer-zh
description: "中文润色去 AI 助手. Use this skill when the user asks for 中文润色去 AI 助手. Do not use when the user goal does not match this skill description."
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

# ai-humanizer-zh 中文润色去 AI 助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

中文润色去 AI 助手

### 什么时候使用

**适用场景**

- the user asks for 中文润色去 AI 助手

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
python3 scripts/run.py --params '{"goal":"改写目标"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `goal` | string | 否 | - | 例如更像真人、更口语、更专业、更有观点、更适合发布或降低营销腔 |
| `audience` | string | 否 | - | 说明读者是谁、他们熟悉什么、对内容最在意什么 |
| `materialUrl` | string | 否 | - | 填写无需登录即可访问的文章、页面、笔记或文档链接；需要传可访问的完整 URL |
| `reviewDepth` | string | 否 | `标准改写` | 选择只做快速去味、标准改写，还是深度重写并解释修改原因；可选值：`快速去味`、`标准改写`、`深度重写` |
| `materialFile` | string | 否 | - | 支持 docx、pdf、md、txt 等文本稿件，适合提交文章草稿、审稿版或长文材料 |
| `materialText` | string | 否 | - | 粘贴需要改得更自然的中文内容，可以是 AI 生成文章、营销文案、社媒长文、课程稿或说明文 |
| `targetPlatform` | string | 否 | `通用中文内容` | 选择文本最终要发布或交付的场景；可选值：`通用中文内容`、`公众号文章`、`小红书笔记`、`官网博客`、`营销落地页`、`课程讲稿`、`知识库文档` |
| `tonePreference` | string | 否 | - | 例如自然口语、专业克制、创作者第一人称、品牌官方但不生硬 |
| `brandRequirements` | string | 否 | - | 补充必须保留的事实、品牌说法、禁用词、合规边界或不能改变的语气 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"goal":"改写目标"}'
```

等价的 `--params` JSON：

```json
{
  "goal": "改写目标"
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

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `ai-humanizer-zh` 对应的 AI Skills API/工作流。
