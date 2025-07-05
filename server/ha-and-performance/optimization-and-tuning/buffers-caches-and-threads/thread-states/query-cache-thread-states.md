# Query Cache Thread States

This article documents thread states that are related to the [Query Cache](../query-cache.md). These correspond to the `STATE` values listed by the [SHOW PROCESSLIST](../../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md) statement or in the [Information Schema PROCESSLIST Table](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) as well as the `PROCESSLIST_STATE` value listed in the [Performance Schema threads Table](../../../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md).

| Value                               | Description                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------- |
| Value                               | Description                                                                     |
| checking privileges on cached query | Checking whether the user has permission to access a result in the query cache. |
| checking query cache for query      | Checking whether the current query exists in the query cache.                   |
| invalidating query cache entries    | Marking query cache entries as invalid as the underlying tables have changed.   |
| sending cached result to client     | A result found in the query cache is being sent to the client.                  |
| storing result in query cache       | Saving the result of a query into the query cache.                          |
| Waiting for query cache lock        | Waiting to take a query cache lock.                                             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
