---
name: interview-question-scorecard-generator
description: "业务诊断助手适合人力资源、管理者、运营、software在用户提出“这件事该怎么做”这类问题，需要快速拆解目标、判断重点并形成可执行结果时使用，帮助基于输入材料生成摘要、诊断结论、行动建议和可复用交付物。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取API Key，用于运行时技能调用。"
---

# interview-question-scorecard-generator 业务诊断助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

业务诊断助手用于回答「这件事该怎么做」、面试、评分表、招聘，适合人力资源、管理者、运营、software在明确业务目标、内容材料或分析对象后调用。
它会结合面试需求说明、粘贴岗位要求、能力项、面试轮次、候选人级别和考察重点。等输入，整理关键上下文，并输出摘要、诊断结论、行动建议和可复用交付物，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提出“这件事该怎么做”这类问题，需要快速拆解目标、判断重点并形成可执行结果
- 人力资源、管理者、运营、software需要围绕业务诊断助手生成摘要、诊断结论、行动建议和可复用交付物
- 用户已经准备了生成重点（选择本次面试题与评分卡生成最需要优先处理的方向。）、评分规则与限制（补充评分等级、淘汰项、敏感问题禁区和人工复核要求。）、上传面试资料（上传岗位画像、能力模型、历史题库、面试记录或评分模板。），希望整理成可执行的分析或优化结果
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
python3 scripts/run.py --params '{"scorecardFocus":"行为问题"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `scorecardFocus` | string | 否 | `行为问题` | 选择本次面试题与评分卡生成最需要优先处理的方向；可选值：`行为问题`、`案例题`、`评分锚点`、`追问清单` |
| `scoringRuleNotes` | string | 否 | - | 补充评分等级、淘汰项、敏感问题禁区和人工复核要求 |
| `interviewGuideFile` | string | 否 | - | 上传岗位画像、能力模型、历史题库、面试记录或评分模板 |
| `competencyModelLink` | string | 否 | - | 填写公开可访问的能力模型、岗位说明或面试流程链接；需要传可访问的完整 URL |
| `roleInterviewContext` | string | 否 | - | 说明岗位、职级、业务线、面试时长、面试官角色和轮次目标 |
| `interviewRequirementText` | string | 否 | - | 粘贴岗位要求、能力项、面试轮次、候选人级别和考察重点 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"scorecardFocus":"行为问题"}'
```

等价的 `--params` JSON：

```json
{
  "scorecardFocus": "行为问题"
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
- 输入材料解读：结合生成重点（选择本次面试题与评分卡生成最需要优先处理的方向。）、评分规则与限制（补充评分等级、淘汰项、敏感问题禁区和人工复核要求。）、上传面试资料（上传岗位画像、能力模型、历史题库、面试记录或评分模板。）提炼关键上下文和判断依据。
- 下一步动作：给出优先级、执行建议或可继续加工的内容框架。

### 结果使用建议

- 先判断输出是否回答了用户关于「业务诊断助手」的核心问题。
- 再检查结果是否覆盖摘要、诊断结论、行动建议和可复用交付物，以及是否给出明确下一步动作。
- 如果输入材料较少，建议让用户补充目标、受众、限制条件或原始材料后再运行。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
