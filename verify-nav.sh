#!/bin/bash
# 验证所有语言版本的导航栏

echo "🧪 验证所有语言版本的导航栏..."
echo ""

PASSED=0
FAILED=0

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

cd frontend

echo "🇨🇳 检查中文导航栏..."
if grep -q '视频</a>' zh/index.html && \
   grep -q '音频</a>' zh/yinpin.html && \
   grep -q '封面</a>' zh/fengmian.html && \
   grep -q '快拍</a>' zh/kuaipai.html; then
    echo -e "${GREEN}✓${NC} 中文导航栏正确"
    ((PASSED++))
else
    echo -e "${RED}✗${NC} 中文导航栏有问题"
    ((FAILED++))
fi

echo "🇪🇸 检查西班牙语导航栏..."
if grep -q '>Video</a>' es/index.html && \
   grep -q '>MP3</a>' es/mp3.html && \
   grep -q '>Miniatura</a>' es/miniatura.html && \
   grep -q '>Historia</a>' es/historia.html; then
    echo -e "${GREEN}✓${NC} 西班牙语导航栏正确"
    ((PASSED++))
else
    echo -e "${RED}✗${NC} 西班牙语导航栏有问题"
    ((FAILED++))
fi

echo "🇧🇷 检查葡萄牙语导航栏..."
if grep -q '>Vídeo</a>' pt/index.html && \
   grep -q '>MP3</a>' pt/mp3.html && \
   grep -q '>Miniatura</a>' pt/miniatura.html && \
   grep -q '>História</a>' pt/historia.html; then
    echo -e "${GREEN}✓${NC} 葡萄牙语导航栏正确"
    ((PASSED++))
else
    echo -e "${RED}✗${NC} 葡萄牙语导航栏有问题"
    ((FAILED++))
fi

echo "🇫🇷 检查法语导航栏..."
if grep -q '>Vidéo</a>' fr/index.html && \
   grep -q '>MP3</a>' fr/mp3.html && \
   grep -q '>Miniature</a>' fr/miniatura.html && \
   grep -q '>Histoire</a>' fr/historia.html; then
    echo -e "${GREEN}✓${NC} 法语导航栏正确"
    ((PASSED++))
else
    echo -e "${RED}✗${NC} 法语导航栏有问题"
    ((FAILED++))
fi

echo "🇩🇪 检查德语导航栏..."
if grep -q '>Video</a>' de/index.html && \
   grep -q '>MP3</a>' de/mp3.html && \
   grep -q '>Miniatur</a>' de/miniatur.html && \
   grep -q '>Story</a>' de/story.html; then
    echo -e "${GREEN}✓${NC} 德语导航栏正确"
    ((PASSED++))
else
    echo -e "${RED}✗${NC} 德语导航栏有问题"
    ((FAILED++))
fi

echo ""
echo "🌐 检查语言切换器配置..."

# 检查是否所有语言都有完整的 6 个语言选项
for lang in zh es pt fr de; do
    langCount=$(grep -o 'data-lang=' "$lang/index.html" | wc -l)
    if [ "$langCount" -ge 6 ]; then
        echo -e "${GREEN}✓${NC} $lang 语言切换器有 $langCount 个选项"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $lang 语言切换器只有 $langCount 个选项（应该 >= 6）"
        ((FAILED++))
    fi
done

echo ""
echo "❌ 检查 data-i18n 残留..."
dataI18nCount=$(grep -r 'data-i18n=' */index.html */*.html 2>/dev/null | grep -v "index-before" | wc -l)
if [ "$dataI18nCount" -eq 0 ]; then
    echo -e "${GREEN}✓${NC} 没有 data-i18n 残留"
    ((PASSED++))
else
    echo -e "${RED}✗${NC} 还有 $dataI18nCount 处 data-i18n 残留"
    ((FAILED++))
fi

echo ""
echo "═══════════════════════════════════════"
echo -e "${GREEN}通过: $PASSED${NC}"
echo -e "${RED}失败: $FAILED${NC}"
echo "═══════════════════════════════════════"

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 所有导航栏验证通过！${NC}"
    exit 0
else
    echo -e "${RED}⚠️  发现 $FAILED 个问题${NC}"
    exit 1
fi
