#!/bin/bash
# 清理剩余的西班牙语残留

cd /root/.openclaw/workspace/tiktok-video-downloader/frontend/pt

for file in *.html pages/*.html; do
    echo "清理西班牙语残留: $file"
    
    # 西班牙语动词
    sed -i 's/\bPuedes\b/Você pode/g' "$file"
    sed -i 's/\bpuedes\b/você pode/g' "$file"
    sed -i 's/\bNecesidad\b/Necessidade/g' "$file"
    sed -i 's/\bnecesidad\b/necessidade/g' "$file"
    sed -i 's/\bPlanes\b/Planos/g' "$file"
    sed -i 's/\bplanes\b/planos/g' "$file"
    sed -i 's/\bLímites\b/Limites/g' "$file"
    sed -i 's/\blímites\b/limites/g' "$file"
    sed -i 's/\bBaixes\b/Baixe/g' "$file"
    sed -i 's/\bbaixes\b/baixe/g' "$file"
    sed -i 's/\bEs un\b/É um/g' "$file"
    sed -i 's/\bes un\b/é um/g' "$file"
    sed -i 's/\bNuestro\b/Nosso/g' "$file"
    sed -i 's/\bnuestro\b/nosso/g' "$file"
    sed -i 's/\bNuestra\b/Nossa/g' "$file"
    sed -i 's/\bnuestra\b/nossa/g' "$file"
    sed -i 's/\bTe permite\b/Permite que você/g' "$file"
    sed -i 's/\bte permite\b/permite que você/g' "$file"
    sed -i 's/\bElige\b/Escolha/g' "$file"
    sed -i 's/\belige\b/escolha/g' "$file"
    sed -i 's/\bTus\b/Seus/g' "$file"
    sed -i 's/\btus\b/seus/g' "$file"
    sed -i 's/\bPara tus\b/Para seus/g' "$file"
    sed -i 's/\bpara tus\b/para seus/g' "$file"
    
    # 常见短语
    sed -i 's/necesidad de/necessidade de/g' "$file"
    sed -i 's/sin necesidad/sem necessidade/g' "$file"
    sed -i 's/\ben múltiples\b/em múltiplas/g' "$file"
    sed -i 's/\bopciones de\b/opções de/g' "$file"
    
done

echo "✅ 西班牙语残留清理完成！"
