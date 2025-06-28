import os
from scripts.scrape.scrape_fantasy import run as scrape_fantasy
from scripts.scrape.scrape_romance import run as scrape_romance
from scripts.scrape.scrape_scifi import run as scrape_scifi
from scripts.scrape.scrape_history import run as scrape_history
from scripts.analysis.analysis import run as run_analysis

def main():
    print("🚀 Start automation pipeline...")
    
    # Scrape + clean + enrich per genre
    scrape_fantasy()
    scrape_romance()
    scrape_scifi()
    scrape_history()

    # Analisis all books
    run_analysis()

    print("✅ All done!")

if __name__ == "__main__":
    main()
