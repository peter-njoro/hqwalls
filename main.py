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

    # debug: show loaded config values so it's clear why loops run or not
    print(f"[i] resolution: {resolution}, max_pages_per_category: {max_pages}")

    for category, enabled in config["categories"].items():
        if not enabled:
            continue

        print(f"[+] Category: {category}")
        base_url = CATEGORY_URLS[category]

        for page in range(1, max_pages + 1):
            url = f"{base_url}?page={page}"
            html = session.get(url)
            if html is None:
                print(f"    (failed to fetch {url})")
                continue

            pages = extract_wallpaper_pages(html, base_url)
            if not pages:
                print(f"    (no wallpaper pages found for {url})")
                # Helpful debug: show how many bytes we fetched and a short snippet
                try:
                    size = len(html) if html is not None else 0
                    snippet = " ".join(str(html).splitlines())[:500]
                except Exception:
                    size = 0
                    snippet = "(unable to render snippet)"

                print(f"    -> fetched {size} bytes")
                print(f"    -> snippet: {snippet!r}")

            for wp_url in pages:
                wp_html = session.get(wp_url)
                if wp_html is None:
                    print(f"  ✗ failed to fetch wallpaper page {wp_url}")
                    continue
                if not is_hdqwalls_owned(wp_html):
                    print("  ✗ skipped (not hdqwalls-owned)")
                    continue

                print(f"  [-] Wallpaper: {wp_url}")

                img_url = extract_image_url(wp_html, resolution)
                if not img_url or not isinstance(img_url, str):
                    print("  ✗ no image found")
                    continue

                print(f"    -> image URL: {img_url}")

                filename = img_url.split("/")[-1]
                dest = WALLPAPER_DIR / category / filename
                download_image(img_url, dest)

                print(f"  ✓ downloaded {filename}")


if __name__ == "__main__":
    main()
