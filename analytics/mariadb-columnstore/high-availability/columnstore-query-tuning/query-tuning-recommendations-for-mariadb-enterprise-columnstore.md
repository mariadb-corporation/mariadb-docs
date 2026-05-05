---
description: >-
  Query tuning recommendations for MariaDB Enterprise ColumnStore: select only
  required columns, avoid large single-threaded ORDER BY and LIMIT sorts, and
  follow analytical best practices.
---

# Query Tuning Recommendations

When tuning queries for MariaDB Enterprise ColumnStore, there are some important details to consider.

## Avoid Selecting Unnecessary Columns

Enterprise ColumnStore only reads the columns that are necessary to resolve a query.

For example, the following query selects every column in the table:

```sql
SELECT * FROM tab;
```

Whereas the following query only selects two columns in the table, so it requires less I/O:

```sql
SELECT col1, col2 FROM tab;
```

For best performance, only select the columns that are necessary to resolve a query.

## Avoid Large Sorts

When Enterprise ColumnStore performs `ORDER BY` and `LIMIT` operations, the operations are performed in a single-threaded manner after the rest of the query processing has been completed, and the full unsorted result-set has been retrieved. For large data sets, the performance overhead can be significant.

## Avoid Excessive Aggregations

When Enterprise ColumnStore 5 performs aggregations (i.e., `DISTINCT, GROUP BY, COUNT(*)`, etc.), all of the aggregation work happens in-memory by default. As a consequence, more complex aggregation operations require more memory in that version.

For example, the following query could require a lot of memory in Enterprise ColumnStore 5, since it has to calculate many distinct values in memory:

```sql
SELECT DISTINCT col1 FROM tab LIMIT 10000;
```

Whereas the following query could require much less memory in Enterprise ColumnStore 5, since it has to calculate fewer distinct values:

```sql
SELECT DISTINCT col1 FROM tab LIMIT 100;
```

In Enterprise ColumnStore 6, disk-based aggregations can be enabled.

For best performance, avoid excessive aggregations or enable disk-based aggregations.

For additional information, see "[Configure Disk-Based Aggregations](../../architecture/mariadb-enterprise-columnstore-query-evaluation.md#configure-disk-based-aggregations)".

## Avoid Non-Distributed Functions

When Enterprise ColumnStore evaluates built-in functions and aggregate functions, it can often evaluate the function in a distributed manner. Distributed evaluation of functions can significantly improve performance.

Enterprise ColumnStore supports distributed evaluation for some built-in functions. For other built-in functions, the function must be evaluated serially on the final result set.

Enterprise ColumnStore also supports distributed evaluation for user-defined functions developed with [ColumnStore's User-Defined Aggregate Function (UDAF) C++ API](query-tuning-recommendations-for-mariadb-enterprise-columnstore.md#user-defined-aggregate-function-udaf-c-api). For functions developed with Enterprise Server's standard User-Defined Function (UDF) API, the function must be evaluated serially on the final result set.

For best performance, avoid non-distributed functions.

## Optimize Large Joins

By default, Enterprise ColumnStore performs all joins as in-memory hash joins.

If the joined tables are very large, the in-memory hash join can require too much memory for the default configuration. There are a couple options to work around this:

* Enterprise ColumnStore can be configured to use more memory for in-memory hash joins.
* Enterprise ColumnStore can be configured to use disk-based joins.
* Enterprise ColumnStore can use optimizer statistics to better optimize the join order.

For additional information, see "[Configure In-Memory Joins](../../architecture/mariadb-enterprise-columnstore-query-evaluation.md#configure-in-memory-joins)", "[Configure Disk-Based Joins](../../architecture/mariadb-enterprise-columnstore-query-evaluation.md#configure-disk-based-joins)", and "[Optimizer Statistics](collect-statistics-with-analyze-table-for-mariadb-enterprise-columnstore.md)".

## Load Ordered Data in Proper Order

Enterprise ColumnStore uses extent elimination to optimize queries. [Extent elimination](../../architecture/mariadb-enterprise-columnstore-query-evaluation.md#extent-elimination) uses the minimum and maximum values in the [extent map](../../architecture/columnstore-storage-architecture.md#extent-map) to determine which extents can be skipped for a query.

When data is loaded into Enterprise ColumnStore, it appends the data to the latest extent. When an extent reaches the maximum number of column values, Enterprise ColumnStore creates a new extent. As a consequence, if ordered data is loaded in its proper order, then similar values will be clustered together in the same extent. This can improve query performance, because extent elimination performs best when similar values are clustered together.

For example, if you expect to query a table with a filter on a timestamp column, you should sort the data using the timestamp column before loading it into Enterprise ColumnStore. Later, when the table is queried with a filter on the timestamp column, Enterprise ColumnStore would be able to skip many extents using extent elimination.

For best performance, load ordered data in proper order.

## Enable Decimal Overflow Checks

When Enterprise ColumnStore performs mathematical operations with very big values using the [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal), [NUMERIC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/numeric), and [FIXED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/fixed) data types, the operation can sometimes overflow ColumnStore's maximum precision or scale. The maximum precision and scale depend on the version of Enterprise ColumnStore:

* In Enterprise ColumnStore 6, the maximum precision (M) is 38, and the maximum scale (D) is 38.
* In Enterprise ColumnStore 5, the maximum precision (M) is 18, and the maximum scale (D) is 18.

In Enterprise ColumnStore 6, applications can configure Enterprise ColumnStore to check for decimal overflows by setting the `columnstore_decimal_overflow_check` system variable, but only when the column has a decimal precision that is 18 or more:

```sql
SET SESSION columnstore_decimal_overflow_check=ON;

SELECT (big_decimal1 * big_decimal2) AS product
FROM columnstore_tab;
```

When decimal overflow checks are enabled, math operations have extra overhead.

When the decimal overflow check fails, MariaDB Enterprise ColumnStore raises an error with the `ER_INTERNAL_ERROR` error SQL, and it writes detailed information about the overflow check failure to the ColumnStore system logs.

## User-Defined Aggregate Function (UDAF) C++ API

MariaDB Enterprise ColumnStore supports Enterprise Server's standard User-Defined Function (UDF) API. However, UDFs developed using that API cannot be executed in a distributed manner.

To support distributed execution of custom SQL, MariaDB Enterprise ColumnStore supports a Distributed User Defined Aggregate Functions (UDAF) C++ API:

* The Distributed User Defined Aggregate Functions (UDAF) C++ API allows anyone to create aggregate functions of arbitrary complexity for distributed execution in the ColumnStore storage engine.
* These functions can also be used as Analytic (Window) functions just like any built-in aggregate function.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
