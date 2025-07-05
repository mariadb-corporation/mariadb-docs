# mariadbd Options

This page lists all of the options for `mariadbd` (called mysqld before [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105)), ordered by topic. For a full alphabetical list of all mariadbd options, as well as server and status variables, see [Full list of MariaDB options, system and status variables](../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

In many cases, the entry here is a summary, and links to the full description.

By convention, [server variables](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) have usually been specified with an underscore in the configuration files, and a dash on the command line. You can however specify underscores as dashes - they are interchangeable.

See [Configuring MariaDB with Option Files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) for which files and groups mariadbd reads for it's default options.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), the client used to be called `mysqld`, and can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

## Option Prefixes

#### `--autoset-*`

* Description: Sets the option value automatically. Only supported for certain options.

#### `--disable-*`

* Description: For all boolean options, disables the setting (equivalent to setting it to `0`). Same as `--skip`.

#### `--enable-*`

* Description: For all boolean options, enables the setting (equivalent to setting it to `1`).

#### `--loose-*`

* Description: Don't produce an error if the option doesn't exist.

#### `--maximum-*`

* Description: Sets the maximum value for the option.

#### `--skip-*`

* Description: For all boolean options, disables the setting (equivalent to setting it to `0`). Same as `--disable`.

## Option File Options

#### `--defaults-extra-file`

* Commandline: `--defaults-extra-file=name`
* Description: Read this extra option file after all other option files are read.
  * See [Configuring MariaDB with Option Files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

#### `--defaults-file`

* Commandline: `--defaults-file=name`
* Description: Only read options from the given option file.
  * See [Configuring MariaDB with Option Files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

#### `--defaults-group-suffix`

* Commandline: `--defaults-group-suffix=name`
* Description: In addition to the default option groups, also read option groups with the given suffix.
  * See [Configuring MariaDB with Option Files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

#### `--no-defaults`

* Commandline: `--no-defaults`
* Description: Don't read options from any option file.
  * See [Configuring MariaDB with Option Files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

#### `--print-defaults`

* Commandline: `--print-defaults`
* Description: Read options from option files, print all option values, and then exit the program.
  * See [Configuring MariaDB with Option Files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

## Compatibility Options

The following options have been added to MariaDB to make it more compliant with\
other MariaDB and MySQL versions. Options that are also system variables are listed after:

#### `-a, --ansi`

* Description: Use ANSI SQL syntax instead of MariaDB syntax. This mode will also set [transaction isolation level](../../reference/sql-statements/transactions/set-transaction.md) [serializable](../../reference/sql-statements/transactions/set-transaction.md).

#### `--new`

* Description: Use new functionality that will exist in next version of MariaDB. This function exists to make it easier to prepare for an upgrade.

#### `--old-style-user-limits`

* Description: Enable old-style user limits (before MySQL 5.0.3, user resources were counted per each user+host vs. per account).

#### `--safe-mode`

* Description: Disable some potential unsafe optimizations. For 5.2, [INSERT DELAYED](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) is disabled, [myisam\_recover\_options](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options) is set to DEFAULT (automatically recover crashed MyISAM files) and the [query cache](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) is disabled. For [Aria](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/README.md) tables, disable bulk insert optimization to enable one to use [aria\_read\_log](../../clients-and-utilities/aria-clients-and-utilities/aria_read_log.md) to recover tables even if tables are deleted (good for testing recovery).

#### `--skip-new`

* Description: Disables [--new](mariadbd-options.md#-new).

### Compatibility Options and System Variables

* [--old](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old)
* [--old-alter-table](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_alter_table)
* [--old-mode](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_mode)
* [--old-passwords](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords)
* [--show-old-temporals](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#show_old_temporals)

## Locale Options

Options that are also system variables are listed after:

#### `--character-set-client-handshake`

* Commandline: `--character-set-client-handshake`
* Description: Don't ignore client side character set value sent during handshake. `--skip-character-set-client-handshake` will ignore the client value and use the default server value.

#### `--default-character-set`

* Commandline: `--default-character-set=name`
* Description: Still available as an option for setting the default character set for clients and their connections, it was deprecated and removed in [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) as a server option. Use [character-set-server](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_server) instead.

#### `--language`

* Description: This option can be used to set the server's language for error messages. This option can be specified either as a language name or as the path to the directory storing the language's [error message file](../server-monitoring-logs/error-log.md#error-messages-file). See [Server Locales](../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) for a list of supported locales and their associated languages.
  * This option is deprecated. Use the [lc\_messages](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages) and [lc\_messages\_dir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages_dir) system variables instead.
  * See [Setting the Language for Error Messages](../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/setting-the-language-for-error-messages.md) for more information.

### Locale Options and System Variables

* [character-set-filesystem](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_filesystem)
* [character-set-client](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client)
* [character-set-connection](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection)
* [character-set-database](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_database)
* [character-set-filesystem](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_filesystem)
* [character-set-results](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_results)
* [character-set-server](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_server)
* [character-set-system](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_system)
* [character-sets-dir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_sets_dir)
* [collation-connection](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection)
* [collation-database](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_database)
* [collation-server](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_server)
* [default-week-format](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_week_format)
* [default-time-zone](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#time_zone)
* [lc-messages](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages)
* [lc-messages-dir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages_dir)
* [lc-time-names](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names)

## Windows Options

Options that are also system variables are listed after:

#### `--console`

* Description: Windows-only option that keeps the console window open and for writing log messages to stderr and stdout. If specified together with [--log-error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error), the last option will take precedence.

#### `--install`

* Description: Windows-only option that installs the `mariadbd` process as a Windows service.
  * The Windows service created with this option [auto-starts](https://docs.microsoft.com/en-us/windows/desktop/Services/automatically-starting-services). If you want a service that is [started on demand](https://docs.microsoft.com/en-us/windows/desktop/Services/starting-services-on-demand), then use the [--install-manual](mariadbd-options.md#install-manual) option.
  * This option takes a service name as an argument. If this option is provided without a service name, then the service name defaults to "MARIADB".
  * This option is deprecated and may be removed in a future version. See [MDEV-19358](https://jira.mariadb.org/browse/MDEV-19358) for more information.

#### `--install-manual`

* Description: Windows-only option that installs the `mariadbd` process as a Windows service.
  * The Windows service created with this option is [started on demand](https://docs.microsoft.com/en-us/windows/desktop/Services/starting-services-on-demand). If you want a service that [auto-starts](https://docs.microsoft.com/en-us/windows/desktop/Services/automatically-starting-services), use the [--install](mariadbd-options.md#install) option.
  * This option takes a service name as an argument. If this option is provided without a service name, then the service name defaults to "MARIADB".
  * This option is deprecated and may be removed in a future version. See [MDEV-19358](https://jira.mariadb.org/browse/MDEV-19358) for more information.

#### `--remove`

* Description: Windows-only option that removes the Windows service created by the [--install](mariadbd-options.md#install) or [--install-manual](mariadbd-options.md#install-manual) options.
  * This option takes a service name as an argument. If this option is provided without a service name, then the service name defaults to "MARIADB".
  * This option is deprecated and may be removed in a future version. See [MDEV-19358](https://jira.mariadb.org/browse/MDEV-19358) for more information.

#### `--slow-start-timeout`

* Description: Windows-only option that defines the maximum number of milliseconds that the service control manager should wait before trying to kill the Windows service during startup. Defaults to `15000`.

#### `--standalone`

* Description: Windows-only option that has no effect. Kept for compatibility reasons.

### Windows Options and System Variables

The following options and system variables are related to using MariaDB on Windows:

* [--named-pipe](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#named_pipe)

## Replication and Binary Logging Options

The following options are related to [replication](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/broken-reference/README.md) and the [binary log](../server-monitoring-logs/binary-log/). Options that are also system variables are listed after:

#### `--abort-slave-event-count`

* Commandline: `--abort-slave-event-count=#`
* Description: Option used by mysql-test for debugging and testing of replication.

#### `--binlog-do-db`

* Commandline: `--binlog-do-db=name`
* Description: This option allows you to configure a [replication master](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/broken-reference/README.md) to write statements and transactions affecting databases that match a specified name into its [binary log](../server-monitoring-logs/binary-log/). Since the filtered statements or transactions will not be present in the [binary log](../server-monitoring-logs/binary-log/), its replicas will not be able to replicate them.
  * This option will not work with cross-database updates with [statement-based logging](../server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](../../ha-and-performance/standard-replication/replication-filters.md#statement-based-logging) section for more information.
  * This option can not be set dynamically. Available as a [system variable](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_do_db) from [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes).
  * When setting it on the command-line or in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), the option does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the option multiple times.
  * See [Replication Filters](../../ha-and-performance/standard-replication/replication-filters.md) for more information.

#### `--binlog-ignore-db`

* Commandline: `--binlog-ignore-db=name`
* Description: This option allows you to configure a [replication master](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/broken-reference/README.md) to not write statements and transactions affecting databases that match a specified name into its [binary log](../server-monitoring-logs/binary-log/). Since the filtered statements or transactions will not be present in the [binary log](../server-monitoring-logs/binary-log/), its replicas will not be able to replicate them.
  * This option will not work with cross-database updates with [statement-based logging](../server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](../../ha-and-performance/standard-replication/replication-filters.md#statement-based-logging) section for more information.
  * This option can not be set dynamically. Available as a [system variable](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_ignore_db) from [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes).
  * When setting it on the command-line or in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), the option does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the option multiple times.
  * See [Replication Filters](../../ha-and-performance/standard-replication/replication-filters.md) for more information.

#### `--binlog-row-event-max-size`

* Commandline: `--binlog-row-event-max-size=#`
* Description: The maximum size of a row-based [binary log](../server-monitoring-logs/binary-log/) event in bytes. Rows will be grouped into events smaller than this size if possible. The value has to be a multiple of 256. Available as a [system variable](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_event_max_size) from [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes).
* Default value `8192`

#### `--disconnect-slave-event-count`

* Commandline: `--disconnect-slave-event-count=#`
* Description: Option used by mysql-test for debugging and testing of replication.

#### `--flashback`

* Commandline: `--flashback`
* Description: Setup the server to use flashback. This enables the [binary log](../server-monitoring-logs/binary-log/) and sets `binlog_format=ROW`.

#### `--init-rpl-role`

* Commandline: `--init-rpl-role=name`
* Description: Set the replication role. From [MariaDB 10.6.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-19-release-notes), [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-9-release-notes), [MariaDB 11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-3-release-notes) and [MariaDB 11.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes), changes the condition for [semi-sync recovery](../../ha-and-performance/standard-replication/semisynchronous-replication.md) to truncate the [binlog](../server-monitoring-logs/binary-log/) to instead use this option, when set to SLAVE. This allows for both [rpl\_semi\_sync\_master\_enabled](../../ha-and-performance/standard-replication/semisynchronous-replication.md#rpl_semi_sync_master_enabled) and [rpl\_semi\_sync\_slave\_enabled](../../ha-and-performance/standard-replication/semisynchronous-replication.md#rpl_semi_sync_slave_enabled) to be set for a primary that is restarted, and no transactions will be lost, so long as `--init-rpl-role` is not set to SLAVE. In earlier versions, for servers configured with both [rpl\_semi\_sync\_master\_enabled=1](../../ha-and-performance/standard-replication/semisynchronous-replication.md#rpl_semi_sync_master_enabled) and [rpl\_semi\_sync\_slave\_enabled=1](../../ha-and-performance/standard-replication/semisynchronous-replication.md#rpl_semi_sync_slave_enabled), if a primary is just re-started (i.e. retaining its role as primary), it can truncate its binlog to drop transactions which its replica(s) have already received and executed. If this happens, when the replica reconnects, its [gtid\_slave\_pos](../../ha-and-performance/standard-replication/gtid.md) can be ahead of the recovered primary’s [gtid\_binlog\_pos](../../ha-and-performance/standard-replication/gtid.md), resulting in an error state where the replica’s state is ahead of the primary’s. See [-init-rpl-role](mariadbd-options.md#-init-rpl-role).
* Valid values: Empty, `MASTER` or `SLAVE`

#### `--log-basename`

* Commandline: `--log-basename=name`
* Description: Basename for all log files and the .pid file. This sets all log file names at once (in 'datadir') and is normally the only option you need for specifying log files. This is especially recommended to be set if you are using [replication](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/broken-reference/README.md) as it ensures that your log file names are not dependent on your host name. Sets names for the [binary log](../server-monitoring-logs/binary-log/), [relay log](../server-monitoring-logs/binary-log/relay-log.md), [general query log](../server-monitoring-logs/general-query-log.md), [slow query log](../server-monitoring-logs/slow-query-log/) and [error log](../server-monitoring-logs/error-log.md). Note that if you explicity set log file names with any of these other options; [log-bin-index](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md), [relay-log](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md), [relay-log-index](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md), [general-log-file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#general_log_file), [log\_slow\_query\_file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_file) ([slow\_query\_log\_file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file)), [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error), and [pid-file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#pid_file), these should be placed after `--log-basename` in the config files. Later settings override earlier settings, so `log-basename` will override any earlier log file name settings.

#### `--log-bin-trust-routine-creators`

* Commandline: `--log-bin-trust-routine-creators`
* Description: Deprecated, use [log-bin-trust-function-creators](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md).

#### `--master-host`

* Commandline: `--master-host=name`
* Description: Primary hostname or IP address for replication. If not set, the replica thread will not be started. Note that the setting of master-host will be ignored if there exists a valid master.info file.

#### `--master-info-file`

* Commandline: `--master-info-file=name`
* Description: Name and location of the file on the replica where the `MASTER_LOG_FILE` and `MASTER_LOG_POS` options (i.e. the [binary log](../server-monitoring-logs/binary-log/) position on the primary) and most other [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) options are written. The [replica's I/O thread](../../ha-and-performance/standard-replication/replication-threads.md#replica-io-thread) keeps this [binary log](../server-monitoring-logs/binary-log/) position updated as it downloads events.
  * See [CHANGE MASTER TO: Option Persistence](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#option-persistence) for more information.

#### `--master-password`

* Commandline: `--master-password=name`
* Description: The password the replica thread will authenticate with when connecting to the primary. If not set, an empty password is assumed. The value in master.info will take precedence if it can be read.

#### `--master-port`

* Commandline: `--master-port=#`
* Description: The port the master is listening on. If not set, the compiled setting of MYSQL\_PORT is assumed. If you have not tinkered with configure options, this should be 3306. The value in master.info will take precedence if it can be read.

#### `--master-retry-count`

* Commandline: `--master-retry-count=#`
* Description: Number of times a replica will attempt to connect to a primary before giving up. The retry interval is determined by the MASTER\_CONNECT\_RETRY option for the CHANGE MASTER statement. A value of 0 means the replica will not stop attempting to reconnect. Reconnects are triggered when a replica has timed out. See [slave\_net\_timeout](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md).
* Default Value: `86400` through 10.5, `100000` as of 10.6
* Range - 32 bit: `0 to 4294967295`
* Range - 64 bit: `0 to 18446744073709551615`

#### `--master-ssl`

* Commandline: `--master-ssl`
* Description: Enable the replica to [connect to the master using TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md).

#### `--master-ssl-ca`

* Commandline: `--master-ssl-ca[=name]`
* Description: Master TLS CA file. Only applies if you have enabled [master-ssl](mariadbd-options.md#-master-ssl).

#### `--master-ssl-capath`

* Commandline: `--master-ssl-capath[=name]`
* Description: Master TLS CA path. Only applies if you have enabled [master-ssl](mariadbd-options.md#-master-ssl).

#### `--master-ssl-cert`

* Commandline: `--master-ssl-cert[=name]`
* Description: Master TLS certificate file name. Only applies if you have enabled [master-ssl](mariadbd-options.md#-master-ssl).

#### `--master-ssl-cipher`

* Commandline: `--master-ssl-cipher[=name]`
* Description: Master TLS cipher. Only applies if you have enabled [master-ssl](mariadbd-options.md#-master-ssl).

#### `--master-ssl-key`

* Commandline: `--master-ssl-key[=name]`
* Description: Master TLS keyfile name. Only applies if you have enabled [master-ssl](mariadbd-options.md#-master-ssl).

#### `--master-user`

* Commandline: `--master-user=name`
* Description: The username the replica thread will use for authentication when connecting to the primary. The user must have FILE privilege. If the primary user is not set, user test is assumed. The value in master.info will take precedence if it can be read.

#### `--max-binlog-dump-events`

* Commandline: `--max-binlog-dump-events=#`
* Description: Option used by mysql-test for debugging and testing of replication.

#### `--replicate-same-server-id`

* Commandline: `--replicate-same-server-id`
* Description: In replication, if set to 1, do not skip events having our server id. Default value is 0 (to break infinite loops in circular replication). Can't be set to 1 if [log-slave-updates](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) is used.

#### `--sporadic-binlog-dump-fail`

* Commandline: `--sporadic-binlog-dump-fail`
* Description: Option used by mysql-test for debugging and testing of replication.

#### `--sysdate-is-now`

* Commandline: `--sysdate-is-now`
* Description: Non-default option to alias [SYSDATE()](../../reference/sql-functions/date-time-functions/sysdate.md) to [NOW()](../../reference/sql-functions/date-time-functions/now.md) to make it safe for [replication](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/broken-reference/README.md). Since 5.0, SYSDATE() has returned a \`dynamic' value different for different invocations, even within the same statement.

### Replication and Binary Logging Options and System Variables

The following options and system variables are related to [replication](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/broken-reference/README.md) and the [binary log](../server-monitoring-logs/binary-log/):

* [auto-increment-increment](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [auto-increment-offset](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-alter-two-phase](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-annotate-row-events](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-cache-size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-checksum](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-commit-wait-count](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-commit-wait-usec](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-direct-non-transactional-updates|](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-expire-logs-seconds](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-file-cache-size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-format](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-gtid-index](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-gtid-index-page-size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-gtid-index-span-min](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-large-commit-threshold](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-legacy-event-pos](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-optimize-thread-scheduling](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-row-image](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-row-metadata](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-space-limit](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-stmt-cache-size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [default-master-connection](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [gtid-cleanup-batch-size](../../ha-and-performance/standard-replication/gtid.md)
* [gtid-domain-id](../../ha-and-performance/standard-replication/gtid.md)
* [gtid-ignore-duplicates](../../ha-and-performance/standard-replication/gtid.md)
* [gtid-strict-mode](../../ha-and-performance/standard-replication/gtid.md)
* [init-slave](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [log-bin](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [log-bin-compress](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [log-bin-compress-min-len](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [log-bin-index](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [log-bin-trust-function-creators](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [log-slave-updates](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [master-verify-checksum](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [max-binlog-cache-size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [max-binlog-size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [max-binlog-stmt-cache-size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [max-binlog-total-size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [max-relay-log-size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [read-binlog-speed-limit](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log-index](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log-info-file](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log-purge](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log-recovery](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log-space-limit](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-annotate-row-events](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-do-db](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-do-table](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-events-marked-for-skip](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-ignore-db](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-ignore-table](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-rewrite-db](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-wild-do-table](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-wild-ignore-table](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [report-host](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [report-password](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [report-port](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [report-user](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [rpl-recovery-rank](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [server-id](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-abort-blocking-timeout](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_abort_blocking_timeout)
* [slave-compressed-protocol](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-connections-needed-for-purge](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-ddl-exec-mode](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-domain-parallel-threads](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-exec-mode](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-load-tmpdir](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-max-allowed-packet](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-max-statement-time](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-net-timeout](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-parallel-max-queued](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-parallel-threads](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-run-triggers-for-rbr](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-skip-errors](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-sql-verify-checksum](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-transaction-retries](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave\_transaction\_retry\_errors](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave\_transaction\_retry\_interval](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-type-conversions](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [sync-binlog](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [sync-master-info](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [sync-relay-log](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [sync-relay-log-info](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)

### Semisynchronous Replication Options and System Variables

The options and system variables related to [Semisynchronous Replication](../../ha-and-performance/standard-replication/semisynchronous-replication.md) are described [here](../../ha-and-performance/standard-replication/semisynchronous-replication.md#system-variables).

## Optimizer Options

Options that are also system variables are listed after:

#### `--record-buffer`

* Commandline: `--record-buffer=#`
* Description: Old alias for [read\_buffer\_size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_buffer_size).
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `--table-cache`

* Commandline: `--table-open-cache=#`
* Description: Removed; use [--table-open-cache](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache) instead.
* Removed: [MariaDB 5.1.3](https://mariadb.com/kb/en/mariadb-513-release-notes/)

### Optimizer Options and System Variables

* [alter-algorithm](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#alter_algorithm)
* [analyze-sample-percentage](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#analyze_sample_percentage)
* [big-tables](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#big_tables)
* [bulk-insert-buffer-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#bulk_insert_buffer_size)
* [expensive-subquery-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#expensive_subquery_limit)
* [join-buffer-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size)
* [join-buffer-space-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_space_limit)
* [join-cache-level](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_cache_level)
* [max-heap-table-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size)
* [max-join-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_join_size)
* [max-seeks-for-key](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_seeks_for_key)
* [max-sort-length](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_sort_length)
* [mrr-buffer-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#mrr_buffer_size)
* [optimizer-adjust-secondary-key-costs](../../ha-and-performance/optimization-and-tuning/query-optimizations/optimizer_adjust_secondary_key_costs.md)
* [optimizer-extra-pruning-depth](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_extra_pruning_depth)
* [optimizer-join-limit-pref-ratio](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_join_limit_pref_ratio)
* [optimizer-max-sel-arg-weight](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_max_sel_arg_weight)
* [optimizer-max-sel-args](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_max_sel_args)
* [optimizer-prune-level](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_prune_level)
* [optimizer-search-depth](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_search_depth)
* [optimizer-selectivity-sampling-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_selectivity_sampling_limit)
* [optimizer-switch](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_switch)
* [optimizer-trace](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_trace)
* [optimizer-trace-max-mem-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_trace_max_mem_size)
* [optimizer-use-condition-selectivity](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_use_condition_selectivity)
* [query-alloc-block-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_alloc_block_size)
* [query-prealloc-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_prealloc_size)
* [range-alloc-block-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#range_alloc_block_size)
* [read-buffer-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_buffer_size)
* [rowid-merge-buff-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#rowid_merge_buff_size)
* [table-definition-cache](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#table_definition_cache)
* [table-open-cache](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache)
* [table-open-cache-instances](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache_instances)
* [tmp-disk-table-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tmp_disk_table_size)
* [tmp-memory-table-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tmp_memory_table_size)
* [tmp-table-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tmp_table_size)
* [use-stat-tables](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#use_stat_tables)

## Storage Engine Options

#### `--skip-bdb`

* Commandline: `----skip-bdb`
* Description: Deprecated option; Exists only for compatibility with very old my.cnf files.
* Removed: [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1051-release-notes)

#### `--external-locking`

* Commandline: `--external-locking`
* Description: Use system (external) locking (disabled by default). With this option enabled you can run [myisamchk](../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) to test (not repair) tables while the server is running. Disable with [--skip-external-locking](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_external_locking). From [MariaDB 10.2.40](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10240-release-notes), [MariaDB 10.3.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10331-release-notes), [MariaDB 10.4.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10421-release-notes), [MariaDB 10.5.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10512-release-notes), [MariaDB 10.6.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1064-release-notes) and all later version, this effects InnoDB and can be used to prevent multiple instances running on the same data.

### MyISAM Storage Engine Options

The options related to the [MyISAM](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/README.md) storage engine are described below. Options that are also system variables are listed after:

#### `--log-isam`

* Commandline: `--log-isam[=file_name]`
* Description: Enable the [MyISAM log](../server-monitoring-logs/myisam-log.md), which logs all MyISAM changes to file. If no filename is provided, the default, myisam.log is used.

#### MyISAM Storage Engine Options and System Variables

Some options and system variables related to the [MyISAM](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/README.md) storage engine can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md). Direct links to many of them can be found below.

* [concurrent-insert](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#concurrent_insert)
* [delayed-insert-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#delayed_insert_limit)
* [delayed-insert-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#delayed_insert_timeout)
* [delayed-queue-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#delayed_queue_size)
* [keep-files-on-create](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#keep_files_on_create)
* [key-buffer-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size)
* [key-cache-age-threshold](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_age_threshold)
* [key-cache-block-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_block_size)
* [key-cache-division-limit](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_division_limit)
* [key-cache-file-hash-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_file_hash_size)
* [key-cache-segments](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_segments)
* [myisam-block-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-data-pointer-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-max-sort-file-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-mmap-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-recover-options](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-repair-threads](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-sort-buffer-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-stats-method](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-use-mmap](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)

### InnoDB Storage Engine Options

The options related to the [InnoDB](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/README.md) storage engine are described below. Options that are also system variables are listed after:

#### `--innodb`

* Commandline: `--innodb=value`, `--skip-innodb`
* Description: This variable controls whether or not to load the InnoDB storage engine. Possible values are `ON`, `OFF`, `FORCE` or `FORCE_PLUS_PERMANENT` (from [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)). If set to `OFF` (the same as --skip-innodb), since InnoDB is the default storage engine, the server will not start unless another storage engine has been chosen with [--default-storage-engine](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine). `FORCE` means that the storage engine must be successfully loaded, or else the server won't start. `FORCE_PLUS_PERMANENT` enables the plugin, but if plugin cannot initialize, the server will not start. In addition, the plugin cannot be uninstalled while the server is running.

#### `--innodb-cmp`

* Commandline: `--innodb-cmp`
* Description:
* Default: `ON`

#### `--innodb-cmp-reset`

* Commandline: `--innodb-cmp-reset`
* Description:
* Default: `ON`

#### `--innodb-cmpmem`

* Commandline: `--innodb-cmpmem`
* Description:
* Default: `ON`

#### `--innodb-cmpmem-reset`

* Commandline: `--innodb-cmpmem-reset`
* Description:
* Default: `ON`

#### `--innodb-file-io-threads`

* Commandline: `--innodb-file-io-threads`
* Description:
* Default: `4`
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `--innodb-index-stats`

* Commandline: `--innodb-index-stats`
* Description:
* Default: `ON`
* Removed: [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes)

#### `--innodb-lock-waits`

* Commandline: `--innodb-lock-waits`
* Description:
* Default: `ON`

#### `--innodb-locks`

* Commandline: `--innodb-locks`
* Description:
* Default: `ON`

#### `--innodb-rseg`

* Commandline: `--innodb-rseg`
* Description:
* Default: `ON`
* Removed: [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes)

#### `--innodb-status-file`

* Commandline: `--innodb-status-file`
* Description:
* Default: `FALSE`

#### `--innodb-sys-indexes`

* Commandline: `--innodb-sys-indexes`
* Description:
* Default: `ON`

#### `--innodb-sys-stats`

* Commandline: `--innodb-sys-stats`
* Description:
* Default: `ON`
* Removed: [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes)

#### `--innodb-sys-tables`

* Commandline: `--innodb-sys-tables`
* Description:
* Default: `ON`

#### `--innodb-table-stats`

* Commandline: `--innodb-table-stats`
* Description:
* Default: `ON`
* Removed: [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes)

#### `--innodb-trx`

* Commandline: `--innodb-trx`
* Description:
* Default: `ON`

#### InnoDB Storage Engine Options and System Variables

Some options and system variables related to the [InnoDB](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/README.md) storage engine can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md). Direct links to many of them can be found below.

* [ignore-builtin-innodb](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#ignore_builtin_innodb)
* [innodb-adaptive-checkpoint](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_checkpoint)
* [innodb-adaptive-flushing](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_flushing)
* [innodb-adaptive-flushing-lwm](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_flushing_lwm)
* [innodb-adaptive-flushing-method](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_flushing_method)
* [innodb-adaptive-hash-index](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index)
* [innodb-adaptive-hash-index-partitions](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index_partitions)
* [innodb-adaptive-hash-index-parts](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index_parts)
* [innodb-adaptive-max-sleep-delay](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_max_sleep_delay)
* [innodb-additional-mem-pool-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_additional_mem_pool_size)
* [innodb-alter-copy-bulk](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_alter_copy_bulk)
* [innodb-api-bk-commit-interval](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_api_bk_commit_interval)
* [innodb-api-disable-rowlock](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_api_disable_rowlock)
* [innodb-api-enable-binlog](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_api_enable_binlog)
* [innodb-api-enable-mdl](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_api_enable_mdl)
* [innodb-api-trx-level](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_api_trx_level)
* [innodb-auto-lru-dump](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_auto_lru_dump)
* [innodb-autoextend-increment](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_autoextend_increment)
* [innodb-autoinc-lock-mode](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_autoinc_lock_mode)
* [innodb-background-scrub-data-check-interval](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_check_interval)
* [innodb-background-scrub-data-compressed](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_compressed)
* [innodb-background-scrub-data-interval](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_interval)
* [innodb-background-scrub-data-uncompressed](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_uncompressed)
* [innodb-blocking-buffer-pool-restore](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_blocking_buffer_pool_restore)
* [innodb-buf-dump-status-frequency](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buf_dump_status_frequency)
* [innodb-buffer-pool-chunk-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_chunk_size)
* [innodb-buffer-pool-dump-at-shutdown](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_dump_at_shutdown)
* [innodb-buffer-pool-dump-now](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_dump_now)
* [innodb-buffer-pool-dump-pct](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_dump_pct)
* [innodb-buffer-pool-evict](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_evict)
* [innodb-buffer-pool-filename](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_filename)
* [innodb-buffer-pool-instances](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances)
* [innodb-buffer-pool-load-abort](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_abort)
* [innodb-buffer-pool-load-at-startup](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_at_startup)
* [innodb-buffer-pool-load-now](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_now)
* [innodb-buffer-pool-load-pages-abort](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_pages_abort)
* [innodb-buffer-pool-populate](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_populate)
* [innodb-buffer-pool-restore-at-startup](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_restore_at_startup)
* [innodb-buffer-pool-shm-checksum](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_shm_checksum)
* [innodb-buffer-pool-shm-key](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_shm_key)
* [innodb-buffer-pool-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size)
* [innodb-change-buffer-max-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffer_max_size)
* [innodb-change-buffering](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffering)
* [innodb-change-buffering-debug](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffering_debug)
* [innodb-checkpoint-age-target](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_checkpoint_age_target)
* [innodb-checksum-algorithm](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm)
* [innodb-checksums](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksums)
* [innodb-cleaner-lsn-age-factor](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_cleaner_lsn_age_factor)
* [innodb-cmp-per-index-enabled](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_cmp_per_index_enabled)
* [innodb-commit-concurrency](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_commit_concurrency)
* [innodb-compression-algorithm](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_compression_algorithm)
* [innodb-compression-failure-threshold-pct](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_compression_failure_threshold_pct)
* [innodb-compression-level](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_compression_level)
* [innodb-compression-pad-pct-max](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_compression_pad_pct_max)
* [innodb-concurrency-tickets](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_concurrency_tickets)
* [innodb-corrupt-table-action](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_corrupt_table_action)
* [innodb-data-file-buffering](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_data_file_buffering)
* [innodb-data-file-path](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_data_file_path)
* [innodb-data-file-write-through](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_data_file_write_through)
* [innodb-data-home-dir](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_data_home_dir)
* [innodb-deadlock-detect](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_deadlock_detect)
* [innodb-deadlock-report](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_deadlock_report)
* [innodb-default-encryption-key-id](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id)
* [innodb-default-page-encryption-key](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_default_page_encryption_key)
* [innodb-default-row-format](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_default_row_format)
* [innodb-defragment](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment)
* [innodb-defragment-fill-factor](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor)
* [innodb-defragment-fill-factor-n-recs](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor_n_recs)
* [innodb-defragment-frequency](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_frequency)
* [innodb-defragment-n-pages](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages)
* [innodb-defragment-stats-accuracy](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_stats_accuracy)
* [innodb-dict-size-limit](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_dict_size_limit)
* [innodb\_disable\_sort\_file\_cache](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_disable_sort_file_cache)
* [innodb-doublewrite](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_doublewrite)
* [innodb-doublewrite-file](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_doublewrite_file)
* [innodb-empty-free-list-algorithm](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_empty_free_list_algorithm)
* [innodb-enable-unsafe-group-commit](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_enable_unsafe_group_commit)
* [innodb-encrypt-log](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log)
* [innodb-encrypt-tables](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables)
* [innodb-encrypt-temporary-tables](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables)
* [innodb-encryption-rotate-key-age](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age)
* [innodb-encryption-rotation\_iops](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotation_iops)
* [innodb-encryption-threads](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads)
* [innodb-extra-rsegments](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_extra_rsegments)
* [innodb-extra-undoslots](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_extra_undoslots)
* [innodb-fake-changes](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_fake_changes)
* [innodb-fast-checksum](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_fast_checksum)
* [innodb-fast-shutdown](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown)
* [innodb-fatal-semaphore-wait-threshold](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_fatal_semaphore_wait_threshold)
* [innodb-file-format](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_format)
* [innodb-file-format-check](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_format_check)
* [innodb-file-format-max](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_format_max)
* [innodb-file-per-table](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table)
* [innodb-fill-factor](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_fill_factor)
* [innodb-flush-log-at-trx-commit](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit)
* [innodb-flush-method](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method)
* [innodb-flush-neighbor-pages](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_neighbor_pages)
* [innodb-flush-neighbors](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_neighbors)
* [innodb-flush-sync](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_sync)
* [innodb-flushing-avg-loops](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_flushing_avg_loops)
* [innodb-force-load-corrupted](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_force_load_corrupted)
* [innodb-force-primary-key](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_force_primary_key)
* [innodb-force-recovery](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_force_recovery)
* [innodb-foreground-preflush](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_foreground_preflush)
* [innodb-ft-aux-table](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_aux_table)
* [innodb-ft-cache-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_cache_size)
* [innodb-ft-enable-diag-print](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_enable_diag_print)
* [innodb-ft-enable-stopword](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_enable_stopword)
* [innodb-ft-max-token-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_max_token_size)
* [innodb-ft-min-token-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_min_token_size)
* [innodb-ft-num-word-optimize](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_num_word_optimize)
* [innodb-ft-result-cache-limit](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_result_cache_limit)
* [innodb-ft-server-stopword-table](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_server_stopword_table)
* [innodb-ft-sort-pll-degree](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_sort_pll_degree)
* [innodb-ft-total-cache-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_total_cache_size)
* [innodb-ft-user-stopword-table](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_user_stopword_table)
* [innodb-ibuf-accel-rate](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ibuf_accel_rate)
* [innodb-ibuf-active-contract](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ibuf_active_contract)
* [innodb-ibuf-max-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_ibuf_max_size)
* [innodb-idle-flush-pct](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_idle_flush_pct)
* [innodb-immediate-scrub-data-uncompressed](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_immediate_scrub_data_uncompressed)
* [innodb-import-table-from-xtrabackup](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_import_table_from_xtrabackup)
* [innodb-instant-alter-column-allowed](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_instant_alter_column_allowed)
* [innodb-instrument-semaphores](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_instrument_semaphores)
* [innodb-io-capacity](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_io_capacity)
* [innodb-io-capacity-max](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_io_capacity_max)
* [innodb-large-prefix](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_large_prefix)
* [innodb-lazy-drop-table](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_lazy_drop_table)
* [innodb-lock-schedule-algorithm](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_lock_schedule_algorithmt)
* [innodb-locking-fake-changes](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_locking_fake_changes)
* [innodb-locks-unsafe-for-binlog](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_locks_unsafe_for_binlog)
* [innodb-log-arch-dir](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_arch_dir)
* [innodb-log-arch-expire-sec](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_arch_expire_sec)
* [innodb-log-archive](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_archive)
* [innodb-log-block-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_block_size)
* [innodb-log-buffer-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_buffer_size)
* [innodb-log-checksum-algorithm](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_checksum_algorithm)
* [innodb-log-checksums](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_checksums)
* [innodb-log-compressed-pages](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_compressed_pages)
* [innodb-log-file-buffering](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_buffering)
* [innodb-log-file-mmap](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_mmap)
* [innodb-log-file-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_size)
* [innodb-log-file-write-through](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_write_through)
* [innodb-log-files-in-group](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_files_in_group)
* [innodb-log-group-home-dir](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_group_home_dir)
* [innodb-log-optimize-ddl](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_optimize_ddl)
* [innodb-log-spin-wait-delay](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb-log_spin_wait_delay)
* [innodb-log-write-ahead-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_write_ahead_size)
* [innodb-lru-flush-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_lru_flush_size)
* [innodb-lru-scan-depth](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_lru_scan_depth)
* [innodb-max-bitmap-file-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_bitmap_file_size)
* [innodb-max-changed-pages](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_changed_pages)
* [innodb-max-dirty-pages-pct](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_dirty_pages_pct)
* [innodb-max-dirty-pages-pct-lwm](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_dirty_pages_pct_lwm)
* [innodb-max-purge-lag](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_purge_lag)
* [innodb-max-purge-lag-delay](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_purge_lag_delay)
* [innodb-max-purge-lag-wait](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_purge_lag_wait)
* [innodb-max-undo-log-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_undo_log_size)
* [innodb-merge-sort-block-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_merge_sort_block_size)
* [innodb-mirrored-log-groups](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_mirrored_log_groups)
* [innodb-monitor-disable](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_disable)
* [innodb-monitor-enable](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_enable)
* [innodb-monitor-reset](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_reset)
* [innodb-monitor-reset-all](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_reset_all)
* [innodb-mtflush-threads](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_mtflush_threads)
* [innodb-numa-interleave](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_numa_interleave)
* [innodb-old-blocks-pct](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_old_blocks_pct)
* [innodb-old-blocks-time](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_old_blocks_time)
* [innodb-online-alter-log-max-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_online_alter_log_max_size)
* [innodb-open-files](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_open_files)
* [innodb-optimize-fulltext-only](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_optimize_fulltext_only)
* [innodb-page-cleaners](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_cleaners)
* [innodb-page-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_size)
* [innodb-pass-corrupt-table](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_pass_corrupt_table)
* [innodb-prefix-index-cluster-optimization](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_prefix_index_cluster_optimization)
* [innodb-print-all-deadlocks](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_print_all_deadlocks)
* [innodb-purge-batch-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_purge_batch_size)
* [innodb-purge-rseg-truncate-frequency](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_purge_rseg_truncate_frequency)
* [innodb-purge-threads](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_purge_threads)
* [innodb-random-read-ahead](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_random_read_ahead)
* [innodb-read-ahead](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_read_ahead)
* [innodb-read-ahead-threshold](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_read_ahead_threshold)
* [innodb-read-io-threads](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_read_io_threads)
* [innodb-read-only](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_read_only)
* [innodb-recovery-update-relay-log](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_recovery_update_relay_log)
* [innodb-replication-delay](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_replication_delay)
* [innodb-rollback-on-timeout](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_rollback_on_timeout)
* [innodb-rollback-segments](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_rollback_segments)
* [innodb-safe-truncate](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_safe_truncate)
* [innodb-sched-priority-cleaner](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_sched_priority_cleaner)
* [innodb-scrub-log](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log)
* [innodb-scrub-log-interval](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log_interval)
* [innodb-scrub-log-speed](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log_speed)
* [innodb-show-locks-held](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_show_locks_held)
* [innodb-show-verbose-locks](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_show_verbose_locks)
* [innodb-snapshot-isolation](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation)
* [innodb-sort-buffer-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_sort_buffer_size)
* [innodb-spin-wait-delay](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_spin_wait_delay)
* [innodb-stats-auto-recalc](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_auto_recalc)
* [innodb-stats-auto-update](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_auto_update)
* [innodb-stats-include-delete-marked](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_include_delete_marked)
* [innodb-stats-method](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_method)
* [innodb-stats-modified-counter](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_modified_counter)
* [innodb-stats-on-metadata](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_on_metadata)
* [innodb-stats-persistent](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent)
* [innodb-stats-persistent-sample-pages](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent_sample_pages)
* [innodb-stats-sample-pages](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_sample_pages)
* [innodb-stats-transient-sample-pages](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_transient_sample_pages)
* [innodb-stats-traditional](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_traditional)
* [innodb-stats-update-need-lock](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_update_need_lock)
* [innodb-status-output](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_status_output)
* [innodb-status-output-locks](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_status_output_locks)
* [innodb-strict-mode](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_strict_mode)
* [innodb-support-xa](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_support_xa)
* [innodb-sync-array-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_sync_array_size)
* [innodb-sync-spin-loops](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_sync_spin_loops)
* [innodb-table-locks](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_table_locks)
* [innodb-temp-data-file-path](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_temp_data_file_path)
* [innodb-thread-concurrency](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_concurrency)
* [innodb-thread-concurrency-timer-based](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_concurrency_timer_based)
* [innodb-thread-sleep-delay](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_sleep_delay)
* [innodb-tmpdir](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_tmpdir)
* [innodb-track-changed-pages](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_track_changed_pages)
* [innodb-track-redo-log-now](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_track_redo_log_now)
* [innodb-truncate-temporary-tablespace-now](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_truncate_temporary_tablespace_now)
* [innodb-undo-directory](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_directory)
* [innodb-undo-log-truncate](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_log_truncate)
* [innodb-undo-logs](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs)
* [innodb-undo-tablespaces](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_tablespaces)
* [innodb-use-atomic-writes](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_atomic_writes)
* [innodb-use-fallocate](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_fallocate)
* [innodb-use-global-flush-log-at-trx-commit](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_global_flush_log_at_trx_commit)
* [innodb-use-mtflush](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_mtflush)
* [innodb-use-native\_aio](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_native_aio)
* [innodb-use-purge-thread](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_purge_thread)
* [innodb-use-stacktrace](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_stacktrace)
* [innodb-use-sys-malloc](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_sys_malloc)
* [innodb-use-sys-stats-table](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_sys_stats_table)
* [innodb-use-trim](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_trim)
* [innodb-write-io-threads](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_write_io_threads)
* [skip-innodb](mariadbd-options.md#-innodb)
* [skip-innodb-checksums](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksums)
* [skip-innodb-doublewrite](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_doublewrite)

### Aria Storage Engine Options

Options related to the [Aria](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/README.md) storage engine are listed below:

#### Aria Storage Engine Options and System Variables

Some options and system variables related to the [Aria](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/README.md) storage engine can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md). Direct links to many of them can be found below.

* [aria-block-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_block_size)
* [aria-checkpoint-interval](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_checkpoint_interval)
* [aria-checkpoint-log-activity](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_checkpoint_log_activity)
* [aria-encrypt-tables](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_encrypt_tables)
* [aria-force-start-after-recovery-failures](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_force_start_after_recovery_failures)
* [aria-group-commit](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_group_commit)
* [aria-group-commit-interval](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_group_commit_interval)
* [aria-log-dir-path](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_log_dir_path)
* [aria-log-file-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_log_file_size)
* [aria-log-purge-type](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_log_purge_type)
* [aria-max-sort-file-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_max_sort_file_size)
* [aria-page-checksum](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_page_checksum)
* [aria-pagecache-age-threshold](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_pagecache_age_threshold)
* [aria-pagecache-buffer-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size)
* [aria-pagecache-division-limit](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_pagecache_division_limit)
* [aria-pagecache-file-hash-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_pagecache_file_hash_size)
* [aria-recover](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_recover)
* [aria-recover-options](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_recover_options)
* [aria-repair-threads](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_repair_threads)
* [aria-sort-buffer-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_sort_buffer_size)
* [aria-stats-method](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_stats_method)
* [aria-sync-log-dir](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_sync_log_dir)
* [aria-used-for-temp-tables](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#aria_used_for_temp_tables)
* [deadlock-search-depth-long](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#deadlock_search_depth_long)
* [deadlock-search-depth-short](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#deadlock_search_depth_short)
* [deadlock-timeout-long](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#deadlock_timeout_long)
* [deadlock-timeout-short](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md#deadlock_timeout_short)

### MyRocks Storage Engine Options

The options and system variables related to the [MyRocks](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myrocks/README.md) storage engine can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myrocks/myrocks-system-variables.md).

### S3 Storage Engine Options

The options and system variables related to the [S3](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/s3-storage-engine/README.md) storage engine can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/s3-storage-engine/s3-storage-engine-system-variables.md).

### CONNECT Storage Engine Options

The options related to the [CONNECT](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/README.md) storage engine are described below.

#### CONNECT Storage Engine Options and System Variables

Some options and system variables related to the [CONNECT](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/README.md) storage engine can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md). Direct links to many of them can be found below.

* [connect-class-path](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_class_path)
* [connect-cond-push](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_cond_push)
* [connect-conv-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_conv_size)
* [connect-default-depth](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_default_depth)
* [connect-default-prec](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_default_prec)
* [connect-enable-mongo](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_enable_mongo)
* [connect-exact-info](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_exact_info)
* [connect-force\_bson](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_force_bson)
* [connect-indx-map](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_indx_map)
* [connect-java-wrapper](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_java_wrapper)
* [connect-json-all-path](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_json_all_path)
* [connect-json-grp-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_json_grp_size)
* [connect-json-null](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_json_null)
* [connect-jvm-path](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_jvm_path)
* [connect-type-conv](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_type_conv)
* [connect-use-tempfile](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_use_tempfile)
* [connect-work-size](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_work_size)
* [connect-xtrace](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/connect/connect-system-variables.md#connect_xtrace)

### Spider Storage Engine Options

The options and system variables related to the [Spider](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/spider/README.md) storage engine can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/spider/spider-system-variables.md).

### Mroonga Storage Engine Options

The options and system variables related to the [Mroonga](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/mroonga/README.md) storage engine can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/mroonga/mroonga-system-variables.md).

### TokuDB Storage Engine Options

The options and system variables related to the [TokuDB](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/tokudb/README.md) storage engine can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/tokudb/tokudb-system-variables.md).

### Vector Options

The options and system variables related to [Vectors](../../reference/sql-structure/vectors/) storage engine (beginning with `mhnsw`) can be found [here](../../reference/sql-structure/vectors/vector-system-variables.md).

## Performance Schema Options

The options related to the [Performance Schema](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/) are described below. Options that are also system variables are listed after:

#### `--performance-schema-consumer-events-stages-current`

* Commandline: `--performance-schema-consumer-events-stages-current`
* Description: Enable the [events-stages-current](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_stages_current-table.md) consumer.
* Default: `OFF`

#### `--performance-schema-consumer-events-stages-history`

* Commandline: `--performance-schema-consumer-events-stages-history`
* Description: Enable the [events-stages-history](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_stages_history-table.md) consumer.
* Default: `OFF`

#### `--performance-schema-consumer-events-stages-history-long`

* Commandline: `--performance-schema-consumer-events-stages-history-long`
* Description: Enable the [events-stages-history-long](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_stages_history_long-table.md) consumer.
* Default: `OFF`

#### `--performance-schema-consumer-events-statements-current`

* Commandline: `--performance-schema-consumer-events-statements-current`
* Description: Enable the [events-statements-current](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_statements_current-table.md) consumer. Use `--skip-performance-schema-consumer-events-statements-current` to disable.
* Default: `ON`

#### `--performance-schema-consumer-events-statements-history`

* Commandline: `--performance-schema-consumer-events-statements-history`
* Description: Enable the [events-statements-history](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_statements_history-table.md) consumer.
* Default: `OFF`

#### `--performance-schema-consumer-events-statements-history-long`

* Commandline: `--performance-schema-consumer-events-statements-history-long`
* Description: Enable the [events-statements-history-long](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_statements_history_long-table.md) consumer.
* Default: `OFF`

#### `--performance-schema-consumer-events-waits-current`

* Commandline: `--performance-schema-consumer-events-waits-current`
* Description: Enable the [events-waits-current](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_waits_current-table.md) consumer.
* Default: `OFF`

#### `--performance-schema-consumer-events-waits-history`

* Commandline: `--performance-schema-consumer-events-waits-history`
* Description: Enable the [events-waits-history](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_waits_history-table.md) consumer.
* Default: `OFF`

#### `--performance-schema-consumer-events-waits-history-long`

* Commandline: `--performance-schema-consumer-events-waits-history-long`
* Description: Enable the [events-waits-history-long](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_waits_history_long-table.md) consumer.
* Default: `OFF`

#### `--performance-schema-consumer-global-instrumentation`

* Commandline: `--performance-schema-consumer-global-instrumentation`
* Description: Enable the global-instrumentation consumer. Use `--skip-performance-schema-consumer-global-instrumentation` to disable.
* Default: `ON`

#### `--performance-schema-consumer-statements-digest`

* Commandline: `--performance-schema-consumer-statements-digest`
* Description: Enable the statements-digest consumer. Use `--skip-performance-schema-consumer-statements-digest` to disable.
* Default: `ON`

#### `--performance-schema-consumer-thread-instrumentation`

* Commandline: `--performance-schema-consumer-thread-instrumentation`
* Description: Enable the statements-thread-instrumentation. Use `--skip-performance-schema-thread-instrumentation` to disable.
* Default: `ON`

### Performance Schema Options and System Variables

Some options and system variables related to the [Performance Schema](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/) can be found [here](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md). Direct links to many of them can be found below.

* [performance-schema](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema)
* [performance-schema-accounts-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_accounts_size)
* [performance-schema-digests-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_digests_size)
* [performance-schema-events-stages-history-long-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_stages_history_long_size)
* [performance-schema-events-stages-history-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_stages_history_size)
* [performance-schema-events-statements-history-long-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_statements_history_long_size)
* [performance-schema-events-statements-history-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_statements_history_size)
* [performance-schema-events-waits-history-long-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_waits_history_long_size)
* [performance-schema-events-waits-history-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_waits_history_size)
* [performance-schema-hosts-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_hosts_size)
* [performance-schema-max-cond-classes](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_cond_classes)
* [performance-schema-max-cond-instances](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_cond_instances)
* [performance-schema-max-digest-length](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_digest_length)
* [performance-schema-max-file-classes](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_file_classes)
* [performance-schema-max-file-handles](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_file_handles)
* [performance-schema-max-file-instances](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_file_instances)
* [performance-schema-max-mutex-classes](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_mutex_classes)
* [performance-schema-max-mutex-instances](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_mutex_instances)
* [performance-schema-max-rwlock-classes](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_rwlock_classes)
* [performance-schema-max-rwlock-instances](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_rwlock_instances)
* [performance-schema-max-socket-classes](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_socket_classes)
* [performance-schema-max-socket-instances](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_socket_instances)
* [performance-schema-max-stage-classes](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_stage_classes)
* [performance-schema-max-statement-classes](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_statement_classes)
* [performance-schema-max-table-handles](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_table_handles)
* [performance-schema-max-table-instances](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_table_instances)
* [performance-schema-max-thread-classes](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_thread_classes)
* [performance-schema-max-thread-instances](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_thread_instances)
* [performance-schema-session-connect-attrs-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_session_connect_attrs_size)
* [performance-schema-setup-actors-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_setup_actors_size)
* [performance-schema-setup-objects-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_setup_objects_size)
* [performance-schema-users-size](../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_users_size)

## Galera Cluster Options

The options related to [Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md) are described below. Options that are also system variables are listed after:

#### `--wsrep-new-cluster`

* Commandline: `--wsrep-new-cluster`
* Description: Bootstrap a cluster. It works by overriding the current value of wsrep\_cluster\_address. It is recommended not to add this option to the config file as this will trigger bootstrap on every server start.

### Galera Cluster Options and System Variables

Some options and system variables related to [Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md) can be found [here](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables). Direct links to many of them can be found below.

* [wsrep-allowlist](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_allowlist)
* [wsrep-auto-increment-control](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_auto_increment_control)
* [wsrep-causal-reads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_causal_reads)
* [wsrep-certify-nonPK](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_certify_nonpk)
* [wsrep-cluster-address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_cluster_address)
* [wsrep-cluster-name](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_cluster_name)
* [wsrep-convert-LOCK-to-trx](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_convert_lock_to_trx)
* [wsrep-data-home-dir](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_data_home_dir)
* [wsrep-dbug-option](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_dbug_option)
* [wsrep-debug](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_debug)
* [wsrep-desync](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_desync)
* [wsrep-dirty-reads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_dirty_reads)
* [wsrep-drupal-282555-workaround](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_drupal_282555_workaround)
* [wsrep-forced-binlog-format](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_forced_binlog_format)
* [wsrep-gtid-domain-id](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_gtid_domain_id)
* [wsrep-gtid-mode](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_gtid_mode)
* [wsrep-ignore-apply-errors](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_ignore_apply_errors)
* [wsrep-load-data-splitting](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_load_data_splitting)
* [wsrep-log-conflicts](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_log_conflicts)
* [wsrep-max-ws-rows](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_max_ws_rows)
* [wsrep-max-ws-size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_max_ws_size)
* [wsrep-mode](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_mode)
* [wsrep-mysql-replication-bundle](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_mysql_replication_bundle)
* [wsrep-node-address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_node_address)
* [wsrep-node-incoming-address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_node_incoming_address)
* [wsrep-node-name](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_node_name)
* [wsrep-notify-cmd](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_notify_cmd)
* [wsrep-on](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_on)
* [wsrep-OSU-method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_osu_method)
* [wsrep-provider](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider)
* [wsrep-provider-options](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider_options)
* [wsrep-recover](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_recover)
* [wsrep-reject\_queries](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_reject_queries)
* [wsrep-retry-autocommit](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_retry_autocommit)
* [wsrep-slave-FK-checks](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_slave_fk_checks)
* [wsrep-slave-threads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_slave_threads)
* [wsrep-slave-UK-checks](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_slave_uk_checks)
* [wsrep-sr-store](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sr_store)
* [wsrep-sst-auth](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_auth)
* [wsrep-sst-donor](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_donor)
* [wsrep-sst-donor-rejects-queries](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_donor_rejects_queries)
* [wsrep-sst-method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method)
* [wsrep-sst-receive-address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_receive_address)
* [wsrep-start-position](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_start_position)
* [wsrep-status-file](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_status_file)
* [wsrep-strict-ddl](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_strict_ddl)
* [wsrep-sync-wait](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sync_wait)
* [wsrep-trx\_fragment\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_trx_fragment_size)
* [wsrep-trx\_fragment\_unit](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_trx_fragment_unit)

## Options When Debugging mariadbd

#### `--debug-assert-if-crashed-table`

* Description: Do an assert in handler::print\_error() if we get a crashed table.

#### `--debug-binlog-fsync-sleep`

* Description: `--debug-binlog-fsync-sleep=#`If not set to zero, sets the number of micro-seconds to sleep after running fsync() on the [binary log](../server-monitoring-logs/binary-log/) to flush transactions to disk. This can thus be used to artificially increase the perceived cost of such an fsync().

#### `--debug-crc-break`

* Description: `--debug-crc-break=#`Call my\_debug\_put\_break\_here() if crc matches this number (for debug).

#### `--debug-flush`

* Description: Default debug log with flush after write.

#### `--debug-no-sync`

* Description: `debug-no-sync[=#]`Disables system sync calls. Only for running tests or debugging!

#### `--debug-sync-timeout`

* Description: `debug-sync-timeout[=#]`Enable the debug sync facility and optionally specify a default wait timeout in seconds. A zero value keeps the facility disabled.

#### `--gdb`

* Description: Set up signals usable for debugging.

#### `--silent-startup`

* Description: Don't print Notes to the [error log](../server-monitoring-logs/error-log.md) during startup.

#### `--sync-sys`

* Description: Enable/disable system sync calls. Syncs should only be turned off (`--disable-sync-sys`) when running tests or debugging! Replaced by [debug-no-sync](mariadbd-options.md#-debug-no-sync) from [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `--thread-alarm`

* Description: Enable/disable system thread alarm calls. Should only be turned off (`--disable-thread-alarm`) when running tests or debugging!

### Debugging Options and System Variables

* [core-file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#core_file)
* [debug](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#debug)
* [debug-no-thread-alarm](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#debug_no_thread_alarm)

## Other Options

Options that are also system variables are listed after:

#### `--allow-suspicious-udfs`

* Commandline: `--allow-suspicious-udfs`
* Description: Allows use of [user-defined functions](../../server-usage/user-defined-functions/) consisting of only one symbol `x()` without corresponding `x_init()` or `x_deinit()`. That also means that one can load any function from any library, for example `exit()` from `libc.so`. Not recommended unless you require old UDFs with one symbol that cannot be recompiled. From [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010), available as a [system variable](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#allow_suspicious_udfs) as well.

#### `--bootstrap`

* Commandline: `--bootstrap`
* Description: Used by mariadb installation scripts, such as [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md) to execute SQL scripts before any privilege or system tables exist. Do no use while an existing MariaDB instance is running.

#### `--chroot`

* Commandline: `--chroot=name`
* Description: Chroot mariadbd daemon during startup.

#### `--des-key-file`

* Commandline: `--des-key-file=name`
* Description: Load keys for [des\_encrypt()](../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_encrypt.md) and des\_encrypt from given file.

#### `--exit-info`

* Commandline: `--exit-info[=#]`
* Description: Used for debugging. Use at your own risk.

#### `--getopt-prefix-matching`

* Commandline: `--getopt-prefix-matching={0|1}`
* Description: Makes it possible to disable historical "unambiguous prefix" matching in the command-line option parsing.
* Default: TRUE
* Introduced: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes)

#### `--help`

* Commandline: `--help`
* Description: Displays help with many commandline options described, and exits. From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115), includes deprecation information.

#### `--log-ddl-recovery`

* Commandline: `--log-ddl-recovery=name`
* Description: Path to file used for recovery of DDL statements after a crash.
* Default Value: `ddl-recover.log`
* Introduced: [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1061-release-notes)

#### `--log-short-format`

* Commandline: `--log-short-format`
* Description: Don't log extra information to update and [slow-query](../server-monitoring-logs/slow-query-log/) logs.

#### `--log-slow-file`

* Commandline: `--log-slow-file=name`
* Description: Log [slow queries](../server-monitoring-logs/slow-query-log/) to given log file. Defaults logging to hostname-slow.log

#### `--log-slow-time`

* Commandline: `--log-slow-time=#`
* Description: Log all queries that have taken more than [long-query-time](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#long_query_time) seconds to execute to the slow query log, if active. The argument will be treated as a decimal value with microsecond precision.

#### `--log-tc`

* Commandline: `--log-tc=name`
* Description: Defines the path to the memory-mapped file-based transaction coordinator log, which is only used if the [binary log](../server-monitoring-logs/binary-log/) is disabled. If you have two or more XA-capable storage engines enabled, then a transaction coordinator log must be available. See [Transaction Coordinator Log](../server-monitoring-logs/transaction-coordinator-log/) for more information. Also see the [log\_tc\_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_tc_size) system variable and the [--tc-heuristic-recover](mariadbd-options.md#-tc-heuristic-recover) option.
* Default Value: `tc.log`

#### `--master-connect-retry`

* Commandline: `--master-connect-retry=#`
* Description: Deprecated in 5.1.17 and removed in 5.5. The number of seconds the replica thread will sleep before retrying to connect to the master, in case the master goes down or the connection is lost.

#### `--memlock`

* Commandline: `--memlock`
* Description: Lock mariadbd in memory.

#### `--ndb-use-copying-alter-table`

* Commandline: `--ndb-use-copying-alter-table`
* Description: Force ndbcluster to always copy tables at alter table (should only be used if on-line alter table fails).

#### `--one-thread`

* Commandline: `--one-thread`
* Description: (Deprecated): Only use one thread (for debugging under Linux). Use [thread-handling=no-threads](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md) instead.
* Removed: [MariaDB 10.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes)

#### `--plugin-load`

* Commandline: `--plugin-load=name`
* Description: This option can be used to configure the server to load specific [plugins](../../reference/plugins/). This option uses the following format:
  * Plugins can be specified in the format `name=library`, where `name` is the plugin name and `library` is the plugin library. This format installs a single plugin from the given plugin library.
  * Plugins can also be specified in the format `library`, where `library` is the plugin library. This format installs all plugins from the given plugin library.
  * Multiple plugins can be specified by separating them with semicolons.
* Special care must be taken when specifying the [--plugin-load](mariadbd-options.md#-plugin-load) option multiple times, or when specifying both the [--plugin-load](mariadbd-options.md#-plugin-load) option and the [--plugin-load-add](mariadbd-options.md#-plugin-load-add) option together. The [--plugin-load](mariadbd-options.md#-plugin-load) option resets the plugin load list, and this can cause unexpected problems if you are not aware. The [--plugin-load-add](mariadbd-options.md#-plugin-load-add) option does not reset the plugin load list, so it is much safer to use. See [Plugin Overview: Specifying Multiple Plugin Load Options](../../reference/plugins/plugin-overview.md#specifying-multiple-plugin-load-options) for more information.
* See [Plugin Overview: Installing a Plugin with Plugin Load Options](../../reference/plugins/plugin-overview.md#installing-a-plugin-with-plugin-load-options) for more information.

#### `--plugin-load-add`

* Commandline: `--plugin-load-add=name`
* Description: This option can be used to configure the server to load specific [plugins](../../reference/plugins/). This option uses the following format:
  * Plugins can be specified in the format `name=library`, where `name` is the plugin name and `library` is the plugin library. This format installs a single plugin from the given plugin library.
  * Plugins can also be specified in the format `library`, where `library` is the plugin library. This format installs all plugins from the given plugin library.
  * Multiple plugins can be specified by separating them with semicolons.
* Special care must be taken when specifying both the [--plugin-load](mariadbd-options.md#-plugin-load) option and the [--plugin-load-add](mariadbd-options.md#-plugin-load-add) option together. The [--plugin-load](mariadbd-options.md#-plugin-load) option resets the plugin load list, and this can cause unexpected problems if you are not aware. The [--plugin-load-add](mariadbd-options.md#-plugin-load-add) option does not reset the plugin load list, so it is much safer to use. See [Plugin Overview: Specifying Multiple Plugin Load Options](../../reference/plugins/plugin-overview.md#specifying-multiple-plugin-load-options) for more information.
* See [Plugin Overview: Installing a Plugin with Plugin Load Options](../../reference/plugins/plugin-overview.md#installing-a-plugin-with-plugin-load-options) for more information.

#### `--port-open-timeout`

* Commandline: `--port-open-timeout=#`
* Description: Maximum time in seconds to wait for the port to become free. (Default: No wait).

#### `--safe-user-create`

* Commandline: `--safe-user-create`
* Description: Don't allow new user creation by the user who has no write privileges to the [mysql.user](../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md) table.

#### `--safemalloc-mem-limit`

* Commandline: `--safemalloc-mem-limit=#`
* Description: Simulate memory shortage when compiled with the `--with-debug=full` option.

#### `--show-slave-auth-info`

* Commandline: `--show-slave-auth-info`
* Description: Show user and password in SHOW SLAVE HOSTS on this primary.

#### `--skip-grant-tables`

* Commandline: `--skip-grant-tables`
* Description: Start without grant tables. This gives all users FULL ACCESS to all tables, which is useful in case of a lost root password. Use [mariadb-admin flush-privileges](../../clients-and-utilities/administrative-tools/mariadb-admin.md), [mariadb-admin reload](../../clients-and-utilities/administrative-tools/mariadb-admin.md) or [FLUSH PRIVILEGES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) to resume using the grant tables. From [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010), available as a [system variable](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_grant_tables) as well.

Because the [Event Scheduler](../../server-usage/triggers-events/event-scheduler/) also depends on the grant tables for its functionality, it is automatically disabled when running with `--skip-grant-tables`.

#### `--skip-host-cache`

* Commandline: `--skip-host-cache`
* Description: Don't cache host names.

#### `--skip-partition`

* Commandline: `--skip-partition`, `--disable-partition`
* Description: Disables user-defined [partitioning](../../server-usage/partitioning-tables/). Previously partitioned tables cannot be accessed or modifed. Tables can still be seen with [SHOW TABLES](../../reference/sql-statements/administrative-sql-statements/show/show-tables.md) or by viewing the [INFORMATION\_SCHEMA.TABLES table](../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-tables-table.md). Tables can be dropped with [DROP TABLE](../../reference/sql-statements/data-definition/drop/drop-table.md), but this only removes .frm files, not the associated .par files, which will need to be removed manually.

#### `--skip-slave-start`

* Commandline: `--skip-slave-start`
* Description: If set, replica is not autostarted. From [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120), server will display in the log if this option is set.

#### `--skip-ssl`

* Commandline: `--skip-ssl`
* Description: Disable [TLS connections](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md).

#### `--skip-symlink`

* Commandline: `--skip-symlink`
* Description: Don't allow symlinking of tables. Deprecated and removed in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5). Use [symbolic-links](mariadbd-options.md#-symbolic-links) with the `skip` [option prefix](mariadbd-options.md#option-prefixes) instead.
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `--skip-thread-priority`

* Commandline: `--skip-thread-priority`
* Description: Don't give threads different priorities. Deprecated and removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0).
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `--sql-bin-update-same`

* Commandline: `--sql-bin-update-same=#`
* Description: The update log was deprecated in version 5.0 and replaced by the [binary log](../server-monitoring-logs/binary-log/), so this option did nothing since then. Deprecated and removed in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `--ssl`

* Commandline: `--ssl`
* Description: Enable [TLS for connection](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md) (automatically enabled with other flags). Disable with '`--skip-ssl`'.

#### `--stack-trace`

* Commandline: `--stack-trace`, `--skip-stack-trace`
* Description: Print a stack trace on failure. Enabled by default, disable with `-skip-stack-trace`.

#### `--symbolic-links`

* Commandline: `--symbolic-links`
* Description: Enables symbolic link support. When set, the [have\_symlink](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#have_symlink) system variable shows as `YES`. Silently ignored in Windows. Use `--skip-symbolic-links` to disable.

#### `--tc-heuristic-recover`

* Commandline: `--tc-heuristic-recover=name`
* Description: If [manual heuristic recovery](../server-monitoring-logs/transaction-coordinator-log/heuristic-recovery-with-the-transaction-coordinator-log.md) is needed, this option defines the decision to use in the heuristic recovery process. Manual heuristic recovery may be needed if the [transaction coordination log](../server-monitoring-logs/transaction-coordinator-log/) is missing or if it doesn't contain all prepared transactions. This option can be set to `OFF`, `COMMIT`, or `ROLLBACK`. The default is `OFF`. See also the [--log-tc](mariadbd-options.md#-log-tc) server option and the [log\_tc\_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_tc_size) system variable.

#### `--temp-pool`

* Commandline: `--temp-pool`
* Description: Using this option will cause most temporary files created to use a small set of names, rather than a unique name for each new file. This behavior works around a bug in old Linux kernels where the kernel appeared to "leak" memory. In a Docker environment it might look like an unbounded working-set memory growth.\
  Defaults to `1` until [MariaDB 10.5.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1056-release-notes), use `--skip-temp-pool` to disable. Defaults to `0` from [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1057-release-notes), as benchmarking shows it causes a heavy mutex contention.

#### `--test-expect-abort`

* Commandline: `--test-expect-abort`
* Description: Expect that server aborts with 'abort'; Don't write out server variables on 'abort'. Useful only for test scripts.

#### `--test-ignore-wrong-options`

* Commandline: `--test-ignore-wrong-options`
* Description: Ignore wrong enums values in command line arguments. Useful only for test scripts.

#### `--user`

* Commandline: `--user=name`
* Description: Run mariadbd daemon as user.

#### `--verbose`

* Commandline: `-v`, `--verbose`
* Description: Used with [help](mariadbd-options.md#help) option for detailed help.

## Other Options and System Variables

* [allow-suspicious-udfs](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#allow-suspicious-udfs)
* [automatic-sp-privileges](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges)
* [back-log](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#back_log)
* [basedir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#basedir)
* [check-constraint-checks](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#check_constraint_checks)
* [column-compression-threshold](../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md#column_compression_threshold)
* [column-compression-zlib-level](../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md#column_compression_zlib_level)
* [column-compression-zlib-strategy](../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md#column_compression_zlib_strategy)
* [column-compression-zlib-wrap](../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md#column_compression_zlib_wrap)
* [completion-type](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#completion_type)
* [connect-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#connect_timeout)
* [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir)
* [date-format](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#date_format)
* [datetime-format](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datetime_format)
* [deadlock-search-depth-long](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md)
* [deadlock-search-depth-short](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md)
* [deadlock-timeout-long](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md)
* [deadlock-timeout-short](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/aria-system-variables.md)
* [default-password-lifetime](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_password_lifetime)
* [default-regex-flags](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags)
* [default-storage-engine](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine)
* [default-table-type](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_table_type)
* [delay-key-write](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#delay_key_write)
* [disconnect-on-expired-password](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#disconnect_on_expired_password)
* [div-precision-increment](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#div_precision_increment)
* [enable-named-pipe](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#named_pipe)
* [encrypt-binlog](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_binlog)
* [encrypt-tmp-disk-tables](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_disk_tables)
* [encrypt-tmp-files](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_files)
* [encryption-algorithm](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#encryption_algorithm)
* [engine-condition-pushdown](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#engine_condition_pushdown)
* [eq-range-index-dive-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#eq_range_index_dive_limit)
* [event-scheduler](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#event_scheduler)
* [expire-logs-days](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#expire_logs_days)
* [explicit-defaults-for-timestamp](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#explicit_defaults_for_timestamp)
* [extra-max-connections](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [extra-port](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [flush](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#flush)
* [flush-time](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#flush_time)
* [ft-boolean-syntax](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#ft_boolean_syntax)
* [ft-max-word-len](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#ft_max_word_len)
* [ft-min-word-len](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#ft_min_word_len)
* [ft-query-expansion-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#ft_query_expansion_limit)
* [ft-stopword-file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#ft_stopword_file)
* [general-log](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#general_log)
* [general-log-file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#general_log_file)
* [group-concat-max-len](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#group_concat_max_len)
* [histogram-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#histogram_size)
* [histogram-type](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#histogram_type)
* [host-cache-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#host_cache_size)
* [idle-readonly-transaction-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_readonly_transaction_timeout)
* [idle-transaction-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout)
* [idle-write-transaction-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_write_transaction_timeout)
* [ignore-db-dirs](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#ignore_db_dirs)
* [in-predicate-conversion-threshold](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#in_predicate_conversion_threshold)
* [init-connect](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#init_connect)
* [init-file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#init_file)
* [interactive-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#interactive_timeout)
* [large-pages](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#large_pages)
* [local-infile](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#local_infile)
* [lock-wait-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lock_wait_timeout)
* [log](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log)
* [log-disabled-statements](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_disabled_statements)
* [log-error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error)
* [log-output](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_output)
* [log-queries-not-using-indexes](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_queries_not_using_indexes)
* [log-slow-admin-statements](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements)
* [log-slow-always-query-time](../server-monitoring-logs/slow-query-log/log_slow_always_query_time-system-variable.md)
* [log-slow-disabled-statements](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_disabled_statements)
* [log-slow-filter](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter)
* [log-slow-min-examined-row-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_min_examined_row_limit)
* [log-slow-queries](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_queries)
* [log-slow-query](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query)
* [log-slow-query-file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_file)
* [log-slow-query-time](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_time)
* [log-slow-rate-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_rate_limit)
* [log-slow-slave-statements](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_slow_slave_statements)
* [log-slow-verbosity](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_verbosity)
* [log-tc-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_tc_size)
* [log-warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings)
* [long-query-time](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#long_query_time)
* [low-priority-updates](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#low_priority_updates)
* [lower-case-table-names](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lower_case_table_names)
* [max-allowed-packet](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet)
* [max-connections](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_connections)
* [max-connect-errors](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_connect_errors)
* [max-delayed-threads](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_delayed_threads)
* [max-digest-length](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_digest_length")
* [max-error-count](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_error_count)
* [max-length-for-sort-data](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_length_for_sort_data)
* [max-long-data-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_long_data_size)
* [max-password-errors](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_password_errors)
* [max-prepared-stmt-count](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_prepared_stmt_count)
* [max-recursive-iterations](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_recursive_iterations)
* [max-rowid-filter-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_rowid_filter_size)
* [max-session-mem-used](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_session_mem_used)
* [max-sp-recursion-depth](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_sp_recursion_depth)
* [max-statement-time](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_statement_time)
* [max-tmp-session-space-usage](../../security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_session_space_usage-system-variable.md)
* [max-tmp-tables](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_tmp_tables)
* [max-tmp-total-space-usage](../../security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_total_space_usage-system-variable.md)
* [max-user-connections](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_user_connections)
* [max-write-lock-count](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_write_lock_count)
* [metadata-locks-cache-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#metadata_locks_cache_size)
* [metadata-locks-hash-instances](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#metadata_locks_hash_instances)
* [min-examined-row-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#min_examined_row_limit)
* [mrr-buffer-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#mrr_buffer_size)
* [multi-range-count](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#multi_range_count)
* [--mysql56-temporal-format](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format)
* [net-buffer-length](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#net_buffer_length)
* [net-read-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#net_read_timeout)
* [net-retry-count](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#net_retry_count)
* [net-write-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#net_write_timeout)
* [open-files-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#open_files_limit)
* [pid-file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#pid_file)
* [plugin-dir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir)
* [plugin-maturity](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_maturity)
* [port](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#port)
* [preload-buffer-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#preload_buffer_size)
* [profiling-history-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#profiling_history_size)
* [progress-report-time](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#progress_report_time)
* [proxy-protocol-networks](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#proxy_protocol_networks)
* [query-cache-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_limit)
* [query-cache-min-res-unit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_min_res_unit)
* [query-cache-strip-comments](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_strip_comments)
* [query-cache-wlock-invalidate](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_wlock_invalidate)
* [read-rnd-buffer-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_rnd_buffer_size)
* [read-only](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_only)
* [redirect-url](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#redirect_url)
* [require-secure-transport](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#require_secure_transport)
* [safe-show-database](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#safe_show_database)
* [secure-auth](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_auth)
* [secure-file-priv](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_file_priv)
* [secure-timestamp](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_timestamp)
* [session-track-schema](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#session_track_schema)
* [session-track-state-change](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#session_track_state_change)
* [session-track-system-variables](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#session_track_system_variables)
* [session-track-transaction-info](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#session_track_transaction_info)
* [skip-automatic-sp-privileges](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges)
* [skip-external-locking](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_external_locking)
* [skip-large-pages](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#large_pages)
* [skip-log-error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error)
* [skip-name-resolve](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_name_resolve)
* [skip-networking](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_networking)
* [skip-show-database](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_show_database)
* [slow-launch-time](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#slow_launch_time)
* [slow-query-log](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log)
* [slow-query-log-file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file)
* [socket](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#socket)
* [sort-buffer-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sort_buffer_size)
* [sql-if-exists](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_if_exists)
* [sql-mode](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode)
* [ssl-ca](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-capath](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-cert](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-cipher](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-crl](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-crlpath](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-key](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [standards\_compliant\_cte](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#standards_compliant_cte)
* [stored-program-cache](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#stored_program_cache)
* [strict\_password\_validation](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#strict_password_validation)
* [sync-frm](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sync_frm)
* [system-versioning-alter-history](../../reference/sql-structure/temporal-tables/system-versioned-tables.md#system_versioning_alter_history)
* [system-versioning-asof](../../reference/sql-structure/temporal-tables/system-versioned-tables.md#system_versioning_asof)
* [system-versioning-innodb-algorithm-simple](../../reference/sql-structure/temporal-tables/system-versioned-tables.md#system_versioning_innodb_algorithm_simple)
* [system-versioning-insert-history](../../reference/sql-structure/temporal-tables/system-versioned-tables.md#system_versioning_insert_history)
* [table-lock-wait-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#table_lock_wait_timeout)
* [tcp-keepalive-interval](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tcp_keepalive_interval)
* [tcp-keepalive-probes](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tcp_keepalive_probes)
* [tcp-keepalive-time](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tcp_keepalive_time)
* [tcp-nodelay](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tcp_nodelay)
* [thread-cache-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size)
* [thread-concurrency](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#thread_concurrency)
* [thread-handling](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#thread_handling)
* [thread-pool-dedicated-listener](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-exact-stats](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-idle-timeout](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-max-threads](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-min-threads](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-oversubscribe](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-prio-kickup-timer](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-priority](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-size](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-stall-limit](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-stack](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#thread_stack)
* [timed-mutexes](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#timed_mutexes)
* [time-format](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#time_format)
* [tls-version](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [tmpdir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tmpdir)
* [transaction-isolation](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_isolation)
* [transaction-alloc-block-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#transaction_alloc_block_size)
* [transaction-prealloc-size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#transaction_prealloc_size)
* [transaction-read-only](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_read_only)
* [updatable-views-with-limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#updatable_views_with_limit)
* [userstat](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#userstat)
* [version](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#version)
* [wait-timeout](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#wait_timeout)

## Authentication Plugins - Options and System Variables

### Authentication Plugin - `ed25519`

The options related to the [ed25519](../../../reference/plugins/authentication-plugins/authentication-plugin-ed25519.md) authentication plugin can be found [here](../../reference/plugins/authentication-plugins/authentication-plugin-ed25519.md#options).

### Authentication Plugin - `gssapi`

The system variables related to the [gssapi](../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md) authentication plugin can be found [here](../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md#system-variables).

The options related to the [gssapi](../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md) authentication plugin can be found [here](../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md#options).

### Authentication Plugin - `named_pipe`

The options related to the [named\_pipe](../../../reference/plugins/authentication-plugins/authentication-plugin-named-pipe.md) authentication plugin can be found [here](../../reference/plugins/authentication-plugins/authentication-plugin-named-pipe.md#options).

### Authentication Plugin - `pam`

The system variables related to the [pam](../../../reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md) authentication plugin can be found [here](../../reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#system-variables).

The options related to the [pam](../../../reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md) authentication plugin can be found [here](../../reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#options).

### Authentication Plugin - `unix_socket`

The options related to the [unix\_socket](../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin can be found [here](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md#options).

## Encryption Plugins - Options and System Variables

### Encryption Plugin - `aws_key_management`

The system variables related to the [aws\_key\_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md) encryption plugin can be found [here](../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md#system-variables).

The options elated to the [aws\_key\_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md) encryption plugin can be found [here](../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md#options).

### Encryption Plugin - `file_key_management`

The system variables related to the [file\_key\_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) encryption plugin can be found [here](../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#system-variables).

The options related to the [file\_key\_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) encryption plugin can be found [here](../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#options).

## Password Validation Plugins - Options and System Variables

### Password Validation Plugin - `simple_password_check`

The system variables related to the [simple\_password\_check](../../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md) password validation plugin can be found [here](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md).

The options related to the [simple\_password\_check](../../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md) password validation plugin can be found [here](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md).

### Password Validation Plugin - `cracklib_password_check`

The system variables related to the [cracklib\_password\_check](../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin can be found [here](../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md).

The options related to the [cracklib\_password\_check](../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin can be found [here](../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md).

## Audit Plugins - Options and System Variables

### Audit Plugin - `server_audit`

Options and system variables related to the [server\_audit](../../../reference/plugins/mariadb-audit-plugin/) audit plugin can be found [here](../../reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md).

### Audit Plugin - `SQL_ERROR_LOG`

The options and system variables related to the [SQL\_ERROR\_LOG](../server-monitoring-logs/sql-error-log-plugin.md) audit plugin can be found [here](../../ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md#system-variables).

### Audit Plugin - QUERY\_RESPONSE\_TIME\_AUDIT

The options related to the [QUERY\_RESPONSE\_TIME\_AUDIT](../../../reference/plugins/other-plugins/query-response-time-plugin.md) audit plugin can be found [here](../../reference/plugins/other-plugins/query-response-time-plugin.md#options).

## Daemon Plugins - Options and System Variables

### Daemon Plugin - `handlersocket`

The options for the HandlerSocket plugin are all described on the [HandlerSocket Configuration Option](../../reference/sql-structure/nosql/handlersocket/handlersocket-configuration-options.md) page.

## Information Schema Plugins - Options and System Variables

### Information Schema Plugin - `DISKS`

The options related to the [DISKS](../../../reference/plugins/other-plugins/disks-plugin.md) information schema plugin can be found [here](../../reference/plugins/other-plugins/disks-plugin.md#options).

### Information Schema Plugin - `feedback`

The system variables related to the [feedback](../../../reference/plugins/other-plugins/feedback-plugin.md) plugin can be found [here](../../reference/plugins/other-plugins/feedback-plugin.md#system-variables).

The options related to the [feedback](../../../reference/plugins/other-plugins/feedback-plugin.md) plugin can be found [here](../../reference/plugins/other-plugins/feedback-plugin.md#options).

### Information Schema Plugin - `LOCALES`

The options related to the [LOCALES](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md) information schema plugin can be found [here](../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md#options).

### Information Schema Plugin - `METADATA_LOCK_INFO`

The options related to the [METADATA\_LOCK\_INFO](../../../reference/plugins/other-plugins/metadata-lock-info-plugin.md) information schema plugin can be found [here](../../reference/plugins/other-plugins/metadata-lock-info-plugin.md).

### Information Schema Plugin - `QUERY_CACHE_INFO`

The options related to the [QUERY\_CACHE\_INFO](../../../reference/plugins/other-plugins/query-cache-information-plugin.md) information schema plugin can be found [here](../../reference/plugins/other-plugins/query-cache-information-plugin.md#options).

### Information Schema Plugin - `QUERY_RESPONSE_TIME`

The system variables related to the [QUERY\_RESPONSE\_TIME](../../../reference/plugins/other-plugins/query-response-time-plugin.md) information schema plugin can be found [here](../../reference/plugins/other-plugins/query-response-time-plugin.md#system-variables).

The options related to the [QUERY\_RESPONSE\_TIME](../../../reference/plugins/other-plugins/query-response-time-plugin.md) information schema plugin can be found [here](../../reference/plugins/other-plugins/query-response-time-plugin.md#options).

### Information Schema Plugin - `user_variables`

The options related to the [user\_variables](../../../reference/plugins/other-plugins/user-variables-plugin.md) information schema plugin can be found [here](../../reference/plugins/other-plugins/user-variables-plugin.md#options).

### Information Schema Plugin - `WSREP_MEMBERSHIP`

The options related to the [WSREP\_MEMBERSHIP](../../../reference/plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md) information schema plugin can be found [here](../../reference/plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md#options).

### Information Schema Plugin - `WSREP_STATUS`

The options related to the [WSREP\_STATUS](../../../reference/plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md) information schema plugin can be found [here](../../reference/plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md#options).

## Replication Plugins - Options and System Variables

### Replication Plugin - `rpl_semi_sync_master`

The system variables related to the [rpl\_semi\_sync\_master](../../../server-usage/replication-cluster-multi-master/standard-replication/semisynchronous-replication.md) replication plugin can be found [here](../../ha-and-performance/standard-replication/semisynchronous-replication.md#system-variables).

The options related to the [rpl\_semi\_sync\_master](../../../server-usage/replication-cluster-multi-master/standard-replication/semisynchronous-replication.md) replication plugin can be found [here](../../ha-and-performance/standard-replication/semisynchronous-replication.md#options).

### Replication Plugin - `rpl_semi_sync_slave`

The system variables related to the [rpl\_semi\_sync\_slave](../../../server-usage/replication-cluster-multi-master/standard-replication/semisynchronous-replication.md) replication plugin can be found [here](../../ha-and-performance/standard-replication/semisynchronous-replication.md#system-variables).

The options related to the [rpl\_semi\_sync\_slave](../../../server-usage/replication-cluster-multi-master/standard-replication/semisynchronous-replication.md) replication plugin can be found [here](../../ha-and-performance/standard-replication/semisynchronous-replication.md#options).

## Default Values

You can verify the default values for an option by doing:

```
mariadbd --no-defaults --help --verbose
```

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
