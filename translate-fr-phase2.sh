#!/bin/bash
# 法语翻译 Phase 2: 短语和句子

FR_DIR="/root/.openclaw/workspace/tiktok-video-downloader/frontend/fr"

for file in "$FR_DIR"/*.html "$FR_DIR"/pages/*.html; do
    echo "Phase 2: $file"
    
    # 常见短语
    sed -i 's/Você pode/Vous pouvez/g' "$file"
    sed -i 's/você pode/vous pouvez/g' "$file"
    sed -i 's/Posso/Puis-je/g' "$file"
    sed -i 's/posso/puis-je/g' "$file"
    
    # 疑问词
    sed -i 's/Como faço para/Comment/g' "$file"
    sed -i 's/Como/Comment/g' "$file"
    sed -i 's/Por que/Pourquoi/g' "$file"
    sed -i 's/O que/Quoi/g' "$file"
    sed -i 's/Quando/Quand/g' "$file"
    sed -i 's/Onde/Où/g' "$file"
    sed -i 's/Qual/Quel/g' "$file"
    
    # 是/否
    sed -i 's/\bSim\b/Oui/g' "$file"
    sed -i 's/\bsim\b/oui/g' "$file"
    sed -i 's/\bNão\b/Non/g' "$file"
    sed -i 's/\bnão\b/non/g' "$file"
    
    # 设备
    sed -i 's/celular/mobile/g' "$file"
    sed -i 's/Celular/Mobile/g' "$file"
    sed -i 's/celulares/mobiles/g' "$file"
    sed -i 's/aplicativo/application/g' "$file"
    sed -i 's/Aplicativo/Application/g' "$file"
    sed -i 's/aplicativos/applications/g' "$file"
    sed -i 's/navegador/navigateur/g' "$file"
    sed -i 's/Navegador/Navigateur/g' "$file"
    sed -i 's/dispositivo/appareil/g' "$file"
    sed -i 's/Dispositivo/Appareil/g' "$file"
    sed -i 's/dispositivos/appareils/g' "$file"
    
    # 其他常用词
    sed -i 's/cadastro/inscription/g' "$file"
    sed -i 's/Cadastro/Inscription/g' "$file"
    sed -i 's/conta/compte/g' "$file"
    sed -i 's/Conta/Compte/g' "$file"
    sed -i 's/senha/mot de passe/g' "$file"
    sed -i 's/Senha/Mot de passe/g' "$file"
    sed -i 's/login/connexion/g' "$file"
    sed -i 's/Login/Connexion/g' "$file"
    
    # 时间
    sed -i 's/segundos/secondes/g' "$file"
    sed -i 's/minutos/minutes/g' "$file"
    sed -i 's/horas/heures/g' "$file"
    sed -i 's/dias/jours/g' "$file"
    sed -i 's/instantaneamente/instantanément/g' "$file"
    sed -i 's/rapidamente/rapidement/g' "$file"
    
    # 特定短语
    sed -i 's/Todos os/Tous les/g' "$file"
    sed -i 's/todos os/tous les/g' "$file"
    sed -i 's/Todas as/Toutes les/g' "$file"
    sed -i 's/todas as/toutes les/g' "$file"
    
    sed -i 's/mais de/plus de/g' "$file"
    sed -i 's/Mais de/Plus de/g' "$file"
    sed -i 's/menos de/moins de/g' "$file"
    sed -i 's/Menos de/Moins de/g' "$file"
    
    sed -i 's/Perguntas Frequentes/Questions Fréquentes/g' "$file"
    sed -i 's/Contato/Contact/g' "$file"
    sed -i 's/Privacidade/Confidentialité/g' "$file"
    sed -i 's/Termos/Conditions/g' "$file"
    sed -i 's/Política de/Politique de/g' "$file"
    sed -i 's/Aviso Legal/Avertissement Légal/g' "$file"
    sed -i 's/Cookies/Cookies/g' "$file"  # 保持不变
    
done

echo "✅ Phase 2 完成：短语翻译"
