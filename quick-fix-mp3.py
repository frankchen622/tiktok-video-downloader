#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速修复MP3页面残留英文
"""

with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/yinpin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 关键英文文本替换
critical_fixes = {
    # Hero区
    'Convert TikTok videos to MP3 in seconds. 下载 audio in high quality (320kbps) for free. Extract music, sound effects, and voiceovers from any video with our fast converter.':
        '秒级转换TikTok视频为MP3。免费下载高品质音频（320kbps）。使用我们的快速转换器从任何视频中提取音乐、音效和配音。',
    
    # 副标题
    '下载 TikTok audio in 3 simple steps with our free TikTok to MP3 converter.':
        '使用我们的免费TikTok转MP3转换器，3步即可下载TikTok音频',
    
    # 步骤1
    'Open the TikTok app, find the video with audio you want to download, tap Share, and select "Copy link". DLTK works with any public TikTok video to extract audio as MP3.':
        '打开TikTok，找到你想下载音频的视频，点击分享，选择"复制链接"。DLTK支持从任何公开TikTok视频提取音频为MP3。',
    
    # 步骤2
    'Return to DLTK.io and paste the TikTok video link into the input field above. Our converter will process the audio instantly.':
        '回到DLTK.io，将TikTok视频链接粘贴到上方输入框。我们的转换器会即时处理音频。',
    
    # 步骤3
    'Click "Convert to MP3" and download the extracted audio file. Your TikTok MP3 download will start immediately in high quality (up to 320kbps).':
        '点击"转换为MP3"并下载提取的音频文件。你的TikTok MP3下载会立即开始，高品质（最高320kbps）。',
    
    # 功能特点副标题
    'The best free audio downloader with powerful features.':
        '功能强大的最佳免费音频下载器',
    
    # 功能1
    '下载 TikTok audio in the best available quality, up to 320kbps MP3. Our converter preserves the original audio quality from TikTok videos, giving you crystal-clear sound for music, podcasts, or voiceovers.':
        '下载最高品质的TikTok音频，最高320kbps MP3。我们的转换器保留TikTok视频的原始音频质量，为你提供音乐、播客或配音的清晰音质。',
    
    # 功能2
    'Convert TikTok videos to MP3 in seconds. Our audio downloader uses advanced technology to extract audio instantly':
        '秒级转换TikTok视频为MP3。我们的音频下载器使用先进技术即时提取音频',
    
    # 下载相关词汇
    '下载 audio': '下载音频',
    '下载 TikTok audio': '下载TikTok音频',
    '下载 TikTok Audio': '下载TikTok音频',
    'TikTok Audio 下载': 'TikTok音频下载',
    'TikTok audio': 'TikTok音频',
    'TikTok Audio': 'TikTok音频',
    '下载er': '下载器',
    '下载s': '下载',
    '下载ed': '下载的',
}

count = 0
for eng, chn in critical_fixes.items():
    if eng in html:
        html = html.replace(eng, chn)
        count += 1

# 保存
with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/yinpin.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ MP3页面快速修复完成")
print(f"📊 替换了 {count} 处关键英文")
print(f"📄 文件大小: {len(html)} 字符")
