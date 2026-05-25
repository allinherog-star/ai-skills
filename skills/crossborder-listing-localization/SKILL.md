---
name: crossborder-listing-localization
description: "转化实验助手适合运营、市场营销、销售、产品在用户提出“这个改动值得测吗”这类问题，需要快速拆解目标、判断重点并形成可执行结果时使用，帮助基于输入材料生成摘要、诊断结论、行动建议和可复用交付物。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取API Key，用于运行时技能调用。"
---

# crossborder-listing-localization 转化实验助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

转化实验助手用于回答「这个改动值得测吗」、电商运营、商品转化、用户反馈，适合运营、市场营销、销售、产品在明确业务目标、内容材料或分析对象后调用。
它会结合原始 Listing、粘贴标题、五点、描述、A+ 文案、搜索词或需要本地化的商品页面内容。等输入，整理关键上下文，并输出摘要、诊断结论、行动建议和可复用交付物，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提出“这个改动值得测吗”这类问题，需要快速拆解目标、判断重点并形成可执行结果
- 运营、市场营销、销售、产品需要围绕转化实验助手生成摘要、诊断结论、行动建议和可复用交付物
- 用户已经准备了发布平台（发布平台）、上传 Listing 资料（支持 Listing 文档、关键词表、竞品摘录、商品资料或翻译稿。）、原始 Listing（粘贴标题、五点、描述、A+ 文案、搜索词或需要本地化的商品页面内容。），希望整理成可执行的分析或优化结果
- 用户需要把转化实验助手相关材料转成清晰结论、优先级和下一步动作

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

### 交付内容

- 摘要、诊断结论、行动建议和可复用交付物：围绕用户目标整理可直接阅读、复盘或交付的核心结果。
- 输入材料解读：结合发布平台（发布平台）、上传 Listing 资料（支持 Listing 文档、关键词表、竞品摘录、商品资料或翻译稿。）、原始 Listing（粘贴标题、五点、描述、A+ 文案、搜索词或需要本地化的商品页面内容。）提炼关键上下文和判断依据。
- 下一步动作：给出优先级、执行建议或可继续加工的内容框架。

### 结果使用建议

- 先判断输出是否回答了用户关于「转化实验助手」的核心问题。
- 再检查结果是否覆盖摘要、诊断结论、行动建议和可复用交付物，以及是否给出明确下一步动作。
- 如果输入材料较少，建议让用户补充目标、受众、限制条件或原始材料后再运行。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
