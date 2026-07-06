---
description: >-
  An optimization that can pick a join order which shortens ORDER BY ... LIMIT
  queries.
---

# optimizer\_join\_limit\_pref\_ratio Optimization

## Basics

Off (0) by default, when enabling this optimization, MariaDB will consider a join order that may shorten query execution time based on the `ORDER BY ... LIMIT n` clause. For small values of `n`, this may improve performance.

Set the value of `optimizer_join_limit_pref_ratio` to a non-zero value to enable this option (higher values are more conservative, recommended value is 100), or set to 0 (the default value) to disable it.

## Detailed description

### Problem setting

By default, the MariaDB optimizer picks a join order without considering the ORDER BY ... LIMIT clause, when present.

For example, consider a query looking at latest 10 orders together with customers who made them:

```sql
SELECT *
FROM
  customer,ORDER
WHERE
  customer.name=ORDER.customer_name
ORDER BY
  ORDER.DATE DESC
LIMIT 10
```

The two possible plans are:`customer->orders`:

```
+------+-------------+----------+------+---------------+---------------+---------+---------------+------+----------------------------------------------+
| id   | select_type | table    | type | possible_keys | key           | key_len | ref           | rows | Extra                                        |
+------+-------------+----------+------+---------------+---------------+---------+---------------+------+----------------------------------------------+
|    1 | SIMPLE      | customer | ALL  | name          | NULL          | NULL    | NULL          | 9623 | Using where; Using temporary; Using filesort |
|    1 | SIMPLE      | orders   | ref  | customer_name | customer_name | 103     | customer.name | 1    |                                              |
+------+-------------+----------+------+---------------+---------------+---------+---------------+------+----------------------------------------------+
```

and `orders->customer`:

```
+------+-------------+----------+-------+---------------+------------+---------+----------------------+------+-------------+
| id   | select_type | table    | type  | possible_keys | key        | key_len | ref                  | rows | Extra       |
+------+-------------+----------+-------+---------------+------------+---------+----------------------+------+-------------+
|    1 | SIMPLE      | orders   | index | customer_name | order_date | 4       | NULL                 | 10   | Using where |
|    1 | SIMPLE      | customer | ref   | name          | name       | 103     | orders.customer_name | 1    |             |
+------+-------------+----------+-------+---------------+------------+---------+----------------------+------+-------------+
```

The `customer->orders` plan computes a join between all customers and orders, saves that result into a temporary table, and then uses filesort to get the 10 most recent orders. This query plan doesn't benefit from the fact that just 10 orders are needed.

However, in contrast, the `orders->customers` plan uses an index to read rows in the ORDER BY order. The query can stop execution once it finds 10 `order-and-customer` combinations. This is much faster than computing the entire join. Under this plan, and when this new optimization, we can leverage ORDER BY ... LIMIT to stop early, when we have the 10 combinations.

### Plans with LIMIT shortcuts are difficult to estimate

It is fundamentally difficult to produce a reliable estimate for ORDER BY ... LIMIT shortcuts. Let's take an example from the previous section to see why. This query searches for last 10 orders that were shipped by air:

```sql
SELECT *
FROM
  customer,ORDER
WHERE
  customer.name=ORDER.customer_name 
  AND ORDER.shipping_method='Airplane'
ORDER BY
  ORDER.DATE DESC
LIMIT 10
```

Suppose we know beforehand that 50% of orders are shipped by air.\
Assuming there's no correlation between date and shipping method, `orders->customer` plan will need to scan 20 orders before we find 10 that are shipped by air.\
But if there is correlation, then we may need to scan up to `(total_orders*0.5 + 10)` before we find first 10 orders that are shipped by air. Scanning about 50% of all orders can be expensive.

This situation worsens when the query has constructs whose selectivity is not known. For example, suppose the WHERE condition was

```
order.shipping_method='%Airplane%'
```

in this case, we can't reliably say whether we will be able to stop after scanning #LIMIT rows or we will need to enumerate all rows before we find #LIMIT matches.

## Providing guidelines to the optimizer

Due to these challenges, the optimization is not enabled by default.

When running a mostly OLTP workload such that query WHERE conditions have suitable\
indexes or are not very selective, then any ORDER BY ... LIMIT queries will typically find matching rows\
quickly. In this case, it makes sense to give the following guidance to the optimizer:

```
Do consider the query plan using LIMIT short-cutting 
and prefer it if it promises at least X times speedup.
```

The value of `X` is given to the optimizer via `optimizer_join_limit_pref_ratio` setting.\
Higher values carry less risk. The recommended value is 100: prefer the LIMIT join order if it\
promises at least 100x speedup.

## References

* [MDEV-34720](https://jira.mariadb.org/browse/MDEV-34720) introduces optimizer\_join\_limit\_pref\_ratio optimization
* [MDEV-18079](https://jira.mariadb.org/browse/MDEV-18079) is about future development that would make the optimizer handle such cases without user guidance.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
