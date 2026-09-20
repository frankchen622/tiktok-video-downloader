#!/bin/bash
# 批量翻译所有葡萄牙语页面

PT_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/pt"

# 复制西班牙语页面作为基础
echo "复制西班牙语页面作为基础..."
cp /root/.openclaw/workspace/tiktok-video-downloader/frontend/es/mp3.html $PT_DIR/
cp /root/.openclaw/workspace/tiktok-video-downloader/frontend/es/miniatura.html $PT_DIR/
cp /root/.openclaw/workspace/tiktok-video-downloader/frontend/es/historia.html $PT_DIR/

# 复制法律页面
cp -r /root/.openclaw/workspace/tiktok-video-downloader/frontend/es/pages/* $PT_DIR/pages/

echo "开始批量翻译..."

# 定义翻译函数
translate_file() {
    local file="$1"
    echo "翻译: $file"
    
    # 基础替换
    sed -i 's/lang="es"/lang="pt"/g' "$file"
    sed -i 's|/es/|/pt/|g' "$file"
    sed -i 's|/es"|/pt"|g' "$file"
    sed -i 's|href="https://dltk.io/es|href="https://dltk.io/pt|g' "$file"
    
    # 西班牙语到葡萄牙语通用词汇
    sed -i 's/Descargar/Baixar/g' "$file"
    sed -i 's/Descarga/Baixe/g' "$file"  
    sed -i 's/descarga/baixe/g' "$file"
    sed -i 's/descargar/baixar/g' "$file"
    sed -i 's/Gratis/Grátis/g' "$file"
    sed -i 's/gratis/grátis/g' "$file"
    sed -i 's/Rápido/Rápido/g' "$file"
    sed -i 's/Sin/Sem/g' "$file"
    sed -i 's/ sin / sem /g' "$file"
    sed -i 's/Calidad/Qualidade/g' "$file"
    sed -i 's/calidad/qualidade/g' "$file"
    sed -i 's/Video/Vídeo/g' "$file"
    sed -i 's/video/vídeo/g' "$file"
    sed -i 's/Audio/Áudio/g' "$file"
    sed -i 's/audio/áudio/g' "$file"
    sed -i 's/Convertir/Converter/g' "$file"
    sed -i 's/Convierte/Converta/g' "$file"
    sed -i 's/convertir/converter/g' "$file"
    sed -i 's/Guardar/Salvar/g' "$file"
    sed -i 's/Guarda/Salve/g' "$file"
    sed -i 's/guardar/salvar/g' "$file"
    sed -i 's/Historia/Story/g' "$file"
    sed -i 's/historia/story/g' "$file"
    sed -i 's/Miniatura/Miniatura/g' "$file"
    sed -i 's/miniatura/miniatura/g' "$file"
    sed -i 's/Marca de Agua/Marca d'\''Água/g' "$file"
    sed -i 's/marca de agua/marca d'\''água/g' "$file"
    
    # 常见短语
    sed -i 's/¿Cómo/Como/g' "$file"
    sed -i 's/¿Por qué/Por que/g' "$file"
    sed -i 's/¿Puedo/Posso/g' "$file"
    sed -i 's/¿Es/É/g' "$file"
    sed -i 's/Sí,/Sim,/g' "$file"
    sed -i 's/No,/Não,/g' "$file"
    sed -i 's/ es / é /g' "$file"
    sed -i 's/ son / são /g' "$file"
    sed -i 's/ tiene / tem /g' "$file"
    sed -i 's/ tienen / têm /g' "$file"
    sed -i 's/Abre/Abra/g' "$file"
    sed -i 's/Copia/Copie/g' "$file"
    sed -i 's/Pega/Cole/g' "$file"
    sed -i 's/Haz clic/Clique/g' "$file"
    sed -i 's/haz clic/clique/g' "$file"
    sed -i 's/Selecciona/Selecione/g' "$file"
    sed -i 's/selecciona/selecione/g' "$file"
    sed -i 's/Enlace/Link/g' "$file"
    sed -i 's/enlace/link/g' "$file"
    sed -i 's/aplicación/aplicativo/g' "$file"
    sed -i 's/Aplicación/Aplicativo/g' "$file"
    sed -i 's/teléfono/celular/g' "$file"
    sed -i 's/Teléfono/Celular/g' "$file"
    sed -i 's/ordenador/computador/g' "$file"
    sed -i 's/Ordenador/Computador/g' "$file"
    sed -i 's/registro/cadastro/g' "$file"
    sed -i 's/Registro/Cadastro/g' "$file"
    sed -i 's/Iniciar sesión/Fazer login/g' "$file"
    sed -i 's/iniciar sesión/fazer login/g' "$file"
    sed -i 's/Cuenta/Conta/g' "$file"
    sed -i 's/cuenta/conta/g' "$file"
    sed -i 's/completamente/completamente/g' "$file"
    sed -i 's/automáticamente/automaticamente/g' "$file"
    sed -i 's/fácilmente/facilmente/g' "$file"
    sed -i 's/rápidamente/rapidamente/g' "$file"
    sed -i 's/perfectamente/perfeitamente/g' "$file"
    
    # 疑问词
    sed -i 's/Qué/Que/g' "$file"
    sed -i 's/Cuál/Qual/g' "$file"
    sed -i 's/Cuáles/Quais/g' "$file"
    sed -i 's/Cuándo/Quando/g' "$file"
    sed -i 's/Dónde/Onde/g' "$file"
    
    # hreflang 更新
    sed -i 's/hreflang="es"/hreflang="pt"/g' "$file"
}

# 翻译所有页面
for file in $PT_DIR/*.html; do
    translate_file "$file"
done

for file in $PT_DIR/pages/*.html; do
    translate_file "$file"
done

echo "✅ 所有页面批量翻译完成！"
