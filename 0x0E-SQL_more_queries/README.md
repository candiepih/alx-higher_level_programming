# SQL - More queries

Topics aim was to understand the following concepts:
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a `PRIMARY KEY`
* What’s a `FOREIGN KEY`
* How to use `NOT NULL` and `UNIQUE` constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are `JOIN` and `UNION`

The following task files were used to test my understanding on the above concepts

[0-privileges.sql](../0x0E-SQL_more_queries/0-privileges.sql)

script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2`

[1-create_user.sql](../0x0E-SQL_more_queries/1-create_user.sql)

script that creates the MySQL server user `user_0d_1`.

* `user_0d_1` should have all privileges on your MySQL server
* The `user_0d_1` password should be set to `user_0d_1_pwd`
* If the user `user_0d_1` already exists, your script should not fail

[2-create_read_user.sql](../0x0E-SQL_more_queries/2-create_read_user.sql)

script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

* `user_0d_2` should have only `SELECT` privilege in the database `hbtn_0d_2`
* The `user_0d_2` password should be set to `user_0d_2_pwd`
* If the database `hbtn_0d_2` already exists, your script should not fail
* If the user `user_0d_2` already exists, your script should not fail

[3-force_name.sql](../0x0E-SQL_more_queries/3-force_name.sql)

script that creates the table `force_name` on your MySQL server.

`force_name` description:

* `id` INT
* `name` VARCHAR(256) can’t be null

[4-never_empty.sql](../0x0E-SQL_more_queries/4-never_empty.sql)

script that creates the table `id_not_null` on your MySQL server.

`id_not_null` description:

* `id` INT with the default value 1
* `name` VARCHAR(256)

[5-unique_id.sql](../0x0E-SQL_more_queries/5-unique_id.sql)

script that creates the table `unique_id` on your MySQL server.

`unique_id` description:

* `id` INT with the default value 1 and must be unique
* `name` VARCHAR(256)

[6-states.sql](../0x0E-SQL_more_queries/6-states.sql)

script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`)

`states` description:
* `id` INT unique, auto generated, can’t be null and is a primary key
* `name` VARCHAR(256) can’t be null

[7-cities.sql](../0x0E-SQL_more_queries/7-cities.sql)

script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) 

`cities` description:

* `id` INT unique, auto generated, can’t be null and is a primary key
* `state_id` INT, can’t be null and must be a `FOREIGN KEY` that references to `id` of the states table
* `name` VARCHAR(256) can’t be null

[8-cities_of_california_subquery.sql](../0x0E-SQL_more_queries/8-cities_of_california_subquery.sql)

script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

* The states table contains only one record where `name = California` (but the `id` can be different, as per the example)
* Results must be sorted in ascending order by `cities.id`
* You are not allowed to use the `JOIN` keyword

[9-cities_by_state_join.sql](../0x0E-SQL_more_queries/9-cities_by_state_join.sql)

script that lists all cities contained in the database `hbtn_0d_usa`.

* Each record should display: `cities.id - cities.name - states.name`
* Results must be sorted in ascending order by `cities.id`
* Use only one `SELECT` statement

[10-genre_id_by_show.sql](../0x0E-SQL_more_queries/10-genre_id_by_show.sql)

Imports the database dump from `hbtn_0d_tvshows` to your MySQL server

