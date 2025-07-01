import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load data
df = pd.read_csv("data/booksdb_all_genres.csv")

# Bersihkan kolom Harga dari simbol £ dan ubah ke float
df['Harga'] = df['Harga'].astype(str).str.replace('£', '', regex=False).astype(float)

# 📦 Dimensi data
print("\n📦 Dimensi data:")
print(df.shape)

# 🧠 Kolom
print("\n🧠 Kolom:")
print(df.columns.tolist())

# 🧼 Missing values
print("\n🧼 Missing values per kolom:")
print(df.isnull().sum())

# 📊 Statistik harga
print("\n📊 Statistik harga:")
print(df['Harga'].describe())

# 🔥 Top 5 buku termahal per kategori
print("\n🔥 Top 5 buku termahal per kategori:")
for kategori in df['Kategori'].unique():
    print(f"\nKategori: {kategori}")
    top5 = df[df['Kategori'] == kategori].sort_values(by='Harga', ascending=False).head(5)
    print(top5[['Judul', 'Harga']].to_string(index=False))

# 🔎 Frekuensi keyword per genre
print("\n🔎 Frekuensi keyword per genre:")
keyword_cols = [col for col in df.columns if col.startswith("Keyword_")]

for col in keyword_cols:
    bool_col = df[col].fillna(False).astype(bool)
    print(f"{col}: {bool_col.sum()}")

top5_df = pd.DataFrame()

for kategori in df['Kategori'].unique():
    top5 = df[df['Kategori'] == kategori].sort_values(by='Harga', ascending=False).head(1)
    top5_df = pd.concat([top5_df, top5])

top5_df.to_csv("output/tables/each_genre_top_book.csv", index=False)