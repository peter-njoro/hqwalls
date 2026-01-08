from picker import pick_random_wallpaper
from gnome import set_gnome_wallpaper

def rotate():
    wallpaper = pick_random_wallpaper()
    set_gnome_wallpaper(wallpaper)
    print(f"🖼️  Wallpaper set: {wallpaper.name}")

if __name__ == "__main__":
    rotate()
