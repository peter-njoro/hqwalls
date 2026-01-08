from bs4 import BeautifulSoup

ALLOWED_MARKERS = [
    "© hdqwalls.com",
    "By hdqwalls.com",
]

def is_hdqwalls_owned(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ").lower()

    return any(marker.lower() in text for marker in ALLOWED_MARKERS)

licence = is_hdqwalls_owned
print(license)