# Form Schema

本文件描述 `bilibili-sentiment-dashboard` 技能的输入参数格式规范。

## 参数定义

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | B站分享链接，格式为 URI |

## 链接格式说明

### B站

- 分享链接格式：`https://www.bilibili.com/video/BV1xx411c7mD`
- 短链接格式：`https://b23.tv/xxxxxx`

## JSON Schema

```json
{
  "type": "object",
  "required": ["link"],
  "properties": {
    "link": {
      "type": "string",
      "title": "分享链接",
      "format": "uri",
      "description": "B站视频/直播的分享链接"
    }
  }
}
```

## 验证规则

- `link` 字段必须为有效的 URI 格式
- `link` 字段必须包含 `bilibili.com` 或 `b23.tv` 域名
- 平台自动固定为 `bilibili`，无需用户额外指定
