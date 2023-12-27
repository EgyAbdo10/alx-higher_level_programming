-- list non-genre shows
SELECT s.title, g.genre_id
FROM tv_show_genres AS g
RIGHT OUTER JOIN tv_shows AS s
ON g.show_id = s.id
WHERE g.genre_id IS NULL
ORDER BY s.title, g.genre_id ASC