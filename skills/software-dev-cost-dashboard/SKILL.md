---
name: software-dev-cost-dashboard
description: "软件成本评估看板. Use this skill when the user asks for software project cost estimation; the user wants a budget or quote planning dashboard; the user can continue in the external web app. Do not use when the user expects an API-executable agent skill; the user wants Douyin / Xiaohongshu / Bilibili / Kuaishou content analysis."
requiredEnvVars: []
security:
  thirdPartyDomain: soft.ai-skills.ai
  dataSent:
    - "用户在浏览器中直接访问 https://soft.ai-skills.ai 输入的内容（技能本身不经导出 runner 传递数据）"
  warning: "此技能为 external-link 模式，不通过导出 runner 直接调用 API。请在访问目标站点前确认其数据安全与隐私政策。"
---

# software-dev-cost-dashboard 软件成本评估看板

官网入口：<https://ai-skills.ai>

### 概述

软件成本评估看板

### 什么时候使用

**适用场景**

- the user asks for software project cost estimation
- the user wants a budget or quote planning dashboard
- the user can continue in the external web app

**典型用户提问**

- 这个软件项目大概要多少钱？
- 帮我评估一下开发成本
- 我需要一个立项预算看板

**不要用于**

- the user expects an API-executable agent skill
- the user wants Douyin / Xiaohongshu / Bilibili / Kuaishou content analysis

**相邻技能选择**

- use the executable social-media skills for traffic, hot-topic, creator, and comment-analysis tasks

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
    "externalLinkLabel": "软件开发成本不可控?",
    "message": "Open this external-link target to continue."
  }
}
```

### 结果重点看什么

- `data.externalLink`：外部站点入口，打开后继续使用技能。
- `data.externalLinkLabel`：目标站点显示名称，便于在市场中识别跳转目标。

### 运行前准备

- 当前技能不依赖本地 API Key 环境变量。

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `software-dev-cost-dashboard` 对应的 AI Skills API/工作流。
