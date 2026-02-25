#!/usr/bin/env python3
"""
批量生成所有知识点的提示词
Usage: python scripts/batch_generate.py
"""

import json
import sys
from pathlib import Path

CONFIG_PATH = Path("config/grammar_points.json")
OUTPUT_DIR = Path("prompts/generated")

PROMPT_TEMPLATE = """你是一位专业的英语语法教学专家，擅长用中文清晰讲解英语语法概念。

## 当前知识点信息
- 知识点名称：{grammar_point}
- 所属分类：{category}
- 序号：{index}/24

## 任务要求

请严格按照以下 JSON 格式输出（不要包含任何 Markdown 代码块标记外的解释性文字）：

{{
  "grammar_point": "{grammar_point}",
  "category": "{category}",
  "index": {index},
  "content": {{
    "overview": {{
      "function": "【它能做什么？】用 2-3 句话说明该语法点的核心功能",
      "usage_scenarios": ["使用场景1", "使用场景2", "使用场景3"]
    }},
    "rules": {{
      "description": "【核心规则】简明扼要列出 3-5 条核心语法规则",
      "key_points": [
        {{"point": "规则要点1", "explanation": "详细说明"}},
        {{"point": "规则要点2", "explanation": "详细说明"}},
        {{"point": "规则要点3", "explanation": "详细说明"}}
      ]
    }},
    "examples": [
      {{
        "sentence": "英文例句1",
        "translation": "中文翻译1",
        "analysis": "语法解析：说明该句如何运用此语法点"
      }},
      {{
        "sentence": "英文例句2",
        "translation": "中文翻译2",
        "analysis": "语法解析"
      }},
      {{
        "sentence": "英文例句3",
        "translation": "中文翻译3",
        "analysis": "语法解析"
      }},
      {{
        "sentence": "英文例句4（进阶）",
        "translation": "中文翻译4",
        "analysis": "语法解析"
      }},
      {{
        "sentence": "英文例句5（易错点）",
        "translation": "中文翻译5",
        "analysis": "语法解析，强调常见错误"
      }}
    ],
    "exercises": {{
      "multiple_choice": [
        {{
          "question": "题目1",
          "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
          "answer": "A",
          "explanation": "解析"
        }},
        {{
          "question": "题目2",
          "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
          "answer": "B",
          "explanation": "解析"
        }},
        {{
          "question": "题目3",
          "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
          "answer": "C",
          "explanation": "解析"
        }}
      ],
      "fill_blank": [
        {{
          "question": "填空题1：用正确的形式填空",
          "answer": "正确答案",
          "explanation": "解析"
        }},
        {{
          "question": "改写题2：将句子改写为...",
          "answer": "改写后的句子",
          "explanation": "解析"
        }}
      ]
    }},
    "summary": "【一句话总结】用一句话概括该语法点的核心要义",
    "related_points": ["相关知识点1", "相关知识点2", "相关知识点3"]
  }}
}}

## 内容质量标准

1. **例句质量**：例句要实用、地道，避免过于简单或生僻的表达
2. **解析深度**：不仅说明\"是什么\"，还要解释\"为什么\"
3. **难度递进**：例句和练习题应从基础到进阶
4. **常见错误**：至少包含一个易错点的警示

## 输出格式要求

- 输出必须是合法的 JSON 格式
- 所有字符串值使用双引号
- 不要在 JSON 字符串中使用原始换行符，如需换行使用 \\\\n
请开始生成知识点：{grammar_point}
"""


def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_prompt(point_id: str, content: str):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"prompt_{point_id}.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ 已生成: prompts/generated/prompt_{point_id}.txt")


def main():
    config = load_config()
    
    print("开始批量生成提示词...\n")
    
    total = 0
    for cat in config["categories"]:
        print(f"【{cat['name']}】")
        for point in cat["points"]:
            point_info = {
                "category": cat["name"],
                "index": int(point["id"]),
                "grammar_point": point["name"],
            }
            
            prompt = PROMPT_TEMPLATE.format(**point_info)
            save_prompt(point["id"], prompt)
            total += 1
        print()
    
    print(f"✅ 共生成 {total} 个提示词文件")
    print(f"📁 保存位置: prompts/generated/")


if __name__ == "__main__":
    main()
