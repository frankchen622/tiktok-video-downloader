#!/bin/bash
# 最终完整法语清理

FR_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/fr"

for file in "$FR_DIR"/*.html "$FR_DIR"/pages/*.html; do
    echo "最终清理: $file"
    
    # 修复混合的句子
    sed -i 's/que supprime les filigranes automaticamente/qui supprime automatiquement les filigranes/g' "$file"
    sed -i 's/Téléchargez vidéos TikTok/Téléchargez des vidéos TikTok/g' "$file"
    
    # 修复输入框文本
    sed -i 's/Collez el Link del Vidéo de TikTok Aquí\.\.\./Collez le lien de la vidéo TikTok ici.../g' "$file"
    sed -i 's/Collez el link/Collez le lien/g' "$file"
    sed -i 's/del vidéo/de la vidéo/g' "$file"
    sed -i 's/Aquí/ici/g' "$file"
    sed -i 's/aquí/ici/g' "$file"
    
    # 西班牙语残留
    sed -i 's/\bel\b/le/g' "$file"
    sed -i 's/\bEl\b/Le/g' "$file"
    sed -i 's/\bla\b/la/g' "$file"
    sed -i 's/\bLa\b/La/g' "$file"
    sed -i 's/\bdel\b/de/g' "$file"
    sed -i 's/\bDel\b/De/g' "$file"
    
    # 葡萄牙语 "automaticamente" → 法语 "automatiquement"
    sed -i 's/automaticamente/automatiquement/g' "$file"
    
    # 其他混合语言
    sed -i 's/Link/lien/g' "$file"
    sed -i 's/link/lien/g' "$file" 
    
    # 按钮文本
    sed -i 's/BAIXAR/TÉLÉCHARGER/g' "$file"
    sed -i 's/Baixar/Télécharger/g' "$file"
    
    # 修复ID和name属性（这些是技术性的，但让我们统一）
    sed -i 's/id="vídeoUrl"/id="videoUrl"/g' "$file"
    sed -i 's/for="vídeoUrl"/for="videoUrl"/g' "$file"
    
done

echo "✅ 最终法语清理完成"
