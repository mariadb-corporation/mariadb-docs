# my\_print\_defaults

`my_print_defaults` displays the options from option groups of option files. It is useful to see which options a particular tool will use.

Output is one option per line, displayed in the form in which they would be specified on the command line.

### Usage

```ini
my_print_defaults [OPTIONS] [groups]
```

### Options

| Option                             | Description                                                                                                                                                                                  |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -c, --config-file=_name_           | Deprecated, use `--defaults-file` instead. Name of config file to read; if no extension is given, default extension (`.ini` or `.cnf`) are added.                                            |
| -d, --debug\[=#]                   | In debug versions, write a debugging log. A typical debug\_options string is `d:t:o,file_name`. The default is `d:t:o,/tmp/my_print_defaults.trace`.                                         |
| -c, --defaults-file=_name_         | Like `--config-file`, except if it is the first option. In that case, read this file only, do not read global or per-user config files; should be the first option. Removed in MariaDB 10.8. |
| -e, --defaults-extra-file=_name_   | Read this file after the global config file and before the config file in the users home directory; should be the first option. Removed in MariaDB 10.8.                                     |
| -g, --defaults-group-suffix=_name_ | In addition to the given groups, read also groups with this suffix. Removed in MariaDB 10.8.                                                                                                 |
| -e, --extra-file=_name_            | Deprecated. Synonym for `--defaults-extra-file`.                                                                                                                                             |
| --mariadbd                         | Read the same set of groups that the [mariadbd](../../server-management/starting-and-stopping-mariadb/mariadbd.md) server does. Available from MariaDB 10.11.3.                              |
| --mysqld                           | Read the same set of groups that the [mysqld](../../server-management/starting-and-stopping-mariadb/mariadbd.md) server does.                                                                                 |
| -n, --no-defaults                  | Return an empty string (useful for scripts).                                                                                                                                                 |
| ?, --help                          | Display this help message and exit.                                                                                                                                                          |
| -v, --verbose                      | Increase the output level.                                                                                                                                                                   |
| -V, --version                      | Output version information and exit.                                                                                                                                                         |

### Examples

```
my_print_defaults --defaults-file=example.cnf client client-server mysql
```

[mariadb-check](../table-tools/mariadb-check.md) reads from the `[mariadb-check]` and `[client]` sections in [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), so the following would display the mariadb-check options.

```
my_print_defaults mariadb-check client
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
