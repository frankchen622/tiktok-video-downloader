#!/bin/bash

# 中文站URL验证脚本
# 用于检查所有中文页面是否能正常访问

echo "🧪 开始验证中文站URL..."
echo "================================"

# 基础URL（本地测试用localhost，生产用dltk.io）
BASE_URL="${1:-http://localhost:8000}"

# 定义所有需要测试的URL
urls=(
  "/zh"
  "/zh/yinpin"
  "/zh/fengmian"
  "/zh/kuaipai"
  "/zh/lianxi"
  "/zh/yinsi"
  "/zh/tiaokuan"
  "/zh/mianze"
  "/zh/banquan"
  "/zh/cookie"
)

# 计数器
total=${#urls[@]}
passed=0
failed=0

# 遍历测试每个URL
for url in "${urls[@]}"; do
  full_url="${BASE_URL}${url}"
  
  # 发送HTTP请求
  status_code=$(curl -s -o /dev/null -w "%{http_code}" "$full_url")
  
  if [ "$status_code" == "200" ]; then
    echo "✅ $url - OK (200)"
    ((passed++))
  else
    echo "❌ $url - FAILED ($status_code)"
    ((failed++))
  fi
done

echo "================================"
echo "📊 测试结果："
echo "   总计: $total"
echo "   通过: $passed"
echo "   失败: $failed"

if [ $failed -eq 0 ]; then
  echo "🎉 所有测试通过！"
  exit 0
else
  echo "⚠️  部分测试失败，请检查"
  exit 1
fi