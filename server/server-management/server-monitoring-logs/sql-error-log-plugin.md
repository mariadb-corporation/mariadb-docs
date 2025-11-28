# SQL Error Log Plugin

The `SQL_ERROR_LOG` plugin collects errors sent to clients in a log file defined by [sql\_error\_log\_filename](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md#sql_error_log_filename), so that they can later be analyzed. The log file can be rotated if [sql\_error\_log\_rotate](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md#sql_error_log_rotate) is set.

Errors are logged as they happen and an error will be logged even if it was handled by a [condition handler](../../reference/sql-statements/programmatic-compound-statements/declare-handler.md) and was never technically _sent_ to the client.

From [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.5) warnings can also be logged if [sql\_error\_log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md#sql_error_log_warnings) is enabled.

Comments are also logged, which can make the log easier to search. But this is only possible if the client does not strip the comments away. For example, the [mariadb](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) command-line client only leaves comments when started with the [--comments](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#mariadb-options) option.

## Installing the Plugin

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:

```sql
INSTALL SONAME 'sql_errlog';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) or the [--plugin-load-add](../starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) options. This can be specified as a command-line argument to [mariadbd](../starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = sql_errlog
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```sql
UNINSTALL SONAME 'sql_errlog';
```

If you installed the plugin by providing the [--plugin-load](../starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) or the [--plugin-load-add](../starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) options in a relevant server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Logging

The log format until [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010) is:

```
Time User Error_code: Error_message : Query
```

Starting from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), the format is:

```
Time User Type Error_code: Error_message : Query
```

Starting from [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.17), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.7), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes), [MariaDB 11.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes), and [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.1), when the [sql\_error\_log\_with\_db\_and\_thread\_info](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md#sql_error_log_with_db_and_thread_info) variable is enabled, the log also contains thread id and database name. If there is no database, `NULL` will be displayed.

```
Time Thread_id User Database_name Type Error_code: Error_message : Query
```

Each separated by a space or : as above

| Option        | Description                                                                            | Version |
| ------------- | -------------------------------------------------------------------------------------- | ------- |
| Time          | Time (YYYY-MM-DD hh-mm-ss)                                                             | 5.5.22  |
| Thread Id     | Thread Id of current thread                                                            | 10.6.17 |
| User          | privilege\_user \[login\_user\_name] @ hostname \[ip]                                  | 5.5.22  |
| Database name | Name of the currently selected database                                                | 10.6.17 |
| Type          | ERROR or WARNING                                                                       | 10.11.6 |
| Error\_code   | OS error, MariaDB storage engine code (120-199) or MariaDB internal error code (1000-) | 5.5.22  |
| Query         | Query text                                                                             | 5.5.22  |

## Example of Logs

```
2023-10-31 15:54:37 root[root] @ localhost [] ERROR 1146: Table 'test.t_doesnt_exist' doesn't exist : select * from t_doesnt_exist
2023-10-31 15:54:37 root[root] @ localhost [] ERROR 1064: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'syntax_error_query' at line 1 : syntax_error_query
2023-10-31 15:54:37 root[root] @ localhost [] ERROR 1146: Table 'test.temptab' doesn't exist : SELECT `c` FROM `temptab`
2023-11-01 11:31:15 [monty] @ storm [192.168.0.12] ERROR 1051: Unknown table 'test.t1' : drop table t1
```

With [sql\_error\_log\_with\_db\_and\_thread\_info](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md#sql_error_log_with_db_and_thread_info) enabled (database `test` and thread id `4`):

```
2023-10-31 15:54:37 4 root[root] @ localhost [] `test` ERROR 1146: Table 'test.t_doesnt_exist' doesn't exist : select * from t_doesnt_exist
```

## Example Usage

```sql
install plugin SQL_ERROR_LOG soname 'sql_errlog';
Query OK, 0 rows affected (0.00 sec)

USE test;

SET sql_mode='STRICT_ALL_TABLES,NO_ENGINE_SUBSTITUTION';
Query OK, 0 rows affected (0.00 sec)

CREATE TABLE foo2 (id INT) ENGINE=WHOOPSIE;
ERROR 1286 (42000): Unknown storage engine 'WHOOPSIE'
\! cat data/sql_errors.log
2013-03-19  9:38:40 msandbox[msandbox] @ localhost [] ERROR 1286: Unknown storage engine 'WHOOPSIE' : CREATE TABLE foo2 (id int) ENGINE=WHOOPSIE
```

## Versions

| Version | Status | Introduced                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1     | Stable | [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.17), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.7), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes) |
| 1.0     | Stable | [MariaDB 10.1.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10113-release-notes)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 1.0     | Gamma  | [MariaDB 10.0.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 1.0     | Alpha  | [MariaDB 5.5.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5522-release-notes)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## System Variables and Options

* [sql\_error\_log](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md)
* [sql\_error\_log\_filename](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md)
* [sql\_error\_log\_rate](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md)
* [sql\_error\_log\_rotate](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md)
* [sql\_error\_log\_rotations](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md)
* [sql\_error\_log\_size\_limit](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md)
* [sql\_error\_log\_size\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md)
* [sql\_error\_log\_with\_db\_and\_thread\_info](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
