import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DB_PATH = "books.db"
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def analyze_top5_per_genre():
    conn = sqlite3.connect(DB_PATH)

    genres = pd.read_sql("SELECT DISTINCT Kategori FROM all_genres", conn)['Kategori'].tolist()

    for genre in genres:
        query = f"""
        SELECT Judul, Harga 
        FROM all_genres 
        WHERE Kategori = '{genre}' 
        ORDER BY Harga DESC 
        LIMIT 5
        """
        df = pd.read_sql(query, conn)

        plt.figure(figsize=(10, 5))
        sns.barplot(data=df, x="Harga", y="Judul", palette="rocket")
        plt.title(f"Top 5 Buku Termahal - {genre}")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f"top5_{genre.lower().replace(' ', '_')}.png")
        print(f"Saved top 5 chart for {genre}")

    conn.close()

def price_stats_per_genre():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT 
        Kategori, 
        COUNT(*) AS Jumlah_Buku,
        ROUND(AVG(Harga), 2) AS Rata2_Harga,
        ROUND(MIN(Harga), 2) AS Harga_Termurah,
        ROUND(MAX(Harga), 2) AS Harga_Termahal
    FROM all_genres
    GROUP BY Kategori
    ORDER BY Rata2_Harga DESC
    """
    
    df = pd.read_sql(query, conn)
    print("\n📊 Statistik Harga per Genre:")
    print(df.to_string(index=False))

    # Optional visual
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="Rata2_Harga", y="Kategori", palette="crest")
    plt.title("📈 Rata-rata Harga Buku per Genre")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "avg_price_per_genre.png")
    print("✅ Saved: avg_price_per_genre.png")

    conn.close()

def keyword_stats_per_genre():
    conn = sqlite3.connect(DB_PATH)

    # Ambil semua kolom keyword
    df = pd.read_sql("SELECT * FROM all_genres", conn)
    keyword_cols = [col for col in df.columns if col.startswith("Keyword_")]

    # Transformasi long-form
    melted = df.melt(id_vars=["Kategori"], value_vars=keyword_cols, 
                     var_name="Keyword", value_name="Ada")

    melted = melted[melted["Ada"] == True]

    keyword_counts = (
        melted.groupby(["Kategori", "Keyword"])
        .size()
        .reset_index(name="Jumlah")
        .sort_values(by=["Kategori", "Jumlah"], ascending=[True, False])
    )

    print("\nFrekuensi Keyword per Genre:")
    print(keyword_counts.to_string(index=False))

    # Visualisasi
    plt.figure(figsize=(12, 6))
    sns.barplot(data=keyword_counts, x="Keyword", y="Jumlah", hue="Kategori")
    plt.title("Frekuensi Kata Kunci per Genre")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "keyword_freq_per_genre.png")
    print("Saved: keyword_freq_per_genre.png")

    conn.close()

if __name__ == "__main__":
    analyze_top5_per_genre()
    price_stats_per_genre()
    keyword_stats_per_genre()