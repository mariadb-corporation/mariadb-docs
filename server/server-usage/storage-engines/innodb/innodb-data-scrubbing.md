---
description: >-
  This feature allows for the secure deletion of data by overwriting deleted
  records in tablespaces and logs to prevent data recovery.
---

# InnoDB Data Scrubbing

Sometimes there is a requirement that when some data is deleted, it is really gone. This might be the case when one stores user's personal information or some other sensitive data. Normally though, when a row is deleted, the space is only marked as free on the page. It may eventually be overwritten, but there is no guarantee when that will happen. A copy of the deleted rows may also be present in the log files.

Support for [InnoDB](./) data scrubbing: Background threads periodically scan tablespaces and logs and remove all data that should be deleted. The number of background threads for tablespace scans is set by [innodb-encryption-threads](innodb-system-variables.md). Log scrubbing happens in a separate thread.

To configure scrubbing one can use the following variables:

|                                                                                                                       |           |                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------- |
| [innodb-immediate-scrub-data-uncompressed](innodb-system-variables.md#innodb_immediate_scrub_data_uncompressed)       | Boolean   | Enable scrubbing of uncompressed data.                                                          |

Redo log scrubbing is not supported ([MDEV-21870](https://jira.mariadb.org/browse/MDEV-21870)). If old log contents should be kept secret, enabling [innodb\_encrypt\_log](innodb-system-variables.md#innodb_encrypt_log) or setting a smaller [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) could help.

## Thanks

* Scrubbing was donated to the MariaDB project by Google.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
