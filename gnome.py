import subprocess
from pathlib import Path

def set_gnome_wallpaper(image_path: Path):
    uri = f"file://{image_path.resolve()}"

    subprocess.run([
        "gsettings", "set",
        "org.gnome.desktop.background",
        "picture-uri", uri
    ], check=True)

    # Also set dark variant (safe even if unused)
    subprocess.run([
        "gsettings", "set",
        "org.gnome.desktop.background",
        "picture-uri-dark", uri
    ], check=True)
    print(f"Set GNOME wallpaper to {image_path}")