#!/bin/bash
# 深度清理所有混合语言

FR_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/fr"

for file in "$FR_DIR"/*.html; do
    echo "深度清理: $file"
    
    # Feature 4
    sed -i 's/Baixedor de Miniatures de TikTok/Téléchargeur de Miniatures TikTok/g' "$file"
    sed -i 's/Enregistrez imágenes de portada de vidéos TikTok en resolución completa/Enregistrez les images de couverture des vidéos TikTok en résolution complète/g' "$file"
    sed -i 's/Téléchargez miniatures de TikTok pour vos proyectos/Téléchargez des miniatures TikTok pour vos projets/g' "$file"
    
    # Feature 5
    sed -i 's/Funciona en Tous les Appareils/Fonctionne sur Tous les Appareils/g' "$file"
    sed -i 's/fonctionne en Windows/fonctionne sur Windows/g' "$file"
    sed -i 's/y cualquier appareil/et tout appareil/g' "$file"
    sed -i 's/con navigateur/avec navigateur/g' "$file"
    sed -i 's/Sans necessidade de instalar app/Sans besoin d'\''installer d'\''application/g' "$file"
    sed -i 's/desde cualquier appareil/depuis n'\''importe quel appareil/g' "$file"
    
    # Feature 6
    sed -i 's/Baixedor 100% Gratuit/Téléchargeur 100% Gratuit/g' "$file"
    sed -i 's/Téléchargez vidéos de TikTok gratuit/Téléchargez des vidéos TikTok gratuitement/g' "$file"
    sed -i 's/sans suscripción/sans abonnement/g' "$file"
    sed -i 's/sans tarifas ocultas/sans frais cachés/g' "$file"
    sed -i 's/pour siempre/pour toujours/g' "$file"
    
    # Feature 7
    sed -i 's/incluso qualité 4K cuando esté disponible/même en qualité 4K lorsque disponible/g' "$file"
    sed -i 's/preserva la qualité de vidéo original/préserve la qualité vidéo originale/g' "$file"
    sed -i 's/pour la mejor experiencia de visualización/pour la meilleure expérience de visionnage/g' "$file"
    
    # Feature 8
    sed -i 's/Sûr y Privado/Sûr et Privé/g' "$file"
    
    # 通用西班牙语清理
    sed -i 's/\by\b/et/g' "$file"
    sed -i 's/\bcon\b/avec/g' "$file"
    sed -i 's/\bdesde\b/depuis/g' "$file"
    sed -i 's/\bcualquier\b/n'\''importe quel/g' "$file"
    sed -i 's/\bsiempre\b/toujours/g' "$file"
    sed -i 's/\bimágenes\b/images/g' "$file"
    sed -i 's/\bportada\b/couverture/g' "$file"
    sed -i 's/\bresolución\b/résolution/g' "$file"
    sed -i 's/\bcompleta\b/complète/g' "$file"
    sed -i 's/\bproyectos\b/projets/g' "$file"
    sed -i 's/\bde alta\b/de haute/g' "$file"
    
    # 葡萄牙语清理
    sed -i 's/\bnecessidade\b/besoin/g' "$file"
    sed -i 's/\binstalar\b/installer/g' "$file"
    
done

echo "✅ 深度清理完成"
