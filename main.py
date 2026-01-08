from constants import CATEGORY_URLS, WALLPAPER_DIR
from config import load_config
from http_client import HTTPSession
from scraper import extract_wallpaper_pages
from license_filter import is_hdqwalls_owned
from images import extract_image_url
from downloader import download_image
from pathlib import Path

def main():
    config = load_config()
    session = HTTPSession(config["general"]["user_agent"])

    resolution = config["general"]["resolution"]
    max_pages = config["general"]["max_pages_per_category"]

    for category, enabled in config["categories"].items():
        if not enabled:
            continue

        print(f"[+] Category: {category}")
        base_url = CATEGORY_URLS[category]

        for page in range(1, max_pages + 1):
            url = f"{base_url}?page={page}"
            html = session.get(url)

            pages = extract_wallpaper_pages(html, base_url)
            for wp_url in pages:
                wp_html = session.get(wp_url)

                if not is_hdqwalls_owned(wp_html):
                    continue

                img_url = extract_image_url(wp_html, resolution)
                if not img_url or not isinstance(img_url, str):
                    continue

                filename = img_url.split("/")[-1]
                dest = WALLPAPER_DIR / category / filename
                download_image(img_url, dest)

                print(f"  ✓ downloaded {filename}")

if __name__ == "__main__":
    main()
