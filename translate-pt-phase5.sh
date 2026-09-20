#!/bin/bash
# Phase 5: 页脚和最终部分翻译

cd /root/.openclaw/workspace/tiktok-video-downloader/frontend/pt

# 更多FAQ
sed -i 's/¿Cuál es la diferencia entre DLTK y otros descargadores de TikTok?/Qual é a diferença entre o DLTK e outros baixadores de TikTok?/g' index.html
sed -i 's/DLTK es el mejor descargador gratuito/O DLTK é o melhor baixador gratuito/g' index.html
sed -i 's/más rápido, fácil y confiable que otros descargadores de videos de TikTok/mais rápido, fácil e confiável que outros baixadores de vídeos do TikTok/g' index.html
sed -i 's/Ofrecemos descargas HD, sin marcas de agua, conversión a MP3/Oferecemos downloads HD, sem marcas d'\''água, conversão para MP3/g' index.html
sed -i 's/y funcionamos en todos los dispositivos/e funcionamos em todos os dispositivos/g' index.html
sed -i 's/completamente gratis sin anuncios ni registro requerido/completamente grátis sem anúncios ou cadastro necessário/g' index.html

sed -i 's/¿DLTK es seguro de usar?/O DLTK é seguro de usar?/g' index.html
sed -i 's/DLTK es completamente seguro/O DLTK é completamente seguro/g' index.html
sed -i 's/No almacenamos tus videos, no requerimos credenciales de inicio de sesión/Não armazenamos seus vídeos, não exigimos credenciais de login/g' index.html
sed -i 's/ni recopilamos datos personales/nem coletamos dados pessoais/g' index.html
sed -i 's/Nuestro descargador de videos de TikTok funciona de forma segura en tu navegador/Nosso baixador de vídeos do TikTok funciona com segurança em seu navegador/g' index.html
sed -i 's/sin malware ni virus/sem malware ou vírus/g' index.html
sed -i 's/Sin embargo, siempre ten cuidado con sitios descargadores de TikTok desconocidos/No entanto, sempre tenha cuidado com sites baixadores de TikTok desconhecidos/g' index.html
sed -i 's/que solicitan contraseñas o información de pago/que solicitam senhas ou informações de pagamento/g' index.html

# 页脚
sed -i 's/Sobre DLTK/Sobre o DLTK/g' index.html
sed -i 's/Enlaces Rápidos/Links Rápidos/g' index.html
sed -i 's/Legal/Jurídico/g' index.html
sed -i 's/Política de Privacidad/Política de Privacidade/g' index.html
sed -i 's/Términos de Servicio/Termos de Serviço/g' index.html
sed -i 's/Descargo de Responsabilidad/Aviso Legal/g' index.html
sed -i 's/Política de Derechos de Autor/Política de Direitos Autorais/g' index.html
sed -i 's/Política de Cookies/Política de Cookies/g' index.html

# 最终描述
sed -i 's/Ya sea que uses nuestro descargador para ver videos personalmente/Seja você usando nosso baixador para assistir vídeos pessoalmente/g' index.html
sed -i 's/crear compilaciones o guardar tu contenido favorito/criar compilações ou salvar seu conteúdo favorito/g' index.html
sed -i 's/DLTK proporciona la forma más rápida y confiable de descargar videos de TikTok sin marca de agua/o DLTK fornece a forma mais rápida e confiável de baixar vídeos do TikTok sem marca d'\''água/g' index.html
sed -i 's/Nuestro descargador de videos de TikTok soporta descargas HD/Nosso baixador de vídeos do TikTok suporta downloads HD/g' index.html
sed -i 's/conversión a MP3/conversão para MP3/g' index.html
sed -i 's/extracción de miniaturas/extração de miniaturas/g' index.html
sed -i 's/descargas de historias/downloads de stories/g' index.html
sed -i 's/tienes todo lo que necesitas para descargar contenido de TikTok rápida y fácilmente/você tem tudo o que precisa para baixar conteúdo do TikTok rápida e facilmente/g' index.html
sed -i 's/Nuestro descargador de TikTok gratis funciona en todos los dispositivos/Nosso baixador de TikTok grátis funciona em todos os dispositivos/g' index.html
sed -i 's/no requiere registro y elimina marcas de agua automáticamente/não requer cadastro e remove marcas d'\''água automaticamente/g' index.html
sed -i 's/¡Prueba DLTK - el descargador de videos TikTok #1 hoy/Experimente o DLTK - o baixador de vídeos TikTok #1 hoje/g' index.html
sed -i 's/es completamente gratis, sin tarifas ocultas y descargas ilimitadas!/é completamente grátis, sem taxas ocultas e downloads ilimitados!/g' index.html

# 页脚版权
sed -i 's/Descargador de Videos TikTok Gratis Sin Marca de Agua/Baixador de Vídeos TikTok Grátis Sem Marca d'\''Água/g' index.html

# 更新所有内部链接
sed -i 's|href="/es/mp3"|href="/pt/mp3"|g' index.html
sed -i 's|href="/es/miniatura"|href="/pt/miniatura"|g' index.html
sed -i 's|href="/es/historia"|href="/pt/historia"|g' index.html
sed -i 's|href="/es/contacto"|href="/pt/contato"|g' index.html
sed -i 's|href="/es/privacidad"|href="/pt/privacidade"|g' index.html
sed -i 's|href="/es/terminos"|href="/pt/termos"|g' index.html
sed -i 's|href="/es/descargo"|href="/pt/aviso-legal"|g' index.html
sed -i 's|href="/es/dmca"|href="/pt/dmca"|g' index.html
sed -i 's|href="/es/cookies"|href="/pt/cookies"|g' index.html
sed -i 's|href="/es"|href="/pt"|g' index.html

# 更新hreflang标签
sed -i 's|hreflang="es"|hreflang="pt"|g' index.html
sed -i 's|href="https://dltk.io/es"|href="https://dltk.io/pt"|g' index.html

# 添加葡萄牙语hreflang（如果还没有）
if ! grep -q 'hreflang="pt"' index.html; then
    sed -i '/<link rel="alternate" hreflang="es"/a\  <link rel="alternate" hreflang="pt" href="https://dltk.io/pt" />' index.html
fi

echo "Phase 5 完成：页脚和最终翻译"
