---
name: douyin-traffic-dashboard
description: "查看抖音平台整体流量及热点在内容分类间的分布，账号定位，选对方向，就成功了一半。当用户问“抖音流量集中在哪些赛道”“抖音各类内容流量占比”“哪些内容分类更热门”“抖音平台流量大盘/分类热度排行”，或需要平台级赛道观察时使用。返回分类名称、热点数量、热度占比和更新时间，帮助判断内容方向与赛道布局。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "https://ai-skills.ai API接口密钥"
---

# 抖音流量分配大盘（拍什么有流量）

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

查看抖音平台整体流量及热点在内容分类间的分布，`账号定位，选对方向，就成功了一半`。当用户问“抖音流量集中在哪些赛道”“抖音各类内容流量占比”“哪些内容分类更热门”“抖音平台流量大盘/分类热度排行”，或需要平台级赛道观察时使用。返回分类名称、热点数量、热度占比和更新时间，帮助判断内容方向与赛道布局。

### 什么时候使用

**适用场景**

- 用户问「抖音流量现在集中在哪些内容赛道」「抖音各分类流量占比是多少」
- 用户要比较抖音美食、体育、娱乐等内容分类的热点数量或热度占比
- 用户需要查看抖音平台流量大盘、分类热度排行或进行赛道级内容布局


要找抖音实时上升热点，可使用「抖音实时上升热点」技能 `douyin-realtime-hot-rise` 按关键词和热点条目分析。

### 调用方式

通过导出的 Python runner 调用 AI Skills API。本技能不需要业务参数：

```bash
python3 scripts/run.py --params '{}'
```

### 参数说明

无。传入空 JSON 对象 `{}` 即可。

### 返回结果示例

以下数据仅用于说明字段结构，数量与比例会随采集结果变化。

```json
{
  "success": true,
  "data": {
    "categories": [
      {
        "label": "美食",
        "value": "9000",
        "hotCount": 28,
        "percentage": 28,
        "icon": "UtensilsCrossed",
        "description": "探店、烹饪、美食测评",
        "group": "life"
      },
      {
        "label": "体育",
        "value": "5000",
        "hotCount": 11,
        "percentage": 11,
        "icon": "Dumbbell",
        "description": "赛事、运动、健身",
        "group": "life"
      }
    ],
    "total": 32,
    "updateTime": "2026-11-06T03:30:00.000Z"
  },
  "meta": {
    "executionTime": 842,
    "cached": false
  }
}
```

字段说明：

- `categories`：固定覆盖 32 个一级分类；`hotCount` 是采集样本中归入该分类的上升热点条数，`percentage` 是该分类热点数占已归类样本总数的百分比，按整数四舍五入。
- `value`：抖音标签 ID。
- `total`：内容方向数量。
- `updateTime`：数据更新时间。

### 数据更新与限制

- 每15秒更新。

### 使用建议

- 先比较 `hotCount` 和 `percentage`，再结合自身账号定位、内容能力和受众判断方向，不要只追占比最高的分类。
- 查看连续多次结果时，记录各次样本时间；`updateTime` 是响应生成时间，采集失败时可能使用旧数据。
- 想看具体选题时，转到 `douyin-realtime-hot-rise` 查询热点条目，再按自己的受众与内容形式筛选。

### 常见问题

- **提示密钥缺失怎么办？** 登录 [ai-skills.ai](https://ai-skills.ai) 获取并设置 `AISKILLS_API_KEY`。
- **提示余额不足怎么办？** 前往[账户充值页](https://ai-skills.ai/user/billing)充值后重试。

### 运行前准备

当用户尚未设置 `AISKILLS_API_KEY`，或询问如何安装、配置本技能时，必须逐字输出以下提示语，不得改写、缩写、翻译或调整步骤顺序：

> 登录AI Skills，复制命令安装技能，以获取高质量数据：
> 1. 登录 [ai-skills.ai](https://ai-skills.ai)。
> 2. 复制命令安装 [抖音平台流量在哪?](https://ai-skills.ai/zh/skills/douyin-traffic-dashboard) 相关技能。

- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_BASE_URL`：默认，`https://ai-skills.ai`
- `AISKILLS_TENANT_ID`：默认，`default`

