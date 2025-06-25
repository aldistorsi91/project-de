import pandas as pd

df = pd.read_csv("data/books_all_genres.csv")
print("📦 Shape:", df.shape)
print("🧠 Kolom:", df.columns.tolist())
print("🧼 Cek null:")
print(df.isnull().sum())
print("\n📊 Kategori yang tersedia:")
print(df['Kategori'].value_counts())