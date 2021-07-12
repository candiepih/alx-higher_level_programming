-- Imports in `hbtn_0c_0` database table dump from file
-- and finds
SET autocommit=0; source temperatures.sql; COMMIT;
SELECT state, MAX(value) AS max_temp FROM `temperatures`
GROUP BY state ORDER BY state;
