#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os

def fix_index_html():
    """修复 index.html 中的英文残留"""
    filepath = 'frontend/es/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replacements = [
        # FAQ 答案中的英文
        (
            r'Puedes descargar videos en múltiples opciones de calidad: HD \(720p\), Full HD \(1080p\) y 4K cuando esté disponible\. Our TikTok video downloader preserves the original video quality, so you get the best possible downloads\.',
            'Puedes descargar videos en múltiples opciones de calidad: HD (720p), Full HD (1080p) y 4K cuando esté disponible. Nuestro descargador de videos TikTok preserva la calidad original del video, así obtienes las mejores descargas posibles.'
        ),
        (
            r'Downloading TikTok videos for personal use is generally acceptable\. However, never redistribute or use downloaded content commercially without the creator\'s permission\. Always respect copyright and give credit to original creators\.',
            'Descargar videos de TikTok para uso personal es generalmente aceptable. Sin embargo, nunca redistribuyas ni uses contenido descargado comercialmente sin el permiso del creador. Siempre respeta los derechos de autor y da crédito a los creadores originales.'
        ),
        (
            r'With DLTK TikTok video downloader, para descargar tus propios videos de TikTok, simplemente copia el enlace de tu perfil y pégalo en DLTK\. Our TikTok video downloader works for your own content just like any other video\. You can download TikTok videos you created in HD quality without watermark\.',
            'Con el descargador de videos TikTok de DLTK, para descargar tus propios videos de TikTok, simplemente copia el enlace de tu perfil y pégalo en DLTK. Nuestro descargador de videos TikTok funciona para tu propio contenido igual que cualquier otro video. Puedes descargar videos de TikTok que creaste en calidad HD sin marca de agua.'
        ),
        (
            r'Si tu video descargado aparece borroso, la subida original puede ser de baja resolución\. DLTK preserves the original video quality - we cannot enhance beyond what TikTok stored\. Always select the highest quality option \(HD or Full HD\) when downloading TikTok videos for best results\.',
            'Si tu video descargado aparece borroso, la subida original puede ser de baja resolución. DLTK preserva la calidad original del video - no podemos mejorar más allá de lo que TikTok almacenó. Siempre selecciona la opción de más alta calidad (HD o Full HD) al descargar videos de TikTok para mejores resultados.'
        ),
        (
            r'Si tu video descargado todavía muestra marca de agua, intenta actualizar la página y descargar nuevamente\. Ensure you\'re using DLTK\'s "Download Without Watermark" button\. Occasionally, TikTok changes their system - if the issue persists, the video may have the watermark embedded in the original file\.',
            'Si tu video descargado todavía muestra marca de agua, intenta actualizar la página y descargar nuevamente. Asegúrate de usar el botón "Descargar Sin Marca de Agua" de DLTK. Ocasionalmente, TikTok cambia su sistema - si el problema persiste, el video puede tener la marca de agua incrustada en el archivo original.'
        ),
        (
            r'Actualmente, DLTK procesa un video de TikTok a la vez para velocidad y calidad óptimas\. For batch downloads, simply paste each link one by one - our fast TikTok downloader processes videos in seconds\. We recommend downloading TikTok videos individually to ensure the best quality and reliability\.',
            'Actualmente, DLTK procesa un video de TikTok a la vez para velocidad y calidad óptimas. Para descargas por lotes, simplemente pega cada enlace uno por uno - nuestro rápido descargador de TikTok procesa videos en segundos. Recomendamos descargar videos de TikTok individualmente para asegurar la mejor calidad y confiabilidad.'
        ),
        (
            r'Ya sea que uses nuestro descargador para ver videos personalmente, crear compilaciones o guardar tu contenido favorito, DLTK provides the fastest and most reliable way to download TikTok videos without watermark\.',
            'Ya sea que uses nuestro descargador para ver videos personalmente, crear compilaciones o guardar tu contenido favorito, DLTK proporciona la forma más rápida y confiable de descargar videos de TikTok sin marca de agua.'
        ),
        # FAQ 问题
        (
            r'<dt>What video quality can I download TikTok videos in\?</dt>',
            '<dt>¿En qué calidad puedo descargar videos de TikTok?</dt>'
        ),
    ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Fixed {filepath}")

def fix_mp3_html():
    """修复 mp3.html 中的英文残留"""
    filepath = 'frontend/es/mp3.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否有英文残留
    english_patterns = [
        r'\bDownload\b',
        r'\bwithout\b',
        r'\bquality\b',
        r'\bour\b',
        r'\bthe best\b'
    ]
    
    has_english = False
    for pattern in english_patterns:
        if re.search(pattern, content) and not re.search(pattern + r'["\']', content):
            has_english = True
            break
    
    if has_english:
        print(f"⚠ {filepath} - 发现英文残留，需要手动检查")
    else:
        print(f"✓ {filepath} - 无明显英文残留")

def fix_miniatura_html():
    """修复 miniatura.html 中的英文残留"""
    filepath = 'frontend/es/miniatura.html'
    fix_mp3_html()  # 使用相同的检查逻辑

def fix_historia_html():
    """修复 historia.html 中的英文残留"""
    filepath = 'frontend/es/historia.html'
    fix_mp3_html()  # 使用相同的检查逻辑

# 执行修复
os.chdir('/root/.openclaw/workspace/tiktok-video-downloader')

print("=== 修复西班牙语页面英文残留 ===\n")
fix_index_html()
print("\n检查其他页面...")
fix_mp3_html()
# fix_miniatura_html()
# fix_historia_html()

print("\n✅ 修复完成！")
