---
name: ai-kpi-dashboard-design
description: "KPI 看板设计助手适合technical、产品、市场营销、software在用户提出“看板讲清 KPI 吗”这类问题，需要快速拆解目标、判断重点并形成可执行结果时使用，帮助基于输入材料生成销售策略、沟通素材、跟进计划。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取API Key，用于运行时技能调用。"
---

# ai-kpi-dashboard-design KPI 看板设计助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

KPI 看板设计助手用于回答「看板讲清 KPI 吗」、性能诊断、网站质量、体验指标，适合technical、产品、市场营销、software在明确业务目标、内容材料或分析对象后调用。
它会结合视觉 brief 或截图说明、粘贴视觉 brief、截图说明、品牌规范、页面问题、平台规格或修改…等输入，整理关键上下文，并输出销售策略、沟通素材、跟进计划，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提出“看板讲清 KPI 吗”这类问题，需要快速拆解目标、判断重点并形成可执行结果
- technical、产品、市场营销、software需要围绕KPI 看板设计助手生成销售策略、沟通素材、跟进计划
- 用户已经准备了审查目标（说明要检查的版面、可读性、品牌一致性、转化目标或交付标准。）、使用场景（说明视觉素材面向的平台、受众、设备、活动或评审场景。）、页面或素材链接（填写公开可访问的页面、素材、设计稿预览或参考链接；受限内容请改为上传。），希望整理成可执行的分析或优化结果
- 用户需要把KPI 看板设计助手相关材料转成清晰结论、优先级和下一步动作

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**基础调用**

```bash
python3 scripts/run.py --params '{}'
```

**带常用参数调用**

```bash
python3 scripts/run.py --params '{"goal":"审查目标"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `goal` | string | 否 | - | 说明要检查的版面、可读性、品牌一致性、转化目标或交付标准 |
| `audience` | string | 否 | - | 说明视觉素材面向的平台、受众、设备、活动或评审场景 |
| `materialUrl` | string | 否 | - | 填写公开可访问的页面、素材、设计稿预览或参考链接；受限内容请改为上传；需要传可访问的完整 URL |
| `materialFile` | string | 否 | - | 上传截图、图片、演示稿、品牌规范、产品图或视觉参考文件 |
| `materialText` | string | 否 | - | 粘贴视觉 brief、截图说明、品牌规范、页面问题、平台规格或修改目标 |
| `brandRequirements` | string | 否 | - | 补充品牌规范、尺寸比例、平台限制、不可改动元素、无障碍要求或人工复核重点 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数；如果参数里包含链接字段，请传完整、可访问的 URL。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"goal":"审查目标"}'
```

等价的 `--params` JSON：

```json
{
  "goal": "审查目标"
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

- 销售策略、沟通素材、跟进计划：围绕用户目标整理可直接阅读、复盘或交付的核心结果。
- 输入材料解读：结合审查目标（说明要检查的版面、可读性、品牌一致性、转化目标或交付标准。）、使用场景（说明视觉素材面向的平台、受众、设备、活动或评审场景。）、页面或素材链接（填写公开可访问的页面、素材、设计稿预览或参考链接；受限内容请改为上传。）提炼关键上下文和判断依据。
- 下一步动作：给出优先级、执行建议或可继续加工的内容框架。

### 结果使用建议

- 先判断输出是否回答了用户关于「KPI 看板设计助手」的核心问题。
- 再检查结果是否覆盖销售策略、沟通素材、跟进计划，以及是否给出明确下一步动作。
- 如果输入材料较少，建议让用户补充目标、受众、限制条件或原始材料后再运行。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
