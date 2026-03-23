# Form Schema

本文件描述 `douyin-realtime-hot-rise` 技能的输入参数规范。

## 参数列表

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `order` | string | `"rank"` | 排序方式，控制热点列表的排列顺序 |
| `tag` | string | `null` | 热点分类，用于筛选特定垂直领域的话题 |
| `keyword` | string | `null` | 搜索关键词，在热点标题和描述中进行过滤匹配 |

## order 参数详解

```json
{
  "type": "string",
  "enum": ["rank", "rank_diff"],
  "default": "rank"
}
```

| 枚举值 | 显示名称 | 说明 |
|--------|----------|------|
| `rank` | 热度排序 | 按话题当前的绝对热度值排序，适合寻找已经验证的高流量话题 |
| `rank_diff` | 变化排序 | 按话题排名的变化幅度（上升速度）排序，适合寻找正在爆发的新兴话题 |

- **热度排序（rank）**：适合寻找"已被验证"的高流量话题，风险低但竞争激烈
- **变化排序（rank_diff）**：适合寻找"正在爆发"的上升话题，可能有先发红利但热度持续性不确定

## tag 参数详解

```json
{
  "type": "string",
  "x-component": "CategorySelect"
}
```

- 用于筛选特定垂直分类的热点话题
- `x-component` 为 `CategorySelect`，表示由前端组件提供分类选择器
- 常见分类包括：美妆、美食、科技、游戏、娱乐、教育、健身、旅行、时尚等
- 若不传或为空，则返回全部分类的热点

## keyword 参数详解

```json
{
  "type": "string"
}
```

- 在热点话题的标题、描述等字段中进行关键词匹配过滤
- 支持模糊匹配（包含关系）
- 若不传或为空，则不过滤关键词，返回全部匹配 `tag` 条件的结果
- 典型使用场景：用户指定了一个内容方向（如"减脂"），需要缩小范围

## 完整 Schema（JSON Schema 格式）

```json
{
  "type": "object",
  "properties": {
    "order": {
      "type": "string",
      "title": "排序方式",
      "enum": ["rank", "rank_diff"],
      "enumNames": ["热度排序", "变化排序"],
      "default": "rank"
    },
    "tag": {
      "type": "string",
      "title": "热点分类",
      "x-component": "CategorySelect"
    },
    "keyword": {
      "type": "string",
      "title": "搜索词"
    }
  }
}
```
