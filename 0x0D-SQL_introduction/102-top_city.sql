-- top cities in temperatures
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 8 OR month = 7
GROUP BY city
ORDER BY AVG(value) DESC
limit 3;