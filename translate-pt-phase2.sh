#!/bin/bash
# 葡萄牙语翻译 Phase 2: index.html 页面主体内容

cd /root/.openclaw/workspace/tiktok-video-downloader/frontend/pt

# HowTo Schema
sed -i 's/Cómo Descargar Videos de TikTok Sin Marca de Agua/Como Baixar Vídeos do TikTok Sem Marca d'\''Água/g' index.html
sed -i 's/Guía paso a paso para descargar videos de TikTok sin marca de agua usando DLTK/Guia passo a passo para baixar vídeos do TikTok sem marca d'\''água usando DLTK/g' index.html
sed -i 's/Copiar Enlace del Video de TikTok/Copiar Link do Vídeo do TikTok/g' index.html
sed -i 's/Abre TikTok, encuentra el video que quieres guardar, toca Compartir y selecciona/Abra o TikTok, encontre o vídeo que deseja salvar, toque em Compartilhar e selecione/g' index.html
sed -i "s/'Copiar enlace'/'Copiar link'/g" index.html
sed -i 's/Pegar Enlace en DLTK/Colar Link no DLTK/g' index.html
sed -i 's/Regresa a DLTK\.io y pega el enlace copiado de TikTok en el campo de entrada arriba/Volte ao DLTK.io e cole o link copiado do TikTok no campo de entrada acima/g' index.html
sed -i 's/Descargar Video de TikTok/Baixar Vídeo do TikTok/g' index.html
sed -i 's/Haz clic en el botón Descargar y elige tu calidad preferida/Clique no botão Baixar e escolha sua qualidade preferida/g' index.html

# 导航栏
sed -i 's/data-i18n="nav_video">Video/data-i18n="nav_video">Vídeo/g' index.html
sed -i 's/data-i18n="nav_thumbnail">Miniatura/data-i18n="nav_thumbnail">Miniatura/g' index.html
sed -i 's/data-i18n="nav_story">Historia/data-i18n="nav_story">Story/g' index.html

# Hero 标题
sed -i 's/Descargar Videos de TikTok Sin Marca de Agua/Baixar Vídeos do TikTok Sem Marca d'\''Água/g' index.html
sed -i 's/Gratis, Rápido y en Calidad HD/Grátis, Rápido e em Qualidade HD/g' index.html
sed -i 's/DLTK es un descargador gratuito de videos de TikTok que elimina marcas de agua automáticamente/O DLTK é um baixador gratuito de vídeos do TikTok que remove marcas d'\''água automaticamente/g' index.html
sed -i 's/Descarga videos de TikTok en calidad HD, conviértelos a MP3 o guarda miniaturas/Baixe vídeos do TikTok em qualidade HD, converta para MP3 ou salve miniaturas/g' index.html
sed -i 's/todo en un solo lugar/tudo em um só lugar/g' index.html
sed -i 's/Sin necesidad de app, sin registro requerido/Sem necessidade de app, sem cadastro necessário/g' index.html
sed -i 's/Rápido, simple y funciona en todos los dispositivos/Rápido, simples e funciona em todos os dispositivos/g' index.html

# 输入框和按钮
sed -i 's/Pega aquí el enlace del video de TikTok/Cole aqui o link do vídeo do TikTok/g' index.html
sed -i 's/placeholder="https:\/\/www\.tiktok\.com\/@usuario\/video\/123456789"/placeholder="https:\/\/www.tiktok.com\/@usuario\/video\/123456789"/g' index.html
sed -i 's/>Descargar</>Baixar</g' index.html

# 使用步骤
sed -i 's/Cómo Usar el Descargador de Videos TikTok/Como Usar o Baixador de Vídeos TikTok/g' index.html
sed -i 's/Copia el Enlace/Copie o Link/g' index.html
sed -i 's/Abre TikTok y copia el enlace del video/Abra o TikTok e copie o link do vídeo/g' index.html
sed -i 's/Pega y Descarga/Cole e Baixe/g' index.html
sed -i 's/Pega el enlace aquí y haz clic en Descargar/Cole o link aqui e clique em Baixar/g' index.html
sed -i 's/Guarda el Video/Salve o Vídeo/g' index.html
sed -i 's/Descarga tu video de TikTok en segundos/Baixe seu vídeo do TikTok em segundos/g' index.html

echo "Phase 2 完成：页面主体内容翻译"
