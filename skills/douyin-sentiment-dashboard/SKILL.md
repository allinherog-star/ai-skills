---
name: douyin-sentiment-dashboard
description: "抖音短视频运营增长大盘"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 https://ai-skills.ai 获取的 API Key。运行脚本时会随请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "params（技能参数，含用户提供的分享链接）"
    - "X-API-Key（认证密钥）"
  warning: "此技能会将用户提供的分享链接发送至 ai-skills.ai 进行解析和评论分析。启用前请确认您信任该平台的数据安全政策。"
---

# AI Skills 技能库：为每一个场景做真正有价值的AI技能库

> 大多数人用 AI 还停在「问一句答一句」。AI Skills（[ai-skills.ai](https://ai-skills.ai/)）想换一种姿势：把 AI 能力拆成一条条能直接执行的 Skill，像查字典一样调出来用。无论你从 AI Skills 官网、skills.sh 还是 ClawHub 进入，先按这 5 步完成接入，再继续看当前技能说明。

![AI Skills 官网场景导览图](./assets/marketplace/content-01.webp)

## 5 步接入 AI Skills

### 1. 扫码登录

![扫码登录 AI Skills 账号](./assets/marketplace/1-scan-login.png)

先在 AI Skills 官网完成扫码登录，确保后续 API Key、安装命令和技能调用都绑定到同一个账号。

### 2. 申请 API Key

![在 AI Skills 站点申请 API Key](./assets/marketplace/2-request-api-key.png)

登录后进入 API Key 页面申请密钥，后续 CLI 安装和运行技能都会读取 AISKILLS_API_KEY。

### 3. 复制安装命令

![复制 AI Skills 技能安装命令](./assets/marketplace/3-copy-install-command.png)

在 AI Skills 官网、skills.sh 或 ClawHub 页面复制安装命令，优先使用官方 CLI，避免手动拼接参数。

### 4. 执行安装命令

![在终端执行 AI Skills 安装命令](./assets/marketplace/4-run-install-command.png)

回到终端执行安装命令，CLI 会写入 AISKILLS_API_KEY，并调用下游 skills add 完成技能安装。

### 5. 成功获取技能

![AI Skills 技能安装成功界面](./assets/marketplace/5-install-success.png)

安装成功后，你会在 agent 的技能列表里看到对应 Skill，可以直接调用并复用到工作流中。

## 当前技能：douyin-sentiment-dashboard

### 概述

抖音短视频运营增长大盘

### 调用方式

运行脚本后会自动完成三步：解析分享链接、创建分析任务、轮询直到任务完成。

### 命令示例

**按必填参数调用**

```bash
python3 scripts/run.py --params '{"link":"https://v.douyin.com/xxxxx"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `link` | string | 是 | - | 分享链接；需要传可访问的完整 URL |

完整机器可读参数结构见 `references/form-schema.json`。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `douyin-sentiment-dashboard` 对应的 AI Skills API/工作流。
