// 完整的语言切换系统 - 所有代码在一个文件中
(function() {
  'use strict';
  
  console.log('🌍 Language system loading...');
  
  // 1. 翻译数据（简化版，只包含关键内容）
  const translations = {
    en: { nav_video: "Video", nav_mp3: "MP3", nav_thumbnail: "Thumbnail", nav_story: "Story", hero_title: "TikTok Video Downloader Without Watermark", hero_subtitle: "Free, Fast & HD Quality" },
    zh: { nav_video: "视频", nav_mp3: "MP3", nav_thumbnail: "封面", nav_story: "故事", hero_title: "TikTok视频下载器 - 无水印", hero_subtitle: "免费、快速、高清画质" },
    es: { nav_video: "Video", nav_mp3: "MP3", nav_thumbnail: "Miniatura", nav_story: "Historia", hero_title: "Descargar Videos de TikTok Sin Marca de Agua", hero_subtitle: "Gratis, Rápido y HD" },
    pt: { nav_video: "Vídeo", nav_mp3: "MP3", nav_thumbnail: "Miniatura", nav_story: "Story", hero_title: "Baixar Vídeos do TikTok Sem Marca D'água", hero_subtitle: "Grátis, Rápido e HD" },
    id: { nav_video: "Video", nav_mp3: "MP3", nav_thumbnail: "Thumbnail", nav_story: "Story", hero_title: "Download Video TikTok Tanpa Watermark", hero_subtitle: "Gratis, Cepat & HD" }
  };
  
  // 2. 当前语言
  let currentLang = localStorage.getItem('dltk_lang') || navigator.language.split('-')[0] || 'en';
  if (!translations[currentLang]) currentLang = 'en';
  
  console.log('📍 Initial language:', currentLang);
  
  // 3. 切换语言函数
  window.switchLanguage = function(lang) {
    console.log('🔄 Switching to:', lang);
    
    if (!translations[lang]) {
      console.error('❌ Language not found:', lang);
      return;
    }
    
    currentLang = lang;
    localStorage.setItem('dltk_lang', lang);
    
    // 更新所有元素
    let count = 0;
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const text = translations[lang][key];
      
      if (text) {
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
          el.placeholder = text;
        } else {
          el.textContent = text;
        }
        count++;
      }
    });
    
    console.log('✅ Updated', count, 'elements');
    
    // 更新按钮显示
    const langNames = { en: 'EN', zh: '中文', es: 'ES', pt: 'PT', id: 'ID' };
    const btn = document.getElementById('currentLangText');
    if (btn) btn.textContent = langNames[lang];
    
    // 关闭下拉菜单
    const switcher = document.getElementById('langSwitcher');
    if (switcher) switcher.classList.remove('active');
    
    console.log('🎉 Language switch complete!');
  };
  
  // 4. 初始化下拉菜单
  document.addEventListener('DOMContentLoaded', function() {
    console.log('📦 Initializing dropdown...');
    
    const langCurrent = document.getElementById('langCurrent');
    const langSwitcher = document.getElementById('langSwitcher');
    
    if (!langCurrent || !langSwitcher) {
      console.error('❌ Dropdown elements not found');
      return;
    }
    
    // 点击切换
    langCurrent.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      langSwitcher.classList.toggle('active');
      console.log('🖱️ Dropdown toggled');
    });
    
    // 点击外部关闭
    document.addEventListener('click', function(e) {
      if (!langSwitcher.contains(e.target)) {
        langSwitcher.classList.remove('active');
      }
    });
    
    // 初始化显示
    const langNames = { en: 'EN', zh: '中文', es: 'ES', pt: 'PT', id: 'ID' };
    const btn = document.getElementById('currentLangText');
    if (btn) btn.textContent = langNames[currentLang];
    
    // 应用初始语言
    switchLanguage(currentLang);
    
    console.log('✅ Language system ready!');
  });
  
})();
