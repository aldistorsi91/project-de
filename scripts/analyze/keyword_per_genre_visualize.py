import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV gabungan
df = pd.read_csv("data/booksdb_all_genres.csv")

# Ambil kolom keyword
keyword_cols = [col for col in df.columns if col.startswith("Keyword_")]

# Buat kombinasi semua genre x keyword
all_combinations = pd.MultiIndex.from_product(
    [df["Kategori"].unique(), keyword_cols],
    names=["Kategori", "Keyword"]
).to_frame(index=False)

# Ubah data jadi long format untuk hitung
melted = df.melt(id_vars=["Kategori"], value_vars=keyword_cols,
                 var_name="Keyword", value_name="Ada")
melted = melted[melted["Ada"] == True]

# Hitung keyword yang muncul
keyword_counts = (
    melted.groupby(["Kategori", "Keyword"])
    .size()
    .reset_index(name="Jumlah")
)

# Merge untuk masukkan keyword yang 0 juga
keyword_counts = pd.merge(all_combinations, keyword_counts,
                          on=["Kategori", "Keyword"], how="left").fillna(0)
keyword_counts["Jumlah"] = keyword_counts["Jumlah"].astype(int)

# Rapihin nama keyword biar enak dibaca
keyword_counts["Keyword"] = keyword_counts["Keyword"].str.replace("Keyword_", "").str.capitalize()

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=keyword_counts, x="Keyword", y="Jumlah", hue="Kategori", palette="Set2")
plt.title("Frekuensi Keyword per Genre")
plt.xlabel("Keyword")
plt.ylabel("Jumlah Kemunculan")
plt.legend(title="Genre", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=0, ha='center')
plt.tight_layout()

# Simpan
plt.savefig("output/keyword_per_genre_full.png")
plt.show()