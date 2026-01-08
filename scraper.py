from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_wallpaper_pages(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    # hdqwalls wallpaper cards
    for a in soup.select("a[href]"):
        href = a.get("href")

        # skip empty values
        if not href:
            continue

        # normalize href to a string if BeautifulSoup returns an AttributeValueList
        if not isinstance(href, str):
            try:
                href = href[0]
            except Exception:
                href = str(href)

        # valid wallpaper pages look like /category/id-name
        if href.count("/") >= 2 and not href.lower().endswith(".jpg") and href.startswith("/"):
            full = urljoin(base_url, href)
            links.add(full)

    return list(links)

