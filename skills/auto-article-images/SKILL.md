---
name: auto-article-images
description: "智能配图助手. Use this skill when the user asks for 智能配图助手. Do not use when the user goal does not match this skill description."
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网获取的 API Key。运行脚本时会随请求发送至 ai-skills.ai 服务器。"
security:
  thirdPartyDomain: ai-skills.ai
  dataSent:
    - "skillId（技能标识符）"
    - "params（技能参数，不含用户对话上下文）"
    - "X-API-Key（认证密钥）"
  warning: "此技能会调用 AI Skills API。启用前请确认您信任 ai-skills.ai 的数据安全政策，并使用可随时撤销的 API Key。"
---

# 当前技能：auto-article-images

官网入口：[AI Skills 官网](https://ai-skills.ai/)

### 概述

智能配图助手

### 什么时候使用

**适用场景**

- the user asks for 智能配图助手

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
python3 scripts/run.py --params '{"sourceText":"文章内容"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `sourceText` | string | 否 | - | 文章内容 |
| `sourceDocument` | string | 否 | - | 上传文章文件 |
| `title` | string | 否 | - | 标题 |
| `imageCount` | number | 否 | `4` | 正文配图数量 |
| `coverRatios` | array | 否 | `["2.35:1","1:1","16:9","3:4","9:16"]` | 封面比例；可选值：公众号头图（`2.35:1`）、方图（`1:1`）、横图（`16:9`）、小红书竖图（`3:4`）、短视频竖屏（`9:16`） |
| `publishPlatform` | string | 否 | `all` | 发布平台；可选值：全平台（`all`）、微信公众号（`wechat`）、小红书（`xhs`）、博客/官网（`blog`）、知乎（`zhihu`） |
| `style` | string | 否 | `clean-commercial` | 视觉风格；可选值：清爽商业（`clean-commercial`）、杂志摄影（`editorial-photo`）、柔和插画（`soft-illustration`）、科技图解（`tech-diagram`） |
| `brandRequirements` | string | 否 | - | 水印/品牌要求 |
| `watermarkMode` | string | 否 | `off` | 水印；可选值：不加水印（`off`）、右下角（`corner`）、角标 + 平铺（`both`） |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{"sourceText":"文章内容"}'
```

等价的 `--params` JSON：

```json
{
  "sourceText": "文章内容"
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

- `AISKILLS_BASE_URL`：默认使用 AI Skills 官方服务
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `auto-article-images` 对应的 AI Skills API/工作流。
