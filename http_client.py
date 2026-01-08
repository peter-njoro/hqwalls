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

    def get(self, url):
        time.sleep(self.delay)
        response = self.session.get(url, timeout=15)
        response.raise_for_status()
        return response.text
