#!/bin/bash
# Phase 3: 功能特性和FAQ翻译

cd /root/.openclaw/workspace/tiktok-video-downloader/frontend/pt

# 功能特性标题
sed -i 's/Por Qué Elegir DLTK como Tu Descargador de TikTok/Por Que Escolher o DLTK como Seu Baixador de TikTok/g' index.html

# Feature 1
sed -i 's/Sin Marca de Agua/Sem Marca d'\''Água/g' index.html
sed -i 's/Descarga videos de TikTok sin marca de agua en calidad HD original\./Baixe vídeos do TikTok sem marca d'\''água em qualidade HD original./g' index.html
sed -i 's/Nuestro descargador elimina la marca de agua de TikTok automáticamente/Nosso baixador remove a marca d'\''água do TikTok automaticamente/g' index.html

# Feature 2
sed -i 's/Descarga Rápida/Download Rápido/g' index.html
sed -i 's/Descarga videos de TikTok en segundos/Baixe vídeos do TikTok em segundos/g' index.html
sed -i 's/Nuestro descargador de alta velocidad procesa videos al instante/Nosso baixador de alta velocidade processa vídeos instantaneamente/g' index.html

# Feature 3
sed -i 's/100% Gratuito/100% Grátis/g' index.html
sed -i 's/Descarga ilimitada de videos de TikTok sin tarifas ocultas/Download ilimitado de vídeos do TikTok sem taxas ocultas/g' index.html
sed -i 's/Sin registro, sin suscripción, completamente gratis para siempre/Sem cadastro, sem assinatura, completamente grátis para sempre/g' index.html

# Feature 4
sed -i 's/Descarga de Miniaturas/Download de Miniaturas/g' index.html
sed -i 's/Extrae y descarga miniaturas de TikTok en alta resolución/Extraia e baixe miniaturas do TikTok em alta resolução/g' index.html

# Feature 5
sed -i 's/Conversión a MP3/Conversão para MP3/g' index.html
sed -i 's/Convierte videos de TikTok a MP3 y descarga solo el audio/Converta vídeos do TikTok para MP3 e baixe apenas o áudio/g' index.html

# Feature 6
sed -i 's/Todos los Dispositivos/Todos os Dispositivos/g' index.html
sed -i 's/Funciona en iPhone, Android, PC, Mac y cualquier dispositivo/Funciona em iPhone, Android, PC, Mac e qualquer dispositivo/g' index.html
sed -i 's/sin necesidad de instalar aplicaciones/sem necessidade de instalar aplicativos/g' index.html

# Feature 7
sed -i 's/Calidad HD/Qualidade HD/g' index.html
sed -i 's/Descarga videos de TikTok en múltiples calidades/Baixe vídeos do TikTok em múltiplas qualidades/g' index.html
sed -i 's/incluyendo 4K cuando esté disponible/incluindo 4K quando disponível/g' index.html

# Feature 8
sed -i 's/Privado y Seguro/Privado e Seguro/g' index.html
sed -i 's/Tus descargas son privadas/Seus downloads são privados/g' index.html
sed -i 's/No almacenamos tus videos ni rastreamos tu actividad/Não armazenamos seus vídeos nem rastreamos sua atividade/g' index.html

# FAQ 问题
sed -i 's/Preguntas Frecuentes/Perguntas Frequentes/g' index.html
sed -i 's/¿En qué calidad puedo descargar videos de TikTok?/Em que qualidade posso baixar vídeos do TikTok?/g' index.html
sed -i 's/Puedes descargar videos en múltiples opciones de calidad/Você pode baixar vídeos em múltiplas opções de qualidade/g' index.html
sed -i 's/Nuestro descargador de videos TikTok preserva la calidad original del video/Nosso baixador de vídeos TikTok preserva a qualidade original do vídeo/g' index.html
sed -i 's/así obtienes las mejores descargas posibles/assim você obtém os melhores downloads possíveis/g' index.html

sed -i 's/¿Es legal descargar videos de TikTok?/É legal baixar vídeos do TikTok?/g' index.html
sed -i 's/Descargar videos de TikTok para uso personal es generalmente aceptable/Baixar vídeos do TikTok para uso pessoal é geralmente aceitável/g' index.html
sed -i 's/Sin embargo, nunca redistribuyas ni uses contenido descargado comercialmente sin el permiso del creador/No entanto, nunca redistribua ou use conteúdo baixado comercialmente sem a permissão do criador/g' index.html
sed -i 's/Siempre respeta los derechos de autor y da crédito a los creadores originales/Sempre respeite os direitos autorais e dê crédito aos criadores originais/g' index.html

echo "Phase 3 完成：功能特性和FAQ翻译"
