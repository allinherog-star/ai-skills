---
name: xhs-viral-copywriter
description: "爆款文案助手. Use this skill when the user asks for 爆款文案助手. Do not use when the user goal does not match this skill description."
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key。运行脚本时会随请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数，不含用户对话上下文）"
    - "X-API-Key（认证密钥）"
  warning: "此技能会调用 AI Skills API。启用前请确认您信任 ai-skills.ai 的数据安全政策，并使用可随时撤销的 API Key。"
---

# xhs-viral-copywriter 爆款文案助手

快速开始：<https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B>
更多技能：<https://ai-skills.ai>

### 概述

爆款文案助手

### 什么时候使用

**适用场景**

- the user asks for 爆款文案助手

**不要用于**

- the user goal does not match this skill description

**相邻技能选择**

- compare neighboring skill cards before execution

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**按必填参数调用**

```bash
python3 scripts/run.py --params '{"topic":"主题/产品"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `topic` | string | 是 | - | 主题/产品 |
| `audience` | string | 否 | - | 目标人群 |
| `sellingPoint` | string | 否 | - | 核心卖点 |
| `accountPersona` | string | 否 | - | 账号人设 |
| `noteType` | string | 否 | `种草` | 笔记类型；可选值：`种草`、`测评`、`攻略`、`避坑`、`清单`、`复盘` |
| `tone` | string | 否 | `真实具体` | 语气；可选值：`真实具体`、`轻松口语`、`专业测评`、`强反差`、`温柔陪伴` |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"topic":"主题/产品"}'
```

等价的 `--params` JSON：

```json
{
  "topic": "主题/产品"
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

### 结果重点看什么

- `data`：技能主返回结果，先看核心业务字段是否符合预期。
- `meta.executionTime`：本次执行耗时，便于排查慢请求。
- `meta.cached`：是否命中缓存，帮助判断结果新鲜度。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `xhs-viral-copywriter` 对应的 AI Skills API/工作流。
