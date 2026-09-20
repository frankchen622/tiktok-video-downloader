#!/bin/bash
# 德语翻译脚本 - 从英语直接翻译，保护HTML技术元素

DE_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/de"

echo "=== 开始德语翻译 ==="

translate_to_german() {
    local file="$1"
    echo "翻译: $file"
    
    # 1. 基础元数据
    sed -i 's/lang="en"/lang="de"/g' "$file"
    
    # 2. Meta标签翻译（小心保护HTML结构）
    sed -i 's/<title>TikTok Video Downloader Without Watermark - Free & Fast | DLTK<\/title>/<title>TikTok Videos Ohne Wasserzeichen Herunterladen - Kostenlos & Schnell | DLTK<\/title>/g' "$file"
    
    sed -i 's/content="Download TikTok videos without watermark in HD quality\. Save TikTok to MP4 instantly - no app, no registration\. 100% free TikTok video downloader\. Try now!"/content="TikTok-Videos ohne Wasserzeichen in HD-Qualität herunterladen. TikTok sofort als MP4 speichern - keine App, keine Registrierung. 100% kostenloser TikTok-Video-Downloader. Jetzt ausprobieren!"/g' "$file"
    
    sed -i 's/content="Download TikTok videos without watermark in seconds\. HD quality, no registration, completely free\."/content="TikTok-Videos ohne Wasserzeichen in Sekunden herunterladen. HD-Qualität, keine Registrierung, völlig kostenlos."/g' "$file"
    
    # 3. 更新URL引用
    sed -i 's|https://dltk\.io/"|https://dltk.io/de"|g' "$file"
    sed -i 's|content="https://dltk\.io/"|content="https://dltk.io/de"|g' "$file"
    
    # 4. Canonical和hreflang
    sed -i 's|<link rel="canonical" href="https://dltk\.io/" />|<link rel="canonical" href="https://dltk.io/de" />|g' "$file"
    
    # 添加德语hreflang（在x-default之前）
    sed -i 's|<link rel="alternate" hreflang="x-default"|<link rel="alternate" hreflang="de" href="https://dltk.io/de" />\n  <link rel="alternate" hreflang="x-default"|g' "$file"
}

# 翻译所有HTML文件
for file in "$DE_DIR"/*.html; do
    [ -f "$file" ] && translate_to_german "$file"
done

for file in "$DE_DIR"/pages/*.html; do
    [ -f "$file" ] && translate_to_german "$file"
done

echo "✅ Phase 1完成：基础设置"
