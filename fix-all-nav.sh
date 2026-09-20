#!/bin/bash
# 批量修复所有语言版本的导航栏

echo "🔧 修复中文页面导航栏..."

# 修复中文页面（zh/）
for file in frontend/zh/*.html; do
  if [ -f "$file" ]; then
    echo "  修复: $file"
    
    # 替换导航栏链接文本为中文
    sed -i 's|<a href="/zh" data-i18n="nav_video">Video</a>|<a href="/zh">视频</a>|g' "$file"
    sed -i 's|<a href="/zh/yinpin" data-i18n="nav_mp3">MP3</a>|<a href="/zh/yinpin">音频</a>|g' "$file"
    sed -i 's|<a href="/zh/fengmian" data-i18n="nav_thumbnail">Thumbnail</a>|<a href="/zh/fengmian">封面</a>|g' "$file"
    sed -i 's|<a href="/zh/kuaipai" data-i18n="nav_story">Story</a>|<a href="/zh/kuaipai">快拍</a>|g' "$file"
    
    # 修复语言切换器
    sed -i 's|<span id="currentLangText">EN</span>|<span id="currentLangText">中文</span>|g' "$file"
    sed -i 's|data-lang="zh-CN"|data-lang="en"|g' "$file"
    sed -i 's|data-lang="id"|data-lang="fr"|g' "$file"
    sed -i 's|🇮🇩 Indonesia|🇫🇷 Français|g' "$file"
    
    # 添加德语选项（如果不存在）
    if ! grep -q "🇩🇪 Deutsch" "$file"; then
      sed -i 's|</div><!-- lang-dropdown -->|            <button class="lang-btn" data-lang="de" onclick="switchLanguage('\''de'\'')">🇩🇪 Deutsch</button>\n          </div>|g' "$file"
    fi
  fi
done

echo ""
echo "🔧 修复西班牙语页面导航栏..."

# 修复西班牙语页面（es/）
for file in frontend/es/*.html; do
  if [ -f "$file" ]; then
    echo "  修复: $file"
    
    sed -i 's|<a href="/es" data-i18n="nav_video">Video</a>|<a href="/es">Video</a>|g' "$file"
    sed -i 's|<a href="/es/mp3" data-i18n="nav_mp3">MP3</a>|<a href="/es/mp3">MP3</a>|g' "$file"
    sed -i 's|<a href="/es/miniatura" data-i18n="nav_thumbnail">Thumbnail</a>|<a href="/es/miniatura">Miniatura</a>|g' "$file"
    sed -i 's|<a href="/es/historia" data-i18n="nav_story">Story</a>|<a href="/es/historia">Historia</a>|g' "$file"
    
    sed -i 's|<span id="currentLangText">EN</span>|<span id="currentLangText">ES</span>|g' "$file"
    sed -i 's|data-lang="zh-CN"|data-lang="en"|g' "$file"
    sed -i 's|data-lang="id"|data-lang="fr"|g' "$file"
    sed -i 's|🇮🇩 Indonesia|🇫🇷 Français|g' "$file"
  fi
done

echo ""
echo "🔧 修复葡萄牙语页面导航栏..."

# 修复葡萄牙语页面（pt/）
for file in frontend/pt/*.html; do
  if [ -f "$file" ]; then
    echo "  修复: $file"
    
    sed -i 's|<a href="/pt" data-i18n="nav_video">Video</a>|<a href="/pt">Vídeo</a>|g' "$file"
    sed -i 's|<a href="/pt/mp3" data-i18n="nav_mp3">MP3</a>|<a href="/pt/mp3">MP3</a>|g' "$file"
    sed -i 's|<a href="/pt/miniatura" data-i18n="nav_thumbnail">Thumbnail</a>|<a href="/pt/miniatura">Miniatura</a>|g' "$file"
    sed -i 's|<a href="/pt/historia" data-i18n="nav_story">Story</a>|<a href="/pt/historia">História</a>|g' "$file"
    
    sed -i 's|<span id="currentLangText">EN</span>|<span id="currentLangText">PT</span>|g' "$file"
    sed -i 's|data-lang="zh-CN"|data-lang="en"|g' "$file"
    sed -i 's|data-lang="id"|data-lang="fr"|g' "$file"
    sed -i 's|🇮🇩 Indonesia|🇫🇷 Français|g' "$file"
  fi
done

echo ""
echo "🔧 修复法语页面导航栏..."

# 修复法语页面（fr/）
for file in frontend/fr/*.html; do
  if [ -f "$file" ]; then
    echo "  修复: $file"
    
    sed -i 's|<a href="/fr" data-i18n="nav_video">Video</a>|<a href="/fr">Vidéo</a>|g' "$file"
    sed -i 's|<a href="/fr/mp3" data-i18n="nav_mp3">MP3</a>|<a href="/fr/mp3">MP3</a>|g' "$file"
    sed -i 's|<a href="/fr/miniatura" data-i18n="nav_thumbnail">Thumbnail</a>|<a href="/fr/miniatura">Miniature</a>|g' "$file"
    sed -i 's|<a href="/fr/historia" data-i18n="nav_story">Story</a>|<a href="/fr/historia">Histoire</a>|g' "$file"
    
    sed -i 's|<span id="currentLangText">EN</span>|<span id="currentLangText">FR</span>|g' "$file"
    sed -i 's|data-lang="zh-CN"|data-lang="en"|g' "$file"
    sed -i 's|data-lang="id"|data-lang="de"|g' "$file"
    sed -i 's|🇮🇩 Indonesia|🇩🇪 Deutsch|g' "$file"
  fi
done

echo ""
echo "🔧 修复德语页面导航栏..."

# 修复德语页面（de/）
for file in frontend/de/*.html; do
  if [ -f "$file" ]; then
    echo "  修复: $file"
    
    sed -i 's|<a href="/de" data-i18n="nav_video">Video</a>|<a href="/de">Video</a>|g' "$file"
    sed -i 's|<a href="/de/mp3" data-i18n="nav_mp3">MP3</a>|<a href="/de/mp3">MP3</a>|g' "$file"
    sed -i 's|<a href="/de/miniatur" data-i18n="nav_thumbnail">Thumbnail</a>|<a href="/de/miniatur">Miniatur</a>|g' "$file"
    sed -i 's|<a href="/de/story" data-i18n="nav_story">Story</a>|<a href="/de/story">Story</a>|g' "$file"
    
    sed -i 's|<span id="currentLangText">EN</span>|<span id="currentLangText">DE</span>|g' "$file"
    sed -i 's|data-lang="zh-CN"|data-lang="en"|g' "$file"
    sed -i 's|data-lang="id"|data-lang="fr"|g' "$file"
    sed -i 's|🇮🇩 Indonesia|🇫🇷 Français|g' "$file"
  fi
done

echo ""
echo "✅ 所有导航栏修复完成！"

