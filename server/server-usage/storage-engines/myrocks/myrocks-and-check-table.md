---
description: >-
  Details on using the CHECK TABLE statement with MyRocks to verify the
  integrity of tables and indexes, and how it differs from other engines.
---

# MyRocks CHECK TABLE

MyRocks supports the [CHECK TABLE](../../../reference/sql-statements/table-statements/check-table.md) command.

The command will do a number of checks to verify that the table data is self-consistent.

The details about the errors are printed into the [error log](../../../server-management/server-monitoring-logs/error-log.md).\
If [log\_warnings](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) > 2, the error log will also have some informational messages which can help with troubleshooting.

Besides this, RocksDB has its own (low-level) log in `#rocksdb/LOG` file.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
