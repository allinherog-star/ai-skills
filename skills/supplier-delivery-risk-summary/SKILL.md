---
name: supplier-delivery-risk-summary
description: "风险审阅助手适合运营、管理者、manufacturing、供应商在用户提出“这里有什么风险”这类问题，需要快速拆解目标、判断重点并形成可执行结果时使用，帮助基于输入材料生成摘要、诊断结论、行动建议和可复用交付物。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key，用于运行导出的技能调用。"
---

# supplier-delivery-risk-summary 风险审阅助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

风险审阅助手用于回答「这里有什么风险」、供应商、交付风险、采购，适合运营、管理者、manufacturing、供应商在明确业务目标、内容材料或分析对象后调用。
它会结合交付情况说明、粘贴供应商延期、缺货、质量异常、排产变更或沟通记录。等输入，整理关键上下文，并输出摘要、诊断结论、行动建议和可复用交付物，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提出“这里有什么风险”这类问题，需要快速拆解目标、判断重点并形成可执行结果
- 运营、管理者、manufacturing、供应商需要围绕风险审阅助手生成摘要、诊断结论、行动建议和可复用交付物
- 用户已经准备了供应商与物料背景（说明供应商等级、物料类别、采购周期、替代来源和合同约束。）、上传交付数据（上传订单、排产表、到货记录、库存表或供应商邮件。）、摘要重点（选择本次供应商交付风险摘要最需要优先处理的方向。），希望整理成可执行的分析或优化结果
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
python3 scripts/run.py --params '{"supplierContext":"供应商与物料背景"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `supplierContext` | string | 否 | - | 说明供应商等级、物料类别、采购周期、替代来源和合同约束 |
| `deliveryDataFile` | string | 否 | - | 上传订单、排产表、到货记录、库存表或供应商邮件 |
| `deliveryRiskFocus` | string | 否 | `延期风险` | 选择本次供应商交付风险摘要最需要优先处理的方向；可选值：`延期风险`、`缺料影响`、`替代方案`、`沟通清单` |
| `supplierPortalLink` | string | 否 | - | 填写公开可访问的供应商公告、物流页面或资料链接；需要传可访问的完整 URL |
| `purchaseImpactNotes` | string | 否 | - | 补充安全库存、客户交期、替代料、加急成本和责任人 |
| `supplierDeliveryText` | string | 否 | - | 粘贴供应商延期、缺货、质量异常、排产变更或沟通记录 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"supplierContext":"供应商与物料背景"}'
```

等价的 `--params` JSON：

```json
{
  "supplierContext": "供应商与物料背景"
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
- 输入材料解读：结合供应商与物料背景（说明供应商等级、物料类别、采购周期、替代来源和合同约束。）、上传交付数据（上传订单、排产表、到货记录、库存表或供应商邮件。）、摘要重点（选择本次供应商交付风险摘要最需要优先处理的方向。）提炼关键上下文和判断依据。
- 下一步动作：给出优先级、执行建议或可继续加工的内容框架。

### 结果使用建议

- 先判断输出是否回答了用户关于「风险审阅助手」的核心问题。
- 再检查结果是否覆盖摘要、诊断结论、行动建议和可复用交付物，以及是否给出明确下一步动作。
- 如果输入材料较少，建议让用户补充目标、受众、限制条件或原始材料后再运行。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
