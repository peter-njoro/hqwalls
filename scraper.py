from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_wallpaper_pages(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    # hdqwalls wallpaper cards
    for a in soup.select("a[href]"):
        href = a.get("href")

        # valid wallpaper pages look like /category/id-name
        if href and href.count("/") >= 2 and not href.endswith(".jpg"):
            if href and isinstance(href, str) and href.startswith("/"):
                full = urljoin(base_url, href)
                links.add(full)

    return list(links)

