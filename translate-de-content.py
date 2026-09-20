#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
德语内容翻译 - 使用Python进行精确替换
避免破坏HTML结构
"""

import re
import os

DE_DIR = "/root/.openclaw/workspace/tiktok-video-downloader/frontend/de"

# 德语翻译词典（注意德语名词首字母大写）
TRANSLATIONS = {
    # Schema.org内容
    "DLTK - TikTok Video Downloader": "DLTK - TikTok-Video-Downloader",
    "Download TikTok videos without watermark in HD quality. Free, fast, and no registration required.": 
        "Laden Sie TikTok-Videos ohne Wasserzeichen in HD-Qualität herunter. Kostenlos, schnell und keine Registrierung erforderlich.",
    
    # FAQ Questions
    "Is DLTK free to use?": "Ist DLTK kostenlos?",
    "How can I download TikTok videos without watermark?": "Wie kann ich TikTok-Videos ohne Wasserzeichen herunterladen?",
    "Do I need to install an app to download TikTok videos?": "Muss ich eine App installieren, um TikTok-Videos herunterzuladen?",
    "Can I download TikTok videos on iPhone or Android?": "Kann ich TikTok-Videos auf iPhone oder Android herunterladen?",
    "Are downloaded TikTok videos free of watermarks?": "Sind heruntergeladene TikTok-Videos ohne Wasserzeichen?",
    "Do I need to create an account?": "Muss ich ein Konto erstellen?",
    
    # FAQ Answers
    "Yes, DLTK is completely free.": "Ja, DLTK ist völlig kostenlos.",
    "You can download TikTok videos without watermark with no sign-up, no premium tier, and no limits on how many videos you download.":
        "Sie können TikTok-Videos ohne Wasserzeichen ohne Anmeldung, ohne Premium-Stufe und ohne Begrenzung der Anzahl der Videos herunterladen.",
    "It's a 100% free TikTok video downloader.": "Es ist ein 100% kostenloser TikTok-Video-Downloader.",
    
    # Hero section
    "TikTok Video Downloader Without Watermark": "TikTok-Videos Ohne Wasserzeichen Herunterladen",
    "Free, Fast and HD Quality": "Kostenlos, Schnell und in HD-Qualität",
    "DLTK is a free TikTok video downloader that removes watermarks automatically.":
        "DLTK ist ein kostenloser TikTok-Video-Downloader, der Wasserzeichen automatisch entfernt.",
    
    # Features
    "No Watermark": "Ohne Wasserzeichen",
    "Fast Download": "Schneller Download",
    "100% Free": "100% Kostenlos",
    "All Devices": "Alle Geräte",
    "HD Quality": "HD-Qualität",
    "Private & Safe": "Privat & Sicher",
    
    # Navigation
    "Video": "Video",
    "Thumbnail": "Miniatur",
    "Story": "Story",
    "Contact": "Kontakt",
    "Privacy": "Datenschutz",
    "Terms": "Nutzungsbedingungen",
    
    # Buttons
    "Download": "Herunterladen",
    "Convert": "Konvertieren",
    
    # Common phrases
    "Frequently Asked Questions": "Häufig Gestellte Fragen",
    "Quick Links": "Schnelllinks",
    "Legal": "Rechtliches",
    "About DLTK": "Über DLTK",
}

def translate_file(filepath):
    """翻译单个文件"""
    print(f"翻译: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 执行翻译（按长度排序，先替换长的避免部分匹配）
    for english, german in sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        content = content.replace(english, german)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("=== 开始德语内容翻译 ===")
    
    # 翻译主页面
    for filename in ['index.html', 'mp3.html', 'miniatur.html', 'story.html']:
        filepath = os.path.join(DE_DIR, filename)
        if os.path.exists(filepath):
            translate_file(filepath)
    
    # 翻译法律页面
    pages_dir = os.path.join(DE_DIR, 'pages')
    for filename in os.listdir(pages_dir):
        if filename.endswith('.html'):
            translate_file(os.path.join(pages_dir, filename))
    
    print("✅ 内容翻译完成")

if __name__ == '__main__':
    main()
