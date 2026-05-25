---
name: ai-remotion-best-practices
description: "Remotion 实践助手适合technical、运营、software、内容媒体在用户提出“视频代码够稳吗”这类问题，需要快速拆解目标、判断重点并形成可执行结果时使用，帮助基于输入材料生成摘要、诊断结论、行动建议和可复用交付物。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取API Key，用于运行时技能调用。"
---

# ai-remotion-best-practices Remotion 实践助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

Remotion 实践助手用于回答「视频代码够稳吗」、Remotion、React、视频生成，适合technical、运营、software、内容媒体在明确业务目标、内容材料或分析对象后调用。
它会结合Remotion 项目背景、粘贴 Remotion 组件、动画需求、目录结构、渲染问题或需要评…等输入，整理关键上下文，并输出摘要、诊断结论、行动建议和可复用交付物，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提出“视频代码够稳吗”这类问题，需要快速拆解目标、判断重点并形成可执行结果
- technical、运营、software、内容媒体需要围绕Remotion 实践助手生成摘要、诊断结论、行动建议和可复用交付物
- 用户已经准备了优化目标（例如排查渲染问题、优化动画结构、提升可维护性、整理最佳实践或准备交付检查。）、交付对象（说明结果面向开发者、设计师、客户、内容团队还是内部评审。）、项目或文档链接（填写公开可访问的代码仓库、文档、预览页或问题链接；私有内容请上传或粘贴。），希望整理成可执行的分析或优化结果
- 用户需要把Remotion 实践助手相关材料转成清晰结论、优先级和下一步动作

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**基础调用**

```bash
python3 scripts/run.py --params '{}'
```

**带常用参数调用**

```bash
python3 scripts/run.py --params '{"goal":"优化目标"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `goal` | string | 否 | - | 例如排查渲染问题、优化动画结构、提升可维护性、整理最佳实践或准备交付检查 |
| `audience` | string | 否 | - | 说明结果面向开发者、设计师、客户、内容团队还是内部评审 |
| `materialUrl` | string | 否 | - | 填写公开可访问的代码仓库、文档、预览页或问题链接；私有内容请上传或粘贴；需要传可访问的完整 URL |
| `materialFile` | string | 否 | - | 上传 Remotion 代码、错误日志、需求说明、截图或项目文档 |
| `materialText` | string | 否 | - | 粘贴 Remotion 组件、动画需求、目录结构、渲染问题或需要评审的代码片段 |
| `brandRequirements` | string | 否 | - | 补充 Remotion 版本、性能要求、浏览器限制、视频规格、不可改动代码或上线时间 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"goal":"优化目标"}'
```

等价的 `--params` JSON：

```json
{
  "goal": "优化目标"
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
- 输入材料解读：结合优化目标（例如排查渲染问题、优化动画结构、提升可维护性、整理最佳实践或准备交付检查。）、交付对象（说明结果面向开发者、设计师、客户、内容团队还是内部评审。）、项目或文档链接（填写公开可访问的代码仓库、文档、预览页或问题链接；私有内容请上传或粘贴。）提炼关键上下文和判断依据。
- 下一步动作：给出优先级、执行建议或可继续加工的内容框架。

### 结果使用建议

- 先判断输出是否回答了用户关于「Remotion 实践助手」的核心问题。
- 再检查结果是否覆盖摘要、诊断结论、行动建议和可复用交付物，以及是否给出明确下一步动作。
- 如果输入材料较少，建议让用户补充目标、受众、限制条件或原始材料后再运行。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
