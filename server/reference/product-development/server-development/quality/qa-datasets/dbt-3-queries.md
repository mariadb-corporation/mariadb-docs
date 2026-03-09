---
description: >-
  Information on the standardized datasets and database dumps used for DBT-3
  Queries tests.
---

# DBT-3 Queries

## Q1

See [MDEV-4309](https://jira.mariadb.org/browse/MDEV-4309) (just speeding up temptable-based GROUP BY execution). Optimizer seems to make a good choice here.

```
SELECT
        l_returnflag,
        l_linestatus,
        SUM(l_quantity) AS sum_qty,
        SUM(l_extendedprice) AS sum_base_price,
        SUM(l_extendedprice * (1 - l_discount)) AS sum_disc_price,
        SUM(l_extendedprice * (1 - l_discount) * (1 + l_tax)) AS sum_charge,
        AVG(l_quantity) AS avg_qty,
        AVG(l_extendedprice) AS avg_price,
        AVG(l_discount) AS avg_disc,
        COUNT(*) AS count_order
FROM
        lineitem
WHERE
        l_shipdate <= date_sub('1998-12-01', INTERVAL 63 DAY)
GROUP BY
        l_returnflag,
        l_linestatus
ORDER BY
        l_returnflag,
        l_linestatus
```

## Q4

See [MDEV-6015](https://jira.mariadb.org/browse/MDEV-6015).

Applicable optimizations:

* subquery cache brings no benefit because subquery refers to outer\_table.pk, which is different for each row
* EXISTS-to-IN is applicable
  * After that, BKA brings slight speedup

Comments on query plan choice

* It seems, we're using the best possible query plan here.

```
SELECT
	o_orderpriority,
	COUNT(*) AS order_count
FROM
	orders
WHERE
	o_orderdate >= '1995-06-06'
	AND o_orderdate < date_add('1995-06-06', INTERVAL 3 MONTH)
	AND EXISTS (
		SELECT
			*
		FROM
			lineitem
		WHERE
			l_orderkey = o_orderkey
			AND l_commitdate < l_receiptdate
	)
GROUP BY
	o_orderpriority
ORDER BY
	o_orderpriority;
```

.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
