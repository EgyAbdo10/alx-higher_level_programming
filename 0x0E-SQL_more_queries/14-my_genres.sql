-- list dexter
SELECT g.name
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg
ON sg.genre_id = g.id
LEFT JOIN tv_shows AS s
ON s.id = sg.show_id
WHERE s.title = "Dexter"
ORDER BY g.name ASC