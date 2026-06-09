# mariadb\_free\_rpl\_event()

Frees the memory allocated for a `MARIADB_RPL_EVENT` structure returned by [`mariadb_rpl_fetch()`](mariadb_rpl_fetch.md).

### Syntax

```sql
#include <mariadb_rpl.h>

void mariadb_free_rpl_event(MARIADB_RPL_EVENT *event);
```

### Parameters

| Parameter | Description                                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------------------------- |
| `event`   | A pointer previously returned by [`mariadb_rpl_fetch()`](mariadb_rpl_fetch.md). Passing `NULL` is safe and has no effect. |

### Return Value

None

### Notes

Avoid calling this function on an event pointer that will be passed back to [`mariadb_rpl_fetch()`](mariadb_rpl_fetch.md) for reuse. Only call it when you are done processing the event and will not reuse the pointer.

### History

Added in [MariaDB Connector/C 3.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/c/3.1/3.1.0).

### See Also

* [`mariadb_rpl_fetch()`](mariadb_rpl_fetch.md)

