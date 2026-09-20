#!/bin/bash
# 最终清理所有英文残留

cd /root/.openclaw/workspace/tiktok-video-downloader/frontend/pt

for file in *.html pages/*.html; do
    echo "最终清理: $file"
    
    # 常见英文动词和形容词
    sed -i 's/\bDownload\b/Baixe/g' "$file"
    sed -i 's/\bdownload\b/baixe/g' "$file"
    sed -i 's/\bSave\b/Salve/g' "$file"
    sed -i 's/\bsave\b/salve/g' "$file"
    sed -i 's/\bSimply\b/Simplesmente/g' "$file"
    sed -i 's/\bsimply\b/simplesmente/g' "$file"
    sed -i 's/\bClick\b/Clique/g' "$file"
    sed -i 's/\bclick\b/clique/g' "$file"
    sed -i 's/\bExtract\b/Extraia/g' "$file"
    sed -i 's/\bextract\b/extraia/g' "$file"
    sed -i 's/\bCreate\b/Crie/g' "$file"
    sed -i 's/\bcreate\b/crie/g' "$file"
    sed -i 's/\bPerfect\b/Perfeito/g' "$file"
    sed -i 's/\bperfect\b/perfeito/g' "$file"
    sed -i 's/\bAvailable\b/Disponível/g' "$file"
    sed -i 's/\bavailable\b/disponível/g' "$file"
    sed -i 's/\bInstant\b/Instantâneo/g' "$file"
    sed -i 's/\binstant\b/instantâneo/g' "$file"
    sed -i 's/\bQuality\b/Qualidade/g' "$file"
    sed -i 's/\bquality\b/qualidade/g' "$file"
    sed -i 's/\bWithout\b/Sem/g' "$file"
    sed -i 's/\bwithout\b/sem/g' "$file"
    
    # 动词短语
    sed -i 's/\bwill be\b/será/g' "$file"
    sed -i 's/\bcan be\b/pode ser/g' "$file"
    sed -i 's/\bready to\b/pronto para/g' "$file"
    sed -i 's/\bin seconds\b/em segundos/g' "$file"
    
done

echo "✅ 最终清理完成！"
