-- SQLite
SELECT Kategori, ROUND(AVG(Harga), 2) AS Rata_Harga
FROM all_genres
GROUP BY Kategori
ORDER BY Rata_Harga DESC;

SELECT 
  Kategori,
  SUM(Keyword_Magic) AS Magic,
  SUM(Keyword_War) AS War,
  SUM(Keyword_Love) AS Love
FROM all_genres
GROUP BY Kategori;

SELECT Kategori, Judul, MAX(Judul_Length) AS Panjang
FROM all_genres
GROUP BY Kategori;

SELECT Kategori, COUNT(*) AS Jumlah_Series
FROM all_genres
WHERE Is_Series = 1
GROUP BY Kategori;