---
description: >-
  Combine results from multiple SELECT statements into a single result set. This
  operator can optionally remove duplicates or include all rows.
---

# UNION

`UNION` is used to combine the results from multiple [SELECT](../select.md) statements into a single result set.

## Syntax

```
SELECT ...
UNION [ALL | DISTINCT] SELECT ...
[UNION [ALL | DISTINCT] SELECT ...]
[ORDER BY [column [, column ...]]]
[LIMIT {[offset,] row_count | row_count OFFSET offset}]
```

## Description

`UNION` is used to combine the results from multiple [SELECT](../select.md) statements into a single result set.

The column names from the first `SELECT` statement are used as the column names for the results returned. Selected columns listed in corresponding positions of each SELECT statement should have the same data type. (For example, the first column selected by the first statement should have the same type as the first column selected by the other statements.)

If they don't, the type and length of the columns in the result take into account the values returned by all of the SELECTs, so there is no need for explicit casting. Note that currently this is not the case for [recursive CTEs](../common-table-expressions/recursive-common-table-expressions-overview.md) - see [MDEV-12325](https://jira.mariadb.org/browse/MDEV-12325).

Table names can be specified as `db_name`.`tbl_name`. This permits writing `UNION`s which involve multiple databases. See [Identifier Qualifiers](../../../../sql-structure/sql-language-structure/identifier-qualifiers.md) for syntax details.

UNION queries cannot be used with [aggregate functions](../../../../sql-functions/aggregate-functions/).

`EXCEPT` and `UNION` have the same operation precedence and `INTERSECT` has a higher precedence, unless [running in Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), in which case all three have the same precedence.

### ALL/DISTINCT

The `ALL` keyword causes duplicate rows to be preserved. The `DISTINCT` keyword (the default if the keyword is omitted) causes duplicate rows to be removed by the results.

`UNION ALL` and `UNION DISTINCT` can both be present in a query. In this case, `UNION` DISTINCT will override any `UNION ALL` to its left.

The server can in most cases execute `UNION ALL` without creating a temporary table (see [MDEV-334](https://jira.mariadb.org/browse/MDEV-334)).

### ORDER BY and LIMIT

Individual `SELECT` statements can contain their own [ORDER BY](../order-by.md) and [LIMIT](../limit.md) clauses. In this case, the individual queries need to be wrapped between parentheses. However, this does not affect the order of the UNION, so they only are useful to limit the record read by one `SELECT`.

The `UNION` can have global [ORDER BY](../order-by.md) and [LIMIT](../limit.md) clauses, which affect the whole result set. If the columns retrieved by individual SELECT statements have an alias (AS), the `ORDER BY` must use that alias, not the real column names.

### HIGH\_PRIORITY

Specifying a query as [HIGH\_PRIORITY](../select.md#high-priority) does not work inside a `UNION`. If applied to the first `SELECT`, it is ignored. Applying to a later `SELECT` results in a syntax error:

```sql
ERROR 1234 (42000): Incorrect usage/placement of 'HIGH_PRIORITY'
```

### SELECT ... INTO ...

Individual `SELECT` statements cannot be written [INTO DUMPFILE](../select-into-dumpfile.md) or [INTO OUTFILE](../select-into-outfile.md). If the last `SELECT` statement specifies `INTO DUMPFILE` or `INTO OUTFILE`, the entire result of the `UNION` will be written. Placing the clause after any other `SELECT` will result in a syntax error.

If the result is a single row, [SELECT ... INTO @var\_name](../../../programmatic-compound-statements/selectinto.md) can also be used.

### Parentheses

{% tabs %}
{% tab title="Current" %}
Parentheses can be used to specify precedence.
{% endtab %}

{% tab title="< 10.4" %}
Parentheses **cannot** be used to specify precedence.
{% endtab %}
{% endtabs %}

## Examples

`UNION` between tables having different column names:

```sql
(SELECT e_name AS name, email FROM employees)
UNION
(SELECT c_name AS name, email FROM customers);
```

Specifying the `UNION` global order and limiting total rows:

```sql
(SELECT name, email FROM employees)
UNION
(SELECT name, email FROM customers)
ORDER BY name LIMIT 10;
```

Adding a constant row:

```sql
(SELECT 'John Doe' AS name, 'john.doe@example.net' AS email)
UNION
(SELECT name, email FROM customers);
```

Differing types:

```sql
SELECT CAST('x' AS CHAR(1)) UNION SELECT REPEAT('y',4);
+----------------------+
| CAST('x' AS CHAR(1)) |
+----------------------+
| x                    |
| yyyy                 |
+----------------------+
```

Returning the results in order of each individual `SELECT` by use of a sort column:

```sql
(SELECT 1 AS sort_column, e_name AS name, email FROM employees)
UNION
(SELECT 2, c_name AS name, email FROM customers) ORDER BY sort_column;
```

Difference between UNION, [EXCEPT](except.md) and [INTERSECT](intersect.md):

```sql
CREATE TABLE seqs (i INT);
INSERT INTO seqs VALUES (1),(2),(2),(3),(3),(4),(5),(6);

SELECT i FROM seqs WHERE i <= 3 UNION SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    1 |
|    2 |
|    3 |
|    4 |
|    5 |
|    6 |
+------+

SELECT i FROM seqs WHERE i <= 3 UNION ALL SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    1 |
|    2 |
|    2 |
|    3 |
|    3 |
|    3 |
|    3 |
|    4 |
|    5 |
|    6 |
+------+

SELECT i FROM seqs WHERE i <= 3 EXCEPT SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    1 |
|    2 |
+------+

SELECT i FROM seqs WHERE i <= 3 EXCEPT ALL SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    1 |
|    2 |
|    2 |
+------+

SELECT i FROM seqs WHERE i <= 3 INTERSECT SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    3 |
+------+

SELECT i FROM seqs WHERE i <= 3 INTERSECT ALL SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    3 |
|    3 |
+------+
```

```sql
CREATE OR REPLACE TABLE t1 (a INT);
CREATE OR REPLACE TABLE t2 (b INT);
CREATE OR REPLACE TABLE t3 (c INT);

INSERT INTO t1 VALUES (1),(2),(3),(4);
INSERT INTO t2 VALUES (5),(6);
INSERT INTO t3 VALUES (1),(6);

((SELECT a FROM t1) UNION (SELECT b FROM t2)) INTERSECT (SELECT c FROM t3);
+------+
| a    |
+------+
|    1 |
|    6 |
+------+

(SELECT a FROM t1) UNION ((SELECT b FROM t2) INTERSECT (SELECT c FROM t3));
+------+
| a    |
+------+
|    1 |
|    2 |
|    3 |
|    4 |
|    6 |
+------+
```

## See Also

* [SELECT](../select.md)
* [EXCEPT](except.md)
* [INTERSECT](intersect.md)
* [Recursive Common Table Expressions Overview](../common-table-expressions/recursive-common-table-expressions-overview.md)
* [Get Set for Set Theory: UNION, INTERSECT and EXCEPT in SQL](https://www.youtube.com/watch?v=UNi-fVSpRm0) (video tutorial)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
