# Condition Pushdown into Derived Table Optimization

If a query uses a derived table (or a view), the first action that the query optimizer will attempt is to apply the [derived-table-merge-optimization](derived-table-merge-optimization.md) and merge the derived table into its parent select. However, that optimization is only applicable when the select inside the derived table has a join as the top-level operation. If it has a [GROUP-BY](../../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md), [DISTINCT](../../../../reference/sql-statements/data-manipulation/selecting-data/select.md#distinct), or uses [window functions](../../../../reference/sql-functions/special-functions/window-functions/), then [derived-table-merge-optimization](derived-table-merge-optimization.md) is not applicable.

In that case, the Condition Pushdown optimization is applicable.

## Introduction to Condition Pushdown

Consider an example

```sql
CREATE VIEW OCT_TOTALS AS
SELECT
  customer_id,
  SUM(amount) AS TOTAL_AMT
FROM orders
WHERE  order_date BETWEEN '2017-10-01' AND '2017-10-31'
GROUP BY customer_id;

SELECT * FROM OCT_TOTALS WHERE customer_id=1
```

The naive way to execute the above is to

1. Compute the OCT\_TOTALS contents (for all customers).
2. The, select the line with customer\_id=1

This is obviously inefficient, if there are 1000 customers, then one will be doing up to 1000 times more work than necessary.

However, the optimizer can take the condition `customer_id=1` and push it down into the OCT\_TOTALS view.

Inside the OCT\_\TOTALS, the added condition is put into its HAVING clause, so we end up with:

```sql
SELECT
  customer_id,
  SUM(amount) AS TOTAL_AMT
FROM orders
WHERE  order_date BETWEEN '2017-10-01' AND '2017-10-31'
GROUP BY customer_id
HAVING
  customer_id=1 
```

Then, parts of HAVING clause that refer to GROUP BY columns are moved into the WHERE clause:

```sql
SELECT
  customer_id,
  SUM(amount) AS TOTAL_AMT
FROM orders
WHERE
  order_date BETWEEN '2017-10-01' AND '2017-10-31' AND
  customer_id=1
GROUP BY customer_id
```

Once a restriction like `customer_id=1` is in the WHERE, the query optimizer can use it to construct efficient table access paths.

## Controlling the Optimization

The optimization is enabled by default. One can disable it by setting the [`optimizer_switch`](../optimizer-switch.md) flag `condition_pushdown_for_derived` to OFF.

The pushdown from HAVING to WHERE part is controlled by `condition_pushdown_from_having` flag in [`optimizer_switch`](../optimizer-switch.md).

{% tabs %}
{% tab title="Current" %}
From MariaDB 12.1, it is possible to enable or disable the optimization with an optimizer hint, [DERIVED\_CONDITION\_PUSHDOWN and NO\_DERIVED\_CONDITION\_PUSHDOWN](../../optimizer-hints/#derived_condition_pushdown-and-no_derived_condition_pushdown).
{% endtab %}

{% tab title="<12.1" %}
No optimizer hint is available.
{% endtab %}
{% endtabs %}

## See Also

* Condition Pushdown through Window Functions (since [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103))
* [Condition Pushdown into IN Subqueries](../subquery-optimizations/condition-pushdown-into-in-subqueries.md) (since [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104))
* The Jira task for the feature is [MDEV-9197](https://jira.mariadb.org/browse/MDEV-9197).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
