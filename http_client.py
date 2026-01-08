import requests
import time

class HTTPSession:
    def __init__(self, user_agent, delay=1.5):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": user_agent,
            "Accept-Language": "en-US,en;q=0.9",
        })
        self.delay = delay

    def get(self, url, retries: int = 3):
        """GET with retries and optional Cloudflare-bypass fallback.

        Returns response text on success, or None on failure.
        """
        time.sleep(self.delay)
        backoff = 1.0
        for attempt in range(1, retries + 1):
            try:
                resp = self.session.get(url, timeout=15)

                # If Cloudflare returns a challenge/forbidden, attempt a cloudscraper fallback
                if resp.status_code in (403, 429):
                    print(f"[!] Received HTTP {resp.status_code} for {url!r}; trying cloudscraper fallback")
                    try:
                        import cloudscraper

                        scraper = cloudscraper.create_scraper()
                        cs = scraper.get(url, timeout=15)
                        if cs.status_code == 200:
                            return cs.text
                        else:
                            print(f"[!] cloudscraper returned status {cs.status_code} for {url!r}")
                            return None
                    except Exception as e:
                        print(f"[!] cloudscraper fallback failed: {e}. Install it with: pip install cloudscraper")
                        return None

                resp.raise_for_status()
                return resp.text
            except requests.RequestException as e:
                print(f"[!] HTTP GET error for {url!r}: {e} (attempt {attempt}/{retries})")
                if attempt == retries:
                    print(f"[!] Giving up on {url!r} after {retries} attempts")
                    return None
                time.sleep(backoff)
                backoff *= 2
        return None
