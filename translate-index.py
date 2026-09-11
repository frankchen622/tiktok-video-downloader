#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速中文化 index.html - 批量替换关键文本
"""

import re

# 读取英文版本
with open('/root/.openclaw/workspace/tiktok-downloader/frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 定义替换规则（英文 -> 中文）
replacements = {
    # Meta 标签
    'lang="en"': 'lang="zh-CN"',
    '<title>TikTok Video Downloader Without Watermark - Free & Fast | DLTK</title>': 
        '<title>TikTok视频下载器 - 免费无水印高清下载 | DLTK</title>',
    'Download TikTok videos without watermark in HD quality. Save TikTok to MP4 instantly - no app, no registration. 100% free TikTok video downloader. Try now!':
        '免费TikTok视频下载工具，一键去水印，支持高清下载、MP3转换、封面图保存。无需注册，无需下载APP，快速安全。',
    
    # URL 替换
    'https://dltk.io/"': 'https://dltk.io/zh"',
    'href="/"': 'href="/zh"',
    'href="/mp3.html"': 'href="/zh/yinpin"',
    'href="/thumbnail.html"': 'href="/zh/fengmian"',
    'href="/story.html"': 'href="/zh/kuaipai"',
    
    # 导航栏
    '<li><a href="/zh" class="active">Video</a></li>': '<li><a href="/zh" class="active">视频</a></li>',
    '<li><a href="/zh/yinpin">MP3</a></li>': '<li><a href="/zh/yinpin">MP3</a></li>',
    '<li><a href="/zh/fengmian">Thumbnail</a></li>': '<li><a href="/zh/fengmian">封面图</a></li>',
    '<li><a href="/zh/kuaipai">Story</a></li>': '<li><a href="/zh/kuaipai">快拍</a></li>',
    
    # Hero 区域
    '<h1>TikTok Video Downloader Without Watermark</h1>': '<h1>TikTok视频下载器 - 免费无水印</h1>',
    '<p class="hero-subtitle">Free, Fast & HD Quality</p>': '<p class="hero-subtitle">免费、快速、高清画质</p>',
    'placeholder="Paste TikTok Video Link Here..."': 'placeholder="粘贴TikTok视频链接..."',
    '<span>DOWNLOAD</span>': '<span>下载</span>',
    
    # 信任徽章
    '<strong>100% Secure</strong>': '<strong>100%安全</strong>',
    '<span>No malware or viruses</span>': '<span>无病毒无恶意软件</span>',
    '<strong>10M+ Downloads</strong>': '<strong>1000万+下载</strong>',
    '<span>Trusted by millions</span>': '<span>数百万用户信赖</span>',
    '<strong>4.8/5 Rating</strong>': '<strong>4.8/5评分</strong>',
    '<span>Based on 1,250+ reviews</span>': '<span>基于1,250+评价</span>',
    '<strong>Always Free</strong>': '<strong>永久免费</strong>',
    '<span>No hidden charges</span>': '<span>无隐藏费用</span>',
    
    # 使用说明标题
    '<h2>How to Download TikTok Videos Without Watermark</h2>': '<h2>如何下载TikTok无水印视频</h2>',
    '<p class="section-subtitle">Simple 3-step process to save TikTok videos. No app or registration needed.</p>':
        '<p class="section-subtitle">简单3步即可保存TikTok视频，无需APP，无需注册</p>',
    
    # 步骤
    '<h3>Copy the TikTok Video Link</h3>': '<h3>复制TikTok视频链接</h3>',
    '<h3>Paste the Link into DLTK</h3>': '<h3>粘贴链接到DLTK</h3>',
    '<h3>Download TikTok Video</h3>': '<h3>下载TikTok视频</h3>',
    
    # 功能特点标题
    '<h2>Why Choose Our Free TikTok Video Downloader</h2>': '<h2>为什么选择我们的免费TikTok视频下载器</h2>',
    '<p class="section-subtitle">The best free TikTok downloader with powerful features for all your needs.</p>':
        '<p class="section-subtitle">功能强大的免费TikTok下载工具，满足所有需求</p>',
    
    # 功能卡片标题
    '<h3>Download TikTok Without Watermark</h3>': '<h3>下载TikTok无水印视频</h3>',
    '<h3>Fast TikTok Downloader</h3>': '<h3>快速TikTok下载器</h3>',
    '<h3>TikTok to MP3 Converter</h3>': '<h3>TikTok转MP3转换器</h3>',
    '<h3>TikTok Thumbnail Downloader</h3>': '<h3>TikTok封面图下载器</h3>',
    '<h3>Works on All Devices</h3>': '<h3>支持所有设备</h3>',
    '<h3>100% Free TikTok Downloader</h3>': '<h3>100%免费TikTok下载器</h3>',
    '<h3>HD TikTok Video Downloader</h3>': '<h3>HD TikTok视频下载器</h3>',
    '<h3>Safe & Private</h3>': '<h3>安全私密</h3>',
    
    # FAQ 标题
    '<h2>TikTok Video Downloader FAQ - Common Questions</h2>': '<h2>TikTok视频下载器常见问题</h2>',
    
    # 页脚
    '<h4>About DLTK</h4>': '<h4>关于DLTK</h4>',
    '<h4>Quick Links</h4>': '<h4>快速链接</h4>',
    '<h4>Legal</h4>': '<h4>法律信息</h4>',
    'Contact Us': '联系我们',
    'Privacy Policy': '隐私政策',
    'Terms of Service': '使用条款',
    'Disclaimer': '免责声明',
    'DMCA': '版权政策',
    'Cookie Policy': 'Cookie政策',
}

# 执行替换
for eng, chn in replacements.items():
    html = html.replace(eng, chn)

# 特殊处理：hreflang 标签
html = re.sub(
    r'<link rel="alternate" hreflang="x-default" href="https://dltk.io/zh" />',
    '<link rel="alternate" hreflang="zh-CN" href="https://dltk.io/zh" />\n  <link rel="alternate" hreflang="x-default" href="https://dltk.io/" />',
    html
)

# 保存中文版本
with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ 中文首页已生成：/root/.openclaw/workspace/tiktok-downloader/frontend/zh/index.html")
print("📊 文件大小：", len(html), "字符")
