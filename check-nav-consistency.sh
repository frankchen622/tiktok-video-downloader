#!/bin/bash
# 全面检查所有语言的导航栏一致性

echo "🔍 检查所有语言导航栏一致性..."
echo ""

cd frontend

# 中文
echo "🇨🇳 中文页面:"
for file in zh/*.html; do
  nav=$(grep -A 4 "site-nav" "$file" | grep "<a href" | head -4 | sed 's/.*>//g' | sed 's/<\/a>//g' | tr '\n' ' ')
  echo "  $(basename $file): $nav"
done
echo ""

# 西班牙语
echo "🇪🇸 西班牙语页面:"
for file in es/*.html; do
  nav=$(grep -A 4 "site-nav" "$file" | grep "<a href" | head -4 | sed 's/.*>//g' | sed 's/<\/a>//g' | tr '\n' ' ')
  echo "  $(basename $file): $nav"
done
echo ""

# 葡萄牙语
echo "🇧🇷 葡萄牙语页面:"
for file in pt/*.html; do
  nav=$(grep -A 4 "site-nav" "$file" | grep "<a href" | head -4 | sed 's/.*>//g' | sed 's/<\/a>//g' | tr '\n' ' ')
  echo "  $(basename $file): $nav"
done
echo ""

# 法语
echo "🇫🇷 法语页面:"
for file in fr/*.html; do
  nav=$(grep -A 4 "site-nav" "$file" | grep "<a href" | head -4 | sed 's/.*>//g' | sed 's/<\/a>//g' | tr '\n' ' ')
  echo "  $(basename $file): $nav"
done
echo ""

# 德语
echo "🇩🇪 德语页面:"
for file in de/*.html; do
  nav=$(grep -A 4 "site-nav" "$file" | grep "<a href" | head -4 | sed 's/.*>//g' | sed 's/<\/a>//g' | tr '\n' ' ')
  echo "  $(basename $file): $nav"
done
echo ""

echo "✅ 检查完成"
