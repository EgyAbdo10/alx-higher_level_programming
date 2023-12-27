-- list all shows
SELECT s.title, g.genre_id
FROM tv_show_genres AS g
RIGHT OUTER JOIN tv_shows AS s
ON g.show_id = s.id
ORDER BY s.title, g.genre_id ASC