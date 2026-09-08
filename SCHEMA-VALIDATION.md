# Schema.org 结构化数据 - 验证指南

## ✅ 已添加的 Schema 类型

### 所有页面
- **WebApplication** - 定义网页应用程序
- **FAQPage** - FAQ 富文本片段
- **HowTo** - 步骤指南（首页和 MP3）
- **Organization** - 品牌信息（首页）
- **AggregateRating** - 评分（首页：4.8/5）

## 🔍 如何验证 Schema

### 1. Google Rich Results Test
URL: https://search.google.com/test/rich-results

步骤：
1. 部署网站后，复制页面 URL
2. 粘贴到 Rich Results Test 工具
3. 检查是否检测到 FAQPage, HowTo, WebApplication
4. 确保没有错误或警告

### 2. Schema Markup Validator
URL: https://validator.schema.org/

步骤：
1. 选择 "Fetch URL" 或 "Code Snippet"
2. 输入页面 URL 或粘贴 HTML 代码
3. 验证 JSON-LD 语法是否正确
4. 检查所有必填字段

### 3. Google Search Console
部署后 2-4 周：
1. 登录 Google Search Console
2. 进入 "Enhancements" → "FAQ" 
3. 查看 FAQ 页面被索引的数量
4. 检查错误和警告

## 📊 预期效果

### FAQ Rich Snippets (FAQPage Schema)
**展示效果：**
- 搜索结果中显示折叠式 FAQ
- 用户可以直接在搜索结果中展开问题
- 提高 CTR（点击率）+15-30%

**示例：**
```
DLTK - TikTok Video Downloader
dltk.io
Download TikTok videos without watermark...

▼ Is DLTK free to use?
▼ How can I download TikTok videos...
▼ Do I need to install an app...
```

### HowTo Rich Snippets (HowTo Schema)
**展示效果：**
- 显示步骤编号和标题
- 显示总时间（PT1M = 1 分钟）
- 可能显示缩略图（如果提供）

**示例：**
```
How to Download TikTok Videos
1. Copy TikTok Video Link
2. Paste Link into DLTK  
3. Download TikTok Video
⏱ Time: 1 minute
```

### WebApplication Rich Snippets
**展示效果：**
- 应用名称和描述
- 价格信息（Free）
- 星级评分（4.8/5）
- 功能列表

## ⏰ 生效时间

- **首次索引：** 1-2 周
- **Rich Snippets 显示：** 2-4 周
- **完全生效：** 4-8 周

## 🛠️ 故障排查

### 如果 Rich Snippets 不显示：
1. 使用 Rich Results Test 验证语法
2. 确保 Schema 在 `<head>` 中
3. 检查 JSON-LD 格式是否正确
4. 等待 Google 重新索引（提交 sitemap）
5. 检查 robots.txt 是否阻止爬虫

### 常见错误：
- ❌ 缺少必填字段（name, description）
- ❌ JSON 语法错误（逗号、括号）
- ❌ URL 不匹配（canonical vs actual）
- ❌ 内容与页面不符

## 📈 监控指标

部署后追踪以下指标：
- Click-Through Rate (CTR) - 应提升 15-30%
- 搜索展示次数 - Rich Snippets 增加曝光
- 平均排名 - 可能小幅提升
- FAQ 点击率 - 新的互动方式

## 🔗 有用的工具

- **Google Rich Results Test:** https://search.google.com/test/rich-results
- **Schema Markup Validator:** https://validator.schema.org/
- **Google Search Console:** https://search.google.com/search-console
- **Bing Markup Validator:** https://www.bing.com/webmaster/tools/markup-validator

---

**下一步：** 部署到 Railway，然后提交 URL 到 Google Search Console 请求索引。
