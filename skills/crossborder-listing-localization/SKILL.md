---
name: crossborder-listing-localization
description: "转化实验助手. Use this skill when the user asks for 转化实验助手. Do not use when the user goal does not match this skill description."
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

# crossborder-listing-localization 转化实验助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

转化实验助手

### 什么时候使用

**适用场景**

- the user asks for 转化实验助手

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
python3 scripts/run.py --params '{"platform":"Amazon"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `platform` | string | 否 | `Amazon` | 发布平台；可选值：`Amazon`、`TikTok Shop`、`Shopee`、`Lazada`、`eBay`、`Etsy`、`独立站`、`通用跨境平台` |
| `listingFile` | string | 否 | - | 支持 Listing 文档、关键词表、竞品摘录、商品资料或翻译稿 |
| `listingText` | string | 否 | - | 粘贴标题、五点、描述、A+ 文案、搜索词或需要本地化的商品页面内容 |
| `productInfo` | string | 否 | - | 补充规格、材质、功能、适用场景、认证、包装、售后和必须保留的信息 |
| `marketRegion` | string | 否 | `美国` | 目标市场；可选值：`美国`、`英国`、`加拿大`、`德国`、`法国`、`意大利`、`西班牙`、`日本`、`韩国`、`澳大利亚`、`中东`、`东南亚`、`拉美` |
| `sourceLanguage` | string | 否 | `中文` | 原语言；可选值：`中文`、`英语`、`日语`、`韩语`、`德语`、`法语`、`西班牙语`、`其他` |
| `targetLanguage` | string | 否 | `英语` | 目标语言；可选值：`英语`、`日语`、`韩语`、`德语`、`法语`、`西班牙语`、`意大利语`、`葡萄牙语`、`阿拉伯语` |
| `localizationGoal` | string | 否 | `提升自然搜索和转化` | 优化目标；可选值：`提升自然搜索和转化`、`降低直译感`、`优化标题五点`、`适配目标市场`、`降低风险表达` |
| `keywordRequirements` | string | 否 | - | 填写目标关键词、必须保留词、禁用词、竞品关键词或搜索词报告摘要 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"platform":"Amazon"}'
```

等价的 `--params` JSON：

```json
{
  "platform": "Amazon"
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

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `crossborder-listing-localization` 对应的 AI Skills API/工作流。
