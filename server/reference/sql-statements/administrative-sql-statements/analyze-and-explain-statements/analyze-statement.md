---
description: >-
  Learn to use the ANALYZE statement to execute a query and produce a
  performance report. This command reveals how close the optimizer's plan was to
  the actual execution.
---

# ANALYZE Statement

## Description

The `ANALYZE statement` is similar to the `EXPLAIN statement`. `ANALYZE statement` will invoke the optimizer, execute the statement, and then produce `EXPLAIN` output instead of the result set. The `EXPLAIN` output will be annotated with statistics from statement execution.

This lets one check how close the optimizer's estimates about the query plan are to the reality. `ANALYZE` produces an overview, while the [ANALYZE FORMAT=JSON](analyze-format-json.md) command provides a more detailed view of the query plan and the query execution.

The syntax is

```sql
ANALYZE explainable_statement;
```

where the statement is any statement for which one can run [EXPLAIN](explain.md).

## Command Output

Consider an example:

```sql
ANALYZE SELECT * FROM tbl1 
WHERE key1 
  BETWEEN 10 AND 200 AND 
  col1 LIKE 'foo%'\G
```

```
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: tbl1
         type: range
possible_keys: key1
          key: key1
      key_len: 5
          ref: NULL
         rows: 181
       r_rows: 181
     filtered: 100.00
   r_filtered: 10.50
        Extra: Using index condition; Using where
```

Compared to `EXPLAIN`, `ANALYZE` produces two extra columns:

* `r_rows` is an observation-based counterpart of the rows column. It shows how many rows were actually read from the table.
* `r_filtered` is an observation-based counterpart of the filtered column. It shows which fraction of rows was left after applying the WHERE condition.

## Interpreting the Output

### Joins

Let's consider a more complicated example.

```sql
ANALYZE SELECT *
FROM orders, customer 
WHERE
  customer.c_custkey=orders.o_custkey AND
  customer.c_acctbal < 0 AND
  orders.o_totalprice > 200*1000
```

```
+----+-------------+----------+------+---------------+-------------+---------+--------------------+--------+--------+----------+------------+-------------+
| id | select_type | table    | type | possible_keys | key         | key_len | ref                | rows   | r_rows | filtered | r_filtered | Extra       |
+----+-------------+----------+------+---------------+-------------+---------+--------------------+--------+--------+----------+------------+-------------+
|  1 | SIMPLE      | customer | ALL  | PRIMARY,...   | NULL        | NULL    | NULL               | 149095 | 150000 |    18.08 |       9.13 | Using where |
|  1 | SIMPLE      | orders   | ref  | i_o_custkey   | i_o_custkey | 5       | customer.c_custkey |      7 |     10 |   100.00 |      30.03 | Using where |
+----+-------------+----------+------+---------------+-------------+---------+--------------------+--------+--------+----------+------------+-------------+
```

Here, one can see that

* For table customer, customer.rows=149095, customer.r\_rows=150000. The estimate for number of rows we will read was fairly precise
* customer.filtered=18.08, customer.r\_filtered=9.13. The optimizer somewhat overestimated the number of records that will match selectivity of condition attached to `customer` table (in general, when you have a full scan and r\_filtered is less than 15%, it's time to consider adding an appropriate index).
* For table orders, orders.rows=7, orders.r\_rows=10. This means that on average, there are 7 orders for a given c\_custkey, but in our case there were 10, which is close to the expectation (when this number is consistently far from the expectation, it may be time to run ANALYZE TABLE, or even edit the table statistics manually to get better query plans).
* orders.filtered=100, orders.r\_filtered=30.03. The optimizer didn't have any way to estimate which fraction of records will be left after it checks the condition that is attached to table orders (it's orders.o\_totalprice > 200\*1000). So, it used 100%. In reality, it is 30%. 30% is typically not selective enough to warrant adding new indexes. For joins with many tables, it might be worth to collect and use [column statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md) for columns in question, this may help the optimizer to pick a better query plan.

### Meaning of NULL in r\_rows and r\_filtered

Let's modify the previous example slightly

```sql
ANALYZE SELECT * 
FROM orders, customer 
WHERE
  customer.c_custkey=orders.o_custkey AND
  customer.c_acctbal < -0 AND 
  customer.c_comment LIKE '%foo%' AND
  orders.o_totalprice > 200*1000;
```

```
+----+-------------+----------+------+---------------+-------------+---------+--------------------+--------+--------+----------+------------+-------------+
| id | select_type | table    | type | possible_keys | key         | key_len | ref                | rows   | r_rows | filtered | r_filtered | Extra       |
+----+-------------+----------+------+---------------+-------------+---------+--------------------+--------+--------+----------+------------+-------------+
|  1 | SIMPLE      | customer | ALL  | PRIMARY,...   | NULL        | NULL    | NULL               | 149095 | 150000 |    18.08 |       0.00 | Using where |
|  1 | SIMPLE      | orders   | ref  | i_o_custkey   | i_o_custkey | 5       | customer.c_custkey |      7 |   NULL |   100.00 |       NULL | Using where |
+----+-------------+----------+------+---------------+-------------+---------+--------------------+--------+--------+----------+------------+-------------+
```

The output of **orders.r\_rows=NULL** and **orders.r\_filtered=NULL** shows that the table `orders` was never scanned. Indeed, we can also see customer.r\_filtered=0.00. This shows that a part of WHERE attached to table `customer` was never satisfied (or, satisfied in less than 0.01% of cases).

## ANALYZE FORMAT=JSON

[ANALYZE FORMAT=JSON](analyze-format-json.md) produces JSON output. It produces much more information than tabular `ANALYZE`.

## Notes

* `ANALYZE UPDATE` or `ANALYZE DELETE` will actually make updates/deletes (`ANALYZE SELECT` will perform the select operation and then discard the resultset).
* PostgreSQL has a similar command, `EXPLAIN ANALYZE`.
* The [EXPLAIN in the slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/explain-in-the-slow-query-log.md) feature allows MariaDB to have `ANALYZE` output of slow queries printed into the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/) (see [MDEV-6388](https://jira.mariadb.org/browse/MDEV-6388)).

## See Also

* [ANALYZE FORMAT=JSON](analyze-format-json.md)
* [SHOW ANALYZE](../show/show-analyze.md)
* [ANALYZE TABLE](../../table-statements/analyze-table.md)
* JIRA task for ANALYZE statement, [MDEV-406](https://jira.mariadb.org/browse/MDEV-406)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
