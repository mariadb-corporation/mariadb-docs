# mariadb\_rpl\_get\_optionsv()

Retrieves the current value of a replication handle option previously set with [`mariadb_rpl_optionsv()`](mariadb_rpl_optionsv.md).

### Syntax

```sql
#include <mariadb_rpl.h>

int mariadb_rpl_get_optionsv(MARIADB_RPL *rpl,
                               enum mariadb_rpl_option option,
                               ...);
```

### Parameters

| Parameter | Description                                                                               |
| --------- | ----------------------------------------------------------------------------------------- |
| `rpl`     | A replication handle previously allocated by [`mariadb_rpl_init()`](mariadb_rpl_init.md). |
| `option`  | The option to be set, followed by one or more values.                                     |
| `...`     | A pointer to a variable of the appropriate type to receive the option value.              |

### Options

| Option                  | Output type           | Description                                                                             |
| ----------------------- | --------------------- | --------------------------------------------------------------------------------------- |
| `MARIADB_RPL_FILENAME`  | `char **`, `size_t *` | Pointer to the binary log filename and its length.                                      |
| `MARIADB_RPL_START`     | `unsigned long *`     | Start position in the binary log.                                                       |
| `MARIADB_RPL_SERVER_ID` | `uint32_t *`          | Configured server ID.                                                                   |
| `MARIADB_RPL_FLAGS`     | `uint32_t *`          | Current flags bitmask.                                                                  |
| `MARIADB_RPL_SEMI_SYNC` | `uint32_t *`          | Semi-sync replication state: `1` = enabled, `0` = disabled. Added in Connector/C 3.3.6. |

### Return Value

Returns zero on success, non-zero if the option is not recognized.

### History

Added in [MariaDB Connector/C 3.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/c/3.1/3.1.0).

### See also

* [`mariadb_rpl_optionsv()`](mariadb_rpl_optionsv.md)
