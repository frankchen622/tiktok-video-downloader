#!/bin/bash
# 修复被错误翻译的HTML技术词汇

FR_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/fr"

echo "修复HTML技术标签和URL..."

for file in "$FR_DIR"/*.html "$FR_DIR"/pages/*.html; do
    echo "修复: $file"
    
    # 修复被翻译的域名和URL
    sed -i 's/googletagmanager\.avec/googletagmanager.com/g' "$file"
    sed -i 's/dltk\.io\/ptstatic/dltk.io\/static/g' "$file"
    sed -i 's/\.avec/.com/g' "$file"
    
    # 修复可能被翻译的其他技术词
    sed -i 's/completamente gratuit/complètement gratuit/g' "$file"
    sed -i 's/completamente/complètement/g' "$file"
    
    # 确保 HTML 属性正确
    sed -i 's/type="application\/ld\+json"/type="application\/ld+json"/g' "$file"
    
    # 修复可能的其他URL问题
    sed -i 's/\/frstatic/\/static/g' "$file"
    
done

echo "✅ HTML技术标签修复完成"
