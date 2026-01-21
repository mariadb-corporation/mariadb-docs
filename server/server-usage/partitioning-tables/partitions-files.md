---
description: >-
  Learn how MariaDB stores partitioned tables on the filesystem, typically
  creating separate .ibd files for each partition when using InnoDB.
---

# Partitions Files

A partitioned table is stored in multiple files. By default, these files are stored in the MariaDB (or InnoDB) data directory. It is possible to keep them in different paths by specifying [DATA\_DIRECTORY and INDEX\_DIRECTORY](../../reference/sql-statements/data-definition/create/create-table.md#data-directoryindex-directory) table options. This is useful to store different partitions on different devices.

Note that, if the [innodb\_file\_per\_table](../storage-engines/innodb/innodb-system-variables.md) server system variable is set to 0 at the time of the table creation, all partitions are stored in the system tablespace.

The following files exist for each partitioned tables:

| File name                         | Notes                                                                                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| table\_name.frm                   | Contains the table definition. Non-partitioned tables have this file, too.                                          |
| table\_name.par                   | Contains the partitions definitions.                                                                                |
| table\_name#P#partition\_name.ext | Normal files created by the storage engine use this pattern for names. The extension depends on the storage engine. |

For example, an InnoDB table with 4 partitions will have the following files:

```bash
orders.frm
orders.par
orders#P#p0.ibd
orders#P#p1.ibd
orders#P#p2.ibd
orders#P#p3.ibd
```

If we convert the table to MyISAM, we will have these files:

```bash
orders.frm
orders.par
orders#P#p0.MYD
orders#P#p0.MYI
orders#P#p1.MYD
orders#P#p1.MYI
orders#P#p2.MYD
orders#P#p2.MYI
orders#P#p3.MYD
orders#P#p3.MYI
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
