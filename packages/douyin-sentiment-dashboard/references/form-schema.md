# Form Schema

本文件描述 `douyin-sentiment-dashboard` 技能的输入参数格式规范。

## 参数定义

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | 抖音分享链接，格式为 URI |

## 链接格式说明

### 抖音

- 分享链接格式：`https://www.douyin.com/video/7381234567890123456`
- 短链接格式：`https://v.douyin.com/xxxxxx`

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
      "description": "抖音视频/笔记/直播的分享链接"
    }
  }
}
```

## 验证规则

- `link` 字段必须为有效的 URI 格式
- `link` 字段必须包含 `douyin.com` 或 `v.douyin.com` 域名
- 平台自动固定为 `douyin`，无需用户额外指定
