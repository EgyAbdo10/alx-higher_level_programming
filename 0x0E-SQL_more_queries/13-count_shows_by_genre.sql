-- count genres
SELECT g.name AS genre, count(g.name) AS number_of_shows
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg
ON sg.genre_id = g.id
LEFT JOIN tv_shows AS s
ON s.id = sg.show_id
GROUP BY g.name
ORDER BY number_of_shows DESC