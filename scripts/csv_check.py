import pandas as pd

df = pd.read_csv("data/booksdb_all_genres.csv")
print("Shape:", df.shape)
print("Kolom:", df.columns.tolist())
print("Cek null:")
print(df.isnull().sum())
print("\nBuku yang tersedia:")
print(df['Kategori'].value_counts())