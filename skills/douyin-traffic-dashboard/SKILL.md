---
name: douyin-traffic-dashboard
description: "抖音流量分配大盘. Use this skill when the user asks where Douyin traffic is going; the user asks which categories are getting more traffic; the user wants a platform-level directional read. Do not use when the user wants specific rising topics; the user wants a real-time hot list."
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

# douyin-traffic-dashboard 抖音流量分配大盘

官网入口：<https://ai-skills.ai>
快速开始：<https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B>

### 概述

抖音流量分配大盘

### 什么时候使用

**适用场景**

- the user asks where Douyin traffic is going
- the user asks which categories are getting more traffic
- the user wants a platform-level directional read

**典型用户提问**

- 抖音平台流量在哪？
- 最近流量更多流向了哪些内容分类？
- 现在哪些赛道值得加大内容投入？

**不要用于**

- the user wants specific rising topics
- the user wants a real-time hot list
- the user wants creators or benchmark accounts

**相邻技能选择**

- use `douyin-realtime-hot-rise` for rising topic discovery
- use `douyin-hotlist-overall` for real-time hot topics

### 调用方式

通过导出的 Python runner 直接调用 AI Skills API：

### 命令示例

**查看全站流量分布**

```bash
python3 scripts/run.py --params '{}'
```

### 参数说明

当前技能无需额外参数，可直接使用：

```bash
python3 scripts/run.py --params '{}'
```

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

当前技能直接接收 JSON 参数，不涉及分享链接解析。

### 示例请求

下面的示例参数可直接传给 `scripts/run.py`，runner 会把它们发送给 AI Skills API。

```bash
python3 scripts/run.py --params '{}'
```

等价的 `--params` JSON：

```json
{}
```

### 返回结果示例

```json
{
  "success": true,
  "data": {
    "categories": [
      {
        "label": "美食",
        "value": "9000",
        "hotCount": 128,
        "percentage": 14,
        "icon": "utensils",
        "description": "探店、烹饪、美食测评",
        "group": "life"
      },
      {
        "label": "体育",
        "value": "5000",
        "hotCount": 96,
        "percentage": 11,
        "icon": "dumbbell",
        "description": "赛事、运动员、训练内容",
        "group": "knowledge"
      }
    ],
    "total": 32,
    "timeRange": "抖音平台实时流量占比",
    "updateTime": "2026-04-24T11:30:00.000Z"
  },
  "meta": {
    "executionTime": 842,
    "cached": false
  }
}
```

### 结果重点看什么

- `data.categories`：平台流量分类列表，重点看 `percentage` 和 `hotCount`。
- `category.value`：分类编码，可直接复用到其它技能的筛选参数。
- `data.updateTime`：流量分布快照时间。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`

### 备注

当前导出包由 AI Skills 站点目录自动生成，运行时后端仍然指向 `douyin-traffic-dashboard` 对应的 AI Skills API/工作流。
