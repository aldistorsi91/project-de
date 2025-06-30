import os
import argparse
import pandas as pd
from config.genre_config import genres, keywords
from scripts.scrape.scraper import scrape_books
from scripts.transform.cleaner import clean_prices
from scripts.transform.enricher import enrich_keywords, enrich_features

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def process_genre(genre_name, genre_url, keywords):
    print(f"Processing genre: {genre_name.title()}")

    raw_books = scrape_books(genre_url)  # FIXED HERE
    df = pd.DataFrame(raw_books)
    df["Kategori"] = genre_name.title()
    df = clean_prices(df)
    df = enrich_keywords(df, keywords)
    df = enrich_features(df)

    save_path = os.path.join(DATA_DIR, f"booksdb_{genre_name}.csv")
    df.to_csv(save_path, index=False)
    print(f"Saved: {save_path}")

# ========== CLI Entry Point ==========
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--genre", type=str, help="Genre to scrape (e.g., fantasy)")
    parser.add_argument("--all", action="store_true", help="Scrape all genres")
    args = parser.parse_args()

    if args.all:
        for genre_name, genre_url in genres.items():
            keywords = genres.get(genre_name, {})
            process_genre(genre_name, genre_url, keywords)
    elif args.genre:
        genre_name = args.genre
        if genre_name not in genres:
            print(f"Genre '{genre_name}' not found.")
        else:
            genre_url = genres[genre_name]
            keywords = keywords.get(genre_name, {})
            process_genre(genre_name, genre_url, keywords)
    else:
        print("Use --genre=<name> to scrape specific genre or --all for all genres.")