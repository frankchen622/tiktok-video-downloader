#!/bin/bash
# 批量翻译西班牙语到葡萄牙语（巴西）

cd /root/.openclaw/workspace/tiktok-video-downloader/frontend/pt

# 翻译 index.html
sed -i 's/lang="es"/lang="pt"/g' index.html
sed -i 's|https://dltk.io/es|https://dltk.io/pt|g' index.html
sed -i 's|/esstatic/|/static/|g' index.html

# Meta 标签翻译
sed -i 's/Descargar Videos de TikTok Sin Marca de Agua - Gratis y Rápido/Baixar Vídeos do TikTok Sem Marca d'\''Água - Grátis e Rápido/g' index.html
sed -i 's/Descarga videos de TikTok sin marca de agua en calidad HD/Baixe vídeos do TikTok sem marca d'\''água em qualidade HD/g' index.html
sed -i 's/Guarda TikTok a MP4 al instante/Salve TikTok em MP4 instantaneamente/g' index.html
sed -i 's/sin app, sin registro/sem app, sem cadastro/g' index.html
sed -i 's/Descargador de videos TikTok 100% gratis/Baixador de vídeos TikTok 100% grátis/g' index.html
sed -i 's/¡Pruébalo ahora!/Experimente agora!/g' index.html
sed -i 's/Descarga videos de TikTok sin marca de agua en segundos/Baixe vídeos do TikTok sem marca d'\''água em segundos/g' index.html
sed -i 's/Calidad HD, sin registro, completamente gratis/Qualidade HD, sem cadastro, completamente grátis/g' index.html

# Schema.org 翻译
sed -i 's/Descargador de Videos TikTok/Baixador de Vídeos TikTok/g' index.html
sed -i 's/Descarga videos de TikTok sin marca de agua en calidad HD\. Gratis, rápido y sin necesidad de registro\./Baixe vídeos do TikTok sem marca d'\''água em qualidade HD. Grátis, rápido e sem necessidade de cadastro./g' index.html
sed -i 's/Descargar videos de TikTok sin marca de agua/Baixar vídeos do TikTok sem marca d'\''água/g' index.html
sed -i 's/Convertir TikTok a audio MP3/Converter TikTok para áudio MP3/g' index.html
sed -i 's/Descargar miniaturas de TikTok/Baixar miniaturas do TikTok/g' index.html
sed -i 's/Guardar historias de TikTok/Salvar stories do TikTok/g' index.html
sed -i 's/Descargas en calidad HD/Downloads em qualidade HD/g' index.html
sed -i 's/Sin necesidad de registro/Sem necessidade de cadastro/g' index.html
sed -i 's/Gratis e ilimitado/Grátis e ilimitado/g' index.html

# FAQ Schema 翻译
sed -i 's/¿DLTK es gratis?/O DLTK é grátis?/g' index.html
sed -i 's/Sí, DLTK es completamente gratuito\./Sim, o DLTK é completamente gratuito./g' index.html
sed -i 's/No hay tarifas ocultas, límites o requisitos de registro\./Não há taxas ocultas, limites ou requisitos de cadastro./g' index.html
sed -i 's/Puedes descargar tantos videos de TikTok como quieras sin pagar nada\./Você pode baixar quantos vídeos do TikTok quiser sem pagar nada./g' index.html

sed -i 's/¿Cómo descargo videos de TikTok sin marca de agua?/Como faço para baixar vídeos do TikTok sem marca d'\''água?/g' index.html
sed -i 's/Abre la aplicación TikTok y encuentra el video que quieres descargar\./Abra o aplicativo TikTok e encontre o vídeo que deseja baixar./g' index.html
sed -i 's/Toca el botón "Compartir"/Toque no botão "Compartilhar"/g' index.html
sed -i 's/Selecciona "Copiar enlace"/Selecione "Copiar link"/g' index.html
sed -i 's/Pega el enlace en el cuadro de arriba y haz clic en "Descargar"\./Cole o link na caixa acima e clique em "Baixar"./g' index.html
sed -i 's/Tu video se descargará sin marca de agua en segundos\./Seu vídeo será baixado sem marca d'\''água em segundos./g' index.html

sed -i 's/¿Puedo usar DLTK en mi teléfono?/Posso usar o DLTK no meu celular?/g' index.html
sed -i 's/¡Por supuesto! DLTK funciona en todos los dispositivos/Claro! O DLTK funciona em todos os dispositivos/g' index.html
sed -i 's/iPhone, Android, tabletas y computadoras de escritorio\./iPhone, Android, tablets e computadores./g' index.html
sed -i 's/Solo necesitas un navegador web, no se requiere instalar ninguna aplicación\./Você só precisa de um navegador, não é necessário instalar nenhum aplicativo./g' index.html

sed -i 's/¿Los videos descargados tienen marca de agua?/Os vídeos baixados têm marca d'\''água?/g' index.html
sed -i 's/¡No! DLTK elimina automáticamente la marca de agua de TikTok\./Não! O DLTK remove automaticamente a marca d'\''água do TikTok./g' index.html
sed -i 's/Obtendrás videos limpios en alta calidad sin ningún logotipo ni texto superpuesto\./Você receberá vídeos limpos em alta qualidade sem nenhum logotipo ou texto sobreposto./g' index.html

sed -i 's/¿Necesito crear una cuenta?/Preciso criar uma conta?/g' index.html
sed -i 's/No, DLTK no requiere registro ni inicio de sesión\./Não, o DLTK não requer cadastro nem login./g' index.html
sed -i 's/Simplemente pega el enlace del video y descárgalo al instante\./Simplesmente cole o link do vídeo e baixe instantaneamente./g' index.html
sed -i 's/Tu privacidad es nuestra prioridad\./Sua privacidade é nossa prioridade./g' index.html

echo "Fase 1 de tradução concluída: Meta tags e Schema"
