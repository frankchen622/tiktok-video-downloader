#!/bin/bash
# 修复法语页面的footer

FR_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/fr"

for file in "$FR_DIR"/*.html; do
    echo "修复footer: $file"
    
    # 1. 修复CSS类名
    sed -i 's/class="compteiner footer-content"/class="container footer-content"/g' "$file"
    sed -i 's/class="compteiner footer-bottom"/class="container footer-bottom"/g' "$file"
    sed -i 's/class="footer-liens"/class="footer-links"/g' "$file"
    
    # 2. 修复标题
    sed -i 's/Sobre o DLTK/À Propos de DLTK/g' "$file"
    sed -i 's/liens Rápidos/Liens Rapides/g' "$file"
    sed -i 's/Jurídico/Légal/g' "$file"
    
    # 3. 修复footer描述文本
    sed -i 's/DLTK\.io est un téléchargeur gratuit en línea de vidéos de TikTok pour télécharger vidéos sans filigrane, extraer audio a MP3, enregistrer miniatures et preservar storys\./DLTK.io est un téléchargeur gratuit en ligne de vidéos TikTok pour télécharger des vidéos sans filigrane, extraire l'\''audio en MP3, enregistrer des miniatures et préserver les stories./g' "$file"
    
    # 4. 修复链接文本
    sed -i 's/TikTok a MP3/TikTok vers MP3/g' "$file"
    sed -i 's/Baixedor de Miniatures/Téléchargeur de Miniatures/g' "$file"
    sed -i 's/Baixedor de Storys/Téléchargeur de Stories/g' "$file"
    
    # 5. 修复法律页面链接
    sed -i 's|href="/pages/comptect\.html"|href="/fr/contact"|g' "$file"
    sed -i 's|href="/pages/privacy\.html"|href="/fr/confidentialite"|g' "$file"
    sed -i 's|href="/pages/terms\.html"|href="/fr/conditions"|g' "$file"
    sed -i 's|href="/pages/disclaimer\.html"|href="/fr/avertissement"|g' "$file"
    sed -i 's|href="/pages/dmca\.html"|href="/fr/dmca"|g' "$file"
    sed -i 's|href="/pages/cookies\.html"|href="/fr/cookies"|g' "$file"
    
    # 6. 修复链接文本
    sed -i 's/Contáctanos/Contactez-nous/g' "$file"
    sed -i 's/Conditions de Serviço/Conditions de Service/g' "$file"
    sed -i 's/DMCA et Derechos de Autor/DMCA et Droits d'\''Auteur/g' "$file"
    
    # 7. 修复footer底部版权文本
    sed -i 's/Baixador de Vídeos TikTok Grátis Sem Marca d'\''Água/Téléchargeur de Vidéos TikTok Gratuit Sans Filigrane/g' "$file"
    
done

echo "✅ Footer修复完成"
