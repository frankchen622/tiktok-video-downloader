# 🚀 中文站部署检查清单

## 部署前检查

### 代码检查
- [x] 所有HTML文件已创建
- [x] main.py路由已添加
- [x] sitemap.xml已更新
- [x] Git提交完成
- [x] 推送到远程仓库

### 文件完整性
- [x] `/zh/index.html` - 首页
- [x] `/zh/yinpin.html` - MP3转换
- [x] `/zh/fengmian.html` - 封面图
- [x] `/zh/kuaipai.html` - 快拍
- [x] `/zh/pages/lianxi.html` - 联系我们
- [x] `/zh/pages/yinsi.html` - 隐私政策
- [x] `/zh/pages/tiaokuan.html` - 使用条款
- [x] `/zh/pages/mianze.html` - 免责声明
- [x] `/zh/pages/banquan.html` - 版权政策
- [x] `/zh/pages/cookie.html` - Cookie政策

## 部署步骤

### 1. Railway 部署（自动）
```bash
# Railway 会自动检测到 git push 并重新部署
# 等待 2-3 分钟
```

### 2. 验证部署
访问以下URL确认正常：
- [ ] https://dltk.io/zh
- [ ] https://dltk.io/zh/yinpin
- [ ] https://dltk.io/zh/fengmian
- [ ] https://dltk.io/zh/kuaipai
- [ ] https://dltk.io/zh/lianxi

### 3. 本地测试（可选）
```bash
# 启动本地服务器
cd /root/.openclaw/workspace/tiktok-downloader
python3 main.py

# 在另一个终端运行测试脚本
./test-zh-urls.sh http://localhost:8000
```

## 部署后验证

### SEO标签验证
使用浏览器开发者工具检查：

#### 首页 (/zh)
- [ ] `<html lang="zh-CN">`
- [ ] `<title>` 包含中文
- [ ] `<meta name="description">` 是中文
- [ ] `<link rel="canonical" href="https://dltk.io/zh" />`
- [ ] `<link rel="alternate" hreflang="zh-CN" href="https://dltk.io/zh" />`
- [ ] `<link rel="alternate" hreflang="en" href="https://dltk.io/" />`
- [ ] `<meta property="og:locale" content="zh_CN" />`

#### 其他核心页面
- [ ] /zh/yinpin - 标签完整
- [ ] /zh/fengmian - 标签完整
- [ ] /zh/kuaipai - 标签完整

### 功能测试
- [ ] 导航栏链接正常跳转
- [ ] 语言切换器工作（点击EN跳转到 /）
- [ ] 下载表单显示正常
- [ ] 输入框placeholder是中文
- [ ] 按钮文字是中文
- [ ] 页脚链接正常

### 移动端测试
- [ ] 响应式布局正常
- [ ] 中文字体清晰
- [ ] 触摸操作流畅

## 搜索引擎提交

### Google Search Console
1. 登录 https://search.google.com/search-console
2. 选择 dltk.io 属性
3. 提交新的 sitemap.xml
   - URL: https://dltk.io/sitemap.xml
4. 请求索引主要页面：
   - https://dltk.io/zh
   - https://dltk.io/zh/yinpin
   - https://dltk.io/zh/fengmian
   - https://dltk.io/zh/kuaipai

### Bing Webmaster Tools
1. 登录 https://www.bing.com/webmasters
2. 提交 sitemap: https://dltk.io/sitemap.xml
3. 请求索引中文页面

## 监控指标

### 1周内检查
- [ ] Google 收录情况：`site:dltk.io/zh`
- [ ] Bing 收录情况
- [ ] 访问量统计（Google Analytics）
- [ ] 用户反馈

### 2周内检查
- [ ] 中文关键词排名：
  - "TikTok视频下载器"
  - "TikTok无水印下载"
  - "TikTok转MP3"
- [ ] 点击率（CTR）
- [ ] 跳出率（Bounce Rate）

### 1个月内
- [ ] 对比英文站和中文站的转化率
- [ ] 优化表现差的页面
- [ ] 根据搜索词调整内容

## 常见问题排查

### 问题：404错误
- 检查 main.py 路由是否正确部署
- 检查 Railway 日志
- 重启服务

### 问题：中文乱码
- 确认 `<meta charset="UTF-8" />`
- 检查服务器编码设置

### 问题：页面加载慢
- 检查图片优化
- 考虑CDN加速
- 压缩CSS/JS

### 问题：未被搜索引擎收录
- 等待1-2周（新页面需要时间）
- 确认robots.txt没有阻止
- 手动提交sitemap
- 在 Search Console 请求索引

## 回滚计划

如果部署后出现严重问题：

```bash
cd /root/.openclaw/workspace/tiktok-downloader
git revert HEAD
git push origin master
```

Railway 会自动回滚到上一个版本。

## 成功标准

✅ **最低标准**（上线即达成）
- 所有10个URL返回200状态码
- 页面内容正确显示
- 无JavaScript错误
- 移动端可访问

✅ **1周目标**
- Google收录至少5个页面
- 零404错误报告
- 用户反馈正面

✅ **1个月目标**
- 中文站带来10%+新流量
- 至少1个关键词进入前10页
- 转化率≥英文站80%

---

**创建时间**：2024-09-11
**负责人**：Kiro + User
**状态**：✅ 准备部署
**预计完成时间**：24小时内