from urllib.parse import urlsplit
from bs4 import BeautifulSoup


def normalize_url(url):
    parts = urlsplit(url)
    normalized_url = f"{parts.netloc}{parts.path}"
    normalized_url = normalized_url.rstrip("/")
    return normalized_url.lower()


def get_heading_from_html(html):
    html_soup = BeautifulSoup(html, "html.parser")
    heading = html_soup.find("h1")
    if heading is None:
        heading = html_soup.find("h2")
    if heading is None:
        return ""
    heading_text = heading.get_text()
    return heading_text


def get_first_paragraph_from_html(html):
    html_soup = BeautifulSoup(html, "html.parser")
    paragraph = html_soup.find("main")
    if paragraph is None:
        paragraph = html_soup.find("p")
    else:
        paragraph = paragraph.find("p")
    if paragraph is None:
        return ""
    paragraph_text = paragraph.get_text()
    return paragraph_text
