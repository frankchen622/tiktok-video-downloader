#!/bin/bash
# 多语言切换功能测试脚本

echo "🧪 开始测试多语言切换功能..."
echo ""

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 测试计数
PASSED=0
FAILED=0

# 检查文件是否存在
check_file() {
    local file=$1
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} 文件存在: $file"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}✗${NC} 文件缺失: $file"
        ((FAILED++))
        return 1
    fi
}

# 检查文件中是否包含指定内容
check_content() {
    local file=$1
    local search=$2
    local description=$3
    
    if grep -q "$search" "$file" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} $description: $file"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}✗${NC} $description: $file"
        ((FAILED++))
        return 1
    fi
}

cd "$(dirname "$0")/frontend"

echo "📁 检查核心文件..."
check_file "static/lang-switcher.js"
check_file "static/lang-switcher.css"
echo ""

echo "📄 检查主要页面..."
for lang in "" "zh" "es" "pt" "fr" "de"; do
    if [ -z "$lang" ]; then
        check_file "index.html"
    else
        check_file "$lang/index.html"
    fi
done
echo ""

echo "🔍 检查 JS 引用..."
# 检查是否所有文件都引用了正确的 JS
check_content "index.html" "lang-switcher.js" "英文首页引用正确"
check_content "zh/index.html" "lang-switcher.js" "中文首页引用正确"
check_content "es/index.html" "lang-switcher.js" "西语首页引用正确"
check_content "pt/index.html" "lang-switcher.js" "葡语首页引用正确"
check_content "fr/index.html" "lang-switcher.js" "法语首页引用正确"
check_content "de/index.html" "lang-switcher.js" "德语首页引用正确"
echo ""

echo "❌ 检查旧文件残留..."
OLD_JS_COUNT=$(find . -name "*.html" -type f -exec grep -l "lang-simple.js" {} \; 2>/dev/null | wc -l)
if [ "$OLD_JS_COUNT" -eq 0 ]; then
    echo -e "${GREEN}✓${NC} 没有文件引用旧的 lang-simple.js"
    ((PASSED++))
else
    echo -e "${RED}✗${NC} 还有 $OLD_JS_COUNT 个文件引用旧的 lang-simple.js"
    find . -name "*.html" -type f -exec grep -l "lang-simple.js" {} \; 2>/dev/null | head -5
    ((FAILED++))
fi
echo ""

echo "🌐 检查语言按钮配置..."
check_content "index.html" 'onclick="switchLanguage' "语言切换函数已配置"
check_content "index.html" 'data-lang="en"' "英语按钮配置正确"
check_content "index.html" 'data-lang="zh"' "中文按钮配置正确"
check_content "index.html" 'data-lang="es"' "西语按钮配置正确"
check_content "index.html" 'data-lang="pt"' "葡语按钮配置正确"
check_content "index.html" 'data-lang="fr"' "法语按钮配置正确"
check_content "index.html" 'data-lang="de"' "德语按钮配置正确"
echo ""

echo "📊 检查 JS 文件内容..."
check_content "static/lang-switcher.js" "window.switchLanguage" "switchLanguage 函数已定义"
check_content "static/lang-switcher.js" "getCurrentLanguage" "getCurrentLanguage 函数已定义"
check_content "static/lang-switcher.js" "getPageType" "getPageType 函数已定义"
check_content "static/lang-switcher.js" "pageNames" "页面名称映射已定义"
echo ""

echo "🎨 检查 CSS 样式..."
check_content "static/lang-switcher.css" ".lang-btn.active" "active 样式已定义"
check_content "static/lang-switcher.css" ".lang-dropdown" "下拉菜单样式已定义"
echo ""

echo "═══════════════════════════════════════"
echo "测试完成！"
echo -e "${GREEN}通过: $PASSED${NC}"
echo -e "${RED}失败: $FAILED${NC}"
echo "═══════════════════════════════════════"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 所有测试通过！多语言切换功能修复完成。${NC}"
    echo ""
    echo "📝 下一步："
    echo "1. 推送代码到生产环境"
    echo "2. 在浏览器中访问 https://dltk.io 进行实际测试"
    echo "3. 测试所有语言和页面类型的切换"
    exit 0
else
    echo -e "${RED}⚠️  发现 $FAILED 个问题，请检查后重试。${NC}"
    exit 1
fi
