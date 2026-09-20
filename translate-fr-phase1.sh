#!/bin/bash
# 法语翻译脚本 - Phase 1: 基础替换

FR_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/fr"

translate_to_french() {
    local file="$1"
    echo "翻译为法语: $file"
    
    # 语言和URL
    sed -i 's/lang="pt"/lang="fr"/g' "$file"
    sed -i 's|/pt/|/fr/|g' "$file"
    sed -i 's|/pt"|/fr"|g' "$file"
    sed -i 's|href="https://dltk.io/pt|href="https://dltk.io/fr|g' "$file"
    sed -i 's|hreflang="pt"|hreflang="fr"|g' "$file"
    
    # 核心功能词汇
    sed -i 's/Baixar Vídeos do TikTok Sem Marca d'\''Água/Télécharger des Vidéos TikTok Sans Filigrane/g' "$file"
    sed -i 's/Grátis e Rápido/Gratuit et Rapide/g' "$file"
    sed -i 's/Baixe vídeos do TikTok sem marca d'\''água/Téléchargez des vidéos TikTok sans filigrane/g' "$file"
    sed -i 's/em qualidade HD/en qualité HD/g' "$file"
    sed -i 's/Salve TikTok em MP4 instantaneamente/Enregistrez TikTok en MP4 instantanément/g' "$file"
    sed -i 's/sem app, sem cadastro/sans app, sans inscription/g' "$file"
    sed -i 's/Baixador de vídeos TikTok 100% grátis/Téléchargeur de vidéos TikTok 100% gratuit/g' "$file"
    sed -i 's/Experimente agora!/Essayez maintenant!/g' "$file"
    
    # 常用动词 (葡萄牙语 → 法语)
    sed -i 's/\bBaixar\b/Télécharger/g' "$file"
    sed -i 's/\bbaixar\b/télécharger/g' "$file"
    sed -i 's/\bBaixe\b/Téléchargez/g' "$file"
    sed -i 's/\bbaixe\b/téléchargez/g' "$file"
    sed -i 's/\bBaixado\b/Téléchargé/g' "$file"
    sed -i 's/\bbaixado\b/téléchargé/g' "$file"
    sed -i 's/\bBaixador\b/Téléchargeur/g' "$file"
    sed -i 's/\bbaixador\b/téléchargeur/g' "$file"
    
    sed -i 's/\bConverter\b/Convertir/g' "$file"
    sed -i 's/\bconverter\b/convertir/g' "$file"
    sed -i 's/\bConverta\b/Convertissez/g' "$file"
    sed -i 's/\bconverta\b/convertissez/g' "$file"
    sed -i 's/\bConversor\b/Convertisseur/g' "$file"
    sed -i 's/\bconversor\b/convertisseur/g' "$file"
    
    sed -i 's/\bSalvar\b/Enregistrer/g' "$file"
    sed -i 's/\bsalvar\b/enregistrer/g' "$file"
    sed -i 's/\bSalve\b/Enregistrez/g' "$file"
    sed -i 's/\bsalve\b/enregistrez/g' "$file"
    
    sed -i 's/\bCopiar\b/Copier/g' "$file"
    sed -i 's/\bcopiar\b/copier/g' "$file"
    sed -i 's/\bCopie\b/Copiez/g' "$file"
    sed -i 's/\bcopie\b/copiez/g' "$file"
    
    sed -i 's/\bColar\b/Coller/g' "$file"
    sed -i 's/\bcolar\b/coller/g' "$file"
    sed -i 's/\bCole\b/Collez/g' "$file"
    sed -i 's/\bcole\b/collez/g' "$file"
    
    sed -i 's/\bClicar\b/Cliquer/g' "$file"
    sed -i 's/\bclicar\b/cliquer/g' "$file"
    sed -i 's/\bClique\b/Cliquez/g' "$file"
    sed -i 's/\bclique\b/cliquez/g' "$file"
    
    # 名词
    sed -i 's/\bVídeo\b/Vidéo/g' "$file"
    sed -i 's/\bvídeo\b/vidéo/g' "$file"
    sed -i 's/\bVídeos\b/Vidéos/g' "$file"
    sed -i 's/\bvídeos\b/vidéos/g' "$file"
    
    sed -i 's/\bÁudio\b/Audio/g' "$file"
    sed -i 's/\báudio\b/audio/g' "$file"
    
    sed -i 's/\bQualidade\b/Qualité/g' "$file"
    sed -i 's/\bqualidade\b/qualité/g' "$file"
    
    sed -i 's/\bMiniatura\b/Miniature/g' "$file"
    sed -i 's/\bminiatura\b/miniature/g' "$file"
    sed -i 's/\bMiniaturas\b/Miniatures/g' "$file"
    sed -i 's/\bminiaturas\b/miniatures/g' "$file"
    
    sed -i 's/\bStory\b/Story/g' "$file"  # 保持 Story
    sed -i 's/\bstory\b/story/g' "$file"
    sed -i 's/\bStories\b/Stories/g' "$file"
    sed -i 's/\bstories\b/stories/g' "$file"
    
    sed -i 's/Marca d'\''Água/Filigrane/g' "$file"
    sed -i 's/marca d'\''água/filigrane/g' "$file"
    sed -i 's/marcas d'\''água/filigranes/g' "$file"
    
    # 形容词
    sed -i 's/\bGrátis\b/Gratuit/g' "$file"
    sed -i 's/\bgrátis\b/gratuit/g' "$file"
    sed -i 's/\bGratuito\b/Gratuit/g' "$file"
    sed -i 's/\bgratuito\b/gratuit/g' "$file"
    
    sed -i 's/\bRápido\b/Rapide/g' "$file"
    sed -i 's/\brápido\b/rapide/g' "$file"
    
    sed -i 's/\bFácil\b/Facile/g' "$file"
    sed -i 's/\bfácil\b/facile/g' "$file"
    
    sed -i 's/\bSeguro\b/Sûr/g' "$file"
    sed -i 's/\bseguro\b/sûr/g' "$file"
    
    # 介词和连词
    sed -i 's/\bSem\b/Sans/g' "$file"
    sed -i 's/\bsem\b/sans/g' "$file"
    sed -i 's/\bCom\b/Avec/g' "$file"
    sed -i 's/\bcom\b/avec/g' "$file"
    sed -i 's/\be\b/et/g' "$file"
    sed -i 's/\bou\b/ou/g' "$file"
    sed -i 's/\bpara\b/pour/g' "$file"
    sed -i 's/\bPara\b/Pour/g' "$file"
    sed -i 's/\bem\b/en/g' "$file"
    sed -i 's/\bEm\b/En/g' "$file"
    
    echo "  ✓ $file 翻译完成"
}

# 翻译所有文件
for file in "$FR_DIR"/*.html; do
    translate_to_french "$file"
done

for file in "$FR_DIR"/pages/*.html; do
    translate_to_french "$file"
done

echo "✅ Phase 1 完成：基础法语翻译"
