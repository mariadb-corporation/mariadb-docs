---
description: >-
  The format_path function replaces specific system paths in a given string with
  their corresponding system variable names for better readability.
---

# format\_path

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.format_path(path)
```

## Description

`format_path` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../) that, given a path, returns a modified path after replacing subpaths matching the values of various system variables with the variable name.

The system variables that are matched are, in order:

* [datadir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir)
* [tmpdir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tmpdir)
* [slave\_load\_tmpdir](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_load_tmpdir)
* [innodb\_data\_home\_dir](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_data_home_dir)
* [innodb\_log\_group\_home\_dir](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_group_home_dir)
* [innodb\_undo\_directory](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_undo_directory)
* [basedir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#basedir)

## Examples

```sql
SELECT @@tmpdir;
+------------------------------------+
| @@tmpdir                           |
+------------------------------------+
| /home/ian/sandboxes/msb_10_8_2/tmp |
+------------------------------------+

SELECT sys.format_path('/home/ian/sandboxes/msb_10_8_2/tmp/testdb.ibd');
+------------------------------------------------------------------+
| sys.format_path('/home/ian/sandboxes/msb_10_8_2/tmp/testdb.ibd') |
+------------------------------------------------------------------+
| @@tmpdir/testdb.ibd                                              |
+------------------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
