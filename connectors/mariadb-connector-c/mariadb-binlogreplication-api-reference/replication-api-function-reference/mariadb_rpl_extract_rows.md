# mariadb\_rpl\_extract\_rows()

Extracts row data from a replication event and returns a linked list of individual row change records for further processing.

### Syntax

```sql
#include <mariadb_rpl.h>

MARIADB_RPL_ROW *mariadb_rpl_extract_rows(
    MARIADB_RPL *rpl,
    MARIADB_RPL_EVENT *tm_event,
    MARIADB_RPL_EVENT *row_event);
```

### Parameters

| Parameter   | Description                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| `rpl`       | A replication handle previously allocated by [`mariadb_rpl_init()`](mariadb_rpl_init.md).                              |
| `tm_event`  | The last `TABLE_MAP_EVENT`, which defines the table structure and column metadata.                                     |
| `row_event` | The row event (`WRITE_ROWS_EVENT`, `UPDATE_ROWS_EVENT`, or `DELETE_ROWS_EVENT`) containing the raw row data to decode. |

### Return Value

Returns a pointer to a linked list of `MARIADB_RPL_ROW` structures on success, or `NULL` on failure. Each node in the list represents one row in the event.

### History

Added in MariaDB Connector/C 3.3.5.

### See also

* [`mariadb_rpl_fetch()`](mariadb_rpl_fetch.md)
