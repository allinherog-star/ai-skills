---
name: douyin-traffic-dashboard
description: "抖音流量分配大盘。当用户提到抖音流量分配、流量大盘、流量趋势、抖音运营数据、视频流量分析时，务必使用此技能。适用于运营人员分析抖音账号流量分配、内容创作者了解视频流量来源。通过 TikHub API 获取抖音流量分布数据。"
---

# douyin-traffic-dashboard

## 概述

此技能帮助用户获取抖音流量分配大盘数据，分析视频/账号的流量来源与分布。

## API 调用

**Endpoint**: `POST /api/v1/douyin/billboard/fetch_hot_rise_list`
**Provider**: TikHub
**认证**: `X-API-Key` header
**聚合模式**: `traffic-distribution`

### 请求参数

此接口无额外参数，返回抖音平台整体流量分布数据。

## 执行流程

1. **构建请求**：使用 `aggregateMode: traffic-distribution` 参数调用 TikHub API
2. **调用 API**：通过 Gateway `/api/execute` 转发至 TikHub
3. **解析响应**：提取流量分布数据（各来源占比、趋势等）
4. **格式化输出**：以结构化文本或图表展示流量大盘

## 输出格式

```
# 抖音流量分配大盘

**更新时间**: YYYY-MM-DD HH:mm

## 流量来源分布

| 来源类型 | 占比 | 趋势 |
|----------|------|------|
| 推荐feed | 45%  | ↑3%  |
| 关注 | 20%  | ↓1%  |
| 搜索 | 15%  | ↑5%  |
| 同城 | 8%   | →    |
| 其他 | 12%  | ↓2%  |

## 关键洞察

- 推荐feed流量占比最高，达 45%
- 搜索流量呈上升趋势（+5%），建议优化关键词
- ...
```

## 错误处理

- **401 Unauthorized**: 检查 API Key 是否有效
- **429 Rate Limit**: 请求过于频繁，提示用户稍后重试
- **500/502/503**: TikHub 服务异常，记录错误并返回友好提示
