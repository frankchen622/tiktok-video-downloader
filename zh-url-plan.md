# 中文小语种站 URL 规划方案

## 设计原则
1. **本地化优先**：URL 使用拼音或符合中文用户习惯的词汇
2. **SEO 友好**：简短、易记、语义化
3. **避免直译**：考虑上下文和实际用法

## URL 映射表

### 核心功能页面
| 英文页面 | 中文名称 | 建议 URL | 理由 |
|---------|---------|---------|------|
| / (index) | TikTok视频下载 | `/zh/xiazai` | "下载"是最直接的动作词 |
| /mp3.html | MP3转换器 | `/zh/yinpin` | "音频"比"MP3"更本地化 |
| /thumbnail.html | 缩略图下载 | `/zh/fengmian` | "封面"是中文用户常用词 |
| /story.html | Story下载 | `/zh/kuaipai` | "快拍"是本地化术语 |

### 法律/信息页面
| 英文页面 | 中文名称 | 建议 URL | 理由 |
|---------|---------|---------|------|
| /pages/contact.html | 联系我们 | `/zh/lianxi` | 简洁直接 |
| /pages/privacy.html | 隐私政策 | `/zh/yinsi` | 常用术语 |
| /pages/terms.html | 使用条款 | `/zh/tiaokuan` | 法律文档标准用语 |
| /pages/disclaimer.html | 免责声明 | `/zh/mianze` | 简化版"免责" |
| /pages/dmca.html | 版权政策 | `/zh/banquan` | 本地化"版权" |
| /pages/cookies.html | Cookie政策 | `/zh/cookie` | 保留技术术语 |

## 备选方案

### 方案A：完全拼音化（推荐）
- 优点：纯中文拼音，对国内用户友好
- 缺点：国际用户可能不理解
- 适用：主要面向中国大陆用户

### 方案B：混合英文关键词
- 例如：`/zh-cn/download`, `/zh-cn/mp3`
- 优点：国际通用，SEO更好
- 缺点：不够本地化

### 方案C：语义化中文词汇
- 例如：`/zh/shipin-xiazai`（视频下载）, `/zh/yinyue-zhuanhuan`（音乐转换）
- 优点：SEO极佳，语义清晰
- 缺点：URL较长

## 最终推荐：方案A + 部分语义化

**核心页面（短URL）：**
```
/zh                     → 首页（视频下载）
/zh/yinpin             → MP3音频转换
/zh/fengmian           → 封面图下载
/zh/kuaipai            → 快拍下载
```

**法律页面（简化拼音）：**
```
/zh/lianxi             → 联系我们
/zh/yinsi              → 隐私政策
/zh/tiaokuan           → 使用条款
/zh/mianze             → 免责声明
/zh/banquan            → 版权政策
/zh/cookie             → Cookie政策
```

## 实现方式

### 后端路由（main.py）
添加中文路由映射：

```python
# 中文站路由
@app.get("/zh")
async def serve_index_zh():
    return FileResponse(os.path.join(frontend_path, "zh", "xiazai.html"))

@app.get("/zh/yinpin")
async def serve_mp3_zh():
    return FileResponse(os.path.join(frontend_path, "zh", "yinpin.html"))

@app.get("/zh/fengmian")
async def serve_thumbnail_zh():
    return FileResponse(os.path.join(frontend_path, "zh", "fengmian.html"))

@app.get("/zh/kuaipai")
async def serve_story_zh():
    return FileResponse(os.path.join(frontend_path, "zh", "kuaipai.html"))

# 法律页面
@app.get("/zh/{page_name}")
async def serve_page_zh(page_name: str):
    allowed = ["lianxi", "yinsi", "tiaokuan", "mianze", "banquan", "cookie"]
    if page_name not in allowed:
        raise HTTPException(status_code=404)
    return FileResponse(os.path.join(frontend_path, "zh", "pages", f"{page_name}.html"))
```

### 前端文件结构
```
frontend/
  zh/                    ← 新建中文站目录
    xiazai.html         ← 首页（视频下载）
    yinpin.html         ← MP3转换
    fengmian.html       ← 缩略图
    kuaipai.html        ← Story
    pages/              ← 法律页面
      lianxi.html
      yinsi.html
      tiaokuan.html
      mianze.html
      banquan.html
      cookie.html
```

## SEO 优化建议

1. **hreflang 标签**：在每个页面添加语言版本互链
```html
<link rel="alternate" hreflang="en" href="https://dltk.io/" />
<link rel="alternate" hreflang="zh-CN" href="https://dltk.io/zh" />
<link rel="alternate" hreflang="x-default" href="https://dltk.io/" />
```

2. **Canonical URL**：明确指定规范链接
```html
<link rel="canonical" href="https://dltk.io/zh/xiazai" />
```

3. **本地化 Meta 标签**：
```html
<meta name="description" content="免费TikTok视频下载器，无水印高清下载，支持MP3转换和封面图保存" />
<meta property="og:locale" content="zh_CN" />
```

## 注意事项

1. ⚠️ **避免重复内容惩罚**：中文页面和英文页面内容相似，必须使用 hreflang 标签
2. ⚠️ **301 重定向**：如果有旧的中文 URL，需要设置 301 重定向到新 URL
3. ⚠️ **Sitemap 更新**：在 sitemap.xml 中添加所有中文页面
4. ⚠️ **语言切换器**：更新语言切换逻辑，点击"中文"时跳转到对应的中文 URL

## 下一步行动

1. [ ] 创建 `frontend/zh/` 目录结构
2. [ ] 复制并本地化所有页面内容
3. [ ] 更新 `main.py` 添加中文路由
4. [ ] 修改语言切换器，支持 URL 跳转
5. [ ] 添加 hreflang 标签到所有页面
6. [ ] 更新 sitemap.xml
7. [ ] 测试所有中文 URL 路由
8. [ ] 部署并验证 SEO 标签
