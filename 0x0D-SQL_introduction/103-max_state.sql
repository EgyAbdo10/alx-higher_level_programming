-- max temperatures in states
SELECT state, max(value)
GROUP BY state
ORDER BY state