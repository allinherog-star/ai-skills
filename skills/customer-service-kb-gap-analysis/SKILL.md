---
name: customer-service-kb-gap-analysis
description: "业务诊断助手适合运营、产品、市场营销、technical在用户提出“这件事该怎么做”这类问题，需要快速拆解目标、判断重点并形成可执行结果时使用，帮助基于输入材料生成摘要、诊断结论、行动建议和可复用交付物。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key，用于运行导出的技能调用。"
---

# customer-service-kb-gap-analysis 业务诊断助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

业务诊断助手用于回答「这件事该怎么做」、文档处理、资料审阅、摘要，适合运营、产品、市场营销、technical在明确业务目标、内容材料或分析对象后调用。
它会结合客服样本、粘贴工单、聊天记录、用户问题、FAQ 片段或知识库摘录；请先去除不…等输入，整理关键上下文，并输出摘要、诊断结论、行动建议和可复用交付物，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提出“这件事该怎么做”这类问题，需要快速拆解目标、判断重点并形成可执行结果
- 运营、产品、市场营销、technical需要围绕业务诊断助手生成摘要、诊断结论、行动建议和可复用交付物
- 用户已经准备了诊断深度（诊断深度）、诊断目标（例如减少重复咨询、补齐上线 FAQ、优化升级路径或统一客服口径。）、客服样本（粘贴工单、聊天记录、用户问题、FAQ 片段或知识库摘录；请先去除不必要的个人信息。），希望整理成可执行的分析或优化结果
- 用户需要把业务诊断助手相关材料转成清晰结论、优先级和下一步动作

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**基础调用**

```bash
python3 scripts/run.py --params '{}'
```

**带常用参数调用**

```bash
python3 scripts/run.py --params '{"reviewDepth":"快速缺口"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `reviewDepth` | string | 否 | `标准诊断` | 诊断深度；可选值：`快速缺口`、`标准诊断`、`深度知识库计划` |
| `analysisGoal` | string | 否 | - | 例如减少重复咨询、补齐上线 FAQ、优化升级路径或统一客服口径 |
| `ticketSamples` | string | 否 | - | 粘贴工单、聊天记录、用户问题、FAQ 片段或知识库摘录；请先去除不必要的个人信息 |
| `productContext` | string | 否 | - | 补充产品功能、用户类型、服务政策、常见限制和业务背景 |
| `currentKbContext` | string | 否 | - | 填写已有栏目、文章标题、宏话术、客服流程或已知缺口 |
| `ticketSamplesFile` | string | 否 | - | 支持 docx、pdf、md、txt、csv 等工单样本或知识库文件 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"reviewDepth":"快速缺口"}'
```

等价的 `--params` JSON：

```json
{
  "reviewDepth": "快速缺口"
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
- 输入材料解读：结合诊断深度（诊断深度）、诊断目标（例如减少重复咨询、补齐上线 FAQ、优化升级路径或统一客服口径。）、客服样本（粘贴工单、聊天记录、用户问题、FAQ 片段或知识库摘录；请先去除不必要的个人信息。）提炼关键上下文和判断依据。
- 下一步动作：给出优先级、执行建议或可继续加工的内容框架。

### 结果使用建议

- 先判断输出是否回答了用户关于「业务诊断助手」的核心问题。
- 再检查结果是否覆盖摘要、诊断结论、行动建议和可复用交付物，以及是否给出明确下一步动作。
- 如果输入材料较少，建议让用户补充目标、受众、限制条件或原始材料后再运行。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
