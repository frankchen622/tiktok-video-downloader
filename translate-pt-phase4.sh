#!/bin/bash
# Phase 4: 剩余FAQ和页脚翻译

cd /root/.openclaw/workspace/tiktok-video-downloader/frontend/pt

# 更多FAQ
sed -i 's/¿DLTK funciona en teléfonos móviles?/O DLTK funciona em celulares?/g' index.html
sed -i 's/Sí, nuestro descargador gratuito funciona perfectamente en todos los dispositivos móviles/Sim, nosso baixador gratuito funciona perfeitamente em todos os dispositivos móveis/g' index.html
sed -i 's/incluyendo teléfonos Android, iPhones y tablets/incluindo celulares Android, iPhones e tablets/g' index.html
sed -i 's/Descarga videos de TikTok en cualquier dispositivo con navegador web/Baixe vídeos do TikTok em qualquer dispositivo com navegador/g' index.html

sed -i 's/¿Puedo descargar mis propios videos de TikTok?/Posso baixar meus próprios vídeos do TikTok?/g' index.html
sed -i 's/Con el descargador de videos TikTok de DLTK, para descargar tus propios videos de TikTok/Com o baixador de vídeos TikTok do DLTK, para baixar seus próprios vídeos do TikTok/g' index.html
sed -i 's/simplemente copia el enlace de tu perfil y pégalo en DLTK/simplesmente copie o link do seu perfil e cole no DLTK/g' index.html
sed -i 's/Nuestro descargador de videos TikTok funciona para tu propio contenido igual que cualquier otro video/Nosso baixador de vídeos TikTok funciona para seu próprio conteúdo igual a qualquer outro vídeo/g' index.html
sed -i 's/Puedes descargar videos de TikTok que creaste en calidad HD sin marca de agua/Você pode baixar vídeos do TikTok que criou em qualidade HD sem marca d'\''água/g' index.html

sed -i 's/¿Por qué mi video descargado está borroso?/Por que meu vídeo baixado está embaçado?/g' index.html
sed -i 's/Si tu video descargado aparece borroso, la subida original puede ser de baja resolución/Se seu vídeo baixado aparece embaçado, o upload original pode ter baixa resolução/g' index.html
sed -i 's/DLTK preserva la calidad original del video/O DLTK preserva a qualidade original do vídeo/g' index.html
sed -i 's/no podemos mejorar más allá de lo que TikTok almacenó/não podemos melhorar além do que o TikTok armazenou/g' index.html
sed -i 's/Siempre selecciona la opción de más alta calidad/Sempre selecione a opção de maior qualidade/g' index.html
sed -i 's/al descargar videos de TikTok para mejores resultados/ao baixar vídeos do TikTok para melhores resultados/g' index.html

sed -i 's/¿Puedo descargar videos de TikTok de cuentas privadas?/Posso baixar vídeos do TikTok de contas privadas?/g' index.html
sed -i 's/No, no puedes descargar videos de TikTok de cuentas privadas a menos que sigas esa cuenta/Não, você não pode baixar vídeos do TikTok de contas privadas a menos que siga essa conta/g' index.html
sed -i 's/La configuración de privacidad de TikTok impide el acceso público a videos privados/As configurações de privacidade do TikTok impedem o acesso público a vídeos privados/g' index.html
sed -i 's/Nuestro descargador de TikTok solo puede descargar videos de TikTok disponibles públicamente/Nosso baixador de TikTok só pode baixar vídeos do TikTok disponíveis publicamente/g' index.html

sed -i 's/¿Por qué mi video todavía tiene marca de agua?/Por que meu vídeo ainda tem marca d'\''água?/g' index.html
sed -i 's/Si tu video descargado todavía muestra marca de agua/Se seu vídeo baixado ainda mostra marca d'\''água/g' index.html
sed -i 's/intenta actualizar la página y descargar nuevamente/tente atualizar a página e baixar novamente/g' index.html
sed -i 's/Asegúrate de usar el botón "Descargar Sin Marca de Agua" de DLTK/Certifique-se de usar o botão "Baixar Sem Marca d'\''Água" do DLTK/g' index.html
sed -i 's/Ocasionalmente, TikTok cambia su sistema/Ocasionalmente, o TikTok muda seu sistema/g' index.html
sed -i 's/si el problema persiste, el video puede tener la marca de agua incrustada en el archivo original/se o problema persistir, o vídeo pode ter a marca d'\''água incorporada no arquivo original/g' index.html

sed -i 's/¿Puedo descargar varios videos a la vez?/Posso baixar vários vídeos de uma vez?/g' index.html
sed -i 's/Actualmente, DLTK procesa un video de TikTok a la vez/Atualmente, o DLTK processa um vídeo do TikTok por vez/g' index.html
sed -i 's/para velocidad y calidad óptimas/para velocidade e qualidade ideais/g' index.html
sed -i 's/Para descargas por lotes, simplemente pega cada enlace uno por uno/Para downloads em lote, simplesmente cole cada link um por um/g' index.html
sed -i 's/nuestro rápido descargador de TikTok procesa videos en segundos/nosso rápido baixador de TikTok processa vídeos em segundos/g' index.html
sed -i 's/Recomendamos descargar videos de TikTok individualmente/Recomendamos baixar vídeos do TikTok individualmente/g' index.html
sed -i 's/para asegurar la mejor calidad y confiabilidad/para garantir a melhor qualidade e confiabilidade/g' index.html

echo "Phase 4 完成：剩余FAQ翻译"
