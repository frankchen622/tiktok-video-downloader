#!/usr/bin/env python3
"""
Complete German translation fix for TikTok downloader
Replaces all remaining English text with proper German translations
"""

import re
import sys

# Complete translation mapping
translations = {
    # Navigation and buttons
    "Herunterladen TikTok videos without watermark": "TikTok-Videos ohne Wasserzeichen herunterladen",
    "Herunterladen": "Herunterladen",
    "Try TikTok zu MP3 Konvertierener": "TikTok zu MP3 Konvertierer ausprobieren",
    "Herunterladen TikTok Miniaturs": "TikTok-Miniaturansichten herunterladen",
    "Works on Alle Geräte": "Funktioniert auf allen Geräten",
    
    # Feature titles and descriptions
    "Fast TikTok Herunterladener": "Schneller TikTok-Downloader",
    "TikTok zu MP3 Konvertierener": "TikTok zu MP3 Konvertierer",
    "TikTok Miniatur Herunterladener": "TikTok-Miniaturansichten-Downloader",
    "100% Kostenlos TikTok Herunterladener": "100% Kostenloser TikTok-Downloader",
    "HD TikTok Video Herunterladener": "HD TikTok-Video-Downloader",
    "Sicher & Privat": "Sicher & Privat",
    
    # Long English paragraphs in features
    "Fast, simple, and actually removes the watermark. I use it daily for my content creation.":
        "Schnell, einfach und entfernt tatsächlich das Wasserzeichen. Ich benutze es täglich für meine Content-Erstellung.",
    
    "Finally, a TikTok downloader that works on iPhone without installing apps. The quality is perfect and it's super fast!":
        "Endlich ein TikTok-Downloader, der auf dem iPhone funktioniert, ohne Apps zu installieren. Die Qualität ist perfekt und es ist super schnell!",
    
    "I love that it's completely free with no ads. Herunterladens are instant and the HD quality is amazing. Highly recommend!":
        "Ich liebe es, dass es völlig kostenlos und ohne Werbung ist. Downloads sind sofort verfügbar und die HD-Qualität ist erstaunlich. Sehr empfehlenswert!",
    
    # Feature descriptions
    "Unser kostenloser TikTok-Video-Downloader entfernt Wasserzeichen automatisch und liefert Ihnen saubere, professionell aussehende Videos. Laden Sie TikTok-Videos in Originalqualität ohne TikTok-Logo herunter.":
        "Unser kostenloser TikTok-Video-Downloader entfernt Wasserzeichen automatisch und liefert Ihnen saubere, professionell aussehende Videos. Laden Sie TikTok-Videos in Originalqualität ohne TikTok-Logo herunter.",
    
    "Laden Sie TikTok-Videos in Sekunden herunter. Unser TikTok-Video-Downloader nutzt fortschrittliche Technologie zur sofortigen Videoverarbeitung. Kein Warten, keine Warteschlangen - nur schnelle TikTok-Downloads.":
        "Laden Sie TikTok-Videos in Sekunden herunter. Unser TikTok-Video-Downloader nutzt fortschrittliche Technologie zur sofortigen Videoverarbeitung. Kein Warten, keine Warteschlangen - nur schnelle TikTok-Downloads.",
    
    # Headers
    "TikTok Video Herunterladener - Quality Options": "TikTok-Video-Downloader - Qualitätsoptionen",
    "Choose the perfect quality for your TikTok downloads.": "Wählen Sie die perfekte Qualität für Ihre TikTok-Downloads.",
    "Available TikTok Video Formats": "Verfügbare TikTok-Video-Formate",
    
    # Quality descriptions
    "Perfektes Gleichgewicht zwischen Dateigröße und Qualität. Ideal für die meisten Verwendungszwecke und schnelle Downloads.":
        "Perfektes Gleichgewicht zwischen Dateigröße und Qualität. Ideal für die meisten Verwendungszwecke und schnelle Downloads.",
    
    "High-quality TikTok video downloads with excellent clarity. Best for professional use.":
        "Hochwertige TikTok-Video-Downloads mit hervorragender Klarheit. Am besten für professionelle Zwecke.",
    
    "Maximum quality when the original TikTok video supports it. Ideal for large screens and editing.":
        "Maximale Qualität, wenn das Original-TikTok-Video dies unterstützt. Ideal für große Bildschirme und Bearbeitung.",
    
    "Universal video format that works on all devices. Herunterladen TikTok videos as MP4 for maximum compatibility.":
        "Universelles Videoformat, das auf allen Geräten funktioniert. Laden Sie TikTok-Videos als MP4 für maximale Kompatibilität herunter.",
    
    "Extract audio only from TikTok videos. Perfect for music and sounds.":
        "Nur Audio aus TikTok-Videos extrahieren. Perfekt für Musik und Sounds.",
    
    # Device compatibility section
    "Herunterladen TikTok Videos on Any Device": "TikTok-Videos auf jedem Gerät herunterladen",
    "Our TikTok downloader works perfectly across all platforms.": "Unser TikTok-Downloader funktioniert perfekt auf allen Plattformen.",
    "Supported Platforms for TikTok Herunterladens": "Unterstützte Plattformen für TikTok-Downloads",
    "Mobile Devices:": "Mobile Geräte:",
    "Desktop Computers:": "Desktop-Computer:",
    "Supported Browsers:": "Unterstützte Browser:",
    
    # Android description
    "Herunterladen TikTok videos on Samsung, Huawei, Xiaomi, and all Android phones. Works in Chrome, Firefox, and other mobile browsers.":
        "Laden Sie TikTok-Videos auf Samsung, Huawei, Xiaomi und allen Android-Telefonen herunter. Funktioniert in Chrome, Firefox und anderen mobilen Browsern.",
    
    # iPhone description
    "Herunterladen TikTok videos on iOS devices using Safari or any web browser. No app installation required.":
        "Laden Sie TikTok-Videos auf iOS-Geräten mit Safari oder einem beliebigen Webbrowser herunter. Keine App-Installation erforderlich.",
    
    # Windows description
    "Herunterladen TikTok videos on Windows 10, 11, and earlier versions. Compatible with all browsers.":
        "Laden Sie TikTok-Videos unter Windows 10, 11 und früheren Versionen herunter. Kompatibel mit allen Browsern.",
    
    # Mac description
    "Herunterladen TikTok videos on macOS with Safari, Chrome, or Firefox.":
        "Laden Sie TikTok-Videos auf macOS mit Safari, Chrome oder Firefox herunter.",
    
    # Linux description
    "Our TikTok video downloader works on all Linux distributions.":
        "Unser TikTok-Video-Downloader funktioniert auf allen Linux-Distributionen.",
    
    # Browser descriptions
    "Google Chrome - Best performance for TikTok downloads": "Google Chrome - Beste Leistung für TikTok-Downloads",
    "Mozilla Firefox - Full feature support": "Mozilla Firefox - Vollständige Funktionsunterstützung",
    "Safari - Optimized for Mac and iOS": "Safari - Optimiert für Mac und iOS",
    "Microsoft Edge - Perfect for Windows users": "Microsoft Edge - Perfekt für Windows-Benutzer",
    "Opera, Brave, and other modern browsers": "Opera, Brave und andere moderne Browser",
    
    # Final paragraph in device section
    "Herunterladen TikTok videos without watermark from anywhere, anytime. DLTK is a web-based TikTok downloader that requires no app installation - just visit our website and start downloading!":
        "Laden Sie TikTok-Videos ohne Wasserzeichen von überall und jederzeit herunter. DLTK ist ein webbasierter TikTok-Downloader, der keine App-Installation erfordert - besuchen Sie einfach unsere Website und beginnen Sie mit dem Herunterladen!",
    
    # Testimonials section
    "What Users Say Über DLTK": "Was Benutzer über DLTK sagen",
    "Von Millionen vertraut of TikTok users worldwide.": "Von Millionen TikTok-Benutzern weltweit vertraut.",
    
    # User testimonials
    "Best TikTok downloader I've found!": "Der beste TikTok-Downloader, den ich gefunden habe!",
    "Content Creator": "Content Creator",
    "iPhone User": "iPhone-Benutzer",
    "Social Media Manager": "Social Media Manager",
    
    # FAQ section fixes
    "TikTok Video Herunterladener FAQ - Common Questions": "TikTok-Video-Downloader FAQ - Häufig gestellte Fragen",
    
    # FAQ answers with "With DLTK TikTok video downloader" prefix
    "With DLTK TikTok video downloader, yes, DLTK is completely free.": "Ja, DLTK ist völlig kostenlos.",
    "Simply copy the TikTok video link, paste it into DLTK's input field, and click Herunterladen.": 
        "Kopieren Sie einfach den TikTok-Video-Link, fügen Sie ihn in das Eingabefeld von DLTK ein und klicken Sie auf Herunterladen.",
    "With DLTK TikTok video downloader, no. DLTK is a web-based TikTok video downloader":
        "Nein. DLTK ist ein webbasierter TikTok-Video-Downloader",
    
    # More FAQ content
    "You can download TikTok videos in multiple quality options: HD (720p), Full HD (1080p), and 4K when available.":
        "Sie können TikTok-Videos in mehreren Qualitätsoptionen herunterladen: HD (720p), Full HD (1080p) und 4K, wenn verfügbar.",
    
    "With DLTK TikTok video downloader, yes! Our TikTok video downloader includes a TikTok zu MP3 converter.":
        "Ja! Unser TikTok-Video-Downloader enthält einen TikTok zu MP3 Konvertierer.",
    
    "Herunterladening TikTok videos for personal use is generally acceptable.":
        "Das Herunterladen von TikTok-Videos für den persönlichen Gebrauch ist im Allgemeinen akzeptabel.",
    
    "With DLTK TikTok video downloader, yes, our free TikTok video downloader works perfectly on all mobile devices":
        "Ja, unser kostenloser TikTok-Video-Downloader funktioniert perfekt auf allen mobilen Geräten",
    
    "Yes, you can download TikTok stories before they expire.":
        "Ja, Sie können TikTok-Storys herunterladen, bevor sie ablaufen.",
    
    "With DLTK TikTok video downloader, use our": "Verwenden Sie unseren",
    "um Video-Coverbilder in voller Auflösung zu speichern. Perfekt zum Erstellen benutzerdefinierter Miniaturansichten oder zum Speichern unvergesslicher Momente.":
        "um Video-Coverbilder in voller Auflösung zu speichern. Perfekt zum Erstellen benutzerdefinierter Miniaturansichten oder zum Speichern unvergesslicher Momente.",
    
    # Why choose DLTK
    "DLTK is the best free TikTok video downloader - faster, easier, and more reliable than other TikTok video downloaders.":
        "DLTK ist der beste kostenlose TikTok-Video-Downloader - schneller, einfacher und zuverlässiger als andere TikTok-Video-Downloader.",
    
    # Download own videos
    "With DLTK TikTok video downloader, to download your own TikTok videos, simply copy the link from your profile and paste it into DLTK.":
        "Um Ihre eigenen TikTok-Videos herunterzuladen, kopieren Sie einfach den Link aus Ihrem Profil und fügen Sie ihn in DLTK ein.",
    
    # Low quality video
    "If your downloaded TikTok video appears blurry, the original upload may be low resolution.":
        "Wenn Ihr heruntergeladenes TikTok-Video unscharf erscheint, kann der Original-Upload eine niedrige Auflösung haben.",
    
    # Safety
    "DLTK is completely safe. We don't store your videos, require login credentials, or collect personal data.":
        "DLTK ist völlig sicher. Wir speichern Ihre Videos nicht, benötigen keine Anmeldedaten und sammeln keine persönlichen Daten.",
    
    # Private accounts
    "No, you cannot download TikTok videos from private accounts unless you follow that account.":
        "Nein, Sie können keine TikTok-Videos von privaten Konten herunterladen, es sei denn, Sie folgen diesem Konto.",
    
    # Watermark still present
    "If your downloaded TikTok video still shows a watermark, try refreshing the page and downloading again.":
        "Wenn Ihr heruntergeladenes TikTok-Video immer noch ein Wasserzeichen zeigt, versuchen Sie, die Seite zu aktualisieren und erneut herunterzuladen.",
    
    # Video format
    "Herunterladened TikTok videos are saved as MP4 files, which work on all devices and media players.":
        "Heruntergeladene TikTok-Videos werden als MP4-Dateien gespeichert, die auf allen Geräten und Mediaplayern funktionieren.",
    
    # Multiple downloads
    "Currently, DLTK processes one TikTok video at a time for optimal speed and quality.":
        "Derzeit verarbeitet DLTK jeweils ein TikTok-Video für optimale Geschwindigkeit und Qualität.",
    
    # Conclusion CTA
    "Start Herunterladening TikTok Videos Now": "Beginnen Sie jetzt mit dem Herunterladen von TikTok-Videos",
    "Herunterladen TikTok Videos Now →": "TikTok-Videos jetzt herunterladen →",
    
    # Footer fixes
    "Kontakt Us": "Kontaktieren Sie uns",
    "Datenschutz Policy": "Datenschutzrichtlinie",
    "Nutzungsbedingungen of Service": "Nutzungsbedingungen",
    
    # Final footer
    "We are not affiliated with TikTok or ByteDance.": "Wir sind nicht mit TikTok oder ByteDance verbunden.",
    "All rights belong to their respective owners.": "Alle Rechte gehören ihren jeweiligen Eigentümern.",
}

def fix_german_file(filepath):
    """Fix German translations in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = 0
        
        # Apply all translations
        for english, german in translations.items():
            if english in content:
                content = content.replace(english, german)
                changes_made += 1
                print(f"✓ Replaced: {english[:50]}...")
        
        # Save if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"\n✅ Fixed {filepath}")
            print(f"   Made {changes_made} translation fixes\n")
            return True
        else:
            print(f"ℹ️  No changes needed in {filepath}\n")
            return False
            
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

if __name__ == "__main__":
    files_to_fix = [
        "frontend/de/index.html",
        "frontend/de/mp3.html",
        "frontend/de/miniatur.html",
        "frontend/de/story.html"
    ]
    
    print("=" * 60)
    print("German Translation Complete Fix")
    print("=" * 60 + "\n")
    
    fixed_count = 0
    for filepath in files_to_fix:
        if fix_german_file(filepath):
            fixed_count += 1
    
    print("=" * 60)
    print(f"✅ Completed! Fixed {fixed_count}/{len(files_to_fix)} files")
    print("=" * 60)
