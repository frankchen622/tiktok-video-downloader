// 多语言切换系统 - 通过 URL 导航切换语言
(function() {
  'use strict';
  
  console.log('🌍 Language switcher loading...');
  
  // 语言显示名称
  const langNames = {
    'en': '🇺🇸 EN',
    'zh': '🇨🇳 中文',
    'es': '🇪🇸 ES',
    'pt': '🇧🇷 PT',
    'fr': '🇫🇷 FR',
    'de': '🇩🇪 DE'
  };
  
  // 每种页面在各语言下的标准路径
  const pagePaths = {
    'index':      { en: '/',                       zh: '/zh',          es: '/es',            pt: '/pt',             fr: '/fr',                 de: '/de' },
    'mp3':        { en: '/mp3',                    zh: '/zh/yinpin',   es: '/es/mp3',        pt: '/pt/mp3',         fr: '/fr/mp3',             de: '/de/mp3' },
    'thumbnail':  { en: '/thumbnail',              zh: '/zh/fengmian', es: '/es/thumbnail',  pt: '/pt/thumbnail',   fr: '/fr/thumbnail',       de: '/de/thumbnail' },
    'story':      { en: '/story',                  zh: '/zh/kuaipai',  es: '/es/story',      pt: '/pt/story',       fr: '/fr/story',           de: '/de/story' },
    'contact':    { en: '/pages/contact.html',     zh: '/zh/lianxi',   es: '/es/contacto',   pt: '/pt/contato',     fr: '/fr/contact',         de: '/de/kontakt' },
    'privacy':    { en: '/pages/privacy.html',     zh: '/zh/yinsi',    es: '/es/privacidad', pt: '/pt/privacidade', fr: '/fr/confidentialite', de: '/de/datenschutz' },
    'terms':      { en: '/pages/terms.html',       zh: '/zh/tiaokuan', es: '/es/terminos',   pt: '/pt/termos',      fr: '/fr/conditions',      de: '/de/nutzungsbedingungen' },
    'disclaimer': { en: '/pages/disclaimer.html',  zh: '/zh/mianze',   es: '/es/descargo',   pt: '/pt/aviso-legal', fr: '/fr/avertissement',   de: '/de/haftungsausschluss' },
    'dmca':       { en: '/pages/dmca.html',        zh: '/zh/banquan',  es: '/es/dmca',       pt: '/pt/dmca',        fr: '/fr/dmca',            de: '/de/dmca' },
    'cookies':    { en: '/pages/cookies.html',     zh: '/zh/cookie',   es: '/es/cookies',    pt: '/pt/cookies',     fr: '/fr/cookies',         de: '/de/cookies' }
  };

  // 旧URL，仅用于识别页面类型（服务端会301到标准URL）
  const legacyPaths = {
    '/mp3.html': 'mp3', '/thumbnail.html': 'thumbnail', '/story.html': 'story',
    '/es/miniatura': 'thumbnail', '/pt/miniatura': 'thumbnail', '/fr/miniatura': 'thumbnail', '/de/miniatur': 'thumbnail',
    '/es/historia': 'story', '/pt/historia': 'story', '/fr/historia': 'story'
  };
  
  // 检测当前语言
  function getCurrentLanguage() {
    const path = window.location.pathname;
    const match = path.match(/^\/(zh|es|pt|fr|de)(\/|$)/);
    return match ? match[1] : 'en';
  }
  
  // 检测当前页面类型
  function getPageType() {
    let path = window.location.pathname;
    if (path.length > 1) path = path.replace(/\/+$/, '');
    if (path === '/index.html') return 'index';
    if (legacyPaths[path]) return legacyPaths[path];
    for (const [pageType, paths] of Object.entries(pagePaths)) {
      if (Object.values(paths).includes(path)) return pageType;
    }
    return 'index';
  }
  
  // 切换语言函数
  window.switchLanguage = function(targetLang) {
    console.log('🔄 Switching to:', targetLang);
    
    if (!pagePaths.index[targetLang]) {
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
    
    const targetPath = pagePaths[pageType][targetLang];
    
    console.log('🚀 Navigating from', pageType, 'to:', targetPath);
    window.location.href = targetPath;
  };
  
  // 初始化语言切换器
  document.addEventListener('DOMContentLoaded', function() {
    console.log('📦 Initializing language switcher...');
    
    const langCurrent = document.getElementById('langCurrent');
    const langSwitcher = document.getElementById('langSwitcher');
    const currentLangText = document.getElementById('currentLangText');
    const currentLang = getCurrentLanguage();
    const header = document.querySelector('.site-header');
    const navToggle = document.getElementById('navToggle');
    const siteNav = document.getElementById('siteNav');
    
    // 高亮当前语言按钮
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === currentLang);
    });

    function closeNav() {
      if (!header || !navToggle) return;
      header.classList.remove('nav-open');
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.setAttribute('aria-label', 'Open menu');
    }

    if (navToggle && header) {
      navToggle.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        const open = header.classList.toggle('nav-open');
        navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        navToggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        if (open && langSwitcher) langSwitcher.classList.remove('active');
      });
    }
    
    if (langCurrent && langSwitcher) {
      if (currentLangText) {
        currentLangText.textContent = langNames[currentLang];
      }

      langCurrent.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        langSwitcher.classList.toggle('active');
        closeNav();
        console.log('🖱️ Dropdown toggled');
      });
    }

    document.addEventListener('click', function(e) {
      if (langSwitcher && !langSwitcher.contains(e.target)) {
        langSwitcher.classList.remove('active');
      }
      if (header && navToggle && siteNav &&
          header.classList.contains('nav-open') &&
          !siteNav.contains(e.target) &&
          !navToggle.contains(e.target)) {
        closeNav();
      }
    });

    window.addEventListener('resize', function() {
      if (window.innerWidth > 768) closeNav();
    });
    
    console.log('✅ Language switcher ready! Current:', currentLang, '| Page:', getPageType());
  });
  
})();


