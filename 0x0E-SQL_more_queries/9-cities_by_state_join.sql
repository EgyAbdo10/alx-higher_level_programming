-- JOIN TABLES
SELECT c.id, c.name, s.name
FROM cities AS c
JOIN states AS s
ON c.id = s.id
ORDER BY c.id ASC