-- count genres
SELECT g.name AS genre, count(g.name) AS number_of_shows
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg
ON sg.genre_id = g.id
RIGHT JOIN tv_shows AS s
ON s.id = sg.show_id
WHERE g.name IS NOT NULL
GROUP BY g.name
ORDER BY number_of_shows DESC