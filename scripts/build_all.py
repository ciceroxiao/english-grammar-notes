#!/usr/bin/env python3
"""
批量构建所有 HTML 页面
Usage: uv run python scripts/build_all.py [--force]
"""

import argparse
import json
from pathlib import Path

CONTENT_DIR = Path("content")
DOCS_DIR = Path("docs")


def build_html(input_file: Path) -> bool:
    """调用 build_html.py 构建单个页面"""
    import subprocess
    
    try:
        result = subprocess.run(
            ["python", "scripts/build_html.py", str(input_file)],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ 构建失败: {e}")
        print(f"  错误输出: {e.stderr}")
        return False


def main():
    parser = argparse.ArgumentParser(description="批量构建所有 HTML 页面")
    parser.add_argument("--force", action="store_true", help="强制重新构建")
    
    args = parser.parse_args()
    
    # 获取所有 JSON 文件
    json_files = sorted(CONTENT_DIR.glob("[0-9][0-9].json"))
    
    if not json_files:
        print("没有找到 JSON 文件，请先运行 generate_content.py 生成内容")
        return
    
    print(f"=" * 50)
    print(f"开始构建 HTML 页面 ({len(json_files)} 个)")
    print(f"=" * 50)
    
    success_count = 0
    fail_count = 0
    
    for json_file in json_files:
        point_id = json_file.stem
        html_file = DOCS_DIR / f"{point_id}.html"
        
        # 检查是否需要构建
        if html_file.exists() and not args.force:
            # 比较修改时间
            if html_file.stat().st_mtime >= json_file.stat().st_mtime:
                print(f"\n[{point_id}] HTML 已是最新，跳过")
                success_count += 1
                continue
        
        print(f"\n[{point_id}] 构建中...")
        if build_html(json_file):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n" + "=" * 50)
    print(f"构建完成: 成功 {success_count} 个, 失败 {fail_count} 个")
    print(f"=" * 50)


if __name__ == "__main__":
    main()
