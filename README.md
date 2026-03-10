# Hacker News 标题抓取（Python 新手版）

这是一个最简单的 Python 小项目：
- 抓取 Hacker News 首页新闻
- 提取前 10 条的标题和链接
- 生成 `daily_news.md`

## 项目结构

```text
ai-tools/
├── fetch_hn_news.py     # 主脚本：抓取并生成 Markdown
├── requirements.txt     # 说明：本项目无第三方依赖
├── daily_news.md        # 运行后生成的结果文件
└── README.md            # 使用说明
```

## 环境要求

- Python 3.9+

## 安装依赖

本项目仅使用 Python 标准库，无需安装第三方依赖。

## 运行方法

```bash
python fetch_hn_news.py
```

运行后会在当前目录生成 `daily_news.md`，内容包括：
- 生成时间
- Hacker News 首页前 10 条新闻的「标题 + 链接」

## 示例输出（daily_news.md）

```markdown
# Hacker News 今日头条

生成时间：2026-01-01 09:00:00

## 前 10 条新闻（标题 + 链接）

1. [Example News A](https://example.com/a)
2. [Example News B](https://example.com/b)
...
```

## 代码说明

`fetch_hn_news.py` 只有 4 个步骤，方便新手理解：
1. 请求 Hacker News 首页 HTML
2. 提取新闻标题和链接
3. 组装 Markdown 内容
4. 保存到 `daily_news.md`
