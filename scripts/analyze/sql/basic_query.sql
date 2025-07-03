-- SQLite

-- Buku yang harganya diatas 50 Euro
SELECT *
FROM all_genres
WHERE Harga > 50
ORDER BY Harga DESC;

-- Total Buku
SELECT COUNT(*) AS Jumlah_Magic
FROM all_genres
WHERE Keyword_Magic = 1;

-- Rata-rata harga per genre
SELECT Kategori, ROUND(AVG(Harga), 2) AS Rata2_Harga_in_€,
COUNT(*) AS Jumlah_buku_per_Kategori
FROM all_genres
GROUP BY Kategori;

-- 5 Buku termahal dengan keyword Love
SELECT *
FROM romance
WHERE Keyword_Love=1
ORDER BY Harga DESC
LIMIT  5;

-- Kategori dengan harga buku termahal
SELECT Kategori, ROUND(AVG(Harga), 2) AS Avg_Harga
FROM all_genres
GROUP BY Kategori
ORDER BY 2 DESC
LIMIT 3;
