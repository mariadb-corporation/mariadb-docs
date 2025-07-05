
# Window Functions Overview


## Introduction


Window functions allow calculations to be performed across a set of rows related to the current row.


### Syntax


```
function (expression) OVER (
  [ PARTITION BY expression_list ]
  [ ORDER BY order_list [ frame_clause ] ] ) 

function:
  A valid window function

expression_list:
  expression | column_name [, expr_list ]

order_list:
  expression | column_name [ ASC | DESC ] 
  [, ... ]

frame_clause:
  {ROWS | RANGE} {frame_border | BETWEEN frame_border AND frame_border}

frame_border:
  | UNBOUNDED PRECEDING
  | UNBOUNDED FOLLOWING
  | CURRENT ROW
  | expr PRECEDING
  | expr FOLLOWING
```

### Description


Window functions perform calculations across a set of rows (in a defined window).


Dedicated window functions include


* [CUME_DIST](cume_dist.md)
* [DENSE_RANK](dense_rank.md)
* [FIRST_VALUE](first_value.md)
* [LAG](lag.md)
* [LAST_VALUE](../../secondary-functions/information-functions/last_value.md)
* [LEAD](lead.md)
* [MEDIAN](median.md)
* [NTH_VALUE](nth_value.md)
* [NTILE](ntile.md)
* [PERCENT_RANK](percent_rank.md)
* [PERCENTILE_CONT](percentile_cont.md)
* [PERCENTILE_DISC](percentile_disc.md)
* [RANK](rank.md), [ROW_NUMBER](row_number.md)


[Aggregate functions](../../aggregate-functions/README.md) that can also be used as window functions include


* [AVG](../../aggregate-functions/avg.md)
* [BIT_AND](../../aggregate-functions/bit_and.md)
* [BIT_OR](../../aggregate-functions/bit_or.md)
* [BIT_XOR](../../aggregate-functions/bit_xor.md)
* [COUNT](../../aggregate-functions/count.md)
* [MAX](../../aggregate-functions/max.md)
* [MIN](../../aggregate-functions/min.md)
* [STD](../../aggregate-functions/std.md)
* [STDDEV](../../aggregate-functions/stddev.md)
* [STDDEV_POP](../../aggregate-functions/stddev_pop.md)
* [STDDEV_SAMP](../../aggregate-functions/stddev_samp.md)
* [SUM](../../aggregate-functions/sum.md)
* [VAR_POP](../../aggregate-functions/var_pop.md)
* [VAR_SAMP](../../aggregate-functions/var_samp.md)
* [VARIANCE](../../aggregate-functions/variance.md)


Window function queries are characterised by the OVER keyword, following which the set of rows used for the calculation is specified. By default, the set of rows used for the calculation (the "window) is the entire dataset, which can be ordered with the ORDER BY clause. The PARTITION BY clause is used to reduce the window to a particular group within the dataset.


For example, given the following data:


```
CREATE TABLE student (name CHAR(10), test CHAR(10), score TINYINT); 

INSERT INTO student VALUES 
  ('Chun', 'SQL', 75), ('Chun', 'Tuning', 73), 
  ('Esben', 'SQL', 43), ('Esben', 'Tuning', 31), 
  ('Kaolin', 'SQL', 56), ('Kaolin', 'Tuning', 88), 
  ('Tatiana', 'SQL', 87), ('Tatiana', 'Tuning', 83);
```

the following two queries return the average partitioned by test and by name respectively:


```
SELECT name, test, score, AVG(score) OVER (PARTITION BY test) 
  AS average_by_test FROM student;
+---------+--------+-------+-----------------+
| name    | test   | score | average_by_test |
+---------+--------+-------+-----------------+
| Chun    | SQL    |    75 |         65.2500 |
| Chun    | Tuning |    73 |         68.7500 |
| Esben   | SQL    |    43 |         65.2500 |
| Esben   | Tuning |    31 |         68.7500 |
| Kaolin  | SQL    |    56 |         65.2500 |
| Kaolin  | Tuning |    88 |         68.7500 |
| Tatiana | SQL    |    87 |         65.2500 |
| Tatiana | Tuning |    83 |         68.7500 |
+---------+--------+-------+-----------------+

SELECT name, test, score, AVG(score) OVER (PARTITION BY name) 
  AS average_by_name FROM student;
+---------+--------+-------+-----------------+
| name    | test   | score | average_by_name |
+---------+--------+-------+-----------------+
| Chun    | SQL    |    75 |         74.0000 |
| Chun    | Tuning |    73 |         74.0000 |
| Esben   | SQL    |    43 |         37.0000 |
| Esben   | Tuning |    31 |         37.0000 |
| Kaolin  | SQL    |    56 |         72.0000 |
| Kaolin  | Tuning |    88 |         72.0000 |
| Tatiana | SQL    |    87 |         85.0000 |
| Tatiana | Tuning |    83 |         85.0000 |
+---------+--------+-------+-----------------+
```

It is also possible to specify which rows to include for the window function (for example, the current row and all preceding rows). See [Window Frames](window-frames.md) for more details.


## Scope


Window functions were introduced in SQL:2003, and their definition was expanded in subsequent versions of the standard. The last expansion was in the latest version of the standard, SQL:2011.


Most database products support a subset of the standard, they implement some functions defined as late as in SQL:2011, and at the same time leave some parts of SQL:2008 unimplemented.


MariaDB:


* Supports ROWS and RANGE-type frames

  * All kinds of frame bounds are supported, including `RANGE PRECEDING|FOLLOWING n` frame bounds (unlike PostgreSQL or MS SQL Server)
  * Does not yet support DATE[TIME] datatype and arithmetic for RANGE-type frames ([MDEV-9727](https://jira.mariadb.org/browse/MDEV-9727))
* Does not support GROUPS-type frames (it seems that no popular database supports it, either)


* Does not support frame exclusion (no other database seems to support it, either) ([MDEV-9724](https://jira.mariadb.org/browse/MDEV-9724))
* Does not support explicit `NULLS FIRST` or `NULLS LAST`.
* Does not support nested navigation in window functions (this is `VALUE_OF(expr AT row_marker [, default_value)` syntax)


* The following window functions are supported:

  * "Streamable" window functions: [ROW_NUMBER](row_number.md), [RANK](rank.md), [DENSE_RANK](dense_rank.md),
  * Window functions that can be streamed once the number of rows in partition is known: [PERCENT_RANK](percent_rank.md), [CUME_DIST](cume_dist.md), [NTILE](ntile.md)


* Aggregate functions that are currently supported as window functions are: [COUNT](../../aggregate-functions/count.md), [SUM](../../aggregate-functions/sum.md), [AVG](../../aggregate-functions/avg.md), [BIT_OR](../../aggregate-functions/bit_or.md), [BIT_AND](../../aggregate-functions/bit_and.md), [BIT_XOR](../../aggregate-functions/bit_xor.md).
* Aggregate functions with the `DISTINCT` specifier (e.g. `COUNT( DISTINCT x)`) are not supported as window functions.


## Links


* [MDEV-6115](https://jira.mariadb.org/browse/MDEV-6115) is the main jira task for window functions development. Other tasks are attached as sub-tasks
* [bb-10.2-mdev9543](https://github.com/MariaDB/server/commits/bb-10.2-mdev9543) is the feature tree for window functions. Development is ongoing, and this tree has the newest changes.
* Testcases are in `mysql-test/t/win*.test`


## Examples


Given the following sample data:


```
CREATE TABLE users (
  email VARCHAR(30), 
  first_name VARCHAR(30), 
  last_name VARCHAR(30), 
  account_type VARCHAR(30)
);

INSERT INTO users VALUES 
  ('admin@boss.org', 'Admin', 'Boss', 'admin'), 
  ('bob.carlsen@foo.bar', 'Bob', 'Carlsen', 'regular'),
  ('eddie.stevens@data.org', 'Eddie', 'Stevens', 'regular'),
  ('john.smith@xyz.org', 'John', 'Smith', 'regular'), 
  ('root@boss.org', 'Root', 'Chief', 'admin')
```

First, let's order the records by email alphabetically, giving each an ascending *rnum* value starting with 1. This will make use of the [ROW_NUMBER](row_number.md) window function:


```
SELECT row_number() OVER (ORDER BY email) AS rnum,
    email, first_name, last_name, account_type
FROM users ORDER BY email;
+------+------------------------+------------+-----------+--------------+
| rnum | email                  | first_name | last_name | account_type |
+------+------------------------+------------+-----------+--------------+
|    1 | admin@boss.org         | Admin      | Boss      | admin        |
|    2 | bob.carlsen@foo.bar    | Bob        | Carlsen   | regular      |
|    3 | eddie.stevens@data.org | Eddie      | Stevens   | regular      |
|    4 | john.smith@xyz.org     | John       | Smith     | regular      |
|    5 | root@boss.org          | Root       | Chief     | admin        |
+------+------------------------+------------+-----------+--------------
```

We can generate separate sequences based on account type, using the PARTITION BY clause:


```
SELECT row_number() OVER (PARTITION BY account_type ORDER BY email) AS rnum, 
  email, first_name, last_name, account_type 
FROM users ORDER BY account_type,email;
+------+------------------------+------------+-----------+--------------+
| rnum | email                  | first_name | last_name | account_type |
+------+------------------------+------------+-----------+--------------+
|    1 | admin@boss.org         | Admin      | Boss      | admin        |
|    2 | root@boss.org          | Root       | Chief     | admin        |
|    1 | bob.carlsen@foo.bar    | Bob        | Carlsen   | regular      |
|    2 | eddie.stevens@data.org | Eddie      | Stevens   | regular      |
|    3 | john.smith@xyz.org     | John       | Smith     | regular      |
+------+------------------------+------------+-----------+--------------+
```

Given the following structure and data, we want to find the top 5 salaries from each department.


```
CREATE TABLE employee_salaries (dept VARCHAR(20), name VARCHAR(20), salary INT(11));

INSERT INTO employee_salaries VALUES
('Engineering', 'Dharma', 3500),
('Engineering', 'Binh', 3000),
('Engineering', 'Adalynn', 2800),
('Engineering', 'Samuel', 2500),
('Engineering', 'Cveta', 2200),
('Engineering', 'Ebele', 1800),
('Sales', 'Carbry', 500),
('Sales', 'Clytemnestra', 400),
('Sales', 'Juraj', 300),
('Sales', 'Kalpana', 300),
('Sales', 'Svantepolk', 250),
('Sales', 'Angelo', 200);
```

We could do this without using window functions, as follows:


```
select dept, name, salary
from employee_salaries as t1
where (select count(t2.salary)
       from employee_salaries as t2
       where t1.name != t2.name and
             t1.dept = t2.dept and
             t2.salary > t1.salary) < 5
order by dept, salary desc;

+-------------+--------------+--------+
| dept        | name         | salary |
+-------------+--------------+--------+
| Engineering | Dharma       |   3500 |
| Engineering | Binh         |   3000 |
| Engineering | Adalynn      |   2800 |
| Engineering | Samuel       |   2500 |
| Engineering | Cveta        |   2200 |
| Sales       | Carbry       |    500 |
| Sales       | Clytemnestra |    400 |
| Sales       | Juraj        |    300 |
| Sales       | Kalpana      |    300 |
| Sales       | Svantepolk   |    250 |
+-------------+--------------+--------+
```

This has a number of disadvantages:


* if there is no index, the query could take a long time if the employee_salary_table is large
* Adding and maintaining indexes adds overhead, and even with indexes on dept and salary, each subquery execution adds overhead by performing a lookup through the index.


Let's try achieve the same with window functions. First, generate a rank for all employees, using the [RANK](rank.md) function.


```
select rank() over (partition by dept order by salary desc) as ranking,
    dept, name, salary
    from employee_salaries
    order by dept, ranking;
+---------+-------------+--------------+--------+
| ranking | dept        | name         | salary |
+---------+-------------+--------------+--------+
|       1 | Engineering | Dharma       |   3500 |
|       2 | Engineering | Binh         |   3000 |
|       3 | Engineering | Adalynn      |   2800 |
|       4 | Engineering | Samuel       |   2500 |
|       5 | Engineering | Cveta        |   2200 |
|       6 | Engineering | Ebele        |   1800 |
|       1 | Sales       | Carbry       |    500 |
|       2 | Sales       | Clytemnestra |    400 |
|       3 | Sales       | Juraj        |    300 |
|       3 | Sales       | Kalpana      |    300 |
|       5 | Sales       | Svantepolk   |    250 |
|       6 | Sales       | Angelo       |    200 |
+---------+-------------+--------------+--------+
```

Each department has a separate sequence of ranks due to the *PARTITION BY* clause. This particular sequence of values for *rank()* is given by the *ORDER BY* clause inside the window function’s *OVER* clause. Finally, to get our results in a readable format we order the data by *dept* and the newly generated *ranking* column.


Now, we need to reduce the results to find only the top 5 per department. Here is a common mistake:


```
select
rank() over (partition by dept order by salary desc) as ranking,
dept, name, salary
from employee_salaries
where ranking <= 5
order by dept, ranking;

ERROR 1054 (42S22): Unknown column 'ranking' in 'where clause'
```

Trying to filter only the first 5 values per department by putting a where clause in the statement does not work, due to the way window functions are computed. The computation of window functions happens after all WHERE, GROUP BY and HAVING clauses have been completed, right before ORDER BY, so the WHERE clause has no idea that the ranking column exists. It is only present after we have filtered and grouped all the rows.


To counteract this problem, we need to wrap our query into a derived table. We can then attach a where clause to it:


```
select *from (select rank() over (partition by dept order by salary desc) as ranking,
  dept, name, salary
from employee_salaries) as salary_ranks
where (salary_ranks.ranking <= 5)
  order by dept, ranking;
+---------+-------------+--------------+--------+
| ranking | dept        | name         | salary |
+---------+-------------+--------------+--------+
|       1 | Engineering | Dharma       |   3500 |
|       2 | Engineering | Binh         |   3000 |
|       3 | Engineering | Adalynn      |   2800 |
|       4 | Engineering | Samuel       |   2500 |
|       5 | Engineering | Cveta        |   2200 |
|       1 | Sales       | Carbry       |    500 |
|       2 | Sales       | Clytemnestra |    400 |
|       3 | Sales       | Juraj        |    300 |
|       3 | Sales       | Kalpana      |    300 |
|       5 | Sales       | Svantepolk   |    250 |
+---------+-------------+--------------+--------+
```

## See Also


* [Window Frames](window-frames.md)
* [Introduction to Window Functions in MariaDB Server 10.2](https://mariadb.com/resources/blog/introduction-window-functions-mariadb-server-102)


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
