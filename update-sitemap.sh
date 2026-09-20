#!/bin/bash
# 更新 sitemap.xml 添加葡萄牙语页面

SITEMAP="/root/.openclaw/workspace/tiktok-video-downloader/frontend/sitemap.xml"

# 1. 在所有现有URL的hreflang部分添加pt链接
sed -i 's|<xhtml:link rel="alternate" hreflang="zh-CN" href="https://dltk.io/zh"/>|<xhtml:link rel="alternate" hreflang="pt" href="https://dltk.io/pt"/>\n    <xhtml:link rel="alternate" hreflang="zh-CN" href="https://dltk.io/zh"/>|g' "$SITEMAP"

# 2. 在西班牙语首页后添加葡萄牙语首页
sed -i '/<!-- Spanish Homepage -->/a\  \n  <!-- Portuguese Homepage -->\n  <url>\n    <loc>https://dltk.io/pt</loc>\n    <xhtml:link rel="alternate" hreflang="en" href="https://dltk.io/"/>\n    <xhtml:link rel="alternate" hreflang="es" href="https://dltk.io/es"/>\n    <xhtml:link rel="alternate" hreflang="pt" href="https://dltk.io/pt"/>\n    <xhtml:link rel="alternate" hreflang="zh-CN" href="https://dltk.io/zh"/>\n    <lastmod>2024-09-14</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>' "$SITEMAP"

# 3. 添加葡萄牙语MP3页面
sed -i '/<!-- Spanish MP3 Page -->/a\  \n  <!-- Portuguese MP3 Page -->\n  <url>\n    <loc>https://dltk.io/pt/mp3</loc>\n    <xhtml:link rel="alternate" hreflang="en" href="https://dltk.io/mp3"/>\n    <xhtml:link rel="alternate" hreflang="es" href="https://dltk.io/es/mp3"/>\n    <xhtml:link rel="alternate" hreflang="pt" href="https://dltk.io/pt/mp3"/>\n    <xhtml:link rel="alternate" hreflang="zh-CN" href="https://dltk.io/zh/mp3"/>\n    <lastmod>2024-09-14</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n  </url>' "$SITEMAP"

# 4. 添加葡萄牙语封面图页面
sed -i '/<!-- Spanish Thumbnail Page -->/a\  \n  <!-- Portuguese Thumbnail Page -->\n  <url>\n    <loc>https://dltk.io/pt/miniatura</loc>\n    <xhtml:link rel="alternate" hreflang="en" href="https://dltk.io/thumbnail"/>\n    <xhtml:link rel="alternate" hreflang="es" href="https://dltk.io/es/miniatura"/>\n    <xhtml:link rel="alternate" hreflang="pt" href="https://dltk.io/pt/miniatura"/>\n    <xhtml:link rel="alternate" hreflang="zh-CN" href="https://dltk.io/zh/fengmian"/>\n    <lastmod>2024-09-14</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>' "$SITEMAP"

# 5. 添加葡萄牙语Story页面
sed -i '/<!-- Spanish Story Page -->/a\  \n  <!-- Portuguese Story Page -->\n  <url>\n    <loc>https://dltk.io/pt/historia</loc>\n    <xhtml:link rel="alternate" hreflang="en" href="https://dltk.io/story"/>\n    <xhtml:link rel="alternate" hreflang="es" href="https://dltk.io/es/historia"/>\n    <xhtml:link rel="alternate" hreflang="pt" href="https://dltk.io/pt/historia"/>\n    <xhtml:link rel="alternate" hreflang="zh-CN" href="https://dltk.io/zh/gushi"/>\n    <lastmod>2024-09-14</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>' "$SITEMAP"

# 6. 添加葡萄牙语法律页面
cat >> "$SITEMAP" << 'EOF'

  <!-- Portuguese Legal Pages -->
  <url>
    <loc>https://dltk.io/pt/contato</loc>
    <lastmod>2024-09-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>

  <url>
    <loc>https://dltk.io/pt/privacidade</loc>
    <lastmod>2024-09-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.4</priority>
  </url>

  <url>
    <loc>https://dltk.io/pt/termos</loc>
    <lastmod>2024-09-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.4</priority>
  </url>

  <url>
    <loc>https://dltk.io/pt/aviso-legal</loc>
    <lastmod>2024-09-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>

  <url>
    <loc>https://dltk.io/pt/dmca</loc>
    <lastmod>2024-09-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>

  <url>
    <loc>https://dltk.io/pt/cookies</loc>
    <lastmod>2024-09-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>

EOF

# 移除最后的 </urlset> 然后重新添加
sed -i '$ d' "$SITEMAP"
echo '</urlset>' >> "$SITEMAP"

echo "✅ Sitemap 更新完成！"
