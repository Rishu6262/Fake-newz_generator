import json
import os

class Exporter:

    def save_txt(self, article):
        os.makedirs("output", exist_ok=True)

        with open("output/news.txt", "w", encoding="utf-8") as f:
            f.write(article["headline"] + "\n\n")
            f.write(article["subheadline"] + "\n\n")
            f.write(article["body"])

    def save_json(self, article):
        os.makedirs("output", exist_ok=True)

        with open("output/news.json", "w", encoding="utf-8") as f:
            json.dump(article, f, indent=4)