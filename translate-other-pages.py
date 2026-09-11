#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量翻译其他3个页面：MP3、封面图、快拍
"""

import os
import shutil

# 定义文件映射
pages = {
    'mp3.html': 'yinpin.html',
    'thumbnail.html': 'fengmian.html', 
    'story.html': 'kuaipai.html'
}

# 通用翻译规则
common_translations = {
    # Meta 和基础
    'lang="en"': 'lang="zh-CN"',
    'https://dltk.io/mp3.html"': 'https://dltk.io/zh/yinpin"',
    'https://dltk.io/thumbnail.html"': 'https://dltk.io/zh/fengmian"',
    'https://dltk.io/story.html"': 'https://dltk.io/zh/kuaipai"',
    'href="/"': 'href="/zh"',
    'href="/mp3.html"': 'href="/zh/yinpin"',
    'href="/thumbnail.html"': 'href="/zh/fengmian"',
    'href="/story.html"': 'href="/zh/kuaipai"',
    
    # 导航
    '<li><a href="/zh" class="active">Video</a></li>': '<li><a href="/zh">视频</a></li>',
    '<li><a href="/zh/yinpin" class="active">MP3</a></li>': '<li><a href="/zh/yinpin" class="active">MP3</a></li>',
    '<li><a href="/zh/fengmian" class="active">Thumbnail</a></li>': '<li><a href="/zh/fengmian" class="active">封面图</a></li>',
    '<li><a href="/zh/kuaipai" class="active">Story</a></li>': '<li><a href="/zh/kuaipai" class="active">快拍</a></li>',
    
    # 通用按钮和文本
    'DOWNLOAD': '下载',
    'Download': '下载',
    'CONVERT TO MP3': '转换为MP3',
    'Loading...': '加载中...',
}

# MP3页面专属翻译
mp3_translations = {
    '<title>TikTok to MP3 Converter - Free Audio Downloader | DLTK</title>':
        '<title>TikTok转MP3 - 免费音频下载工具 | DLTK</title>',
    'Download TikTok audio in high quality. Convert TikTok videos to MP3 (320kbps) for free. No app, no registration, fast and easy.':
        '高品质下载TikTok音频。免费转换TikTok视频为MP3（320kbps）。无需APP，无需注册，快速简单。',
    
    '<h1>TikTok to MP3 Converter</h1>': '<h1>TikTok转MP3转换器</h1>',
    '<p class="hero-subtitle">Download Audio Free & Fast</p>': '<p class="hero-subtitle">免费快速下载音频</p>',
    'Convert TikTok videos to MP3 in seconds. Download audio in high quality (320kbps) for free. Extract music, sound effects, and voiceovers from any video with our fast converter.':
        '秒级转换TikTok视频为MP3。免费下载高品质音频（320kbps）。使用我们的快速转换器从任何视频中提取音乐、音效和配音。',
    
    'placeholder="Paste TikTok Video Link Here..."': 'placeholder="粘贴TikTok视频链接..."',
    '<span>CONVERT TO MP3</span>': '<span>转换为MP3</span>',
    
    '<h2>How to Convert TikTok to MP3 Audio</h2>': '<h2>如何转换TikTok为MP3音频</h2>',
    '<p class="section-subtitle">Download TikTok audio in 3 simple steps with our free TikTok to MP3 converter.</p>':
        '<p class="section-subtitle">使用我们的免费TikTok转MP3转换器，3步即可下载TikTok音频</p>',
}

# 封面图页面专属翻译
thumbnail_translations = {
    '<title>TikTok Thumbnail Downloader - Save Video Covers | DLTK</title>':
        '<title>TikTok封面图下载 - 保存视频封面 | DLTK</title>',
    'Download TikTok thumbnails in full resolution. Save video cover images with one click. Free TikTok thumbnail downloader, no registration required.':
        '全分辨率下载TikTok封面图。一键保存视频封面。免费TikTok封面图下载器，无需注册。',
    
    '<h1>TikTok Thumbnail Downloader</h1>': '<h1>TikTok封面图下载器</h1>',
    '<p class="hero-subtitle">Save Cover Images in Full HD</p>': '<p class="hero-subtitle">保存全高清封面图</p>',
    'Save TikTok video cover images in full resolution with one click. Download TikTok thumbnails for free - perfect for creating custom covers, saving memorable moments, or using in your projects.':
        '一键保存全分辨率TikTok视频封面图。免费下载TikTok封面 - 非常适合制作自定义封面、保存难忘瞬间或用于你的项目。',
    
    '<span>DOWNLOAD THUMBNAIL</span>': '<span>下载封面图</span>',
    
    '<h2>How to Download TikTok Thumbnails</h2>': '<h2>如何下载TikTok封面图</h2>',
    '<p class="section-subtitle">Save TikTok video covers in 3 easy steps.</p>':
        '<p class="section-subtitle">3步即可保存TikTok视频封面</p>',
}

# 快拍页面专属翻译
story_translations = {
    '<title>TikTok Story Downloader - Save Stories | DLTK</title>':
        '<title>TikTok快拍下载 - 保存快拍 | DLTK</title>',
    'Download TikTok stories before they expire. Save TikTok story videos and photos permanently. Free TikTok story downloader, works on all devices.':
        '在TikTok快拍过期前下载。永久保存TikTok快拍视频和照片。免费TikTok快拍下载器，支持所有设备。',
    
    '<h1>TikTok Story Downloader</h1>': '<h1>TikTok快拍下载器</h1>',
    '<p class="hero-subtitle">Save Stories Before They Expire</p>': '<p class="hero-subtitle">在过期前保存快拍</p>',
    'Download TikTok stories and save them permanently before they disappear after 24 hours. Our free TikTok story downloader lets you save story videos and photos in high quality.':
        '下载TikTok快拍并在其24小时后消失前永久保存。我们的免费TikTok快拍下载器让你保存高质量的快拍视频和照片。',
    
    '<span>DOWNLOAD STORY</span>': '<span>下载快拍</span>',
    
    '<h2>How to Download TikTok Stories</h2>': '<h2>如何下载TikTok快拍</h2>',
    '<p class="section-subtitle">Save TikTok stories in 3 simple steps before they expire.</p>':
        '<p class="section-subtitle">在快拍过期前3步保存</p>',
}

# 处理每个页面
base_path = '/root/.openclaw/workspace/tiktok-downloader/frontend'

for eng_file, chn_file in pages.items():
    print(f"\n处理 {eng_file} -> {chn_file}...")
    
    # 读取英文版
    with open(os.path.join(base_path, eng_file), 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 应用通用翻译
    for eng, chn in common_translations.items():
        html = html.replace(eng, chn)
    
    # 应用专属翻译
    if eng_file == 'mp3.html':
        for eng, chn in mp3_translations.items():
            html = html.replace(eng, chn)
    elif eng_file == 'thumbnail.html':
        for eng, chn in thumbnail_translations.items():
            html = html.replace(eng, chn)
    elif eng_file == 'story.html':
        for eng, chn in story_translations.items():
            html = html.replace(eng, chn)
    
    # 保存中文版
    output_path = os.path.join(base_path, 'zh', chn_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ {chn_file} 创建完成 ({len(html)} 字符)")

print("\n🎉 所有页面翻译完成！")
