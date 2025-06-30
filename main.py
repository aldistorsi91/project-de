import argparse
import pandas as pd
from pathlib import Path
from config.genre_config import genres
from scripts.scrape.scraper import scrape_books
from scripts.transform.cleaner import clean_prices
from scripts.transform.enricher import enrich_keywords, enrich_features

# === Setup Direktori Output ===
DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

def process_genre(genre_name, genre_url, keywords):
    print(f"\nProcessing genre: {genre_name.title()}")

    df = scrape_books(genre_name, genre_url)  # langsung return dataframe
    df = clean_prices(df)
    df = enrich_keywords(df, keywords)
    df = enrich_features(df)

    save_path = DATA_DIR / f"booksdb_{genre_name}.csv"
    df.to_csv(save_path, index=False)
    print(f"Saved: {save_path}")

# === CLI Entry Point ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape books by genre")
    parser.add_argument("--genre", type=str, help="Scrape specific genre only (e.g., fantasy)")
    parser.add_argument("--all", action="store_true", help="Scrape all genres")
    args = parser.parse_args()

    if args.all:
        for genre in genres:
            process_genre(genre["name"], genre["url"], genre["keywords"])
    elif args.genre:
        found = next((g for g in genres if g["name"] == args.genre), None)
        if found:
            process_genre(found["name"], found["url"], found["keywords"])
        else:
            print(f"Genre '{args.genre}' not found.")
    else:
        print("Use --genre=<name> to scrape a specific genre or --all to scrape all.")