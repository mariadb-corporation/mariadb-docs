# Sargable UPPER

Starting from [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.3/what-is-mariadb-113), expressions in the form

```sql
UPPER(key_col) = expr
UPPER(key_col) IN (constant-list)
```

are sargable if `key_col` uses either the `utf8mb3_general_ci` or `utf8mb4_general_ci` collation.

`UCASE` is a synonym for [UPPER](../../../reference/sql-functions/string-functions/upper.md) so is covered as well.

Sargable means that the optimizer is able to use such conditions to construct access methods, estimate their selectivity, or perform partition pruning.

## Example

```sql
CREATE TABLE t1 (
  key1 VARCHAR(32) COLLATE utf8mb4_general_ci,
  ...
  KEY(key1)
);
```

```sql
EXPLAIN SELECT * FROM t1 WHERE UPPER(key1)='ABC'
+------+-------------+-------+------+---------------+------+---------+-------+------+--------------------------+
| id   | select_type | table | type | possible_keys | key  | key_len | ref   | rows | Extra                    |
+------+-------------+-------+------+---------------+------+---------+-------+------+--------------------------+
|    1 | SIMPLE      | t1    | ref  | key1          | key1 | 131     | const | 1    | Using where; Using index |
+------+-------------+-------+------+---------------+------+---------+-------+------+--------------------------+
```

Note that `ref` access is used.

An example with join:

```sql
EXPLAIN SELECT * FROM t0,t1 WHERE upper(t1.key1)=t0.col;
+------+-------------+-------+------+---------------+------+---------+-------------+------+-------------+
| id   | select_type | table | type | possible_keys | key  | key_len | ref         | rows | Extra       |
+------+-------------+-------+------+---------------+------+---------+-------------+------+-------------+
|    1 | SIMPLE      | t0    | ALL  | NULL          | NULL | NULL    | NULL        | 10   | Using where |
|    1 | SIMPLE      | t1    | ref  | key1          | key1 | 131     | test.t0.col | 1    | Using index |
+------+-------------+-------+------+---------------+------+---------+-------------+------+-------------+
```

Here, the optimizer was able to construct `ref` access.

## Controlling the Optimization

The [optimizer\_switch](optimizer-switch.md) variable has the flag `sargable_casefold` to turn the optimization on and off. The default is ON.

## Optimizer Trace

The optimization is implemented as a rewrite for a query's WHERE/ON conditions. It uses the `sargable_casefold_removal` object name in the trace:

```json
"join_optimization": {
        "select_id": 1,
        "steps": [
          {
            "sargable_casefold_removal": {
              "before": "ucase(t1.key1) = t0.col",
              "after": "t1.key1 = t0.col"
            }
          },
```

## References

* [MDEV-31496](https://jira.mariadb.org/browse/MDEV-31496): Make optimizer handle UCASE(varchar\_col)=...
* An analog for [LCASE](../../../reference/sql-functions/string-functions/lcase.md) is not possible. See [MDEV-31955](https://jira.mariadb.org/browse/MDEV-31955): Make optimizer handle LCASE(varchar\_col)=... for details.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
