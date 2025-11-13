# CHECK TABLE

## Syntax

```sql
CHECK TABLE tbl_name [, tbl_name] ... [option] ...

option = {FOR UPGRADE | QUICK | FAST | MEDIUM | EXTENDED | CHANGED}
```

## Description

`CHECK TABLE` checks a table or tables for errors. `CHECK TABLE` works for [Archive](../../../server-usage/storage-engines/archive.md), [Aria](../../../server-usage/storage-engines/aria/), [CSV](../../../server-usage/storage-engines/csv/), [InnoDB](../../../server-usage/storage-engines/innodb/), [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/), and, from [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.0), [Sequence](../../../server-usage/storage-engines/sequence-storage-engine.md) tables. For Aria and MyISAM tables, the key statistics are updated as well. For CSV, see also [Checking and Repairing CSV Tables](../../../server-usage/storage-engines/csv/checking-and-repairing-csv-tables.md).

As an alternative, [myisamchk](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) is a command-line tool for checking MyISAM tables when the tables are not being accessed. For Aria tables, there is a similar tool: [aria\_chk](../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md).

For checking [dynamic columns](../../sql-structure/nosql/dynamic-columns.md)' integrity, [COLUMN\_CHECK()](../../sql-structure/nosql/dynamic-columns.md#column_check) can be used.

`CHECK TABLE` can also check views for problems, such as tables that are referenced in the view definition that no longer exist.

`CHECK TABLE` is also supported for partitioned tables. You can use [`ALTER TABLE ... CHECK PARTITION`](../data-definition/alter/alter-table/#check-partition) to check one or more partitions.

The meaning of the different options is as follows - note that this can vary a bit between storage engines:

| Option      | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FOR UPGRADE | Do a very quick check if the storage format for the table has changed so that one needs to do a `REPAIR`. This is only needed when one upgrades between major versions of MariaDB or MySQL. This is usually done by [running mariadb-upgrade](../../../server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/migrating-to-mariadb-from-mysql-obsolete-articles/upgrading-to-mariadb-from-mysql-50-or-older.md). |
| FAST        | Only check tables that has not been closed properly or are marked as corrupt. Only supported by the MyISAM and Aria engines. For other engines the table is checked normally                                                                                                                                                                                                                                                                   |
| CHANGED     | Check only tables that have changed since the last `REPAIR` / `CHECK`. Only supported by the MyISAM and Aria engines. For other engines, the table is checked normally.                                                                                                                                                                                                                                                                        |
| QUICK       | Do a fast check. For MyISAM and Aria, this means skipping the check of the delete link chain, which may take some time.                                                                                                                                                                                                                                                                                                                        |
| MEDIUM      | Scan also the data files. Checks the integrity between data and index files with checksums. In most cases, this should find all possible errors.                                                                                                                                                                                                                                                                                               |
| EXTENDED    | Does a full check to verify every possible error. For InnoDB, Aria, and MyISAM, verify for each row that all its keys exist, and for those index keys, they point back to the primary clustered key. This may take a long time on large tables.                                                                                                                                                                                                |

{% tabs %}
{% tab title="Current" %}
The `EXTENDED` option is available to InnoDB, too.
{% endtab %}

{% tab title="< 10.9.4 / 10.8.6 / 10.7.7 / 10.6.11" %}
The `EXTENDED` option is ignored by InnoDB.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
When the `EXTENDED` option is given, MariaDB also checks for referential integrity.
{% endtab %}

{% tab title="< 11.8" %}
MariaDB does not check for referential integrity, even if the `EXTENDED` option is given.
{% endtab %}
{% endtabs %}

For most cases, running `CHECK TABLE` without options or `MEDIUM` should be good enough.

The [Aria](../../../server-usage/storage-engines/aria/) storage engine supports [progress reporting](../administrative-sql-statements/show/show-processlist.md) for this statement.

If you want to know if two tables are identical, take a look at [CHECKSUM TABLE](checksum-table.md).

## InnoDB

If `CHECK TABLE` finds an error in an InnoDB table, MariaDB might shut down to prevent the error propagation. In this case, the problem will be reported in the error log. Otherwise, the table or an index might be marked as corrupted, to prevent use. This does not happen with some minor problems, like a wrong number of entries in a secondary index. Those problems are reported in the output of `CHECK TABLE`.

Each tablespace contains a header with metadata. This header is not checked by this statement.

During the execution of `CHECK TABLE`, other threads may be blocked.

## Examples

```sql
CHECK TABLE y EXTENDED;
+--------+-------+----------+----------+
| Table  | Op    | Msg_type | Msg_text |
+--------+-------+----------+----------+
| test.y | check | status   | OK       |
+--------+-------+----------+----------+
```

In newer MariaDB versions, the `EXTENDED` clause provides more information:

```sql
CHECK TABLE t1 EXTENDED;
+---------+-------+----------+----------------------------------------------------------------------+
| Table   | Op    | Msg_type | Msg_text                                                             |
+---------+-------+----------+----------------------------------------------------------------------+
| test.t1 | check | Warning  | No suitable key found for foreign key t2_ibfk_1 in table test.t1    |
+---------+-------+----------+----------------------------------------------------------------------+

CHECK TABLE t2 EXTENDED;
+---------+-------+----------+--------------------------------------------------------------------------------------------------+
| Table   | Op    | Msg_type | Msg_text                                                                                         |
+---------+-------+----------+--------------------------------------------------------------------------------------------------+
| test.t2 | check | status   | Cannot add or update a child row: a foreign key constraint fails (Key: t2_ibfk_1, record: '2')  |
| test.t2 | check | status   | Cannot add or update a child row: a foreign key constraint fails (Key: t2_ibfk_1, record: '2')  |
| test.t2 | check | status   | Cannot add or update a child row: a foreign key constraint fails (Key: t2_ibfk_1, record: '3')  |
| test.t2 | check | error    | Corrupt                                                                                          |
+---------+-------+----------+--------------------------------------------------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
