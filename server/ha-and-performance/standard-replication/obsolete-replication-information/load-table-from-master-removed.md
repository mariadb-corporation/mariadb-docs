# LOAD TABLE FROM MASTER (removed)

## Syntax

```bnf
LOAD TABLE tbl_name FROM MASTER
```

## Description

This feature has been removed from recent versions of MariaDB.

Since the current implementation of [LOAD DATA FROM MASTER](load-data-from-master-removed.md)\
and `LOAD TABLE FROM MASTER` is very limited, these statements\
are deprecated in versions 4.1 of MySQL and above. We will introduce a more\
advanced technique (called "online backup") in a future version. That technique\
will have the additional advantage of working with more storage engines.

For MariaDB and MySQL 5.1 and earlier, the recommended alternative solution to\
using `LOAD DATA FROM MASTER` or`LOAD TABLE FROM MASTER` is using [mysqldump](../../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md) or [mysqlhotcopy](../../../clients-and-utilities/legacy-clients-and-utilities/mysqlhotcopy.md).\
The latter requires Perl and two Perl modules (DBI and DBD:mysql) and works for [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) and [ARCHIVE](../../../server-usage/storage-engines/archive.md) tables only. With mysqldump, you can create SQL dumps on the\
master and pipe (or copy) these to a mysql client on the slave. This has the\
advantage of working for all storage engines, but can be quite slow, since it\
works using `SELECT`.

Transfers a copy of the table from the master to the slave. This statement is\
implemented mainly debugging `LOAD DATA FROM MASTER`\
operations. To use `LOAD TABLE`, the account used for\
connecting to the master server must have the `RELOAD` and [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#global-privileges) privileges on the master and the`SELECT` privilege for the master table to load. On the slave\
side, the user that issues `LOAD TABLE FROM MASTER` must have\
privileges for dropping and creating the table.

The conditions for `LOAD DATA FROM MASTER` apply here as well.\
For example, `LOAD TABLE FROM MASTER` works only for MyISAM\
tables. The timeout notes for `LOAD DATA FROM MASTER` apply as\
well.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
