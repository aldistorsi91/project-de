from config.genre_config import genres
from scrape.scraper import scrape_books
from transform.cleaner import clean_prices
from transform.enricher import enrich_keywords, enrich_features
import os

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

for genre in genres:
    name = genre["name"]
    url = genre["url"]
    keywords = genre["keywords"]

    print(f"🚀 Running for genre: {name.title()}")
    df = scrape_books(name, url)
    df = clean_prices(df)
    df = enrich_keywords(df, keywords)
    df = enrich_features(df)

    save_path = os.path.join(DATA_DIR, f"booksdb_{name.replace(' ', '_')}.csv")
    df.to_csv(save_path, index=False)
    print(f"Saved to {save_path}\n")