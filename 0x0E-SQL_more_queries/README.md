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

[]()
