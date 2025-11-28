---
description: >-
  The sys_config table holds persistent configuration options for the Sys
  Schema, stored using the Aria storage engine to maintain settings across
  restarts.
---

# Sys Schema sys\_config Table

{% include "../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

The _sys.sys\_config_ table holds configuration options for the [Sys Schema](./).

This is a persistent table (using the [Aria](../../../server-usage/storage-engines/aria/) storage engine), with the configuration persisting across upgrades (new options are added with [INSERT IGNORE](../../sql-statements/data-manipulation/inserting-loading-data/insert-ignore.md).

The table also has two related triggers, which maintain the user that INSERTs or UPDATEs the configuration - sys\_config\_insert\_set\_user and sys\_config\_update\_set\_user respectively.

Its structure is as follows:

```sql
+----------+--------------+------+-----+-------------------+-----------------------------+
| Field    | Type         | Null | Key | Default           | Extra                       |
+----------+--------------+------+-----+-------------------+-----------------------------+
| variable | varchar(128) | NO   | PRI | NULL              |                             |
| value    | varchar(128) | YES  |     | NULL              |                             |
| set_time | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
| set_by   | varchar(128) | YES  |     | NULL              |                             |
+----------+--------------+------+-----+-------------------+-----------------------------+
```

{% hint style="warning" %}
Note, when functions check for configuration options, they first check whether a similar named user variable exists with a value, and if this is not set then pull the configuration option from this table in to that named user variable. This is done for performance reasons (to not continually `SELECT` from the table), however this comes with the side effect that once inited, the values last with the session, somewhat like how session variables are inited from global variables. If the values within this table are changed, they will not take effect until the user logs in again.
{% endhint %}

### Options Included

| Variable                               | Default Value | Description                                                                                                                                                                                                          |
| -------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| statement\_truncate\_len               | 64            | Sets the size to truncate statements to, for the [format\_statement](sys-schema-stored-functions/format_statement.md) function.                                                                                      |
| statement\_performance\_analyzer.limit | 100           | The maximum number of rows to include for the views that does not have a built-in limit (e.g. the 95th percentile view). If not set the limit is 100.                                                                |
| statement\_performance\_analyzer.view  | NULL          | Used together with the 'custom' view. If the value contains a space, it is considered a query, otherwise it must be an existing view querying the performance\_schema.events\_statements\_summary\_by\_digest table. |
| diagnostics.allow\_i\_s\_tables        | OFF           | Specifies whether it is allowed to do table scan queries on information\_schema.TABLES for the diagnostics procedure.                                                                                                |
| diagnostics.include\_raw               | OFF           | Set to 'ON' to include the raw data (e.g. the original output of "SELECT \* FROM sys.metrics") for the diagnostics procedure.                                                                                        |
| ps\_thread\_trx\_info.max\_length      | 65535         | Sets the maximum output length for JSON object output by the ps\_thread\_trx\_info() function.                                                                                                                       |

### Notes

Some early versions of _sys\_config_ were stored in [InnoDB](../../../server-usage/storage-engines/innodb/) format.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
