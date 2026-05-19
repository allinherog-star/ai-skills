---
name: lark-task
description: "业务诊断助手. Use this skill when the user asks for 业务诊断助手. Do not use when the user goal does not match this skill description."
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

# lark-task 业务诊断助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

业务诊断助手

### 什么时候使用

**适用场景**

- the user asks for 业务诊断助手

**不要用于**

- the user goal does not match this skill description

**相邻技能选择**

- compare neighboring skill cards before execution

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**基础调用**

```bash
python3 scripts/run.py --params '{}'
```

**带常用参数调用**

```bash
python3 scripts/run.py --params '{"goal":"推进目标"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `goal` | string | 否 | - | 例如清理逾期任务、明确责任人、准备周会或形成交接清单 |
| `audience` | string | 否 | - | 例如项目负责人、执行成员、管理者、客户成功团队或外部协作方 |
| `materialUrl` | string | 否 | - | 填写飞书任务或项目链接，并补充链接中可见的任务摘要；系统不会自动打开链接；需要传可访问的完整 URL |
| `reviewDepth` | string | 否 | `标准诊断` | 选择快速梳理、标准复盘或深度诊断；可选值：`快速体检`、`标准诊断`、`深度改稿` |
| `materialFile` | string | 否 | - | 上传任务导出、截图 OCR 文本、项目周报、任务清单或协作文档 |
| `materialText` | string | 否 | - | 粘贴任务标题、描述、评论、负责人、截止时间、状态变化或导出的任务清单 |
| `targetPlatform` | string | 否 | - | 说明报告用于飞书同步、项目周会、管理层汇报还是跨团队交接 |
| `brandRequirements` | string | 否 | - | 补充团队术语、保密要求、表达语气、格式规范或对外口径 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"goal":"推进目标"}'
```

等价的 `--params` JSON：

```json
{
  "goal": "推进目标"
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

### 结构化结果约定

异步执行完成时，运行时必须在产物目录根部写出 `result.json`，并使用 `ResultEnvelope` 结构：

- `items` 是预览导航的唯一来源；默认只写一个主结果 `item`。
- `artifacts` 是可下载产物清单，不会自动变成预览 Tab。
- `item.artifactIds` 或 `item.artifacts` 只表示某个结果项需要引用这些文件进行展示。
- 多结构预览必须由技能在 `items` 中显式声明多个结果项，必要时使用 `presentation.mode: "tabs"`。

### 结果重点看什么

- `data`：技能主返回结果，先看核心业务字段是否符合预期。
- `meta.executionTime`：本次执行耗时，便于排查慢请求。
- `meta.cached`：是否命中缓存，帮助判断结果新鲜度。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `lark-task` 对应的 AI Skills API/工作流。
