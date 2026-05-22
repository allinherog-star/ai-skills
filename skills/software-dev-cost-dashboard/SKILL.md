---
name: software-dev-cost-dashboard
description: "软件成本评估看板适合管理、技术、软件、通用在用户想估算软件项目开发成本时使用，帮助基于输入材料生成外部 Web 应用入口、`https://soft.ai-skills.ai` 内的软件成本评估流程。"
requiredEnvVars: []
---

# software-dev-cost-dashboard 软件成本评估看板

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

软件成本评估看板用于回答「软件开发成本不可控」、估算软件开发成本、梳理项目预算、辅助立项和报价沟通，适合管理、技术、软件、通用在明确业务目标、内容材料或分析对象后调用。
它会结合用户输入的业务背景和目标等输入，整理关键上下文，并输出外部 Web 应用入口、`https://soft.ai-skills.ai` 内的软件成本评估流程，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户想估算软件项目开发成本
- 用户需要预算或报价规划看板
- 用户可以继续到外部 Web 应用完成评估

### 调用方式

当前技能为 external-link 模式，请直接访问 [https://soft.ai-skills.ai](https://soft.ai-skills.ai) 完成操作。

### 命令示例

当前技能不通过 `python3 scripts/run.py` 直接调用，请直接访问 [https://soft.ai-skills.ai](https://soft.ai-skills.ai)。

### 参数说明

当前技能不通过本地 runner 传参，直接在目标站点内完成输入与操作。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能不解析本地 JSON 参数，请直接访问 [https://soft.ai-skills.ai](https://soft.ai-skills.ai) 完成后续操作。

### 示例请求

当前技能为 external-link 模式，不适用 CLI 请求示例。请直接访问 [https://soft.ai-skills.ai](https://soft.ai-skills.ai)。

### 返回结果示例

```json
{
  "success": true,
  "data": {
    "invocationMode": "external-link",
    "externalLink": "https://soft.ai-skills.ai",
    "externalLinkLabel": "打开成本看板",
    "message": "Open this external-link target to continue."
  }
}
```

### 交付内容

- 打开成本看板的外部操作入口。
- 面向业务用户的表单、看板或工作流页面，用于继续完成评估和交付。

### 结果使用建议

- 进入外部页面后，优先补全项目背景、目标范围和约束条件，结果会更适合直接用于决策。
- 把评估结果用于预算讨论、方案对齐或后续报价沟通，而不是只看单一数字。

### 运行前准备

- 当前技能不依赖本地 API Key 环境变量。
