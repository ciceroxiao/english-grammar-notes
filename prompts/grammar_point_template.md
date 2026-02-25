# DeepSeek 提示词模板

## 系统角色设定

```
你是一位专业的英语语法教学专家，擅长用中文清晰讲解英语语法概念。
你的输出将被转换为 HTML 格式，用于构建英语语法学习网站。
```

## 变量说明

- `{{GRAMMAR_POINT}}`：当前要讲解的语法知识点名称（如：名词片语）
- `{{CATEGORY}}`：所属分类（如：简单句的成分）
- `{{INDEX}}`：知识点序号（如：1/26）

## 提示词模板

```markdown
# 英语语法知识点讲解任务

## 当前知识点信息
- 知识点名称：{{GRAMMAR_POINT}}
- 所属分类：{{CATEGORY}}
- 序号：{{INDEX}}

## 输出要求

请严格按照以下 JSON 格式输出（不要包含任何 Markdown 代码块标记外的内容）：

```json
{
  "grammar_point": "{{GRAMMAR_POINT}}",
  "category": "{{CATEGORY}}",
  "index": {{INDEX}},
  "content": {
    "overview": {
      "function": "【它能做什么？】用 2-3 句话说明该语法点的核心功能",
      "usage_scenarios": ["使用场景1", "使用场景2", "使用场景3"]
    },
    "rules": {
      "description": "【核心规则】简明扼要列出 3-5 条核心语法规则",
      "key_points": [
        {"point": "规则要点1", "explanation": "详细说明"},
        {"point": "规则要点2", "explanation": "详细说明"},
        {"point": "规则要点3", "explanation": "详细说明"}
      ]
    },
    "examples": [
      {
        "sentence": "英文例句1",
        "translation": "中文翻译1",
        "analysis": "语法解析：说明该句如何运用此语法点"
      },
      {
        "sentence": "英文例句2",
        "translation": "中文翻译2",
        "analysis": "语法解析"
      },
      {
        "sentence": "英文例句3",
        "translation": "中文翻译3",
        "analysis": "语法解析"
      },
      {
        "sentence": "英文例句4（进阶）",
        "translation": "中文翻译4",
        "analysis": "语法解析"
      },
      {
        "sentence": "英文例句5（易错点）",
        "translation": "中文翻译5",
        "analysis": "语法解析，强调常见错误"
      }
    ],
    "exercises": {
      "multiple_choice": [
        {
          "question": "题目1",
          "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
          "answer": "A",
          "explanation": "解析"
        },
        {
          "question": "题目2",
          "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
          "answer": "B",
          "explanation": "解析"
        },
        {
          "question": "题目3",
          "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
          "answer": "C",
          "explanation": "解析"
        }
      ],
      "fill_blank": [
        {
          "question": "填空题1：用正确的形式填空",
          "answer": "正确答案",
          "explanation": "解析"
        },
        {
          "question": "改写题2：将句子改写为...",
          "answer": "改写后的句子",
          "explanation": "解析"
        }
      ]
    },
    "summary": "【一句话总结】用一句话概括该语法点的核心要义",
    "related_points": ["相关知识点1", "相关知识点2", "相关知识点3"]
  }
}
```

## 内容质量标准

1. **例句质量**：例句要实用、地道，避免过于简单或生僻的表达
2. **解析深度**：不仅说明"是什么"，还要解释"为什么"
3. **难度递进**：例句和练习题应从基础到进阶
4. **常见错误**：至少包含一个易错点的警示

## 特别说明

- 输出必须是合法的 JSON 格式
- 所有字符串值使用双引号
- 不要在 JSON 中使用换行符（\n），如需换行使用 \\n
请开始生成知识点：{{GRAMMAR_POINT}}
```

## 批量处理脚本参考

```python
# generate_prompts.py
# 用于生成所有知识点的提示词文件

GRAMMAR_POINTS = [
    # 简单句的成分（14个）
    {"category": "简单句的成分", "points": [
        "名词片语", "代名词", "形容词", "副词", "比较句法", 
        "介系词", "分词", "动词时态", "语态", "语气助动词", 
        "语气", "动名词", "不定词片语", "对等连接词"
    ]},
    # 复合句的类型（5个）
    {"category": "复合句的类型", "points": [
        "对等子句", "名词子句", "副词子句", "关系子句", "主词动词一致性"
    ]},
    # 简化句的类型（5个）
    {"category": "简化句的类型", "points": [
        "倒装句", "简化子句", "关系子句简化", "名词子句简化", "副词子句简化"
    ]}
]

def generate_prompt(grammar_point, category, index):
    template = open('prompts/grammar_point_template.md').read()
    # 提取提示词部分并替换变量
    # ...
    return prompt_content

# 生成 24 个提示词文件
# 输出到 prompts/generated/ 目录
```
