#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
翻译FAQ和CTA中的长段落英文
"""

with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# FAQ答案替换（需要精确匹配HTML结构）
faq_replacements = [
    # MP3转换FAQ
    (
        'With DLTK TikTok video downloader, yes! Our TikTok video downloader includes a TikTok转MP3 converter. You can extract audio from any TikTok video and save it as an MP3 file. Visit our TikTok转MP3 page for audio downloads.',
        '可以！我们的TikTok视频下载器包含TikTok转MP3转换器。你可以从任何TikTok视频中提取音频，保存为MP3文件。访问我们的TikTok转MP3页面进行音频下载。'
    ),
    # 快拍下载FAQ
    (
        'Yes, you can download TikTok stories before they expire. Visit our TikTok快拍下载器 to save stories permanently.',
        '可以，你可以在TikTok快拍过期前下载它们。访问我们的TikTok快拍下载器永久保存快拍。'
    ),
    # 封面图下载FAQ
    (
        'With DLTK TikTok video downloader, use our TikTok封面图下载器 to save video cover images in full resolution. Perfect for creating custom thumbnails or saving memorable moments.',
        '使用我们的TikTok封面图下载器，保存全分辨率视频封面图。非常适合制作自定义缩略图或保存难忘瞬间。'
    ),
    # 视频格式FAQ
    (
        'Downloaded TikTok videos are saved as MP4 files, which work on all devices and media players. For audio-only downloads, visit our TikTok转MP3 converter to save as MP3 format. MP4 provides the best balance of quality and compatibility.',
        '下载的TikTok视频保存为MP4文件，可在所有设备和媒体播放器上播放。如需仅音频下载，请访问我们的TikTok转MP3转换器以MP3格式保存。MP4提供了质量和兼容性的最佳平衡。'
    ),
    # 最终CTA第一段
    (
        'DLTK is your go-to free TikTok video downloader for saving TikTok videos without watermarks. Our TikTok video downloader supports HD downloads, MP3 conversion, thumbnail extraction, and story downloads, you have everything you need to download TikTok content quickly and easily. Our free TikTok downloader works on all devices, requires no registration, and removes watermarks automatically.',
        'DLTK是你首选的免费TikTok视频下载工具，用于保存无水印TikTok视频。我们的TikTok视频下载器支持HD下载、MP3转换、封面图提取和快拍下载，你拥有快速轻松下载TikTok内容所需的一切。我们的免费TikTok下载器适用于所有设备，无需注册，自动去除水印。'
    ),
]

count = 0
for eng, chn in faq_replacements:
    if eng in html:
        html = html.replace(eng, chn)
        count += 1
        print(f"✅ 替换长段落 ({len(eng)} 字符)")

with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n📊 总计替换了 {count} 个长段落")
print(f"📄 最终文件大小: {len(html)} 字符")

# 检查是否还有残留英文（简单检测）
import re
english_pattern = r'\b(Download|TikTok video downloader|Our|You can|Perfect for|Best for|Great for|Works in|Compatible with|No app)\b'
matches = re.findall(english_pattern, html)
if matches:
    unique = set(matches)
    print(f"\n⚠️  检测到 {len(unique)} 种可能的残留英文关键词:")
    for word in sorted(unique)[:10]:
        print(f"   - {word}")
else:
    print("\n✅ 未检测到明显的英文关键词残留")
