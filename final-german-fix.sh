#!/bin/bash
# 最终的德语翻译修复

DE_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/de"

for file in "$DE_DIR"/index.html; do
    echo "最终修复: $file"
    
    # Step 2描述 (在Schema.org和页面内容中都有)
    sed -i 's/Come back to DLTK\.io and paste the copied TikTok link into the input field above\. Our TikTok downloader will instantly process your video and remove the watermark automatically\./Kehren Sie zu DLTK.io zurück und fügen Sie den kopierten TikTok-Link in das Eingabefeld oben ein. Unser TikTok-Downloader verarbeitet Ihr Video sofort und entfernt das Wasserzeichen automatisch./g' "$file"
    
    # Feature descriptions that were missed
    sed -i 's/Our free TikTok video downloader removes watermarks automatically, giving you clean, professional-looking videos\. Herunterladen TikTok videos in original quality without the TikTok logo\./Unser kostenloser TikTok-Video-Downloader entfernt Wasserzeichen automatisch und liefert Ihnen saubere, professionell aussehende Videos. Laden Sie TikTok-Videos in Originalqualität ohne TikTok-Logo herunter./g' "$file"
    
    sed -i 's/Herunterladen TikTok videos in seconds\. Our TikTok video downloader uses advanced technology to process videos instantly\. No waiting, no queues - just fast TikTok downloads\./Laden Sie TikTok-Videos in Sekunden herunter. Unser TikTok-Video-Downloader nutzt fortschrittliche Technologie zur sofortigen Videoverarbeitung. Kein Warten, keine Warteschlangen - nur schnelle TikTok-Downloads./g' "$file"
    
    sed -i 's/Extract audio from TikTok videos and save as high-quality MP3 files\. Perfect for creating music collections or podcasts\./Extrahieren Sie Audio aus TikTok-Videos und speichern Sie es als hochwertige MP3-Dateien. Perfekt zum Erstellen von Musiksammlungen oder Podcasts./g' "$file"
    
    sed -i 's/Our TikTok video downloader works on Windows, Mac, Android, iOS, and any device with a web browser\. No app installation needed - download TikTok videos from any device\./Unser TikTok-Video-Downloader funktioniert auf Windows, Mac, Android, iOS und jedem Gerät mit Webbrowser. Keine App-Installation erforderlich - laden Sie TikTok-Videos von jedem Gerät herunter./g' "$file"
    
    sed -i 's/Herunterladen TikTok videos for free with no limits\. No registration, no subscription, no hidden fees\. DLTK is completely free to use forever\./Laden Sie TikTok-Videos kostenlos und ohne Limits herunter. Keine Registrierung, kein Abonnement, keine versteckten Gebühren. DLTK ist für immer völlig kostenlos./g' "$file"
    
    sed -i 's/Herunterladen TikTok videos in HD, Full HD, and even 4K quality when available\. Our downloader preserves the original video quality for the best viewing experience\./Laden Sie TikTok-Videos in HD, Full HD und sogar 4K-Qualität herunter, wenn verfügbar. Unser Downloader erhält die Original-Videoqualität für das beste Seherlebnis./g' "$file"
    
    sed -i 's/Your privacy is our priority\. We don'\''t store your downloaded videos, track your activity, or require any personal information\. Herunterladen TikTok videos safely and anonymously\./Ihre Privatsphäre hat für uns Priorität. Wir speichern Ihre heruntergeladenen Videos nicht, verfolgen Ihre Aktivitäten nicht und benötigen keine persönlichen Informationen. Laden Sie TikTok-Videos sicher und anonym herunter./g' "$file"
    
done

echo "✅ 最终德语修复完成"
