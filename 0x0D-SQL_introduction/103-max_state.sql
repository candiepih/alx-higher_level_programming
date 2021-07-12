-- Imports in `hbtn_0c_0` database table dump from file
-- and finds maximum average temparature depending on state
SELECT state, MAX(value) AS max_temp FROM `temperatures`
GROUP BY state ORDER BY state;
