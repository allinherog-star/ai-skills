---
name: bilibili-sentiment-dashboard
description: "B站短视频运营增长助手适合内容创作者、运营、品牌方、电商在用户提供了 B 站视频链接时使用，帮助基于输入材料生成评论情绪和讨论结构、观众画像和兴趣信号、内容与互动建议。"
requiredEnvVars:
  - name: AISKILLS_API_KEY
    description: "从 AI Skills 官网 https://ai-skills.ai 获取的 API Key，用于运行导出的技能调用。"
---

# bilibili-sentiment-dashboard B站短视频运营增长助手

[快速开始](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

[更多技能](https://ai-skills.ai)

### 概述

B站短视频运营增长助手用于回答「B站短视频怎么运营」、分析视频评论、看观众情绪、看讨论重点，适合内容创作者、运营、品牌方、电商在明确业务目标、内容材料或分析对象后调用。
它会结合视频/笔记链接、粘贴B站分享链接等输入，整理关键上下文，并输出评论情绪和讨论结构、观众画像和兴趣信号、内容与互动建议，便于继续执行、复盘或交付。

### 什么时候使用

**适用场景**

- 用户提供了 B 站视频链接
- 用户想做评论诊断并获得后续运营建议

### 调用方式

运行脚本后会自动完成三步：解析分享链接、创建分析任务、轮询直到任务完成。

### 命令示例

**分析 B 站视频评论**

```bash
python3 scripts/run.py --params '{"link":"https://www.bilibili.com/video/BV1xx411c7mD"}'
```

### 参数说明

| 参数 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| `videoUrl` | string | 是 | - | 粘贴B站分享链接 |

完整机器可读参数结构见 `references/form-schema.json`。

### 参数取值参考

当前技能没有需要额外查表的分类参数。

### 支持的输入格式

粘贴B站分享链接或 BV 号，以下格式都可以直接尝试：

- `https://www.bilibili.com/video/BV1GJ411x7h7`
- `https://b23.tv/BV1GJ411x7h7`
- `BV1GJ411x7h7`

### 示例请求

下面的示例参数直接传给 `scripts/run.py` 即可，脚本会自动完成解析链接、创建任务、轮询结果。

```bash
python3 scripts/run.py --params '{"link":"https://www.bilibili.com/video/BV1xx411c7mD"}'
```

等价的 `--params` JSON：

```json
{
  "link": "https://www.bilibili.com/video/BV1xx411c7mD"
}
```

### 返回结果示例

```json
{
  "success": true,
  "data": {
    "task": {
      "id": "task_demo_123",
      "platform": "bilibili",
      "contentId": "7505866362912425270",
      "contentTitle": "B 站运营拆解示例",
      "status": "completed",
      "progress": 100,
      "progressMessage": "分析完成",
      "result": {
        "summary": {
          "analyzedComments": 168,
          "timeRange": {
            "start": "2026-04-23T00:00:00.000Z",
            "end": "2026-04-24T00:00:00.000Z"
          },
          "platform": "bilibili",
          "contentId": "7505866362912425270",
          "contentTitle": "B 站运营拆解示例",
          "analyzedAt": "2026-04-24T11:35:00.000Z"
        },
        "aiInsights": {
          "summary": "评论区更在意细节证明、对比实验和补充资料，适合继续加强知识密度与长尾问题回应。",
          "sentiment": {
            "trend": "mixed",
            "label": "正向为主",
            "riskLevel": "low"
          },
          "operationAdvice": [
            {
              "category": "content",
              "priority": "P1",
              "title": "补证据链",
              "detail": "下一版补充数据来源和对比图，回应评论区对细节证明的需求。",
              "reason": "B 站用户更关注论证过程，补证据链能显著提升信任感。"
            }
          ]
        },
        "labeledComments": [
          {
            "id": "comment_1",
            "content": "能不能把你提到的对比数据和资料出处也放出来？",
            "sentiment": "positive",
            "likes": 26
          }
        ]
      }
    }
  }
}
```

### 交付内容

- 评论区整体结论：帮助快速判断内容口碑、讨论焦点和潜在舆情风险。
- 用户反馈拆解：提炼高频诉求、典型评论、情绪倾向和用户画像线索。
- 运营动作建议：给出后续内容优化、评论回复、系列选题或转化承接方向。

### 结果使用建议

- 先看整体情绪和一句话总结，判断内容反馈是正向、争议、观望还是存在风险。
- 再看高频评论和用户画像，识别用户真正关心的问题、购买/互动意图和内容缺口。
- 最后把运营建议转成下一条内容选题、评论回复策略或私域承接动作。

### 运行前准备

- `AISKILLS_BASE_URL`：默认 `https://ai-skills.ai`
- `AISKILLS_API_KEY`：必填，用于认证调用
- `AISKILLS_TENANT_ID`：默认 `default`
