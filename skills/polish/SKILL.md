---
name: polish
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

# polish 业务诊断助手

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
python3 scripts/run.py --params '{"goal":"精修目标"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `goal` | string | 否 | - | 说明希望提升的专业感、转化、理解效率、品牌一致性或展示效果 |
| `audience` | string | 否 | - | 说明目标用户、访问者、评审者或客户，以及他们最在意的体验 |
| `materialUrl` | string | 否 | - | 填写公开可访问的页面、原型、设计预览、作品集或参考链接；需要传可访问的完整 URL |
| `reviewDepth` | string | 否 | `标准诊断` | 选择快速 polish、标准精修建议或深度打磨清单；可选值：`快速体检`、`标准诊断`、`深度改稿` |
| `materialFile` | string | 否 | - | 支持 UI 截图、视觉稿、标注图、前后对比图、设计文档或 PDF |
| `materialText` | string | 否 | - | 粘贴界面说明、页面文案、设计目标、当前版本问题或希望重点精修的区域 |
| `targetPlatform` | string | 否 | - | 选择 Web、移动端、后台系统、营销页、社媒图、演示页或其它载体 |
| `brandRequirements` | string | 否 | - | 补充品牌规范、组件库、色彩/字体限制、客户要求和必须保留的信息 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"goal":"精修目标"}'
```

等价的 `--params` JSON：

```json
{
  "goal": "精修目标"
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

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `polish` 对应的 AI Skills API/工作流。
