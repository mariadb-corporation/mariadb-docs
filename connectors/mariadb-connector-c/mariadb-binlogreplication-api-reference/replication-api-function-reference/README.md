---
description: >-
  All functions in the Binlog/Replication API are defined in
  include/mariadb_rpl.h
---

# Replication API Function Reference

The Binlog/Replication API provides a low‑level interface for consuming and processing binary log events from a MariaDB server. It allows applications to configure replication handles, open streams, fetch and decode events, and manage errors.

Together, these functions enable developers to build custom replication clients and event processing tools.

## Function Overview

| Function                                                     | Description                                                     |
| ------------------------------------------------------------ | --------------------------------------------------------------- |
| [`mariadb_rpl_init()` ](mariadb_rpl_init.md)                 | Allocates and initializes a replication handle                  |
| [`mariadb_rpl_optionsv()`](mariadb_rpl_optionsv.md)          | Sets options on a replication handle                            |
| [`mariadb_rpl_get_optionsv()`](mariadb_rpl_get_optionsv.md)  | Retrieves the current value of a replication handle option      |
| [`mariadb_rpl_open()`](mariadb_rpl_open.md)                  | Opens a binary log stream and registers the client as a replica |
| [`mariadb_rpl_fetch()`](mariadb_rpl_fetch.md)                | Fetches the next event from a binary log stream                 |
| [`mariadb_free_rpl_event()`](mariadb_free_rpl_event.md)      | Frees memory allocated for an event                             |
| [`mariadb_rpl_extract_rows()`](mariadb_rpl_extract_rows.md)  | Extracts a list of rows from a row event                        |
| [`mariadb_rpl_errno()`](mariadb_rpl_errno.md)                | Returns the error number for the last Binlog API call           |
| [`mariadb_rpl_error()`](mariadb_rpl_error.md)                | Returns the error message for the last Binlog API call          |
| [`mariadb_rpl_close()`](mariadb_rpl_close.md)                | Closes a binary log stream and frees the replication handle     |

## See Also

* [MariaDB Binlog/Replication API Reference](../)
* [Replication API Types and Definitions](../replication-api-types-and-definitions.md)
* [Replication API Function Reference](./)
