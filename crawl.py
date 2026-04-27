from urllib.parse import urlsplit


def normalize_url(url):
    parts = urlsplit(url)
    normalized_url = f"{parts.netloc}{parts.path}"
    normalized_url = normalized_url.rstrip("/")
    return normalized_url.lower()
