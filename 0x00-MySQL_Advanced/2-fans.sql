-- Task: Aggregate fan counts per country and rank the country origins based on the total number of fans

-- Create a temporary table to store the aggregated fan counts per country
CREATE TEMPORARY TABLE temp_fan_counts AS
SELECT origin, SUM(nb_fans) AS total_fans
FROM metal_bands
GROUP BY origin;

-- Rank the country origins based on the total number of fans
SELECT origin, total_fans
FROM temp_fan_counts
ORDER BY total_fans DESC;

