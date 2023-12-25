-- top cities in temperatures
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC
WHERE month = 8 OR month = 7