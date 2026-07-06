---
description: >-
  Quickly back up MyISAM and Aria tables by copying table files with the
  mariadb-hotcopy Perl script (formerly mysqlhotcopy).
---

# mariadb-hotcopy

`mariadb-hotcopy` is a Perl script that was originally written and contributed by Tim Bunce. It uses [FLUSH TABLES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), [LOCK TABLES](../../reference/sql-statements/transactions/lock-tables.md), and cp or scp to make a database backup.

{% hint style="info" %}
Previously, the client was called `mysqlhotcopy`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

It is a fast way to make a backup of the database or single tables, but it can be run only on the same machine where the database directories are located. `mariadb-hotcopy` works only for backing up [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/) and [ARCHIVE](../../server-usage/storage-engines/archive.md) tables. It runs on Unix and NetWare.

To use `mariadb-hotcopy`, you must have read access to the files for the tables that you are backing up, the `SELECT` [privilege](../../reference/sql-statements/account-management-sql-statements/grant.md) for those tables, the `RELOAD` privilege (to be able to execute `FLUSH TABLES`), and the `LOCK TABLES` privilege (to be able to lock the tables).

```bash
shell> mariadb-hotcopy db_name [/path/to/new_directory]
shell> mariadb-hotcopy db_name_1 ... db_name_n /path/to/new_directory
```

Back up tables in the given database that match a regular expression:

```bash
shell> mariadb-hotcopy db_name./regex/
```

The regular expression for the table name can be negated by prefixing it with a tilde (`~`):

```bash
shell> mariadb-hotcopy db_name./~regex/
```

`mariadb-hotcopy` supports the following options, which can be specified on the command line or in the \[`mariadb-hotcopy`] and \[`client`] option file groups.

#### `--help`, `-?`

Display a help message and exit.

#### `--addtodest`

Do not rename target directory (if it exists); merely add files to it.

#### `--allowold`

Do not abort if a target exists; rename it by adding an \_old suffix.

#### `--checkpoint`=_db\_name.tbl\_name_

Insert checkpoint entries into the specified database _db\_name_ and table _tbl\_name_.

#### `--chroot`=_directory_

Base _directory_ of the chroot jail in which mariadbd operates. The path value should match that of the \
`--chroot` option given to `mariadbd`.

#### `--debug`

Enable debug output.

#### `--dryrun`, `-n`

Report actions without performing them.

#### `--flushlog`

Flush logs after all tables are locked.

#### `--host`=_host\_name_, `-h` _host\_name_

The _host name_ of the local host to use for making a TCP/IP connection to the local server. By default, the connection is made to localhost using a Unix socket file.

#### `--keepold`

Do not delete previous (renamed) target when done.

#### `--method`=_method_

The _method_ for copying files (`cp` or `scp`). The default is `cp`.

#### `--noindices`

Do not include full index files for MyISAM tables in the backup. This makes the backup smaller and faster. The indexes for reloaded tables can be reconstructed later with [myisamchk -rq](../myisam-clients-and-utilities/myisamchk.md).

#### `--old-server`

Connect to old MySQL server (before MySQL 5.5) which doesn't have [FLUSH TABLES WITH READ LOCK](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) fully implemented.

#### `--password`=_password_, `-p`_password_

The _password_ to use when connecting to the server. The password value is mandatory for this option, unlike for other MariaDB programs. Specifying a password on the command line should be considered insecure. You can use an option file to avoid giving the password on the command line.

#### `--port`=_port-number_, `-P` _port-number_

The TCP/IP _port number_ to use when connecting to the local server.

#### `--quiet`, `-q`

Be silent except for errors.

#### `--record\_log\_pos`=_db\_name_._tbl\_name_

Record master and slave status in the specified database _db\_name_ and table _tbl\_name_.

#### `--regexp`=_expression_

Copy all databases with names that match the given regular _expression_.

#### `--resetmaster`

Reset the binary log after locking all the tables.

#### `--resetslave`

Reset the `master.info` file after locking all the tables.

#### `--socket`=_socket-file_, `-S` _socket-file_

The Unix _socket file_ to use for connections to localhost.

#### `--suffix`=_string_

The _suffix string_ to use for names of copied databases.

#### `--tmpdir`=_directory_

The temporary _directory_. The default is `/tmp`.

#### `--user`=_username_, `-u` _username_

The MariaDB _username_ to use when connecting to the server.

Use perldoc for additional `mariadb-hotcopy` documentation, including information about the structure of the tables needed for the`--checkpoint` and \`\`--record`_log_pos` options:

```bash
shell> perldoc mariadb-hotcopy
```

## See Also

* [mariadb-dump](mariadb-dump.md)
* [mariadb-backup](../../server-usage/backup-and-restore/mariadb-backup/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
