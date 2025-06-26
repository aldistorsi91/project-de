import pandas as pd

df = pd.read_csv("data/booksdb_all_genres.csv")
print("Shape:", df.shape)
print("Kolom:", df.columns.tolist())
print("Cek null:")
print(df.isnull().sum())
print("\nKategori yang tersedia:")
print(df['Kategori'].value_counts())