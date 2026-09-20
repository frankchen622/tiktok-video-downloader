#!/bin/bash
# 修复葡萄牙语页面中的英文和西班牙语残留

cd /root/.openclaw/workspace/tiktok-video-downloader/frontend/pt

fix_file() {
    local file="$1"
    echo "修复: $file"
    
    # FAQ 混合语言修复
    sed -i 's/You can download TikTok vídeos without watermark with no sign-up, no premium tier, and no limits on how many vídeos you download\. It'\''s a 100% free TikTok vídeo downloader\./Você pode baixar vídeos do TikTok sem marca d'\''água sem cadastro, sem plano premium e sem limites de quantos vídeos você baixa. É um baixador de vídeos TikTok 100% grátis./g' "$file"
    
    sed -i 's/How can I download TikTok vídeos without watermark?/Como faço para baixar vídeos do TikTok sem marca d'\''água?/g' "$file"
    
    sed -i 's/Simplemente copia el link del vídeo de TikTok, pégalo en el campo de DLTK y clique en Baixar\. Our TikTok vídeo downloader automatically removes the watermark and lets you save TikTok vídeos in HD quality\. The entire process takes less than 10 seconds\./Copie o link do vídeo do TikTok, cole no campo do DLTK e clique em Baixar. Nosso baixador de vídeos TikTok remove automaticamente a marca d'\''água e permite que você salve vídeos do TikTok em qualidade HD. O processo inteiro leva menos de 10 segundos./g' "$file"
    
    sed -i 's/Do I need to install an app to download TikTok vídeos?/Preciso instalar um aplicativo para baixar vídeos do TikTok?/g' "$file"
    
    sed -i 's/No\. DLTK é un baixedor web that runs entirely in your browser\. You don'\''t need to download any app or software\. Just visit our website to download TikTok vídeos instantly\./Não. O DLTK é um baixador web que funciona inteiramente em seu navegador. Você não precisa baixar nenhum aplicativo ou software. Apenas visite nosso site para baixar vídeos do TikTok instantaneamente./g' "$file"
    
    sed -i 's/y 4K cuando esté disponible/e 4K quando disponível/g' "$file"
    
    sed -i 's/¡Sí! Nuestro baixedor incluye un convertidor de TikTok a MP3\. You can extract áudio from any TikTok vídeo and save it as an MP3 file\./Sim! Nosso baixador inclui um conversor de TikTok para MP3. Você pode extrair áudio de qualquer vídeo do TikTok e salvá-lo como arquivo MP3./g' "$file"
    
    sed -i 's/Visit our <a href="\/pt\/mp3">TikTok a MP3<\/a> page for áudio downloads\./Visite nossa página <a href="\/pt\/mp3">TikTok para MP3<\/a> para downloads de áudio./g' "$file"
    
    sed -i 's/Posso baixer storys de TikTok?/Posso baixar stories do TikTok?/g' "$file"
    
    sed -i 's/Sim, puedes baixer storys de TikTok antes de que expiren\. Visita nuestro <a href="\/pt\/story">baixedor de storys de TikTok<\/a> para salvar storys permanentemente\./Sim, você pode baixar stories do TikTok antes que expirem. Visite nosso <a href="\/pt\/historia">baixador de stories do TikTok<\/a> para salvar stories permanentemente./g' "$file"
    
    sed -i 's/Como descargo miniaturas de TikTok?/Como faço para baixar miniaturas do TikTok?/g' "$file"
    
    sed -i 's/Usa nuestro <a href="\/pt\/miniatura">baixedor de miniaturas de TikTok<\/a> para salvar imágenes de portada en resolución completa\. Perfect for creating custom thumbnails or saving memorable moments\./Use nosso <a href="\/pt\/miniatura">baixador de miniaturas do TikTok<\/a> para salvar imagens de capa em resolução completa. Perfeito para criar miniaturas personalizadas ou salvar momentos memoráveis./g' "$file"
    
    sed -i 's/Por que elegir DLTK sobre otros baixedores de TikTok?/Por que escolher o DLTK sobre outros baixadores de TikTok?/g' "$file"
    
    sed -i 's/Como descargo mis propios vídeos de TikTok?/Como faço para baixar meus próprios vídeos do TikTok?/g' "$file"
    
    sed -i 's/Por que mi vídeo baixedo de TikTok é de baja qualidade o borroso?/Por que meu vídeo baixado do TikTok está com baixa qualidade ou embaçado?/g' "$file"
    
    sed -i 's/(HD o Full HD)/(HD ou Full HD)/g' "$file"
    
    sed -i 's/¿Son seguros los sitios baixedores de TikTok?/Os sites baixadores de TikTok são seguros?/g' "$file"
    
    # 更多混合语言修复
    sed -i 's/Posso baixar meus próprios vídeos do TikTok?/Posso baixar meus próprios vídeos do TikTok?/g' "$file"
    
    sed -i 's/Por que meu vídeo baixado está embaçado?/Por que meu vídeo baixado está embaçado?/g' "$file"
    
    sed -i 's/Puedo baixer vídeos de TikTok de cuentas privadas?/Posso baixar vídeos do TikTok de contas privadas?/g' "$file"
    
    sed -i 's/No, you cannot download TikTok vídeos from private accounts unless you follow that account\./Não, você não pode baixar vídeos do TikTok de contas privadas a menos que você siga essa conta./g' "$file"
    
    sed -i 's/TikTok'\''s privacy settings prevent public access to private vídeos\./As configurações de privacidade do TikTok impedem o acesso público a vídeos privados./g' "$file"
    
    sed -i 's/Our TikTok downloader can only download publicly available TikTok vídeos\./Nosso baixador de TikTok só pode baixar vídeos do TikTok disponíveis publicamente./g' "$file"
    
    # 更正拼写错误
    sed -i 's/baixedor/baixador/g' "$file"
    sed -i 's/baixedo/baixado/g' "$file"
    sed -i 's/baixer/baixar/g' "$file"
    sed -i 's/descargo/baixo/g' "$file"
    sed -i 's/mis propios/meus próprios/g' "$file"
    sed -i 's/nuestro/nosso/g' "$file"
    sed -i 's/nuestra/nossa/g' "$file"
    
    # 西班牙语疑问词
    sed -i 's/¿Cómo/Como/g' "$file"
    sed -i 's/¿Por qué/Por que/g' "$file"
    sed -i 's/¿Puedo/Posso/g' "$file"
    sed -i 's/¿Son/São/g' "$file"
    sed -i 's/¿Puedes/Você pode/g' "$file"
    
    # 动词变位修正
    sed -i 's/ puedo / posso /g' "$file"
    sed -i 's/ puedes / você pode /g' "$file"
    sed -i 's/ puede / pode /g' "$file"
    sed -i 's/ pueden / podem /g' "$file"
}

# 修复所有页面
for file in index.html mp3.html miniatura.html historia.html; do
    fix_file "$file"
done

for file in pages/*.html; do
    fix_file "$file"
done

echo "✅ 葡萄牙语页面修复完成"
