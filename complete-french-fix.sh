#!/bin/bash
# 彻底修复法语页面的所有问题

FR_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/fr"

echo "=== 开始全面修复法语页面 ==="

for file in "$FR_DIR"/*.html "$FR_DIR"/pages/*.html; do
    echo "修复: $file"
    
    # 1. 修复所有CSS类名
    sed -i 's/class="compteiner"/class="container"/g' "$file"
    sed -i 's/class="feature-image-compteiner"/class="feature-image-container"/g' "$file"
    sed -i 's/class="feature-text-compteiner"/class="feature-text-container"/g' "$file"
    sed -i 's/class="feature-lien"/class="feature-link"/g' "$file"
    
    # 2. 修复图片路径
    sed -i 's/src="\/static\/images\/feature-dans le-watermark\.jpg"/src="\/static\/images\/feature-no-watermark.jpg"/g' "$file"
    
    # 3. 清除西班牙语残留
    sed -i 's/Por Que Elegir/Pourquoi Choisir/g' "$file"
    sed -i 's/Nosso Baixedor/Notre Téléchargeur/g' "$file"
    sed -i 's/Le mejor téléchargeur gratuit de TikTok con características potentes pour todas vos necesidades/Le meilleur téléchargeur gratuit TikTok avec des fonctionnalités puissantes pour tous vos besoins/g' "$file"
    
    # 4. 清除葡萄牙语+西班牙语混合
    sed -i 's/Nosso téléchargeur gratuit elimina marcas de agua automatiquement, dándote vidéos limpios y de aspecto profesional/Notre téléchargeur gratuit supprime automatiquement les filigranes, vous donnant des vidéos propres et professionnelles/g' "$file"
    sed -i 's/Téléchargez vidéos de TikTok en qualité original sans le logo de TikTok/Téléchargez des vidéos TikTok en qualité originale sans le logo TikTok/g' "$file"
    
    sed -i 's/Baixedor Rapide de TikTok/Téléchargeur TikTok Rapide/g' "$file"
    sed -i 's/Nosso téléchargeur usa tecnología avanzada pour procesar vidéos al instante/Notre téléchargeur utilise une technologie avancée pour traiter les vidéos instantanément/g' "$file"
    sed -i 's/Sans esperas, sans colas - solo téléchargez rápidas/Sans attente, sans files - juste des téléchargements rapides/g' "$file"
    
    sed -i 's/Convertidor de TikTok a MP3/Convertisseur TikTok vers MP3/g' "$file"
    sed -i 's/Extrae audio de vidéos de TikTok y guárdalo como archivos MP3/Extrayez l'\''audio des vidéos TikTok et enregistrez-le en fichiers MP3/g' "$file"
    sed -i 's/Perfecto pour crear colecciones de música o podcasts/Parfait pour créer des collections musicales ou des podcasts/g' "$file"
    sed -i 's/Prueba le Convertidor TikTok a MP3/Essayez le Convertisseur TikTok vers MP3/g' "$file"
    
    # 5. 通用西班牙语词汇清除
    sed -i 's/\bNosso\b/Notre/g' "$file"
    sed -i 's/\bnosso\b/notre/g' "$file"
    sed -i 's/\bmarcas de agua\b/filigranes/g' "$file"
    sed -i 's/\bdándote\b/vous donnant/g' "$file"
    sed -i 's/\bvidéos limpios\b/vidéos propres/g' "$file"
    sed -i 's/\btecnología avanzada\b/technologie avancée/g' "$file"
    sed -i 's/\bprocesar\b/traiter/g' "$file"
    sed -i 's/\bal instante\b/instantanément/g' "$file"
    sed -i 's/\besperas\b/attente/g' "$file"
    sed -i 's/\bcolas\b/files/g' "$file"
    sed -i 's/\bsolo\b/juste/g' "$file"
    sed -i 's/\brápidas\b/rapides/g' "$file"
    
done

echo "✅ 全面修复完成"
