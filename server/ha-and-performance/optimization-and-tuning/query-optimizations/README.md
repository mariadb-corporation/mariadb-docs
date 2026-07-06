---
description: >-
  Optimize queries for peak performance. This section provides techniques for
  writing efficient SQL, understanding query execution plans, and leveraging
  indexes effectively to speed up your queries.
---

# Optimizing Queries

{% columns %}
{% column %}
{% content-ref url="aborting-statements.md" %}
[aborting-statements.md](aborting-statements.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to abort statements that exceed a maximum execution time.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="big-deletes.md" %}
[big-deletes.md](big-deletes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for deleting large numbers of rows from big tables efficiently.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="charset-narrowing-optimization.md" %}
[charset-narrowing-optimization.md](charset-narrowing-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Charset Narrowing optimization, which speeds up equality comparisons between columns of different character sets.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-sampling-techniques-for-efficiently-finding-a-random-row.md" %}
[data-sampling-techniques-for-efficiently-finding-a-random-row.md](data-sampling-techniques-for-efficiently-finding-a-random-row.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Efficient techniques for selecting random rows, avoiding a slow ORDER BY RAND().
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-warehousing-high-speed-ingestion.md" %}
[data-warehousing-high-speed-ingestion.md](data-warehousing-high-speed-ingestion.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for high-speed data ingestion when INSERT performance is the bottleneck.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-warehousing-summary-tables.md" %}
[data-warehousing-summary-tables.md](data-warehousing-summary-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Creating and maintaining summary tables to speed up data-warehouse queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-warehousing-techniques.md" %}
[data-warehousing-techniques.md](data-warehousing-techniques.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for improving performance of data-warehouse-style tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="query-optimizations-distinct-removal-in-aggregate-functions.md" %}
[query-optimizations-distinct-removal-in-aggregate-functions.md](query-optimizations-distinct-removal-in-aggregate-functions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the optimizer removes redundant DISTINCT from aggregate-function arguments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="equality-propagation-optimization.md" %}
[equality-propagation-optimization.md](equality-propagation-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The equality propagation optimization, which propagates equality conditions through a query's WHERE clause.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="filesort-with-small-limit-optimization.md" %}
[filesort-with-small-limit-optimization.md](filesort-with-small-limit-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The filesort optimization that uses a priority queue when sorting with a small LIMIT.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="force-index.md" %}
[force-index.md](force-index.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Using FORCE INDEX to make the optimizer use an index instead of a table scan.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="groupwise-max-in-mariadb.md" %}
[groupwise-max-in-mariadb.md](groupwise-max-in-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for finding the largest, or top, row within each group.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="guiduuid-performance.md" %}
[guiduuid-performance.md](guiduuid-performance.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Why random GUID/UUID keys hurt index performance, and how to mitigate it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="hash_join_cardinality-optimizer_switch-flag.md" %}
[hash_join_cardinality-optimizer_switch-flag.md](hash_join_cardinality-optimizer_switch-flag.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The hash_join_cardinality optimizer_switch flag, which affects hash-join cardinality estimates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="how-to-quickly-insert-data-into-mariadb.md" %}
[how-to-quickly-insert-data-into-mariadb.md](how-to-quickly-insert-data-into-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for inserting data into MariaDB as quickly as possible.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ignore-index.md" %}
[ignore-index.md](ignore-index.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Using IGNORE INDEX to tell the optimizer not to consider specific indexes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="index-condition-pushdown.md" %}
[index-condition-pushdown.md](index-condition-pushdown.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Index Condition Pushdown, which pushes WHERE conditions into the index scan to reduce row reads.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="index-hints-how-to-force-query-plans.md" %}
[index-hints-how-to-force-query-plans.md](index-hints-how-to-force-query-plans.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Using index hints to influence the query plan when the optimizer's choice is not ideal.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="index_merge-sort_intersection.md" %}
[index_merge-sort_intersection.md](index_merge-sort_intersection.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The index_merge sort_intersection access method, which merges results from several index scans.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="limit-rows-examined.md" %}
[limit-rows-examined.md](limit-rows-examined.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Using LIMIT ROWS EXAMINED to cap how many rows a query examines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-53-optimizer-debugging.md" %}
[mariadb-53-optimizer-debugging.md](mariadb-53-optimizer-debugging.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An obsolete optimizer-debugging facility from an early MariaDB release (historical).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="not_null_range_scan-optimization.md" %}
[not_null_range_scan-optimization.md](not_null_range_scan-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The not_null_range_scan optimization, which builds range scans from inferred NOT NULL conditions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer-switch.md" %}
[optimizer-switch.md](optimizer-switch.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The optimizer_switch system variable, used to enable or disable individual optimizations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer_adjust_secondary_key_costs.md" %}
[optimizer_adjust_secondary_key_costs.md](optimizer_adjust_secondary_key_costs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The optimizer_adjust_secondary_key_costs setting, which tunes cost estimates for secondary keys.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer_join_limit_pref_ratio-optimization.md" %}
[optimizer_join_limit_pref_ratio-optimization.md](optimizer_join_limit_pref_ratio-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An optimization that can pick a join order which shortens ORDER BY ... LIMIT queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizing-for-latest-news-style-queries.md" %}
[optimizing-for-latest-news-style-queries.md](optimizing-for-latest-news-style-queries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Optimizing queries that fetch the latest items on a topic, such as news feeds.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="pagination-optimization.md" %}
[pagination-optimization.md](pagination-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Efficient pagination techniques for splitting long lists across pages.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="pivoting-in-mariadb.md" %}
[pivoting-in-mariadb.md](pivoting-in-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for pivoting row data into a spreadsheet-like columnar layout.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="query-limits-and-timeouts.md" %}
[query-limits-and-timeouts.md](query-limits-and-timeouts.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The methods MariaDB provides to limit or time out queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="reorder_outer_joins.md" %}
[reorder_outer_joins.md](reorder_outer_joins.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The reorder_outer_joins optimizer_switch flag, which controls reordering of independent outer joins.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rollup-unique-user-counts.md" %}
[rollup-unique-user-counts.md](rollup-unique-user-counts.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Efficiently rolling up unique-user counts without repeatedly reprocessing large logs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rowid-filtering-optimization.md" %}
[rowid-filtering-optimization.md](rowid-filtering-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The rowid filtering optimization, which pre-filters rowids to reduce expensive row lookups.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sargable-date-and-year.md" %}
[sargable-date-and-year.md](sargable-date-and-year.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The sargable DATE and YEAR optimization, letting the optimizer use indexes for certain date and year conditions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sargable-upper.md" %}
[sargable-upper.md](sargable-upper.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The sargable UPPER optimization, letting the optimizer use indexes for UPPER() expressions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="use-index.md" %}
[use-index.md](use-index.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Using USE INDEX to limit which indexes the optimizer considers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="virtual-column-support-in-the-optimizer.md" %}
[virtual-column-support-in-the-optimizer.md](virtual-column-support-in-the-optimizer.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Optimizer support for virtual (generated) columns.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimization-strategies/" %}
[optimization-strategies](optimization-strategies/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discover effective optimization strategies for MariaDB Server queries. This section provides a variety of techniques and approaches to enhance query performance and overall database efficiency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizations-for-derived-tables/" %}
[optimizations-for-derived-tables](optimizations-for-derived-tables/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Optimize derived tables in MariaDB Server queries. This section provides techniques and strategies to improve the performance of subqueries and complex joins, enhancing overall query efficiency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="statistics-for-optimizing-queries/" %}
[statistics-for-optimizing-queries](statistics-for-optimizing-queries/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Utilize statistics to optimize queries in MariaDB Server. This section explains how the database uses statistical information to generate efficient query execution plans and improve performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subquery-optimizations/" %}
[subquery-optimizations](subquery-optimizations/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Optimize subqueries in MariaDB Server for improved performance. This section provides techniques and best practices to ensure your nested queries execute efficiently and enhance overall query speed.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="table-elimination/" %}
[table-elimination](table-elimination/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about table elimination for query optimization in MariaDB Server. This section explains how the optimizer removes unnecessary tables from query plans, improving performance.
{% endcolumn %}
{% endcolumns %}
