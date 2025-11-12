# REPAIR TABLE

## Syntax

{% tabs %}
{% tab title="Current" %}
```sql
REPAIR [NO_WRITE_TO_BINLOG | LOCAL] TABLE
    tbl_name [, tbl_name] ...
    [QUICK] [EXTENDED] [USE_FRM] [FORCE
```
{% endtab %}

{% tab title="< 11.5" %}
```
REPAIR [NO_WRITE_TO_BINLOG | LOCAL] TABLE
    tbl_name [, tbl_name] ...
    [QUICK] [EXTENDED] [USE_FRM]
```
{% endtab %}
{% endtabs %}

## Description

`REPAIR TABLE` repairs a possibly corrupted table. By default, it has the same effect as

```sql
myisamchk --recover tbl_name
```

or

```sql
aria_chk --recover tbl_name
```

See [aria\_chk](../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md) and [myisamchk](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) for more.

`REPAIR TABLE` works for [Archive](../../../server-usage/storage-engines/archive.md), [Aria](../../../server-usage/storage-engines/aria/), [CSV](../../../server-usage/storage-engines/csv/), and [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) tables. For [InnoDB](../../../server-usage/storage-engines/innodb/), see [recovery modes](../../../server-usage/storage-engines/innodb/innodb-troubleshooting/innodb-recovery-modes.md). For CSV, see also [Checking and Repairing CSV Tables](../../../server-usage/storage-engines/csv/checking-and-repairing-csv-tables.md). For Archive, this statement also improves compression. If the storage engine does not support this statement, a warning is issued.

This statement requires [SELECT and INSERT privileges](../account-management-sql-statements/grant.md) for the table.

By default, `REPAIR TABLE` statements are written to the [binary log](../../../server-management/server-monitoring-logs/binary-log/) and will be [replicated](../../../server-usage/storage-engines/myrocks/myrocks-and-replication.md). The `NO_WRITE_TO_BINLOG` keyword (`LOCAL` is an alias) will ensure the statement is not written to the binary log.

{% tabs %}
{% tab title="Current" %}
`REPAIR TABLE` statements are not logged to the binary log if [read\_only](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_only) is set. See also [Read-Only Replicas](../../../ha-and-performance/standard-replication/read-only-replicas.md).
{% endtab %}

{% tab title="< 10.3.19" %}
`REPAIR TABLE` statements are logged to the binary log.
{% endtab %}
{% endtabs %}

When an index is recreated, the storage engine may use a configurable buffer in the process. Incrementing the buffer speeds up the index creation. [Aria](../../../server-usage/storage-engines/aria/) and [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) allocate a buffer whose size is defined by [aria\_sort\_buffer\_size](../../../server-usage/storage-engines/aria/aria-system-variables.md) or [myisam\_sort\_buffer\_size](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md), also used for [ALTER TABLE](../data-definition/alter/alter-table/).

### QUICK

When specified, `REPAIR TABLE` will not modify the data file, only attempting to repair the index file. The same behavior can be achieved with [myisamchk --recover --quick](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md#repairing-tables).

### EXTENDED

Creates the index row by row rather than sorting and creating a single index. Similar to [myisamchk --safe-recover](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md#repairing-tables).

### USE\_FRM

For use only when the index file is missing or its header corrupted. MariaDB then attempts to recreate it using the `.frm` file. There is no equivalent [myisamchk](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) option.

### FORCE

{% tabs %}
{% tab title="Current" %}
The `FORCE` argument allows to first run internal repair to fix damaged blocks and then follow it up with `ALTER TABLE` ([MDEV-33449](https://jira.mariadb.org/browse/MDEV-33449)).
{% endtab %}

{% tab title="< 11.5" %}
The `FORCE` option is not available.
{% endtab %}
{% endtabs %}

### Partitioned Tables

`REPAIR TABLE` is also supported for [partitioned tables](../../../server-usage/partitioning-tables/) with the [ALTER TABLE ... REPAIR PARTITION](../data-definition/alter/alter-table/) statement. However, the `USE_FRM` option cannot be used with this statement on a partitioned table. See [Repairing Partitions](../../../server-usage/partitioning-tables/partitioning-overview.md#repairing-partitions) for details.

### Progress Reporting

The [Aria](../../../server-usage/storage-engines/aria/) storage engine supports [progress reporting](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) for this statement.

## See Also

* [mariadb-check](../../../clients-and-utilities/table-tools/mariadb-check.md)
* [aria\_chk](../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md)
* [myisamchk](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
