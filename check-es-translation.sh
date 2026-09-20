#!/bin/bash

echo "=== 检查西班牙语翻译质量 ==="
echo ""

# 检查所有西班牙语 HTML 文件
ES_FILES=(
  "frontend/es/index.html"
  "frontend/es/mp3.html"
  "frontend/es/miniatura.html"
  "frontend/es/historia.html"
  "frontend/es/pages/contacto.html"
  "frontend/es/pages/cookies.html"
  "frontend/es/pages/descargo.html"
  "frontend/es/pages/dmca.html"
  "frontend/es/pages/privacidad.html"
  "frontend/es/pages/terminos.html"
)

echo "1. 检查 Schema.org 英文残留..."
for file in "${ES_FILES[@]}"; do
  if [ -f "$file" ]; then
    # 检查 JSON-LD 中是否有英文（排除常见的技术词汇）
    english_in_schema=$(grep -o '"text":\s*"[^"]*\b(the|and|or|is|are|for|with|without|how|can|do|does)\b[^"]*"' "$file" | head -5)
    if [ ! -z "$english_in_schema" ]; then
      echo "  ⚠️ $file - 发现英文 Schema 数据"
    fi
  fi
done

echo ""
echo "2. 检查 meta 标签翻译..."
for file in "${ES_FILES[@]}"; do
  if [ -f "$file" ]; then
    # 检查关键 meta 标签
    has_es_desc=$(grep '<meta name="description"' "$file" | grep -i "descarga\|gratis\|rápido" | wc -l)
    if [ "$has_es_desc" -eq 0 ]; then
      echo "  ⚠️ $file - description meta 标签可能未翻译"
    fi
  fi
done

echo ""
echo "3. 检查 hreflang 标签..."
for file in "${ES_FILES[@]}"; do
  if [ -f "$file" ]; then
    has_hreflang=$(grep 'hreflang="es"' "$file" | wc -l)
    if [ "$has_hreflang" -eq 0 ]; then
      echo "  ⚠️ $file - 缺少 hreflang 标签"
    fi
  fi
done

echo ""
echo "4. 检查语言属性..."
