#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第三轮完整中文化 - 清除所有英文残留
"""

import re

with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 所有残留的英文文本（从页面抓取）
complete_translations = {
    # Hero标题（如果还有英文）
    'TikTok Video Downloader Without Watermark': 'TikTok视频下载器 - 免费无水印',
    'Free, Fast & HD Quality': '免费、快速、高清画质',
    
    # 信任徽章
    '100% Secure': '100%安全',
    'No malware or viruses': '无病毒无恶意软件',
    '10M+ Downloads': '1000万+下载',
    'Trusted by millions': '数百万用户信赖',
    '4.8/5 Rating': '4.8/5评分',
    'Based on 1,250+ reviews': '基于1,250+评价',
    'Always Free': '永久免费',
    'No hidden charges': '无隐藏费用',
    
    # 使用说明标题
    'How to Download TikTok Videos Without Watermark': '如何下载TikTok无水印视频',
    'Simple 3-step process to save TikTok videos. No app or registration needed.':
        '简单3步即可保存TikTok视频，无需APP，无需注册',
    
    # 步骤标题
    'Copy the TikTok Video Link': '复制TikTok视频链接',
    'Paste the Link into DLTK': '粘贴链接到DLTK',
    'Download TikTok Video': '下载TikTok视频',
    
    # 功能标题
    'Why Choose Our Free TikTok Video Downloader': '为什么选择我们的免费TikTok视频下载器',
    'The best free TikTok downloader with powerful features for all your needs.':
        '功能强大的免费TikTok下载工具，满足所有需求',
    
    # 功能卡片
    'Download TikTok Without Watermark': '下载TikTok无水印视频',
    'Fast TikTok Downloader': '快速TikTok下载器',
    'TikTok转MP3 Converter': 'TikTok转MP3转换器',
    'TikTok Thumbnail Downloader': 'TikTok封面图下载器',
    'Works on All Devices': '支持所有设备',
    '100% Free TikTok Downloader': '100%免费TikTok下载器',
    'HD TikTok Video Downloader': 'HD TikTok视频下载器',
    'Safe & Private': '安全私密',
    
    # 画质部分
    'TikTok Video Downloader - Quality Options': 'TikTok视频下载器 - 画质选项',
    'Choose the perfect quality for your TikTok downloads.': '为你的TikTok下载选择完美画质',
    'Available TikTok Video Formats': '可用的TikTok视频格式',
    
    # 画质列表
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
    
    'Our TikTok video downloader automatically detects the best available quality for each video and lets you choose your preferred format. Whether you need to download TikTok videos for personal viewing or professional projects, DLTK has you covered.':
        '我们的TikTok视频下载器会自动检测每个视频的最佳可用画质，让你选择喜欢的格式。无论你需要下载TikTok视频用于个人观看还是专业项目，DLTK都能满足你。',
    
    # 设备部分
    'Download TikTok Videos on Any Device': '在任何设备上下载TikTok视频',
    'Our TikTok downloader works perfectly across all platforms.': '我们的TikTok下载器完美支持所有平台',
    'Supported Platforms for TikTok Downloads': '支持的TikTok下载平台',
    
    # 设备列表
    'Mobile Devices:': '移动设备：',
    'Android - Download TikTok videos on Samsung, Huawei, Xiaomi, and all Android phones. Works in Chrome, Firefox, and other mobile browsers.':
        'Android - 在三星、华为、小米及所有安卓手机上下载TikTok视频。支持Chrome、Firefox等移动浏览器。',
    'iPhone & iPad - Download TikTok videos on iOS devices using Safari or any web browser. No app installation required.':
        'iPhone & iPad - 使用Safari或任何浏览器在iOS设备上下载TikTok视频。无需安装APP。',
    
    'Desktop Computers:': '桌面电脑：',
    'Windows PC - Download TikTok videos on Windows 10, 11, and earlier versions. Compatible with all browsers.':
        'Windows PC - 在Windows 10、11及更早版本上下载TikTok视频。兼容所有浏览器。',
    'Mac - Download TikTok videos on macOS with Safari, Chrome, or Firefox.':
        'Mac - 使用Safari、Chrome或Firefox在macOS上下载TikTok视频。',
    'Linux - Our TikTok video downloader works on all Linux distributions.':
        'Linux - 我们的TikTok视频下载器适用于所有Linux发行版。',
    
    'Supported Browsers:': '支持的浏览器：',
    'Google Chrome - Best performance for TikTok downloads': 'Google Chrome - TikTok下载最佳性能',
    'Mozilla Firefox - Full feature support': 'Mozilla Firefox - 完整功能支持',
    'Safari - Optimized for Mac and iOS': 'Safari - 为Mac和iOS优化',
    'Microsoft Edge - Perfect for Windows users': 'Microsoft Edge - Windows用户完美选择',
    'Opera, Brave, and other modern browsers': 'Opera、Brave及其他现代浏览器',
    
    'Download TikTok videos without watermark from anywhere, anytime. DLTK is a web-based TikTok downloader that requires no app installation - just visit our website and start downloading!':
        '随时随地下载无水印TikTok视频。DLTK是基于网页的TikTok下载器，无需安装APP，只需访问我们的网站即可开始下载！',
    
    # 用户评价
    'What Users Say About DLTK': '用户对DLTK的评价',
    'Trusted by millions of TikTok users worldwide.': '全球数百万TikTok用户信赖',
    
    # 评价内容
    '"Best TikTok downloader I\'ve found! Fast, simple, and actually removes the watermark. I use it daily for my content creation."':
        '"我找到的最好的TikTok下载器！快速、简单，而且确实去除了水印。我每天都用它进行内容创作。"',
    '"Finally, a TikTok downloader that works on iPhone without installing apps. The quality is perfect and it\'s super fast!"':
        '"终于有一个在iPhone上无需安装APP就能用的TikTok下载器了。画质完美，速度超快！"',
    '"I love that it\'s completely free with no ads. Downloads are instant and the HD quality is amazing. Highly recommend!"':
        '"我喜欢它完全免费且无广告。下载即时，HD画质令人惊叹。强烈推荐！"',
    
    # FAQ
    'TikTok Video Downloader FAQ - Common Questions': 'TikTok视频下载器常见问题',
    
    # FAQ 答案
    'With DLTK TikTok video downloader, yes, DLTK is completely free. You can download TikTok videos without watermark with no sign-up, no premium tier, and no limits on how many videos you download. It\'s a 100% free TikTok video downloader.':
        '是的，DLTK完全免费。你可以无限制下载无水印TikTok视频，无需注册，没有高级版付费，100%免费的TikTok下载工具。',
    
    'Simply copy the TikTok video link, paste it into DLTK\'s input field, and click Download. Our TikTok video downloader automatically removes the watermark and lets you save TikTok videos in HD quality. The entire process takes less than 10 seconds.':
        '只需复制TikTok视频链接，粘贴到DLTK输入框，点击下载即可。我们的TikTok视频下载器会自动去除水印，让你保存高清无水印视频，整个过程不到10秒。',
    
    'With DLTK TikTok video downloader, no. DLTK is a web-based TikTok video downloader that runs entirely in your browser. You don\'t need to download any app or software. Just visit our website to download TikTok videos instantly.':
        '不需要。DLTK是网页版TikTok下载器，完全在浏览器中运行，无需下载任何应用程序或软件，直接访问网站即可使用。',
    
    'You can download TikTok videos in multiple quality options: HD (720p), Full HD (1080p), and 4K when available. Our TikTok video downloader preserves the original video quality, so you get the best possible downloads.':
        '你可以下载多种画质的TikTok视频：HD (720p)、Full HD (1080p)，以及4K（如果可用）。我们的TikTok视频下载器保留原始视频画质，让你获得最佳下载体验。',
    
    'With DLTK TikTok video downloader, yes! Our TikTok video downloader includes a TikTok转MP3 converter. You can extract audio from any TikTok video and save it as an MP3 file. Visit our TikTok转MP3 page for audio downloads.':
        '可以！我们的TikTok视频下载器包含TikTok转MP3转换器。你可以从任何TikTok视频中提取音频，保存为MP3文件。访问我们的TikTok转MP3页面进行音频下载。',
    
    'Downloading TikTok videos for personal use is generally acceptable. However, never redistribute or use downloaded content commercially without the creator\'s permission. Always respect copyright and give credit to original creators.':
        '下载TikTok视频用于个人用途通常是可以的。但是，未经创作者许可，切勿重新分发或商业使用下载的内容。始终尊重版权，给予原创作者应有的署名。',
    
    'With DLTK TikTok video downloader, yes, our free TikTok video downloader works perfectly on all mobile devices including Android phones, iPhones, and tablets. Download TikTok videos on any device with a web browser.':
        '是的，我们的免费TikTok视频下载器完美支持所有移动设备，包括Android手机、iPhone和平板电脑。在任何有浏览器的设备上下载TikTok视频。',
    
    'Yes, you can download TikTok stories before they expire. Visit our TikTok快拍下载器 to save stories permanently.':
        '可以，你可以在TikTok快拍过期前下载它们。访问我们的TikTok快拍下载器永久保存快拍。',
    
    'With DLTK TikTok video downloader, use our TikTok封面图下载器 to save video cover images in full resolution. Perfect for creating custom thumbnails or saving memorable moments.':
        '使用我们的TikTok封面图下载器，保存全分辨率视频封面图。非常适合制作自定义缩略图或保存难忘瞬间。',
    
    'DLTK is the best free TikTok video downloader - faster, easier, and more reliable than other TikTok video downloaders. We offer HD downloads, no watermarks, MP3 conversion, and work on all devices - completely free with no ads or registration required.':
        'DLTK是最好的免费TikTok视频下载器 - 比其他TikTok视频下载器更快、更简单、更可靠。我们提供HD下载、无水印、MP3转换，支持所有设备 - 完全免费，无广告，无需注册。',
    
    # 额外FAQ
    'How do I download my own TikTok videos?': '如何下载我自己的TikTok视频？',
    'With DLTK TikTok video downloader, to download your own TikTok videos, simply copy the link from your profile and paste it into DLTK. Our TikTok video downloader works for your own content just like any other video. You can download TikTok videos you created in HD quality without watermark.':
        '要下载你自己的TikTok视频，只需从你的个人资料复制链接并粘贴到DLTK。我们的TikTok视频下载器对你自己的内容和其他视频一样有效。你可以下载自己创作的TikTok视频，高清无水印。',
    
    'Why is my downloaded TikTok video low quality or blurry?': '为什么我下载的TikTok视频画质低或模糊？',
    'If your downloaded TikTok video appears blurry, the original upload may be low resolution. DLTK preserves the original video quality - we cannot enhance beyond what TikTok stored. Always select the highest quality option (HD or Full HD) when downloading TikTok videos for best results.':
        '如果你下载的TikTok视频看起来模糊，可能是原始上传的分辨率较低。DLTK保留原始视频画质 - 我们无法提升TikTok存储的画质。下载TikTok视频时始终选择最高画质选项（HD或Full HD）以获得最佳效果。',
    
    'Are TikTok downloader sites safe to use?': 'TikTok下载器网站安全吗？',
    'DLTK is completely safe. We don\'t store your videos, require login credentials, or collect personal data. Our TikTok video downloader runs securely in your browser with no malware or viruses. However, always be cautious with unknown TikTok downloader sites that ask for passwords or payment information.':
        'DLTK完全安全。我们不存储你的视频，不要求登录凭据，也不收集个人数据。我们的TikTok视频下载器在你的浏览器中安全运行，无恶意软件或病毒。但是，对于要求密码或付款信息的未知TikTok下载器网站，请务必小心。',
    
    'Can I download TikTok videos from private accounts?': '可以下载私密账户的TikTok视频吗？',
    'No, you cannot download TikTok videos from private accounts unless you follow that account. TikTok\'s privacy settings prevent public access to private videos. Our TikTok downloader can only download publicly available TikTok videos.':
        '不可以，除非你关注该账户，否则无法下载私密账户的TikTok视频。TikTok的隐私设置阻止公开访问私密视频。我们的TikTok下载器只能下载公开的TikTok视频。',
    
    'Why does my downloaded video still have a watermark?': '为什么我下载的视频还有水印？',
    'If your downloaded TikTok video still shows a watermark, try refreshing the page and downloading again. Ensure you\'re using DLTK\'s "Download Without Watermark" button. Occasionally, TikTok changes their system - if the issue persists, the video may have the watermark embedded in the original file.':
        '如果你下载的TikTok视频仍然显示水印，请尝试刷新页面并重新下载。确保你使用的是DLTK的"无水印下载"按钮。偶尔TikTok会更改其系统 - 如果问题持续存在，视频可能在原始文件中嵌入了水印。',
    
    'What format are downloaded TikTok videos?': '下载的TikTok视频是什么格式？',
    'Downloaded TikTok videos are saved as MP4 files, which work on all devices and media players. For audio-only downloads, visit our TikTok转MP3 converter to save as MP3 format. MP4 provides the best balance of quality and compatibility.':
        '下载的TikTok视频保存为MP4文件，可在所有设备和媒体播放器上播放。如需仅音频下载，请访问我们的TikTok转MP3转换器以MP3格式保存。MP4提供了质量和兼容性的最佳平衡。',
    
    'Can I download multiple TikTok videos at once?': '可以一次下载多个TikTok视频吗？',
    'Currently, DLTK processes one TikTok video at a time for optimal speed and quality. For batch downloads, simply paste each link one by one - our fast TikTok downloader processes videos in seconds. We recommend downloading TikTok videos individually to ensure the best quality and reliability.':
        '目前，DLTK一次处理一个TikTok视频，以获得最佳速度和质量。对于批量下载，只需逐个粘贴链接 - 我们快速的TikTok下载器可在几秒钟内处理视频。我们建议单独下载TikTok视频，以确保最佳质量和可靠性。',
    
    # 最终CTA
    'Start Downloading TikTok Videos Now': '立即开始下载TikTok视频',
    'DLTK is your go-to free TikTok video downloader for saving TikTok videos without watermarks. Our TikTok video downloader supports HD downloads, MP3 conversion, thumbnail extraction, and story downloads, you have everything you need to download TikTok content quickly and easily. Our free TikTok downloader works on all devices, requires no registration, and removes watermarks automatically.':
        'DLTK是你首选的免费TikTok视频下载工具，用于保存无水印TikTok视频。我们的TikTok视频下载器支持HD下载、MP3转换、封面图提取和快拍下载，你拥有快速轻松下载TikTok内容所需的一切。我们的免费TikTok下载器适用于所有设备，无需注册，自动去除水印。',
    
    'Whether you use our TikTok video downloader to download TikTok videos for personal viewing, create compilations, or save your favorite content, DLTK provides the fastest and most reliable way to download TikTok videos without watermark. Try DLTK - the #1 rated TikTok video downloader today - it\'s completely free, with no hidden fees and unlimited downloads!':
        '无论你使用我们的TikTok视频下载器下载TikTok视频用于个人观看、制作合集，还是保存你喜爱的内容，DLTK都提供最快、最可靠的无水印TikTok视频下载方式。立即试用DLTK - 排名第一的TikTok视频下载器 - 完全免费，无隐藏费用，无限下载！',
}

# 执行替换
for eng, chn in complete_translations.items():
    html = html.replace(eng, chn)

# 保存
with open('/root/.openclaw/workspace/tiktok-downloader/frontend/zh/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ 第三轮完整中文化完成")
print("📊 替换了", len(complete_translations), "个文本片段")
print("📄 最终文件大小：", len(html), "字符")
