# INTERSECT

Return only rows that appear in both result sets. This set operator identifies the common records shared between two queries.

## Syntax

```sql
SELECT ...
(INTERSECT [ALL | DISTINCT] | EXCEPT [ALL | DISTINCT] | UNION [ALL | DISTINCT]) SELECT ...
[(INTERSECT [ALL | DISTINCT] | EXCEPT [ALL | DISTINCT] | UNION [ALL | DISTINCT]) SELECT ...]
[ORDER BY [column [, column ...]]]
[LIMIT {[offset,] row_count | row_count OFFSET offset}]
```

## Description

MariaDB has supported `INTERSECT` (as well as [EXCEPT](except.md)) in addition to [UNION](union.md) since [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103).

All behavior for naming columns, `ORDER BY` and `LIMIT` is the same as for [UNION](union.md).

`INTERSECT` implicitly supposes a `DISTINCT` operation.

The result of an intersect is the intersection of right and left `SELECT` results, i.e. only records that are present in both result sets will be included in the result of the operation.

`INTERSECT` has higher precedence than `UNION` and `EXCEPT` (unless running [running in Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), in which case all three have the same precedence). If possible it will be executed linearly, but if not, it will be translated to a subquery in the `FROM` clause:

```sql
(SELECT a,b FROM t1)
UNION
(SELECT c,d FROM t2)
INTERSECT
(SELECT e,f FROM t3)
UNION
(SELECT 4,4);
```

will be translated to:

```sql
(SELECT a,b FROM t1)
UNION
SELECT c,d FROM
  ((SELECT c,d FROM t2)
   INTERSECT
   (SELECT e,f FROM t3)) dummy_subselect
UNION
(SELECT 4,4)
```

### Parentheses

{% tabs %}
{% tab title="Current" %}
Parentheses can be used to specify precedence.
{% endtab %}

{% tab title="< 10.4" %}
Parentheses **cannot** be used to specify precedence.
{% endtab %}
{% endtabs %}

**MariaDB starting with** [**10.5.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes)

### ALL/DISTINCT

{% tabs %}
{% tab title="Current" %}
`INTERSECT ALL` and `INTERSECT DISTINCT` . The `ALL` operator leaves duplicates intact, while the `DISTINCT` operator removes duplicates. `DISTINCT` is the default behavior if neither operator is supplied.
{% endtab %}

{% tab title="< 10.5" %}
`DISTINCT` is the only behavior available.
{% endtab %}
{% endtabs %}

## Examples

Show customers which are employees:

```sql
(SELECT e_name AS name, email FROM employees)
INTERSECT
(SELECT c_name AS name, email FROM customers);
```

Difference between [UNION](union.md), [EXCEPT](except.md) and `INTERSECT`:

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

* [UNION](union.md)
* [EXCEPT](except.md)
* [Get Set for Set Theory: UNION, INTERSECT and EXCEPT in SQL](https://www.youtube.com/watch?v=UNi-fVSpRm0) (video tutorial)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
