import json
import logging

class JSONExporter:
    @staticmethod
    def export(data, filepath):
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logging.info(f"Export complete: {filepath}")
        except Exception as e:
            logging.error(f"Failed to write output JSON: {e}")
            raise