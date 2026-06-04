# BACKUP TABLE (removed)

{% hint style="warning" %}
`BACKUP TABLE` was removed and is no longer a part of MariaDB
{% endhint %}

## Syntax

```bnf
BACKUP TABLE tbl_name [, tbl_name] ... TO '/path/to/backup/directory'
```

## Description

**Note:** Like [RESTORE TABLE](restore-table-removed.md), this command was not reliable and has been removed in current versions of MariaDB.

For doing a backup of MariaDB use [mysqldump](../../../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md) or [MariaDB Backup](../../../../server-usage/backup-and-restore/mariadb-backup/). See [Backing Up and Restoring](../../../../server-usage/backup-and-restore/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
