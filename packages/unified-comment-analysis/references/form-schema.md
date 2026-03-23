# Form Schema

本文件描述 `unified-comment-analysis` 技能的输入参数格式规范。

## 参数定义

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `link` | string | 是 | 分享链接，格式为 URI。支持抖音、小红书、B站、快手的分享链接格式 |
| `platform` | enum | 否 | 平台类型，可选值：`douyin`（抖音）、`xhs`（小红书）、`bilibili`（B站）、`kuaishou`（快手）。若不提供，将自动从链接中识别 |

## 平台识别规则

系统支持从分享链接自动识别平台：

| 平台 | 链接示例域名/格式 | platform 值 |
|------|------------------|-------------|
| 抖音 | `douyin.com`、`v.douyin.com` | `douyin` |
| 小红书 | `xiaohongshu.com`、`xhslink.com` | `xhs` |
| B站 | `bilibili.com`、`b23.tv` | `bilibili` |
| 快手 | `kuaishou.com`、`v.kuaishou.com` | `kuaishou` |

## 链接格式说明

### 抖音
- 分享链接格式：`https://www.douyin.com/video/7381234567890123456`
- 短链接格式：`https://v.douyin.com/xxxxxx`

### 小红书
- 分享链接格式：`https://www.xiaohongshu.com/explore/67890abcdef`
- 短链接格式：`https://xhslink.com/xxxxxx`

### B站
- 分享链接格式：`https://www.bilibili.com/video/BV1xx411c7mD`
- 短链接格式：`https://b23.tv/xxxxxx`

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
      "description": "抖音、小红书、B站或快手的分享链接"
    },
    "platform": {
      "type": "string",
      "title": "平台",
      "enum": ["douyin", "xhs", "bilibili", "kuaishou"],
      "description": "平台类型，若不提供则自动从链接中识别"
    }
  }
}
```

## 验证规则

- `link` 字段必须为有效的 URI 格式
- `link` 字段必须包含可识别的平台域名
- `platform` 可选，若提供必须是枚举值之一
