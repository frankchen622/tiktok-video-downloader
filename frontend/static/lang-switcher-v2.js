// 🌍 多语言切换系统 - 完整版
// 支持：EN, ZH, ES, PT, FR, DE

// === 配置 ===
const LANGUAGE_CONFIG = {
  'en': {
    code: 'en',
    name: 'English',
    flag: '🇺🇸',
    shortName: 'EN',
    baseUrl: '/'
  },
  'zh': {
    code: 'zh',
    name: '简体中文',
    flag: '🇨🇳',
    shortName: '中文',
    baseUrl: '/zh/'
  },
  'es': {
    code: 'es',
    name: 'Español',
    flag: '🇪🇸',
    shortName: 'ES',
    baseUrl: '/es/'
  },
  'pt': {
    code: 'pt',
    name: 'Português',
    flag: '🇧🇷',
    shortName: 'PT',
    baseUrl: '/pt/'
  },
  'fr': {
    code: 'fr',
    name: 'Français',
    flag: '🇫🇷',
    shortName: 'FR',
    baseUrl: '/fr/'
  },
  'de': {
    code: 'de',
    name: 'Deutsch',
    flag: '🇩🇪',
    shortName: 'DE',
    baseUrl: '/de/'
  }
};

// 页面映射表 (中文特殊文件名)
const PAGE_MAPPING = {
  'en': {
    'index.html': 'index.html',
    'mp3.html': 'mp3.html',
    'thumbnail.html': 'thumbnail.html',
    'story.html': 'story.html'
  },
  'zh': {
    'index.html': 'index.html',
    'mp3.html': 'yinpin.html',       // 音频
    'thumbnail.html': 'fengmian.html', // 封面
    'story.html': 'kuaipai.html'       // 快拍
  },
  'es': {
    'index.html': 'index.html',
    'mp3.html': 'mp3.html',
    'thumbnail.html': 'miniatura.html',
    'story.html': 'historia.html'
  },
  'pt': {
    'index.html': 'index.html',
    'mp3.html': 'mp3.html',
    'thumbnail.html': 'miniatura.html',
    'story.html': 'historia.html'
  },
  'fr': {
    'index.html': 'index.html',
    'mp3.html': 'mp3.html',
    'thumbnail.html': 'miniatura.html',
    'story.html': 'historia.html'
  },
  'de': {
    'index.html': 'index.html',
    'mp3.html': 'mp3.html',
    'thumbnail.html': 'miniatur.html',
    'story.html': 'story.html'
  }
};

// === 核心函数 ===

// 获取当前页面类型
function getCurrentPageType() {
  const path = window.location.pathname;
  
  if (path.endsWith('mp3.html') || path.includes('yinpin.html')) {
    return 'mp3.html';
  } else if (path.endsWith('thumbnail.html') || path.includes('miniatura') || path.includes('fengmian') || path.includes('miniatur')) {
    return 'thumbnail.html';
  } else if (path.endsWith('story.html') || path.includes('historia') || path.includes('kuaipai')) {
    return 'story.html';
  } else {
    return 'index.html';
  }
}

// 检测当前语言
function detectCurrentLanguage() {
  const path = window.location.pathname;
  
  for (const [code, config] of Object.entries(LANGUAGE_CONFIG)) {
    if (code === 'en') continue; // 英语是默认的
    if (path.startsWith(config.baseUrl)) {
      return code;
    }
  }
  
  return 'en'; // 默认英语
}

// 构建目标URL
function buildTargetUrl(targetLang) {
  const currentPageType = getCurrentPageType();
  const targetConfig = LANGUAGE_CONFIG[targetLang];
  const targetFileName = PAGE_MAPPING[targetLang][currentPageType] || 'index.html';
  
  // 构建完整路径
  if (targetLang === 'en') {
    return '/' + targetFileName;
  } else {
    return targetConfig.baseUrl + targetFileName;
  }
}

// === 主切换函数 ===
window.switchLanguage = function(lang) {
  console.log('🌍 Switching to:', lang);
  
  // 保存语言偏好
  localStorage.setItem('dltk_lang', lang);
  
  // 构建目标URL
  const targetUrl = buildTargetUrl(lang);
  console.log('→ Target URL:', targetUrl);
  
  // 跳转
  window.location.href = targetUrl;
};

// === UI 更新函数 ===

// 更新当前语言显示
function updateCurrentLangText() {
  const currentLang = detectCurrentLanguage();
  const config = LANGUAGE_CONFIG[currentLang];
  const currentText = document.getElementById('currentLangText');
  
  if (currentText && config) {
    currentText.textContent = config.shortName;
  }
}

// 更新激活状态
function updateActiveButton() {
  const currentLang = detectCurrentLanguage();
  
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.remove('active');
    if (btn.dataset.lang === currentLang) {
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

// === 初始化 ===
document.addEventListener('DOMContentLoaded', function() {
  console.log('🌍 Language switcher v2 initializing...');
  
  const langCurrent = document.getElementById('langCurrent');
  const langSwitcher = document.getElementById('langSwitcher');
  
  if (!langCurrent || !langSwitcher) {
    console.warn('Language switcher elements not found');
    return;
  }
  
  // 切换下拉菜单
  langCurrent.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    langSwitcher.classList.toggle('active');
  });
  
  // 点击外部关闭
  document.addEventListener('click', function(e) {
    if (!langSwitcher.contains(e.target)) {
      langSwitcher.classList.remove('active');
    }
  });
  
  // 更新UI
  updateCurrentLangText();
  updateActiveButton();
  
  console.log('✅ Language switcher ready! Current:', detectCurrentLanguage());
});
