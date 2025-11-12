# EXCEPT

## EXCEPT

The result of `EXCEPT` contains all records of the left `SELECT` result set except records which are in right `SELECT` result set. In other words, it is the subtraction of two result sets.

{% tabs %}
{% tab title="Current" %}
`MINUS` is a synonym when [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) is set.
{% endtab %}

{% tab title="< 10.6.1" %}
`MINUS` is a synonym is not available.
{% endtab %}
{% endtabs %}

## Syntax

```sql
SELECT ...
(INTERSECT [ALL | DISTINCT] | EXCEPT [ALL | DISTINCT] | UNION [ALL | DISTINCT]) 
  SELECT ...
[(INTERSECT [ALL | DISTINCT] | EXCEPT [ALL | DISTINCT] | UNION [ALL | DISTINCT]) 
  SELECT ...]
[ORDER BY [{col_name | expr | position} [ASC | DESC] 
  [, {col_name | expr | position} [ASC | DESC] ...]]]
[LIMIT {[offset,] row_count | row_count OFFSET offset}
| OFFSET start { ROW | ROWS }
| FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES } ]
```

{% hint style="warning" %}
Brackets for explicit operation precedence are not supported; use a subquery in the `FROM` clause as a workaround.
{% endhint %}

### Description

MariaDB supports `EXCEPT` and [INTERSECT](intersect.md) in addition to [UNION](union.md).

The queries before and after `EXCEPT` must be [SELECT](../select.md) or [VALUES](../../../../sql-structure/sql-language-structure/table-value-constructors.md) statements.

All behavior for naming columns, `ORDER BY` and `LIMIT` is the same as for [UNION](union.md). Note that the alternative [SELECT ... OFFSET ... FETCH](../select-offset-fetch.md) syntax is only supported. This allows us to use the `WITH TIES` clause.

`EXCEPT` implicitly supposes a `DISTINCT` operation.

The result of `EXCEPT` is all records of the left `SELECT` result except records which are in right `SELECT` result set, i.e. it is subtraction of two result sets.

`EXCEPT` and `UNION` have the same operation precedence and `INTERSECT` has a higher precedence, unless [running in Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), in which case all three have the same precedence.

#### Parentheses

Parentheses can be used to specify precedence. Before this, a syntax error would be returned.

**MariaDB starting with** [**10.5.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes)

#### ALL/DISTINCT

{% tabs %}
{% tab title="Current" %}
`EXCEPT ALL` and `EXCEPT DISTINCT` . The `ALL` operator leaves duplicates intact, while the `DISTINCT` operator removes duplicates. `DISTINCT` is the default behavior if neither operator is supplied.
{% endtab %}

{% tab title="< 10.5" %}
Only `EXCEPT DISTINCT` is available.
{% endtab %}
{% endtabs %}

### Examples

Show customers which are not employees:

```sql
(SELECT e_name AS name, email FROM customers)
EXCEPT
(SELECT c_name AS name, email FROM employees);
```

Difference between [UNION](union.md), EXCEPT and [INTERSECT](intersect.md):

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

Parentheses for specifying precedence:

```sql
CREATE OR REPLACE TABLE t1 (a INT);
CREATE OR REPLACE TABLE t2 (b INT);
CREATE OR REPLACE TABLE t3 (c INT);

INSERT INTO t1 VALUES (1),(2),(3),(4);
INSERT INTO t2 VALUES (5),(6);
INSERT INTO t3 VALUES (1),(6);

((SELECT a FROM t1) UNION (SELECT b FROM t2)) EXCEPT (SELECT c FROM t3);
+------+
| a    |
+------+
|    2 |
|    3 |
|    4 |
|    5 |
+------+

(SELECT a FROM t1) UNION ((SELECT b FROM t2) EXCEPT (SELECT c FROM t3));
+------+
| a    |
+------+
|    1 |
|    2 |
|    3 |
|    4 |
|    5 |
+------+
```

Here is an example that makes use of the [SEQUENCE](../../../../../server-usage/storage-engines/sequence-storage-engine.md) storage engine and the [VALUES](../../../../sql-structure/sql-language-structure/table-value-constructors.md) statement, to generate a numeric sequence and remove some arbitrary numbers from it:

```sql
(SELECT seq FROM seq_1_to_10) EXCEPT VALUES (2), (3), (4);
+-----+
| seq |
+-----+
|   1 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
+-----+
```

### See Also

* [UNION](union.md)
* [INTERSECT](intersect.md)
* [Get Set for Set Theory: UNION, INTERSECT and EXCEPT in SQL](https://www.youtube.com/watch?v=UNi-fVSpRm0) (video tutorial)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
