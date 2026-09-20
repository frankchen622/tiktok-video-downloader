#!/usr/bin/env python3
"""
Final pass: Fix remaining English in German pages
Focus on alt tags, remaining content, and edge cases
"""

import re

def final_german_fixes(filepath):
    """Apply final German translation fixes"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix title tags
        content = content.replace('- Free & Fast', '- Kostenlos & Schnell')
        content = content.replace('Free |', 'Kostenlos |')
        content = content.replace('Save Cover Images Free', 'Cover-Bilder kostenlos speichern')
        content = content.replace('Save Stories Before They Expire', 'Stories speichern bevor sie ablaufen')
        
        # Fix alt tags
        content = content.replace('alt="Herunterladen TikTok Without Watermark"', 'alt="TikTok ohne Wasserzeichen herunterladen"')
        content = content.replace('alt="TikTok video thumbnail preview"', 'alt="TikTok-Video-Miniaturansicht Vorschau"')
        content = content.replace('alt="Video thumbnail"', 'alt="Video-Miniaturansicht"')
        content = content.replace('alt="Story thumbnail"', 'alt="Story-Miniaturansicht"')
        
        # Fix feature descriptions still in English
        content = re.sub(
            r'Herunterladen TikTok videos in HD, Full HD, and even 4K quality when available\. Our TikTok video downloader preserves original video quality for the best viewing experience\.',
            'Laden Sie TikTok-Videos in HD, Full HD und sogar 4K-Qualität herunter, wenn verfügbar. Unser TikTok-Video-Downloader bewahrt die ursprüngliche Videoqualität für das beste Seherlebnis.',
            content
        )
        
        content = re.sub(
            r'Your privacy is our priority\. We don\'t store your downloaded videos or personal information\. Herunterladen TikTok videos safely and anonymously with DLTK\.',
            'Ihre Privatsphäre hat für uns Priorität. Wir speichern weder Ihre heruntergeladenen Videos noch persönliche Informationen. Laden Sie TikTok-Videos sicher und anonym mit DLTK herunter.',
            content
        )
        
        # Fix downloads text
        content = content.replace('10M+ Downloads', '10M+ Heruntergeladen')
        
        # Fix FAQ questions that are still in English
        content = content.replace('Can I download TikTok videos from private accounts?', 'Kann ich TikTok-Videos von privaten Konten herunterladen?')
        content = content.replace('Can I download audio from private accounts?', 'Kann ich Audio von privaten Konten herunterladen?')
        content = content.replace('Can I download thumbnails from private TikTok accounts?', 'Kann ich Miniaturansichten von privaten TikTok-Konten herunterladen?')
        content = content.replace('Can I download TikTok story videos from private TikTok accounts?', 'Kann ich TikTok-Story-Videos von privaten TikTok-Konten herunterladen?')
        
        # Fix specific phrases in content
        content = content.replace('high quality (320kbps) for free', 'hoher Qualität (320kbps) kostenlos')
        content = content.replace('work on all devices', 'funktioniert auf allen Geräten')
        content = content.replace('on all devices', 'auf allen Geräten')
        content = content.replace('and work on all devices', 'und funktioniert auf allen Geräten')
        
        content = content.replace('for the best viewing experience', 'für das beste Seherlebnis')
        content = content.replace('The best free', 'Das beste kostenlose')
        content = content.replace('the best possible', 'die bestmöglichen')
        
        content = content.replace('safely and anonymously', 'sicher und anonym')
        content = content.replace('in your own content', 'in Ihrem eigenen Inhalt')
        content = content.replace('without installing apps', 'ohne Apps zu installieren')
        content = content.replace('from any device', 'von jedem Gerät')
        
        # Fix specific MP3 page content
        content = content.replace('find the video with audio you want to download', 'finden Sie das Video mit dem Audio, das Sie herunterladen möchten')
        
        # Fix miniatur page content
        content = content.replace('Get your TikTok thumbnails faster than any other tool', 'Holen Sie sich Ihre TikTok-Miniaturansichten schneller als mit jedem anderen Tool')
        content = content.replace('Herunterladen TikTok thumbnails and video cover images', 'Laden Sie TikTok-Miniaturansichten und Video-Cover-Bilder herunter')
        
        # Fix story page content
        content = content.replace('Save 24-hour TikTok stories permanently', 'Speichern Sie 24-Stunden-TikTok-Stories dauerhaft')
        content = content.replace('with our free TikTok story downloader', 'mit unserem kostenlosen TikTok-Story-Downloader')
        content = content.replace('Act fast - stories disappear after 24 hours!', 'Handeln Sie schnell - Stories verschwinden nach 24 Stunden!')
        
        # Fix "using" phrases
        content = content.replace("Ensure you're using DLTK's", "Stellen Sie sicher, dass Sie DLTK's")
        content = content.replace('using downloaded TikTok thumbnails', 'mit heruntergeladenen TikTok-Miniaturansichten')
        content = content.replace('using third-party tools like DLTK', 'mit Tools von Drittanbietern wie DLTK')
        content = content.replace('for personal use is fine, but using it', 'für den persönlichen Gebrauch ist in Ordnung, aber die Verwendung')
        
        # Fix device compatibility text
        content = content.replace('and any device with a web browser', 'und jedem Gerät mit einem Webbrowser')
        content = content.replace('to your device', 'auf Ihr Gerät')
        
        # Fix quality mentions
        content = content.replace('in HD quality', 'in HD-Qualität')
        content = content.replace('in high quality', 'in hoher Qualität')
        
        # Fix header/section comments (these are just for developers, but let's make them consistent)
        content = content.replace('<!-- Device Compatibility -->', '<!-- Gerätekompatibilität -->')
        
        # Save if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Applied final fixes to {filepath}")
            return True
        else:
            print(f"ℹ️  No additional fixes needed in {filepath}")
            return False
            
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

if __name__ == "__main__":
    files = [
        "frontend/de/index.html",
        "frontend/de/mp3.html",
        "frontend/de/miniatur.html",
        "frontend/de/story.html"
    ]
    
    print("=" * 60)
    print("Final German Translation Pass")
    print("=" * 60 + "\n")
    
    for filepath in files:
        final_german_fixes(filepath)
    
    print("\n" + "=" * 60)
    print("✅ Final pass completed!")
    print("=" * 60)
