#!/bin/bash
# 完整的德语翻译 - 使用sed进行全面替换

DE_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/de"

for file in "$DE_DIR"/index.html "$DE_DIR"/mp3.html "$DE_DIR"/miniatur.html "$DE_DIR"/story.html; do
    echo "全面翻译: $file"
    
    # Trust indicators 子文本
    sed -i 's/No malware or viruses/Keine Malware oder Viren/g' "$file"
    sed -i 's/Trusted by millions/Von Millionen vertraut/g' "$file"
    sed -i 's/Based on 1,250+ reviews/Basierend auf 1.250+ Bewertungen/g' "$file"
    sed -i 's/No hidden charges/Keine versteckten Gebühren/g' "$file"
    sed -i 's/10M+ Herunterladens/10M+ Downloads/g' "$file"
    
    # How to section
    sed -i 's/How to Herunterladen TikTok Videos Without Watermark/So Laden Sie TikTok-Videos Ohne Wasserzeichen Herunter/g' "$file"
    sed -i 's/Simple 3-step process to save TikTok videos\. No app or registration needed\./Einfacher 3-Schritte-Prozess zum Speichern von TikTok-Videos. Keine App oder Registrierung erforderlich./g' "$file"
    
    # Steps
    sed -i 's/Copy the TikTok Video Link/Kopieren Sie den TikTok-Video-Link/g' "$file"
    sed -i 's/Open TikTok app or website, find the video you want, and copy its URL\./Öffnen Sie die TikTok-App oder Website, finden Sie das gewünschte Video und kopieren Sie seine URL./g' "$file"
    
    sed -i 's/Paste Link and Click Herunterladen/Link Einfügen und auf Herunterladen Klicken/g' "$file"
    sed -i 's/Paste the link into DLTK'\''s input field and hit the Herunterladen button\./Fügen Sie den Link in das DLTK-Eingabefeld ein und klicken Sie auf die Schaltfläche Herunterladen./g' "$file"
    
    sed -i 's/Save the TikTok Video/Speichern Sie das TikTok-Video/g' "$file"
    sed -i 's/Choose your quality and click Herunterladen\. The video saves without watermark\./Wählen Sie Ihre Qualität und klicken Sie auf Herunterladen. Das Video wird ohne Wasserzeichen gespeichert./g' "$file"
    
    # FAQ section
    sed -i 's/Yes, DLTK is completely free\. You can Herunterladen TikTok videos without watermark with no sign-up, no premium tier, and no limits on how many videos you Herunterladen\. It'\''s a 100% free TikTok video downloader\./Ja, DLTK ist völlig kostenlos. Sie können TikTok-Videos ohne Wasserzeichen ohne Anmeldung, ohne Premium-Stufe und ohne Begrenzung der Anzahl der Videos herunterladen. Es ist ein 100% kostenloser TikTok-Video-Downloader./g' "$file"
    
    sed -i 's/Simply copy the TikTok video link, paste it into DLTK'\''s field, and click Herunterladen\. Our TikTok video downloader automatically removes the watermark and lets you save TikTok videos in HD quality\./Kopieren Sie einfach den TikTok-Video-Link, fügen Sie ihn in das DLTK-Feld ein und klicken Sie auf Herunterladen. Unser TikTok-Video-Downloader entfernt automatisch das Wasserzeichen und ermöglicht Ihnen das Speichern von TikTok-Videos in HD-Qualität./g' "$file"
    
    sed -i 's/No, you don'\''t need to install any app\. DLTK is a web-based tool that works directly in your browser\. Just visit DLTK\.io, paste your link, and Herunterladen your video\./Nein, Sie müssen keine App installieren. DLTK ist ein webbasiertes Tool, das direkt in Ihrem Browser funktioniert. Besuchen Sie einfach DLTK.io, fügen Sie Ihren Link ein und laden Sie Ihr Video herunter./g' "$file"
    
    sed -i 's/Yes, DLTK works on all devices including iPhone, Android, tablets, and computers\. Our TikTok downloader is optimized for mobile and desktop use\./Ja, DLTK funktioniert auf allen Geräten einschließlich iPhone, Android, Tablets und Computern. Unser TikTok-Downloader ist für die mobile und Desktop-Nutzung optimiert./g' "$file"
    
    sed -i 's/Yes, all videos downloaded through DLTK are completely watermark-free\. We remove the TikTok logo so you get clean videos\./Ja, alle über DLTK heruntergeladenen Videos sind völlig wasserzeichenfrei. Wir entfernen das TikTok-Logo, damit Sie saubere Videos erhalten./g' "$file"
    
    sed -i 's/No, DLTK doesn'\''t require any registration or account creation\. You can start downloading TikTok videos immediately\./Nein, DLTK erfordert keine Registrierung oder Kontoerstellung. Sie können sofort mit dem Herunterladen von TikTok-Videos beginnen./g' "$file"
    
    sed -i 's/Our TikTok video downloader offers multiple quality options: HD (720p), Full HD (1080p), and 4K when available\. Our downloader preserves original video quality so you get the best downloads possible\./Unser TikTok-Video-Downloader bietet mehrere Qualitätsoptionen: HD (720p), Full HD (1080p) und 4K, wenn verfügbar. Unser Downloader bewahrt die ursprüngliche Videoqualität, damit Sie die bestmöglichen Downloads erhalten./g' "$file"
    
    # Reviews section
    sed -i 's/What People Say About Us/Was Die Leute Über Uns Sagen/g' "$file"
    sed -i 's/Join thousands of satisfied users who love DLTK/Schließen Sie sich Tausenden zufriedener Benutzer an, die DLTK lieben/g' "$file"
    
    sed -i 's/"Best free TikTok downloader I'\''ve used\. No ads, no bs, just works\."/"Bester kostenloser TikTok-Downloader, den ich je benutzt habe. Keine Werbung, kein Unsinn, funktioniert einfach."/g' "$file"
    sed -i 's/"Finally, a TikTok saver that actually removes watermarks perfectly\!"/"Endlich ein TikTok-Speicherer, der Wasserzeichen tatsächlich perfekt entfernt!"/g' "$file"
    sed -i 's/"Love the audio extraction\. Makes creating my music library so easy\."/"Liebe die Audio-Extraktion. Macht das Erstellen meiner Musikbibliothek so einfach."/g' "$file"
    
    # CTA section
    sed -i 's/Ready to Herunterladen TikTok Videos\?/Bereit, TikTok-Videos Herunterzuladen\?/g' "$file"
    sed -i 's/Start downloading your favorite TikTok videos without watermark in seconds\./Beginnen Sie in Sekunden mit dem Herunterladen Ihrer Lieblings-TikTok-Videos ohne Wasserzeichen./g' "$file"
    sed -i 's/Start Now/Jetzt Starten/g' "$file"
    
    # Footer links text
    sed -i 's/>Video</>Video</g' "$file"
    sed -i 's/>MP3</>MP3</g' "$file"
    sed -i 's/>Thumbnail</>Miniatur</g' "$file"
    sed -i 's/>Story</>Story</g' "$file"
    
done

echo "✅ 全面德语翻译完成"
