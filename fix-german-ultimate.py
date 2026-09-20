#!/usr/bin/env python3
"""
Ultimate German cleanup - fix ALL remaining English text
"""

def ultimate_cleanup(filepath):
    """Final ultimate cleanup of German pages"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix ALL title/header translations
        content = content.replace('Free & Fast', 'Kostenlos & Schnell')
        content = content.replace('— Herunterladen Audio Free & Fast', '— Audio kostenlos & schnell herunterladen')
        
        # Fix aria-label
        content = content.replace('aria-label="DLTK Logo - Free TikTok Video Herunterladener"', 
                                  'aria-label="DLTK Logo - Kostenloser TikTok-Video-Downloader"')
        
        # Fix feature headers
        content = content.replace('<h3 >Herunterladen TikTok Without Watermark</h3>',
                                  '<h3 >TikTok ohne Wasserzeichen herunterladen</h3>')
        content = content.replace('<h3>Herunterladen TikTok Without Watermark</h3>',
                                  '<h3>TikTok ohne Wasserzeichen herunterladen</h3>')
        content = content.replace('<h3>Herunterladen Stories Without Watermarks</h3>',
                                  '<h3>Stories ohne Wasserzeichen herunterladen</h3>')
        content = content.replace('<h3 >Herunterladen Stories Without Watermarks</h3>',
                                  '<h3 >Stories ohne Wasserzeichen herunterladen</h3>')
        
        # Fix FAQ questions
        content = content.replace('<dt>How do I download TikTok thumbnails?</dt>',
                                  '<dt>Wie lade ich TikTok-Miniaturansichten herunter?</dt>')
        content = content.replace('<dt>Are TikTok downloader sites safe to use?</dt>',
                                  '<dt>Sind TikTok-Downloader-Websites sicher zu verwenden?</dt>')
        content = content.replace('<dt>Can I convert TikTok videos to MP3?</dt>',
                                  '<dt>Kann ich TikTok-Videos zu MP3 konvertieren?</dt>')
        
        # Fix "the best" phrases
        content = content.replace('automatically detects the best available quality',
                                  'erkennt automatisch die beste verfügbare Qualität')
        
        # Fix device/quality/story mentions in plain text
        content = content.replace('on any device with a web browser', 'auf jedem Gerät mit einem Webbrowser')
        content = content.replace('with a web browser', 'mit einem Webbrowser')
        
        # Fix downloader mention
        content = content.replace('our fast TikTok downloader processes', 'unser schneller TikTok-Downloader verarbeitet')
        content = content.replace('Our TikTok video downloader automatically detects', 
                                  'Unser TikTok-Video-Downloader erkennt automatisch')
        
        # Fix specific MP3 page text
        content = content.replace('Click "Konvertieren to MP3" and download the extracted audio file',
                                  'Klicken Sie auf "Zu MP3 konvertieren" und laden Sie die extrahierte Audiodatei herunter')
        content = content.replace('Your TikTok MP3 download starts', 'Ihr TikTok-MP3-Download beginnt')
        content = content.replace('will be saved to your device', 'wird auf Ihr Gerät gespeichert')
        
        # Fix story page remaining English
        content = content.replace('No watermarks, no sign-up, instant downloads',
                                  'Keine Wasserzeichen, keine Anmeldung, sofortiger Download')
        content = content.replace('saved permanently to your device', 'dauerhaft auf Ihrem Gerät gespeichert')
        
        # Fix miniatur page
        content = content.replace('Save TikTok cover photos instantly', 'Speichern Sie TikTok-Cover-Fotos sofort')
        content = content.replace('without watermarks', 'ohne Wasserzeichen')
        
        # Comments (for code clarity - optional but nice)
        content = content.replace('<!-- Quality Options -->', '<!-- Qualitätsoptionen -->')
        
        # Save if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Ultimate cleanup applied to {filepath}")
            return True
        else:
            print(f"ℹ️  No additional cleanup needed in {filepath}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    files = [
        "frontend/de/index.html",
        "frontend/de/mp3.html",
        "frontend/de/miniatur.html",
        "frontend/de/story.html"
    ]
    
    print("=" * 60)
    print("🔧 Ultimate German Translation Cleanup")
    print("=" * 60 + "\n")
    
    fixed = 0
    for filepath in files:
        if ultimate_cleanup(filepath):
            fixed += 1
    
    print("\n" + "=" * 60)
    print(f"✅ Cleanup complete! Fixed {fixed} files")
    print("=" * 60)
