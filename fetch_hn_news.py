from datetime import datetime
from html import unescape
import re
from urllib.parse import urljoin
from urllib.request import urlopen

HN_URL = "https://news.ycombinator.com/"
OUTPUT_FILE = "daily_news.md"
TOP_N = 10


def fetch_top_news(limit: int = TOP_N) -> list[tuple[str, str]]:
    with urlopen(HN_URL, timeout=10) as response:
        html = response.read().decode("utf-8", errors="ignore")

    matches = re.findall(
        r'<span class="titleline"><a href="(.*?)"[^>]*>(.*?)</a>',
        html,
    )

    news_list: list[tuple[str, str]] = []
    for href, raw_title in matches[:limit]:
        title = clean_html_text(raw_title)
        link = urljoin(HN_URL, unescape(href).strip())
        news_list.append((title, link))

    return news_list


def clean_html_text(text: str) -> str:
    text = re.sub(r"<.*?>", "", text)
    return unescape(text).strip()


def build_markdown(news_list: list[tuple[str, str]], error_message: str = "") -> str:
    generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "# Hacker News 今日头条",
        "",
        f"生成时间：{generated_time}",
        "",
        "## 前 10 条新闻（标题 + 链接）",
        "",
    ]

    if error_message:
        lines.append(f"> 抓取失败：{error_message}")
        lines.append("")

    for index, (title, link) in enumerate(news_list, start=1):
        lines.append(f"{index}. [{title}]({link})")

    lines.append("")
    return "\n".join(lines)


def save_markdown(content: str, filename: str = OUTPUT_FILE) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main() -> None:
    try:
        news_list = fetch_top_news()
        error_message = ""
    except Exception as error:
        news_list = []
        error_message = str(error)

    markdown_content = build_markdown(news_list, error_message)
    save_markdown(markdown_content)
    print(f"已生成 {OUTPUT_FILE}，共 {len(news_list)} 条新闻。")


if __name__ == "__main__":
    main()
