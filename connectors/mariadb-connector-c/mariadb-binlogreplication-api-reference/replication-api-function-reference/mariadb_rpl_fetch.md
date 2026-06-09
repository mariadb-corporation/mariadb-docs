# mariadb\_rpl\_fetch()

Fetches the next event from an open binary log stream.

### Syntax

```sql
#include <mariadb_rpl.h>

MARIADB_RPL_EVENT *mariadb_rpl_fetch(MARIADB_RPL *rpl,
                                      MARIADB_RPL_EVENT *event);
```

### Parameters

| Parameter | Description                                                                                                                                                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rpl`     | An open replication handle initialized by [mariadb\_rpl\_init()](mariadb_rpl_init.md) and connected by [mariadb\_rpl\_open()](mariadb_rpl_open.md).                                                                                               |
| `event`   | An event returned by a previous call to `mariadb_rpl_fetch`. If this parameter is set to `NULL`, the function allocates new memory for the event. If a non‑NULL value is provided, the existing event structure is overwritten with the new data. |

### Return Value

Returns a pointer to a [`MARIADB_RPL_EVENT`](http://replication-api-data-structures.md/#mariadb_rpl_event) structure containing the next event on success, or `NULL` when the EOF packet is received or an error occurs.

### Note

Event memory must be freed by calling `mariadb_free_rpl_event()` when the event is no longer needed.

### History

Added in [MariaDB Connector/C 3.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/c/3.1/3.1.0).

### See also

* [`mariadb_free_rpl_event()`](mariadb_free_rpl_event.md)&#x20;
* [`mariadb_rpl_extract_rows()`](mariadb_rpl_extract_rows.md)
