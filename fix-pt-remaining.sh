#!/bin/bash
# 修复所有葡萄牙语页面的剩余英文

cd /root/.openclaw/workspace/tiktok-video-downloader/frontend/pt

echo "修复 miniatura.html..."

sed -i 's/Our downloader is perfect for various creative and professional uses:/Nosso baixador é perfeito para vários usos criativos e profissionais:/g' miniatura.html

sed -i 's/Save TikTok cover images as reference frames for vídeo editing projects\. Create compilation thumbnails, reaction vídeo covers, or montage posters using downloaded TikTok thumbnails\./Salve imagens de capa do TikTok como quadros de referência para projetos de edição de vídeo. Crie miniaturas de compilação, capas de vídeos de reação ou pôsteres de montagem usando miniaturas do TikTok baixadas./g' miniatura.html

sed -i 's/TikTok thumbnails maintain the standard <strong>9:16 vertical aspect ratio<\/strong> (portrait orientation), perfect for mobile viewing and vertical vídeo platforms like Instagram Reels, YouTube Shorts, and Snapchat\./As miniaturas do TikTok mantêm a <strong>proporção padrão 9:16 vertical<\/strong> (orientação retrato), perfeita para visualização móvel e plataformas de vídeo vertical como Instagram Reels, YouTube Shorts e Snapchat./g' miniatura.html

sed -i 's/"Best TikTok downloader I'\''ve found! Fast, simple, and actually removes the watermark\. I use it daily for my content creation\."/"Melhor baixador de TikTok que encontrei! Rápido, simples e realmente remove a marca d'\''água. Uso diariamente para minha criação de conteúdo."/g' miniatura.html

sed -i 's/Is DLTK thumbnail downloader free?/O baixador de miniaturas DLTK é grátis?/g' miniatura.html

sed -i 's/How do I download TikTok thumbnails?/Como faço para baixar miniaturas do TikTok?/g' miniatura.html

sed -i 's/Simply copy the TikTok vídeo link, paste it into DLTK'\''s thumbnail downloader above, and click "Get Thumbnail"\. The cover image will be extracted and ready to download in seconds\./Simplesmente copie o link do vídeo do TikTok, cole no baixador de miniaturas do DLTK acima e clique em "Obter Miniatura". A imagem de capa será extraída e estará pronta para download em segundos./g' miniatura.html

sed -i 's/You can download TikTok thumbnails in up to Full HD (1080x1920) resolution - the highest quality available from the original vídeo\. Our thumbnail downloader preserves the best possible image quality\./Você pode baixar miniaturas do TikTok em até resolução Full HD (1080x1920) - a mais alta qualidade disponível do vídeo original. Nosso baixador de miniaturas preserva a melhor qualidade de imagem possível./g' miniatura.html

sed -i 's/Can I download TikTok thumbnails on iPhone or Android?/Posso baixar miniaturas do TikTok no iPhone ou Android?/g' miniatura.html

sed -i 's/Yes! Our downloader works on all devices including iPhone, Android, tablets, and computers\. No app installation required - just use your mobile browser to save cover images\./Sim! Nosso baixador funciona em todos os dispositivos incluindo iPhone, Android, tablets e computadores. Não é necessário instalar aplicativo - apenas use seu navegador móvel para salvar imagens de capa./g' miniatura.html

sed -i 's/Are downloaded TikTok thumbnails free of watermarks?/As miniaturas do TikTok baixadas estão livres de marcas d'\''água?/g' miniatura.html

sed -i 's/Yes, our thumbnail downloader extracts the original cover image without watermarks\. You get clean, high-quality TikTok thumbnails perfect for any use\./Sim, nosso baixador de miniaturas extrai a imagem de capa original sem marcas d'\''água. Você obtém miniaturas do TikTok limpas e de alta qualidade perfeitas para qualquer uso./g' miniatura.html

sed -i 's/What format are downloaded TikTok thumbnails?/Em que formato são as miniaturas do TikTok baixadas?/g' miniatura.html

sed -i 's/Downloaded TikTok thumbnails are saved as JPG\/JPEG images - the most universal and compatible format that works on all devices and platforms\./As miniaturas do TikTok baixadas são salvas como imagens JPG\/JPEG - o formato mais universal e compatível que funciona em todos os dispositivos e plataformas./g' miniatura.html

echo "修复 historia.html..."

sed -i 's/Our downloader works on all devices/Nosso baixador funciona em todos os dispositivos/g' historia.html
sed -i 's/No app installation required/Não é necessário instalar aplicativo/g' historia.html
sed -i 's/You can download/Você pode baixar/g' historia.html
sed -i 's/Our TikTok downloader/Nosso baixador de TikTok/g' historia.html
sed -i 's/Simply copy/Simplesmente copie/g' historia.html
sed -i 's/paste it into/cole no/g' historia.html
sed -i 's/and click/e clique/g' historia.html
sed -i 's/The vídeo will be/O vídeo será/g' historia.html
sed -i 's/ready to download/pronto para download/g' historia.html
sed -i 's/in seconds/em segundos/g' historia.html

echo "✅ 所有葡萄牙语页面修复完成"
