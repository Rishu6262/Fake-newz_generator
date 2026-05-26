from generator import NewsGenerator
from exporter import Exporter
from data import categories

def display(article):
    print("\n" + "=" * 60)
    print("FAKE NEWS ARTICLE")
    print("=" * 60)

    print("\nCategory:", article["category"])
    print("\nHeadline:", article["headline"])
    print("\nSubheadline:", article["subheadline"])
    print("\nBody:\n")
    print(article["body"])
    print("\nAuthor:", article["author"])
    print("Date:", article["date"])

def main():
    generator = NewsGenerator()
    exporter = Exporter()
    article = None

    while True:
        print("\n1. Generate News")
        print("2. Export TXT")
        print("3. Export JSON")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nCategories:")
            for i, cat in enumerate(categories, 1):
                print(i, cat)

            cat_choice = int(input("Choose category: "))
            category = categories[cat_choice - 1]

            article = generator.generate_news(category)
            display(article)

        elif choice == "2":
            if article:
                exporter.save_txt(article)
                print("TXT saved successfully.")
            else:
                print("Generate news first.")

        elif choice == "3":
            if article:
                exporter.save_json(article)
                print("JSON saved successfully.")
            else:
                print("Generate news first.")

        elif choice == "4":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()