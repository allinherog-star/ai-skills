# Form Schema

本文件描述 `xhs-sentiment-dashboard` 技能的输入参数格式规范。

## 参数定义

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | 小红书分享链接，格式为 URI |

## 链接格式说明

### 小红书

- 分享链接格式：`https://www.xiaohongshu.com/explore/67890abcdef`
- 短链接格式：`https://xhslink.com/xxxxxx`

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
      "description": "小红书笔记/视频的分享链接"
    }
  }
}
```

## 验证规则

- `link` 字段必须为有效的 URI 格式
- `link` 字段必须包含 `xiaohongshu.com` 或 `xhslink.com` 域名
- 平台自动固定为 `xhs`，无需用户额外指定
