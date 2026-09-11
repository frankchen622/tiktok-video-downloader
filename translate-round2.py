#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整中文化脚本 - 第二轮深度替换
"""

import re

# 读取第一轮生成的文件
with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 更多翻译对照（包括段落、句子）
translations = {
    # Hero intro
    'DLTK is a free TikTok video downloader that removes watermarks automatically. Download TikTok videos in HD quality, convert to MP3, or save thumbnails - all in one place. No app needed, no registration required. Fast, simple, and works on all devices.':
        'DLTK是免费的TikTok视频下载工具，自动去除水印。支持HD高清下载、MP3转换、封面图保存，一站式解决。无需APP，无需注册，快速简单，支持所有设备。',
    
    # 步骤描述
    'Open TikTok app, find the video you want to download, tap the Share button, and select "Copy link". Our TikTok video downloader works with any TikTok video URL.':
        '打开TikTok，找到你想下载的视频，点击分享按钮，选择"复制链接"。我们的TikTok下载器支持任何TikTok视频URL。',
    'Come back to DLTK.io and paste the copied TikTok link into the input field above. Our TikTok downloader will instantly process your video and remove the watermark automatically.':
        '回到DLTK.io，将复制的TikTok链接粘贴到上方输入框。我们的TikTok下载器会即时处理视频并自动去除水印。',
    'Click the Download button and choose your preferred quality (HD, Full HD, or MP4). The video saves directly to your device without watermark. You can also convert TikTok to MP3 if you only need the audio.':
        '点击下载按钮，选择你喜欢的画质（HD、Full HD或MP4）。视频会直接保存到你的设备，无水印。如果只需要音频，也可以转换TikTok为MP3。',
    
    # 功能描述
    'Our free TikTok video downloader removes watermarks automatically, giving you clean, professional-looking videos. Download TikTok videos in original quality without the TikTok logo.':
        '免费TikTok视频下载器自动去除水印，为你提供干净、专业的视频。下载TikTok视频保留原始画质，无TikTok标志。',
    'Download TikTok videos in seconds. Our TikTok video downloader uses advanced technology to process videos instantly. No waiting, no queues - just fast TikTok downloads.':
        '秒级下载TikTok视频。我们的TikTok视频下载器采用先进技术即时处理视频。无需等待，无需排队，只有快速的TikTok下载。',
    'Extract audio from TikTok videos and save as high-quality MP3 files. Perfect for creating music collections or podcasts.':
        '从TikTok视频中提取音频，保存为高品质MP3文件。非常适合制作音乐合集或播客。',
    'Save TikTok video cover images in full resolution with one click. Download TikTok thumbnails for your projects.':
        '一键保存全分辨率TikTok视频封面图。下载TikTok封面用于你的项目。',
    'Our TikTok video downloader works on Windows, Mac, Android, iOS, and any device with a web browser. No app installation needed - download TikTok videos from any device.':
        '我们的TikTok视频下载器支持Windows、Mac、Android、iOS及任何带浏览器的设备。无需安装APP，从任何设备下载TikTok视频。',
    'Download TikTok videos for free with no limits. No registration, no subscription, no hidden fees. DLTK is completely free to use forever.':
        '免费下载TikTok视频，无限制。无需注册，无需订阅，无隐藏费用。DLTK永久完全免费。',
    'Download TikTok videos in HD, Full HD, and even 4K quality when available. Our TikTok video downloader preserves original video quality for the best viewing experience.':
        '下载HD、Full HD甚至4K画质的TikTok视频（如果可用）。我们的TikTok视频下载器保留原始视频画质，提供最佳观看体验。',
    'Your privacy is our priority. We don\'t store your downloaded videos or personal information. Download TikTok videos safely and anonymously with DLTK.':
        '您的隐私是我们的首要任务。我们不存储你下载的视频或个人信息。使用DLTK安全匿名地下载TikTok视频。',
    
    # 画质部分
    '<h2>TikTok Video Downloader - Quality Options</h2>': '<h2>TikTok视频下载器 - 画质选项</h2>',
    '<p class="section-subtitle">Choose the perfect quality for your TikTok downloads.</p>':
        '<p class="section-subtitle">为你的TikTok下载选择完美画质</p>',
    'When you download TikTok videos with DLTK, you have multiple quality options to choose from:':
        '使用DLTK下载TikTok视频时，你可以选择多种画质选项：',
    '<h3>Available TikTok Video Formats</h3>': '<h3>可用的TikTok视频格式</h3>',
    
    # 设备部分
    '<h2>Download TikTok Videos on Any Device</h2>': '<h2>在任何设备上下载TikTok视频</h2>',
    '<p class="section-subtitle">Our TikTok downloader works perfectly across all platforms.</p>':
        '<p class="section-subtitle">我们的TikTok下载器完美支持所有平台</p>',
    '<h3>Supported Platforms for TikTok Downloads</h3>': '<h3>支持的TikTok下载平台</h3>',
    'Mobile Devices:': '移动设备：',
    'Desktop Computers:': '桌面电脑：',
    'Supported Browsers:': '支持的浏览器：',
    
    # 用户评价
    '<h2>What Users Say About DLTK</h2>': '<h2>用户对DLTK的评价</h2>',
    '<p class="section-subtitle">Trusted by millions of TikTok users worldwide.</p>':
        '<p class="section-subtitle">全球数百万TikTok用户信赖</p>',
    'Content Creator': '内容创作者',
    'iPhone User': 'iPhone用户',
    'Social Media Manager': '社交媒体经理',
    
    # FAQ 问题
    'Is DLTK free to use?': 'DLTK是免费的吗？',
    'How can I download TikTok videos without watermark?': '如何下载无水印TikTok视频？',
    'Do I need to install an app to download TikTok videos?': '需要下载APP吗？',
    'What video quality can I download TikTok videos in?': '可以下载什么画质？',
    'Can I convert TikTok videos to MP3?': '可以转换TikTok为MP3吗？',
    'Is it legal to download TikTok videos?': '下载TikTok视频合法吗？',
    'Does DLTK work on mobile phones?': 'DLTK支持手机吗？',
    'Can I download TikTok stories?': '可以下载TikTok快拍吗？',
    'How do I download TikTok thumbnails?': '如何下载TikTok封面图？',
    'Why choose DLTK over other TikTok downloaders?': '为什么选择DLTK？',
    
    # 链接文本
    'Try TikTok to MP3 Converter': '试试TikTok转MP3转换器',
    'Download TikTok Thumbnails': '下载TikTok封面图',
    'TikTok to MP3': 'TikTok转MP3',
    'TikTok story downloader': 'TikTok快拍下载器',
    'TikTok thumbnail downloader': 'TikTok封面图下载器',
    
    # 最终CTA
    '<h2>Start Downloading TikTok Videos Now</h2>': '<h2>立即开始下载TikTok视频</h2>',
    'Download TikTok Videos Now →': '立即下载TikTok视频 →',
}

# 执行替换
for eng, chn in translations.items():
    html = html.replace(eng, chn)

# Schema.org FAQ 翻译
faq_translations = {
    'Yes, DLTK is completely free': '是的，DLTK完全免费',
    'Using our TikTok video downloader is simple': '使用我们的TikTok视频下载器很简单',
    'No. DLTK is a web-based': '不需要。DLTK是基于网页的',
}

for eng, chn in faq_translations.items():
    html = html.replace(eng, chn)

# 保存
with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ 第二轮翻译完成")
print("📊 文件大小：", len(html), "字符")
