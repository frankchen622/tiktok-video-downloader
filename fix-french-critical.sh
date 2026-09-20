#!/bin/bash
# 修复法语页面的严重问题

FR_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/fr"

echo "修复法语页面问题..."

for file in "$FR_DIR"/*.html "$FR_DIR"/pages/*.html; do
    echo "修复: $file"
    
    # 1. 修复 CSS 类名错误
    sed -i 's/class="compteiner"/class="container"/g' "$file"
    sed -i 's/<div class="compteiner">/<div class="container">/g' "$file"
    
    # 2. 修复拼写错误
    sed -i 's/Quelité/Qualité/g' "$file"
    sed -i 's/quelité/qualité/g' "$file"
    
    # 3. 修复导航链接
    sed -i 's|href="/fr/miniature"|href="/fr/miniatura"|g' "$file"
    sed -i 's|href="/fr/story"|href="/fr/historia"|g' "$file"
    
    # 4. 清除葡萄牙语残留
    sed -i 's/O DLTK é um téléchargeur gratuit/DLTK est un téléchargeur gratuit/g' "$file"
    sed -i 's/vidéos do TikTok/vidéos TikTok/g' "$file"
    sed -i 's/remove filigranes/supprime les filigranes/g' "$file"
    sed -i 's/Téléchargez vidéos do TikTok/Téléchargez des vidéos TikTok/g' "$file"
    sed -i 's/convertissez pour MP3/convertissez en MP3/g' "$file"
    sed -i 's/enregistrez miniatures/enregistrez des miniatures/g' "$file"
    sed -i 's/tudo en um só lugar/tout en un seul endroit/g' "$file"
    sed -i 's/Sans necessidade de app/Sans besoin d'\''application/g' "$file"
    sed -i 's/sans inscription necessário/sans inscription requise/g' "$file"
    sed -i 's/simples et funciona en tous les appareils/simple et fonctionne sur tous les appareils/g' "$file"
    
    # 5. 修复更多葡萄牙语
    sed -i 's/\bO\b/Le/g' "$file"
    sed -i 's/\bdo\b/de/g' "$file"
    sed -i 's/\bda\b/de la/g' "$file"
    sed -i 's/\bdos\b/des/g' "$file"
    sed -i 's/\bdas\b/des/g' "$file"
    sed -i 's/\bem\b/en/g' "$file"
    sed -i 's/\bEm\b/En/g' "$file"
    sed -i 's/\bno\b/dans le/g' "$file"
    sed -i 's/\bna\b/dans la/g' "$file"
    sed -i 's/\bpara\b/pour/g' "$file"
    sed -i 's/\bPara\b/Pour/g' "$file"
    sed -i 's/\btudo\b/tout/g' "$file"
    sed -i 's/\bTudo\b/Tout/g' "$file"
    
    # 6. 常见葡萄牙语动词 → 法语
    sed -i 's/\bfunciona\b/fonctionne/g' "$file"
    sed -i 's/\bpossíveis\b/possibles/g' "$file"
    sed -i 's/\bnecessário\b/nécessaire/g' "$file"
    sed -i 's/\bnecessária\b/nécessaire/g' "$file"
    
done

echo "✅ 法语页面关键问题修复完成"
