import pandas as pd

# Load all-genres csv
fantasy = pd.read_csv("data/booksdb_fantasy.csv")
history = pd.read_csv("data/booksdb_history.csv")
scifi = pd.read_csv("data/booksdb_scifi.csv")
romance = pd.read_csv("data/booksdb_romance.csv")

# Join
df = pd.concat([fantasy, history, scifi, romance], ignore_index=True)

# Pastikan semua 'Harga' udah dibersihkan dari simbol £ dan dikonversi ke float
for df_ in [fantasy, history, scifi, romance]:
    df_['Harga'] = df_['Harga'].astype(str).str.replace('£', '').astype(float)

print(df_['Harga'].unique())

# Export to csv
df.to_csv("data/booksdb_all_genres.csv", index=False)
print("booksdb_all_genre.csv siap digunakan buat analisis lanjutan!")
