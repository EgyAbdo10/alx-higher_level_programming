-- list records
SELECT s.title, g.genre_id
FROM tv_show_genres AS g
LEFT JOIN tv_shows AS s
ON g.show_id = s.id
ORDER BY s.title, g.genre_id ASC