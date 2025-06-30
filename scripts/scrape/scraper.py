from bs4 import BeautifulSoup
import requests

def scrape_books(url):
    books = []
    page_url = "index.html"
    while True:
        res = requests.get(url + page_url)
        soup = BeautifulSoup(res.content, "lxml")
        for book in soup.select(".product_pod"):
            books.append({
                "Judul": book.h3.a["title"],
                "Harga": book.select_one(".price_color").text.strip()
            })
        next_btn = soup.select_one(".next > a")
        page_url = next_btn["href"] if next_btn else None
        if not page_url:
            break
    return books