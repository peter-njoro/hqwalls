# HQWalls – Because I Wanted All the Wallpapers

TL;DR: I got obsessed with hdqwalls.com’s wallpapers, wrote a Python bot to download and rotate them on my GNOME desktop… then realized I was basically automating my own procrastination.  

It’s paused now. The code still works (it works on my machine), it’s not illegal, but honestly, it’s mostly just me having fun with Python, scraping, and systemd timers.  

Enjoy the wallpapers, admire the code, but don’t expect world-changing software here 😎

# HQWalls – GNOME Wallpaper Rotator (Project Paused)

**Status:** Paused / Not actively maintained  

---

## Overview

HQWalls was a personal project I started because I thought [hdqwalls.com](https://hdqwalls.com) has *amazing wallpapers*, and I wanted a way to collect and enjoy as many of them as possible on my GNOME desktop.  

The goal was to automatically fetch wallpapers from hdqwalls.com (legally owned ones), organize them by category, and rotate them every 30 minutes on a GNOME desktop environment.

---

## Features (Implemented)

- Category-aware wallpaper fetching:
  - Categories included: `anime`, `nature`, `celebrities`, `girls`, `fantasy-girls`, `cute`, `cartoons`
- Legal filtering: only wallpapers that explicitly belong to hdqwalls.com
- Configurable resolution (default `2560x1440`)
- Random wallpaper rotation
- GNOME wallpaper integration (X11 & Wayland safe)
- Systemd user timer for automatic rotation every 30 minutes
- Local caching to avoid unnecessary downloads

---

## Why I Stopped

After working on it, I realized a few things:

1. It’s more of a **glorified waste of time** than a meaningful project — fun to build, but not really useful beyond my own desktop.
2. **Legal considerations:** while fetching hdqwalls-owned wallpapers is **not illegal**, it still doesn’t feel quite right to automate their content collection at scale.  
   > Don’t worry — there’s no illegal activity here. The project respects copyrights and doesn’t remove watermarks or redistribute content.
3. I got what I wanted: a deep dive into Python automation, scraping, systemd timers, and GNOME integration. That experience was the real value.

---

## Installation & Usage

If you still want to try it at your own discretion:

1. Place the project folder somewhere (e.g., `~/projects/hqwalls`)
2. Create a Python virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Run the installer script to set up config, systemd timer, and fetch wallpapers:
```bash
python install_hqwalls.py
```
4. Wallpapers will rotate every 30 minutes automatically.

Conclusion

HQWalls was a personal experiment in automation, scraping, and desktop integration.
While I’ve paused it due to being more of a “fun distraction” than a serious project, it served its purpose: I learned a lot and collected some awesome wallpapers for myself.

If you’re curious, you can still explore the code — just be mindful of copyright rules and don’t redistribute content.