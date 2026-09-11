# 西班牙语站 URL 规划

## 核心页面

| 功能 | 英文URL | 西班牙语URL | 西班牙语名称 |
|------|---------|-------------|-------------|
| 首页 | `/` | `/es` | Descargador de Videos de TikTok |
| MP3转换 | `/mp3.html` | `/es/mp3` | Convertidor de TikTok a MP3 |
| 封面图 | `/thumbnail.html` | `/es/miniatura` | Descargador de Miniaturas |
| 快拍 | `/story.html` | `/es/historia` | Descargador de Historias |

## 法律页面

| 功能 | 英文URL | 西班牙语URL | 西班牙语名称 |
|------|---------|-------------|-------------|
| 联系我们 | `/pages/contact.html` | `/es/contacto` | Contacto |
| 隐私政策 | `/pages/privacy.html` | `/es/privacidad` | Política de Privacidad |
| 使用条款 | `/pages/terms.html` | `/es/terminos` | Términos de Servicio |
| 免责声明 | `/pages/disclaimer.html` | `/es/descargo` | Descargo de Responsabilidad |
| 版权政策 | `/pages/dmca.html` | `/es/dmca` | Política de Derechos de Autor |
| Cookie政策 | `/pages/cookies.html` | `/es/cookies` | Política de Cookies |

## URL 设计原则

1. **简洁易记**：使用西班牙语常用词汇
2. **SEO友好**：完整西班牙语单词，避免缩写
3. **语义清晰**：URL即能理解页面内容
4. **保持一致**：与英文站结构对应

## 关键词翻译对照

- Video Downloader → Descargador de Videos
- MP3 Converter → Convertidor a MP3
- Thumbnail → Miniatura
- Story → Historia
- Contact → Contacto
- Privacy → Privacidad
- Terms → Términos
- Disclaimer → Descargo de Responsabilidad
- DMCA → DMCA (保持不变)
- Cookies → Cookies (保持不变)

## Hreflang 标签

所有西班牙语页面需要添加：
```html
<link rel="alternate" hreflang="es" href="https://dltk.io/es" />
<link rel="alternate" hreflang="en" href="https://dltk.io/" />
<link rel="alternate" hreflang="zh-CN" href="https://dltk.io/zh" />
<link rel="alternate" hreflang="x-default" href="https://dltk.io/" />
```

## 实施步骤

1. 创建 `frontend/es/` 目录
2. 复制英文HTML文件
3. 翻译所有文本为西班牙语
4. 更新 main.py 添加西班牙语路由
5. 更新 sitemap.xml
6. 测试和部署
