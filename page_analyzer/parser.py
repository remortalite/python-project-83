from bs4 import BeautifulSoup
import requests


def parse_html(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    title = soup.title.text
    h1_tag = soup.find("h1") or None
    description = (soup.find("meta", attrs={"name": "description"}) or {}).get("content")
    return {"title": soup.title.text,
            "h1": h1_tag.text if h1_tag else None,
            "description": description}