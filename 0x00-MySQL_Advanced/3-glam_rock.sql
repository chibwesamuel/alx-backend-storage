-- Create a temporary table to compute the lifespan
CREATE TEMPORARY TABLE temp_bands AS
SELECT band_name, 
       YEAR('2022-01-01') - YEAR(formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';

-- List the bands ranked by longevity
SELECT band_name, lifespan
FROM temp_bands
ORDER BY lifespan DESC;
