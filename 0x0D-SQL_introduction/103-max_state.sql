-- max temperatures in states
SELECT state, max(value) AS max_temp
GROUP BY state
ORDER BY state