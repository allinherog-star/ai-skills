---
name: policy-execution-checklist-generator
description: "风险审阅助手适合人力资源、管理者、运营、software在用户提出“这里有什么风险”这类问题，需要快速拆解目标、判断重点并形成可执行结果时使用，帮助基于输入材料生成摘要、诊断结论、行动建议和可复用交付物。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key，用于运行导出的技能调用。"
---

# policy-execution-checklist-generator 风险审阅助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

风险审阅助手用于回答「这里有什么风险」、企业制度、执行清单、内控，适合人力资源、管理者、运营、software在明确业务目标、内容材料或分析对象后调用。
它会结合制度条款内容、粘贴制度、流程要求、审批规则、岗位责任和例外处理。等输入，整理关键上下文，并输出摘要、诊断结论、行动建议和可复用交付物，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提出“这里有什么风险”这类问题，需要快速拆解目标、判断重点并形成可执行结果
- 人力资源、管理者、运营、software需要围绕风险审阅助手生成摘要、诊断结论、行动建议和可复用交付物
- 用户已经准备了制度条款内容（粘贴制度、流程要求、审批规则、岗位责任和例外处理。）、上传制度文件（上传制度文件、流程图、检查表、会议纪要或内控要求。）、制度参考链接（填写公开可访问的制度说明、政策文件、流程页面或公告链接。），希望整理成可执行的分析或优化结果
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
python3 scripts/run.py --params '{"policyRuleText":"制度条款内容"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `policyRuleText` | string | 否 | - | 粘贴制度、流程要求、审批规则、岗位责任和例外处理 |
| `policyDocumentFile` | string | 否 | - | 上传制度文件、流程图、检查表、会议纪要或内控要求 |
| `policyReferenceLink` | string | 否 | - | 填写公开可访问的制度说明、政策文件、流程页面或公告链接；需要传可访问的完整 URL |
| `responsibleTeamNotes` | string | 否 | - | 补充责任人、审批节点、证据留存、例外条件和检查周期 |
| `rolloutScenarioContext` | string | 否 | - | 说明适用部门、岗位、流程频次、系统工具和管理目标 |
| `checklistGenerationFocus` | string | 否 | `步骤拆解` | 选择本次制度执行清单生成最需要优先处理的方向；可选值：`步骤拆解`、`责任分工`、`证据留存`、`检查节奏` |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"policyRuleText":"制度条款内容"}'
```

等价的 `--params` JSON：

```json
{
  "policyRuleText": "制度条款内容"
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
- 输入材料解读：结合制度条款内容（粘贴制度、流程要求、审批规则、岗位责任和例外处理。）、上传制度文件（上传制度文件、流程图、检查表、会议纪要或内控要求。）、制度参考链接（填写公开可访问的制度说明、政策文件、流程页面或公告链接。）提炼关键上下文和判断依据。
- 下一步动作：给出优先级、执行建议或可继续加工的内容框架。

### 结果使用建议

- 先判断输出是否回答了用户关于「风险审阅助手」的核心问题。
- 再检查结果是否覆盖摘要、诊断结论、行动建议和可复用交付物，以及是否给出明确下一步动作。
- 如果输入材料较少，建议让用户补充目标、受众、限制条件或原始材料后再运行。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
