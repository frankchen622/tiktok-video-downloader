#!/usr/bin/env python3
"""
Fix German Schema.org structured data - remove English mixed content
"""

import re

def fix_schema_data(filepath):
    """Fix Schema.org structured data in German pages"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix featureList in WebApplication schema
        content = re.sub(
            r'"Herunterladen TikTok videos without watermark"',
            '"TikTok-Videos ohne Wasserzeichen herunterladen"',
            content
        )
        
        content = re.sub(
            r'"Konvertieren TikTok zu MP3 audio"',
            '"TikTok zu MP3-Audio konvertieren"',
            content
        )
        
        content = re.sub(
            r'"Herunterladen TikTok thumbnails"',
            '"TikTok-Miniaturansichten herunterladen"',
            content
        )
        
        content = re.sub(
            r'"Save TikTok stories"',
            '"TikTok-Storys speichern"',
            content
        )
        
        content = re.sub(
            r'"HD quality downloads"',
            '"HD-Qualität Downloads"',
            content
        )
        
        content = re.sub(
            r'"No registration required"',
            '"Keine Registrierung erforderlich"',
            content
        )
        
        content = re.sub(
            r'"Free and unlimited"',
            '"Kostenlos und unbegrenzt"',
            content
        )
        
        # Fix FAQ Schema answers
        content = re.sub(
            r'Using our TikTok video downloader is simple: copy the TikTok video link, paste it into DLTK\'s input field, and click Herunterladen\. Our TikTok video downloader automatically removes the watermark and lets you save TikTok videos in HD quality\. The entire process takes less than 10 seconds\.',
            'Die Verwendung unseres TikTok-Video-Downloaders ist einfach: Kopieren Sie den TikTok-Video-Link, fügen Sie ihn in das Eingabefeld von DLTK ein und klicken Sie auf Herunterladen. Unser TikTok-Video-Downloader entfernt automatisch das Wasserzeichen und ermöglicht es Ihnen, TikTok-Videos in HD-Qualität zu speichern. Der gesamte Vorgang dauert weniger als 10 Sekunden.',
            content
        )
        
        content = re.sub(
            r'No\. DLTK is a web-based TikTok video downloader that runs entirely in your browser\. You don\'t need to download any app or software\. Just visit our website to download TikTok videos instantly\.',
            'Nein. DLTK ist ein webbasierter TikTok-Video-Downloader, der vollständig in Ihrem Browser läuft. Sie müssen keine App oder Software herunterladen. Besuchen Sie einfach unsere Website, um TikTok-Videos sofort herunterzuladen.',
            content
        )
        
        content = re.sub(
            r'What video quality can I download TikTok videos in\?',
            'In welcher Videoqualität kann ich TikTok-Videos herunterladen?',
            content
        )
        
        content = re.sub(
            r'Our TikTok video downloader lets you download TikTok videos in multiple quality options: HD \(720p\), Full HD \(1080p\), and 4K when available\. Our TikTok video downloader preserves the original video quality, so you get the best possible downloads\.',
            'Unser TikTok-Video-Downloader ermöglicht es Ihnen, TikTok-Videos in mehreren Qualitätsoptionen herunterzuladen: HD (720p), Full HD (1080p) und 4K, wenn verfügbar. Unser TikTok-Video-Downloader bewahrt die ursprüngliche Videoqualität, sodass Sie die bestmöglichen Downloads erhalten.',
            content
        )
        
        content = re.sub(
            r'Is it legal to download TikTok videos\?',
            'Ist es legal, TikTok-Videos herunterzuladen?',
            content
        )
        
        content = re.sub(
            r'Herunterladening TikTok videos for personal use is generally acceptable\. However, never redistribute or use downloaded content commercially without the creator\'s permission\. Always respect copyright and give credit to original creators\.',
            'Das Herunterladen von TikTok-Videos für den persönlichen Gebrauch ist im Allgemeinen akzeptabel. Verbreiten oder verwenden Sie heruntergeladene Inhalte jedoch niemals kommerziell ohne die Erlaubnis des Urhebers. Respektieren Sie immer das Urheberrecht und geben Sie den ursprünglichen Urhebern die Anerkennung.',
            content
        )
        
        # Fix HowTo Schema
        content = re.sub(
            r'Step-by-step guide to download TikTok videos without watermark using DLTK',
            'Schritt-für-Schritt-Anleitung zum Herunterladen von TikTok-Videos ohne Wasserzeichen mit DLTK',
            content
        )
        
        content = re.sub(
            r'Copy TikTok Video Link',
            'TikTok-Video-Link kopieren',
            content
        )
        
        content = re.sub(
            r'Open TikTok, find the video you want to save, tap Share, and select \'Copy link\'',
            'Öffnen Sie TikTok, finden Sie das Video, das Sie speichern möchten, tippen Sie auf Teilen und wählen Sie \'Link kopieren\'',
            content
        )
        
        content = re.sub(
            r'Paste Link into DLTK',
            'Link in DLTK einfügen',
            content
        )
        
        content = re.sub(
            r'Come back to DLTK\.io and paste the copied TikTok link into the input field above',
            'Kehren Sie zu DLTK.io zurück und fügen Sie den kopierten TikTok-Link in das obige Eingabefeld ein',
            content
        )
        
        content = re.sub(
            r'Herunterladen TikTok Video',
            'TikTok-Video herunterladen',
            content
        )
        
        content = re.sub(
            r'Click the Herunterladen button and choose your preferred quality \(HD, Full HD, or MP4\)',
            'Klicken Sie auf die Herunterladen-Schaltfläche und wählen Sie Ihre bevorzugte Qualität (HD, Full HD oder MP4)',
            content
        )
        
        # Save if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed Schema.org data in {filepath}")
            return True
        else:
            print(f"ℹ️  No Schema changes needed in {filepath}")
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
    print("Fixing German Schema.org Structured Data")
    print("=" * 60 + "\n")
    
    for filepath in files:
        fix_schema_data(filepath)
    
    print("\n" + "=" * 60)
    print("✅ Schema.org fix completed")
    print("=" * 60)
