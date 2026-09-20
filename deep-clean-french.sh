#!/bin/bash
# 彻底清除法语页面中的葡萄牙语

FR_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/fr"

for file in "$FR_DIR"/*.html "$FR_DIR"/pages/*.html; do
    echo "深度清理: $file"
    
    # 葡萄牙语特征词完全替换
    sed -i 's/\bvocê\b/vous/g' "$file"
    sed -i 's/\bVocê\b/Vous/g' "$file"
    sed -i 's/\bseu\b/votre/g' "$file"
    sed -i 's/\bSeu\b/Votre/g' "$file"
    sed -i 's/\bsua\b/votre/g' "$file"
    sed -i 's/\bSua\b/Votre/g' "$file"
    sed -i 's/\bseus\b/vos/g' "$file"
    sed -i 's/\bsuas\b/vos/g' "$file"
    
    # 疑问词
    sed -i 's/\bPosso\b/Puis-je/g' "$file"
    sed -i 's/\bposso\b/puis-je/g' "$file"
    sed -i 's/\bPode\b/Peut/g' "$file"
    sed -i 's/\bpode\b/peut/g' "$file"
    sed -i 's/\bPodem\b/Peuvent/g' "$file"
    sed -i 's/\bpodem\b/peuvent/g' "$file"
    
    # 常见动词
    sed -i 's/\bé\b/est/g' "$file"
    sed -i 's/\bÉ\b/Est/g' "$file"
    sed -i 's/\bsão\b/sont/g' "$file"
    sed -i 's/\bSão\b/Sont/g' "$file"
    sed -i 's/\btem\b/a/g' "$file"
    sed -i 's/\bTem\b/A/g' "$file"
    sed -i 's/\btêm\b/ont/g' "$file"
    sed -i 's/\bestá\b/est/g' "$file"
    sed -i 's/\bEstá\b/Est/g' "$file"
    sed -i 's/\bestão\b/sont/g' "$file"
    sed -i 's/\bfoi\b/était/g' "$file"
    
    # 完整短语替换
    sed -i 's/mais rápido, fácil e confiável que/plus rapide, facile et fiable que/g' "$file"
    sed -i 's/outros baixadores/autres téléchargeurs/g' "$file"
    sed -i 's/completamente grátis/entièrement gratuit/g' "$file"
    sed -i 's/sem anúncios ou/sans publicités ou/g' "$file"
    
    # 技术词汇
    sed -i 's/\baplicativo\b/application/g' "$file"
    sed -i 's/\bAplicativo\b/Application/g' "$file"
    sed -i 's/\baplicativos\b/applications/g' "$file"
    sed -i 's/\bcelular\b/mobile/g' "$file"
    sed -i 's/\bCelular\b/Mobile/g' "$file"
    sed -i 's/\bcelulares\b/mobiles/g' "$file"
    sed -i 's/\bnavegador\b/navigateur/g' "$file"
    sed -i 's/\bNavegador\b/Navigateur/g' "$file"
    
done

echo "✅ 葡萄牙语深度清理完成"
