---
description: >-
  Defragment the query cache to optimize memory usage. This command reorganizes
  the cache to eliminate fragmentation without removing existing cached queries.
---

# FLUSH QUERY CACHE

## Description

You can defragment [the query cache](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) to better utilize its memory with the `FLUSH QUERY CACHE` statement. The statement does not remove any queries from the cache.

The [RESET QUERY CACHE](../reset.md) statement removes all query results from the query cache.\
The [FLUSH TABLES](flush.md) statement also does this.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
