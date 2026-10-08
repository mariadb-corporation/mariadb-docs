---
description: >-
  The file_instances table lists all file objects currently open by the server,
  including filenames and the number of open handles.
---

# Performance Schema file\_instances Table

## Description

The `file_instances` table lists instances of instruments seen by the Performance Schema when executing file I/O instrumentation, and the associated files. Only files that have been opened, and that have not been deleted, will be listed in the table.

The [performance\_schema\_max\_file\_instances](../performance-schema-system-variables.md#performance_schema_max_file_instances) system variable specifies the maximum number of instrumented file objects.

| Column      | Description                                                                                   |
| ----------- | --------------------------------------------------------------------------------------------- |
| FILE\_NAME  | File name.                                                                                    |
| EVENT\_NAME | Instrument name associated with the file.                                                     |
| OPEN\_COUNT | Open handles on the file. A value of greater than zero means that the file is currently open. |

## Example

```sql
SELECT * FROM performance_schema.file_instances WHERE OPEN_COUNT>0;
+----------------------------------------------------+--------------------------------------+------------+
| FILE_NAME                                          | EVENT_NAME                           | OPEN_COUNT |
+----------------------------------------------------+--------------------------------------+------------+
| /var/log/mysql/mariadb-bin.index                   | wait/io/file/sql/binlog_index        |          1 |
| /var/lib/mysql/ibdata1                             | wait/io/file/innodb/innodb_data_file |          2 |
| /var/lib/mysql/ib_logfile0                         | wait/io/file/innodb/innodb_log_file  |          2 |
| /var/lib/mysql/ib_logfile1                         | wait/io/file/innodb/innodb_log_file  |          2 |
| /var/lib/mysql/mysql/gtid_slave_pos.ibd            | wait/io/file/innodb/innodb_data_file |          3 |
| /var/lib/mysql/mysql/innodb_index_stats.ibd        | wait/io/file/innodb/innodb_data_file |          3 |
| /var/lib/mysql/mysql/innodb_table_stats.ibd        | wait/io/file/innodb/innodb_data_file |          3 |
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
