#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

filepath = 'frontend/es/historia.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 所有需要翻译的英文内容
replacements = [
    # Meta 标签
    (r'<meta name="description" content="Download TikTok stories before they disappear\. Free TikTok TikTok story downloader - save 24-hour stories permanently in HD\. No watermarks, instant download\." />',
     '<meta name="description" content="Descarga historias de TikTok antes de que desaparezcan. Descargador de historias de TikTok gratis - guarda historias de 24 horas permanentemente en HD. Sin marcas de agua, descarga instantánea." />'),
    
    (r'<meta property="og:description" content="Download TikTok stories in HD\. Free, instant, save before expiration\." />',
     '<meta property="og:description" content="Descarga historias de TikTok en HD. Gratis, instantáneo, guarda antes de que expiren." />'),
    
    (r'<meta property="twitter:description" content="Download TikTok stories in HD\. Free, instant, save before expiration\." />',
     '<meta property="twitter:description" content="Descarga historias de TikTok en HD. Gratis, instantáneo, guarda antes de que expiren." />'),
    
    # Schema
    (r'"description": "Download TikTok stories before they expire\. Save 24-hour TikTok story videos permanently in HD quality\."',
     '"description": "Descarga historias de TikTok antes de que expiren. Guarda videos de historias de TikTok de 24 horas permanentemente en calidad HD."'),
    
    # Hero text
    (r'Download TikTok stories before they expire\. Save 24-hour TikTok stories permanently in HD quality with our free TikTok story downloader\. No watermarks, no sign-up, instant download\.',
     'Descarga historias de TikTok antes de que expiren. Guarda historias de TikTok de 24 horas permanentemente en calidad HD con nuestro descargador de historias de TikTok gratis. Sin marcas de agua, sin registro, descarga instantánea.'),
    
    # Features
    (r'<h3>Download Story</h3>',
     '<h3>Descarga Historia</h3>'),
    
    (r'Download TikTok stories within their 24-hour window\. Our downloader processes videos instantly, ensuring you save content before it disappears forever\. Never miss memorable moments, important updates, or trending stories again\.',
     'Descarga historias de TikTok dentro de su ventana de 24 horas. Nuestro descargador procesa videos instantáneamente, asegurando que guardes contenido antes de que desaparezca para siempre. Nunca más pierdas momentos memorables, actualizaciones importantes o historias en tendencia.'),
    
    (r'<h3>Calidad HD Story Downloads</h3>',
     '<h3>Descargas de Historias en Calidad HD</h3>'),
    
    (r'<h3>Download Stories Without Watermarks</h3>',
     '<h3>Descarga Historias Sin Marcas de Agua</h3>'),
    
    (r'Save TikTok stories without watermarks\. Our downloader removes TikTok branding automatically, giving you clean videos perfect for repurposing or personal archives\.',
     'Guarda historias de TikTok sin marcas de agua. Nuestro descargador elimina la marca de TikTok automáticamente, brindándote videos limpios perfectos para reutilización o archivos personales.'),
    
    (r'<h3>100% Free Story Downloader</h3>',
     '<h3>Descargador de Historias 100% Gratis</h3>'),
    
    (r'Download TikTok stories for free with no limits\. No registration, no subscription, no hidden fees\. DLTK is a completely free TikTok TikTok story downloader forever\.',
     'Descarga historias de TikTok gratis sin límites. Sin registro, sin suscripción, sin tarifas ocultas. DLTK es un descargador de historias de TikTok completamente gratis para siempre.'),
    
    (r'Our downloader works on iPhone, Android, Windows, Mac, and any device with a web browser\. Save stories from any device without installing apps\.',
     'Nuestro descargador funciona en iPhone, Android, Windows, Mac y cualquier dispositivo con navegador web. Guarda historias desde cualquier dispositivo sin instalar apps.'),
    
    (r'Your privacy matters\. We don\'t store your downloaded stories or personal information\. Download TikTok stories safely and anonymously with DLTK\.',
     'Tu privacidad importa. No almacenamos tus historias descargadas ni información personal. Descarga historias de TikTok de forma segura y anónima con DLTK.'),
    
    # Use cases list items
    (r'<strong>Content Repurposing</strong> - Download TikTok story to create compilations, highlights, or cross-platform content\.',
     '<strong>Reutilización de Contenido</strong> - Descarga historias de TikTok para crear compilaciones, destacados o contenido multiplataforma.'),
    
    # Use cases section
    (r'<h2>What Can You Do with Downloaded TikTok Stories\?</h2>',
     '<h2>¿Qué Puedes Hacer con Historias de TikTok Descargadas?</h2>'),
    
    (r'Download multiple TikTok stories and combine them into highlight reels or best-of compilations\. Perfect for preserving your favorite creator\'s moments or building narrative sequences\.',
     'Descarga múltiples historias de TikTok y combínalas en carretes de destacados o compilaciones de lo mejor. Perfecto para preservar los momentos de tu creador favorito o construir secuencias narrativas.'),
    
    (r'Save TikTok stories and share them on Instagram, Facebook, Twitter, or YouTube\. Download TikTok story to extend their reach beyond TikTok\'s 24-hour limit\.',
     'Guarda historias de TikTok y compártelas en Instagram, Facebook, Twitter o YouTube. Descarga historias de TikTok para extender su alcance más allá del límite de 24 horas de TikTok.'),
    
    (r'Download your own TikTok stories to create permanent personal archives\. Save memories, special occasions, daily vlogs, or travel stories before they disappear\.',
     'Descarga tus propias historias de TikTok para crear archivos personales permanentes. Guarda recuerdos, ocasiones especiales, vlogs diarios o historias de viaje antes de que desaparezcan.'),
    
    (r'Save brand stories, product launches, event coverage, or promotional content\. Download TikTok stories for marketing analysis, portfolio building, or client presentations\.',
     'Guarda historias de marca, lanzamientos de productos, cobertura de eventos o contenido promocional. Descarga historias de TikTok para análisis de marketing, construcción de portafolio o presentaciones de clientes.'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✓ Fixed {filepath}")
print(f"✅ 共修复 {len(replacements)} 处翻译")
