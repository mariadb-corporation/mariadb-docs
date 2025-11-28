# mariadb-access

`mariadb-access` is a tool for checking access privileges, developed by Yves Carlier.

{% tabs %}
{% tab title="Current" %}
The client tool can alternatively be called by its former name,  `mysqlaccess`, via a symlink in Linux, or an alternate binary in Windows.
{% endtab %}

{% tab title="< 10.5" %}
The client tool is called `mysqlaccess`.
{% endtab %}
{% endtabs %}

It checks the access privileges for a host name, user name, and database combination. 

{% hint style="info" %}
mariadb-access checks access using only the [user](../../reference/system-tables/the-mysql-database-tables/mysql-user-table.md), [db](../../reference/system-tables/the-mysql-database-tables/mysql-db-table.md), and host tables. It does not check table, column, or routine privileges specified in the [tables\_priv](../../reference/system-tables/the-mysql-database-tables/mysql-tables_priv-table.md), [columns\_priv](../../reference/system-tables/the-mysql-database-tables/mysql-columns_priv-table.md), or [procs\_priv](../../reference/system-tables/the-mysql-database-tables/mysql-procs_priv-table.md) tables.
{% endhint %}

## Usage

```bash
mariadb-access [host [user [db]]] OPTIONS
```

If your MariaDB distribution is installed in some non-standard location, you must change the location where _mariadb-access_ expects to find the mariadb client. Edit the _mariadb-access_ script at approximately line 18. Search for a line that looks like this:

```ini
$MYSQL = ´/usr/local/bin/mariadb;
path to mariadb executable
```

Change the path to reflect the location where the _mariadb_ client tool is stored on your system. Otherwise, a _Broken pipe error_ occurs when running _mariadb-access_.

## Options

| Option                                | Description                                                                                                                                                      |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -?, --help                            | Display help and exit.                                                                                                                                           |
| -v, --version                         | Display version.                                                                                                                                                 |
| -u username, --user=username          | Username for logging in to the server.                                                                                                                           |
| -p\[password], --password\[=password] | Password to use for user. If omitted, mariadb-access prompts for one.                                                                                            |
| -h hostname, --host=hostname          | Name or IP of the host.                                                                                                                                          |
| -d dbname, --db=dbname                | Name of the database.                                                                                                                                            |
| -U username, --superuser=username     | Connect as superuser.                                                                                                                                            |
| -P password, --spassword=password     | Password for superuser.                                                                                                                                          |
| -H server, --rhost=server             | Remote server to connect to.                                                                                                                                     |
| --old\_server                         | Connect to a very old MySQL servers (before version 3.21) that does not know how to handle full WHERE clauses.                                                   |
| -b, --brief                           | Single-line tabular report.                                                                                                                                      |
| -t, --table                           | Report in table-format.                                                                                                                                          |
| --relnotes                            | Print release-notes.                                                                                                                                             |
| --plan                                | Print suggestions/ideas for future releases.                                                                                                                     |
| --howto                               | Some examples of how to run \`mariadb-access'.                                                                                                                   |
| --debug=N                             | Enter debug level N (0..3).                                                                                                                                      |
| --copy                                | Reload temporary grant tables from original ones.                                                                                                                |
| --preview                             | Show differences in privileges after making changes in (temporary) grant tables.                                                                                 |
| --commit                              | Copy grant rules from temporary tables to grant tables (the grant tables must be flushed afterwards, for example with [mariadb-admin reload](mariadb-admin.md)). |
| --rollback                            | Undo the last changes to the grant tables.                                                                                                                       |

## Note

At least the user (`-u`) and the database (`-d`) options must be given, even when using wildcards. If no host is provided, \``localhost`' is assumed. Wildcards (`?`, `%`, and `_`) are allowed for host, user, and database, but be sure to escape them from your shell.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
