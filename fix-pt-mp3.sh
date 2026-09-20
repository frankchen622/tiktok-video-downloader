#!/bin/bash
# 修复 mp3.html 的英文残留

cd /root/.openclaw/workspace/tiktok-video-downloader/frontend/pt

echo "修复 mp3.html..."

sed -i 's/Convert TikTok vídeos to MP3 in seconds\. Our áudio downloader uses advanced technology to extract áudio instantly\. No waiting, no queues - just fast TikTok MP3 downloads every time\./Converta vídeos do TikTok para MP3 em segundos. Nosso baixador de áudio usa tecnologia avançada para extrair áudio instantaneamente. Sem espera, sem filas - apenas downloads rápidos de MP3 do TikTok sempre./g' mp3.html

sed -i 's/Our converter is perfect for various use cases:/Nosso conversor é perfeito para vários casos de uso:/g' mp3.html

sed -i 's/<strong>192kbps (Good Quality)<\/strong> - Smaller file size while maintaining good sound quality\. Ideal for mobile devices with limited storage\./<strong>192kbps (Boa Qualidade)<\/strong> - Tamanho de arquivo menor mantendo boa qualidade de som. Ideal para dispositivos móveis com armazenamento limitado./g' mp3.html

sed -i 's/<strong>128kbps (Basic Quality)<\/strong> - Smallest file size\. Acceptable for casual listening and voice content\./<strong>128kbps (Qualidade Básica)<\/strong> - Menor tamanho de arquivo. Aceitável para audição casual e conteúdo de voz./g' mp3.html

sed -i 's/<strong>Note:<\/strong> The maximum áudio quality depends on the original TikTok vídeo upload\. Our converter automatically selects the best available quality, up to 320kbps when the source supports it\./<strong>Nota:<\/strong> A qualidade máxima de áudio depende do upload original do vídeo do TikTok. Nosso conversor seleciona automaticamente a melhor qualidade disponível, até 320kbps quando a fonte suporta./g' mp3.html

sed -i 's/"Best TikTok downloader I'\''ve found! Fast, simple, and actually removes the watermark\. I use it daily for my content creation\."/"Melhor baixador de TikTok que encontrei! Rápido, simples e realmente remove a marca d'\''água. Uso diariamente para minha criação de conteúdo."/g' mp3.html

sed -i 's/"Finally, a TikTok downloader that works on iPhone without installing apps\. The quality is perfect and it'\''s super fast!"/"Finalmente, um baixador de TikTok que funciona no iPhone sem instalar apps. A qualidade é perfeita e é super rápido!"/g' mp3.html

sed -i 's/"I love that it'\''s completely free with no ads\. Downloads are instant and the HD quality is amazing\. Highly recommend!"/"Adoro que seja completamente grátis sem anúncios. Os downloads são instantâneos e a qualidade HD é incrível. Super recomendo!"/g' mp3.html

sed -i 's/Yes, DLTK is completely free\. You can convert TikTok vídeos to MP3 with no sign-up, no premium tier, and unlimited downloads\. It'\''s a 100% free áudio downloader forever\./Sim, o DLTK é completamente grátis. Você pode converter vídeos do TikTok para MP3 sem cadastro, sem plano premium e downloads ilimitados. É um baixador de áudio 100% grátis para sempre./g' mp3.html

sed -i 's/Simply copy the TikTok vídeo link, paste it into DLTK'\''s TikTok to MP3 converter above, and click "Convert to MP3"\. The áudio will be extracted and ready to download in seconds\./Simplesmente copie o link do vídeo do TikTok, cole no conversor de TikTok para MP3 do DLTK acima e clique em "Converter para MP3". O áudio será extraído e estará pronto para download em segundos./g' mp3.html

sed -i 's/What áudio quality can I download áudio in?/Em que qualidade de áudio posso baixar o áudio?/g' mp3.html

echo "✅ mp3.html 修复完成"
