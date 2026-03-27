# API Schema

本文件描述 `douyin-realtime-hot-rise` 技能调用后端 API 的接口规范。

## 接口概述

| 项目 | 说明 |
|------|------|
| **Method** | `POST` |
| **Path** | `/api/v1/execute` |
| **认证方式** | API Key（`X-API-Key` header） + 租户 ID（`X-Tenant-Id` header） |
| **数据格式** | JSON |

## 请求头

| Header | 说明 | 示例 |
|--------|------|------|
| `Content-Type` | 请求体类型，固定为 `application/json` | `application/json` |
| `X-API-Key` | API 密钥，从 `AISKILLS_API_KEY` 环境变量获取 | `sk-xxxxxxxx` |
| `X-Tenant-Id` | 租户 ID，从 `AISKILLS_TENANT_ID` 环境变量获取，默认 `default` | `default` |

## 请求体

```json
{
  "skillId": "douyin-realtime-hot-rise",
  "params": {
    "order": "rank",
    "tag": "美妆",
    "keyword": "春季"
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `skillId` | string | 是 | 固定为 `douyin-realtime-hot-rise`，标识调用的技能 |
| `params` | object | 是 | 技能执行参数，对应 `formSchema` 中的字段 |
| `params.order` | string | 否 | 排序方式：`rank`（热度，默认）或 `rank_diff`（变化） |
| `params.tag` | string | 否 | 热点分类筛选 |
| `params.keyword` | string | 否 | 搜索关键词过滤 |

## 响应结构

### 成功响应

```json
{
  "success": true,
  "data": {
    "skillId": "douyin-realtime-hot-rise",
    "result": {
      "items": [
        {
          "title": "#春季护肤",
          "rank": 12,
          "rank_diff": 8,
          "tag": "美妆",
          "hot_value": 95234,
          "desc": "春季护肤误区大盘点"
        }
      ],
      "total": 50,
      "page": 1,
      "page_size": 50
    }
  }
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `success` | boolean | 是否成功 |
| `data.skillId` | string | 技能 ID |
| `data.result.items` | array | 热点话题列表 |
| `data.result.items[].title` | string | 话题标题/标签 |
| `data.result.items[].rank` | number | 当前热度排名 |
| `data.result.items[].rank_diff` | number | 排名变化幅度（正数=上升） |
| `data.result.items[].tag` | string | 话题分类 |
| `data.result.items[].hot_value` | number | 热度值（可选） |
| `data.result.items[].desc` | string | 话题描述（可选） |
| `data.result.total` | number | 符合条件的热点总数 |
| `data.result.page` | number | 当前页码 |
| `data.result.page_size` | number | 每页数量 |

### 错误响应

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
| `HTTP_422` | 参数格式错误 |
| `HTTP_500` | 服务端内部错误 |
| `HTTP_503` | 服务不可用（上游 TikHub API 异常） |

## 执行流程

1. 从环境变量读取 `AISKILLS_BASE_URL`、`AISKILLS_API_KEY`、`AISKILLS_TENANT_ID`
2. 构造请求体 `{ skillId: "douyin-realtime-hot-rise", params: {...} }`
3. 发送 `POST` 请求到 `${AISKILLS_BASE_URL}/api/v1/execute`
4. 解析响应中的 `data.result.items`，按结论 -> 证据 -> 建议结构组织输出
5. 若响应 `success` 为 `false`，输出错误信息并终止

## 实际调用示例

```bash
# 环境变量设置
export AISKILLS_BASE_URL="https://ai-skills.ai"
export AISKILLS_API_KEY="sk-your-api-key"
export AISKILLS_TENANT_ID="default"

# 调用示例（热度排序）
python3 scripts/run.py --params '{"order":"rank"}'

# 调用示例（变化排序 + 关键词过滤）
python3 scripts/run.py --params '{"order":"rank_diff","keyword":"减脂"}'
```
