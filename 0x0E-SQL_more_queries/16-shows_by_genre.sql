-- show by genre
SELECT s.title, g.name
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg
ON sg.genre_id = g.id
RIGHT OUTER JOIN tv_shows AS s
ON s.id = sg.show_id
ORDER BY s.title ASC