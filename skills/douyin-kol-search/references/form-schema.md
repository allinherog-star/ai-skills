# Form Schema

本文件描述 `douyin-kol-search` 技能的输入参数规范。

## 参数列表

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `keyword` | string | **必填** | - | 搜索词，用于匹配博主昵称、内容关键词或赛道名称 |
| `category` | string | 可选 | - | 内容分类，通过 CategorySelect 组件选择，用于精确定位细分赛道 |

## 说明

`douyin-kol-search` 技能的 `formSchema` 配置如下：

- **`keyword`（必填）**：用户必须提供搜索词才能调用此技能。搜索词可以是博主昵称、内容关键词、赛道名称或品牌关键词。例如："零食"、"美妆"、"家电"等。
- **`category`（可选）**：内容分类字段，通过下拉选择器（CategorySelect 组件）选择。可选的分类包括：美食、美妆、服饰、生活方式、科技、教育、游戏、搞笑等。选择分类可以更精准地筛选目标达人。

## 完整 Schema（JSON Schema 格式）

```json
{
  "type": "object",
  "required": ["keyword"],
  "properties": {
    "keyword": {
      "type": "string",
      "title": "搜索词",
      "description": "搜索博主或内容关键词（必填）"
    },
    "category": {
      "type": "string",
      "title": "内容分类",
      "x-component": "CategorySelect",
      "description": "选择内容分类，可精确定位细分赛道（可选）"
    }
  }
}
```

## API 调用说明

本技能调用 TikHub 抖音 KOL 搜索接口（`/api/v1/douyin/web/fetch_user_search`），传入参数：

- `keyword`：搜索关键词（必填）
- `category`：内容分类（可选）
