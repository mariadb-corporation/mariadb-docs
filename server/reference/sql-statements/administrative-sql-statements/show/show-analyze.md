---
description: >-
  Retrieve runtime statistics for a currently executing query. This statement
  provides insights into query plan execution without waiting for completion.
---

# SHOW ANALYZE

{% hint style="info" %}
`SHOW ANALYZE` was added in MariaDB 10.9.
{% endhint %}

## Syntax

```sql
SHOW ANALYZE [FORMAT=JSON] FOR <connection_id>;
```

## Description

`SHOW ANALYZE` allows one to retrieve [ANALYZE](../analyze-and-explain-statements/analyze-statement.md)-like output from a currently running statement. The statement

```sql
SHOW ANALYZE [FORMAT=JSON] FOR <connection_id>;
```

connects to the query running in connection `connection_id`, gets information about the query plan it is executing, _also gets information about the runtime statistics of the execution so far_ and returns it in a format similar to `ANALYZE [FORMAT=JSON]` output.

This is similar to the [SHOW EXPLAIN](show-explain.md) command, the difference being that `SHOW ANALYZE` also produces runtime statistics information.

## Use Case

You're trying to troubleshoot a query that never finishes. Since it doesn't finish, it is not possible to get [ANALYZE](../analyze-and-explain-statements/analyze-statement.md) output for it. With `SHOW ANALYZE`, you can get the runtime statistics without waiting for the query to finish.

## Examples

### Example 1: Row Counts

Consider the tables `orders` and `customer` and a join query finding the total amount of orders from customers with Gold status:

```sql
EXPLAIN format=json
SELECT sum(orders.amount)
FROM
  customer JOIN orders ON customer.cust_id=orders.cust_id
WHERE
  customer.status='GOLD';
```

The output of this query looks like this:

```
+------+-------------+----------+------+---------------+---------+---------+------------------+--------+-------------+
| id   | select_type | table    | type | possible_keys | key     | key_len | ref              | rows   | Extra       |
+------+-------------+----------+------+---------------+---------+---------+------------------+--------+-------------+
|    1 | SIMPLE      | customer | ALL  | PRIMARY       | NULL    | NULL    | NULL             | 199786 | Using where |
|    1 | SIMPLE      | orders   | ref  | cust_id       | cust_id | 5       | customer.cust_id | 1      |             |
+------+-------------+----------+------+---------------+---------+---------+------------------+--------+-------------+
```

We run the SELECT, and it has been running for 30 seconds. Let's try `SHOW ANALYZE`:

```sql
SHOW ANALYZE format=json FOR 3;
| {
  "r_query_time_in_progress_ms": 32138,
```

The statement shows how long the query has been running.

```json
"query_block": {
    "select_id": 1,
    "r_loops": 1,
    "nested_loop": [
      {
        "table": {
          "table_name": "customer",
          "access_type": "ALL",
          "possible_keys": ["PRIMARY"],
          "r_loops": 1,
          "rows": 199786,
          "r_rows": 110544,
```

`rows` shows the number of rows expected. `r_rows` in shows how many rows were processed so far (110K out of expected 200K). `r_loops` shows we're doing the first table scan (which is obvious for this query plan).

```json
"filtered": 100,
          "r_filtered": 9.538283398,
          "attached_condition": "customer.`status` = 'GOLD'"
        }
      },
      {
        "table": {
          "table_name": "orders",
          "access_type": "ref",
          "possible_keys": ["cust_id"],
          "key": "cust_id",
          "key_length": "5",
          "used_key_parts": ["cust_id"],
          "ref": ["test.customer.cust_id"],
          "r_loops": 10544,
          "rows": 1,
          "r_rows": 99.99222307,
```

`rows: 1` shows the optimizer was expecting 1 order per customer. But `r_rows: 99.9` shows that it has found on average 100 orders per customer. This may be the reason the query is slower than expected.

The final chunk of the output doesn't have anything interesting but here it is:

```json
"filtered": 100,
          "r_filtered": 100
        }
      }
    ]
  }
}
```

### Example 2: Timing Information

Regular SELECT queries collect row count information, so `SHOW ANALYZE` can display it. However, detailed timing information is not collected, as collecting it may have CPU overhead. But if the target query is collecting timing information, `SHOW ANALYZE` will display it. How does one get the target query to collect timing information? Currently there is one way: if the target is running `ANALYZE`, it IS collecting timing information.\
Re-running the previous example:

```sql
Connection 1> ANALYZE SELECT ... ;
```

```sql
Connection 2> SHOW ANALYZE FORMAT=JSON FOR <connection_id>;
ANALYZE
{
  "r_query_time_in_progress_ms": 30727,
  "query_block": {
    "select_id": 1,
    "r_loops": 1,
    "nested_loop": [
      {
        "table": {
          "table_name": "customer",
          "access_type": "ALL",
          "possible_keys": ["PRIMARY"],
          "r_loops": 1,
          "rows": 199786,
          "r_rows": 109994,
          "r_table_time_ms": 232.699,
          "r_other_time_ms": 46.355,
```

`ANALYZE` prints timing information in members named `r_..._time_ms`.\
You can see that, so far, out of 30 seconds, only 232 millisecond were spent in reading the customer table. The bottleneck is elsewhere...

```json
"filtered": 100,
          "r_filtered": 9.085950143,
          "attached_condition": "customer.`status` = 'GOLD'"
        }
      },
      {
        "table": {
          "table_name": "orders",
          "access_type": "ref",
          "possible_keys": ["cust_id"],
          "key": "cust_id",
          "key_length": "5",
          "used_key_parts": ["cust_id"],
          "ref": ["test.customer.cust_id"],
          "r_loops": 9994,
          "rows": 1,
          "r_rows": 99.99779868,
          "r_table_time_ms": 29460.609,
          "r_other_time_ms": 986.842,
```

29.4 seconds were spent reading the orders table (and 0.986 seconds in processing the obtained rows).\
Now we can see where the query is spending time.

```json
"filtered": 100,
          "r_filtered": 100
        }
      }
    ]
  }
}
```

## See Also

* [SHOW EXPLAIN command](show-explain.md)
* [ANALYZE command](../analyze-and-explain-statements/analyze-statement.md)
* [MDEV-27021: Extend SHOW EXPLAIN to support SHOW ANALYZE \[FORMAT=JSON\]](https://jira.mariadb.org/browse/MDEV-27021)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
