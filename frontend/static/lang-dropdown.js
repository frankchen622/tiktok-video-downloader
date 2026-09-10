// Language switcher dropdown control
// 必须在 DOM 加载完成后执行

document.addEventListener('DOMContentLoaded', function() {
  console.log('Language switcher initializing...');
  
  const langCurrent = document.getElementById('langCurrent');
  const langSwitcher = document.getElementById('langSwitcher');
  
  if (!langCurrent || !langSwitcher) {
    console.error('Language switcher elements not found!');
    return;
  }
  
  console.log('Language switcher elements found');
  
  // 点击当前语言按钮，切换下拉菜单
  langCurrent.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    console.log('Language button clicked');
    langSwitcher.classList.toggle('active');
  });
  
  // 点击页面其他地方，关闭下拉菜单
  document.addEventListener('click', function(e) {
    if (!langSwitcher.contains(e.target)) {
      langSwitcher.classList.remove('active');
    }
  });
  
  // 阻止下拉菜单内的点击冒泡
  const langDropdown = langSwitcher.querySelector('.lang-dropdown');
  if (langDropdown) {
    langDropdown.addEventListener('click', function(e) {
      e.stopPropagation();
    });
  }
  
  console.log('Language switcher ready!');
});

// 全局函数：切换语言
window.switchLanguage = function(lang) {
  console.log('switchLanguage called with:', lang);
  console.log('i18n object exists:', typeof i18n !== 'undefined');
  
  if (typeof i18n !== 'undefined') {
    console.log('i18n.setLanguage exists:', typeof i18n.setLanguage === 'function');
    console.log('Current language before switch:', i18n.currentLang);
    
    if (i18n.setLanguage) {
      i18n.setLanguage(lang);
      console.log('Language switched to:', i18n.currentLang);
      console.log('Testing translation:', i18n.t('nav_video'));
      
      updateCurrentLangText(lang);
      closeLangDropdown();
    } else {
      console.error('i18n.setLanguage is not a function!');
    }
  } else {
    console.error('i18n object not found! Window.i18n:', window.i18n);
  }
};

// 更新当前语言显示文本
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

// 关闭下拉菜单
function closeLangDropdown() {
  const switcher = document.getElementById('langSwitcher');
  if (switcher) {
    switcher.classList.remove('active');
  }
}
