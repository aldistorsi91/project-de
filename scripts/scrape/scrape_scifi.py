import pandas as pd
import requests
from bs4 import BeautifulSoup

# ========== Konfigurasi Genre ==========
GENRE_NAME = "scifi"
GENRE_URL = "http://books.toscrape.com/catalogue/category/books/science-fiction_16/"
SAVE_PATH = f"data/booksdb_{GENRE_NAME}.csv"

# ========== Scraping ==========
page_url = "index.html"
books = []

while True:
    print(f"Scraping: {page_url}")
    res = requests.get(GENRE_URL + page_url)
    soup = BeautifulSoup(res.content, "lxml")

    for book in soup.select(".product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip()
        books.append({"Judul": title, "Harga": price, "Kategori": GENRE_NAME.title()})

    next_btn = soup.select_one(".next > a")
    if next_btn:
        page_url = next_btn["href"]
    else:
        break

# ========== Cleaning & Enrichment ==========
df = pd.DataFrame(books)
df['Harga'] = df['Harga'].str.replace('Â£', '').str.replace('Â', '').str.replace('�', '').str.replace('£', '').astype(float)

# Enrichment keywords
keywords = {
    'Keyword_Space': 'space',
    'Keyword_Alien': 'alien',
    'Keyword_Time': 'time',
    'Keyword_Future': 'future',
}

for col, kw in keywords.items():
    df[col] = df['Judul'].str.lower().str.contains(kw)

# Feature engineering
df['Judul_Length'] = df['Judul'].apply(len)
df['Jumlah_Kata_Judul'] = df['Judul'].apply(lambda x: len(x.split()))
df['Is_Series'] = df['Judul'].str.contains(r'#\d+', regex=True)
df['Contains_Colon'] = df['Judul'].str.contains(":")

# ========== Simpan ==========
df.to_csv(SAVE_PATH, index=False)
print(f"Selesai! Disimpan ke {SAVE_PATH}")