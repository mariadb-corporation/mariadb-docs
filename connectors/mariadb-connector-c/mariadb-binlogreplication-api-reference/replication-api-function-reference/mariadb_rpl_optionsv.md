# mariadb\_rpl\_optionsv()

Sets options on a replication handle. All required options must be set before calling [`mariadb_rpl_open()`](mariadb_rpl_open.md).

### Syntax

```sql
#include <mariadb_rpl.h>

int mariadb_rpl_optionsv(MARIADB_RPL *rpl,
                          enum mariadb_rpl_option option,
                          ...);
```

### Parameters

| Parameter | Description                                                                               |
| --------- | ----------------------------------------------------------------------------------------- |
| `rpl`     | A replication handle previously allocated by [`mariadb_rpl_init()`](mariadb_rpl_init.md). |
| `option`  | The option to configure. See the options table below.                                     |
| `...`     | The value for the option. The type varies by option; see the options table.               |

### Options

| Option                        | Type            | Description                                                                                                                                |
| ----------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `MARIADB_RPL_FILENAME`        | `char *`        | Name of the binary log file to open, and its length in bytes.                                                                              |
| `MARIADB_RPL_START`           | `unsigned long` | Binary log position from which to start reading.                                                                                           |
| `MARIADB_RPL_SERVER_ID`       | `uint32_t`      | The server ID to use when registering this client as a replica.                                                                            |
| `MARIADB_RPL_FLAGS`           | `uint32_t`      | Bitmask of protocol flags. See [Replication API Types and Definitions](../replication-api-types-and-definitions.md) for valid flag values. |
| `MARIADB_RPL_VERIFY_CHECKSUM` | `uint32_t`      | CRC32 checksum verification for received events. Added in Connector/C 3.3.5.                                                               |
| `MARIADB_RPL_PORT`            | `uint32_t`      | Port number to report when registering this client as a replica. Added in Connector/C 3.3.5.                                               |
| `MARIADB_RPL_HOST`            | `char *`        | Host name to report when registering this client as a replica. Added in Connector/C 3.3.5.                                                 |
| `MARIADB_RPL_SEMI_SYNC`       | `uint_32_t`     | Enable or disable semi-synchronous replication. Added in Connector/C 3.3.6.                                                                |

### Return Value

Returns zero on success, non-zero on failure.

### History

Added in [MariaDB Connector/C 3.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/c/3.1/3.1.0).

### See also

* [`mariadb_rpl_get_optionsv()`](mariadb_rpl_get_optionsv.md)
* [`mariadb_rpl_open()`](mariadb_rpl_open.md)
