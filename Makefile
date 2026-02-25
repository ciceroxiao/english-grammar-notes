# 英语语法学习项目 Makefile

.PHONY: help install generate build serve clean list status

# 默认目标
help:
	@echo "英语语法学习项目 - 可用命令:"
	@echo ""
	@echo "  make install        - 安装依赖"
	@echo "  make list           - 列出所有知识点及生成状态"
	@echo "  make status         - 查看项目状态"
	@echo ""
	@echo "  make generate       - 生成所有知识点内容 (调用 DeepSeek API)"
	@echo "  make generate ID=01 - 生成单个知识点"
	@echo ""
	@echo "  make build          - 构建所有 HTML 页面"
	@echo "  make build-force    - 强制重新构建所有页面"
	@echo ""
	@echo "  make serve          - 启动本地预览服务器"
	@echo "  make clean          - 清理生成的文件"
	@echo ""

# 安装依赖
install:
	uv pip install -r requirements.txt

# 列出知识点
list:
	@uv run python scripts/generate_content.py --list

# 查看项目状态
status:
	@echo "项目状态:"
	@echo ""
	@echo "提示词文件: $$(ls prompts/generated/*.txt 2>/dev/null | wc -l) / 24"
	@echo "内容文件:   $$(ls content/[0-9][0-9].json 2>/dev/null | wc -l) / 24"
	@echo "HTML 页面:  $$(ls docs/[0-9][0-9].html 2>/dev/null | wc -l) / 24"
	@echo ""
	@make list

# 生成内容
generate:
ifdef ID
	@uv run python scripts/generate_content.py --single $(ID)
else
	@uv run python scripts/generate_content.py --start 01 --end 24
endif

# 构建 HTML
build:
	@uv run python scripts/build_all.py

build-force:
	@uv run python scripts/build_all.py --force

# 启动预览服务器
serve:
	@echo "启动服务器: http://localhost:8000"
	@cd docs && python -m http.server 8000

# 清理
clean:
	@echo "清理生成的文件..."
	rm -rf content/[0-9][0-9].json
	rm -rf docs/[0-9][0-9].html
	@echo "完成"

# 一键构建全部
all: generate build
	@echo "全部完成!"
