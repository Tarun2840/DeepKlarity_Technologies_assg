# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str) -> (str, str):
    headers = {"User-Agent": "ai-quiz-generator/0.1 (intern test)"}
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    title_tag = soup.select_one("#firstHeading")
    title = title_tag.get_text(strip=True) if title_tag else url
    content_div = soup.select_one("#mw-content-text")
    if not content_div:
        content_div = soup.body
    for tag in content_div.select("table, sup, .reference, .mw-editsection"):
        tag.decompose()
    paragraphs = [p.get_text(" ", strip=True) for p in content_div.find_all("p") if p.get_text(strip=True)]
    cleaned = "\n\n".join(paragraphs)
    return title, cleaned
