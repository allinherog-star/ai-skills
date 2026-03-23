# Form Schema

本文件描述 `douyin-traffic-dashboard` 技能的输入参数规范。

## 参数列表

本技能 **无输入参数**，`formSchema` 为空对象 `{}`。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| （无） | - | - | 本技能无需任何参数，直接调用 API 获取抖音流量分配大盘数据 |

## 说明

`douyin-traffic-dashboard` 技能的 `formSchema` 配置如下：

```json
{
  "type": "object",
  "properties": {}
}
```

由于本技能无参数，用户无需提供任何输入，技能将直接调用 TikHub 抖音热榜上升数据接口（`/api/v1/douyin/billboard/fetch_hot_rise_list`），按 `traffic-distribution` 聚合模式返回当前抖音各内容分类的流量分配情况。

## 完整 Schema（JSON Schema 格式）

```json
{
  "type": "object",
  "properties": {}
}
```
