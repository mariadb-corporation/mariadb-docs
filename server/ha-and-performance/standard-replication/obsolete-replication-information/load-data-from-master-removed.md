# LOAD DATA FROM MASTER (removed)

## Syntax

```bnf
LOAD DATA FROM MASTER
```

## Description

This feature has been removed from recent versions of MariaDB.

Since the current implementation of `LOAD DATA FROM MASTER`\
and [LOAD TABLE FROM MASTER](load-table-from-master-removed.md) is very limited, these statements are deprecated in versions 4.1 of MySQL and above. We will introduce a more\
advanced technique (called "online backup") in a future version. That technique\
will have the additional advantage of working with more storage engines.

For MySQL 5.1 and earlier, the recommended alternative solution to\
using `LOAD DATA FROM MASTER` or`LOAD TABLE FROM MASTER` is using [mysqldump](../../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md) or [mysqlhotcopy](../../../clients-and-utilities/legacy-clients-and-utilities/mysqlhotcopy.md).\
The latter requires Perl and two Perl modules (DBI and DBD:mysql) and works for [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) and [ARCHIVE](../../../server-usage/storage-engines/archive.md) tables only. With mysqldump, you can create SQL dumps on the\
master and pipe (or copy) these to a mysql client on the slave. This has the\
advantage of working for all storage engines, but can be quite slow, since it\
works using `SELECT`.

This statement takes a snapshot of the master and copies it to the slave. It\
updates the values of `MASTER_LOG_FILE` and`MASTER_LOG_POS` so that the slave starts replicating from\
the correct position. Any table and database exclusion rules specified with the`--replicate-*-do-*` and`--replicate-*-ignore-*` options are honored.`--replicate-rewrite-db` is not taken into account because a\
user could use this option to set up a non-unique mapping such as`--replicate-rewrite-db="db1->db3"` and`--replicate-rewrite-db="db2->db3"`, which would confuse the\
slave when loading tables from the master.

Use of this statement is subject to the following conditions:

* It works only for MyISAM tables. Attempting to load a non-MyISAM table\
  results in the following error:`ERROR 1189 (08S01): Net error reading from master`
* It acquires a global read lock on the master while taking the snapshot, which\
  prevents updates on the master during the load operation.

If you are loading large tables, you might have to increase the values of`net_read_timeout` and `net_write_timeout` on\
both the master and slave servers.\
See [Server System Variables](../../optimization-and-tuning/system-variables/server-system-variables.md).

Note that `LOAD DATA FROM MASTER` does not copy any tables\
from the mysql database. This makes it easy to have different users and\
privileges on the master and the slave.

To use `LOAD DATA FROM MASTER`, the replication account that\
is used to connect to the master must have the `RELOAD` and [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#global-privileges) privileges on the master and the`SELECT` privilege for all master tables you want to load.\
All master tables for which the user does not have the`SELECT` privilege are ignored by`LOAD DATA FROM MASTER`. This is because the master hides\
them from the user: `LOAD DATA FROM MASTER` calls`SHOW DATABASES` to know the master databases to load, but [SHOW DATABASES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-databases.md) returns only databases\
for which the user has some privilege. On the slave side, the user that\
issues `LOAD DATA FROM MASTER` must have privileges for\
dropping and creating the databases and tables that are copied.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
