import asyncio
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from pathlib import Path
import requests
import os
# === CONFIG ===
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
CACHE_DIR = Path.home() / ".local" / "share" / "hqwalls" / "wallpapers"

# Mapping categories to Telegram public channels
CATEGORY_CHANNELS = {
    "anime": "hdqwalls_anime",
    "nature": "hdqwalls_nature",
    "celebrities": "hdqwalls_celebrities",
    "girls": "hdqwalls_girls",
    "fantasy-girls": "hdqwalls_fantasy_girls",
    "cute": "hdqwalls_cute",
    "cartoons": "hdqwalls_cartoons",
}

# Max number of messages to fetch per channel
MAX_MESSAGES = 50

# ---- FUNCTIONS ----

async def fetch_channel_photos(client, category, channel_username):
    """Fetch recent photos from a public Telegram channel."""
    print(f"[+] Fetching Telegram wallpapers for category '{category}' from @{channel_username}...")
    category_dir = CACHE_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)

    async for message in client.iter_messages(channel_username, limit=MAX_MESSAGES):
        if message.media and isinstance(message.media, MessageMediaPhoto):
            file_path = category_dir / f"{message.id}.jpg"
            if file_path.exists():
                continue
            photo_bytes = await client.download_media(message.media)
            if photo_bytes:
                with open(file_path, "wb") as f:
                    f.write(photo_bytes)
                print(f"  ✓ Downloaded {file_path.name}")

async def main():
    client = TelegramClient("hqwalls_session", API_ID, API_HASH)
    await client.start()
    for category, channel in CATEGORY_CHANNELS.items():
        await fetch_channel_photos(client, category, channel)
    await client.disconnect()
    print("[+] Telegram fetch complete!")

def run():
    asyncio.run(main())

if __name__ == "__main__":
    run()
