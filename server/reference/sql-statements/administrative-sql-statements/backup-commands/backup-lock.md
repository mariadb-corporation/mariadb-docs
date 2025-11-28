---
description: >-
  Protect table files during backups. This command blocks DDL operations like
  ALTER TABLE while allowing read/write activity, ensuring file consistency for
  backup tools.
---

# BACKUP LOCK

`BACKUP LOCK` blocks a table from DDL statements. This is mainly intended to be used by tools like [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/) that need to ensure there are no DDL[^1] statements on a table while the table files are opened. For example, for an Aria table that stores data in 3 files with extensions `.frm`, `.MAI` and `.MAD`. Normal read/write operations can continue as normal.

## Syntax

To lock a table:

```sql
BACKUP LOCK table_name
```

To unlock a table:

```sql
BACKUP UNLOCK
```

## Usage in a Backup Tool

```sql
BACKUP LOCK [database.]table_name;
 - Open all files related to a table (for example, t.frm, t.MAI and t.MYD)
BACKUP UNLOCK;
- Copy data
- Close files
```

This ensures that all files are from the same generation, that is created at the same time by the MariaDB server. This works, because the open files will point to the original table files which will not be affected if there is any ALTER TABLE while copying the files.

## Privileges

{% tabs %}
{% tab title="Current" %}
BACKUP LOCK requires the [database LOCK TABLES](../../account-management-sql-statements/grant.md#database-privileges) privileges.
{% endtab %}

{% tab title="< 11.4.1 / 11.3.2 / 11.2.3 / 11.1.4 / 11.0.5" %}
BACKUP LOCK requires the [RELOAD](../../account-management-sql-statements/grant.md#reload) privilege.
{% endtab %}

{% tab title="< 10.11.7 / 10.6.17 / 10.5.24" %}
BACKUP LOCK requires the [RELOAD](../../account-management-sql-statements/grant.md#reload) privilege.
{% endtab %}
{% endtabs %}

## Notes

* The idea is that the `BACKUP LOCK` should be held for as short a time as possible by the backup tool. The time to take an uncontested lock is very short! One can easily do 50,000 locks/unlocks per second on low end hardware.
* One should use different connections for [BACKUP STAGE](backup-stage.md) commands and `BACKUP LOCK`.

## Implementation

* Internally, BACKUP LOCK is implemented by taking an `MDLSHARED_HIGH_PRIO` MDL lock on the table object, which protects the table from any DDL operations.

## See Also

* [BACKUP STAGE](backup-stage.md)
* [MDEV-17309](https://jira.mariadb.org/browse/MDEV-17309) - BACKUP LOCK: DDL locking of tables during backup

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: 
