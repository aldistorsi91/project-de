# %%

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

books = []
for book in soup.select('.product_pod'):
    title = book.h3.a['title']
    price = book.select_one('.price_color').text.strip()
    books.append({'Judul': title, 'Harga': price})

df = pd.DataFrame(books)
df.to_csv('books_fantasy.csv', index=False)

# Re-load CSV
df = pd.read_csv('books_history.csv')

# Bersihin kolom harga (hapus simbol £ dan convert ke float)
df['Harga'] = df['Harga'].str.replace('£', '').astype(float)

# Cek null dan duplikat
print("\n🧼 Cek data kosong:")
print(df.isnull().sum())

print("\n🧼 Duplikat:")
print(df.duplicated().sum())

# Top 5 buku termahal
top5 = df.sort_values(by='Harga', ascending=False).head()

print("\n🔥 5 Buku Termahal:")
print(top5[['Judul', 'Harga']].to_string(index=False))


# %%
