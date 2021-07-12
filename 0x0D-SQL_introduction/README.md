# SQL - Introduction

Topics aim was to understand SQL(Structured Query Language) and understanding concepts like:-

* What is Database & SQL?
* Basic SQL statements: DDL and DML
* Basic queries: SQL and RA
* SQL technique: functions
* SQL technique: subqueries
* What makes the big difference between a backtick and an apostrophe?
* MySQL 5.7 SQL Statement Syntax

The following files were used to test my understanding of the various concepts

[0-list_databases.sql](../0x0D-SQL_introduction/0-list_databases.sql)

script that lists all databases of MySQL server.

[1-create_database_if_missing.sql](../0x0D-SQL_introduction/1-create_database_if_missing.sql)

script that creates the database `hbtn_0c_0` in MySQL server.

[2-remove_database.sql](../0x0D-SQL_introduction/2-remove_database.sql)

script that deletes the database hbtn_0c_0 in MySQL server.

[3-list_tables.sql](../0x0D-SQL_introduction/3-list_tables.sql)

script that lists all the tables of a database in MySQL server.

[4-first_table.sql](../0x0D-SQL_introduction/4-first_table.sql)

script that creates a table called `first_table` in the current database in MySQL server.

`first_table` description:
* `id` INT
* `name` VARCHAR(256)

[5-full_table.sql](../0x0D-SQL_introduction/5-full_table.sql)

script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in MySQL server

[6-list_values.sql](../0x0D-SQL_introduction/6-list_values.sql)

script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in MySQL server.

[7-insert_value.sql](../0x0D-SQL_introduction/7-insert_value.sql)

script that inserts a new row in the table `first_table` (database hbtn_0c_0) in MySQL server.

New row
* `id = 89`
* `name = Holberton School`

[8-count_89.sql](../0x0D-SQL_introduction/8-count_89.sql)

script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in MySQL server.

[9-full_creation.sql](../0x0D-SQL_introduction/9-full_creation.sql)

script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.

`second_table` description:

* `id` INT
* `name` VARCHAR(256)
* `score` INT

* The database name will be passed as an argument to the `mysql` command
* If the table `second_table` already exists, script should not fail

script creates these records:

* `id` = 1, `name` = “John”, `score` = 10
* `id` = 2, `name` = “Alex”, `score` = 3
* `id` = 3, `name` = “Bob”, `score` = 14
* `id` = 4, `name` = “George”, `score` = 8

[10-top_score.sql](../0x0D-SQL_introduction/10-top_score.sql)

script that lists all records of the table `second_table` of the database `hbtn_0c_0` in MySQL server.

[11-best_score.sql](../0x0D-SQL_introduction/11-best_score.sql)

script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in MySQL server

[12-no_cheating.sql](../0x0D-SQL_introduction/12-no_cheating.sql)

script that updates the score of Bob to `10` in the table `second_table`.
* not allowed to use Bob’s id value, only the  `name` field

[13-change_class.sql](../main/0x0D-SQL_introduction/13-change_class.sql)

script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in MySQL server

[14-average.sql](../0x0D-SQL_introduction/14-average.sql)

script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in MySQL server

[15-groups.sql](../0x0D-SQL_introduction/15-groups.sql)

script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in MySQL server.

[16-no_link.sql](../0x0D-SQL_introduction/16-no_link.sql)

script that lists all records of the table `second_table` of the database `hbtn_0c_0` in MySQL server

[100-move_to_utf8.sql](../0x0D-SQL_introduction/100-move_to_utf8.sql)

script that converts `hbtn_0c_0` database to `UTF8 (utf8mb4, collate utf8mb4_unicode_ci)` in MySQL server.

* Database `hbtn_0c_0`
* Table `first_table`
* Field `name` in `first_table`

[]()
