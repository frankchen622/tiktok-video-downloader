#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# miniatura.html 的翻译
miniatura_replacements = [
    (
        r'"name": "How do I download TikTok thumbnails\?"',
        '"name": "¿Cómo descargo miniaturas de TikTok?"'
    ),
    (
        r'"text": "Copy the TikTok video link, paste it into DLTK\'s thumbnail downloader, and click Get Thumbnail\. The cover image will be extracted and ready to download in seconds\."',
        '"text": "Copia el enlace del video de TikTok, pégalo en el descargador de miniaturas de DLTK y haz clic en Obtener Miniatura. La imagen de portada será extraída y estará lista para descargar en segundos."'
    ),
    (
        r'"name": "What quality are downloaded TikTok thumbnails\?"',
        '"name": "¿En qué calidad se descargan las miniaturas de TikTok?"'
    ),
    (
        r'"text": "You can download TikTok thumbnails in up to Full HD \(1080x1920\) resolution - the highest quality available from the original video\."',
        '"text": "Puedes descargar miniaturas de TikTok en resolución Full HD (1080x1920) - la más alta calidad disponible del video original."'
    ),
    (
        r'"name": "How to Download TikTok Thumbnails"',
        '"name": "Cómo Descargar Miniaturas de TikTok"'
    ),
    (
        r'"description": "Step-by-step guide to download TikTok cover images and thumbnails using DLTK"',
        '"description": "Guía paso a paso para descargar imágenes de portada y miniaturas de TikTok usando DLTK"'
    ),
    (
        r'"name": "Copy TikTok Video Link"',
        '"name": "Copiar Enlace del Video de TikTok"'
    ),
    (
        r'"text": "Open TikTok, find the video, tap Share, and select \'Copy link\'"',
        '"text": "Abre TikTok, encuentra el video, toca Compartir y selecciona \'Copiar enlace\'"'
    ),
    (
        r'"name": "Paste Link into DLTK Thumbnail Downloader"',
        '"name": "Pegar Enlace en el Descargador de Miniaturas de DLTK"'
    ),
    (
        r'"text": "Go to DLTK\.io and paste the TikTok link into the thumbnail downloader input field"',
        '"text": "Ve a DLTK.io y pega el enlace de TikTok en el campo de entrada del descargador de miniaturas"'
    ),
    (
        r'"name": "Download TikTok Thumbnail"',
        '"name": "Descargar Miniatura de TikTok"'
    ),
    (
        r'"text": "Click Get Thumbnail and download the cover image in high resolution"',
        '"text": "Haz clic en Obtener Miniatura y descarga la imagen de portada en alta resolución"'
    ),
]

# historia.html 的翻译
historia_replacements = [
    (
        r'"name": "How do I download TikTok stories\?"',
        '"name": "¿Cómo descargo historias de TikTok?"'
    ),
    (
        r'"text": "Copy the TikTok story link, paste it into DLTK\'s story downloader, and click Download Story\. The story will be saved without watermark in seconds\."',
        '"text": "Copia el enlace de la historia de TikTok, pégalo en el descargador de historias de DLTK y haz clic en Descargar Historia. La historia será guardada sin marca de agua en segundos."'
    ),
    (
        r'"name": "Can I download TikTok stories before they expire\?"',
        '"name": "¿Puedo descargar historias de TikTok antes de que expiren?"'
    ),
    (
        r'"text": "Yes! Download TikTok stories within 24 hours before they disappear\. Once downloaded, you can keep them forever\."',
        '"text": "¡Sí! Descarga historias de TikTok dentro de las 24 horas antes de que desaparezcan. Una vez descargadas, puedes guardarlas para siempre."'
    ),
    (
        r'"name": "How to Download TikTok Stories"',
        '"name": "Cómo Descargar Historias de TikTok"'
    ),
    (
        r'"description": "Step-by-step guide to download TikTok stories before they expire using DLTK"',
        '"description": "Guía paso a paso para descargar historias de TikTok antes de que expiren usando DLTK"'
    ),
    (
        r'"name": "Copy TikTok Story Link"',
        '"name": "Copiar Enlace de la Historia de TikTok"'
    ),
    (
        r'"text": "Open TikTok, find the story, tap Share, and select \'Copy link\'"',
        '"text": "Abre TikTok, encuentra la historia, toca Compartir y selecciona \'Copiar enlace\'"'
    ),
    (
        r'"name": "Paste Link into DLTK Story Downloader"',
        '"name": "Pegar Enlace en el Descargador de Historias de DLTK"'
    ),
    (
        r'"text": "Return to DLTK\.io and paste the TikTok story link into the input field"',
        '"text": "Regresa a DLTK.io y pega el enlace de la historia de TikTok en el campo de entrada"'
    ),
    (
        r'"name": "Download TikTok Story"',
        '"name": "Descargar Historia de TikTok"'
    ),
    (
        r'"text": "Click Download Story and save it without watermark before it expires"',
        '"text": "Haz clic en Descargar Historia y guárdala sin marca de agua antes de que expire"'
    ),
]

# 读取并修复文件
def fix_file(filename, replacements):
    with open(f'frontend/es/{filename}', 'r', encoding='utf-8') as f:
        content = f.read()
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    with open(f'frontend/es/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Fixed {filename}")

# 执行修复
fix_file('miniatura.html', miniatura_replacements)
fix_file('historia.html', historia_replacements)

print("\n✅ 所有翻译已修复！")
