# CHECKSUM TABLE

## Syntax

```sql
CHECKSUM TABLE tbl_name [, tbl_name] ... [ QUICK | EXTENDED ]
```

## Description

`CHECKSUM TABLE` reports a table checksum. This is very useful if you want to know if two tables are the same (for example on a master and a replica).

With `QUICK`, the live table checksum is reported if it is available, or `NULL` otherwise. This is very fast. A live checksum is enabled by specifying the `CHECKSUM=1` table option when you [create the table](../data-definition/create/create-table.md); currently, this is supported only for [Aria](../../../server-usage/storage-engines/aria/) and [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) tables.

With `EXTENDED`, the entire table is read row by row and the checksum is calculated. This can be very slow for large tables.

If neither `QUICK` nor `EXTENDED` is specified, MariaDB returns a live checksum if the table storage engine supports it and scans the table otherwise.

`CHECKSUM TABLE` requires the [SELECT privilege](../account-management-sql-statements/grant.md#table-privileges) for the table.

For a nonexistent table, `CHECKSUM TABLE` returns`NULL` and generates a warning.

The table row format affects the checksum value. If the row format changes, the checksum will change. This means that when a table created with a MariaDB/MySQL version is upgraded to another version, the checksum value will probably change.

Two identical tables should always match to the same checksum value; however, also for non-identical tables there is a very slight chance that they will return the same value as the hashing algorithm is not completely collision-free.

## Identical Tables

Identical tables mean that the CREATE statement is identical and that the following variable, which affects the storage formats, was the same when the tables were created:

* [mysql56-temporal-format](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format)

## Differences Between MariaDB and MySQL

`CHECKSUM TABLE` may give a different result as MariaDB doesn't ignore `NULL`s in the columns like MySQL 5.1 does (later MySQL versions should calculate checksums the same way as MariaDB).&#x20;

{% tabs %}
{% tab title="Current" %}
You can get the 'old style' checksum in MariaDB by setting [old\_mode](../../../server-management/variables-and-modes/old-mode.md) to [COMPAT\_5\_1\_CHECKSUM](../../../server-management/variables-and-modes/old-mode.md#compat_5_1_checksum). Note, however, that the MyISAM and Aria storage engines in MariaDB are using the new checksum internally, so if you are using this old mode, the `CHECKSUM` command will be slower as it needs to calculate the checksum row by row.
{% endtab %}

{% tab title="< 10.9" %}
You can get the 'old style' checksum in MariaDB by starting [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd.md) with the[--old](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old) option. Note, however, that the MyISAM and Aria storage engines in MariaDB are using the new checksum internally, so if you are using this old mode, the `CHECKSUM` command will be slower as it needs to calculate the checksum row by row.
{% endtab %}
{% endtabs %}

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
