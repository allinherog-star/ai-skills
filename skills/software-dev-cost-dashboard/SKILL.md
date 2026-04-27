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

# AI Skills 技能库：为每一个场景做真正有价值的AI技能库

> 大多数人用 AI 还停在「问一句答一句」。AI Skills（[ai-skills.ai](https://ai-skills.ai/)）想换一种姿势：把 AI 能力拆成一条条能直接执行的 Skill，像查字典一样调出来用。无论你从 AI Skills 官网、skills.sh 还是 ClawHub 进入，先按这 5 步完成接入，再继续看当前技能说明。

![AI Skills 官网场景导览图](https://raw.githubusercontent.com/allinherog-star/aiskillsguides/HEAD/guides/images/ai-skills-site-readme/content-01.webp)

## 快速开始

### 1. 扫码登录

![扫码登录 AI Skills 账号](https://raw.githubusercontent.com/allinherog-star/aiskillsguides/HEAD/guides/images/ai-skills-site-readme/step/1%E3%80%81%E6%89%AB%E7%A0%81%E7%99%BB%E5%BD%95.png)

先在 AI Skills 官网完成扫码登录，确保后续 API Key、安装命令和技能调用都绑定到同一个账号。

### 2. 申请 API Key

![在 AI Skills 站点申请 API Key](https://raw.githubusercontent.com/allinherog-star/aiskillsguides/HEAD/guides/images/ai-skills-site-readme/step/2%E3%80%81%E7%94%B3%E8%AF%B7%E4%BD%A0%E7%9A%84API%20Key.png)

登录后进入 API Key 页面申请密钥，后续 CLI 安装和运行技能都会读取 AISKILLS_API_KEY。

### 3. 复制安装命令

![复制 AI Skills 技能安装命令](https://raw.githubusercontent.com/allinherog-star/aiskillsguides/HEAD/guides/images/ai-skills-site-readme/step/3%E3%80%81%E5%A4%8D%E5%88%B6%E5%AE%89%E8%A3%85%E5%91%BD%E4%BB%A4.png)

在 AI Skills 官网、skills.sh 或 ClawHub 页面复制安装命令，优先使用官方 CLI，避免手动拼接参数。

### 4. 执行安装命令

![在终端执行 AI Skills 安装命令](https://raw.githubusercontent.com/allinherog-star/aiskillsguides/HEAD/guides/images/ai-skills-site-readme/step/4%E3%80%81%E5%AE%89%E8%A3%85%E5%91%BD%E4%BB%A42.png)

回到终端执行安装命令，CLI 会写入 AISKILLS_API_KEY，并调用下游 skills add 完成技能安装。

### 5. 成功获取技能

![AI Skills 技能安装成功界面](https://raw.githubusercontent.com/allinherog-star/aiskillsguides/HEAD/guides/images/ai-skills-site-readme/step/5%E3%80%81%E6%88%90%E5%8A%9Fget%E6%8A%80%E8%83%BD.png)

安装成功后，你会在 agent 的技能列表里看到对应 Skill，可以直接调用并复用到工作流中。

## 当前技能：software-dev-cost-dashboard

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
