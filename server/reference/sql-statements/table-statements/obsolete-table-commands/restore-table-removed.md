# RESTORE TABLE (removed)

{% hint style="warning" %}
`RESTORE TABLE` was removed and is no longer a part of MariaDB.
{% endhint %}

## Syntax

```bnf
RESTORE TABLE tbl_name [, tbl_name] ... FROM '/path/to/backup/directory'
```

## Description

#### Note:

Like [BACKUP TABLE](backup-table-removed.md), this command was not reliable and has been removed from MariaDB. For doing a backup of MariaDB use [mysqldump](../../../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md), [mysqlhotcopy](../../../../clients-and-utilities/legacy-clients-and-utilities/mysqlhotcopy.md) or [XtraBackup](../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md). See [Backing Up and Restoring](../../../../server-usage/backup-and-restore/).

`RESTORE TABLE` restores the table or tables from a backup that was made with [BACKUP TABLE](backup-table-removed.md). The\
directory should be specified as a full path name.

Existing tables are not overwritten; if you try to restore over an existing table, an error occurs. Just as for `BACKUP TABLE`,`RESTORE TABLE` works only for [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/) tables. Restored tables are not replicated from master to slave.

The backup for each table consists of its .frm format file and `.MYD` data file. The restore operation restores those files, and then uses them to rebuild the `.MYI` index file. Restoring takes longer than\
backing up due to the need to rebuild the indexes. The more indexes the table has, the longer it takes.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
