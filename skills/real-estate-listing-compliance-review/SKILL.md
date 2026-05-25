---
name: real-estate-listing-compliance-review
description: "风险审阅助手适合运营、市场营销、retail、内容媒体在用户提出“这里有什么风险”这类问题，需要快速拆解目标、判断重点并形成可执行结果时使用，帮助基于输入材料生成摘要、诊断结论、行动建议和可复用交付物。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取API Key，用于运行时技能调用。"
---

# real-estate-listing-compliance-review 风险审阅助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

风险审阅助手用于回答「这里有什么风险」、房产营销、卖点、合规提示，适合运营、市场营销、retail、内容媒体在明确业务目标、内容材料或分析对象后调用。
它会结合房源话术文本、粘贴房源标题、卖点、户型、学区/交通/价格表述、经纪人话术和海报文…等输入，整理关键上下文，并输出摘要、诊断结论、行动建议和可复用交付物，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提出“这里有什么风险”这类问题，需要快速拆解目标、判断重点并形成可执行结果
- 运营、市场营销、retail、内容媒体需要围绕风险审阅助手生成摘要、诊断结论、行动建议和可复用交付物
- 用户已经准备了房源与交易背景（说明城市、区域、新房/二手、产品类型、客群、交易阶段和渠道。）、上传房源资料（上传房源文案、海报、户型资料、价格表、证照说明或审稿表。）、房源公开链接（填写公开可访问的房源页、小区页、项目页或政策说明链接。），希望整理成可执行的分析或优化结果
- 用户需要把风险审阅助手相关材料转成清晰结论、优先级和下一步动作

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**基础调用**

```bash
python3 scripts/run.py --params '{}'
```

**带常用参数调用**

```bash
python3 scripts/run.py --params '{"propertyContext":"房源与交易背景"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `propertyContext` | string | 否 | - | 说明城市、区域、新房/二手、产品类型、客群、交易阶段和渠道 |
| `listingAssetFile` | string | 否 | - | 上传房源文案、海报、户型资料、价格表、证照说明或审稿表 |
| `propertyPageLink` | string | 否 | - | 填写公开可访问的房源页、小区页、项目页或政策说明链接；需要传可访问的完整 URL |
| `propertyListingText` | string | 否 | - | 粘贴房源标题、卖点、户型、学区/交通/价格表述、经纪人话术和海报文案 |
| `licenseDisclosureNotes` | string | 否 | - | 补充证照信息、价格口径、学区/落户/收益限制、不能承诺内容和需核实事实 |
| `listingComplianceFocus` | string | 否 | `夸大承诺` | 选择本次房产房源话术合规审查最需要优先处理的方向；可选值：`夸大承诺`、`价格口径`、`资质披露`、`安全改写` |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"propertyContext":"房源与交易背景"}'
```

等价的 `--params` JSON：

```json
{
  "propertyContext": "房源与交易背景"
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
- 输入材料解读：结合房源与交易背景（说明城市、区域、新房/二手、产品类型、客群、交易阶段和渠道。）、上传房源资料（上传房源文案、海报、户型资料、价格表、证照说明或审稿表。）、房源公开链接（填写公开可访问的房源页、小区页、项目页或政策说明链接。）提炼关键上下文和判断依据。
- 下一步动作：给出优先级、执行建议或可继续加工的内容框架。

### 结果使用建议

- 先判断输出是否回答了用户关于「风险审阅助手」的核心问题。
- 再检查结果是否覆盖摘要、诊断结论、行动建议和可复用交付物，以及是否给出明确下一步动作。
- 如果输入材料较少，建议让用户补充目标、受众、限制条件或原始材料后再运行。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
