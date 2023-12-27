-- comedy only shows
SELECT s.title
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg
ON sg.genre_id = g.id
RIGHT JOIN tv_shows AS s
ON s.id = sg.show_id
WHERE g.name = "Comedy"
ORDER BY s.title ASC