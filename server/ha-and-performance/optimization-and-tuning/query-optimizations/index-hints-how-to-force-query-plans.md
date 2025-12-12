# Index Hints: How to Force Query Plans

The optimizer is largely cost-based and will try to choose the optimal plan for any query. However in some cases it does not have enough information to choose a perfect plan and in these cases you may have to provide hints to force the optimizer to use another plan.

You can examine the query plan for a [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) by writing [EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) before the statement. [SHOW EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/show/show-explain.md) shows the output of a running query. In some cases, its output can be closer to reality than `EXPLAIN`.

For the following queries, we will use the world database for the examples.

## Setting up the World Example Database

Download it from [world.sql.gz](https://mariadb.com/kb/en/ftp://ftp.askmonty.org/public/world.sql.gz)

Install it with:

```bash
mariadb-admin create world
zcat world.sql.gz | ../client/mysql world
```

or

```bash
mariadb-admin create world
gunzip world.sql.gz
../client/mysql world < world.sql
```

## Forcing Join Order

You can force the join order by using [STRAIGHT\_JOIN](../../../reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax.md) either in the [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) or [JOIN](../../../reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax.md) part.

The simplest way to force the join order is to put the tables in the correct order in the `FROM` clause and use `SELECT STRAIGHT_JOIN` like so:

```sql
SELECT STRAIGHT_JOIN SUM(City.Population) FROM Country,City WHERE
City.CountryCode=Country.Code AND Country.HeadOfState="Volodymyr Zelenskyy";
```

If you only want to force the join order for a few tables, use`STRAIGHT_JOIN` in the `FROM` clause. When this is done, only tables connected with `STRAIGHT_JOIN` will have their order forced. For example:

```sql
SELECT SUM(City.Population) FROM Country STRAIGHT_JOIN City WHERE
City.CountryCode=Country.Code AND Country.HeadOfState="Volodymyr Zelenskyy";
```

In both of the above cases `Country` will be scanned first and for each matching country (one in this case) all rows in `City` will be checked for a match. As there is only one matching country this will be faster than the original query.

The output of [EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) for the above cases is:

| id | select\_type | table   | type | possible\_keys | key  | key\_len | ref  | rows | Extra                                           |
| -- | ------------ | ------- | ---- | -------------- | ---- | -------- | ---- | ---- | ----------------------------------------------- |
| 1  | SIMPLE       | Country | ALL  | PRIMARY        | NULL | NULL     | NULL | 239  | Using where                                     |
| 1  | SIMPLE       | City    | ALL  | NULL           | NULL | NULL     | NULL | 4079 | Using where; Using join buffer (flat, BNL join) |

This is one of the few cases where `ALL` is ok, as the scan of the`Country` table will only find one matching row.

## Forcing Usage of a Specific Index for the WHERE Clause

In some cases the optimizer may choose a non-optimal index or it may choose to not use an index at all, even if some index could theoretically be used.

In these cases you have the option to either tell the optimizer to only use a limited set of indexes, ignore one or more indexes, or force the usage of some particular index.

### USE INDEX: Use a Limited Set of Indexes

You can limit which indexes are considered with the [USE INDEX](use-index.md) option.

```sql
USE INDEX [{FOR {JOIN|ORDER BY|GROUP BY}] ([index_list])
```

The default is '`FOR JOIN`', which means that the hint only affects how the`WHERE` clause is optimized.

`USE INDEX` is used after the table name in the `FROM` clause.

Example:

```sql
CREATE INDEX Name ON City (Name);
CREATE INDEX CountryCode ON City (Countrycode);
EXPLAIN SELECT Name FROM City USE INDEX (CountryCode)
WHERE name="Helsingborg" AND countrycode="SWE";
```

This produces:

| id | select\_type | table | type | possible\_keys | key         | key\_len | ref   | rows | Extra       |
| -- | ------------ | ----- | ---- | -------------- | ----------- | -------- | ----- | ---- | ----------- |
| 1  | SIMPLE       | City  | ref  | CountryCode    | CountryCode | 3        | const | 14   | Using where |

If we had not used [USE INDEX](use-index.md), the `Name` index would have been in`possible keys`.

### IGNORE INDEX: Don't Use a Particular Index

You can tell the optimizer to not consider some particular index with the [IGNORE INDEX](ignore-index.md) option.

```sql
IGNORE INDEX [{FOR {JOIN|ORDER BY|GROUP BY}] ([index_list])
```

This is used after the table name in the `FROM` clause:

```sql
CREATE INDEX Name ON City (Name);
CREATE INDEX CountryCode ON City (Countrycode);
EXPLAIN SELECT Name FROM City IGNORE INDEX (Name)
WHERE name="Helsingborg" AND countrycode="SWE";
```

This produces:

| id | select\_type | table | type | possible\_keys | key         | key\_len | ref   | rows | Extra       |
| -- | ------------ | ----- | ---- | -------------- | ----------- | -------- | ----- | ---- | ----------- |
| 1  | SIMPLE       | City  | ref  | CountryCode    | CountryCode | 3        | const | 14   | Using where |

The benefit of using `IGNORE_INDEX` instead of `USE_INDEX` is that it will not disable a new index which you may add later.

Also see [Ignored Indexes](../optimization-and-indexes/ignored-indexes.md) for an option to specify in the index definition that indexes should be ignored.

### FORCE INDEX: Forcing an Index

[Forcing an index](force-index.md) to be used is mostly useful when the optimizer decides to do a table scan even if you know that using an index would be better. (The optimizer could decide to do a table scan even if there is\
an available index when it believes that most or all rows will match and it can avoid the overhead of using the index).

```sql
CREATE INDEX Name ON City (Name);
EXPLAIN SELECT Name,CountryCode FROM City FORCE INDEX (Name)
WHERE name>="A" AND CountryCode >="A";
```

This produces:

| id | select\_type | table | type  | possible\_keys | key  | key\_len | ref  | rows | Extra       |
| -- | ------------ | ----- | ----- | -------------- | ---- | -------- | ---- | ---- | ----------- |
| 1  | SIMPLE       | City  | range | Name           | Name | 35       | NULL | 4079 | Using where |

`FORCE_INDEX` works by only considering the given indexes (like with`USE_INDEX`) but in addition it tells the optimizer to regard a table scan as something very expensive. However if none of the 'forced' indexes can be used, then a table scan will be used anyway.

### Index Prefixes

When using index hints (USE, FORCE or [IGNORE INDEX](ignore-index.md)), the index name value can also be an unambiguous prefix of an index name.

## Forcing an Index to be Used for ORDER BY or GROUP BY

The optimizer will try to use indexes to resolve [ORDER BY](../../../reference/sql-statements/data-manipulation/selecting-data/order-by.md) and [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md).

You can use [USE INDEX](use-index.md), [IGNORE INDEX](ignore-index.md) and [FORCE INDEX](force-index.md) as in the `WHERE` clause above\
to ensure that some specific index used:

```sql
USE INDEX [{FOR {JOIN|ORDER BY|GROUP BY}] ([index_list])
```

This is used after the table name in the `FROM` clause.

Example:

```sql
CREATE INDEX Name ON City (Name);
EXPLAIN SELECT Name,COUNT(*) FROM City
FORCE INDEX FOR GROUP BY (Name)
WHERE population >= 10000000 GROUP BY Name;
```

This produces:

| id | select\_type | table | type  | possible\_keys | key  | key\_len | ref  | rows | Extra       |
| -- | ------------ | ----- | ----- | -------------- | ---- | -------- | ---- | ---- | ----------- |
| 1  | SIMPLE       | City  | index | NULL           | Name | 35       | NULL | 4079 | Using where |

Without the [FORCE INDEX](force-index.md) option we would have '`Using where; Using temporary; Using filesort`' in the 'Extra' column, which means that the optimizer would created a temporary table and sort it.

### Help the Optimizer Optimize GROUP BY and ORDER BY

The optimizer uses several strategies to optimize [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md) and [ORDER BY](../../../reference/sql-statements/data-manipulation/selecting-data/order-by.md):

* Resolve with an index:
  * Scan the table in index order and output data as we go. (This only works if the [ORDER BY](../../../reference/sql-statements/data-manipulation/selecting-data/order-by.md) / [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md) can be resolved by an index after constant propagation is done).
* Filesort:
  * Scan the table to be sorted and collect the sort keys in a temporary file.
  * Sort the keys + reference to row (with filesort)
  * Scan the table in sorted order
* Use a temporary table for [ORDER BY](../../../reference/sql-statements/data-manipulation/selecting-data/order-by.md):
  * Create a temporary (in memory) table for the 'to-be-sorted' data. (If this gets bigger than `max_heap_table_size` or contains blobs then an [Aria](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/README.md) or [MyISAM](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/README.md) disk based table will be used)
  * Sort the keys + reference to row (with filesort)
  * Scan the table in sorted order

A temporary table will always be used if the fields which will be sorted are not from the first table in the [JOIN](../../../reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax.md) order.

* Use a temporary table for [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md):
  * Create a temporary table to hold the [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md) result with an index that matches the [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md) fields.
  * Produce a result row
  * If a row with the [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md) key exists in the temporary table, add the new result row to it. If not, create a new row.
  * Before sending the results to the user, sort the rows with filesort to get the results in the [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md) order.

### Forcing/Disallowing TemporaryTables to be Used for GROUP BY:

Using an in-memory table (as described above) is usually the fastest option for [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md) if the result set is small. It is not optimal if the result set is very big. You can tell the optimizer this by using`SELECT SQL_SMALL_RESULT` or `SELECT SQL_BIG_RESULT`.

For example:

```sql
EXPLAIN SELECT SQL_SMALL_RESULT Name,Count(*) AS Cities 
FROM City GROUP BY Name HAVING Cities > 2;
```

produces:

| id | select\_type | table | type | possible\_keys | key  | key\_len | ref  | rows | Extra                           |
| -- | ------------ | ----- | ---- | -------------- | ---- | -------- | ---- | ---- | ------------------------------- |
| 1  | SIMPLE       | City  | ALL  | NULL           | NULL | NULL     | NULL | 4079 | Using temporary; Using filesort |

while:

```sql
EXPLAIN SELECT SQL_BIG_RESULT Name,Count(*) AS Cities 
FROM City GROUP BY Name HAVING Cities > 2;
```

produces:

| id | select\_type | table | type | possible\_keys | key  | key\_len | ref  | rows | Extra          |
| -- | ------------ | ----- | ---- | -------------- | ---- | -------- | ---- | ---- | -------------- |
| 1  | SIMPLE       | City  | ALL  | NULL           | NULL | NULL     | NULL | 4079 | Using filesort |

The difference is that with `SQL_SMALL_RESULT` a temporary table is used.

## Forcing Usage of Temporary Tables

In some cases you may want to force the use of a temporary table for the result to free up the table/row locks for the used tables as quickly as possible.

You can do this with the `SQL_BUFFER_RESULT` option:

```sql
CREATE INDEX Name ON City (Name);
EXPLAIN SELECT SQL_BUFFER_RESULT Name,COUNT(*) AS Cities FROM City
GROUP BY Name HAVING Cities > 2;
```

This produces:

| id | select\_type | table | type  | possible\_keys | key  | key\_len | ref  | rows | Extra                        |
| -- | ------------ | ----- | ----- | -------------- | ---- | -------- | ---- | ---- | ---------------------------- |
| 1  | SIMPLE       | City  | index | NULL           | Name | 35       | NULL | 4079 | Using index; Using temporary |

Without `SQL_BUFFER_RESULT`, the above query would not use a temporary table for the result set.

## Optimizer Switch

In [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) we added an [optimizer switch](../system-variables/server-system-variables.md#optimizer_switch) which allows you to specify which algorithms will be considered when optimizing a query.

See the [optimizer](./) section for more information about the different algorithms which are used.

## See Also

* [FORCE INDEX](force-index.md)
* [USE INDEX](use-index.md)
* [IGNORE INDEX](ignore-index.md)
* [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md)
* [Ignored Indexes](../optimization-and-indexes/ignored-indexes.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
