---
description: >-
  mariadb-find-rows reads files of SQL statements and extracts those that
  match a regular expression or that contain USE or SET statements.
---

# mariadb-find-rows

`mariadb-find-rows` reads files containing SQL statements and extracts statements that match a given regular expression or that contain [USE db\_name](../../reference/sql-statements/administrative-sql-statements/use-database.md) or [SET](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statements.

Previously, the client was called `mysql_find_rows`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

The utility was written for use with update log files (as used prior to MySQL 5.0), and as such expects statements to be terminated with semicolon (`;`) characters. It may be useful with other files that contain SQL statements, as long as statements are terminated with semicolons.

## Usage

```
mariadb-find-rows [options] [file_name ...]
```

Each file\_name argument should be the name of file containing SQL statements. If no file names are given, the tool reads from `stdin` (standard input).

## Options

`mariadb-find-rows` supports the following options:

| Option                | Description                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| --help, --Information | Display help and exit.                                                                                                                |
| --regexp=_pattern_    | Display queries that match _pattern_.                                                                                                 |
| --rows=N              | Quit after displaying _N_ queries.                                                                                                    |
| --skip-use-db         | Do not include [USE db\_name](../../reference/sql-statements/administrative-sql-statements/use-database.md) statements in the output. |
| --start\_row=_N_      | Start output from this row (first row is `1`).                                                                                        |

## Examples

```
mariadb-find-rows --regexp=problem_table --rows=20 < update.log
mariadb-find-rows --regexp=problem_table  update-log.1 update-log.2
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
