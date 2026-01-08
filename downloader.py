import requests
from pathlib import Path

def download_image(url, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists():
        return dest

    r = requests.get(url, stream=True, timeout=30)
    r.raise_for_status()

    with open(dest, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

    return dest
