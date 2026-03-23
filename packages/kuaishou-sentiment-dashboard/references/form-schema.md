# Form Schema

本文件描述 `kuaishou-sentiment-dashboard` 技能的输入参数格式规范。

## 参数定义

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | 快手分享链接，格式为 URI |

## 链接格式说明

### 快手

- 分享链接格式：`https://www.kuaishou.com/video/3x4c7e9f2g1h`
- 短链接格式：`https://v.kuaishou.com/xxxxxx`

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
      "description": "快手视频/直播的分享链接"
    }
  }
}
```

## 验证规则

- `link` 字段必须为有效的 URI 格式
- `link` 字段必须包含 `kuaishou.com` 或 `v.kuaishou.com` 域名
- 平台自动固定为 `kuaishou`，无需用户额外指定
