#!/usr/bin/env python3
"""
SERP 竞品分析工具
分析目标关键词的竞品页面结构、内容策略
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urlparse
from collections import Counter
import time

class SERPAnalyzer:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
    def analyze_page(self, url):
        """分析单个页面"""
        try:
            print(f"\n🔍 分析: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取标题结构
            h1_tags = [h1.get_text().strip() for h1 in soup.find_all('h1')]
            h2_tags = [h2.get_text().strip() for h2 in soup.find_all('h2')]
            h3_tags = [h3.get_text().strip() for h3 in soup.find_all('h3')]
            
            # 提取内容
            text = soup.get_text()
            word_count = len(text.split())
            
            # 提取关键词密度
            keywords = self.extract_keywords(text)
            
            # 提取内链数量
            internal_links = len([a for a in soup.find_all('a', href=True) 
                                if urlparse(a['href']).netloc == '' or 
                                urlparse(url).netloc in urlparse(a['href']).netloc])
            
            # 提取 Schema 标记
            schemas = []
            for script in soup.find_all('script', type='application/ld+json'):
                try:
                    schemas.append(json.loads(script.string))
                except:
                    pass
            
            # 提取 FAQ 数量
            faq_count = len(soup.find_all(['div', 'section'], 
                            class_=re.compile(r'faq|question', re.I)))
            
            return {
                'url': url,
                'title': soup.title.string if soup.title else 'N/A',
                'h1_count': len(h1_tags),
                'h2_count': len(h2_tags),
                'h3_count': len(h3_tags),
                'h1_samples': h1_tags[:3],
                'h2_samples': h2_tags[:5],
                'word_count': word_count,
                'internal_links': internal_links,
                'top_keywords': keywords[:10],
                'schema_types': [s.get('@type') for s in schemas if isinstance(s, dict)],
                'faq_count': faq_count
            }
        except Exception as e:
            print(f"❌ 错误: {str(e)}")
            return None
    
    def extract_keywords(self, text):
        """提取关键词及频率"""
        words = re.findall(r'\b[a-z]{3,}\b', text.lower())
        stopwords = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 
                    'can', 'has', 'had', 'her', 'was', 'one', 'our', 'out', 'this'}
        words = [w for w in words if w not in stopwords]
        return Counter(words).most_common(20)
    
    def compare_competitors(self, urls):
        """对比多个竞品"""
        results = []
        for url in urls:
            result = self.analyze_page(url)
            if result:
                results.append(result)
            time.sleep(2)
        return self.generate_report(results)
    
    def generate_report(self, results):
        """生成对比报告"""
        if not results:
            return "没有成功分析的页面"
        
        report = "# 🔥 SERP 竞品分析报告\n\n"
        report += f"分析时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += f"分析页面数: {len(results)}\n\n"
        
        report += "## 📊 核心指标对比\n\n"
        report += "| 网站 | 字数 | H1 | H2 | H3 | 内链 | FAQ | Schema |\n"
        report += "|------|------|----|----|----|----|-----|--------|\n"
        
        for r in results:
            domain = urlparse(r['url']).netloc
            report += f"| {domain} | {r['word_count']:,} | {r['h1_count']} | {r['h2_count']} | {r['h3_count']} | {r['internal_links']} | {r['faq_count']} | {len(r['schema_types'])} |\n"
        
        avg_words = sum(r['word_count'] for r in results) // len(results)
        avg_h2 = sum(r['h2_count'] for r in results) // len(results)
        report += f"\n**平均值:** 字数 {avg_words:,} | H2 {avg_h2} 个\n\n"
        
        report += "## 📝 内容结构分析\n\n"
        for i, r in enumerate(results, 1):
            report += f"### {i}. {urlparse(r['url']).netloc}\n\n"
            report += f"**标题:** {r['title'][:100]}...\n\n"
            
            if r['h2_samples']:
                report += "**H2 结构样例:**\n"
                for h2 in r['h2_samples'][:5]:
                    report += f"- {h2}\n"
                report += "\n"
            
            if r['schema_types']:
                schema_list = [s for s in r['schema_types'] if s is not None]
                if schema_list:
                    report += f"**Schema 标记:** {', '.join(set(schema_list))}\n\n"
            
            if r['top_keywords']:
                report += "**高频关键词 (Top 5):**\n"
                for kw, count in r['top_keywords'][:5]:
                    report += f"- {kw}: {count} 次\n"
                report += "\n"
        
        report += "## 🎯 我们的机会点\n\n"
        
        max_words = max(r['word_count'] for r in results)
        our_words = 10243
        if our_words < max_words:
            report += f"⚠️ **内容深度不足:** 竞品最高 {max_words:,} 词，我们 {our_words:,} 词\n"
        else:
            report += f"✅ **内容深度优势:** 我们 {our_words:,} 词 > 竞品平均 {avg_words:,} 词\n"
        
        report += "\n## 💡 立即行动建议\n\n"
        report += "1. 补充竞品有而我们缺的内容板块\n"
        report += "2. 增加内链密度和质量\n"
        report += "3. 优化关键词自然出现频率\n"
        report += "4. Schema 标记完善\n"
        report += "5. FAQ 继续扩充\n\n"
        
        return report

def main():
    print("🚀 SERP 竞品分析工具\n" + "=" * 50)
    
    competitors = [
        "https://snaptik.app/",
        "https://ssstik.io/",
        "https://ttdownloader.com/",
        "https://savetik.co/",
        "https://tikmate.app/"
    ]
    
    print(f"\n目标关键词: tiktok video downloader")
    print(f"分析竞品数: {len(competitors)}\n")
    
    analyzer = SERPAnalyzer()
    report = analyzer.compare_competitors(competitors)
    
    report_file = "SERP-ANALYSIS-REPORT.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ 报告已生成: {report_file}")
    print("\n" + "=" * 50)
    print(report)

if __name__ == "__main__":
    main()
