---
name: sales-meeting-follow-up-plan
description: "销售增长助手适合销售、市场营销、运营、产品在用户提出“客户为什么不推进”这类问题，需要快速拆解目标、判断重点并形成可执行结果时使用，帮助基于输入材料生成摘要、诊断结论、行动建议和可复用交付物。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key，用于运行导出的技能调用。"
---

# sales-meeting-follow-up-plan 销售增长助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

销售增长助手用于回答「客户为什么不推进」、销售赋能、客户研究、跟进计划，适合销售、市场营销、运营、产品在明确业务目标、内容材料或分析对象后调用。
它会结合销售会议纪要、粘贴会议转写、会后速记、聊天记录或客户沟通摘要。等输入，整理关键上下文，并输出摘要、诊断结论、行动建议和可复用交付物，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提出“客户为什么不推进”这类问题，需要快速拆解目标、判断重点并形成可执行结果
- 销售、市场营销、运营、产品需要围绕销售增长助手生成摘要、诊断结论、行动建议和可复用交付物
- 用户已经准备了商机背景（说明客户阶段、联系人、竞争情况、预算时间线或当前推进卡点。）、跟进深度（跟进深度）、跟进目标（例如约下一次会、发送方案、确认试点、推进采购或唤醒客户。），希望整理成可执行的分析或优化结果
- 用户需要把销售增长助手相关材料转成清晰结论、优先级和下一步动作

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**基础调用**

```bash
python3 scripts/run.py --params '{}'
```

**带常用参数调用**

```bash
python3 scripts/run.py --params '{"dealContext":"商机背景"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `dealContext` | string | 否 | - | 说明客户阶段、联系人、竞争情况、预算时间线或当前推进卡点 |
| `reviewDepth` | string | 否 | `标准方案` | 跟进深度；可选值：`快速跟进`、`标准方案`、`深度复盘` |
| `followUpGoal` | string | 否 | - | 例如约下一次会、发送方案、确认试点、推进采购或唤醒客户 |
| `productContext` | string | 否 | - | 补充产品能力、报价、案例、限制条件和会中提到的材料 |
| `meetingNotesFile` | string | 否 | - | 支持 docx、pdf、md、txt 等会议纪要或转写文件 |
| `meetingNotesText` | string | 否 | - | 粘贴会议转写、会后速记、聊天记录或客户沟通摘要 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"dealContext":"商机背景"}'
```

等价的 `--params` JSON：

```json
{
  "dealContext": "商机背景"
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
- 输入材料解读：结合商机背景（说明客户阶段、联系人、竞争情况、预算时间线或当前推进卡点。）、跟进深度（跟进深度）、跟进目标（例如约下一次会、发送方案、确认试点、推进采购或唤醒客户。）提炼关键上下文和判断依据。
- 下一步动作：给出优先级、执行建议或可继续加工的内容框架。

### 结果使用建议

- 先判断输出是否回答了用户关于「销售增长助手」的核心问题。
- 再检查结果是否覆盖摘要、诊断结论、行动建议和可复用交付物，以及是否给出明确下一步动作。
- 如果输入材料较少，建议让用户补充目标、受众、限制条件或原始材料后再运行。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
