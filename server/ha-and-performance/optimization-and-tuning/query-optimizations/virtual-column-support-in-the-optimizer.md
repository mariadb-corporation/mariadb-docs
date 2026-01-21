# Virtual Column Support in the Optimizer

{% hint style="info" %}
This feature is available from MariaDB 11.8.
{% endhint %}

The optimizer can recognize use of indexed virtual column expressions in the `WHERE` clause and use them to construct range and `ref(const)` accesses.

## Example

Consider this table with data in JSON format:

```sql
CREATE TABLE t1 (json_data JSON);
INSERT INTO t1 VALUES('{"column1": 1234}'); 
INSERT INTO t1 ...
```

In order to do efficient queries over data in JSON, you can add a virtual column, and an index on that column:

```sql
ALTER TABLE t1
  ADD COLUMN vcol1 INT AS (cast(json_value(json_data, '$.column1') AS INTEGER)),
  ADD INDEX(vcol1);
```

Before MariaDB 11.8, you had to use `vcol1` in the `WHERE` clause. Now, you can use the virtual column expression, too:

```sql
-- This uses the index before 11.8:
EXPLAIN SELECT * FROM t1 WHERE vcol1=100;
-- Starting from 11.8, this uses the index, too:
EXPLAIN SELECT * FROM t1 
WHERE cast(json_value(json_data, '$.column1') AS INTEGER)=100;
```

```
+------+-------------+-------+------+---------------+-------+---------+-------+------+-------+
| id   | select_type | table | type | possible_keys | key   | key_len | ref   | rows | Extra |
+------+-------------+-------+------+---------------+-------+---------+-------+------+-------+
|    1 | SIMPLE      | t1    | ref  | vcol1         | vcol1 | 5       | const | 1    |       |
+------+-------------+-------+------+---------------+-------+---------+-------+------+-------+
```

## General Considerations

* In MariaDB, one has to create a virtual column and then create an index over it. Other databases allow to create an index directly over expression: `create index on t1((col1+col2))`. This is not yet supported in MariaDB ([MDEV-35853](https://jira.mariadb.org/browse/MDEV-35853)).
* The `WHERE` clause must use the exact same expression as in the virtual column definition.
* The optimization is implemented in a way similar to MySQL – the optimizer finds potentially useful occurrences of `vcol_expr` in the `WHERE` clause and replaces them with `vcol_name`.
* In the optimizer trace, the rewrites are shown like this:

```json
"virtual_column_substitution": {
              "condition": "WHERE",
              "resulting_condition": "t1.vcol1 = 100"
            }
```

{% hint style="info" %}
The following improvements are available from MariaDB 12.1.
{% endhint %}

1. Improved Optimizer plans for `SELECT` statements with `ORDER BY` or `GROUP BY` virtual columns when the virtual column expressions are covered by indexes that can be used.
2. Improved Optimizer plans for `SELECT` statements with `ORDER BY` or `GROUP BY` virtual columns expressions, by substitution of the virtual column expressions with virtual columns when the virtual columns are usable indexes themselves.
3. The same improvements apply for **single-table** `UPDATE` or `DELETE` statements.

## Accessing JSON fields

### Cast the Value to the Desired Type

SQL is strongly-typed language while JSON is weakly-typed. This means one must specify the desired datatype when accessing JSON data from SQL. In the above example, we declared `vcol1` as `INT` and then used `(CAST ... AS INTEGER)` (both in the ALTER TABLE and in the `WHERE` clause in SELECT query:):

```sql
ALTER TABLE t1
  ADD COLUMN vcol1 INT AS (CAST(json_value(json_data, '$.column1') AS INTEGER)) ...
```

```sql
SELECT ...  WHERE ... CAST(json_value(json_data, '$.column1') AS INTEGER) ...;
```

### Specify the Collation for Strings

When extracting string values, `CAST` is not necessary, as `JSON_VALUE` returns strings. However, you must take into account collations. Consider this column declared as `JSON`:

```sql
CREATE TABLE t1 ( 
  json_data JSON 
  ...
```

The collation of `json_data` is `utf8mb4_bin`. The collation  of `JSON_VALUE(json_data, ...)` is `utf8mb4_bin`, too.

Most use cases require a more commonly-used collation. It is possible to achieve that using the `COLLATE` clause:

```sql
ALTER TABLE t1
  ADD col1 VARCHAR(100) COLLATE utf8mb4_uca1400_ai_ci AS
  (json_value(js1, '$.string_column') COLLATE utf8mb4_uca1400_ai_ci),
  ADD INDEX(col1);
...
SELECT  ... 
WHERE
  json_value(js1, '$.string_column') COLLATE utf8mb4_uca1400_ai_ci='string-value';
```

## References

* [MDEV-35616](https://jira.mariadb.org/browse/MDEV-35616): Add basic optimizer support for virtual columns

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
