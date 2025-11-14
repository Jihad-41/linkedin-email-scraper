import json
import logging
from pathlib import Path
from extractors.linkedin_parser import LinkedInParser
from outputs.exporters import JSONExporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def load_settings():
    settings_path = Path(__file__).parent / "config" / "settings.json"
    if not settings_path.exists():
        raise FileNotFoundError("Missing settings.json. Copy settings.example.json to settings.json.")
    with open(settings_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    settings = load_settings()
    keyword = settings.get("keyword")
    domains = settings.get("emailDomains")
    max_results = settings.get("maxResults", 50)

    parser = LinkedInParser(keyword, domains, max_results)
    results = parser.run()

    output_path = Path(__file__).parent.parent / "data" / "output.json"
    JSONExporter.export(results, output_path)

    logging.info(f"Scraping complete. Saved {len(results)} results to {output_path}")

if __name__ == "__main__":
    main()