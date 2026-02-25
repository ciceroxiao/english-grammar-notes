# Project Overview

This is an English grammar learning notes project with an automated workflow for generating learning materials using DeepSeek AI.

🌐 **Live Site**: https://ciceroxiao.github.io/english-grammar-notes/  
📁 **Repository**: https://github.com/ciceroxiao/english-grammar-notes

---

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
4. **Deploy**: 通过 GitHub Pages 部署网站

---

## Project Status

- ✅ 24 Prompt files generated
- ✅ 24 JSON content files (DeepSeek AI generated)
- ✅ 24 HTML pages built
- ✅ GitHub Pages deployed

---

## Environment Setup

### Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python package manager
- DeepSeek API Key

### Setup Steps

```bash
# 1. Create virtual environment
uv venv

# 2. Install dependencies
uv pip install -r requirements.txt

# 3. Set API Key
export DEEPSEEK_API_KEY="your-api-key-here"

# 4. Verify setup
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
├── docs/                         # Generated static website (GitHub Pages source)
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
| # | Name | Link |
|---|------|------|
| 1 | 名词片语 (Noun Phrases) | [01.html](https://ciceroxiao.github.io/english-grammar-notes/01.html) |
| 2 | 代名词 (Pronouns) | [02.html](https://ciceroxiao.github.io/english-grammar-notes/02.html) |
| 3 | 形容词 (Adjectives) | [03.html](https://ciceroxiao.github.io/english-grammar-notes/03.html) |
| 4 | 副词 (Adverbs) | [04.html](https://ciceroxiao.github.io/english-grammar-notes/04.html) |
| 5 | 比较句法 (Comparative Structures) | [05.html](https://ciceroxiao.github.io/english-grammar-notes/05.html) |
| 6 | 介系词 (Prepositions) | [06.html](https://ciceroxiao.github.io/english-grammar-notes/06.html) |
| 7 | 分词 (Participles) | [07.html](https://ciceroxiao.github.io/english-grammar-notes/07.html) |
| 8 | 动词时态 (Verb Tenses) | [08.html](https://ciceroxiao.github.io/english-grammar-notes/08.html) |
| 9 | 语态 (Voice) | [09.html](https://ciceroxiao.github.io/english-grammar-notes/09.html) |
| 10 | 语气助动词 (Modal Verbs) | [10.html](https://ciceroxiao.github.io/english-grammar-notes/10.html) |
| 11 | 语气 (Moods) | [11.html](https://ciceroxiao.github.io/english-grammar-notes/11.html) |
| 12 | 动名词 (Gerunds) | [12.html](https://ciceroxiao.github.io/english-grammar-notes/12.html) |
| 13 | 不定词片语 (Infinitive Phrases) | [13.html](https://ciceroxiao.github.io/english-grammar-notes/13.html) |
| 14 | 对等连接词 (Coordinating Conjunctions) | [14.html](https://ciceroxiao.github.io/english-grammar-notes/14.html) |

### Complex Sentence Types (5)
| # | Name | Link |
|---|------|------|
| 15 | 对等子句 (Coordinate Clauses) | [15.html](https://ciceroxiao.github.io/english-grammar-notes/15.html) |
| 16 | 名词子句 (Noun Clauses) | [16.html](https://ciceroxiao.github.io/english-grammar-notes/16.html) |
| 17 | 副词子句 (Adverbial Clauses) | [17.html](https://ciceroxiao.github.io/english-grammar-notes/17.html) |
| 18 | 关系子句 (Relative Clauses) | [18.html](https://ciceroxiao.github.io/english-grammar-notes/18.html) |
| 19 | 主词动词一致性 (Subject-Verb Agreement) | [19.html](https://ciceroxiao.github.io/english-grammar-notes/19.html) |

### Reduced Sentence Types (5)
| # | Name | Link |
|---|------|------|
| 20 | 倒装句 (Inversion) | [20.html](https://ciceroxiao.github.io/english-grammar-notes/20.html) |
| 21 | 简化子句 (Reduced Clauses) | [21.html](https://ciceroxiao.github.io/english-grammar-notes/21.html) |
| 22 | 关系子句简化 (Reduced Relative Clauses) | [22.html](https://ciceroxiao.github.io/english-grammar-notes/22.html) |
| 23 | 名词子句简化 (Reduced Noun Clauses) | [23.html](https://ciceroxiao.github.io/english-grammar-notes/23.html) |
| 24 | 副词子句简化 (Reduced Adverbial Clauses) | [24.html](https://ciceroxiao.github.io/english-grammar-notes/24.html) |

---

## Development Conventions

- **Point IDs**: Use two digits (01-24)
- **File Naming**: Lowercase with ID prefix (e.g., `01.json`, `01.html`)
- **JSON Content**: Saved in `content/` directory
- **HTML Output**: Saved in `docs/` directory (GitHub Pages source)
- **API Rate Limiting**: Built-in delay between requests (1s)

---

## Technology Stack

- **Python**: 3.13+ (managed by uv)
- **Packages**: openai (for DeepSeek API compatibility)
- **Content Format**: JSON
- **Output**: Static HTML/CSS/JS
- **Deployment**: GitHub Pages

---

## Deployment

The site is deployed via GitHub Pages:

```bash
# Push to GitHub to deploy automatically
git add .
git commit -m "Update content"
git push origin master
```

Site will be available at: https://ciceroxiao.github.io/english-grammar-notes/

---

## Future Enhancements

- [ ] Add progress tracking UI
- [ ] Implement search functionality
- [ ] Add dark mode
- [ ] Mobile app version
- [ ] Export to PDF/EPUB
- [ ] Add audio pronunciation
