#!/bin/bash
# 修复所有页面的语言切换器配置

echo "🔧 修复所有页面的语言切换器..."
echo ""

cd frontend

# 标准的语言按钮配置（正确的）
CORRECT_BUTTONS='            <button class="lang-btn" data-lang="en" onclick="switchLanguage('\''en'\'')">🇺🇸 English</button>
            <button class="lang-btn" data-lang="zh" onclick="switchLanguage('\''zh'\'')">🇨🇳 简体中文</button>
            <button class="lang-btn" data-lang="es" onclick="switchLanguage('\''es'\'')">🇪🇸 Español</button>
            <button class="lang-btn" data-lang="pt" onclick="switchLanguage('\''pt'\'')">🇧🇷 Português</button>
            <button class="lang-btn" data-lang="fr" onclick="switchLanguage('\''fr'\'')">🇫🇷 Français</button>
            <button class="lang-btn" data-lang="de" onclick="switchLanguage('\''de'\'')">🇩🇪 Deutsch</button>
            <button class="lang-btn" data-lang="id" onclick="switchLanguage('\''id'\'')">🇮🇩 Indonesia</button>'

# 修复所有语言目录的页面
for lang in es pt fr de zh; do
  echo "修复 $lang 目录..."
  for file in $lang/*.html; do
    if [ -f "$file" ] && grep -q "lang-dropdown" "$file"; then
      # 提取 lang-dropdown 之前和之后的内容
      # 使用 Python 来精确替换
      python3 << EOF
import re

with open('$file', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 lang-dropdown 部分并替换按钮
pattern = r'(<div class="lang-dropdown">)(.*?)(</div>)'
replacement = r'\1\n$CORRECT_BUTTONS\n          \3'

# 使用正则替换
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('$file', 'w', encoding='utf-8') as f:
    f.write(content)

print('  ✓ $(basename $file)')
EOF
    fi
  done
  echo ""
done

echo "✅ 所有页面修复完成"
