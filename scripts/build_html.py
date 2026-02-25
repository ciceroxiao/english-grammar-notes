#!/usr/bin/env python3
"""
将 DeepSeek 生成的 JSON 内容转换为 HTML 页面
Usage: python scripts/build_html.py <input_json_file>
Example: python scripts/build_html.py content/01_名词片语.json
"""

import json
import re
import sys
from pathlib import Path

# 路径配置
TEMPLATE_PATH = Path("templates/grammar_page.html")
OUTPUT_DIR = Path("docs")
CONFIG_PATH = Path("config/grammar_points.json")


def load_json(file_path: str) -> dict:
    """加载 JSON 文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_template() -> str:
    """加载 HTML 模板"""
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()


def load_config():
    """加载配置获取导航信息"""
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_navigation(config, current_index: int):
    """获取上一页/下一页链接"""
    all_points = []
    for cat in config["categories"]:
        for point in cat["points"]:
            all_points.append({
                "id": point["id"],
                "name": point["name"],
                "category_id": cat["id"]
            })
    
    prev_link = ""
    next_link = ""
    
    # 上一页
    if current_index > 1:
        prev_point = all_points[current_index - 2]
        prev_link = f'<a href="{prev_point["id"]}.html" class="prev">← 上一节：{prev_point["name"]}</a>'
    
    # 下一页
    if current_index < len(all_points):
        next_point = all_points[current_index]
        next_link = f'<a href="{next_point["id"]}.html" class="next">下一节：{next_point["name"]} →</a>'
    
    return prev_link, next_link


def render_usage_scenarios(scenarios: list) -> str:
    """渲染使用场景列表"""
    return "\n".join([f"                    <li>{s}</li>" for s in scenarios])


def render_key_points(points: list) -> str:
    """渲染关键规则点"""
    html = []
    for i, p in enumerate(points, 1):
        html.append(f'<div class="key-point"><h4>{i}. {p["point"]}</h4><p>{p["explanation"]}</p></div>')
    return "\n".join(html)


def render_examples(examples: list) -> str:
    """渲染例句"""
    html = []
    for ex in examples:
        html.append(f'<div class="example-item"><p class="sentence">{ex["sentence"]}</p><p class="translation">{ex["translation"]}</p><p class="analysis">{ex["analysis"]}</p></div>')
    return "\n".join(html)


def render_multiple_choice(questions: list) -> str:
    """渲染选择题"""
    html = []
    for i, q in enumerate(questions, 1):
        options_html = "\n".join([f'<label><input type="radio" name="q{i}" value="{opt[0]}"> {opt}</label>' for opt in q['options']])
        html.append(f'<div class="question" data-answer="{q["answer"]}" data-explanation="{q["explanation"]}"><p class="q-text">{i}. {q["question"]}</p><div class="options">{options_html}</div></div>')
    return "\n".join(html)


def render_fill_blank(questions: list) -> str:
    """渲染填空题"""
    html = []
    for i, q in enumerate(questions, 1):
        html.append(f'<div class="question" data-answer="{q["answer"]}" data-explanation="{q["explanation"]}"><p class="q-text">{i}. {q["question"]}</p><input type="text" class="fill-input" placeholder="请输入答案"></div>')
    return "\n".join(html)


def render_answers(data: dict) -> str:
    """渲染答案部分"""
    html = ["<h3>答案解析</h3>"]
    
    # 选择题答案
    html.append("<h4>选择题</h4>")
    for i, q in enumerate(data['exercises']['multiple_choice'], 1):
        html.append(f"<p><strong>{i}.</strong> 答案：{q['answer']} - {q['explanation']}</p>")
    
    # 填空题答案
    html.append("<h4>填空与改写</h4>")
    for i, q in enumerate(data['exercises']['fill_blank'], 1):
        html.append(f"<p><strong>{i}.</strong> 答案：{q['answer']} - {q['explanation']}</p>")
    
    return "\n".join(html)


def render_related_points(points: list) -> str:
    """渲染相关知识点"""
    return "\n".join([f'<a href="#" class="related-tag">{p}</a>' for p in points])


def build_html(data: dict) -> str:
    """构建 HTML 页面"""
    template = load_template()
    config = load_config()
    
    # 获取导航
    prev_link, next_link = get_navigation(config, data['index'])
    
    # 找到当前分类 ID
    category_id = ""
    for cat in config["categories"]:
        if cat["name"] == data['category']:
            category_id = cat["id"]
            break
    
    # 替换模板变量
    replacements = {
        "{{GRAMMAR_POINT}}": data['grammar_point'],
        "{{CATEGORY}}": data['category'],
        "{{CATEGORY_ID}}": category_id,
        "{{INDEX}}": str(data['index']),
        "{{NAME_EN}}": data.get('name_en', ''),
        "{{OVERVIEW_FUNCTION}}": data['content']['overview']['function'],
        "{{USAGE_SCENARIOS}}": render_usage_scenarios(data['content']['overview']['usage_scenarios']),
        "{{RULES_DESCRIPTION}}": data['content']['rules']['description'],
        "{{KEY_POINTS}}": render_key_points(data['content']['rules']['key_points']),
        "{{EXAMPLES}}": render_examples(data['content']['examples']),
        "{{MULTIPLE_CHOICE}}": render_multiple_choice(data['content']['exercises']['multiple_choice']),
        "{{FILL_BLANK}}": render_fill_blank(data['content']['exercises']['fill_blank']),
        "{{ANSWERS}}": render_answers(data['content']),
        "{{SUMMARY}}": data['content']['summary'],
        "{{RELATED_POINTS}}": render_related_points(data['content']['related_points']),
        "{{PREV_LINK}}": prev_link,
        "{{NEXT_LINK}}": next_link,
    }
    
    html = template
    for key, value in replacements.items():
        html = html.replace(key, value)
    
    return html


def save_html(index: int, content: str):
    """保存 HTML 文件"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"{str(index).zfill(2)}.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"HTML 页面已保存到: {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/build_html.py <input_json_file>")
        print("Example: python scripts/build_html.py content/01_名词片语.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not Path(input_file).exists():
        print(f"错误: 找不到文件 {input_file}")
        sys.exit(1)
    
    # 加载数据
    data = load_json(input_file)
    
    # 构建 HTML
    html = build_html(data)
    
    # 保存
    save_html(data['index'], html)
    
    print(f"\n✅ 成功生成页面: {data['grammar_point']}")


if __name__ == "__main__":
    main()
