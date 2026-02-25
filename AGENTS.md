# Project Overview

This is an English grammar learning notes project with an automated workflow for generating learning materials using DeepSeek AI.

## Workflow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  生成提示词      │ ──▶ │  DeepSeek API   │ ──▶ │  生成 HTML 页面  │ ──▶ │  同步到 GitHub   │
│  (Generate)     │     │  (DeepSeek AI)  │     │  (Build)        │     │  (Deploy)       │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

1. **Generate Prompts**: 自动生成 24 个提示词文件
2. **DeepSeek API**: 调用 API 自动生成结构化 JSON 内容
3. **Build HTML**: 将 JSON 内容转换为静态 HTML 页面
4. **Deploy**: 将生成的页面同步到 GitHub 仓库

---

## Environment Setup

### Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python 包管理器
- DeepSeek API Key

### Setup Steps

```bash
# 1. 创建虚拟环境
uv venv

# 2. 安装依赖
uv pip install -r requirements.txt

# 3. 设置 API Key
export DEEPSEEK_API_KEY="your-api-key-here"

# 4. 验证设置
make status
```

---

## Project Structure

```
.
├── .venv/                        # Python virtual environment (uv)
├── config/
│   └── grammar_points.json       # 24 grammar points configuration
├── prompts/
│   ├── grammar_point_template.md # Prompt template
│   └── generated/                # Generated prompts (24 files)
│       ├── prompt_01.txt ~ prompt_24.txt
├── content/                      # DeepSeek generated JSON content
│   └── 01.json ~ 24.json
├── templates/
│   └── grammar_page.html         # HTML page template
├── scripts/
│   ├── generate_content.py       # Call DeepSeek API
│   ├── build_html.py             # Build single HTML
│   └── build_all.py              # Batch build
├── docs/                         # Generated static website
│   ├── index.html
│   ├── 01.html ~ 24.html
│   └── assets/
│       ├── css/style.css
│       └── js/main.js
├── requirements.txt              # Python dependencies
├── Makefile                      # Quick commands
├── .env.example                  # Environment template
├── AGENTS.md                     # This file
├── README.md                     # User guide
├── English_Grammar_list.md       # Original grammar list
└── learn_method.md              # Learning methodology
```

---

## Usage Guide

### Quick Commands (Make)

```bash
# View project status
make status

# Generate all content (calls DeepSeek API)
make generate

# Generate single point
make generate ID=05

# Build all HTML pages
make build

# Local preview
make serve
```

### Direct Python Scripts

```bash
# Using uv run (auto-activates venv)

# List all points
uv run python scripts/generate_content.py --list

# Generate single point
uv run python scripts/generate_content.py --single 01

# Generate range
uv run python scripts/generate_content.py --start 01 --end 05

# Build HTML
uv run python scripts/build_html.py content/01.json
uv run python scripts/build_all.py
```

---

## Content Generation (DeepSeek API)

### API Configuration

- **Base URL**: `https://api.deepseek.com`
- **Model**: `deepseek-chat` (or `deepseek-reasoner`)
- **API Key**: Set via `DEEPSEEK_API_KEY` environment variable

### Output Format

Each generated JSON file contains:

```json
{
  "grammar_point": "知识点名称",
  "category": "所属分类",
  "index": 1,
  "content": {
    "overview": {
      "function": "它能做什么？",
      "usage_scenarios": ["场景1", "场景2", "场景3"]
    },
    "rules": {
      "description": "核心规则概述",
      "key_points": [
        {"point": "规则1", "explanation": "详细说明"}
      ]
    },
    "examples": [
      {
        "sentence": "英文例句",
        "translation": "中文翻译",
        "analysis": "语法解析"
      }
    ],
    "exercises": {
      "multiple_choice": [...],
      "fill_blank": [...]
    },
    "summary": "一句话总结",
    "related_points": ["相关1", "相关2", "相关3"]
  }
}
```

---

## 24 Grammar Points

### Simple Sentence Components (14)
1. 名词片语 (Noun Phrases)
2. 代名词 (Pronouns)
3. 形容词 (Adjectives)
4. 副词 (Adverbs)
5. 比较句法 (Comparative Structures)
6. 介系词 (Prepositions)
7. 分词 (Participles)
8. 动词时态 (Verb Tenses)
9. 语态 (Voice)
10. 语气助动词 (Modal Verbs)
11. 语气 (Moods)
12. 动名词 (Gerunds)
13. 不定词片语 (Infinitive Phrases)
14. 对等连接词 (Coordinating Conjunctions)

### Complex Sentence Types (5)
15. 对等子句 (Coordinate Clauses)
16. 名词子句 (Noun Clauses)
17. 副词子句 (Adverbial Clauses)
18. 关系子句 (Relative Clauses)
19. 主词动词一致性 (Subject-Verb Agreement)

### Reduced Sentence Types (5)
20. 倒装句 (Inversion)
21. 简化子句 (Reduced Clauses)
22. 关系子句简化 (Reduced Relative Clauses)
23. 名词子句简化 (Reduced Noun Clauses)
24. 副词子句简化 (Reduced Adverbial Clauses)

---

## Development Conventions

- **Point IDs**: Use two digits (01-24)
- **File Naming**: Lowercase with ID prefix (e.g., `01.json`, `01.html`)
- **JSON Content**: Saved in `content/` directory
- **HTML Output**: Saved in `docs/` directory
- **API Rate Limiting**: Built-in delay between requests (1s)

---

## Technology Stack

- **Python**: 3.13+ (managed by uv)
- **Packages**: openai (for DeepSeek API compatibility)
- **Content Format**: JSON
- **Output**: Static HTML/CSS/JS
- **Deployment**: GitHub Pages

---

## Future Enhancements

- [ ] Add progress tracking UI
- [ ] Implement search functionality
- [ ] Add dark mode
- [ ] Mobile app version
- [ ] Export to PDF/EPUB
- [ ] Add audio pronunciation
