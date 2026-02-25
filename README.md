# 英语语法精讲

基于"系统调用学习法"的英语语法学习项目，使用 DeepSeek AI 自动生成结构化内容，构建为静态网站。

## 学习理念

采用三步学习法：
1. **它能做什么？** —— 理解语法功能
2. **它是如何实现的？** —— 掌握语法规则
3. **能不能自己编写一个？** —— 通过练习巩固

## 知识点列表（共24个）

### 简单句的成分（14个）
1. 名词片语
2. 代名词
3. 形容词
4. 副词
5. 比较句法
6. 介系词
7. 分词
8. 动词时态
9. 语态
10. 语气助动词
11. 语气
12. 动名词
13. 不定词片语
14. 对等连接词

### 复合句的类型（5个）
15. 对等子句
16. 名词子句
17. 副词子句
18. 关系子句
19. 主词动词一致性

### 简化句的类型（5个）
20. 倒装句
21. 简化子句
22. 关系子句简化
23. 名词子句简化
24. 副词子句简化

---

## 快速开始

### 1. 环境准备

项目使用 [uv](https://github.com/astral-sh/uv) 管理 Python 虚拟环境和依赖：

```bash
# 创建虚拟环境
uv venv

# 安装依赖
uv pip install -r requirements.txt
```

### 2. 配置 API Key

```bash
# 设置 DeepSeek API Key
export DEEPSEEK_API_KEY="your-api-key-here"

# 或者复制 .env.example 为 .env 并填写（需要 source .env）
cp .env.example .env
```

### 3. 生成所有内容

```bash
# 查看项目状态
make status

# 生成所有知识点内容（调用 DeepSeek API，可能需要较长时间）
make generate

# 或生成单个知识点
make generate ID=05
```

### 4. 构建网站

```bash
# 构建所有 HTML 页面
make build

# 强制重新构建
make build-force
```

### 5. 本地预览

```bash
make serve
```

访问 http://localhost:8000

---

## 完整工作流程

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   生成提示词  │ ──▶ │ DeepSeek API│ ──▶ │  JSON 内容   │ ──▶ │  HTML 页面   │
│  (自动生成)  │     │  (AI 生成)   │     │ (结构化数据) │     │  (静态网站)  │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
     prompts/              API              content/              docs/
   generated/*.txt        调用              *.json              *.html
```

---

## 命令参考

| 命令 | 说明 |
|------|------|
| `make help` | 显示帮助 |
| `make install` | 安装依赖 |
| `make list` | 列出所有知识点及状态 |
| `make status` | 查看项目整体状态 |
| `make generate` | 生成所有内容（调用 API） |
| `make generate ID=05` | 生成单个知识点 |
| `make build` | 构建所有 HTML |
| `make build-force` | 强制重新构建 |
| `make serve` | 启动本地服务器 |
| `make clean` | 清理生成的文件 |

---

## 项目结构

```
.
├── .venv/                       # Python 虚拟环境
├── config/
│   └── grammar_points.json      # 24个知识点配置
├── prompts/
│   ├── grammar_point_template.md # 提示词模板
│   └── generated/               # 生成的提示词文件
│       └── prompt_01.txt ~ prompt_24.txt
├── content/                     # DeepSeek 生成的 JSON 内容
│   └── 01.json ~ 24.json
├── templates/
│   └── grammar_page.html        # HTML 页面模板
├── scripts/
│   ├── generate_content.py      # 调用 DeepSeek API
│   ├── build_html.py            # 构建单个 HTML
│   └── build_all.py             # 批量构建
├── docs/                        # 生成的静态网站
│   ├── index.html
│   ├── 01.html ~ 24.html
│   └── assets/
│       ├── css/style.css
│       └── js/main.js
├── requirements.txt             # Python 依赖
├── Makefile                     # 快捷命令
├── .env.example                 # 环境变量模板
├── AGENTS.md                    # 项目文档
└── README.md                    # 本文件
```

---

## 手动操作

如果你不想使用 Makefile，可以直接使用 Python 脚本：

```bash
# 使用 uv run 自动激活虚拟环境

# 生成内容
uv run python scripts/generate_content.py --list
uv run python scripts/generate_content.py --single 01
uv run python scripts/generate_content.py --start 01 --end 24

# 构建 HTML
uv run python scripts/build_html.py content/01.json
uv run python scripts/build_all.py
```

---

## 部署到 GitHub Pages

```bash
cd docs
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/english-grammar.git
git push -u origin main
```

然后在 GitHub 仓库设置中启用 GitHub Pages。

---

## 注意事项

1. **API 费用**：调用 DeepSeek API 会产生费用，请确保账户有足够余额
2. **生成时间**：生成 24 个知识点可能需要 10-30 分钟，建议分批生成
3. **API 限制**：注意 API 的速率限制，程序已内置延迟

## 贡献

欢迎提交 Issue 或 Pull Request 来改进内容或功能。
