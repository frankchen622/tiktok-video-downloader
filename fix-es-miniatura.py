#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速修复西班牙语页面的英文残留
"""

import os

# 西班牙语翻译对照表（通用）
translations = {
    # 步骤部分
    'Save TikTok cover images in 3 simple steps with our free thumbnail downloader.': 
        'Guarda imágenes de portada de TikTok en 3 simples pasos con nuestro descargador gratuito de miniaturas.',
    'Copy TikTok Video Link': 'Copia el Enlace del Video de TikTok',
    'Open TikTok, find the video whose thumbnail you want to save, tap Share, and select "Copy link". Our downloader works with any public video.':
        'Abre TikTok, encuentra el video cuya miniatura quieres guardar, toca Compartir y selecciona "Copiar enlace". Nuestro descargador funciona con cualquier video público.',
    'Paste Link into DLTK': 'Pega el Enlace en DLTK',
    'Return to DLTK.io and paste the TikTok video link into the input field above. Our thumbnail downloader will extract the cover image instantly.':
        'Regresa a DLTK.io y pega el enlace del video de TikTok en el campo de entrada de arriba. Nuestro descargador de miniaturas extraerá la imagen de portada instantáneamente.',
    'Download Thumbnail Image': 'Descarga la Imagen de Miniatura',
    'Click "Get Thumbnail" and save the TikTok cover image. Your thumbnail download will start immediately in high quality (HD or Full HD resolution).':
        'Haz clic en "Obtener Miniatura" y guarda la imagen de portada de TikTok. Tu descarga de miniatura comenzará inmediatamente en alta calidad (resolución HD o Full HD).',
    
    # 功能特点
    'The best free tool to download TikTok cover images and thumbnails.':
        'La mejor herramienta gratuita para descargar imágenes de portada y miniaturas de TikTok.',
    'High Resolution Thumbnails': 'Miniaturas de Alta Resolución',
    'Download TikTok thumbnails in the highest quality available - up to Full HD (1080p). Our thumbnail downloader preserves the original image resolution, giving you crystal-clear cover photos perfect for social media, design projects, or personal collections.':
        'Descarga miniaturas de TikTok en la más alta calidad disponible - hasta Full HD (1080p). Nuestro descargador de miniaturas preserva la resolución original de la imagen, dándote fotos de portada cristalinas perfectas para redes sociales, proyectos de diseño o colecciones personales.',
    
    'Instant Thumbnail Extraction': 'Extracción Instantánea de Miniaturas',
    'Save TikTok cover images in seconds. Our thumbnail downloader extracts images instantly with no processing delays. Get your TikTok thumbnails faster than any other tool.':
        'Guarda imágenes de portada de TikTok en segundos. Nuestro descargador de miniaturas extrae imágenes instantáneamente sin demoras de procesamiento. Obtén tus miniaturas de TikTok más rápido que con cualquier otra herramienta.',
    
    '100% Gratis Thumbnail Downloader': 'Descargador de Miniaturas 100% Gratis',
    'Download TikTok thumbnails for free with no limits. No registration, no subscription, no hidden fees. DLTK is a completely free thumbnail downloader forever.':
        'Descarga miniaturas de TikTok gratis sin límites. Sin registro, sin suscripción, sin tarifas ocultas. DLTK es un descargador de miniaturas completamente gratuito para siempre.',
    
    'No Watermarks on Images': 'Sin Marcas de Agua en las Imágenes',
    'Save TikTok cover images without watermarks. Our thumbnail downloader extracts the original cover photo without TikTok branding, perfect for clean, professional use.':
        'Guarda imágenes de portada de TikTok sin marcas de agua. Nuestro descargador de miniaturas extrae la foto de portada original sin la marca de TikTok, perfecto para uso limpio y profesional.',
    
    'Works on All Devices': 'Funciona en Todos los Dispositivos',
    'Our downloader works on iPhone, Android, Windows, Mac, and any device with a web browser. Download cover images from any device without installing apps.':
        'Nuestro descargador funciona en iPhone, Android, Windows, Mac y cualquier dispositivo con navegador web. Descarga imágenes de portada desde cualquier dispositivo sin instalar aplicaciones.',
    
    'Safe & Private': 'Seguro y Privado',
    'Your privacy matters. We don\'t store your downloaded thumbnails or personal information. Download TikTok cover images safely and anonymously with DLTK.':
        'Tu privacidad importa. No almacenamos tus miniaturas descargadas ni información personal. Descarga imágenes de portada de TikTok de forma segura y anónima con DLTK.',
    
    # Hero区
    'Download TikTok thumbnails and video cover images in HD quality. Save TikTok cover photos instantly with our free thumbnail downloader. No watermarks, no sign-up, high resolution images.':
        'Descarga miniaturas de TikTok e imágenes de portada de video en calidad HD. Guarda fotos de portada de TikTok instantáneamente con nuestro descargador gratuito de miniaturas. Sin marcas de agua, sin registro, imágenes de alta resolución.',
}

# 处理miniatura.html
filepath = '/root/.openclaw/workspace/tiktok-downloader/frontend/es/miniatura.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

count = 0
for eng, esp in translations.items():
    if eng in html:
        html = html.replace(eng, esp)
        count += 1
        print(f"✅ 替换: {eng[:50]}...")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n📊 miniatura.html: 替换了 {count} 处英文")
print(f"📄 文件大小: {len(html)} 字符")
