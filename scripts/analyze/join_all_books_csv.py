import pandas as pd

# Load all-genres csv
fantasy = pd.read_csv("data/booksdb_fantasy.csv")
history = pd.read_csv("data/booksdb_history.csv")
science_fiction = pd.read_csv("data/booksdb_science_fiction.csv")
romance = pd.read_csv("data/booksdb_romance.csv")

# Join
df = pd.concat([fantasy, history, science_fiction, romance], ignore_index=True)

# Pastikan semua 'Harga' udah dibersihkan dari simbol £ dan dikonversi ke float
for df_ in [fantasy, history, science_fiction, romance]:
    df_['Harga'] = df_['Harga'].astype(str).str.replace('£', '').astype(float)

print(df_['Harga'].unique())

# Export to csv
df.to_csv("data/booksdb_all_genres.csv", index=False)
print("booksdb_all_genre.csv siap digunakan buat analisis lanjutan!")
