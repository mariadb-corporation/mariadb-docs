# mariadb-access

`mariadb-access` is a tool for checking access privileges, developed by Yves Carlier.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105), the client used to be called `mysqlaccess`, and can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

It checks the access privileges for a host name, user name, and database combination. Note that mariadb-access checks access using only the [user](../../reference/system-tables/the-mysql-database-tables/mysql-user-table.md), [db](../../reference/system-tables/the-mysql-database-tables/mysql-db-table.md), and host tables. It does not check table, column, or routine privileges specified in the [tables\_priv](../../reference/system-tables/the-mysql-database-tables/mysql-tables_priv-table.md), [columns\_priv](../../reference/system-tables/the-mysql-database-tables/mysql-columns_priv-table.md), or [procs\_priv](../../reference/system-tables/the-mysql-database-tables/mysql-procs_priv-table.md) tables.

## Usage

```
mariadb-access [host [user [db]]] OPTIONS
```

If your MariaDB distribution is installed in some non-standard location, you must change the location where _mariadb-access_ expects to find the mariadb client. Edit the _mariadb-access_ script at approximately line 18. Search for a line that looks like this:\
<\
`$MYSQL = ´/usr/local/bin/mariadb;`

`path to mariadb executable`

`<`>\
Change the path to reflect the location where _mariadb_ actually is stored on your system. If you do not do this, a _Broken pipe error_ will occur when you run _mariadb-access_.

## Options

| Option                                | Description                                                                                                                                                 |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -?, --help                            | Displayhelp and exit.                                                                                                                                       |
| -v, --version                         | Display version.                                                                                                                                            |
| -u username, --user=username          | Username for logging in to the db.                                                                                                                          |
| -p\[password], --password\[=password] | Password to use for user. If ommitted, mariadb-access prompts for one.                                                                                      |
| -h hostname, --host=hostname          | Name or IP of the host.                                                                                                                                     |
| -d dbname, --db=dbname                | Name of the database.                                                                                                                                       |
| -U username, --superuser=username     | Connect as superuser.                                                                                                                                       |
| -P password, --spassword=password     | Password for superuser.                                                                                                                                     |
| -H server, --rhost=server             | Remote server to connect to.                                                                                                                                |
| --old\_server                         | Connect to a very old MySQL servers (before version 3.21) that does not know how to handle full WHERE clauses.                                              |
| -b, --brief                           | Single-line tabular report.                                                                                                                                 |
| -t, --table                           | Report in table-format.                                                                                                                                     |
| --relnotes                            | Print release-notes.                                                                                                                                        |
| --plan                                | Print suggestions/ideas for future releases.                                                                                                                |
| --howto                               | Some examples of how to run \`mariadb-access'.                                                                                                              |
| --debug=N                             | Enter debug level N (0..3).                                                                                                                                 |
| --copy                                | Reload temporary grant-tables from original ones.                                                                                                           |
| --preview                             | Show differences in privileges after making changes in (temporary) grant-tables.                                                                            |
| --commit                              | Copy grant-rules from temporary tables to grant-tables (the grant tables must be flushed after, for example with [mariadb-admin reload](mariadb-admin.md)). |
| --rollback                            | Undo the last changes to the grant-tables.                                                                                                                  |

## Note

At least the user (`-u`) and the database (`-d`) must be given, even with wildcards. If no host is provided, \`localhost' is assumed. Wildcards (_,?,%,\_) are allowed for host, user and db, but be sure to escape them from your shell!! (ie type \* or '_')

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
