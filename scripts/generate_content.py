#!/usr/bin/env python3
"""
调用 DeepSeek API 生成所有知识点的内容
Usage: uv run python scripts/generate_content.py [--start 01] [--end 24] [--single 05]

环境变量:
    DEEPSEEK_API_KEY: DeepSeek API 密钥
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

# DeepSeek API 配置
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
MODEL = "deepseek-chat"  # 或 "deepseek-reasoner"

# 路径配置
PROMPTS_DIR = Path("prompts/generated")
CONTENT_DIR = Path("content")
CONFIG_PATH = Path("config/grammar_points.json")


def load_config():
    """加载知识点配置"""
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_point_info(config, point_id: str):
    """根据 ID 获取知识点信息"""
    for cat in config["categories"]:
        for point in cat["points"]:
            if point["id"] == point_id:
                return {
                    "id": point["id"],
                    "name": point["name"],
                    "category": cat["name"]
                }
    return None


def load_prompt(point_id: str) -> str:
    """加载提示词文件"""
    prompt_file = PROMPTS_DIR / f"prompt_{point_id}.txt"
    if not prompt_file.exists():
        raise FileNotFoundError(f"提示词文件不存在: {prompt_file}")
    
    with open(prompt_file, 'r', encoding='utf-8') as f:
        return f.read()


def call_deepseek_api(prompt: str) -> str:
    """调用 DeepSeek API"""
    from openai import OpenAI
    
    if not DEEPSEEK_API_KEY:
        raise ValueError("未设置 DEEPSEEK_API_KEY 环境变量")
    
    client = OpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL
    )
    
    print("  正在调用 DeepSeek API...")
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "你是一位专业的英语语法教学专家，擅长用中文清晰讲解英语语法概念。请严格按照用户要求的 JSON 格式输出。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=4000,
        stream=False
    )
    
    return response.choices[0].message.content


def extract_json(content: str) -> dict:
    """从 API 响应中提取 JSON"""
    # 尝试直接解析
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        pass
    
    # 尝试从 Markdown 代码块中提取
    import re
    
    # 匹配 ```json ... ``` 或 ``` ... ```
    patterns = [
        r'```json\s*(.*?)\s*```',
        r'```\s*(.*?)\s*```',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                continue
    
    raise ValueError("无法从响应中提取有效的 JSON")


def save_content(point_id: str, data: dict):
    """保存生成的内容"""
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = CONTENT_DIR / f"{point_id}.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"  ✓ 已保存: {output_file}")


def generate_single(point_id: str, config: dict, delay: float = 1.0):
    """生成单个知识点的内容"""
    point_info = get_point_info(config, point_id)
    if not point_info:
        print(f"错误: 找不到 ID 为 {point_id} 的知识点")
        return False
    
    print(f"\n[{point_id}/24] {point_info['name']} ({point_info['category']})")
    
    # 检查是否已存在
    output_file = CONTENT_DIR / f"{point_id}.json"
    if output_file.exists():
        print(f"  ⚠ 文件已存在，跳过（使用 --force 覆盖）")
        return True
    
    try:
        # 加载提示词
        prompt = load_prompt(point_id)
        
        # 调用 API
        response = call_deepseek_api(prompt)
        
        # 提取 JSON
        data = extract_json(response)
        
        # 验证数据结构
        required_fields = ["grammar_point", "category", "index", "content"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"缺少必要字段: {field}")
        
        # 保存
        save_content(point_id, data)
        
        # 延迟，避免请求过快
        if delay > 0:
            time.sleep(delay)
        
        return True
        
    except Exception as e:
        print(f"  ✗ 错误: {e}")
        return False


def generate_range(start_id: str, end_id: str, force: bool = False):
    """生成指定范围的知识点"""
    config = load_config()
    
    start_num = int(start_id)
    end_num = int(end_id)
    
    success_count = 0
    fail_count = 0
    
    print(f"=" * 50)
    print(f"开始生成知识点内容 [{start_id} - {end_id}]")
    print(f"=" * 50)
    
    for i in range(start_num, end_num + 1):
        point_id = f"{i:02d}"
        
        # 检查是否需要强制覆盖
        output_file = CONTENT_DIR / f"{point_id}.json"
        if output_file.exists() and not force:
            print(f"\n[{point_id}/24] 已存在，跳过")
            success_count += 1
            continue
        
        if generate_single(point_id, config):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n" + "=" * 50)
    print(f"生成完成: 成功 {success_count} 个, 失败 {fail_count} 个")
    print(f"=" * 50)


def main():
    parser = argparse.ArgumentParser(description="调用 DeepSeek API 生成语法知识点内容")
    parser.add_argument("--start", type=str, default="01", help="起始知识点 ID (默认: 01)")
    parser.add_argument("--end", type=str, default="24", help="结束知识点 ID (默认: 24)")
    parser.add_argument("--single", type=str, help="生成单个知识点 (如: 05)")
    parser.add_argument("--force", action="store_true", help="强制覆盖已存在的文件")
    parser.add_argument("--list", action="store_true", help="列出所有知识点")
    
    args = parser.parse_args()
    
    # 检查 API Key
    if not DEEPSEEK_API_KEY:
        print("错误: 未设置 DEEPSEEK_API_KEY 环境变量")
        print("请设置环境变量: export DEEPSEEK_API_KEY='your-api-key'")
        sys.exit(1)
    
    # 列出知识点
    if args.list:
        config = load_config()
        print("\n知识点列表:")
        for cat in config["categories"]:
            print(f"\n【{cat['name']}】")
            for point in cat["points"]:
                status = "✓" if (CONTENT_DIR / f"{point['id']}.json").exists() else "○"
                print(f"  {status} {point['id']}. {point['name']}")
        print()
        return
    
    # 生成单个
    if args.single:
        config = load_config()
        point_id = args.single.zfill(2)
        success = generate_single(point_id, config)
        sys.exit(0 if success else 1)
    
    # 生成范围
    generate_range(args.start, args.end, args.force)


if __name__ == "__main__":
    main()
