from bs4 import BeautifulSoup

# List of strings to search for in page text. Matching is case-insensitive.
# Example: ['hdqwalls', 'hqwalls', '© hdqwalls']
ALLOWED_MARKERS = [
    
]

# When True, accept any page as owned (bypass marker checks).
# Alternatively, including '*' in ALLOWED_MARKERS will also allow all markers.
ALLOW_ALL_MARKERS = False

def is_hdqwalls_owned(html):
    """
    Return True if the given HTML contains any allowed marker.

    Behavior:
    - If ALLOW_ALL_MARKERS is True, always return True.
    - If '*' is present in ALLOWED_MARKERS, treat as allow-all and return True.
    - Otherwise, return True if any marker from ALLOWED_MARKERS appears in the page text.
    """
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ").lower()

    # allow-all shortcuts
    if ALLOW_ALL_MARKERS:
        return True

    if any(marker.strip() == '*' for marker in ALLOWED_MARKERS):
        return True

    return any(marker.lower() in text for marker in ALLOWED_MARKERS)