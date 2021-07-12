-- Imports in `hbtn_0c_0` database table dump from file
-- and finds
SET autocommit=0; source temperatures.sql; COMMIT;
SELECT city, AVG(value) AS avg_temp FROM `temperatures`
GROUP BY city ORDER BY avg_temp DESC;
