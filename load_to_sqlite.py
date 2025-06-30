import os
import pandas as pd
import sqlite3

DATA_DIR = "data"
DB_PATH = "books.db"

# Buat koneksi ke SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Loop semua file csv di folder data
for file in os.listdir(DATA_DIR):
    if file.endswith(".csv"):
        genre_name = file.replace("booksdb_", "").replace(".csv", "")
        print(f"📥 Memuat data: {file} -> tabel: {genre_name}")

        df = pd.read_csv(os.path.join(DATA_DIR, file))
        df.to_sql(genre_name, conn, if_exists="replace", index=False)

print("Semua data sudah dimasukkan ke dalam database SQLite.")
conn.close()