#!/bin/bash
# 验证整站语言选项一致性

echo "🌍 验证整站多语言选项一致性"
echo "================================"
echo ""

cd frontend

TOTAL=0
PASS=0
FAIL=0

# 检查所有 HTML 文件
for file in $(find . -name "*.html" -type f | grep -v "before\|old-backup\|test-"); do
  # 跳过没有语言切换器的简单页面
  if ! grep -q "lang-dropdown\|lang-switcher" "$file"; then
    continue
  fi
  
  ((TOTAL++))
  
  count=$(grep -o 'data-lang=' "$file" | wc -l)
  
  if [ "$count" -eq 6 ]; then
    ((PASS++))
    
    # 检查是否包含错误的印尼语
    if grep -q 'data-lang="id"' "$file"; then
      echo "❌ $file: 包含印尼语 (id)"
      ((FAIL++))
      ((PASS--))
    fi
  else
    echo "❌ $file: $count 个语言（应该是 6）"
    ((FAIL++))
  fi
done

echo ""
echo "================================"
echo "总计: $TOTAL 个页面"
echo "✅ 通过: $PASS"
echo "❌ 失败: $FAIL"
echo "================================"
echo ""

if [ "$FAIL" -eq 0 ]; then
  echo "🎉 所有页面的语言选项都正确！"
  echo ""
  echo "✅ 所有页面都包含完整的 6 种语言："
  echo "   🇺🇸 English (en)"
  echo "   🇨🇳 简体中文 (zh)"
  echo "   🇪🇸 Español (es)"
  echo "   🇧🇷 Português (pt)"
  echo "   🇫🇷 Français (fr)"
  echo "   🇩🇪 Deutsch (de)"
  exit 0
else
  echo "⚠️  发现 $FAIL 个问题"
  exit 1
fi
