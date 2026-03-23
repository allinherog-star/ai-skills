# API Schema

本文件描述 `unified-comment-analysis` 技能调用后端 API 的接口规范，包含 3 个端点。

## 接口概述

| 端点 | Method | Path | 说明 |
|------|--------|------|------|
| parse-link | `POST` | `/api/v1/comment-analysis/parse-link` | 解析分享链接，提取平台和内容 ID |
| create-task | `POST` | `/api/v1/comment-analysis/tasks` | 创建舆情分析任务 |
| get-task | `GET` | `/api/v1/comment-analysis/tasks/:id` | 查询任务状态（轮询） |

认证方式：API Key（`X-API-Key` header）+ 租户 ID（`X-Tenant-Id` header）

---

## 端点 1: parse-link

解析分享链接，提取平台类型、内容 ID、视频/笔记标题等信息。

### 请求

```http
POST /api/v1/comment-analysis/parse-link
Content-Type: application/json
X-API-Key: <AISKILLS_API_KEY>
X-Tenant-Id: <AISKILLS_TENANT_ID>

{
  "input": "https://www.douyin.com/video/7381234567890123456",
  "platform": "douyin"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `input` | string | 是 | 分享链接 |
| `platform` | string | 否 | 平台类型（`douyin`/`xhs`/`bilibili`/`kuaishou`），若不提供则自动识别 |

### 成功响应

```json
{
  "success": true,
  "data": {
    "platform": "douyin",
    "contentId": "7381234567890123456",
    "contentTitle": "视频标题",
    "sourceUrl": "https://www.douyin.com/video/7381234567890123456"
  }
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `platform` | string | 识别出的平台类型 |
| `contentId` | string | 内容 ID（视频/笔记/动态的唯一标识） |
| `contentTitle` | string | 内容标题（可为空） |
| `sourceUrl` | string | 标准化后的原始链接 |

---

## 端点 2: create-task

提交舆情分析任务，获取任务 ID。

### 请求

```http
POST /api/v1/comment-analysis/tasks
Content-Type: application/json
X-API-Key: <AISKILLS_API_KEY>
X-Tenant-Id: <AISKILLS_TENANT_ID>

{
  "platform": "douyin",
  "contentId": "7381234567890123456",
  "contentTitle": "视频标题",
  "options": {
    "sourceUrl": "https://www.douyin.com/video/7381234567890123456"
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `platform` | string | 是 | 平台类型 |
| `contentId` | string | 是 | 内容 ID |
| `contentTitle` | string | 否 | 内容标题 |
| `options.sourceUrl` | string | 否 | 原始链接 |

### 成功响应

```json
{
  "success": true,
  "data": {
    "task": {
      "id": "task_abc123"
    }
  }
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `task.id` | string | 任务唯一标识，用于后续轮询 |

---

## 端点 3: get-task

轮询任务状态，直至任务完成或失败。

### 请求

```http
GET /api/v1/comment-analysis/tasks/:id
X-API-Key: <AISKILLS_API_KEY>
X-Tenant-Id: <AISKILLS_TENANT_ID>
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `:id` | string | 任务 ID（来自 create-task 响应） |

### 成功响应（任务进行中）

```json
{
  "success": true,
  "data": {
    "task": {
      "id": "task_abc123",
      "status": "processing"
    }
  }
}
```

| 任务状态 | 说明 |
|----------|------|
| `pending` | 任务等待中 |
| `processing` | 任务进行中 |
| `completed` | 任务已完成（终止轮询） |
| `failed` | 任务失败（终止轮询） |

### 成功响应（任务完成）

```json
{
  "success": true,
  "data": {
    "task": {
      "id": "task_abc123",
      "status": "completed",
      "result": {
        "platform": "douyin",
        "contentId": "7381234567890123456",
        "contentTitle": "视频标题",
        "sentiment": {
          "positive": 68,
          "neutral": 22,
          "negative": 10
        },
        "sentimentLabel": "positive",
        "userProfile": {
          "ageDistribution": {"18-25": 62, "26-35": 28, "36+": 10},
          "genderDistribution": {"female": 72, "male": 28},
          "topKeywords": ["春季穿搭", "平价好物", "学生党"],
          "regionDistribution": {"广东": 18, "浙江": 14, "江苏": 11}
        },
        "conversionPotential": 78,
        "engagementMetrics": {
          "likes": 23000,
          "comments": 1200,
          "shares": 890,
          "collects": 8600
        },
        "suggestions": [
          "视频后半段加入正向引导，降低负面情绪扩散风险",
          "结合学生党平价好物标签制作后续内容，延续热度",
          "在评论区置顶学生党专属优惠引导评论互动"
        ]
      }
    }
  }
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `result.platform` | string | 平台类型 |
| `result.contentId` | string | 内容 ID |
| `result.contentTitle` | string | 内容标题 |
| `result.sentiment` | object | 情感分析结果（百分比） |
| `result.sentimentLabel` | string | 情感标签：`positive` / `neutral` / `negative` |
| `result.userProfile` | object | 用户画像 |
| `result.conversionPotential` | number | 转化潜力评分（0-100） |
| `result.engagementMetrics` | object | 互动指标 |
| `result.suggestions` | array | 运营建议列表 |

---

## 错误响应

所有端点共享相同的错误格式：

```json
{
  "success": false,
  "error": {
    "code": "HTTP_401",
    "message": "Invalid API key"
  }
}
```

| 错误码 | 说明 |
|--------|------|
| `HTTP_401` | API Key 无效或缺失 |
| `HTTP_403` | 无权访问该技能 |
| `HTTP_422` | 参数格式错误（如链接无法识别） |
| `HTTP_500` | 服务端内部错误 |
| `HTTP_503` | 上游服务不可用 |

---

## 执行流程

`scripts/run.py` 内部完整实现以下流程：

1. **环境准备**：从环境变量读取 `AISKILLS_BASE_URL`、`AISKILLS_API_KEY`、`AISKILLS_TENANT_ID`
2. **Step 1 - parse-link**：POST 请求 `/api/v1/comment-analysis/parse-link`，获取 `platform` 和 `contentId`
3. **Step 2 - create-task**：POST 请求 `/api/v1/comment-analysis/tasks`，获取 `task.id`
4. **Step 3 - get-task**：轮询 GET `/api/v1/comment-analysis/tasks/:id`
   - 每 2 秒轮询一次
   - 最多重试 60 次（超时 120 秒）
   - 状态为 `completed` 或 `failed` 时终止轮询
5. **结果输出**：将最终响应（JSON 格式）打印到 stdout

## 实际调用示例

```bash
# 环境变量设置
export AISKILLS_BASE_URL="https://ai-skills.ai"
export AISKILLS_API_KEY="sk-your-api-key"
export AISKILLS_TENANT_ID="default"

# 调用示例（自动识别平台）
python3 scripts/run.py --params '{"link":"https://www.douyin.com/video/7381234567890123456"}'

# 调用示例（指定平台）
python3 scripts/run.py --params '{"link":"https://www.xiaohongshu.com/explore/67890abcdef","platform":"xhs"}'
```
