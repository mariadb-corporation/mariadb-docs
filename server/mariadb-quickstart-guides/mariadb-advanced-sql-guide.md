---
description: >-
  Learn how to perform essential SQL operations such as creating tables,
  inserting data, and using aggregate functions like MAX, MIN, and AVG.
---

# Essential Queries Guide

The Essential Queries Guide offers a concise collection of commonly-used SQL queries. It's designed to help developers and database administrators quickly find syntax and examples for typical database operations, from table creation and data insertion to effective data retrieval and manipulation.

### Creating a Table

To create new tables:

```sql
CREATE TABLE t1 ( a INT );
```

```sql
CREATE TABLE t2 ( b INT );
```

```sql
CREATE TABLE student_tests (
 name CHAR(10), test CHAR(10),
 score TINYINT, test_date DATE
);
```

For more details, see the official [CREATE TABLE](../reference/sql-statements/data-definition/create/create-table.md) documentation.

### Inserting Records

To add data into your tables:

```sql
INSERT INTO t1 VALUES (1), (2), (3);
```

```sql
INSERT INTO t2 VALUES (2), (4);
```

```sql
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

For more information, see the official INSERT documentation.

### Using AUTO\_INCREMENT

The `AUTO_INCREMENT` attribute automatically generates a unique identity for new rows.

Create a table with an `AUTO_INCREMENT` column:

```sql
CREATE TABLE student_details (
 id INT NOT NULL AUTO_INCREMENT, name CHAR(10),
 date_of_birth DATE, PRIMARY KEY (id)
);
```

When inserting, omit the `id` field; it will be automatically generated:

```sql
INSERT INTO student_details (name,date_of_birth) VALUES
 ('Chun', '1993-12-31'),
 ('Esben','1946-01-01'),
 ('Kaolin','1996-07-16'),
 ('Tatiana', '1988-04-13');
```

Verify the inserted records:

```sql
SELECT * FROM student_details;
```

```sql
+----+---------+---------------+
| id | name    | date_of_birth |
+----+---------+---------------+
|  1 | Chun    | 1993-12-31    |
|  2 | Esben   | 1946-01-01    |
|  3 | Kaolin  | 1996-07-16    |
|  4 | Tatiana | 1988-04-13    |
+----+---------+---------------+
```

For more details, see the [AUTO\_INCREMENT](../reference/data-types/auto_increment.md) documentation.

### Querying from two tables on a common value (JOIN)

To combine rows from two tables based on a related column:

```sql
SELECT * FROM t1 INNER JOIN t2 ON t1.a = t2.b;
```

This type of query is a join. For more details, consult the documentation on [JOINS](../reference/sql-statements/data-manipulation/selecting-data/joins/).

### Finding the Maximum Value

To find the maximum value in a column:

```sql
SELECT MAX(a) FROM t1;
```

```sql
+--------+
| MAX(a) |
+--------+
|      3 |
+--------+
```

See the [MAX() function](../reference/sql-functions/aggregate-functions/max.md) documentation. For a grouped example, refer to _Finding the Maximum Value and Grouping the Results_ below.

### Finding the Minimum Value

To find the minimum value in a column:

```sql
SELECT MIN(a) FROM t1;
```

```sql
+--------+
| MIN(a) |
+--------+
|      1 |
+--------+
```

See the MIN() function documentation.

### Finding the Average Value

To calculate the average value of a column:

```sql
SELECT AVG(a) FROM t1;
```

```
+--------+
| AVG(a) |
+--------+
| 2.0000 |
+--------+
```

See the [AVG() function](../reference/sql-functions/aggregate-functions/avg.md) documentation.

### Finding the Maximum Value and Grouping the Results

To find the maximum value within groups:

```sql
SELECT name, MAX(score) FROM student_tests GROUP BY name;
```

```sql
+---------+------------+
| name    | MAX(score) |
+---------+------------+
| Chun    |         75 |
| Esben   |         43 |
| Kaolin  |         88 |
| Tatiana |         87 |
+---------+------------+
```

Further details are available in the MAX() function documentation.

### Ordering Results

To sort your query results (e.g., in descending order):

```sql
SELECT name, test, score FROM student_tests 
 ORDER BY score DESC; -- Use ASC for ascending order
```

```sql
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

For more options, see the [ORDER BY](../reference/sql-statements/data-manipulation/selecting-data/order-by.md) documentation.

### Finding the Row with the Minimum of a Particular Column

To find the entire row containing the minimum value of a specific column across all records:

```sql
SELECT name, test, score FROM student_tests 
 WHERE score = (SELECT MIN(score) FROM student_tests);
```

```sql
+-------+--------+-------+
| name  | test   | score |
+-------+--------+-------+
| Esben | Tuning |    31 |
+-------+--------+-------+
```

### Finding Rows with the Maximum Value of a Column by Group

To retrieve the full record for the maximum value within each group (e.g., highest score per student):

```sql
SELECT name, test, score FROM student_tests st1
 WHERE score = (SELECT MAX(st2.score) FROM student_tests st2 WHERE st1.name = st2.name);
```

```sql
+---------+--------+-------+
| name    | test   | score |
+---------+--------+-------+
| Chun    | SQL    |    75 |
| Esben   | SQL    |    43 |
| Kaolin  | Tuning |    88 |
| Tatiana | SQL    |    87 |
+---------+--------+-------+
```

### Calculating Age

Use the `TIMESTAMPDIFF` function to calculate age from a birth date.

To see the current date (optional, for reference):

```sql
SELECT CURDATE() AS today;
```

```sql
+------------+
| today      |
+------------+
| 2014-02-17 | -- Example output; actual date will vary
+------------+
```

To calculate age as of a specific date (e.g., '2014-08-02'):

```sql
SELECT name, date_of_birth, TIMESTAMPDIFF(YEAR, date_of_birth, '2014-08-02') AS age
  FROM student_details;
```

```sql
+---------+---------------+------+
| name    | date_of_birth | age  |
+---------+---------------+------+
| Chun    | 1993-12-31    |   20 |
| Esben   | 1946-01-01    |   68 |
| Kaolin  | 1996-07-16    |   18 |
| Tatiana | 1988-04-13    |   26 |
+---------+---------------+------+
```

To calculate current age, replace the specific date string (e.g., '2014-08-02') with CURDATE().

See the [TIMESTAMPDIFF()](../reference/sql-functions/date-time-functions/timestampdiff.md) documentation for more.

### Using User-defined Variables

[User-defined variables ](../reference/sql-structure/sql-language-structure/user-defined-variables.md)can store values for use in subsequent queries within the same session.

Example: Set a variable for the average score and use it to filter results.

```sql
SELECT @avg_score := AVG(score) FROM student_tests;
```

```
+-------------------------+
| @avg_score:= AVG(score) |
+-------------------------+
|            67.000000000 |
+-------------------------+
```

```sql
SELECT * FROM student_tests WHERE score > @avg_score;
```

```sql
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

Example: Add an incremental counter to a result set.

```sql
SET @count = 0;
```

```sql
SELECT @count := @count + 1 AS counter, name, date_of_birth FROM student_details;
```

```sql
+---------+---------+---------------+
| counter | name    | date_of_birth |
+---------+---------+---------------+
|       1 | Chun    | 1993-12-31    |
|       2 | Esben   | 1946-01-01    |
|       3 | Kaolin  | 1996-07-16    |
|       4 | Tatiana | 1988-04-13    |
+---------+---------+---------------+
```

See [User-defined Variables](../reference/sql-structure/sql-language-structure/user-defined-variables.md) for more.

### View Tables in Order of Size

To list all tables in the current database, ordered by their size (data + index) in megabytes:

```sql
SELECT table_schema AS `DB`, table_name AS `TABLE`,
  ROUND(((data_length + index_length) / 1024 / 1024), 2) `Size (MB)`
  FROM information_schema.TABLES
  WHERE table_schema = DATABASE() -- This clause restricts results to the current database
  ORDER BY (data_length + index_length) DESC;
```

```sql
+--------------------+---------------------------------------+-----------+
| DB                 | Table                                 | Size (MB) | -- Example Output
+--------------------+---------------------------------------+-----------+
| your_db_name       | some_large_table                      |      7.05 |
| your_db_name       | another_table                         |      6.59 |
...
+--------------------+---------------------------------------+-----------+
```

### Removing Duplicates

To remove duplicate rows based on specific column values, while keeping one instance (e.g., the instance with the highest `id`).

This example assumes `id` is a unique primary key and duplicates are identified by the values in column `f1`. It keeps the row with the maximum `id` for each distinct `f1` value.

Setup sample table and data:

```sql
CREATE TABLE t (id INT, f1 VARCHAR(2));
```

```sql
INSERT INTO t VALUES (1,'a'), (2,'a'), (3,'b'), (4,'a');
```

To delete duplicate rows, keeping the one with the highest `id` for each group of `f1` values:

```sql
DELETE t_del FROM t AS t_del
INNER JOIN (
    SELECT f1, MAX(id) AS max_id
    FROM t
    GROUP BY f1
    HAVING COUNT(*) > 1 -- Identify groups with actual duplicates
) AS t_keep ON t_del.f1 = t_keep.f1 AND t_del.id < t_keep.max_id;
```

This query targets rows for deletion (`t_del`) where their `f1` value matches an `f1` in a subquery (`t_keep`) that has duplicates, and their `id` is less than the maximum `id` found for that `f1` group.

Verify results after deletion:

```sql
SELECT * FROM t;
```

```sql
+------+------+
| id   | f1   |
+------+------+
|    3 | b    |
|    4 | a    |
+------+------+
```

***

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
