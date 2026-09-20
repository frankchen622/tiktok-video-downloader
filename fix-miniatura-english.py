#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 修复 miniatura.html
filepath = 'frontend/es/miniatura.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Meta 标签
    (
        r'<meta name="description" content="Download TikTok thumbnails and cover images in HD\. Free thumbnail downloader - save video cover photos instantly\. No watermarks, high quality\." />',
        '<meta name="description" content="Descarga miniaturas e imágenes de portada de TikTok en HD. Descargador de miniaturas gratis - guarda fotos de portada de videos al instante. Sin marcas de agua, alta calidad." />'
    ),
    (
        r'<meta property="og:description" content="Download TikTok thumbnails in HD\. Free, instant, no watermarks\." />',
        '<meta property="og:description" content="Descarga miniaturas de TikTok en HD. Gratis, instantáneo, sin marcas de agua." />'
    ),
    (
        r'<meta name="twitter:description" content="Download TikTok thumbnails in HD\. Free, instant, no watermarks\." />',
        '<meta name="twitter:description" content="Descarga miniaturas de TikTok en HD. Gratis, instantáneo, sin marcas de agua." />'
    ),
    # Schema description
    (
        r'"description": "Download TikTok thumbnails and cover images in HD quality\. Free and fast thumbnail extraction tool\."',
        '"description": "Descarga miniaturas e imágenes de portada de TikTok en calidad HD. Herramienta de extracción de miniaturas gratis y rápida."'
    ),
    # Use Cases
    (
        r'Download TikTok thumbnails to create eye-catching social media posts\. Use cover images for Instagram stories, Facebook posts, Twitter headers, or Pinterest pins\. TikTok thumbnails make great visual content for cross-platform sharing\.',
        'Descarga miniaturas de TikTok para crear publicaciones llamativas en redes sociales. Usa imágenes de portada para historias de Instagram, publicaciones de Facebook, encabezados de Twitter o pines de Pinterest. Las miniaturas de TikTok son excelente contenido visual para compartir entre plataformas.'
    ),
    (
        r'Download TikTok thumbnails for graphic design, mood boards, or creative projects\. Use cover images in presentations, portfolios, or as design inspiration for your own content\.',
        'Descarga miniaturas de TikTok para diseño gráfico, tableros de inspiración o proyectos creativos. Usa imágenes de portada en presentaciones, portafolios o como inspiración de diseño para tu propio contenido.'
    ),
    (
        r'Save TikTok thumbnails for market research, trend analysis, or competitive studies\. Download cover images to analyze visual strategies, color schemes, and thumbnail effectiveness across different niches\.',
        'Guarda miniaturas de TikTok para investigación de mercado, análisis de tendencias o estudios competitivos. Descarga imágenes de portada para analizar estrategias visuales, esquemas de colores y efectividad de miniaturas en diferentes nichos.'
    ),
    (
        r'Download TikTok thumbnails to create personal galleries of your favorite videos, creators, or trends\. Save memorable cover photos from dance challenges, comedy sketches, or educational content\.',
        'Descarga miniaturas de TikTok para crear galerías personales de tus videos, creadores o tendencias favoritas. Guarda fotos de portada memorables de desafíos de baile, sketches de comedia o contenido educativo.'
    ),
    (
        r'Save TikTok cover images and use them as profile pictures, avatars, or wallpapers\. Download thumbnails of yourself or your favorite creators for personal use\.',
        'Guarda imágenes de portada de TikTok y úsalas como fotos de perfil, avatares o fondos de pantalla. Descarga miniaturas de ti mismo o de tus creadores favoritos para uso personal.'
    ),
    # Quality Section
    (
        r'When you download TikTok thumbnails with DLTK, we extract images in the highest quality available:',
        'Cuando descargas miniaturas de TikTok con DLTK, extraemos imágenes en la más alta calidad disponible:'
    ),
    (
        r'<strong>Full HD \(1080x1920\)</strong> - Best quality for modern TikTok videos\. Perfect for professional use and high-resolution displays\.',
        '<strong>Full HD (1080x1920)</strong> - Mejor calidad para videos modernos de TikTok. Perfecto para uso profesional y pantallas de alta resolución.'
    ),
    (
        r'<strong>HD \(720x1280\)</strong> - Standard quality for most TikTok content\. Great balance between file size and image clarity\.',
        '<strong>HD (720x1280)</strong> - Calidad estándar para la mayoría del contenido de TikTok. Gran equilibrio entre tamaño de archivo y claridad de imagen.'
    ),
    (
        r'<strong>SD \(480x854\)</strong> - Basic quality for older videos\. Smaller file size, suitable for web use and quick previews\.',
        '<strong>SD (480x854)</strong> - Calidad básica para videos antiguos. Tamaño de archivo más pequeño, adecuado para uso web y vistas previas rápidas.'
    ),
    (
        r'Downloaded TikTok thumbnails are saved as <strong>JPG/JPEG</strong> images - the most universal and compatible format\. JPG images work everywhere: social media platforms, image editors, presentations, and websites\.',
        'Las miniaturas de TikTok descargadas se guardan como imágenes <strong>JPG/JPEG</strong> - el formato más universal y compatible. Las imágenes JPG funcionan en todas partes: plataformas de redes sociales, editores de imágenes, presentaciones y sitios web.'
    ),
    (
        r'<strong>Note:</strong> The maximum thumbnail quality depends on the original TikTok video upload\. Our downloader automatically extracts the best available resolution\.',
        '<strong>Nota:</strong> La calidad máxima de la miniatura depende de la subida del video original de TikTok. Nuestro descargador extrae automáticamente la mejor resolución disponible.'
    ),
    # Testimonials
    (
        r'<h2>What Users Say About DLTK Thumbnail Downloader</h2>',
        '<h2>Lo Que Dicen los Usuarios Sobre el Descargador de Miniaturas DLTK</h2>'
    ),
    (
        r'"Finally, a TikTok downloader that works on iPhone without installing apps\. The quality is perfect and it\'s super fast!"',
        '"¡Finalmente, un descargador de TikTok que funciona en iPhone sin instalar apps. La calidad es perfecta y es súper rápido!"'
    ),
    (
        r'"I love that it\'s completely free with no ads\. Downloads are instant and the HD quality is amazing\. Highly recommend!"',
        '"Me encanta que sea completamente gratis sin anuncios. Las descargas son instantáneas y la calidad HD es increíble. ¡Muy recomendado!"'
    ),
    # FAQ
    (
        r'Yes, DLTK is completely free\. You can download TikTok thumbnails with no sign-up, no premium tier, and unlimited downloads\. It\'s a 100% free thumbnail downloader forever\.',
        'Sí, DLTK es completamente gratis. Puedes descargar miniaturas de TikTok sin registro, sin plan premium y descargas ilimitadas. Es un descargador de miniaturas 100% gratis para siempre.'
    ),
    (
        r'<dt>What quality are downloaded TikTok thumbnails\?</dt>',
        '<dt>¿En qué calidad se descargan las miniaturas de TikTok?</dt>'
    ),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✓ Fixed {filepath}")
print(f"✅ 共修复 {len(replacements)} 处翻译")
