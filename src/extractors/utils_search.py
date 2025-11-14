import logging
import requests
from urllib.parse import urlencode

class GoogleSearchScraper:
    BASE_URL = "https://www.googleapis.com/customsearch/v1"

    def __init__(self):
        # Free scraping fallback (uses serpapi-like pattern but without API key; real projects should integrate API)
        self.session = requests.Session()

    def search(self, query: str, limit: int):
        logging.info("Querying Google search...")
        results = []
        page = 0

        while len(results) < limit:
            params = {
                "q": query,
                "start": page * 10 + 1,
                "num": 10
            }

            url = f"https://www.google.com/search?{urlencode(params)}"
            response = self.session.get(url, headers={"User-Agent": "Mozilla/5.0"})

            if response.status_code != 200:
                logging.error("Google request blocked or failed.")
                break

            text = response.text
            items = self.parse_html(text)
            if not items:
                break

            results.extend(items)
            page += 1

        return results[:limit]

    def parse_html(self, html: str):
        # Minimal HTML pattern extraction
        import re
        pattern = r'<a href="(https://[^"]+)"[^>]*><h3.*?>(.*?)</h3></a>.*?<span class="aCOpRe">(.*?)</span>'
        matches = re.findall(pattern, html, re.S)

        items = []
        for link, title, snippet in matches:
            items.append({
                "title": re.sub("<.*?>", "", title).strip(),
                "link": link.strip(),
                "snippet": re.sub("<.*?>", "", snippet).strip()
            })
        return items