import random
import datetime
import textwrap
from data import *

class NewsGenerator:

    def generate_news(self, category):
        template = random.choice(templates[category])

        headline = template.format(
            person=random.choice(politicians),
            company=random.choice(companies),
            city=random.choice(cities),
            amount=random.choice(amounts)
        )

        subheadline = f"Experts react as this major event creates buzz across {random.choice(cities)}."

        body = textwrap.fill(f"""In a surprising development, {headline.lower()}.Sources suggest this decision may impact industries and citizens significantly.Analysts believe the move could reshape the future of the sector.The announcement has already triggered discussions across multiple regions.
            """,
            width=150
        )

        article = {
            "category": category,
            "headline": headline,
            "subheadline": subheadline,
            "body": body,
            "author": random.choice(authors),
            "date": str(datetime.date.today())
        }

        return article