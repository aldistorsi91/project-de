import pandas as pd

# Load only clean + enriched files
fantasy = pd.read_csv("books_fantasy_enriched.csv")
history = pd.read_csv("books_history_enriched.csv")
scifi = pd.read_csv("books_scifi.csv")
romance = pd.read_csv("books_romance.csv")

# Join
df = pd.concat([fantasy, history, scifi, romance], ignore_index=True)

# Pastikan semua 'Harga' udah dibersihkan dari simbol £ dan dikonversi ke float
for df_ in [fantasy, history, scifi, romance]:
    df_['Harga'] = df_['Harga'].astype(str).str.replace('£', '').astype(float)

print(df_['Harga'].unique())

# Export to csv
df.to_csv("books_all_genres.csv", index=False)
print("✅ books_all_genres.csv siap digunakan buat analisis lanjutan!")
