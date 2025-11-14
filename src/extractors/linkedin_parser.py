import re
import logging
from .utils_search import GoogleSearchScraper

class LinkedInParser:
    EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    def __init__(self, keyword: str, domains: list, max_results: int):
        self.keyword = keyword
        self.domains = [d.lower() for d in domains]
        self.max_results = max_results
        self.scraper = GoogleSearchScraper()

    def extract_email(self, text: str):
        matches = re.findall(self.EMAIL_REGEX, text)
        for email in matches:
            if any(email.lower().endswith(domain) for domain in self.domains):
                return email
        return None

    def run(self):
        logging.info(f"Starting scrape for keyword: {self.keyword}")
        query = f'site:linkedin.com/in "{self.keyword}" email'

        google_results = self.scraper.search(query, self.max_results)
        parsed_results = []

        for item in google_results:
            email = self.extract_email(item.get("snippet", ""))
            if not email:
                continue

            parsed_results.append({
                "keywords": self.keyword,
                "emailDomains": ", ".join(self.domains),
                "email": email,
                "title": item.get("title"),
                "url": item.get("link"),
                "text": item.get("snippet")
            })

            if len(parsed_results) >= self.max_results:
                break

        logging.info(f"Extracted {len(parsed_results)} valid entries.")
        return parsed_results