---
name: lesson-plan-activity-designer
description: "视觉质量诊断助手适合运营、市场营销、教育培训、内容媒体在用户提出“这张图够发布吗”这类问题，需要快速拆解目标、判断重点并形成可执行结果时使用，帮助基于输入材料生成摘要、诊断结论、行动建议和可复用交付物。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取API Key，用于运行时技能调用。"
---

# lesson-plan-activity-designer 视觉质量诊断助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

视觉质量诊断助手用于回答「这张图够发布吗」、教案、课堂活动、培训设计，适合运营、市场营销、教育培训、内容媒体在明确业务目标、内容材料或分析对象后调用。
它会结合课时目标与内容、粘贴本节课主题、知识点、教学目标、课堂时长和已有流程。等输入，整理关键上下文，并输出摘要、诊断结论、行动建议和可复用交付物，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提出“这张图够发布吗”这类问题，需要快速拆解目标、判断重点并形成可执行结果
- 运营、市场营销、教育培训、内容媒体需要围绕视觉质量诊断助手生成摘要、诊断结论、行动建议和可复用交付物
- 用户已经准备了设计重点（选择本次教案活动设计助手最需要优先处理的方向。）、课时目标与内容（粘贴本节课主题、知识点、教学目标、课堂时长和已有流程。）、班级与学员情况（说明年龄/年级、人数、基础、线上线下、设备条件和课堂限制。），希望整理成可执行的分析或优化结果
- 用户需要把视觉质量诊断助手相关材料转成清晰结论、优先级和下一步动作

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**基础调用**

```bash
python3 scripts/run.py --params '{}'
```

**带常用参数调用**

```bash
python3 scripts/run.py --params '{"lessonDesignFocus":"导入活动"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `lessonDesignFocus` | string | 否 | `导入活动` | 选择本次教案活动设计助手最需要优先处理的方向；可选值：`导入活动`、`互动练习`、`分层任务`、`课堂评价` |
| `lessonPlanGoalText` | string | 否 | - | 粘贴本节课主题、知识点、教学目标、课堂时长和已有流程 |
| `classProfileContext` | string | 否 | - | 说明年龄/年级、人数、基础、线上线下、设备条件和课堂限制 |
| `teachingResourceFile` | string | 否 | - | 上传教案、课件、教材摘录、题目或活动素材 |
| `curriculumStandardLink` | string | 否 | - | 填写公开可访问的课标、教材目录、课程说明或案例链接；需要传可访问的完整 URL |
| `activityConstraintNotes` | string | 否 | - | 补充可用工具、分组方式、禁用活动、作业要求和评价标准 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"lessonDesignFocus":"导入活动"}'
```

等价的 `--params` JSON：

```json
{
  "lessonDesignFocus": "导入活动"
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
- 输入材料解读：结合设计重点（选择本次教案活动设计助手最需要优先处理的方向。）、课时目标与内容（粘贴本节课主题、知识点、教学目标、课堂时长和已有流程。）、班级与学员情况（说明年龄/年级、人数、基础、线上线下、设备条件和课堂限制。）提炼关键上下文和判断依据。
- 下一步动作：给出优先级、执行建议或可继续加工的内容框架。

### 结果使用建议

- 先判断输出是否回答了用户关于「视觉质量诊断助手」的核心问题。
- 再检查结果是否覆盖摘要、诊断结论、行动建议和可复用交付物，以及是否给出明确下一步动作。
- 如果输入材料较少，建议让用户补充目标、受众、限制条件或原始材料后再运行。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
