#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整的德语内容翻译 - 修复所有英文残留
"""

import re
import os

DE_DIR = "/root/.openclaw/workspace/tiktok-video-downloader/frontend/de"

def fix_title_tag(content):
    """修复重复的title标签"""
    # 删除第一个title标签，保留完整的第二个
    content = re.sub(
        r'<title>.*?<title>(.*?)</title>.*?</title>',
        r'<title>\1</title>',
        content,
        flags=re.DOTALL
    )
    return content

def translate_content(content):
    """翻译所有英文内容为德语"""
    
    # 大段文本替换
    replacements = {
        # Hero section
        "Free, Fast & HD-Qualität": "Kostenlos, Schnell & HD-Qualität",
        "Free, Fast and HD Quality": "Kostenlos, Schnell und HD-Qualität",
        "Herunterladen TikTok videos in HD quality, convert to MP3, or save thumbnails - all in one place. No app needed, no registration required. Fast, simple, and works on all devices.":
            "Laden Sie TikTok-Videos in HD-Qualität herunter, konvertieren Sie zu MP3 oder speichern Sie Miniaturansichten - alles an einem Ort. Keine App erforderlich, keine Registrierung nötig. Schnell, einfach und funktioniert auf allen Geräten.",
        
        # Placeholder
        "Paste TikTok Video Link Here...": "TikTok-Video-Link hier einfügen...",
        
        # Buttons
        "DOWNLOAD": "HERUNTERLADEN",
        "Download": "Herunterladen",
        
        # Trust indicators
        "100% Secure": "100% Sicher",
        "No registration, no ads, no hidden fees. Your data stays private.":
            "Keine Registrierung, keine Werbung, keine versteckten Gebühren. Ihre Daten bleiben privat.",
        
        "Fast & Easy": "Schnell & Einfach",
        "Herunterladen videos in seconds. Just paste, click, and save - it's that simple.":
            "Laden Sie Videos in Sekunden herunter. Einfach einfügen, klicken und speichern - so einfach ist das.",
        
        "Always Free": "Immer Kostenlos",
        "Unlimited downloads, forever free. No premium tiers or paywalls - ever.":
            "Unbegrenzte Downloads, für immer kostenlos. Keine Premium-Stufen oder Bezahlschranken - niemals.",
        
        # Features section
        "Why Choose Our Free TikTok Video Downloader":
            "Warum Unseren Kostenlosen TikTok-Video-Downloader Wählen",
        "The best free TikTok downloader with powerful features for all your needs.":
            "Der beste kostenlose TikTok-Downloader mit leistungsstarken Funktionen für alle Ihre Bedürfnisse.",
        
        # Feature 1
        "TikTok Downloader No Watermark":
            "TikTok-Downloader Ohne Wasserzeichen",
        "Our free downloader removes watermarks automatically, giving you clean, professional-looking videos. Herunterladen TikTok videos in original quality without the TikTok logo.":
            "Unser kostenloser Downloader entfernt Wasserzeichen automatisch und liefert Ihnen saubere, professionell aussehende Videos. Laden Sie TikTok-Videos in Originalqualität ohne TikTok-Logo herunter.",
        
        # Feature 2  
        "Fast TikTok Downloader": "Schneller TikTok-Downloader",
        "Herunterladen TikTok videos in seconds. Our downloader uses advanced technology to process videos instantly. No waiting, no queues - just fast downloads.":
            "Laden Sie TikTok-Videos in Sekunden herunter. Unser Downloader nutzt fortschrittliche Technologie zur sofortigen Videoverarbeitung. Kein Warten, keine Warteschlangen - nur schnelle Downloads.",
        
        # Feature 3
        "TikTok to MP3 Converter": "TikTok zu MP3 Konverter",
        "Extract audio from TikTok videos and save as high-quality MP3 files. Perfect for building music collections or podcasts.":
            "Extrahieren Sie Audio aus TikTok-Videos und speichern Sie es als hochwertige MP3-Dateien. Perfekt zum Erstellen von Musiksammlungen oder Podcasts.",
        "Try TikTok to MP3 Converter": "TikTok zu MP3 Konverter Ausprobieren",
        
        # Feature 4
        "TikTok Thumbnail Downloader": "TikTok-Miniaturansicht-Downloader",
        "Save TikTok video cover images in full resolution with one click. Herunterladen TikTok thumbnails for your projects.":
            "Speichern Sie TikTok-Video-Coverbilder in voller Auflösung mit einem Klick. Laden Sie TikTok-Miniaturansichten für Ihre Projekte herunter.",
        "Herunterladen TikTok Thumbnails": "TikTok-Miniaturansichten Herunterladen",
        
        # Feature 5
        "Works on All Devices": "Funktioniert auf Allen Geräten",
        "Our downloader works on Windows, Mac, Android, iOS, and any device with a web browser. No app install needed - Herunterladen TikTok videos from any device.":
            "Unser Downloader funktioniert auf Windows, Mac, Android, iOS und jedem Gerät mit einem Webbrowser. Keine App-Installation erforderlich - laden Sie TikTok-Videos von jedem Gerät herunter.",
        
        # Feature 6
        "100% Free TikTok Downloader": "100% Kostenloser TikTok-Downloader",
        "Herunterladen TikTok videos for free with no limits. No registration, no subscription, no hidden fees. DLTK is completely free forever.":
            "Laden Sie TikTok-Videos kostenlos und ohne Limits herunter. Keine Registrierung, kein Abonnement, keine versteckten Gebühren. DLTK ist für immer völlig kostenlos.",
        
        # Feature 7
        "HD TikTok Video Downloader": "HD-TikTok-Video-Downloader",
        "Herunterladen TikTok videos in HD, Full HD, and even 4K quality when available. Our downloader preserves original video quality for the best viewing experience.":
            "Laden Sie TikTok-Videos in HD, Full HD und sogar 4K-Qualität herunter, wenn verfügbar. Unser Downloader erhält die Original-Videoqualität für das beste Seherlebnis.",
        
        # Feature 8
        "Safe & Private": "Sicher & Privat",
        "Your privacy matters. We don't store your data, track your activity, or require registration. Herunterladen TikTok videos safely and anonymously.":
            "Ihre Privatsphäre ist wichtig. Wir speichern Ihre Daten nicht, verfolgen Ihre Aktivitäten nicht und benötigen keine Registrierung. Laden Sie TikTok-Videos sicher und anonym herunter.",
        
        # FAQ
        "Frequently Asked Questions": "Häufig Gestellte Fragen",
        "Everything you need to know about downloading TikTok videos without watermark.":
            "Alles, was Sie über das Herunterladen von TikTok-Videos ohne Wasserzeichen wissen müssen.",
        
        # Footer
        "DLTK.io is a free online TikTok video downloader for downloading TikTok videos without watermark, extracting audio to MP3, saving thumbnails, and preserving stories. Fast, simple, and always free.":
            "DLTK.io ist ein kostenloser Online-TikTok-Video-Downloader zum Herunterladen von TikTok-Videos ohne Wasserzeichen, Extrahieren von Audio zu MP3, Speichern von Miniaturansichten und Bewahren von Stories. Schnell, einfach und immer kostenlos.",
        
        "TikTok Video Downloader": "TikTok-Video-Downloader",
        "TikTok to MP3": "TikTok zu MP3",
        "Thumbnail Downloader": "Miniaturansicht-Downloader",
        "Story Downloader": "Story-Downloader",
        
        "Contact Us": "Kontaktieren Sie Uns",
        "Privacy Policy": "Datenschutzerklärung",
        "Terms of Service": "Nutzungsbedingungen",
        "Disclaimer": "Haftungsausschluss",
        "DMCA & Copyright": "DMCA & Urheberrecht",
        "Cookie Policy": "Cookie-Richtlinie",
        
        "Free TikTok Video Downloader Without Watermark":
            "Kostenloser TikTok-Video-Downloader Ohne Wasserzeichen",
    }
    
    # 应用所有替换
    for english, german in replacements.items():
        content = content.replace(english, german)
    
    return content

def process_file(filepath):
    """处理单个文件"""
    print(f"处理: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复title标签
    content = fix_title_tag(content)
    
    # 翻译内容
    content = translate_content(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("=== 修复德语翻译 ===")
    
    # 处理主页面
    for filename in ['index.html', 'mp3.html', 'miniatur.html', 'story.html']:
        filepath = os.path.join(DE_DIR, filename)
        if os.path.exists(filepath):
            process_file(filepath)
    
    print("✅ 德语翻译修复完成")

if __name__ == '__main__':
    main()
