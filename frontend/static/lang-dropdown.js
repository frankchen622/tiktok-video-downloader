// 简化的语言切换系统 - 确保可靠工作

// 全局切换函数
window.switchLanguage = function(lang) {
  console.log('=== Language Switch Started ===');
  console.log('Target language:', lang);
  
  // 直接调用 window.i18n 的方法
  if (typeof window.i18n !== 'undefined' && window.i18n) {
    console.log('i18n found, current lang:', window.i18n.currentLang);
    
    // 设置语言
    window.i18n.currentLang = lang;
    localStorage.setItem('dltk_lang', lang);
    console.log('Language set to:', window.i18n.currentLang);
    
    // 立即更新页面
    updatePageTranslations(lang);
    
    // 更新按钮文字
    updateCurrentLangText(lang);
    
    // 更新激活状态
    updateActiveButton(lang);
    
    // 关闭下拉菜单
    closeLangDropdown();
    
    console.log('=== Language Switch Complete ===');
  } else {
    console.error('i18n not found!');
  }
};

// 更新页面翻译
function updatePageTranslations(lang) {
  console.log('Updating page translations for:', lang);
  
  if (typeof window.translations === 'undefined') {
    console.error('window.translations object not found!');
    return;
  }
  
  const trans = window.translations[lang] || window.translations['en'];
  let updateCount = 0;
  
  // 更新所有带 data-i18n 的元素
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    const text = trans[key];
    
    if (text) {
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        el.placeholder = text;
      } else if (el.tagName === 'BUTTON') {
        const textSpan = el.querySelector('.btn-text');
        if (textSpan) {
          textSpan.textContent = text;
        } else {
          el.textContent = text;
        }
      } else {
        el.textContent = text;
      }
      updateCount++;
    } else {
      console.warn('Missing translation for key:', key);
    }
  });
  
  console.log('Updated', updateCount, 'elements');
}

// 更新当前语言显示
function updateCurrentLangText(lang) {
  const langNames = {
    'en': 'EN',
    'zh': '中文',
    'es': 'ES',
    'pt': 'PT',
    'id': 'ID'
  };
  const currentText = document.getElementById('currentLangText');
  if (currentText) {
    currentText.textContent = langNames[lang] || 'EN';
  }
}

// 更新激活按钮
function updateActiveButton(lang) {
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.remove('active');
    if (btn.dataset.lang === lang) {
      btn.classList.add('active');
    }
  });
}

// 关闭下拉菜单
function closeLangDropdown() {
  const switcher = document.getElementById('langSwitcher');
  if (switcher) {
    switcher.classList.remove('active');
  }
}

// 初始化下拉菜单控制
document.addEventListener('DOMContentLoaded', function() {
  console.log('Language dropdown initializing...');
  
  const langCurrent = document.getElementById('langCurrent');
  const langSwitcher = document.getElementById('langSwitcher');
  
  if (!langCurrent || !langSwitcher) {
    console.error('Language switcher elements not found!');
    return;
  }
  
  console.log('Elements found, setting up listeners');
  
  // 点击切换下拉菜单
  langCurrent.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    console.log('Language button clicked');
    langSwitcher.classList.toggle('active');
  });
  
  // 点击外部关闭
  document.addEventListener('click', function(e) {
    if (!langSwitcher.contains(e.target)) {
      langSwitcher.classList.remove('active');
    }
  });
  
  // 初始化当前语言显示
  if (window.i18n !== 'undefined' && window.i18n.currentLang) {
    updateCurrentLangText(i18n.currentLang);
    updateActiveButton(i18n.currentLang);
  }
  
  console.log('Language dropdown ready!');
});
