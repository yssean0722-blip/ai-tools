from datetime import datetime
from html import unescape
from urllib.request import urlopen
import re

HN_URL = "https://news.ycombinator.com/"
OUTPUT_FILE = "daily_news.md"
TOP_N = 10


def fetch_top_titles(limit: int = TOP_N) -> list[str]:
    with urlopen(HN_URL, timeout=10) as response:
        html = response.read().decode("utf-8", errors="ignore")

    matches = re.findall(r'<span class="titleline"><a [^>]*>(.*?)</a>', html)
    titles = [clean_html_text(text) for text in matches]
    return titles[:limit]


def clean_html_text(text: str) -> str:
    text = re.sub(r"<.*?>", "", text)
    return unescape(text).strip()


def build_markdown(titles: list[str], error_message: str = "") -> str:
    generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "# Hacker News 今日头条",
        "",
        f"生成时间：{generated_time}",
        "",
        "## 前 10 条新闻标题",
        "",
    ]

    if error_message:
        lines.append(f"> 抓取失败：{error_message}")
        lines.append("")

    for index, title in enumerate(titles, start=1):
        lines.append(f"{index}. {title}")

    lines.append("")
    return "\n".join(lines)


def save_markdown(content: str, filename: str = OUTPUT_FILE) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main() -> None:
    try:
        titles = fetch_top_titles()
        error_message = ""
    except Exception as error:
        titles = []
        error_message = str(error)

    markdown_content = build_markdown(titles, error_message)
    save_markdown(markdown_content)
    print(f"已生成 {OUTPUT_FILE}，共 {len(titles)} 条标题。")


if __name__ == "__main__":
    main()
