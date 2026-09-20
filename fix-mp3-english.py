#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

filepath = 'frontend/es/mp3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# mp3.html 的大量翻译
replacements = [
    # Feature 1
    (
        r'Download TikTok audio in the best available quality, up to 320kbps MP3\. Our converter preserves the original audio quality from TikTok videos, giving you crystal-clear sound for music, podcasts, or voiceovers\.',
        'Descarga audio de TikTok en la mejor calidad disponible, hasta 320kbps MP3. Nuestro convertidor preserva la calidad de audio original de los videos de TikTok, brindándote sonido cristalino para música, podcasts o narraciones.'
    ),
    # Feature 3
    (
        r'<h3>100% Free TikTok MP3 Downloader</h3>',
        '<h3>Descargador de MP3 TikTok 100% Gratis</h3>'
    ),
    (
        r'Download TikTok audio as MP3 for free with no limits\. No registration, no subscription, no hidden fees\. DLTK is a completely free TikTok to MP3 converter that works forever\.',
        'Descarga audio de TikTok como MP3 gratis sin límites. Sin registro, sin suscripción, sin tarifas ocultas. DLTK es un convertidor de TikTok a MP3 completamente gratis que funciona para siempre.'
    ),
    # Feature 4
    (
        r'Our audio downloader works on iPhone, Android, Windows, Mac, and any device with a web browser\. Download TikTok audio as MP3 from any device without installing apps\.',
        'Nuestro descargador de audio funciona en iPhone, Android, Windows, Mac y cualquier dispositivo con navegador web. Descarga audio de TikTok como MP3 desde cualquier dispositivo sin instalar apps.'
    ),
    # Feature 5
    (
        r'Your privacy matters\. We don\'t store your downloaded TikTok audio files or personal information\. Download TikTok MP3 safely and anonymously with DLTK\.',
        'Tu privacidad importa. No almacenamos tus archivos de audio TikTok descargados ni información personal. Descarga MP3 de TikTok de forma segura y anónima con DLTK.'
    ),
    # Feature 6
    (
        r'Downloaded TikTok audio is saved as MP3 - the most compatible audio format\. Play your TikTok MP3 downloads on any music player, smartphone, tablet, or computer\.',
        'El audio de TikTok descargado se guarda como MP3 - el formato de audio más compatible. Reproduce tus descargas MP3 de TikTok en cualquier reproductor de música, smartphone, tablet o computadora.'
    ),
    # Use Cases Section
    (
        r'<h2>What Can You Do with TikTok MP3 Downloads\?</h2>',
        '<h2>¿Qué Puedes Hacer con Descargas MP3 de TikTok?</h2>'
    ),
    (
        r'Download TikTok audio from your favorite music videos and build offline playlists\. Convert to MP3 to enjoy trending songs, remixes, and covers without an internet connection\.',
        'Descarga audio de TikTok de tus videos musicales favoritos y crea listas de reproducción offline. Convierte a MP3 para disfrutar canciones en tendencia, remixes y covers sin conexión a internet.'
    ),
    (
        r'Extract audio from TikTok educational content, storytelling, and podcast clips\. Download TikTok audio as MP3 to listen to valuable content anytime, anywhere\.',
        'Extrae audio de contenido educativo de TikTok, narración y clips de podcasts. Descarga audio de TikTok como MP3 para escuchar contenido valioso en cualquier momento y lugar.'
    ),
    (
        r'Download TikTok audio for sound effects, memes, and viral audio clips\. Use our MP3 downloader to save funny sounds, transitions, and audio memes for your own videos\.',
        'Descarga audio de TikTok para efectos de sonido, memes y clips de audio virales. Usa nuestro descargador MP3 para guardar sonidos graciosos, transiciones y memes de audio para tus propios videos.'
    ),
    (
        r'Convert to MP3 and create custom ringtones for your phone\. Download TikTok audio of your favorite songs, quotes, or sound effects and set them as ringtones or notification sounds\.',
        'Convierte a MP3 y crea tonos de llamada personalizados para tu teléfono. Descarga audio de TikTok de tus canciones, citas o efectos de sonido favoritos y configúralos como tonos de llamada o sonidos de notificación.'
    ),
    (
        r'Download TikTok audio from language learning videos, educational content, and tutorials\. Convert to MP3 to review lessons offline while commuting or exercising\.',
        'Descarga audio de TikTok de videos de aprendizaje de idiomas, contenido educativo y tutoriales. Convierte a MP3 para repasar lecciones offline mientras viajas o haces ejercicio.'
    ),
    # Quality Section
    (
        r'When you download audio with DLTK, we extract audio in the highest quality available:',
        'Cuando descargas audio con DLTK, extraemos el audio en la más alta calidad disponible:'
    ),
    (
        r'<strong>320kbps \(High Quality\)</strong> - Best audio quality for music and professional use\. Near-CD quality sound with excellent clarity\.',
        '<strong>320kbps (Alta Calidad)</strong> - Mejor calidad de audio para música y uso profesional. Sonido de calidad casi-CD con excelente claridad.'
    ),
    (
        r'<strong>256kbps \(Standard Quality\)</strong> - Great balance between file size and audio quality\. Perfect for most listening scenarios\.',
        '<strong>256kbps (Calidad Estándar)</strong> - Gran equilibrio entre tamaño de archivo y calidad de audio. Perfecto para la mayoría de escenarios de escucha.'
    ),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✓ Fixed {filepath}")
print(f"✅ 共修复 {len(replacements)} 处翻译")
