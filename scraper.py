from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_wallpaper_pages(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for a in soup.select("a[href*='wallpaper']"):
        href = a.get("href")
        if href and isinstance(href, str) and href.startswith("/"):
            links.append(urljoin(base_url, href))

    return list(set(links))
