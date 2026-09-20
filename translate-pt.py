#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TikTok Downloader - 葡萄牙语翻译脚本
基于英文版本，翻译为巴西葡萄牙语
"""

import re
import os

# 关键词翻译词典（巴西葡萄牙语）
PT_TRANSLATIONS = {
    # 标题和描述
    "TikTok Video Downloader Without Watermark": "Baixar Vídeos do TikTok Sem Marca d'Água",
    "Free & Fast": "Grátis e Rápido",
    "Download TikTok videos without watermark": "Baixe vídeos do TikTok sem marca d'água",
    "in HD quality": "em qualidade HD",
    "Save TikTok to MP4 instantly": "Salve TikTok em MP4 instantaneamente",
    "no app, no registration": "sem app, sem cadastro",
    "100% free TikTok video downloader": "Baixador de vídeos TikTok 100% grátis",
    "Try now!": "Experimente agora!",
    
    # 功能特性
    "No Watermark": "Sem Marca d'Água",
    "HD Quality": "Qualidade HD",
    "Fast Download": "Download Rápido",
    "Free Forever": "Grátis Para Sempre",
    "All Devices": "Todos os Dispositivos",
    "No Registration": "Sem Cadastro",
    "Private & Safe": "Privado e Seguro",
    "MP3 Converter": "Conversor MP3",
    
    # 按钮和操作
    "Download": "Baixar",
    "Convert": "Converter",
    "Save": "Salvar",
    "Copy": "Copiar",
    "Paste": "Colar",
    "Share": "Compartilhar",
    
    # 导航
    "Video": "Vídeo",
    "MP3": "MP3",
    "Thumbnail": "Miniatura",
    "Story": "Story",
    "Contact": "Contato",
    "Privacy": "Privacidade",
    "Terms": "Termos",
    
    # FAQ
    "Frequently Asked Questions": "Perguntas Frequentes",
    "Is DLTK free to use?": "O DLTK é grátis?",
    "How do I download TikTok videos?": "Como faço para baixar vídeos do TikTok?",
    
    # 通用词汇
    "Yes": "Sim",
    "No": "Não",
    "Free": "Grátis",
    "Quality": "Qualidade",
    "Video": "Vídeo",
    "Audio": "Áudio",
    "Image": "Imagem",
}

def translate_meta_tags(content):
    """翻译 meta 标签"""
    translations = [
        # Title
        (r'<title>TikTok Video Downloader Without Watermark - Free & Fast \| DLTK</title>',
         '<title>Baixar Vídeos do TikTok Sem Marca d\'Água - Grátis e Rápido | DLTK</title>'),
        
        # Description
        (r'<meta name="description" content="Download TikTok videos without watermark in HD quality\. Save TikTok to MP4 instantly - no app, no registration\. 100% free TikTok video downloader\. Try now!" />',
         '<meta name="description" content="Baixe vídeos do TikTok sem marca d\'água em qualidade HD. Salve TikTok em MP4 instantaneamente - sem app, sem cadastro. Baixador de vídeos TikTok 100% grátis. Experimente agora!" />'),
        
        # OG Title
        (r'<meta property="og:title" content="TikTok Video Downloader Without Watermark - Free & Fast" />',
         '<meta property="og:title" content="Baixar Vídeos do TikTok Sem Marca d\'Água - Grátis e Rápido" />'),
        
        # OG Description
        (r'<meta property="og:description" content="Download TikTok videos without watermark in seconds\. HD quality, no registration, completely free\." />',
         '<meta property="og:description" content="Baixe vídeos do TikTok sem marca d\'água em segundos. Qualidade HD, sem cadastro, completamente grátis." />'),
        
        # Twitter Title
        (r'<meta name="twitter:title" content="TikTok Video Downloader Without Watermark - Free & Fast" />',
         '<meta name="twitter:title" content="Baixar Vídeos do TikTok Sem Marca d\'Água - Grátis e Rápido" />'),
        
        # Twitter Description
        (r'<meta name="twitter:description" content="Download TikTok videos without watermark in seconds\. HD quality, no registration, completely free\." />',
         '<meta name="twitter:description" content="Baixe vídeos do TikTok sem marca d\'água em segundos. Qualidade HD, sem cadastro, completamente grátis." />'),
    ]
    
    for pattern, replacement in translations:
        content = re.sub(pattern, replacement, content)
    
    return content

print("葡萄牙语翻译脚本已加载")
print("使用巴西葡萄牙语标准（você）")
