# SELECT Modifier Hints

## HIGH PRIORITY

`HIGH_PRIORITY` gives the statement a higher priority. If the table is locked, high priority `SELECT`s will be executed as soon as the lock is released, even if other statements are queued. `HIGH_PRIORITY` applies only if the storage engine only supports table-level locking (`MyISAM`, `MEMORY`, `MERGE`). See [HIGH\_PRIORITY and LOW\_PRIORITY clauses](../../../reference/sql-statements/data-manipulation/changing-deleting-data/high_priority-and-low_priority.md) for details.

## SQL\_CACHE / SQL\_NO\_CACHE

If the [query\_cache\_type](../system-variables/server-system-variables.md#query_cache_type) system variable is set to 2 or `DEMAND`, and the current statement is cacheable, `SQL_CACHE` causes the query to be cached and `SQL_NO_CACHE` causes the query not to be cached. For `UNION`s, `SQL_CACHE` or `SQL_NO_CACHE` should be specified for the first query. See also [The Query Cache](../buffers-caches-and-threads/query-cache.md) for more detail and a list of the types of statements that aren't cacheable.

## SQL\_BUFFER\_RESULT

`SQL_BUFFER_RESULT` forces the optimizer to use a temporary table to process the result. This is useful to free locks as soon as possible.

## SQL\_SMALL\_RESULT / SQL\_BIG\_RESULT

`SQL_SMALL_RESULT` and `SQL_BIG_RESULT` tell the optimizer whether the result is very big or not. Usually, `GROUP BY` and `DISTINCT` operations are performed using a temporary table. Only if the result is very big, using a temporary table is not convenient. The optimizer automatically knows if the result is too big, but you can force the optimizer to use a temporary table with `SQL_SMALL_RESULT`, or avoid the temporary table using `SQL_BIG_RESULT`.

## STRAIGHT\_JOIN

`STRAIGHT_JOIN` applies to the [JOIN](../../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax.md) queries, and tells the optimizer that the tables must be read in the order they appear in the `SELECT`. For `const` and `system` table this options is sometimes ignored.

## SQL\_CALC\_FOUND\_ROWS

`SQL_CALC_FOUND_ROWS` is only applied when using the `LIMIT` clause. If this option is used, MariaDB will count how many rows would match the query, without the `LIMIT` clause. That number can be retrieved in the next query, using [FOUND\_ROWS()](../../../reference/sql-functions/secondary-functions/information-functions/found_rows.md).

## USE/FORCE/IGNORE INDEX

`USE INDEX`, `FORCE INDEX` and `IGNORE INDEX` constrain the query planning to a specific index. For further information about some of these options, see [How to force query plans](../query-optimizations/index-hints-how-to-force-query-plans.md).
