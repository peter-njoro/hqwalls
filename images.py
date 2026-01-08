from bs4 import BeautifulSoup

def extract_image_url(html, target_resolution):
    soup = BeautifulSoup(html, "html.parser")

    # hdqwalls stores resolution links in anchors
    links = soup.select("a[href$='.jpg']")

    candidates = {}
    for link in links:
        href = link.get("href")
        if target_resolution in href:
            return href  # perfect match
        candidates[href] = href

    # fallback: highest resolution available
    if candidates:
        return sorted(candidates.keys())[-1]

    return None
