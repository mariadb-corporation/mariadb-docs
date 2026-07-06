---
description: >-
  Convert every table in a database to a given storage engine (MyISAM by
  default) with mariadb-convert-table-format (formerly
  mysql_convert_table_format).
---

# mariadb-convert-table-format

`mariadb-convert-table-format` converts the tables in a database to use a particular storage engine ([MyISAM](../../server-usage/storage-engines/myisam-storage-engine/) by default).

{% hint style="info" %}
Previously, the client was called `mysql_convert_table_format`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

## Usage

```bash
mariadb-convert-table-format [options] db_name
```

## Description

`mariadb-convert-table-format` is written in Perl and requires that the DBI and DBD::mysql Perl modules be installed. Invoke `mariadb-convert-table-format` like this:

```bash
shell> mariadb-convert-table-format [options]db_name
```

The `db_name` argument indicates the database containing the tables to be converted.

## Options

`mariadb-convert-table-format` supports the options described in the following list:

| Option                  | Description                                                                                                                                                                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -?, --help              | Display help and exit.                                                                                                                                                                                                           |
| -e, --engine=ENGINE     | Specify the storage engine that the tables should be converted to use. The default is [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/) if this option is not given.                                           |
| -f, --force             | Continue even if errors occur.                                                                                                                                                                                                   |
| -h, --host=host\_name   | Connect to the MariaDB server on the given host. Default localhost.                                                                                                                                                              |
| -p, --password=password | The password to use when connecting to the server. Note that the password value is not optional for this option, unlike for other client programs. Specifying the password on the command line is generally considered insecure. |
| -P, --port=port\_num    | The TCP/IP port number to use for the connection.                                                                                                                                                                                |
| -S, --socket=path       | For connections to localhost, the Unix socket file to use.                                                                                                                                                                       |
| -u, --user=user\_name   | The MariaDB user name to use when connecting to the server.                                                                                                                                                                      |
| -v, --verbose           | Verbose mode. Print more information about what the program does.                                                                                                                                                                |
| -V, --version           | Display version information and exit.                                                                                                                                                                                            |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
