---
description: >-
  This guide provides examples of frequent SQL patterns, such as finding maximum
  values, calculating averages, and using auto-increment columns.
---

# Commonly Used Queries

This page is intended to be a quick reference of commonly-used and/or useful queries in MariaDB.

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/G9gr3KMrlccJhmFh3SNT/" %}

## Creating a Table

```sql
CREATE TABLE t1 ( a INT );
CREATE TABLE t2 ( b INT );
CREATE TABLE student_tests (
 name CHAR(10), test CHAR(10), 
 score TINYINT, test_date DATE
);
```

See [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) for more.

## Inserting Records

```sql
INSERT INTO t1 VALUES (1), (2), (3);
INSERT INTO t2 VALUES (2), (4);

INSERT INTO student_tests 
 (name, test, score, test_date) VALUES
 ('Chun', 'SQL', 75, '2012-11-05'), 
 ('Chun', 'Tuning', 73, '2013-06-14'),
 ('Esben', 'SQL', 43, '2014-02-11'), 
 ('Esben', 'Tuning', 31, '2014-02-09'), 
 ('Kaolin', 'SQL', 56, '2014-01-01'),
 ('Kaolin', 'Tuning', 88, '2013-12-29'), 
 ('Tatiana', 'SQL', 87, '2012-04-28'), 
 ('Tatiana', 'Tuning', 83, '2013-09-30');
```

See [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) for more.

## Using AUTO\_INCREMENT

The AUTO\_INCREMENT attribute is used to automatically generate a unique identity for new rows.

```sql
CREATE TABLE student_details (
 id INT NOT NULL AUTO_INCREMENT, name CHAR(10), 
 date_of_birth DATE, PRIMARY KEY (id)
);
```

When inserting, the id field can be omitted, and is automatically created.

```sql
INSERT INTO student_details (name,date_of_birth) VALUES 
 ('Chun', '1993-12-31'), 
 ('Esben','1946-01-01'),
 ('Kaolin','1996-07-16'),
 ('Tatiana', '1988-04-13');

SELECT * FROM student_details;
+----+---------+---------------+
| id | name    | date_of_birth |
+----+---------+---------------+
|  1 | Chun    | 1993-12-31    |
|  2 | Esben   | 1946-01-01    |
|  3 | Kaolin  | 1996-07-16    |
|  4 | Tatiana | 1988-04-13    |
+----+---------+---------------+
```

See [AUTO\_INCREMENT](../../reference/data-types/auto_increment.md) for more.

## Querying from two tables on a common value

```sql
SELECT * FROM t1 INNER JOIN t2 ON t1.a = t2.b;
```

This kind of query is called a join - see [JOINS](../../reference/sql-statements/data-manipulation/selecting-data/joins/) for more.

## Finding the Maximum Value

```sql
SELECT MAX(a) FROM t1;
+--------+
| MAX(a) |
+--------+
|      3 |
+--------+
```

See the [MAX() function](../../reference/sql-functions/aggregate-functions/max.md) for more, as well as [Finding the maximum value and grouping the results](mariadb-advanced-sql-guide-1.md#finding-the-maximum-value-and-grouping-the-results) below for a more practical example.

## Finding the Minimum Value

```sql
SELECT MIN(a) FROM t1;
+--------+
| MIN(a) |
+--------+
|      1 |
+--------+
```

See the [MIN() function](../../reference/sql-functions/aggregate-functions/min.md) for more.

## Finding the Average Value

```sql
SELECT AVG(a) FROM t1;
+--------+
| AVG(a) |
+--------+
| 2.0000 |
+--------+
```

See the [AVG() function](../../reference/sql-functions/aggregate-functions/avg.md) for more.

## Finding the Maximum Value and Grouping the Results

```sql
SELECT name, MAX(score) FROM student_tests GROUP BY name;
+---------+------------+
| name    | MAX(score) |
+---------+------------+
| Chun    |         75 |
| Esben   |         43 |
| Kaolin  |         88 |
| Tatiana |         87 |
+---------+------------+
```

See the [MAX() function](../../reference/sql-functions/aggregate-functions/max.md) for more.

## Ordering Results

```sql
SELECT name, test, score FROM student_tests ORDER BY score DESC;
+---------+--------+-------+
| name    | test   | score |
+---------+--------+-------+
| Kaolin  | Tuning |    88 |
| Tatiana | SQL    |    87 |
| Tatiana | Tuning |    83 |
| Chun    | SQL    |    75 |
| Chun    | Tuning |    73 |
| Kaolin  | SQL    |    56 |
| Esben   | SQL    |    43 |
| Esben   | Tuning |    31 |
+---------+--------+-------+
```

See [ORDER BY](../../reference/sql-statements/data-manipulation/selecting-data/order-by.md) for more.

## Finding the Row with the Minimum of a Particular Column

In this example, we want to find the lowest test score for any student.

```sql
SELECT name,test, score FROM student_tests WHERE score=(SELECT MIN(score) FROM student);
+-------+--------+-------+
| name  | test   | score |
+-------+--------+-------+
| Esben | Tuning |    31 |
+-------+--------+-------+
```

## Finding Rows with the Maximum Value of a Column by Group

This example returns the best test results of each student:

```sql
SELECT name, test, score FROM student_tests st1 WHERE score = (
  SELECT MAX(score) FROM student st2 WHERE st1.name = st2.name
); 
+---------+--------+-------+
| name    | test   | score |
+---------+--------+-------+
| Chun    | SQL    |    75 |
| Esben   | SQL    |    43 |
| Kaolin  | Tuning |    88 |
| Tatiana | SQL    |    87 |
+---------+--------+-------+
```

## Calculating Age

The [TIMESTAMPDIFF](../../reference/sql-functions/date-time-functions/timestampdiff.md) function can be used to calculate someone's age:

```sql
SELECT CURDATE() AS today;
+------------+
| today      |
+------------+
| 2014-02-17 |
+------------+

SELECT name, date_of_birth, TIMESTAMPDIFF(YEAR,date_of_birth,'2014-08-02') AS age 
  FROM student_details;
+---------+---------------+------+
| name    | date_of_birth | age  |
+---------+---------------+------+
| Chun    | 1993-12-31    |   20 |
| Esben   | 1946-01-01    |   68 |
| Kaolin  | 1996-07-16    |   18 |
| Tatiana | 1988-04-13    |   26 |
+---------+---------------+------+
```

See [TIMESTAMPDIFF()](../../reference/sql-functions/date-time-functions/timestampdiff.md) for more.

## Using User-defined Variables

This example sets a [user-defined variable](../../reference/sql-structure/sql-language-structure/user-defined-variables.md) with the average test score, and then uses it in a later query to return all results above the average.

```sql
SELECT @avg_score:= AVG(score) FROM student_tests;
+-------------------------+
| @avg_score:= AVG(score) |
+-------------------------+
|            67.000000000 |
+-------------------------+

SELECT * FROM student_tests WHERE score > @avg_score;
+---------+--------+-------+------------+
| name    | test   | score | test_date  |
+---------+--------+-------+------------+
| Chun    | SQL    |    75 | 2012-11-05 |
| Chun    | Tuning |    73 | 2013-06-14 |
| Kaolin  | Tuning |    88 | 2013-12-29 |
| Tatiana | SQL    |    87 | 2012-04-28 |
| Tatiana | Tuning |    83 | 2013-09-30 |
+---------+--------+-------+------------+
```

User-defined variables can also be used to add an incremental counter to a resultset:

```sql
SET @count = 0;

SELECT @count := @count + 1 AS counter, name, date_of_birth FROM student_details;
+---------+---------+---------------+
| counter | name    | date_of_birth |
+---------+---------+---------------+
|       1 | Chun    | 1993-12-31    |
|       2 | Esben   | 1946-01-01    |
|       3 | Kaolin  | 1996-07-16    |
|       4 | Tatiana | 1988-04-13    |
+---------+---------+---------------+
```

See [User-defined Variables](../../reference/sql-structure/sql-language-structure/user-defined-variables.md) for more.

## View Tables in Order of Size

Returns a list of all tables in the database, ordered by size:

```sql
SELECT table_schema AS `DB`, table_name AS `TABLE`, 
  ROUND(((data_length + index_length) / 1024 / 1024), 2) `Size (MB)` 
  FROM information_schema.TABLES 
  ORDER BY (data_length + index_length) DESC;

+--------------------+---------------------------------------+-----------+
| DB                 | Table                                 | Size (MB) |
+--------------------+---------------------------------------+-----------+
| wordpress          | wp_simple_history_contexts            |      7.05 |
| wordpress          | wp_posts                              |      6.59 |
| wordpress          | wp_simple_history                     |      3.05 |
| wordpress          | wp_comments                           |      2.73 |
| wordpress          | wp_commentmeta                        |      2.47 |
| wordpress          | wp_simple_login_log                   |      2.03 |
...
```

## Removing Duplicates

This example assumes there's a unique ID, but that all other fields are identical. In the example below, there are 4 records, 3 of which are duplicates, so two of the three duplicates need to be removed. The intermediate SELECT is not necessary, but demonstrates what is being returned.

```sql
CREATE TABLE t (id INT, f1 VARCHAR(2));

INSERT INTO t VALUES (1,'a'), (2,'a'), (3,'b'), (4,'a');

SELECT * FROM t t1, t t2 WHERE t1.f1=t2.f1 AND t1.id<>t2.id AND t1.id=(
  SELECT MAX(id) FROM t tab WHERE tab.f1=t1.f1
);
+------+------+------+------+
| id   | f1   | id   | f1   |
+------+------+------+------+
|    4 | a    |    1 | a    |
|    4 | a    |    2 | a    |
+------+------+------+------+

DELETE FROM t WHERE id IN (
  SELECT t2.id FROM t t1, t t2 WHERE t1.f1=t2.f1 AND t1.id<>t2.id AND t1.id=(
    SELECT MAX(id) FROM t tab WHERE tab.f1=t1.f1
  )
);
Query OK, 2 rows affected (0.120 sec)

SELECT * FROM t;
+------+------+
| id   | f1   |
+------+------+
|    3 | b    |
|    4 | a    |
+------+------
```

CC BY-SA / Gnu FDL
