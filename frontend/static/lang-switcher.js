// 多语言切换系统 - 通过 URL 导航切换语言
(function() {
  'use strict';
  
  console.log('🌍 Language switcher loading...');
  
  // 语言路径映射
  const langPaths = {
    'en': '/',
    'zh': '/zh/',
    'es': '/es/',
    'pt': '/pt/',
    'fr': '/fr/',
    'de': '/de/'
  };
  
  // 语言显示名称
  const langNames = {
    'en': '🇺🇸 EN',
    'zh': '🇨🇳 中文',
    'es': '🇪🇸 ES',
    'pt': '🇧🇷 PT',
    'fr': '🇫🇷 FR',
    'de': '🇩🇪 DE'
  };
  
  // 页面名称映射（不同语言的页面名称）
  const pageNames = {
    'mp3': {
      'en': 'mp3',
      'zh': 'yinpin',
      'es': 'mp3',
      'pt': 'mp3',
      'fr': 'mp3',
      'de': 'mp3'
    },
    'thumbnail': {
      'en': 'thumbnail',
      'zh': 'fengmian',
      'es': 'miniatura',
      'pt': 'miniatura',
      'fr': 'miniatura',
      'de': 'miniatur'
    },
    'story': {
      'en': 'story',
      'zh': 'kuaipai',
      'es': 'historia',
      'pt': 'historia',
      'fr': 'historia',
      'de': 'story'
    }
  };
  
  // 检测当前语言
  function getCurrentLanguage() {
    const path = window.location.pathname;
    
    // 从路径检测语言
    if (path.startsWith('/zh/')) return 'zh';
    if (path.startsWith('/es/')) return 'es';
    if (path.startsWith('/pt/')) return 'pt';
    if (path.startsWith('/fr/')) return 'fr';
    if (path.startsWith('/de/')) return 'de';
    
    return 'en';
  }
  
  // 检测当前页面类型
  function getPageType() {
    const path = window.location.pathname;
    const filename = path.split('/').pop().replace('.html', '');
    
    // 检查是否是首页
    if (filename === '' || filename === 'index') {
      return 'index';
    }
    
    // 检查各种页面名称映射
    for (const [pageType, names] of Object.entries(pageNames)) {
      if (Object.values(names).includes(filename)) {
        return pageType;
      }
    }
    
    return 'index'; // 默认返回首页
  }
  
  // 切换语言函数
  window.switchLanguage = function(targetLang) {
    console.log('🔄 Switching to:', targetLang);
    
    if (!langPaths[targetLang]) {
      console.error('❌ Language not supported:', targetLang);
      return;
    }
    
    const currentLang = getCurrentLanguage();
    
    // 如果已经是目标语言，关闭下拉菜单但不跳转
    if (currentLang === targetLang) {
      console.log('ℹ️ Already on', targetLang);
      const switcher = document.getElementById('langSwitcher');
      if (switcher) switcher.classList.remove('active');
      return;
    }
    
    // 保存语言偏好
    localStorage.setItem('dltk_lang', targetLang);
    
    // 获取当前页面类型
    const pageType = getPageType();
    
    // 构建目标 URL
    let targetPath;
    
    if (pageType === 'index') {
      // 首页
      targetPath = langPaths[targetLang];
    } else {
      // 其他页面
      const pageName = pageNames[pageType][targetLang];
      if (targetLang === 'en') {
        targetPath = `/${pageName}.html`;
      } else {
        targetPath = `/${targetLang}/${pageName}.html`;
      }
    }
    
    console.log('🚀 Navigating from', pageType, 'to:', targetPath);
    window.location.href = targetPath;
  };
  
  // 初始化语言切换器
  document.addEventListener('DOMContentLoaded', function() {
    console.log('📦 Initializing language switcher...');
    
    const langCurrent = document.getElementById('langCurrent');
    const langSwitcher = document.getElementById('langSwitcher');
    const currentLangText = document.getElementById('currentLangText');
    
    if (!langCurrent || !langSwitcher) {
      console.error('❌ Language switcher elements not found');
      return;
    }
    
    // 设置当前语言显示
    const currentLang = getCurrentLanguage();
    if (currentLangText) {
      currentLangText.textContent = langNames[currentLang];
    }
    
    // 高亮当前语言按钮
    document.querySelectorAll('.lang-btn').forEach(btn => {
      const btnLang = btn.getAttribute('data-lang');
      if (btnLang === currentLang) {
        btn.classList.add('active');
      }
    });
    
    // 切换下拉菜单
    langCurrent.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      langSwitcher.classList.toggle('active');
      console.log('🖱️ Dropdown toggled');
    });
    
    // 点击外部关闭下拉菜单
    document.addEventListener('click', function(e) {
      if (!langSwitcher.contains(e.target)) {
        langSwitcher.classList.remove('active');
      }
    });
    
    console.log('✅ Language switcher ready! Current:', currentLang, '| Page:', getPageType());
  });
  
})();


