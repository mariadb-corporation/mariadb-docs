# EXPLAIN

## Syntax

```sql
EXPLAIN tbl_name [col_name | wild]
```

or

```sql
EXPLAIN [EXTENDED | PARTITIONS | FORMAT=JSON] 
  {SELECT select_options | UPDATE update_options | DELETE delete_options}
```

or

```sql
EXPLAIN [FORMAT=JSON] FOR CONNECTION <connection_id>
```

## Description

The `EXPLAIN` statement can be used either as a synonym for[DESCRIBE](../describe.md) or as a way to obtain information about how MariaDB executes a `SELECT`, `UPDATE` or `DELETE` statement:

* `'EXPLAIN tbl_name'` is synonymous with`'[DESCRIBE](../describe.md) tbl_name'` or`'[SHOW COLUMNS](../show/show-columns.md) FROM tbl_name'`.
* When you precede a `SELECT`, `UPDATE` or a `DELETE` statement with the keyword`EXPLAIN`, MariaDB displays information from the optimizer about the query execution plan. That is, MariaDB explains how it would process the `SELECT`, `UPDATE` or `DELETE`, including information about how tables are joined and in which order. `EXPLAIN EXTENDED` can be used to provide additional information.
* `EXPLAIN PARTITIONS` is useful only when examining queries involving partitioned tables. For details, see [Partition pruning and selection](../../../../server-usage/partitioning-tables/partition-pruning-and-selection.md).
* [ANALYZE statement](analyze-statement.md) performs the query as well as producing EXPLAIN output, and provides actual as well as estimated statistics.
* `EXPLAIN` output can be printed in the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/). See [EXPLAIN in the Slow Query Log](../../../../server-management/server-monitoring-logs/slow-query-log/explain-in-the-slow-query-log.md) for details.
* `EXPLAIN FOR CONNECTION` is an alias for `SHOW EXPLAIN FOR`.

[SHOW EXPLAIN](../show/show-explain.md) shows the output of a running statement. In some cases, its output can be closer to reality than `EXPLAIN`.

The [ANALYZE statement](analyze-statement.md) runs a statement and returns information about its execution plan. It also shows additional columns, to check how much the optimizer's estimation about filtering and found rows are close to reality.

There is an online [EXPLAIN Analyzer](../../../../clients-and-utilities/analyzing-tools/explain-analyzer.md) that you can use to share `EXPLAIN` and `EXPLAIN EXTENDED` output with others.

`EXPLAIN` can acquire metadata locks in the same way that `SELECT` does, as it needs to know table metadata and, sometimes, data as well.

### Columns in EXPLAIN ... SELECT

| Column name    | Description                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------- |
| Column name    | Description                                                                                         |
| id             | Sequence number that shows in which order tables are joined.                                        |
| select\_type   | What kind of SELECT the table comes from.                                                           |
| table          | Alias name of table. Materialized temporary tables for sub queries are named \<subquery#>           |
| type           | How rows are found from the table (join type).                                                      |
| possible\_keys | keys in table that could be used to find rows in the table                                          |
| key            | The name of the key that is used to retrieve rows. NULL is no key was used.                         |
| key\_len       | How many bytes of the key that was used (shows if we are using only parts of the multi-column key). |
| ref            | The reference that is used as the key value.                                                        |
| rows           | An estimate of how many rows we will find in the table for each key lookup.                         |
| Extra          | Extra information about this join.                                                                  |

Here are descriptions of the values for some of the more complex columns in `EXPLAIN ... SELECT`:

#### "Select\_type" Column

The `select_type` column can have the following values:

| Value                | Description                                                                                                                                                                                   | Comment                                                                                                                                                                            |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Value                | Description                                                                                                                                                                                   | Comment                                                                                                                                                                            |
| DEPENDENT SUBQUERY   | The SUBQUERY is DEPENDENT.                                                                                                                                                                    |                                                                                                                                                                                    |
| DEPENDENT UNION      | The UNION is DEPENDENT.                                                                                                                                                                       |                                                                                                                                                                                    |
| DERIVED              | The SELECT is DERIVED from the PRIMARY.                                                                                                                                                       |                                                                                                                                                                                    |
| MATERIALIZED         | The SUBQUERY is [MATERIALIZED](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/optimization-strategies/semi-join-materialization-strategy.md).                     | Materialized tables will be populated at first access and will be accessed by the primary key (= one key lookup). Number of rows in EXPLAIN shows the cost of populating the table |
| PRIMARY              | The SELECT is in the outermost query, but there is also a SUBQUERY within it.                                                                                                                 |                                                                                                                                                                                    |
| SIMPLE               | It is a simple SELECT query without any SUBQUERY or UNION.                                                                                                                                    |                                                                                                                                                                                    |
| SUBQUERY             | The SELECT is a SUBQUERY of the PRIMARY.                                                                                                                                                      |                                                                                                                                                                                    |
| UNCACHEABLE SUBQUERY | The SUBQUERY is UNCACHEABLE.                                                                                                                                                                  |                                                                                                                                                                                    |
| UNCACHEABLE UNION    | The UNION is UNCACHEABLE.                                                                                                                                                                     |                                                                                                                                                                                    |
| UNION                | The SELECT is a UNION of the PRIMARY.                                                                                                                                                         |                                                                                                                                                                                    |
| UNION RESULT         | The result of the UNION.                                                                                                                                                                      |                                                                                                                                                                                    |
| LATERAL DERIVED      | The SELECT uses a [Lateral Derived optimization](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/lateral-derived-optimization.md) |                                                                                                                                                                                    |

#### "Type" Column

This column contains information on how the table is accessed.

| Value            | Description                                                                                                                                                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Value            | Description                                                                                                                                                                                                                      |
| ALL              | A full table scan is done for the table (all rows are read). This is bad if the table is large and the table is joined against a previous table! This happens when the optimizer could not find any usable index to access rows. |
| const            | There is only one possibly matching row in the table. The row is read before the optimization phase and all columns in the table are treated as constants.                                                                       |
| eq\_ref          | A unique index is used to find the rows. This is the best possible plan to find the row.                                                                                                                                         |
| filter           | A second index is being used with the [Rowid Filtering Optimization](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/rowid-filtering-optimization.md).                                                |
| fulltext         | A fulltext index is used to access the rows.                                                                                                                                                                                     |
| index\_merge     | A 'range' access is done for several index and the found rows are merged. The key column shows which keys are used.                                                                                                          |
| index\_subquery  | This is similar as ref, but used for sub queries that are transformed to key lookups.                                                                                                                                            |
| index            | A full scan over the used index. Better than ALL but still bad if index is large and the table is joined against a previous table.                                                                                               |
| range            | The table will be accessed with a key over one or more value ranges.                                                                                                                                                             |
| ref\_or\_null    | Like 'ref' but in addition another search for the 'null' value is done if the first value was not found. This happens usually with sub queries.                                                                                  |
| ref              | A non unique index or prefix of an unique index is used to find the rows. Good if the prefix doesn't match many rows.                                                                                                            |
| system           | The table has 0 or 1 rows.                                                                                                                                                                                                       |
| unique\_subquery | This is similar as eq\_ref, but used for sub queries that are transformed to key lookups                                                                                                                                         |

#### "Extra" Column

This column consists of one or more of the following values, separated by ';'

_Note that some of these values are detected after the optimization phase._

The optimization phase can do the following changes to the `WHERE` clause:

* Add the expressions from the `ON` and `USING` clauses to the `WHERE` clause.
* Constant propagation: If there is `column=constant`, replace all column instances with this constant.
* Replace all columns from '`const`' tables with their values.
* Remove the used key columns from the `WHERE` (as this will be tested as part of the key lookup).
* Remove impossible constant sub expressions. For example `WHERE '(a=1 and a=2) OR b=1'` becomes `'b=1'`.
* Replace columns with other columns that has identical values: Example: `WHERE` `a=b` and `a=c` may be treated as `'WHERE a=b and a=c and b=c'`.
* Add extra conditions to detect impossible row conditions earlier. This happens mainly with `OUTER JOIN` where we in some cases add detection of `NULL` values in the `WHERE` (Part of '`Not exists`' optimization). This can cause an unexpected '`Using where`' in the Extra column.
* For each table level we remove expressions that have already been tested when we read the previous row. Example: When joining tables `t1` with `t2` using the following `WHERE 't1.a=1 and t1.a=t2.b'`, we don't have to test `'t1.a=1'` when checking rows in `t2` as we already know that this expression is true.

| Value                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Value                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| const row not found                                  | The table was a system table (a table with should exactly one row), but no row was found.                                                                                                                                                                                                                                                                                                                                                                            |
| Distinct                                             | If distinct optimization (remove duplicates) was used. This is marked only for the last table in the SELECT.                                                                                                                                                                                                                                                                                                                                                         |
| Full scan on NULL key                                | The table is a part of the sub query and if the value that is used to match the sub query will be NULL, we will do a full table scan.                                                                                                                                                                                                                                                                                                                                |
| Impossible HAVING                                    | The used HAVING clause is always false so the SELECT will return no rows.                                                                                                                                                                                                                                                                                                                                                                                            |
| Impossible WHERE noticed after reading const tables. | The used WHERE clause is always false so the SELECT will return no rows. This case was detected after we had read all 'const' tables and used the column values as constant in the WHERE clause. For example: WHERE const\_column=5 and const\_column had a value of 4.                                                                                                                                                                                              |
| Impossible WHERE                                     | The used WHERE clause is always false so the SELECT will return no rows. For example: WHERE 1=2                                                                                                                                                                                                                                                                                                                                                                      |
| No matching min/max row                              | During early optimization of MIN()/MAX() values it was detected that no row could match the WHERE clause. The MIN()/MAX() function will return NULL.                                                                                                                                                                                                                                                                                                                 |
| no matching row in const table                       | The table was a const table (a table with only one possible matching row), but no row was found.                                                                                                                                                                                                                                                                                                                                                                     |
| No tables used                                       | The SELECT was a sub query that did not use any tables. For example a there was no FROM clause or a FROM DUAL clause.                                                                                                                                                                                                                                                                                                                                                |
| Not exists                                           | Stop searching after more row if we find one single matching row. This optimization is used with LEFT JOIN where one is explicitly searching for rows that doesn't exists in the LEFT JOIN TABLE. Example: SELECT \* FROM t1 LEFT JOIN t2 on (...) WHERE t2.not\_null\_column IS NULL. As t2.not\_null\_column can only be NULL if there was no matching row for on condition, we can stop searching if we find a single matching row.                               |
| Open\_frm\_only                                      | For information\_schema tables. Only the frm (table definition file was opened) was opened for each matching row.                                                                                                                                                                                                                                                                                                                                                    |
| Open\_full\_table                                    | For information\_schema tables. A full table open for each matching row is done to retrieve the requested information. (Slow)                                                                                                                                                                                                                                                                                                                                        |
| Open\_trigger\_only                                  | For information\_schema tables. Only the trigger file definition was opened for each matching row.                                                                                                                                                                                                                                                                                                                                                                   |
| Range checked for each record (index map: ...)       | This only happens when there was no good default index to use but there may some index that could be used when we can treat all columns from previous table as constants. For each row combination the optimizer will decide which index to use (if any) to fetch a row from this table. This is not fast, but faster than a full table scan that is the only other choice. The index map is a bitmask that shows which index are considered for each row condition. |
| Scanned 0/1/all databases                            | For information\_schema tables. Shows how many times we had to do a directory scan.                                                                                                                                                                                                                                                                                                                                                                                  |
| Select tables optimized away                         | All tables in the join was optimized away. This happens when we are only using COUNT(\*), MIN() and MAX() functions in the SELECT and we where able to replace all of these with constants.                                                                                                                                                                                                                                                                          |
| Skip\_open\_table                                    | For information\_schema tables. The queried table didn't need to be opened.                                                                                                                                                                                                                                                                                                                                                                                          |
| unique row not found                                 | The table was detected to be a const table (a table with only one possible matching row) during the early optimization phase, but no row was found.                                                                                                                                                                                                                                                                                                                  |
| Using filesort                                       | Filesort is needed to resolve the query. This means an extra phase where we first collect all columns to sort, sort them with a disk based merge sort and then use the sorted set to retrieve the rows in sorted order. If the column set is small, we store all the columns in the sort file to not have to go to the database to retrieve them again.                                                                                                              |
| Using index                                          | Only the index is used to retrieve the needed information from the table. There is no need to perform an extra seek to retrieve the actual record.                                                                                                                                                                                                                                                                                                                   |
| Using index condition                                | Like 'Using where' but the where condition is pushed down to the table engine for internal optimization at the index level.                                                                                                                                                                                                                                                                                                                                          |
| Using index condition(BKA)                           | Like 'Using index condition' but in addition we use batch key access to retrieve rows.                                                                                                                                                                                                                                                                                                                                                                               |
| Using index for group-by                             | The index is being used to resolve a GROUP BY or DISTINCT query. The rows are not read. This is very efficient if the table has a lot of identical index entries as duplicates are quickly jumped over.                                                                                                                                                                                                                                                              |
| Using intersect(...)                                 | For index\_merge joins. Shows which index are part of the intersect.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Using join buffer                                    | We store previous row combinations in a row buffer to be able to match each row against all of the rows combinations in the join buffer at one go.                                                                                                                                                                                                                                                                                                                   |
| Using sort\_union(...)                               | For index\_merge joins. Shows which index are part of the union.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Using temporary                                      | A temporary table is created to hold the result. This typically happens if you are using GROUP BY, DISTINCT or ORDER BY.                                                                                                                                                                                                                                                                                                                                             |
| Using where                                          | A WHERE expression (in additional to the possible key lookup) is used to check if the row should be accepted. If you don't have 'Using where' together with a join type of ALL, you are probably doing something wrong!                                                                                                                                                                                                                                              |
| Using where with pushed condition                    | Like 'Using where' but the where condition is pushed down to the table engine for internal optimization at the row level.                                                                                                                                                                                                                                                                                                                                            |
| Using buffer                                         | The UPDATE statement will first buffer the rows, and then run the updates, rather than do updates on the fly. See [Using Buffer UPDATE Algorithm](using-buffer-update-algorithm.md) for a detailed explanation.                                                                                                                                                                                                                                                      |

### EXPLAIN EXTENDED

The `EXTENDED` keyword adds another column, _filtered_, to the output. This is a percentage estimate of the table rows that will be filtered by the condition.

An `EXPLAIN EXTENDED` will always throw a warning, as it adds extra _Message_ information to a subsequent [SHOW WARNINGS](../show/show-warnings.md) statement. This includes what the `SELECT` query would look like after optimizing and rewriting rules are applied and how the optimizer qualifies columns and tables.

## Examples

As synonym for `DESCRIBE` or `SHOW COLUMNS FROM`:

```sql
DESCRIBE city;
+------------+----------+------+-----+---------+----------------+
| Field      | Type     | Null | Key | Default | Extra          |
+------------+----------+------+-----+---------+----------------+
| Id         | int(11)  | NO   | PRI | NULL    | auto_increment |
| Name       | char(35) | YES  |     | NULL    |                |
| Country    | char(3)  | NO   | UNI |         |                |
| District   | char(20) | YES  | MUL |         |                |
| Population | int(11)  | YES  |     | NULL    |                |
+------------+----------+------+-----+---------+----------------+
```

A simple set of examples to see how `EXPLAIN` can identify poor index usage:

```sql
CREATE TABLE IF NOT EXISTS `employees_example` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `position` varchar(25) NOT NULL,
  `home_address` varchar(50) NOT NULL,
  `home_phone` varchar(12) NOT NULL,
  `employee_code` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_code` (`employee_code`),
  KEY `first_name` (`first_name`,`last_name`)
) ENGINE=Aria;

INSERT INTO `employees_example` (`first_name`, `last_name`, `position`, `home_address`, `home_phone`, `employee_code`)
  VALUES
  ('Mustapha', 'Mond', 'Chief Executive Officer', '692 Promiscuous Plaza', '326-555-3492', 'MM1'),
  ('Henry', 'Foster', 'Store Manager', '314 Savage Circle', '326-555-3847', 'HF1'),
  ('Bernard', 'Marx', 'Cashier', '1240 Ambient Avenue', '326-555-8456', 'BM1'),
  ('Lenina', 'Crowne', 'Cashier', '281 Bumblepuppy Boulevard', '328-555-2349', 'LC1'),
  ('Fanny', 'Crowne', 'Restocker', '1023 Bokanovsky Lane', '326-555-6329', 'FC1'),
  ('Helmholtz', 'Watson', 'Janitor', '944 Soma Court', '329-555-2478', 'HW1');

SHOW INDEXES FROM employees_example;
+-------------------+------------+---------------+--------------+---------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table             | Non_unique | Key_name      | Seq_in_index | Column_name   | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------------------+------------+---------------+--------------+---------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| employees_example |          0 | PRIMARY       |            1 | id            | A         |           7 |     NULL | NULL   |      | BTREE      |         |               |
| employees_example |          0 | employee_code |            1 | employee_code | A         |           7 |     NULL | NULL   |      | BTREE      |         |               |
| employees_example |          1 | first_name    |            1 | first_name    | A         |        NULL |     NULL | NULL   |      | BTREE      |         |               |
| employees_example |          1 | first_name    |            2 | last_name     | A         |        NULL |     NULL | NULL   |      | BTREE      |         |               |
+-------------------+------------+---------------+--------------+---------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
```

`SELECT` on a primary key:

```sql
EXPLAIN SELECT * FROM employees_example WHERE id=1;
+------+-------------+-------------------+-------+---------------+---------+---------+-------+------+-------+
| id   | select_type | table             | type  | possible_keys | key     | key_len | ref   | rows | Extra |
+------+-------------+-------------------+-------+---------------+---------+---------+-------+------+-------+
|    1 | SIMPLE      | employees_example | const | PRIMARY       | PRIMARY | 4       | const |    1 |       |
+------+-------------+-------------------+-------+---------------+---------+---------+-------+------+-------+
```

The type is _const_, which means that only one possible result could be returned.\
Now, returning the same record but searching by their phone number:

```sql
EXPLAIN SELECT * FROM employees_example WHERE home_phone='326-555-3492';
+------+-------------+-------------------+------+---------------+------+---------+------+------+-------------+
| id   | select_type | table             | type | possible_keys | key  | key_len | ref  | rows | Extra       |
+------+-------------+-------------------+------+---------------+------+---------+------+------+-------------+
|    1 | SIMPLE      | employees_example | ALL  | NULL          | NULL | NULL    | NULL |    6 | Using where |
+------+-------------+-------------------+------+---------------+------+---------+------+------+-------------+
```

Here, the type is _All_, which means no index could be used. Looking at the rows count, a full table scan (all six rows) had to be performed in order to retrieve the record. If it's a requirement to search by phone number, an index will have to be created.

[SHOW EXPLAIN](../show/show-explain.md) example:

```sql
SHOW EXPLAIN FOR 1;
+------+-------------+-------+-------+---------------+------+---------+------+---------+-------------+
| id   | select_type | table | type  | possible_keys | key  | key_len | ref  | rows    | Extra       |
+------+-------------+-------+-------+---------------+------+---------+------+---------+-------------+
|    1 | SIMPLE      | tbl   | index | NULL          | a    | 5       | NULL | 1000107 | Using index |
+------+-------------+-------+-------+---------------+------+---------+------+---------+-------------+
1 row in set, 1 warning (0.00 sec)
```

### Example of `ref_or_null` Optimization

```
SELECT * FROM table_name
  WHERE key_column=expr OR key_column IS NULL;
```

`ref_or_null` is something that often happens when you use subqueries with `NOT IN` as then one has to do an extra check for `NULL` values if the first value didn't have a matching row.

## See Also

* [SHOW EXPLAIN](../show/show-explain.md)
* [Ignored Indexes](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/ignored-indexes.md)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
