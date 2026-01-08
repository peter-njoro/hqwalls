#!/usr/bin/env python3
import os
from pathlib import Path
import subprocess
import sys
import shutil
import os

# Read Telegram credentials from environment variables
TELEGRAM_API_ID = os.environ.get("HQWALLS_TELEGRAM_API_ID", "123456")  # default fallback
TELEGRAM_API_HASH = os.environ.get("HQWALLS_TELEGRAM_API_HASH", "abcdef123456...")  # default fallback


# Paths
HOME = Path.home()
CONFIG_DIR = HOME / ".config" / "hqwalls"
DATA_DIR = HOME / ".local" / "share" / "hqwalls"
PROJECT_DIR = Path(__file__).parent.resolve()
PYTHON = sys.executable

SERVICE_FILE = CONFIG_DIR / "hqwalls.service"
TIMER_FILE = CONFIG_DIR / "hqwalls.timer"
CONFIG_FILE = CONFIG_DIR / "config.toml"

# Default config
CONFIG_TOML_CONTENT = """[general]
resolution = "2560x1440"
max_pages_per_category = 2
max_cache_per_category = 20
user_agent = "hqwalls/1.0 (GNOME Wallpaper Rotator)"

[categories]
anime = true
nature = true
celebrities = true
girls = true
fantasy-girls = true
cute = true
cartoons = true

TELEGRAM_SECTION = f"""
[telegram]
enabled = true
api_id = {TELEGRAM_API_ID}
api_hash = "{TELEGRAM_API_HASH}"
channels_enabled = true
"""


"""


print("[+] Telegram section added to config.toml (from environment variables)")

SERVICE_CONTENT = f"""[Unit]
Description=HQWalls GNOME Wallpaper Rotator

[Service]
Type=oneshot
ExecStart={PYTHON} {PROJECT_DIR}/rotate.py
StandardOutput=append:{DATA_DIR}/rotate.log
StandardError=append:{DATA_DIR}/rotate.log
"""

TIMER_CONTENT = """[Unit]
Description=Run HQWalls wallpaper rotation every 30 minutes

[Timer]
OnBootSec=2min
OnUnitActiveSec=30min
Persistent=true

[Install]
WantedBy=timers.target
"""

def ensure_dirs():
    for d in [CONFIG_DIR, DATA_DIR]:
        d.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "wallpapers").mkdir(exist_ok=True)

def write_file(path: Path, content: str):
    with open(path, "w") as f:
        f.write(content)
    print(f"[+] Created {path}")

def run_main():
    main_py = PROJECT_DIR / "main.py"
    if main_py.exists():
        print("[+] Running main.py to fetch wallpapers...")
        subprocess.run([PYTHON, str(main_py)], check=True)
    else:
        print(f"[!] main.py not found in {PROJECT_DIR}")

def rotate_once():
    rotate_py = PROJECT_DIR / "rotate.py"
    if rotate_py.exists():
        print("[+] Rotating wallpaper immediately...")
        subprocess.run([PYTHON, str(rotate_py)], check=True)
    else:
        print(f"[!] rotate.py not found in {PROJECT_DIR}")

def setup_systemd():
    write_file(SERVICE_FILE, SERVICE_CONTENT)
    write_file(TIMER_FILE, TIMER_CONTENT)

    # Reload user systemd and enable timer
    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    subprocess.run(["systemctl", "--user", "enable", "--now", "hqwalls.timer"], check=True)
    print("[+] systemd timer enabled (30 min rotation)")

def main():
    ensure_dirs()
    write_file(CONFIG_FILE, CONFIG_TOML_CONTENT)
    setup_systemd()
    run_main()
    rotate_once()
    print("\n🎉 Installation complete! Wallpapers will now rotate automatically every 30 minutes.")

if __name__ == "__main__":
    main()
