#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全面检查并翻译所有遗漏的英文文本
"""

# 从网页抓取到的未翻译英文文本
remaining_english = {
    # 画质选项部分
    'HD Quality (720p) - Perfect balance between file size and quality. Great for most uses and fast downloads.':
        'HD画质 (720p) - 文件大小与画质的完美平衡。适合大多数用途，下载快速。',
    'Full HD (1080p) - High-quality TikTok video downloads with excellent clarity. Best for professional use.':
        'Full HD (1080p) - 高质量TikTok视频下载，清晰度极佳。最适合专业用途。',
    '4K Ultra HD - Maximum quality when the original TikTok video supports it. Ideal for large screens and editing.':
        '4K超高清 - 当原始TikTok视频支持时的最高画质。适合大屏幕和视频编辑。',
    'MP4 Format - Universal video format that works on all devices. Download TikTok videos as MP4 for maximum compatibility.':
        'MP4格式 - 通用视频格式，所有设备通用。下载TikTok视频为MP4，获得最大兼容性。',
    'MP3 Audio - Extract audio only from TikTok videos. Perfect for music and sounds.':
        'MP3音频 - 仅提取TikTok视频中的音频。非常适合音乐和声音。',
    
    # 设备列表
    'Android - Download TikTok videos on Samsung, Huawei, Xiaomi, and all Android phones. Works in Chrome, Firefox, and other mobile browsers.':
        'Android - 在三星、华为、小米及所有安卓手机上下载TikTok视频。支持Chrome、Firefox等移动浏览器。',
    'iPhone & iPad - Download TikTok videos on iOS devices using Safari or any web browser. No app installation required.':
        'iPhone & iPad - 使用Safari或任何浏览器在iOS设备上下载TikTok视频。无需安装APP。',
    'Windows PC - Download TikTok videos on Windows 10, 11, and earlier versions. Compatible with all browsers.':
        'Windows PC - 在Windows 10、11及更早版本上下载TikTok视频。兼容所有浏览器。',
    'Mac - Download TikTok videos on macOS with Safari, Chrome, or Firefox.':
        'Mac - 使用Safari、Chrome或Firefox在macOS上下载TikTok视频。',
    'Linux - Our TikTok video downloader works on all Linux distributions.':
        'Linux - 我们的TikTok视频下载器适用于所有Linux发行版。',
    
    # 用户评价
    'Trusted by millions of TikTok users worldwide.': '全球数百万TikTok用户信赖',
    'of TikTok users worldwide.': '',  # 删除这个残留
    
    # FAQ答案中的英文
    'With DLTK TikTok video downloader, yes! Our TikTok video downloader includes a TikTok转MP3 converter. You can extract audio from any TikTok video and save it as an MP3 file. Visit our TikTok转MP3 page for audio downloads.':
        '可以！我们的TikTok视频下载器包含TikTok转MP3转换器。你可以从任何TikTok视频中提取音频，保存为MP3文件。访问我们的TikTok转MP3页面进行音频下载。',
    'Yes, you can download TikTok stories before they expire. Visit our TikTok快拍下载器 to save stories permanently.':
        '可以，你可以在TikTok快拍过期前下载它们。访问我们的TikTok快拍下载器永久保存快拍。',
    'With DLTK TikTok video downloader, use our TikTok封面图下载器 to save video cover images in full resolution. Perfect for creating custom thumbnails or saving memorable moments.':
        '使用我们的TikTok封面图下载器，保存全分辨率视频封面图。非常适合制作自定义缩略图或保存难忘瞬间。',
    'Downloaded TikTok videos are saved as MP4 files, which work on all devices and media players. For audio-only downloads, visit our TikTok转MP3 converter to save as MP3 format. MP4 provides the best balance of quality and compatibility.':
        '下载的TikTok视频保存为MP4文件，可在所有设备和媒体播放器上播放。如需仅音频下载，请访问我们的TikTok转MP3转换器以MP3格式保存。MP4提供了质量和兼容性的最佳平衡。',
    
    # 最终CTA段落
    'DLTK is your go-to free TikTok video downloader for saving TikTok videos without watermarks. Our TikTok video downloader supports HD downloads, MP3 conversion, thumbnail extraction, and story downloads, you have everything you need to download TikTok content quickly and easily. Our free TikTok downloader works on all devices, requires no registration, and removes watermarks automatically.':
        'DLTK是你首选的免费TikTok视频下载工具，用于保存无水印TikTok视频。我们的TikTok视频下载器支持HD下载、MP3转换、封面图提取和快拍下载，你拥有快速轻松下载TikTok内容所需的一切。我们的免费TikTok下载器适用于所有设备，无需注册，自动去除水印。',
}

# 处理中文首页
with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

count = 0
for eng, chn in remaining_english.items():
    if eng in html:
        html = html.replace(eng, chn)
        count += 1
        print(f"✅ 替换: {eng[:50]}...")

with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n📊 中文首页：替换了 {count} 处英文文本")
print(f"📄 文件大小: {len(html)} 字符")
