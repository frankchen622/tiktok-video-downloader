#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
深度翻译 - 第二轮：翻译所有残留英文
"""

import os

base_path = '/root/.openclaw/workspace/tiktok-downloader/frontend/zh'

# 通用深度翻译（所有页面共用）
common_deep = {
    # 步骤内容
    '<h3>Copy TikTok Video Link</h3>': '<h3>复制TikTok视频链接</h3>',
    '<h3>Paste Link into DLTK': '<h3>粘贴链接到DLTK',
    '<h3>Download TikTok': '<h3>下载TikTok',
    
    # 功能特点
    '<h2>Why Use DLTK': '<h2>为什么使用DLTK',
    '<h2>Why Choose': '<h2>为什么选择',
    '<h3>High Quality': '<h3>高品质',
    '<h3>Fast': '<h3>快速',
    '<h3>100% Free': '<h3>100%免费',
    '<h3>Works on All Devices</h3>': '<h3>支持所有设备</h3>',
    '<h3>Safe & Private': '<h3>安全私密',
    '<h3>Universal MP3 Format</h3>': '<h3>通用MP3格式</h3>',
    
    # FAQ
    '<h2>TikTok': '<h2>TikTok',
    'FAQ': '常见问题',
    
    # 用户评价
    '<h2>What Users Say About': '<h2>用户对',
    '"Best TikTok downloader I\'ve found!': '"我找到的最好的TikTok下载器！',
    '"Finally, a TikTok downloader that works on iPhone': '"终于有一个在iPhone上能用的TikTok下载器了',
    '"I love that it\'s completely free': '"我喜欢它完全免费',
    
    # 页脚
    '<h3>About DLTK</h3>': '<h3>关于DLTK</h3>',
    '<h3>Quick Links</h3>': '<h3>快速链接</h3>',
    '<h3>Legal</h3>': '<h3>法律信息</h3>',
    'TikTok Video Downloader': 'TikTok视频下载器',
    'TikTok to MP3 Converter': 'TikTok转MP3转换器',
    'TikTok Thumbnail Downloader': 'TikTok封面图下载器',
    'TikTok Story Downloader': 'TikTok快拍下载器',
    'Contact Us': '联系我们',
    'Privacy Policy': '隐私政策',
    'Terms of Service': '使用条款',
    'Disclaimer': '免责声明',
    'DMCA': '版权政策',
    'Cookie Policy': 'Cookie政策',
}

# MP3页面深度翻译
mp3_deep = {
    '<h2>How to Convert to MP3 Audio</h2>': '<h2>如何转换为MP3音频</h2>',
    '<h3>Paste Link into DLTK MP3 Converter</h3>': '<h3>粘贴链接到DLTK MP3转换器</h3>',
    '<h3>Download TikTok Audio as MP3</h3>': '<h3>下载TikTok音频为MP3</h3>',
    '<h2>Why Use DLTK TikTok to MP3 Converter</h2>': '<h2>为什么使用DLTK TikTok转MP3转换器</h2>',
    '<h3>High Quality TikTok Audio Download</h3>': '<h3>高品质TikTok音频下载</h3>',
    '<h3>Fast TikTok to MP3 Conversion</h3>': '<h3>快速TikTok转MP3转换</h3>',
    '<h3>100% Free TikTok MP3 Downloader</h3>': '<h3>100%免费TikTok MP3下载器</h3>',
    '<h3>Safe & Private TikTok MP3 Converter</h3>': '<h3>安全私密的TikTok MP3转换器</h3>',
    
    '<h2>What Can You Do with TikTok MP3 Downloads?</h2>': '<h2>下载的TikTok MP3能做什么？</h2>',
    '<h3>Create Music Collections</h3>': '<h3>创建音乐合集</h3>',
    '<h3>Save Podcast Episodes & Voiceovers</h3>': '<h3>保存播客节目和配音</h3>',
    '<h3>Collect Sound Effects</h3>': '<h3>收集音效</h3>',
    '<h3>Ringtones & Notifications</h3>': '<h3>铃声和通知音</h3>',
    '<h3>Study & Learning</h3>': '<h3>学习和教育</h3>',
    
    '<h2>TikTok Audio Quality Options</h2>': '<h2>TikTok音频画质选项</h2>',
    '<h3>Available TikTok MP3 Quality Levels</h3>': '<h3>可用的TikTok MP3画质等级</h3>',
    '<li><strong>320kbps (High Quality)</strong> - Best audio quality for music and professional use. Near-CD quality sound with excellent clarity.</li>':
        '<li><strong>320kbps（高品质）</strong> - 音乐和专业用途的最佳音频质量。接近CD质量的声音，清晰度极佳。</li>',
    '<li><strong>256kbps (Standard Quality)</strong> - Great balance between file size and audio quality. Perfect for most listening scenarios.</li>':
        '<li><strong>256kbps（标准质量）</strong> - 文件大小和音频质量的完美平衡。适合大多数听音场景。</li>',
    '<li><strong>192kbps (Good Quality)</strong> - Smaller file size while maintaining good sound quality. Ideal for mobile devices with limited storage.</li>':
        '<li><strong>192kbps（良好质量）</strong> - 较小文件大小同时保持良好音质。适合存储空间有限的移动设备。</li>',
    '<li><strong>128kbps (Basic Quality)</strong> - Smallest file size. Acceptable for casual listening and voice content.</li>':
        '<li><strong>128kbps（基本质量）</strong> - 最小文件大小。适合休闲收听和语音内容。</li>',
    '<p><strong>Note:</strong> The maximum audio quality depends on the original TikTok video upload. Our converter automatically selects the best available quality, up to 320kbps when the source supports it.</p>':
        '<p><strong>注意：</strong>最大音频质量取决于原始TikTok视频上传。我们的转换器会自动选择最佳可用质量，当源支持时可达320kbps。</p>',
    
    '<h2>What Users Say About DLTK TikTok to MP3 Converter</h2>': '<h2>用户对DLTK TikTok转MP3转换器的评价</h2>',
    '<h2>TikTok to MP3 Converter FAQ</h2>': '<h2>TikTok转MP3转换器常见问题</h2>',
    '<h2>Start Converting TikTok to MP3 Now</h2>': '<h2>立即开始转换TikTok为MP3</h2>',
}

# 封面图页面深度翻译
thumbnail_deep = {
    '<h2>How to Download TikTok Thumbnails</h2>': '<h2>如何下载TikTok封面图</h2>',
    '<h3>Paste Link into DLTK Thumbnail Downloader</h3>': '<h3>粘贴链接到DLTK封面图下载器</h3>',
    '<h3>Download TikTok Thumbnail</h3>': '<h3>下载TikTok封面图</h3>',
    '<h2>Why Use DLTK TikTok Thumbnail Downloader</h2>': '<h2>为什么使用DLTK TikTok封面图下载器</h2>',
    '<h3>Full Resolution TikTok Thumbnails</h3>': '<h3>全分辨率TikTok封面图</h3>',
    '<h3>Fast Thumbnail Downloads</h3>': '<h3>快速封面图下载</h3>',
    '<h3>100% Free Thumbnail Downloader</h3>': '<h3>100%免费封面图下载器</h3>',
    '<h3>Safe & Private Thumbnail Saver</h3>': '<h3>安全私密的封面图保存器</h3>',
    
    '<h2>What Can You Do with TikTok Thumbnails?</h2>': '<h2>下载的TikTok封面图能做什么？</h2>',
    '<h3>Create Custom Covers</h3>': '<h3>制作自定义封面</h3>',
    '<h3>Design Projects</h3>': '<h3>设计项目</h3>',
    '<h3>Social Media Posts</h3>': '<h3>社交媒体帖子</h3>',
    '<h3>Save Memorable Moments</h3>': '<h3>保存难忘瞬间</h3>',
    
    '<h2>What Users Say About DLTK Thumbnail Downloader</h2>': '<h2>用户对DLTK封面图下载器的评价</h2>',
    '<h2>TikTok Thumbnail Downloader FAQ</h2>': '<h2>TikTok封面图下载器常见问题</h2>',
    '<h2>Start Downloading TikTok Thumbnails Now</h2>': '<h2>立即开始下载TikTok封面图</h2>',
}

# 快拍页面深度翻译
story_deep = {
    '<h2>How to Download TikTok Stories</h2>': '<h2>如何下载TikTok快拍</h2>',
    '<h3>Paste Link into DLTK Story Downloader</h3>': '<h3>粘贴链接到DLTK快拍下载器</h3>',
    '<h3>Download TikTok Story</h3>': '<h3>下载TikTok快拍</h3>',
    '<h2>Why Use DLTK TikTok Story Downloader</h2>': '<h2>为什么使用DLTK TikTok快拍下载器</h2>',
    '<h3>Save Stories Before They Expire</h3>': '<h3>在过期前保存快拍</h3>',
    '<h3>High Quality Story Downloads</h3>': '<h3>高品质快拍下载</h3>',
    '<h3>100% Free Story Downloader</h3>': '<h3>100%免费快拍下载器</h3>',
    '<h3>Safe & Private Story Saver</h3>': '<h3>安全私密的快拍保存器</h3>',
    
    '<h2>What Can You Do with Downloaded TikTok Stories?</h2>': '<h2>下载的TikTok快拍能做什么？</h2>',
    '<h3>Preserve Memories</h3>': '<h3>保存回忆</h3>',
    '<h3>Content Archiving</h3>': '<h3>内容归档</h3>',
    '<h3>Personal Backup</h3>': '<h3>个人备份</h3>',
    
    '<h2>What Users Say About DLTK Story Downloader</h2>': '<h2>用户对DLTK快拍下载器的评价</h2>',
    '<h2>TikTok Story Downloader FAQ</h2>': '<h2>TikTok快拍下载器常见问题</h2>',
    '<h2>Start Downloading TikTok Stories Now</h2>': '<h2>立即开始下载TikTok快拍</h2>',
}

# 处理函数
def process_file(filename, specific_translations):
    filepath = os.path.join(base_path, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 应用通用翻译
    for eng, chn in common_deep.items():
        html = html.replace(eng, chn)
    
    # 应用专属翻译
    for eng, chn in specific_translations.items():
        html = html.replace(eng, chn)
    
    # 保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return len(html)

# 执行翻译
print("开始深度翻译...")

size1 = process_file('yinpin.html', mp3_deep)
print(f"✅ yinpin.html 深度翻译完成 ({size1} 字符)")

size2 = process_file('fengmian.html', thumbnail_deep)
print(f"✅ fengmian.html 深度翻译完成 ({size2} 字符)")

size3 = process_file('kuaipai.html', story_deep)
print(f"✅ kuaipai.html 深度翻译完成 ({size3} 字符)")

print("\n🎉 所有页面深度翻译完成！")
