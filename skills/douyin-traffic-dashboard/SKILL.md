---
name: douyin-traffic-dashboard
description: "抖音流量分配大盘适合内容创作者、运营、电商、营销在用户想知道抖音流量正在流向哪些方向时使用，帮助基于输入材料生成流量分布、分类层级结构、可用于内容布局的平台方向信号。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key，用于运行导出的技能调用。"
---

# douyin-traffic-dashboard 抖音流量分配大盘

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

抖音流量分配大盘用于回答「抖音平台流量在哪」、看流量分配、看分类占比、做赛道判断，适合内容创作者、运营、电商、营销在明确业务目标、内容材料或分析对象后调用。
它会结合用户输入的业务背景和目标等输入，整理关键上下文，并输出流量分布、分类层级结构、可用于内容布局的平台方向信号，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户想知道抖音流量正在流向哪些方向
- 用户想看哪些内容分类正在获得更多流量
- 用户需要平台级方向判断

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
    "updateTime": "2026-04-24T11:30:00.000Z"
  },
  "meta": {
    "executionTime": 842,
    "cached": false
  }
}
```

### 交付内容

- 平台流量分布：展示不同内容分类的热度占比和热点数量。
- 赛道判断线索：帮助判断当前哪些内容方向更值得投入。
- 分类参考：可继续用于抖音热点筛选、内容布局和运营复盘。

### 结果使用建议

- 先看流量占比和热点数量高的分类，再结合账号能力判断是否值得投入。
- 适合做赛道层面的内容布局，不直接替代具体选题判断。
- 可把分类结果继续用于筛选上升热点或规划内容矩阵。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
