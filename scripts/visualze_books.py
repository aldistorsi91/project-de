import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setup
sns.set(style="whitegrid")
plt.rcParams.update({'figure.max_open_warning': 0})

# Load Data
df = pd.read_csv("data/books_all_genres.csv")
df['Harga'] = df['Harga'].astype(str).str.replace("£", "").astype(float)

# 1. Histogram Distribusi Harga
plt.figure(figsize=(10, 6))
sns.histplot(df['Harga'], bins=20, kde=True, color='skyblue')
plt.title("Distribusi Harga Buku (All Genres)")
plt.xlabel("Harga (£)")
plt.ylabel("Frekuensi")
plt.tight_layout()
plt.savefig("output/hist_harga.png")
plt.close()

# 2. Boxplot Harga per Genre
plt.figure(figsize=(10, 6))
sns.boxplot(x='Kategori', y='Harga', data=df, palette='Set2')
plt.title("Harga Buku per Kategori")
plt.ylabel("Harga (£)")
plt.xlabel("Kategori")
plt.tight_layout()
plt.savefig("output/boxplot_genre.png")
plt.close()

# 3. Barplot Jumlah Buku per Genre
plt.figure(figsize=(8, 5))
sns.countplot(x='Kategori', data=df, palette='pastel')
plt.title("Jumlah Buku per Genre")
plt.xlabel("Kategori")
plt.ylabel("Jumlah Buku")
plt.tight_layout()
plt.savefig("output/bar_jumlah_buku.png")
plt.close()

# 4. Barplot Rata-Rata Harga per Genre
avg_price = df.groupby('Kategori')['Harga'].mean().sort_values()
plt.figure(figsize=(8, 5))
sns.barplot(x=avg_price.index, y=avg_price.values, palette='magma')
plt.title("Harga Rata-rata Buku per Genre")
plt.xlabel("Kategori")
plt.ylabel("Rata-Rata Harga (£)")
plt.tight_layout()
plt.savefig("output/bar_avg_price.png")
plt.close()

# 5. Frekuensi Keyword
keyword_cols = [col for col in df.columns if col.startswith("Keyword_")]
keyword_counts = df[keyword_cols].fillna(False).astype(bool).sum()

plt.figure(figsize=(8, 5))
sns.barplot(x=keyword_counts.index.str.replace("Keyword_", ""), 
            y=keyword_counts.values, palette='mako')
plt.title("Frekuensi Keyword di Judul Buku")
plt.ylabel("Jumlah Buku")
plt.xlabel("Keyword")
plt.tight_layout()
plt.savefig("output/bar_keyword_freq.png")
plt.close()

print("✅ Semua visualisasi selesai dan disimpan di folder `output/`")