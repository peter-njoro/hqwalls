import random
from pathlib import Path
from constants import WALLPAPER_DIR

LAST_FILE = WALLPAPER_DIR.parent / "last_wallpaper.txt"

def get_all_wallpapers():
    wallpapers = []

    for category_dir in WALLPAPER_DIR.iterdir():
        if not category_dir.is_dir():
            continue
        for img in category_dir.glob("*.jpg"):
            wallpapers.append(img)

    return wallpapers

def pick_random_wallpaper():
    wallpapers = get_all_wallpapers()
    if not wallpapers:
        raise RuntimeError("No wallpapers found in cache")

    last = LAST_FILE.read_text().strip() if LAST_FILE.exists() else None

    candidates = [w for w in wallpapers if str(w) != last]
    chosen = random.choice(candidates or wallpapers)

    LAST_FILE.write_text(str(chosen))
    return chosen
