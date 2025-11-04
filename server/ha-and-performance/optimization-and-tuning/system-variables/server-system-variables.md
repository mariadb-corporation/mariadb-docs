# Server System Variables

### About the Server System Variables

MariaDB has many system variables that can be changed to suit your needs.

{% include "../../../.gitbook/includes/for-a-full-list-of-server-v....md" %}

Many of the general system variables are described on this page, but others are described elsewhere:

* [Aria System Variables](../../../server-usage/storage-engines/aria/aria-system-variables.md)
* [CONNECT System Variables](../../../server-usage/storage-engines/connect/connect-system-variables.md)
* [Galera System Variables](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables)
* [Global Transaction ID System Variables](../../standard-replication/gtid.md#system-variables-for-global-transaction-id)
* [HandlerSocket Plugin System Variables](../../../reference/sql-structure/nosql/handlersocket/handlersocket-configuration-options.md)
* [InnoDB System Variables](../../../server-usage/storage-engines/innodb/innodb-system-variables.md)
* [Mroonga System Variables](../../../server-usage/storage-engines/mroonga/mroonga-system-variables.md)
* [MyRocks System Variables](../../../server-usage/storage-engines/myrocks/myrocks-system-variables.md)
* [MyISAM System Variables](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [Performance Schema System Variables](../../../reference/system-tables/performance-schema/performance-schema-system-variables.md)
* [Replication and Binary Log System Variables](../../standard-replication/replication-and-binary-log-system-variables.md)
* [S3 Storage Engine System Variables](../../../server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables.md)
* [Server\_Audit System Variables](../../../reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md)
* [Spider System Variables](../../../server-usage/storage-engines/spider/spider-system-variables.md)
* [SQL\_ERROR\_LOG Plugin System Variables](sql-error-log-system-variables-and-options.md)
* [SSL System Variables](../../../security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [Threadpool System Variables](../buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [TokuDB System Variables](../../../server-usage/storage-engines/legacy-storage-engines/tokudb/tokudb-system-variables.md)
* [Vector System Variables](../../../reference/sql-structure/vectors/vector-system-variables.md)

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

Most of these can be set with [command line options](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) and many of them can be changed at runtime.\
Variables that can be changed at runtime (and therefore are not read-only) are described as "Dynamic" below, and elsewhere in the documentation.

There are a few ways to see the full list of server system variables:

* While in the mariadb client, run:

```sql
SHOW VARIABLES;
```

* See [SHOW VARIABLES](../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) for instructions on using this command.
* From your shell, run mariadbd like so:

```
mariadbd --verbose --help
```

* View the Information Schema [GLOBAL\_VARIABLES](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-global_variables-and-session_variables-tables.md), [SESSION\_VARIABLES](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-global_variables-and-session_variables-tables.md), and [SYSTEM\_VARIABLES](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-system_variables-table.md) tables.

### Setting Server System Variables

There are several ways to set server system variables:

* Specify them on the command line:

```
shell> ./mariadbd-safe --aria_group_commit="hard"
```

* Specify them in your my.cnf file (see [Configuring MariaDB with my.cnf](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) for more information):

```
aria_group_commit = "hard"
```

* Set them from the mariadb client using the [SET](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) command. Only variables that are dynamic can be set at runtime in this way. Note that variables set in this way will not persist after a restart.

```sql
SET GLOBAL aria_group_commit="hard";
```

By convention, server variables have usually been specified with an underscore in the configuration files, and a dash on the command line. You can however specify underscores as dashes - they are interchangeable.

Variables that take a numeric size can either be specified in full, or with a suffix for easier readability. Valid suffixes are:

| Suffix | Description | Value                                                                                                                                                                    |
| ------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| K      | kilobytes   | 1024                                                                                                                                                                     |
| M      | megabytes   | 10242                                                                                                                                                                    |
| G      | gigabytes   | 10243                                                                                                                                                                    |
| T      | terabytes   | 10244 (from [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)) |
| P      | petabytes   | 10245 (from [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)) |
| E      | exabytes    | 10246 (from [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)) |

The suffix can be upper or lower-case.

### List of Server System Variables

#### `allow_suspicious_udfs`

* Description: Allows use of [user-defined functions](../../../server-usage/user-defined-functions/) consisting of only one symbol `x()` without corresponding `x_init()` or `x_deinit()`. That also means that one can load any function from any library, for example `exit()` from `libc.so`. Not recommended unless you require old UDFs with one symbol that cannot be recompiled. Before [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010), available as an [option only](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-allow-suspicious-udfs).
* Command line: `--allow-suspicious-udfs`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `alter_algorithm`

* Description: The implied `ALGORITHM` for [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) if no `ALGORITHM` clause is specified. The deprecated variable [old\_alter\_table](server-system-variables.md#old_alter_table) is an alias for this. The feature was removed in [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115). See [ALGORITHM=DEFAULT](../../../reference/sql-statements/data-definition/alter/alter-table/#algorithmdefault).
  * `COPY` corresponds to the pre-MySQL 5.1 approach of creating an intermediate table, copying data one row at a time, and renaming and dropping tables.
  * `INPLACE` requests that the operation be refused if it cannot be done natively inside a the storage engine.
  * `DEFAULT` (the default) chooses `INPLACE` if available, and falls back to `COPY`.
  * `NOCOPY` refuses to copy a table.
  * `INSTANT` refuses an operation that would involve any other than metadata changes.
* Command line: `--alter-algorithm=default`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumerated`
* Default Value: `DEFAULT`
* Valid Values: `DEFAULT`, `COPY`, `INPLACE`, `NOCOPY`, `INSTANT`
* Introduced: [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes)
* Deprecated: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)

#### `analyze_max_length`

* Description: Prevents collection of column statistics for [`CHAR`](../../../reference/data-types/string-data-types/char.md)/[`VARCHAR`](../../../reference/data-types/string-data-types/varchar.md) columns that can be analyzed automatically by [`ANALYZE TABLE PERSISTENT`](../../../reference/sql-statements/table-statements/analyze-table.md). Columns exceeding this threshold in bytes will be skipped unless included explicitly in [`FOR COLUMNS(...)`](../../../reference/sql-statements/table-statements/analyze-table.md#skipping-long-char-varchar-columns).
* Command line: `--analyze-max-length=val`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `INT UNSIGNED`
* Default Value: `4294967295 (4G)`
* Range: `32` to `4294967295`
* Introduced: [MariaDB 10.6.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10.6.23-release-notes), [MariaDB 10.11.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10.11.14-release-notes), [MariaDB 11.4.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11.4.8-release-notes), [MariaDB 11.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-8-series/mariadb-11.8.3-release-notes), [MariaDB 12.0.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/mariadb-12.0.2-release-notes), [MariaDB 12.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/mariadb-12.1.1-release-notes), [MariaDB Enterprise Server 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11.8/whats-new-in-mariadb-enterprise-server-11.8)

#### `analyze_sample_percentage`

* Description: Percentage of rows from the table [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md) will sample to collect table statistics. Set to 0 to let MariaDB decide what percentage of rows to sample.
* Command line: `--analyze-sample-percentage=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100.000000`
* Range: `0` to `100`
* Introduced: [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes)

#### `autocommit`

* Description: If set to 1, the default, all queries are committed immediately. The [LOCK IN SHARE MODE](../../../reference/sql-statements/data-manipulation/selecting-data/lock-in-share-mode.md) and [FOR UPDATE](../../../reference/sql-statements/data-manipulation/selecting-data/for-update.md) clauses therefore have no effect. If set to 0, they are only committed upon a [COMMIT](../../../reference/sql-statements/transactions/commit.md) statement, or rolled back with a [ROLLBACK](../../../reference/sql-statements/transactions/rollback.md) statement. If autocommit is set to 0, and then changed to 1, all open transactions are immediately committed.
* Command line: `--autocommit[=#]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`

#### `automatic_sp_privileges`

* Description: When set to 1, the default, when a stored routine is created, the creator is automatically granted permission to [ALTER](../../../server-usage/stored-routines/stored-procedures/alter-procedure.md) (which includes dropping) and to EXECUTE the routine. If set to 0, the creator is not automatically granted these privileges.
* Command line: `--automatic-sp-privileges`, `--skip-automatic-sp-privileges`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`

#### `back_log`

* Description: Connections take a small amount of time to start, and this setting determines the number of outstanding connection requests MariaDB can have, or the size of the listen queue for incoming TCP/IP requests. Requests beyond this will be refused. Increase if you expect short bursts of connections. Cannot be set higher than the operating system limit (see the Unix listen() man page). If not set, set to `0`, or the `--autoset-back-log` option is used, will be autoset to the lower of `900` and (50 + [max\_connections](server-system-variables.md#max_connections)/5).
* Command line: `--back-log=#`
* Scope: Global
* Dynamic: No
* Type: number
* Default Value:
  * The lower of `900` and (50 + [max\_connections](server-system-variables.md#max_connections)/5)

#### `basedir`

* Description: Path to the MariaDB installation directory. Other paths are usually resolved relative to this base directory.
* Command line: `--basedir=path` or `-b path`
* Scope: Global
* Dynamic: No
* Type: directory name

#### `big_tables`

* Description: If this system variable is set to 1, then temporary tables will be saved to disk intead of memory.
  * This system variable's original intention was to allow result sets that were too big for memory-based temporary tables and to avoid the resulting 'table full' errors.
  * This system variable is no longer needed, because the server can automatically convert large memory-based temporary tables into disk-based temporary tables when they exceed the value of the [tmp\_memory\_table\_size](server-system-variables.md#tmp_memory_table_size) system variable.
  * To prevent memory-based temporary tables from being used at all, set the [tmp\_memory\_table\_size](server-system-variables.md#tmp_memory_table_size) system variable to `0`.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) and earlier, [sql\_big\_tables](server-system-variables.md#sql_big_tables) is a synonym.
  * From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105), this system variable is deprecated.
* Command line: `--big-tables`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`
* Deprecated: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes)
* Removed: [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120)

#### `bind_address`

* Description: By default, the MariaDB server listens for TCP/IP connections on all addresses. You can specify an alternative when the server starts using this option; either a host name, an IPv4 or an IPv6 address, "::" or "_" (all addresses). In some systems, such as Debian and Ubuntu, the bind\_address is set to 127.0.0.1, which binds the server to listen on localhost only. `bind_address` has always been available as a_ [_mariadbd option_](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md)_; from_ [_MariaDB 10.3.3_](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes) _its also available as a system variable. Before_ [_MariaDB 10.6.0_](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes) _"::" implied listening additionally on IPv4 addresses like "_". From 10.6.0 onwards it refers to IPv6 stictly. Starting with [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), a comma-separated list of addresses to bind to can be given. See also [Configuring MariaDB for Remote Client Access](../../../mariadb-quickstart-guides/mariadb-remote-connection-guide.md).
* Command line: `--bind-address=addr`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: (Empty string)
* Valid Values: Host name, IPv4, IPv6, ::, \*
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes) (as a system variable)

#### `block_encryption_mode`

* Description: Default block encryption mode for [AES\_ENCRYPT()](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_encrypt.md) and [AES\_DECRYPT()](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_decrypt.md) functions.
* Command line: `--block-encryption-mode=val`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `aes-128-ecb`
* Valid values: `aes-128-ecb`, `aes-192-ecb`, `aes-256-ecb`, `aes-128-cbc`, `aes-192-cbc`, `aes-256-cbc`, `aes-128-ctr`, `aes-192-ctr`, `aes-256-ctr`
* Introduced: [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes)

#### `bulk_insert_buffer_size`

* Description: Size in bytes of the per-thread cache tree used to speed up bulk inserts into [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) and [Aria](../../../server-usage/storage-engines/aria/) tables. A value of 0 disables the cache tree.
* Command line: `--bulk-insert-buffer-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `8388608`
* Range - 32 bit: `0` to `4294967295`
* Range - 64 bit: `0` to `18446744073709547520`

#### `character_set_client`

* Description: Determines the [character set](../../../reference/data-types/string-data-types/character-sets/) for queries arriving from the client. It can be set per session by the client, although the server can be configured to ignore client requests with the `--skip-character-set-client-handshake` option. If the client does not request a character set, or requests a character set that the server does not support, the global value will be used. utf16, utf16le, utf32 and ucs2 cannot be used as client character sets. From [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106), the `utf8` [character set](../../../reference/data-types/string-data-types/character-sets/) (and related collations) is by default an alias for `utf8mb3` rather than the other way around. It can be set to imply `utf8mb4` by changing the value of the [old\_mode](server-system-variables.md#old_mode) system variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value:&#x20;
  * \>= [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116): `utf8mb4`
  * <= [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115): `latin1`&#x20;

#### `character_set_collations`

* Description: Overrides for character set default collations. Takes a comma-delimited list of character set and collation settings, for example `SET @@character_set_collations = 'utf8mb4=uca1400_ai_ci, latin2=latin2_hungarian_ci';` The new variable will take effect in all cases where a character set is explicitly or implicitly specified without an explicit COLLATE clause, including but not limited to:
  * Column collation
  * Table collation
  * Database collation
  * CHAR(expr USING csname)
  * CONVERT(expr USING csname)
  * CAST(expr AS CHAR CHARACTER SET csname)
  * '' - character string literal
  * \_utf8mb3'text' - a character string literal with an introducer
  * \_utf8mb3 X'61' - a character string literal with an introducer with hex notation
  * \_utf8mb3 0x61 - a character string literal with an introducer with hex hybrid notation
  * @@collation\_connection after a SET NAMES without COLLATE
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value:
  * `utf8mb3=utf8mb3_uca1400_ai_ci, ucs2=ucs2_uca1400_ai_ci, utf8mb4=utf8mb4_uca1400_ai_ci, utf16=utf16_uca1400_ai_ci, utf32=utf32_uca1400_ai_ci` (>= [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115))
  * Empty (<= [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114))
* Introduced: [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112)

#### `character_set_connection`

* Description: [Character set](../../../reference/data-types/string-data-types/character-sets/) used for number to string conversion, as well as for literals that don't have a character set introducer. From [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106), the `utf8` [character set](../../../reference/data-types/string-data-types/character-sets/) (and related collations) is by default an alias for `utf8mb3` rather than the other way around. It can be set to imply `utf8mb4` by changing the value of the [old\_mode](server-system-variables.md#old_mode) system variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value:&#x20;
  * \>=[ MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116): `utf8mb4`
  * \>= [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106): `utf8mb3`
  * <= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105): `utf8`

#### `character_set_database`

* Description: [Character set](../../../reference/data-types/string-data-types/character-sets/) used by the default database, and set by the server whenever the default database is changed. If there's no default database, character\_set\_database contains the same value as [character\_set\_server](server-system-variables.md#character_set_server). This variable is dynamic, but should not be set manually, only by the server.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `utf8mb4` (>= [MariaDB 11.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-0-release-notes)), `latin1` (<= [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115))

#### `character_set_filesystem`

* Description: The [character set](../../../reference/data-types/string-data-types/character-sets/) for the filesystem. Used for converting file names specified as a string literal from [character\_set\_client](server-system-variables.md#character_set_client) to character\_set\_filesystem before opening the file. By default set to `binary`, so no conversion takes place. This could be useful for statements such as [LOAD\_FILE()](../../../reference/sql-functions/string-functions/load_file.md) or [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) on system where multi-byte file names are use.
* Command line: `--character-set-filesystem=name`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `binary`

#### `character_set_results`

* Description: [Character set](../../../reference/data-types/string-data-types/character-sets/) used for results and error messages returned to the client. From [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106), the `utf8` [character set](../../../reference/data-types/string-data-types/character-sets/) (and related collations) is by default an alias for `utf8mb3` rather than the other way around. It can be set to imply `utf8mb4` by changing the value of the [old\_mode](server-system-variables.md#old_mode) system variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `utf8mb3` (>= [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106)), `utf8` (<= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105))

#### `character_set_server`

* Description: Default [character set](../../../reference/data-types/string-data-types/character-sets/) used by the server. See [character\_set\_database](server-system-variables.md#character_set_database) for character sets used by the default database. Defaults may be different on some systems, see for example [Differences in MariaDB in Debian](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md).
* Command line: `--character-set-server`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `utf8mb4` (>= [MariaDB 11.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-0-release-notes)), `latin1` (<= [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115))

#### `character_set_system`

* Description: [Character set](../../../reference/data-types/string-data-types/character-sets/) used by the server to store identifiers, always set to utf8, or its synonym utf8mb3 starting with [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106). From [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106), the `utf8` [character set](../../../reference/data-types/string-data-types/character-sets/) (and related collations) is by default an alias for `utf8mb3` rather than the other way around. It can be set to imply `utf8mb4` by changing the value of the [old\_mode](server-system-variables.md#old_mode) system variable.
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `utf8mb3` (>= [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106)), `utf8` (<= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105))

#### `character_sets_dir`

* Description: Directory where the [character sets](../../../reference/data-types/string-data-types/character-sets/) are installed.
* Command line: `--character-sets-dir=path`
* Scope: Global
* Dynamic: No
* Type: directory name

#### `check_constraint_checks`

* Description: If set to `0`, will disable [constraint checks](../../../reference/sql-statements/data-definition/constraint.md), for example when loading a table that violates some constraints that you plan to fix later.
* Scope: Global, Session
* Dynamic: Yes
* Type: boolean
* Default: ON

#### `collation_connection`

* Description: Collation used for the connection [character set](../../../reference/data-types/string-data-types/character-sets/).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`

#### `collation_database`

* Description: [Collation used](../../../reference/data-types/string-data-types/character-sets/) for the default database. Set by the server if the default database changes, if there is no default database the value from the `collation_server` variable is used. This variable is dynamic, but should not be set manually, only by the server.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`

#### `collation_server`

* Description: Default [collation](../../../reference/data-types/string-data-types/character-sets/) used by the server. This is set to the default collation for a given character set automatically when [character\_set\_server](server-system-variables.md#character_set_server) is changed, but it can also be set manually. Defaults may be different on some systems, see for example [Differences in MariaDB in Debian](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md).
* Command line: `--collation-server=name`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `latin1_swedish_ci`

#### `completion_type`

* Description: The transaction completion type. If set to `NO_CHAIN` or `0` (the default), there is no effect on commits and rollbacks. If set to `CHAIN` or `1`, a [COMMIT](../../../reference/sql-statements/transactions/commit.md) statement is equivalent to COMMIT AND CHAIN, while a [ROLLBACK](../../../reference/sql-statements/transactions/rollback.md) is equivalent to ROLLBACK AND CHAIN, so a new transaction starts straight away with the same isolation level as transaction that's just finished. If set to `RELEASE` or `2`, a [COMMIT](../../../reference/sql-statements/transactions/commit.md) statement is equivalent to COMMIT RELEASE, while a [ROLLBACK](../../../reference/sql-statements/transactions/rollback.md) is equivalent to ROLLBACK RELEASE, so the server will disconnect after the transaction completes. Note that the transaction completion type only applies to explicit commits, not implicit commits.
* Command line: `--completion-type=name`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumerated`
* Default Value: `NO_CHAIN`
* Valid Values: `0`, `1`, `2`, `NO_CHAIN`, `CHAIN`, `RELEASE`

#### `concurrent_insert`

* Description: If set to `AUTO` or `1`, the default, MariaDB allows [concurrent INSERTs](../../../reference/sql-statements/data-manipulation/inserting-loading-data/concurrent-inserts.md) and SELECTs for [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) tables with no free blocks in the data (deleted rows in the middle). If set to `NEVER` or `0`, concurrent inserts are disabled. If set to `ALWAYS` or `2`, concurrent inserts are permitted for all MyISAM tables, even those with holes, in which case new rows are added at the end of a table if the table is being used by another thread. If the [--skip-new](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-skip-new) option is used when starting the server, concurrent\_insert is set to `NEVER`. Changing the variable only affects new opened tables. Use [FLUSH TABLES](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) If you want it to also affect cached tables. See [Concurrent Inserts](../../../reference/sql-statements/data-manipulation/inserting-loading-data/concurrent-inserts.md) for more.
* Command line: `--concurrent-insert[=value]`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumerated`
* Default Value: `AUTO`
* Valid Values: `0`, `1`, `2`, `AUTO`, `NEVER`, `ALWAYS`

#### `connect_timeout`

* Description: Time in seconds that the server waits for a connect packet before returning a 'Bad handshake'. Increasing may help if clients regularly encounter 'Lost connection to MySQL server at 'X', system error: error\_number' type-errors.
* Command line: `--connect-timeout=#`
* Scope: Global
* Dynamic: Yes
* Type: numeric
* Default Value: `10`
* Range: `2` to `31536000`

#### `core_file`

* Description: Write a core-file on crashes. The file name and location are system dependent. On Linux it is usually called `core.${PID}`, and it is usually written to the data directory. However, this can be changed.
  * See [Enabling Core Dumps](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/enabling-core-dumps) for more information.
  * Previously this system variable existed only as an [option](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md), but it was also made into a read-only system variable starting with [MariaDB 10.3.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1039-release-notes), [MariaDB 10.2.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10217-release-notes) and [MariaDB 10.1.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10135-release-notes).
  * On Windows >= [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes), this option is set by default.
  * Note that the option accepts no arguments; specifying `--core-file` sets the value to `ON`. It cannot be disabled in the case of Windows >= [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes).
* Command line: `--core-file`
* Scope: Global
* Dynamic: No
* Type: boolean
* Default Value:
  * Windows >= [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes): `ON`
  * All other systems: `OFF`

#### `datadir`

* Description: Directory where the data is stored.
* Command line: `--datadir=path` or `-h path`
* Scope: Global
* Dynamic: No
* Type: directory name

#### `date_format`

* Description: Unused.
* Removed: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `datetime_format`

* Description: Unused.
* Removed: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `debug/debug_dbug`

* Description: Available in debug builds only (built with -DWITH\_DEBUG=1). Used in debugging through the DBUG library to write to a trace file. Just using `--debug` will write a trace of what mariadbd is doing to the default trace file.
* Command line: `-#`, `--debug[=debug_options]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value:
  * > \= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105): `d:t:i:o,/tmp/mariadbd.trace` (Unix) or `d:t:i:O,\mariadbd.trace` (Windows)
* Debug Options: See the option flags on the [mysql\_debug](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_debug) page

#### `debug_no_thread_alarm`

* Description: Disable system thread alarm calls. Disabling it may be useful in debugging or testing, never do it in production.
* Command line: `--debug-no-thead-alarm=#`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114)

#### `debug_sync`

* Description: Used in debugging to show the interface to the [Debug Sync facility](../../../clients-and-utilities/testing-tools/mariadb-test/the-debug-sync-facility.md). MariaDB needs to be configured with -DENABLE\_DEBUG\_SYNC=1 for this variable to be available.
* Scope: Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `OFF` or `ON - current signal name`

#### `default_password_lifetime`

* Description: This defines the global [password expiration policy](../../../security/user-account-management/user-password-expiry.md). 0 means automatic password expiration is disabled. If the value is a positive integer N, the passwords must be changed every N days. This behavior can be overridden using the password expiration options in [ALTER USER](../../../reference/sql-statements/account-management-sql-statements/alter-user.md).
* Command line: `--default-password-lifetime=#`
* Scope: Global
* Dynamic: Yes
* Type: numeric
* Default Value: `0`
* Range: `0` to `4294967295`

#### `default_regex_flags`

* Description: Introduced to address remaining incompatibilities between [PCRE](../../../reference/sql-functions/string-functions/regular-expressions-functions/pcre.md) and the old regex library. Accepts a comma-separated list of zero or more of the following values:

<table><thead><tr><th width="160"></th><th width="165"></th><th></th></tr></thead><tbody><tr><td>Value</td><td>Pattern equivalent</td><td>Meaning</td></tr><tr><td>DOTALL</td><td>(?s)</td><td>. matches anything including NL</td></tr><tr><td>DUPNAMES</td><td>(?J)</td><td>Allow duplicate names for subpatterns</td></tr><tr><td>EXTENDED</td><td>(?x)</td><td>Ignore white space and comments</td></tr><tr><td>EXTRA</td><td>(?X)</td><td>extra features (e.g. error on unknown escape character)</td></tr><tr><td>MULTILINE</td><td>(?m)</td><td>^ and $ match newlines within data</td></tr><tr><td>UNGREEDY</td><td>(?U)</td><td>Invert greediness of quantifiers</td></tr></tbody></table>

* Command line: `--default-regex-flags=value`
* Scope: Global, Session
* Dynamic: Yes
* Type: enumeration
* Default Value: empty
* Valid Values: `DOTALL`, `DUPNAMES`, `EXTENDED`, `EXTRA`, `MULTILINE`, `UNGREEDY`

#### `default_storage_engine`

* Description: The default [storage engine](../../../server-usage/storage-engines/). The default storage engine must be enabled at server startup or the server won't start.
* Command line: `--default-storage-engine=name`
* Scope: Global, Session
* Dynamic: Yes
* Type: enumeration
* Default Value: `InnoDB`

#### `default_table_type`

* Description: A synonym for [default\_storage\_engine](server-system-variables.md#default_storage_engine). Removed in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).
* Command line: `--default-table-type=name`
* Scope: Global, Session
* Dynamic: Yes
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `default_tmp_storage_engine`

* Description: Default storage engine that will be used for tables created with [CREATE TEMPORARY TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) where no engine is specified. For internal temporary tables see [aria\_used\_for\_temp\_tables](../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_used_for_temp_tables)). The storage engine used must be active or the server will not start. See [default\_storage\_engine](server-system-variables.md#default_storage_engine) for the default for non-temporary tables. Defaults to NULL, in which case the value from [default\_storage\_engine](server-system-variables.md#default_storage_engine) is used. [ROCKSDB](../../../server-usage/storage-engines/myrocks/) temporary tables cannot be created. Before [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107), attempting to do so would silently fail, and a MyISAM table would instead be created. From [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107), an error is returned.
* Command line: `--default-tmp-storage-engine=name`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: NULL

#### `default_week_format`

* Description: Default mode for the [WEEK()](../../../reference/sql-functions/date-time-functions/week.md) function. See that page for details on the different modes
* Command line: `--default-week-format=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `7`

#### `delay_key_write`

* Description: Specifies how MyISAM tables handles [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) DELAY\_KEY\_WRITE. If set to `ON`, the default, any DELAY KEY WRITEs are honored. The key buffer is then flushed only when the table closes, speeding up writes. MyISAM tables should be automatically checked upon startup in this case, and --external locking should not be used, as it can lead to index corruption. If set to `OFF`, DELAY KEY WRITEs are ignored, while if set to `ALL`, all new opened tables are treated as if created with DELAY KEY WRITEs enabled.
* Command line: `--delay-key-write[=name]`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `ON`
* Valid Values: `ON`, `OFF`, `ALL`

#### `delayed_insert_limit`

* Description: After this many rows have been inserted with [INSERT DELAYED](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md), the handler will check for and execute any waiting [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statements.
* Command line: `--delayed-insert-limit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `1` to `4294967295`

#### `delayed_insert_timeout`

* Description: Time in seconds that the [INSERT DELAYED](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) handler will wait for INSERTs before terminating.
* Command line: `--delayed-insert-timeout=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `300`

#### `delayed_queue_size`

* Description: Number of rows, per table, that can be queued when performing [INSERT DELAYED](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) statements. If the queue becomes full, clients attempting to perform INSERT DELAYED's will wait until the queue has room available again.
* Command line: `--delayed-queue-size=#`
* Scope: Global
* Dynamic: Yes
* Type: numeric
* Default Value: `1000`
* Range: `1 to 4294967295`

#### `disconnect_on_expired_password`

* Description: When a user password has expired (see [User Password Expiry](../../../security/user-account-management/user-password-expiry.md)), this variable controls how the server handles clients that are not aware of the sandbox mode. If enabled, the client is not permitted to connect, otherwise the server puts the client in a sandbox mode.
* Command line: `--disconnect-on-expired-password[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Type: boolean
* Default Value: `OFF`

#### `div_precision_increment`

* Description: The precision of the result of the decimal division will be the larger than the precision of the dividend by that number. By default it's `4`, so `SELECT 2/15` would return 0.1333 and `SELECT 2.0/15` would return 0.13333. After setting div\_precision\_increment to `6`, for example, the same operation would return 0.133333 and 0.1333333 respectively.

From [MariaDB 10.1.46](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes), [MariaDB 10.2.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10233-release-notes), [MariaDB 10.3.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10324-release-notes), [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes) and [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1055-release-notes), `div_precision_increment` is taken into account in intermediate calculations. Previous versions did not, and the results were dependent on the optimizer, and therefore unpredictable.

In [MariaDB 10.1.46](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes), [MariaDB 10.1.47](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10147-release-notes), [MariaDB 10.2.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10233-release-notes), [MariaDB 10.2.34](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10234-release-notes), [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10235-release-notes), [MariaDB 10.3.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10324-release-notes), [MariaDB 10.3.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10325-release-notes), [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes), [MariaDB 10.4.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10415-release-notes), [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1055-release-notes) and [MariaDB 10.5.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1056-release-notes) only, the fix truncated decimal values after every division, resulting in lower precision in some cases for those versions only.

From [MariaDB 10.1.48](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes), [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10235-release-notes), [MariaDB 10.3.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10326-release-notes), [MariaDB 10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10416-release-notes) and [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1057-release-notes), a different fix was implemented. Instead of truncating decimal values after every division, they are instead truncated for comparison purposes only.

For example

Versions other than [MariaDB 10.1.46](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes), [MariaDB 10.1.47](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10147-release-notes), [MariaDB 10.2.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10233-release-notes), [MariaDB 10.2.34](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10234-release-notes), [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10235-release-notes), [MariaDB 10.3.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10324-release-notes), [MariaDB 10.3.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10325-release-notes), [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes), [MariaDB 10.4.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10415-release-notes), [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1055-release-notes) and [MariaDB 10.5.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1056-release-notes):

```
SELECT (55/23244*1000);
+-----------------+
| (55/23244*1000) |
+-----------------+
| 2.3662          |
+-----------------+
```

[MariaDB 10.1.46](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes), [MariaDB 10.1.47](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10147-release-notes), [MariaDB 10.2.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10233-release-notes), [MariaDB 10.2.34](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10234-release-notes), [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10235-release-notes), [MariaDB 10.3.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10324-release-notes), [MariaDB 10.3.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10325-release-notes), [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes), [MariaDB 10.4.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10415-release-notes), [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1055-release-notes) and [MariaDB 10.5.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1056-release-notes) only:

```
SELECT (55/23244*1000);
+-----------------+
| (55/23244*1000) |
+-----------------+
| 2.4000          |
+-----------------+
```

This is because the intermediate result, `SELECT 55/23244` takes into account `div_precision_increment` and results were truncated after every division in those versions only.

* Command line: `--div-precision-increment=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4`
* Range: `0` to `30`

#### `encrypt_tmp_disk_tables`

* Description: Enables automatic encryption of all internal on-disk temporary tables that are created during query execution if [aria\_used\_for\_temp\_tables=ON](../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_used_for_temp_tables) is set. See [Data at Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [Enabling Encryption for Internal On-disk Temporary Tables](../../../security/securing-mariadb/encryption/data-at-rest-encryption/aria-encryption/aria-encryption-overview.md).
* Command line: `--encrypt-tmp-disk-tables[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `encrypt_tmp_files`

* Description: Enables automatic encryption of temporary files, such as those created for filesort operations, binary log file caches, etc. See [Data at Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Command line: `--encrypt-tmp-files[={0|1}]`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `encryption_algorithm`

* Description: Which encryption algorithm to use for table encryption. `aes_cbc` is the recommended one. See [Table and Tablespace Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Command line: `--encryption-algorithm=value`
* Scope: Global
* Dynamic: No
* Data Type: `enum`
* Default Value: `none`
* Valid Values: `none`, `aes_ecb`, `aes_cbc`, `aes_ctr`
* Introduced: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes)
* Removed: [MariaDB 10.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes)

#### `enforce_storage_engine`

* Description: Force the use of a particular storage engine for new tables. Used to avoid unwanted creation of tables using another engine. For example, setting to [InnoDB](../../../server-usage/storage-engines/innodb/) will prevent any [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) tables from being created. If another engine is specified in a [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement, the outcome depends on whether the `NO_ENGINE_SUBSTITUTION` [SQL\_MODE](../../../server-management/variables-and-modes/sql-mode.md) has been set or not. If set, the query will fail, while if not set, a warning will be returned and the table created according to the engine specified by this variable. The variable has a session scope, but is only modifiable by a user with the SUPER privilege.
* Command line: None
* Scope: Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `none`

#### `engine_condition_pushdown`

* Description: Deprecated in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) and removed and replaced by the [optimizer\_switch](server-system-variables.md#optimizer_switch) `engine_condition_pushdown={on|off}` flag in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0).. Specifies whether the engine condition pushdown optimization is enabled. Since [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes), engine condition pushdown is enabled for all engines that support it.
* Command line: `--engine-condition-pushdown`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `eq_range_index_dive_limit`

* Description: Limit used for speeding up queries listed by long nested INs. The optimizer will use existing index statistics instead of doing index dives for equality ranges if the number of equality ranges for the index is larger than or equal to this number. If set to `0` (unlimited), index dives are always used.
* Command line: `--eq-range-index-dive-limit=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `200`
* Range: `0` to `4294967295`

#### `error_count`

* Description: Read-only variable denoting the number of errors from the most recent statement in the current session that generated errors. See [SHOW\_ERRORS()](../../../reference/sql-statements/administrative-sql-statements/show/show-errors.md).
* Scope: Session
* Dynamic: Yes
* Data Type: `numeric`

#### `event_scheduler`

* Description: Status of the [Event](../../../server-usage/triggers-events/event-scheduler/events.md) Scheduler. Can be set to `ON` or `OFF`, while `DISABLED` means it cannot be set at runtime. Setting the variable will cause a load of events if they were not loaded at startup.
* Command line: `--event-scheduler[=value]`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `OFF`
* Valid Values: `ON` (or `1`), `OFF` (or `0`), `DISABLED`

#### `expensive_subquery_limit`

* Description: Number of rows to be examined for a query to be considered expensive, that is, maximum number of rows a subquery may examine in order to be executed during optimization and used for constant optimization.
* Command line: `--expensive-subquery-limit=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `0` upwards

#### `explicit_defaults_for_timestamp`

* Description: This option causes [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) to create all [TIMESTAMP](../../../reference/data-types/date-and-time-data-types/timestamp.md) columns as [NULL](../../../reference/data-types/null-values.md) with the DEFAULT NULL attribute, Without this option, TIMESTAMP columns are NOT NULL and have implicit DEFAULT clauses.
* Command line: `--explicit-defaults-for-timestamp=[={0|1}]`
* Scope:
  * Global, Session (>= [MariaDB 10.8.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes), [MariaDB 10.7.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes), [MariaDB 10.6.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1069-release-notes), [MariaDB 10.5.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10517-release-notes))
  * Global (<= [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes), [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.6.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1068-release-notes), [MariaDB 10.5.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10516-release-notes))
* Dynamic:
  * Yes (>= [MariaDB 10.8.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes), [MariaDB 10.7.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes), [MariaDB 10.6.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1069-release-notes), [MariaDB 10.5.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10517-release-notes))
  * No (<= [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes), [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.6.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1068-release-notes), [MariaDB 10.5.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10516-release-notes))
* Data Type: `boolean`
* Default Value:`ON` (>= [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)), `OFF` (<= [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109))

#### `external_user`

* Description: External user name set by the plugin used to authenticate the client. `NULL` if native MariaDB authentication is used. For example, from [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116), the [Unix socket authentication plugin](../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) permits an authentication string, so that the OS and MariaDB user will be different. `external_user` then contains the external OS user. See [Authentication Plugin - Unix Socket: Creating Users](../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md#creating-users)
* Scope: Session
* Dynamic: No
* Data Type: `string`
* Default Value: `NULL`

#### `flush`

* Description: Usually, MariaDB writes changes to disk after each SQL statement, and the operating system handles synchronizing (flushing) it to disk. If set to `ON`, the server will synchronize all changes to disk after each statement.
* Command line: `--flush`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `flush_time`

* Description: Interval in seconds that tables are closed to synchronize (flush) data to disk and free up resources. If set to 0, the default, there is no automatic synchronizing tables and closing of tables. This option should not be necessary on systems with sufficient resources.
* Command line: `--flush_time=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`

#### `foreign_key_checks`

* Description: If set to 1 (the default) [foreign key constraints](../optimization-and-indexes/foreign-keys.md) (including ON UPDATE and ON DELETE behavior) [InnoDB](../../../server-usage/storage-engines/innodb/) tables are checked, while if set to 0, they are not checked. `0` is not recommended for normal use, though it can be useful in situations where you know the data is consistent, but want to reload data in a different order from that specified by parent/child relationships. Setting this variable to 1 does not retrospectively check for inconsistencies introduced while set to 0.
* Command line: None
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`

#### `ft_boolean_syntax`

* Description: List of operators supported by an IN BOOLEAN MODE [full-text search](../optimization-and-indexes/full-text-indexes/). If you wish to change, note that each character must be ASCII and non-alphanumeric, the full string must be 14 characters and the first or second character must be a space (marking the behavior by default). Positions 10, 13 and 14 are reserved for future extensions. Also, no duplicates are permitted except for the phrase quoting characters in positions 11 and 12, which may be the same.
* Command line: `--ft-boolean-syntax=name`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `+ -><()*:""&|`

#### `ft_max_word_len`

* Description: Maximum length for a word to be included in the [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) [full-text index](../optimization-and-indexes/full-text-indexes/). If this variable is changed, the full-text index must be rebuilt in order for the new value to take effect. The quickest way to do this is by issuing a `REPAIR TABLE table_name QUICK` statement. See [innodb\_ft\_max\_token\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_ft_max_token_size) for the [InnoDB](../../../server-usage/storage-engines/innodb/) equivalent.
* Command line: `--ft-max-word-len=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `84`
* Minimum Value: `10`

#### `ft_min_word_len`

* Description: Minimum length for a word to be included in the [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) [full-text index](../optimization-and-indexes/full-text-indexes/). If this variable is changed, the full-text index must be rebuilt in order for the new value to take effect. The quickest way to do this is by issuing a `REPAIR TABLE table_name QUICK` statement. See [innodb\_ft\_min\_token\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_ft_min_token_size) for the [InnoDB](../../../server-usage/storage-engines/innodb/) equivalent.
* Command line: `--ft-min-word-len=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `4`
* Minimum Value: `1`

#### `ft_query_expansion_limit`

* Description: For [full-text searches](../optimization-and-indexes/full-text-indexes/), denotes the numer of top matches when using WITH QUERY EXPANSION.
* Command line: `--ft-query-expansion-limit=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `20`
* Range: `0` to `1000`

#### `ft_stopword_file`

* Description: File containing a list of [stopwords](../optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) for use in [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) [full-text searches](../optimization-and-indexes/full-text-indexes/). Unless an absolute path is specified the file will be looked for in the data directory. The file is not parsed for comments, so all words found become stopwords. By default, a built-in list of words (built from `storage/myisam/ft_static.c file`) is used. Stopwords can be disabled by setting this variable to `''` (an empty string). If this variable is changed, the full-text index must be rebuilt. The quickest way to do this is by issuing a `REPAIR TABLE table_name QUICK` statement. See [innodb\_ft\_server\_stopword\_table](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_ft_server_stopword_table) for the [InnoDB](../../../server-usage/storage-engines/innodb/) equivalent.
* Command line: `--ft-stopword-file=file_name`
* Scope: Global
* Dynamic: No
* Data Type: `file name`
* Default Value: `(built-in)`

#### `general_log`

* Description: If set to 0, the default unless the --general-log option is used, the [general query log](../../../server-management/server-monitoring-logs/general-query-log.md) is disabled, while if set to 1, the general query log is enabled. See [log\_output](server-system-variables.md#log_output) for how log files are written. If that variable is set to `NONE`, no logs will be written even if general\_query\_log is set to `1`.
* Command line: `--general-log`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`

#### `general_log_file`

* Description: Name of the [general query log](../../../server-management/server-monitoring-logs/general-query-log.md) file. If this is not specified, the name is taken from the [log-basename](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) setting or from your system hostname with `.log` as a suffix. If [--log-basename](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `general_log_file` should be placed after in the config files. Later settings override earlier settings, so `log-basename` will override any earlier log file name settings.
* Command line: `--general-log-file=file_name`
* Scope: Global
* Dynamic: Yes
* Data Type: `file name`
* Default Value: `host_name.log`

#### `group_concat_max_len`

* Description: Maximum length in bytes of the returned result for the functions [GROUP\_CONCAT()](../../../reference/sql-functions/aggregate-functions/group_concat.md), [JSON\_OBJECTAGG](../../../reference/sql-functions/special-functions/json-functions/json_objectagg.md) and [JSON\_ARRAYAGG](../../../reference/sql-functions/special-functions/json-functions/json_arrayagg.md).
* Command line: `--group-concat-max-len=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `1048576` (1M)
* Range: `4` to `4294967295`

.

#### `have_compress`

* Description: If the zlib compression library is accessible to the server, this will be set to `YES`, otherwise it will be `NO`. The [COMPRESS()](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/compress.md) and [UNCOMPRESS()](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/uncompress.md) functions will only be available if set to `YES`.
* Scope: Global
* Dynamic: No

#### `have_crypt`

* Description: If the crypt() system call is available this variable will be set to `YES`, otherwise it will be set to `NO`. If set to `NO`, the [ENCRYPT()](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/encrypt.md) function cannot be used.
* Scope: Global
* Dynamic: No

#### `have_csv`

* Description: If the server supports [CSV tables](../../../server-usage/storage-engines/csv/), will be set to `YES`, otherwise will be set to `NO`. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), use the [Information Schema PLUGINS](../../../reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table or [SHOW ENGINES](../../../reference/sql-statements/administrative-sql-statements/show/show-engines.md) instead.
* Scope: Global
* Dynamic: No
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `have_dynamic_loading`

* Description: If the server supports dynamic loading of [plugins](../../../reference/plugins/), will be set to `YES`, otherwise will be set to `NO`.
* Scope: Global
* Dynamic: No

#### `have_geometry`

* Description: If the server supports spatial data types, will be set to `YES`, otherwise will be set to `NO`.
* Scope: Global
* Dynamic: No

#### `have_ndbcluster`

* Description: If the server supports NDBCluster.
* Scope: Global
* Dynamic: No
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `have_partitioning`

* Description: If the server supports partitioning, will be set to `YES`, unless the `--skip-partition` option is used, in which case will be set to `DISABLED`. Will be set to `NO` otherwise. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) - [SHOW PLUGINS](../../../reference/sql-statements/administrative-sql-statements/show/show-plugins.md) should be used instead.
* Scope: Global
* Dynamic: No
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `have_profiling`

* Description: If statement profiling is available, will be set to `YES`, otherwise will be set to `NO`. See [SHOW PROFILES()](../../../reference/sql-statements/administrative-sql-statements/show/show-profiles.md) and [SHOW PROFILE()](../../../reference/sql-statements/administrative-sql-statements/show/show-profile.md).
* Scope: Global
* Dynamic: No

#### `have_query_cache`

* Description: If the server supports the [query cache](../buffers-caches-and-threads/query-cache.md), will be set to `YES`, otherwise will be set to `NO`.
* Scope: Global
* Dynamic: No

#### `have_rtree_keys`

* Description: If RTREE indexes (used for [spatial indexes](../../../reference/sql-structure/geometry/spatial-index.md)) are available, will be set to `YES`, otherwise will be set to `NO`.
* Scope: Global
* Dynamic: No

#### `have_symlink`

* Description: This system variable can be used to determine whether the server supports symbolic links (note that it has no meaning on Windows).
  * If symbolic links are supported, then the value will be `YES`.
  * If symbolic links are not supported, then the value will be `NO`.
  * If symbolic links are disabled with the [--symbolic-links](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-symbolic-links) option and the `skip` [option prefix](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#option-prefixes) (i.e. --skip-symbolic-links), then the value will be `DISABLED`.
  * Symbolic link support is required for the [INDEX DIRECTORY](../../../reference/sql-statements/data-definition/create/create-table.md#data-directoryindex-directory) and [DATA DIRECTORY](../../../reference/sql-statements/data-definition/create/create-table.md#data-directoryindex-directory) table options.
* Scope: Global
* Dynamic: No

#### `histogram_size`

* Description: Number of bytes used for a [histogram](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md), or, from [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107) when [histogram\_type](server-system-variables.md#histogram_type) is set to `JSON_HB`, number of buckets. If set to 0, no histograms are created by [ANALYZE](../../../reference/sql-statements/table-statements/analyze-table.md).
* Command line: `--histogram-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `254`
* Range: `0` to `255`

#### `histogram_type`

* Description: Specifies the type of [histograms](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md) created by [ANALYZE](../../../reference/sql-statements/table-statements/analyze-table.md)..
  * `SINGLE_PREC_HB` - single precision height-balanced.
  * `DOUBLE_PREC_HB` - double precision height-balanced.
  * `JSON_HB` - JSON height-balanced histograms (from [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108))
* Command line: `--histogram-type=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value:
  * `JSON_HB` (>= [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110))
  * `DOUBLE_PREC_HB` (<= [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), >= [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes))
* Valid Values:
  * `SINGLE_PREC_HB`, `DOUBLE_PREC_HB` (<= [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106))
  * `SINGLE_PREC_HB`, `DOUBLE_PREC_HB`, `JSON_HB` (>= [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108))

#### `host_cache_size`

* Description: Number of host names that will be cached to avoid resolving. Setting to `0` disables the cache. Changing the value while the server is running causes an implicit [FLUSH HOSTS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), clearing the host cache and truncating the [performance\_schema.host\_cache](../../../reference/system-tables/performance-schema/performance-schema-tables/performance-schema-host_cache-table.md) table. If you are connecting from a lot of different machines you should consider increasing. Some container configs explicitly set `host_cache_size` to `0`, rather than leave it as the default, `128`.
* Command line: `--host-cache-size=#`.
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `128`
* Range: `0` to `65536`

#### `hostname`

* Description: When the server starts, this variable is set to the server host name.
* Scope: Global
* Dynamic: No
* Data Type: `string`

#### `identity`

* Description: A synonym for [last\_insert\_id](server-system-variables.md#last_insert_id) variable.

#### `idle_readonly_transaction_timeout`

* Description: Time in seconds that the server waits for idle read-only transactions before killing the connection. If set to `0`, the default, connections are never killed. See also [idle\_transaction\_timeout](server-system-variables.md#idle_transaction_timeout), [idle\_write\_transaction\_timeout](server-system-variables.md#idle_write_transaction_timeout) and [Transaction Timeouts](../../../reference/sql-statements/transactions/transaction-timeouts.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `31536000`

#### `idle_transaction_timeout`

* Description: Time in seconds that the server waits for idle transactions before killing the connection. If set to `0`, the default, connections are never killed. See also [idle\_readonly\_transaction\_timeout](server-system-variables.md#idle_readonly_transaction_timeout), [idle\_write\_transaction\_timeout](server-system-variables.md#idle_write_transaction_timeout) and [Transaction Timeouts](../../../reference/sql-statements/transactions/transaction-timeouts.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `31536000`

#### `idle_write_transaction_timeout`

* Description: Time in seconds that the server waits for idle read-write transactions before killing the connection. If set to `0`, the default, connections are never killed. See also [idle\_transaction\_timeout](server-system-variables.md#idle_transaction_timeout), [idle\_readonly\_transaction\_timeout](server-system-variables.md#idle_readonly_transaction_timeout) and [Transaction Timeouts](../../../reference/sql-statements/transactions/transaction-timeouts.md). Called `idle_readwrite_transaction_timeout` until [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `31536000`

#### `ignore_db_dirs`

* Description: Tells the server that this directory can never be a database. That means two things - firstly it is ignored by the [SHOW DATABASES](../../../reference/sql-statements/administrative-sql-statements/show/show-databases.md) command and [INFORMATION\_SCHEMA](../../../reference/system-tables/information-schema/) tables. And secondly, USE, CREATE DATABASE and SELECT statements will return an error if the database from the ignored list specified. Use this option several times if you need to ignore more than one directory. To make the list empty set the void value to the option as --ignore-db-dir=. If the option or configuration is specified multiple times, viewing this value will list the ignore directories separated by commas.
* Command line: `--ignore-db-dirs=dir`.
* Scope: Global
* Dynamic: No
* Data Type: `string`

#### `in_predicate_conversion_threshold`

* Description: The minimum number of scalar elements in the value list of an IN predicate that triggers its conversion to an IN subquery. Set to 0 to disable the conversion. See [Conversion of Big IN Predicates Into Subqueries](../query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md).
* Command line: `--in-predicate-conversion-threshold=#`
* Scope: Global, Session
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1000`
* Range: `0` to `4294967295`

#### `in_transaction`

* Description: Session-only and read-only variable that is set to `1` if a transaction is in progress, `0` if not.
* Command line: No
* Scope: Session
* Dynamic: No
* Data Type: `boolean`
* Default Value: `0`

#### `init_connect`

* Description: String containing one or more SQL statements, separated by semicolons, that will be executed by the server for each client connecting. If there's a syntax error in the one of the statements, the client will fail to connect. For this reason, the statements are not executed for users with the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes), the [CONNECTION ADMIN](../../../reference/sql-statements/account-management-sql-statements/grant.md#connection-admin) privilege, who can then still connect and correct the error. See also [init\_file](server-system-variables.md#init_file).
* Command line: `--init-connect=name`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `init_file`

* Description: Name of a file containing SQL statements that will be executed by the server on startup. Each statement should be on a new line, and end with a semicolon. See also [init\_connect](server-system-variables.md#init_connect).
* Command line: `init-file=file_name`
* Scope: Global
* Dynamic: No
* Data Type: `file name`

#### `insert_id`

* Description: Value to be used for the next statement inserting a new [AUTO\_INCREMENT](../../../reference/data-types/auto_increment.md) value.
* Scope: Session
* Dynamic: Yes
* Data Type: `numeric`

#### `interactive_timeout`

* Description: Time in seconds that the server waits for an interactive connection (one that connects with the mysql\_real\_connect() CLIENT\_INTERACTIVE option) to become active before closing it. See also [wait\_timeout](server-system-variables.md#wait_timeout).
* Command line: `--interactive-timeout=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `28800`
* Range: (Windows): `1` to `2147483`
* Range: (Other): `1` to `31536000`

#### `join_buffer_size`

* Description: Minimum size in bytes of the buffer used for queries that cannot use an index, and instead perform a full table scan. Increase to get faster full joins when adding indexes is not possible, although be aware of memory issues, since joins will always allocate the minimum size. Best left low globally and set high in sessions that require large full joins. In 64-bit platforms, Windows truncates values above 4GB to 4GB with a warning.
* Command line: `--join-buffer-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `262144` (256kB)
* Range (non-Windows): `128` to `18446744073709547520`
* Range (Windows): `8228` to `18446744073709547520`

#### `join_buffer_space_limit`

* Description: Maximum size in bytes of the query buffer, By default 102&#x34;_&#x31;2&#x38;_&#x31;0.
* Command line: `--join-buffer-space-limit=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2097152`
* Range: `2048` to `18446744073709551615`

#### `join_cache_level`

* Description: Controls which of the eight block-based algorithms can be used for join operations.
  * 1 – flat (Block Nested Loop) BNL
  * 2 – incremental BNL
  * 3 – flat Block Nested Loop Hash (BNLH)
  * 4 – incremental BNLH
  * 5 – flat Batch Key Access (BKA)
  * 6 – incremental BKA
  * 7 – flat Batch Key Access Hash (BKAH)
  * 8 – incremental BKAH
* Command line: `--join-cache-level=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2`
* Range: `0` to `8`

#### `keep_files_on_create`

* Description: If a [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) table is created with no DATA DIRECTORY option, the .MYD file is stored in the database directory. When set to `0`, the default, if MariaDB finds another .MYD file in the database directory it will overwrite it. Setting this variable to `1` means that MariaDB will return an error instead, just as it usually does in the same situation outside of the database directory. The same applies for .MYI files and no INDEX DIRECTORY option. Deprecated in [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes).
* Command line: `--keep-files-on-create=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes)

#### `large_files_support`

* Description: ON if the server if was compiled with large file support or not, else OFF
* Scope: Global
* Dynamic: No

#### `large_page_size`

* Description: Indicates the size of memory page if large page support (Linux only) is enabled. The page size is determined from the Hugepagesize setting in `/proc/meminfo`. See [large\_pages](server-system-variables.md#large_pages). Deprecated and unused in [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1053-release-notes) since multiple page size support was added.
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: Autosized (see description)
* Deprecated: [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1053-release-notes)
* Removed: [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120)

#### `large_pages`

* Description: Indicates whether large page support (prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105), Linux only, by now supported Windows and BSD distros, also called huge pages) is used. This is set with `--large-pages` or disabled with `--skip-large-pages`. Large pages are used for the [innodb buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) and for online DDL (of size 3\* [innodb\_sort\_buffer\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_sort_buffer_size) (or 6 when encryption is used)). To use large pages, the Linux `sysctl` variable `kernel.shmmax` must be large than the llocation. Also the `sysctl` variable `vm.nr_hugepages` multipled by [large-page](server-system-variables.md#large_page_size)) must be larger than the usage. The ulimit for locked memory must be sufficient to cover the amount used (`ulimit -l` and equalivent in /etc/security/limits.conf / or in systemd [LimitMEMLOCK](../../../server-management/starting-and-stopping-mariadb/systemd.md)). If these operating system controls or insufficient free huge pages are available, the allocation of large pages will fall back to conventional memory allocation and a warning will appear in the logs. Only allocations of the default `Hugepagesize` currently occur (see `/proc/meminfo`).
* Command line: `--large-pages`, `--skip-large-pages`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `last_insert_id`

* Description: Contains the same value as that returned by [LAST\_INSERT\_ID()](../../../reference/sql-functions/secondary-functions/information-functions/last_insert_id.md). Note that setting this variable doen't update the value returned by the underlying function.
* Scope: Session
* Dynamic: Yes
* Data Type: `numeric`

#### `lc_messages`

* Description: This system variable can be specified as a [locale](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) name. The language of the associated [locale](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) will be used for error messages. See [Server Locales](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) for a list of supported locales and their associated languages.
  * This system variable is set to `en_US` by default, which means that error messages are in English by default.
  * If this system variable is set to a valid [locale](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) name, but the server can't find an [error message file](../../../server-management/server-monitoring-logs/error-log.md#error-messages-file) for the language associated with the [locale](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md), then the default language will be used instead.
  * This system variable is used along with the [lc\_messages\_dir](server-system-variables.md#lc_messages_dir) system variable to construct the path to the [error messages file](../../../server-management/server-monitoring-logs/error-log.md#error-messages-file).
  * See [Setting the Language for Error Messages](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/setting-the-language-for-error-messages.md) for more information.
* Command line: `--lc-messages=name`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `en_us`

#### `lc_messages_dir`

* Description: This system variable can be specified either as the path to the directory storing the server's [error message files](../../../server-management/server-monitoring-logs/error-log.md#error-messages-file) or as the path to the directory storing the specific language's [error message file](../../../server-management/server-monitoring-logs/error-log.md#error-messages-file). See [Server Locales](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) for a list of available locales and their related languages.
  * The server initially tries to interpret the value of this system variable as a path to the directory storing the server's [error message files](../../../server-management/server-monitoring-logs/error-log.md#error-messages-file). Therefore, it constructs the path to the language's [error message file](../../../server-management/server-monitoring-logs/error-log.md#error-messages-file) by concatenating the value of this system variable with the language name of the [locale](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) specified by the [lc\_messages](server-system-variables.md#lc_messages) system variable .
  * If the server does not find the [error message file](../../../server-management/server-monitoring-logs/error-log.md#error-messages-file) for the language, then it tries to interpret the value of this system variable as a direct path to the directory storing the specific language's [error message file](../../../server-management/server-monitoring-logs/error-log.md#error-messages-file).
  * See [Setting the Language for Error Messages](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/setting-the-language-for-error-messages.md) for more information.
* Command line: `--lc-messages-dir=path`
* Scope: Global
* Dynamic: No
* Data Type: `directory name`

#### `lc_time_names`

* Description: The locale that determines the language used for the date and time functions [DAYNAME()](../../../reference/sql-functions/date-time-functions/dayname.md), [MONTHNAME()](../../../reference/sql-functions/date-time-functions/monthname.md) and [DATE\_FORMAT()](https://mariadb.com/kb/en/date-format). Locale names are language and region subtags, for example 'en\_ZA' (English - South Africa) or 'es\_US: Spanish - United States'. The default is always 'en-US' regardless of the system's locale setting. See [server locale](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) for a full list of supported locales.
* Command line: `--lc-time-names=name`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `en_US`

#### `legacy_xa_rollback_at_disconnect`

* Description: If a user session disconnects after putting a transaction into the `XA PREPARE` state, roll back the transaction. Can be used for backwards compatibility to enable this pre-10.5 behavior for applications that expect it. Note that this violates the XA Specification and should not be used for new code.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Introduced: [MariaDB 10.5.27](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10-5-27-release-notes), [MariaDB 10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-20-release-notes), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-10-release-notes), [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-4-release-notes), [MariaDB 11.7.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes)

#### `license`

* Description: Server license, for example `GPL`.
* Scope: Global
* Dynamic: No
* Data Type: `string`

#### `local_infile`

* Description: If set to `1`, LOCAL is supported for [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statements. If set to `0`, usually for security reasons, attempts to perform a LOAD DATA LOCAL will fail with an error message.
* Command line: `--local-infile=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `lock_wait_timeout`

* Description: Timeout in seconds for attempts to acquire [metadata locks](../../../reference/sql-statements/transactions/metadata-locking.md). Statements using metadata locks include [FLUSH TABLES WITH READ LOCK](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), [LOCK TABLES](../../../reference/sql-statements/transactions/lock-tables.md), HANDLER and DML and DDL operations on tables, [stored procedures](../../../server-usage/stored-routines/stored-procedures/) and [functions](../../../server-usage/stored-routines/stored-functions/), and [views](../../../server-usage/views/). The timeout is separate for each attempt, of which there may be multiple in a single statement. `0` means no wait. See [WAIT and NOWAIT](../../../reference/sql-statements/transactions/wait-and-nowait.md).
* Command line: `--lock-wait-timeout=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `86400` (1 day)
* Range:
  * `0` to `31536000`

#### `locked_in_memory`

* Description: Indicates whether --memlock was used to lock mariadbd in memory.
* Command line: `--memlock`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `log`

* Description: Deprecated and removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), use [general\_log](server-system-variables.md#general_log) instead.
* Command line: `-l [filename]` or `--log[=filename]`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `OFF`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `log_disabled_statements`

* Description: If set, the specified type of statements (slave and/or stored procedure statements) will not be logged to the [general log](../../../server-management/server-monitoring-logs/general-query-log.md). Multiple values are comma-separated, without spaces.
* Command line: `--log-disabled_statements=value`
* Scope: Global, Session
* Dynamic: No
* Data Type: `set`
* Default Value: `sp`
* Valid Values: `slave` and/or `sp`, or empty string for none

#### `log_error`

* Description: Specifies the name of the [error log](../../../server-management/server-monitoring-logs/error-log.md). If [--console](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-console) is specified later in the configuration (Windows only) or this option isn't specified, errors will be logged to stderr. If no name is provided, errors will still be logged to `hostname.err` in the `datadir` directory by default. If a configuration file sets `--log-error`, one can reset it with `--skip-log-error` (useful to override a system wide configuration file). MariaDB always writes its error log, but the destination is configurable. See [error log](../../../server-management/server-monitoring-logs/error-log.md) for details. Note that if [--log-basename](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `log_error` should be placed after in the config files. Later settings override earlier settings, so `log-basename` will override any earlier log file name settings.
* Command line: `--log-error[=name]`, `--skip-log-error`
* Scope: Global
* Dynamic: No
* Data Type: `file name`
* Default Value: (empty string)

#### `log_output`

* Description: How the output for the [general query log](../../../server-management/server-monitoring-logs/general-query-log.md) and the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) is stored. By default written to file (`FILE`), it can also be stored in the [general\_log](../../../reference/system-tables/the-mysql-database-tables/mysqlgeneral_log-table.md) and [slow\_log](../../../reference/system-tables/the-mysql-database-tables/mysql-slow_log-table.md) tables in the mysql database (`TABLE`), or not stored at all (`NONE`). More than one option can be chosen at the same time, with `NONE` taking precedence if present. Logs will not be written if logging is not enabled. See [Writing logs into tables](../../../server-management/server-monitoring-logs/writing-logs-into-tables.md), and the [slow\_query\_log](server-system-variables.md#slow_query_log) and [general\_log](server-system-variables.md#general_log) server system variables.
* Command line: `--log-output=name`
* Scope: Global
* Dynamic: Yes
* Data Type: `set`
* Default Value: `FILE`
* Valid Values: `TABLE`, `FILE` or `NONE`

#### `log_queries_not_using_indexes`

* Description: Queries that don't use an index, or that perform a full index scan where the index doesn't limit the number of rows, will be logged to the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) (regardless of time taken). The slow query log needs to be enabled for this to have an effect. Mapped to `log_slow_filter='not_using_index'` from [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes).
* Command line: `--log-queries-not-using-indexes`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `log_slow_admin_statements`

* Description: Log slow [OPTIMIZE](../optimizing-tables/optimize-table.md), [ANALYZE](../../../reference/sql-statements/table-statements/analyze-table.md), [ALTER](../../../reference/sql-statements/data-definition/alter/) and other [administrative](../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md#logging-slow-administrative-statements) statements to the [slow log](../../../server-management/server-monitoring-logs/slow-query-log/) if it is open. See also [log\_slow\_disabled\_statements](server-system-variables.md#log_slow_disabled_statements) and [log\_slow\_filter](server-system-variables.md#log_slow_filter). Deprecated, use [log\_slow\_filter](server-system-variables.md#log_slow_filter) without `admin`.
* Command line: `--log-slow-admin-statements`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value:
  * `ON`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes)

#### `log_slow_disabled_statements`

* Description: If set, the specified type of statements will not be logged to the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/). See also [log\_slow\_admin\_statements](server-system-variables.md#log_slow_admin_statements) and [log\_slow\_filter](server-system-variables.md#log_slow_filter).
* Command line: `--log-slow-disabled_statements=value`
* Scope: Global, Session
* Dynamic: No
* Data Type: `set`
* Default Value: `sp`
* Valid Vales: `admin`, `call`, `slave` and/or `sp`

#### `log_slow_filter`

* Description: Comma-delimited string (without spaces) containing one or more settings for filtering what is logged to the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/). If a query matches one of the types listed in the filter, and takes longer than [long\_query\_time](server-system-variables.md#long_query_time), it will be logged(except for 'not\_using\_index' which is always logged if enabled, regardless of the time). Sets [log-slow-admin-statements](server-system-variables.md#log_slow_admin_statements) to ON. See also [log\_slow\_disabled\_statements](server-system-variables.md#log_slow_disabled_statements).
  * `admin` log [administrative](../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md#logging-slow-administrative-statements) queries (create, optimize, drop etc...)
  * `filesort` logs queries that use a filesort.
  * `filesort_on_disk` logs queries that perform a filesort on disk.
  * `filesort_priority_queue`
  * `full_join` logs queries that perform a join without indexes.
  * `full_scan` logs queries that perform full table scans.
  * `not_using_index` logs queries that don't use an index, or that perform a full index scan where the index doesn't limit the number of rows. Disregards [long\_query\_time](server-system-variables.md#long_query_time), unlike other options. [log\_queries\_not\_using\_indexes](server-system-variables.md#log_queries_not_using_indexes) maps to this option. From [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes).
  * `query_cache` log queries that are resolved by the query cache.
  * `query_cache_miss` logs queries that are not found in the [query cache](../buffers-caches-and-threads/query-cache.md).
  * `tmp_table` logs queries that create an implicit temporary table.
  * `tmp_table_on_disk` logs queries that create a temporary table on disk.
* Command line: `log-slow-filter=value1[,value2...]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value:
  * `admin`, `filesort`, `filesort_on_disk`, `filesort_priority_queue`, `full_join`, `full_scan`, `query_cache`, `query_cache_miss`, `tmp_table`, `tmp_table_on_disk`
* Valid Values:
  * `admin`, `filesort`, `filesort_on_disk`, `filesort_priority_queue`, `full_join`, `full_scan`, `not_using_index`, `query_cache`, `query_cache_miss`, `tmp_table`, `tmp_table_on_disk`

#### `log_slow_max_warnings`

* Description: Max numbers of warnings printed to slow query log per statement
* Command line: `log-slow-max-warnings=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10`
* Range: `0` to `1000`
* Introduced: [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes)

#### `log_slow_min_examined_row_limit`

* Description: Don't write queries to [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) that examine fewer rows than the set value. If set to `0`, the default, no row limit is used. `min_examined_row_limit` is an alias. From [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117), queries slower than [log\_slow\_always\_query\_time](../../../server-management/server-monitoring-logs/slow-query-log/log_slow_always_query_time-system-variable.md) will always be logged.
* Command line: `--log-slow-min-examined-row-limit=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0-4294967295`
* Introduced: [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011)

#### `log_slow_queries`

* Description: Deprecated and removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), use [slow\_query\_log](server-system-variables.md#slow_query_log) instead.
* Command line: `--log-slow-queries[=name]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `log_slow_query`

* Description: If set to 0, the default unless the --slow-query-log option is used, the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) is disabled, while if set to 1 (both global and session variables), the slow query log is enabled. Named [slow\_query\_log](server-system-variables.md#slow_query_log) before [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-0-release-notes), which is now an alias.
* Command line: `--slow-query-log`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`
* Introduced: [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-0-release-notes)
* See also: See [log\_output](server-system-variables.md#log_output) to see how log files are written. If that variable is set to `NONE`, no logs will be written even if log\_slow\_query is set to `1`.

#### `log_slow_query_file`

* Description: Name of the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) file. Before [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), was named [slow\_query\_log\_file](server-system-variables.md#slow_query_log_file). This was named `log_slow_query_file_name` in the [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-0-release-notes) preview release. If [--log-basename](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `log_slow_query_file` should be placed after in the config files. Later settings override earlier settings, so `log-basename` will override any earlier log file name settings.
* Command line: `--log-slow-query-file=file_name`
* Scope: Global
* Dynamic: Yes
* Data Type: `file name`
* Default Value: `host_name-slow.log`
* Introduced: [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-0-release-notes)

#### `log_slow_query_time`

* Description: If a query takes longer than this many seconds to execute (microseconds can be specified too), the [Slow\_queries](server-status-variables.md#slow_queries) status variable is incremented and, if enabled, the query is logged to the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/). Before [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), was named [long\_query\_time](server-system-variables.md#long_query_time). Affected by [log\_slow\_rate\_limit](server-system-variables.md#log_slow_rate_limit) and [log\_slow\_min\_examined\_row\_limit](server-system-variables.md#log_slow_min_examined_row_limit).
* Command line: `--log-slow-query-time=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10.000000`
* Range: `0` to `31536000`
* Introduced: [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-0-release-notes)

#### `log_slow_rate_limit`

* Description: The [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) will log every this many queries. The default is `1`, or every query, while setting it to `20` would log every 20 queries, or five percent. Aims to reduce I/O usage and excessively large slow query logs. See also [Slow Query Log Extended Statistics](../query-optimizations/statistics-for-optimizing-queries/slow-query-log-extended-statistics.md). From [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117), queries slower than [log\_slow\_always\_query\_time](../../../server-management/server-monitoring-logs/slow-query-log/log_slow_always_query_time-system-variable.md) will always be logged.
* Command line: `log-slow-rate-limit=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` upwards

#### `log_slow_verbosity`

* Description: Controls information to be added to the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/). Options are added in a comma-delimited string. See also [Slow Query Log Extended Statistics](../query-optimizations/statistics-for-optimizing-queries/slow-query-log-extended-statistics.md). log\_slow\_verbosity is not supported when log\_output='TABLE'.
  * `query_plan` logs query execution plan information
  * `innodb` Alias to `engine` (from [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-15-release-notes) and [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-5-release-notes)), previously ignored.
  * `explain` prints EXPLAIN output in the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/). See [EXPLAIN in the Slow Query Log](../../../server-management/server-monitoring-logs/slow-query-log/explain-in-the-slow-query-log.md).
  * `engine` Logs engine statistics (from [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-15-release-notes) and [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-5-release-notes)).
  * `warnings` Print all errors, warnings and notes for the statement to the slow query log. (from [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes)).
  * `all` Enables all above options (From [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes))
  * `full` Enables all above options.
* Command line: `log-slow-verbosity=value1[,value2...]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: (Empty)
* Valid Values:
  * > \= [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-6-release-notes): (Empty), `query_plan`, `innodb`, `explain`, `engine`, `warnings`, `all`, `full`
  * > \= [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-15-release-notes), [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-5-release-notes): (Empty), `query_plan`, `innodb`, `explain`, `engine`, `full`
  * <= [MariaDB 10.6.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-14-release-notes), [MariaDB 10.11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-4-release-notes): (Empty), `query_plan`, `innodb`, `explain`

#### `log_tc_size`

* Description: Defines the size in bytes of the memory-mapped file-based transaction coordinator log, which is only used if the [binary log](../../../server-management/server-monitoring-logs/binary-log/) is disabled. If you have two or more XA-capable storage engines enabled, then a transaction coordinator log must be available. This size is defined in multiples of 4096. See [Transaction Coordinator Log](../../../server-management/server-monitoring-logs/transaction-coordinator-log/) for more information. Also see the [--log-tc](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-tc) server option and the [--tc-heuristic-recover](server-system-variables.md#-tc-heuristic-recover) option.
* Command line: `log-tc-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `24576`
* Range: `12288` to `18446744073709551615`

#### `log_warnings`

* Description: Determines which additional warnings are logged. Setting to `0` disables additional warning logging. Note that this does not prevent all warnings, there is a core set of warnings that will always be written to the error log. The additional warnings are as follows:
  * log\_warnings >= 1
    * [Event scheduler](../../../server-usage/triggers-events/event-scheduler/) information.
    * System signals.
    * Wrong usage of `--user`.
    * Failed setrlimit() and mlockall().
    * Changed limits.
    * Wrong values of lower\_case\_table\_names and stack\_size.
    * Wrong values for command line options.
    * Start log position and some master information when starting slaves.
    * Slave reconnects.
    * Killed slaves.
    * Error reading relay logs.
    * [Unsafe statements for statement-based replication](../../standard-replication/unsafe-statements-for-statement-based-replication.md). If this warning occurs frequently, it is throttled to prevent flooding the log.
    * Disabled [plugins](../../../reference/plugins/) that one tried to enable or use.
    * UDF files that didn't include the required init functions.
    * DNS lookup failures.
  * log\_warnings >= 2
    * Access denied errors.
    * Connections aborted or closed due to errors or timeouts.
    * Table handler errors.
    * Messages related to the files used to [persist replication state](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#option-persistence):
      * Either the default `master.info` file or the file that is configured by the [master\_info\_file](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#master-info-file) option.
      * Either the default `relay-log.info` file or the file that is configured by the [relay\_log\_info\_file](../../standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file) system variable.
    * Information about a master's [binary log dump thread](../../standard-replication/replication-threads.md#binary-log-dump-thread).
  * log\_warnings >= 3
    * All errors and warnings during [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) repair and auto recover.
    * Information about old-style language options.
    * Information about [progress of InnoDB online DDL](../../../server-usage/storage-engines/innodb/innodb-online-ddl/).
  * log\_warnings >=4
    * Connections aborted due to "Too many connections" errors.
    * Connections closed normally without authentication.
    * Connections aborted due to [KILL](../../../reference/sql-statements/administrative-sql-statements/kill.md).
    * Connections closed due to released connections, such as when [completion\_type](server-system-variables.md#completion_type) is set to `RELEASE`.
    * Could not read packet: (a lot more information)
    * All read/write errors for a connection are logged to the error log.
  * log\_warnings >=9
    * Information about initializing plugins.
* Command line: `-W [level]` or `--log-warnings[=level]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2`
* Range: `0` to `4294967295`

#### `long_query_time`

* Description: If a query takes longer than this many seconds to execute (microseconds can be specified too), the [Slow\_queries](server-status-variables.md#slow_queries) status variable is incremented and, if enabled, the query is logged to the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/). From [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-0-release-notes), this is an alias for [log\_slow\_query\_time](server-system-variables.md#log_slow_query_time).
* Command line: `--long-query-time=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10.000000`
* Range: `0` upwards

#### `low_priority_updates`

* Description: If set to 1 (0 is the default), for [storage engines](../../../server-usage/storage-engines/) that use only table-level locking ([Aria](../../../server-usage/storage-engines/aria/), [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/), [MEMORY](../../../server-usage/storage-engines/memory-storage-engine.md) and [MERGE](../../../server-usage/storage-engines/merge.md)), all INSERTs, UPDATEs, DELETEs and LOCK TABLE WRITEs will wait until there are no more SELECTs or LOCK TABLE READs pending on the relevant tables. Set this to 1 if reads are prioritized over writes.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) and earlier, [sql\_low\_priority\_updates](server-system-variables.md#sql_low_priority_updates) is a synonym.
* Command line: `--low-priority-updates`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`

#### `lower_case_file_system`

* Description: Read-only variable describing whether the file system is case-sensitive. If set to `OFF`, file names are case-sensitive. If set to `ON`, they are not case-sensitive.
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `##`

#### `lower_case_table_names`

* Description: If set to `0` (the default on Unix-based systems), table names and aliases and database names are compared in a case-sensitive manner. If set to `1` (the default on Windows), names are stored in lowercase and not compared in a case-sensitive manner. If set to `2` (the default on Mac OS X), names are stored as declared, but compared in lowercase.\
  This system variable's value cannot be changed after the datadir has been initialized. lower\_case\_table\_names is set when a MariaDB instance starts, and it remains constant afterwards.
* Command line: `--lower-case-table-names[=#]`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0` (Unix), `1` (Windows), `2` (Mac OS X)
* Range: `0` to `2`

#### `max_allowed_packet`

* Description: Maximum size in bytes of a packet or a generated/intermediate string. The packet message buffer is initialized with the value from [net\_buffer\_length](server-system-variables.md#net_buffer_length), but can grow up to max\_allowed\_packet bytes. Set as large as the largest BLOB, in multiples of 1024. If this value is changed, it should be changed on the client side as well. See [slave\_max\_allowed\_packet](../../standard-replication/replication-and-binary-log-system-variables.md) for a specific limit for replication purposes.
* Command line: `--max-allowed-packet=#`
* Scope: Global, Session
* Dynamic: Yes (Global), No (Session)
* Data Type: `numeric`
* Default Value:
  * `16777216` (16M)
  * `1073741824` (1GB) (client-side)
* Range: `1024` to `1073741824`

#### `max_connect_errors`

* Description: Limit to the number of successive failed connects from a host before the host is blocked from making further connections. The count for a host is reset to zero if they successfully connect. To unblock, flush the host cache with a [FLUSH HOSTS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) statement or [mariadb-admin flush-hosts](../../../clients-and-utilities/administrative-tools/mariadb-admin.md). The [performance\_schema.host\_cache](../../../reference/system-tables/performance-schema/performance-schema-tables/performance-schema-host_cache-table.md) table contains the status of the current hosts.
* Command line: `--max-connect-errors=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `1` to `4294967295`

#### `max_connections`

* Description: The maximum number of simultaneous client connections. See also [Handling Too Many Connections](handling-too-many-connections.md). Note that this value affects the number of file descriptors required on the operating system. Minimum was changed from `1` to `10` to avoid possible unexpected results for the user ([MDEV-18252](https://jira.mariadb.org/browse/MDEV-18252)). Note that MariaDB always has one reserved connection for a `SUPER` (or `CONNECTION ADMIN` user). Additionally it can listen on a separate port, so will be available even when the max\_connections limit is reached.
* Command line: `--max-connections=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `151`
* Range: `10` to `100000`

{% hint style="info" %}
**Systemd thread limit (MDEV-30236)**\
When running MariaDB under systemd, be aware that systemd's default `TasksMax` (≈ 4,915 tasks per service) may prevent reaching high `max_connections` values—even if configured higher. Starting with MariaDB 10.4.33, the systemd unit includes:

```ini
[Service]
TasksMax=infinity
```

This setting removes the artificial cap, allowing `max_connections` to scale per your configuration (subject to OS memory and thread limits).
{% endhint %}

#### `max_delayed_threads`

* Description: Limits to the number of [INSERT DELAYED](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) threads. Once this limit is reached, the insert is handled as if there was no DELAYED attribute. If set to `0`, DELAYED is ignored entirely. The session value can only be set to `0` or to the same as the global value.
* Command line: `--max-delayed-threads=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `20`
* Range: `0` to `16384`

#### `max_digest_length`

* Description: Maximum length considered for computing a statement digest, such as used by the [Performance Schema](../../../reference/system-tables/performance-schema/) and query rewrite plugins. Statements that differ after this many bytes produce the same digest, and are aggregated for statistics purposes. The variable is allocated per session. Increasing will allow longer statements to be distinguished from each other, but increase memory use, while decreasing will reduce memory use, but more statements may become indistinguishable.
* Command line: `--max-digest-length=#`
* Scope: Global,
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1024`
* Range: `0` to `1048576`

#### `max_error_count`

* Description: Specifies the maximum number of messages stored for display by [SHOW ERRORS](../../../reference/sql-statements/administrative-sql-statements/show/show-errors.md) and [SHOW WARNINGS](../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md) statements.
* Command line: `--max-error-count=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `64`
* Range: `0` to `65535`

#### `max_heap_table_size`

* Description: Maximum size in bytes for user-created [MEMORY](../../../server-usage/storage-engines/memory-storage-engine.md) tables. Setting the variable while the server is active has no effect on existing tables unless they are recreated or altered. The smaller of max\_heap\_table\_size and [tmp\_table\_size](server-system-variables.md#tmp_table_size) also limits internal in-memory tables. When the maximum size is reached, any further attempts to insert data will receive a "table ... is full" error. Temporary tables created with [CREATE TEMPORARY](../../../reference/sql-statements/data-definition/create/create-table.md) will not be converted to Aria, as occurs with internal temporary tables, but will also receive a table full error.
* Command line: `--max-heap-table-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `16777216`
* Range : `16384` to `4294966272`

#### `max_insert_delayed_threads`

* Description: Synonym for [max\_delayed\_threads](server-system-variables.md#max_delayed_threads).

#### `max_join_size`

* Description: Statements will not be performed if they are likely to need to examine more than this number of rows, row combinations or do more disk seeks. Can prevent poorly-formatted queries from taking server resources. Changing this value to anything other the default will reset [sql\_big\_selects](server-system-variables.md#sql_big_selects) to 0. If sql\_big\_selects is set again, max\_join\_size will be ignored. This limit is also ignored if the query result is sitting in the [query cache](../buffers-caches-and-threads/query-cache.md). Previously named [sql\_max\_join\_size](server-system-variables.md#sql_max_join_size), which is still a synonym.
* Command line: `--max-join-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `18446744073709551615`
* Range: `1` to `18446744073709551615`

#### `max_length_for_sort_data`

* Description: Used to decide which algorithm to choose when sorting rows. If the total size of the column data, not including columns that are part of the sort, is less than `max_length_for_sort_data`, then we add these to the sort key. This can speed up the sort as we don't have to re-read the same row again later. Setting the value too high can slow things down as there will be a higher disk activity for doing the sort.
* Command line: `--max-length-for-sort-data=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1024`
* Range: `4` to `8388608`

#### `max_long_data_size`

* Description: Maximum size for parameter values sent with mysql\_stmt\_send\_long\_data(). If not set, will default to the value of [max\_allowed\_packet](server-system-variables.md#max_allowed_packet). Deprecated in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) and removed in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes); use [max\_allowed\_packet](server-system-variables.md#max_allowed_packet) instead.
* Command line: `--max-long-data-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `16777216` (16M)
* Range: `1024` to `4294967295`
* Deprecated: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes)

#### `max_open_cursors`

* Description: The maximum number of open [cursors](../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors/) allowed per session.
* Command line: `--max-open-cursors=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `50`
* Range: `0` to 65536
* Introduced: [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120)

#### `max_password_errors`

* Description: The maximum permitted number of failed connection attempts due to an invalid password before a user is blocked from further connections. [FLUSH\_PRIVILEGES](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) will permit the user to connect again. This limit is not applicable for users with the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes), the [CONNECTION ADMIN](../../../reference/sql-statements/account-management-sql-statements/grant.md#connection-admin) privilege, with a hostname of localhost, 127.0.0.1 or ::1. See also the [Information Schema USERS table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-users-table.md).
* Command line: `--max-password-errors=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4294967295`
* Range: `1` to `4294967295`

#### `max_prepared_stmt_count`

* Description: Maximum number of prepared statements on the server. Can help prevent certain forms of denial-of-service attacks. If set to `0`, no prepared statements are permitted on the server.
* Command line: `--max-prepared-stmt-count=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `16382`
* Range: `0` to `4294967295`

#### `max_recursive_iterations`

* Description: Maximum number of iterations when executing recursive queries, used to prevent infinite loops in [recursive CTEs](../../../reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/recursive-common-table-expressions-overview.md).
* Command line: `--max-recursive-iterations=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1000` (>= [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes)), `4294967295` (<= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105))
* Range: `0` to `4294967295`

#### `max_rowid_filter_size`

* Description: The maximum size of the container of a rowid filter.
* Command line: `--max-rowid-filter-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `131072`
* Range: `1024` to `18446744073709551615`

#### `max_seeks_for_key`

* Description: The optimizer assumes that the number specified here is the most key seeks required when searching with an index, regardless of the actual index cardinality. If this value is set lower than its default and maximum, indexes will tend to be preferred over table scans.
* Command line: `--max-seeks-for-key=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4294967295`
* Range: `1` to `4294967295`

#### `max_session_mem_used`

* Description: Amount of memory a single user session is allowed to allocate. This limits the value of the session variable [Memory\_used](server-status-variables.md#memory_used).
* Command line: `--max-session-mem-used=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `9223372036854775807` (8192 PB)
* Range: `8192` to `18446744073709551615`

#### `max_sort_length`

* Description: Maximum size in bytes used for sorting data values - anything exceeding this is ignored. The server uses only the first `max_sort_length` bytes of each value and ignores the rest. Increasing this may require [sort\_buffer\_size](server-system-variables.md#sort_buffer_size) to be increased (especially if ER\_OUT\_OF\_SORTMEMORY errors start appearing). From [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117), a warning is generated when max\_sort\_length is exceeded.
* Command line: `--max-sort-length=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1024`
* Range:
  * `4` to `8388608` (<= [MariaDB 10.4.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10413-release-notes), [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1053-release-notes))
  * `8` to `8388608` (>= [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes), [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes))

#### `max_sp_recursion_depth`

* Description: Permitted number of recursive calls for a [stored procedure](../../../server-usage/stored-routines/stored-procedures/). `0`, the default, no recursion is permitted. Increasing this value increases the thread stack requirements, so you may need to increase [thread\_stack](server-system-variables.md#thread_stack) as well. This limit doesn't apply to [stored functions](../../../server-usage/stored-routines/stored-functions/).
* Command line: `--max-sp-recursion-depth[=#]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `255`

#### `max_statement_time`

* Description: Maximum time in seconds that a query can execute before being aborted. This includes all queries, not just [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statements, but excludes statements in stored procedures. If set to 0, no limit is applied. See [Aborting statements that take longer than a certain time to execute](../query-optimizations/aborting-statements.md) for details and limitations. Useful when combined with [SET STATEMENT](../../../reference/sql-statements/administrative-sql-statements/set-commands/set-statement.md) for limiting the execution times of individual queries. Replicas are not affected by this variable, however, from [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010), there's [slave\_max\_statement\_time](../../standard-replication/replication-and-binary-log-system-variables.md#slave_max_statement_time) that sets the limit to abort queries on a replica.
* Command line: `--max-statement-time[=#]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0.000000`
* Range: `0` to `31536000`

#### `max_tmp_tables`

* Description: Unused.
* Removed: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `max_user_connections`

* Description:\
  Maximum simultaneous connections permitted for each user account. When set to `0`, there is no per user limit. Setting it to `-1` stops users without the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes), the [CONNECTION ADMIN](../../../reference/sql-statements/account-management-sql-statements/grant.md#connection-admin) privilege, from connecting to the server. The session variable is always read-only and only privileged users can modify user limits. The session variable defaults to the global `max_user_connections` variable, unless the user's specific [MAX\_USER\_CONNECTIONS](../../../reference/sql-statements/account-management-sql-statements/create-user.md#resource-limit-options) resource option is non-zero. When both global variable and the user resource option are set, the user's [MAX\_USER\_CONNECTIONS](../../../reference/sql-statements/account-management-sql-statements/create-user.md#max_user_connections) is used. Note: This variable does not affect users with the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes), the [CONNECTION ADMIN](../../../reference/sql-statements/account-management-sql-statements/grant.md#connection-admin) privilege.
* Command line: `--max-user-connections=#`
* Scope: Global, Session
* Dynamic: Yes, (except when globally set to `0` or `-1`)
* Data Type: `numeric`
* Default Value: `0`
* Range: `-1` to `4294967295`

#### `max_write_lock_count`

* Description: Read lock requests will be permitted for processing after this many write locks. Applies only to storage engines that use table level locks (thr\_lock), so no effect with [InnoDB](../../../server-usage/storage-engines/innodb/) or [Archive](../../../server-usage/storage-engines/archive.md).
* Command line: `--max-write-lock-count=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `4294967295`
* Range: `1` to `4294967295`

#### `metadata_locks_cache_size`

* Description: Unused since 10.1.4
* Command line: `--metadata-locks-cache-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1024`
* Range: `1` to `1048576`

#### `metadata_locks_hash_instances`

* Description: Unused since 10.1.4
* Command line: `--metadata-locks-hash-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8`
* Range: `1` to `1024`

#### `metadata_locks_instances`

* Description: Number of fast lanes to create for metadata locks. Can be used to improve DML scalability by eliminating MDL\_lock::rwlock load. Use 1 to disable MDL fast lanes. Supported MDL namespaces: BACKUP.
* Command line: `--metadata-locks-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8`
* Range: `1` to `256`
* Introduced: [MariaDB 12.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1)

#### `min_examined_row_limit`

* Description: Don't write queries to [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) that examine fewer rows than the set value. If set to `0`, the default, no row limit is used. From [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-0-release-notes), this is an alias for [log\_slow\_min\_examined\_row\_limit](server-system-variables.md#log_slow_min_examined_row_limit).
* Command line: `--min-examined-row-limit=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0-4294967295`

#### `mrr_buffer_size`

* Description: Size of buffer to use when using multi-range read with range access. See [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md#range-access) for more information.
* Command line: `--mrr-buffer-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `262144`
* Range `8192` to `2147483647`

#### `multi_range_count`

* Description: Ignored. Use [mrr\_buffer\_size](server-system-variables.md#mrr_buffer_size) instead.
* Command line: `--multi-range-count=#`
* Default Value: `256`
* Removed: [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes)

#### `mysql56_temporal_format`

* Description: If set (the default), MariaDB uses the MySQL 5.6 low level formats for [TIME](../../../reference/data-types/date-and-time-data-types/time.md), [DATETIME](../../../reference/data-types/date-and-time-data-types/datetime.md) and [TIMESTAMP](../../../reference/data-types/date-and-time-data-types/timestamp.md) instead of the [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) version. The version MySQL introduced in 5.6 requires more storage, but potentially allows negative dates and has some advantages in replication. There should be no reason to revert to the old [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) microsecond format. See also [MDEV-10723](https://jira.mariadb.org/browse/MDEV-10723).
* Command line: `--mysql56-temporal-format`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `named_pipe`

* Description: On Windows systems, determines whether connections over named pipes are permitted.
* Command line: `--named-pipe`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `net_buffer_length`

* Description: The starting size, in bytes, for the connection and thread buffers for each client thread. The size can grow to [max\_allowed\_packet](server-system-variables.md#max_allowed_packet). This variable's session value is read-only. Can be set to the expected length of client statements if memory is a limitation.
* Command line: `--net-buffer-length=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `16384`
* Range: `1024` to `1048576`

#### `net_read_timeout`

* Description: Time in seconds the server will wait for a client connection to send more data before aborting the read. See also [net\_write\_timeout](server-system-variables.md#net_write_timeout) and [slave\_net\_timeout](../../standard-replication/replication-and-binary-log-system-variables.md)
* Command line: `--net-read-timeout=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `30`
* Range: `1` to `31536000`

#### `net_retry_count`

* Description: Permit this many retries before aborting when attempting to read or write on a communication port. On FreeBSD systems should be set higher as threads are sent internal interrupts..
* Command line: `--net-retry-count=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10`
* Range: `1` to `4294967295`

#### `net_write_timeout`

* Description: Time in seconds to wait on writing a block to a connection before aborting the write. See also [net\_read\_timeout](server-system-variables.md#net_read_timeout) and [slave\_net\_timeout](../../standard-replication/replication-and-binary-log-system-variables.md).
* Command line: `--net-write-timeout=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `60`
* Range: `1` upwards

#### `new_mode`

* Description: Used to enable new behavior in otherwise stable versions. See [NEW Mode](../../../server-management/variables-and-modes/new-mode.md).  Non-default NEW\_MODE options are by design deprecated and will eventually be removed.
* Command line: `--new-mode`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `(empty string)`
* Valid Values: See [NEW Mode](../../../server-management/variables-and-modes/new-mode.md) for the full list.


#### `note_verbosity`

* Description: Verbosity level for note-warnings given to the user. Options are added in a comma-delimited string, except for `all`, which sets all options. Be aware that if the old [sql\_notes](server-system-variables.md#sql_notes) variable is 0, one will not get any notes. Setting `note_verbosity` to "" is the recommended way to disable notes.
  * `basic` All old notes.
  * `unusable_keys` Give warnings for unusable keys for SELECT, DELETE and UPDATE.
  * `explain` Give warnings for unusable keys for EXPLAIN.
  * `all` Enables all above options. This has to be given alone.
* Command line: `note-verbosity=value1[,value2...]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `basic,explain`
* Valid Values: `basic,explain,unusable_keys` or `all`.
* Introduced: [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes)

#### `old`

* Description: Disabled by default, enabling it reverts index hints to those used before MySQL 5.1.17. Enabling may lead to replication errors. Deprecated and replaced by [old\_mode](server-system-variables.md#old_mode) from [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109).
* Command line: `--old`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109)

#### `old_alter_table`

* Description: From [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes), an alias for [alter\_algorithm](server-system-variables.md#alter_algorithm). Prior to that, if set to `1` (`0` is default), MariaDB reverts to the non-optimized, pre-MySQL 5.1, method of processing [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) statements. A temporary table is created, the data is copied over, and then the temporary table is renamed to the original.
* Command line: `--old-alter-table`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumerated` (>=[MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes))
* Default Value: See [alter\_algorithm](server-system-variables.md#alter_algorithm)
* Valid Values: See [alter\_algorithm](server-system-variables.md#alter_algorithm) for the full list.
* Deprecated: [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes) (superceded by [alter\_algorithm](server-system-variables.md#alter_algorithm))
* Removed: [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes)

#### `old_mode`

* Description: Used for getting MariaDB to emulate behavior from an old version of MySQL or MariaDB. See [OLD Mode](../../../server-management/variables-and-modes/old-mode.md). Fully replaces the [old](server-system-variables.md#old) variable from [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109). Non-default OLD\_MODE options are by design deprecated and will eventually be removed.
* Command line: `--old-mode`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `UTF8_IS_UTF8MB3` (>= [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106)) `(empty string)` (<= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105))
* Valid Values: See [OLD Mode](../../../server-management/variables-and-modes/old-mode.md) for the full list.

#### `old_passwords`

* Description: If set to `1` (`0` is default), MariaDB reverts to using the [mysql\_old\_password](../../../reference/plugins/authentication-plugins/authentication-plugin-mysql_old_password.md) authentication plugin by default for newly created users and passwords, instead of the [mysql\_native\_password](../../../reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) authentication plugin.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `open_files_limit`

* Description: The number of file descriptors available to MariaDB. If you are getting the `Too many open files` error, then you should increase this limit. If set to 0, then MariaDB will calculate a limit based on the following:

MAX([max\_connections](server-system-variables.md#max_connections)\*5, [max\_connections](server-system-variables.md#max_connections) +[table\_open\_cache](server-system-variables.md#table_open_cache)\*2)

MariaDB sets the limit with [setrlimit](https://linux.die.net/man/2/setrlimit). MariaDB cannot set this to exceed the hard limit imposed by the operating system. Therefore, you may also need to change the hard limit. There are a few ways to do so.

* If you are using [mariadbd\_safe](../../../server-management/starting-and-stopping-mariadb/mariadbd-safe.md) to start `mariadbd`, then see the instructions at [mariadbd\_safe: Configuring the Open Files Limit](../../../server-management/starting-and-stopping-mariadb/mariadbd-safe.md#configuring-the-open-files-limit).
* If you are using [systemd](../../../server-management/starting-and-stopping-mariadb/systemd.md) to start `mariadbd`, then see the instructions at [systemd: Configuring the Open Files Limit](../../../server-management/starting-and-stopping-mariadb/systemd.md#configuring-the-open-files-limit).
* Otherwise, you can change the hard limit for the `mysql` user account by modifying [/etc/security/limits.conf](https://linux.die.net/man/5/limits.conf). See [Configuring Linux for MariaDB: Configuring the Open Files Limit](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/configuring-linux-for-mariadb.md#configuring-the-open-files-limit) for more details.
* Command line: `--open-files-limit=count`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: Autosized (see description)
* Range: `0` to `4294967295`

#### `optimizer_extra_pruning_depth`

* Description:If the optimizer needs to enumerate a join prefix of this size or larger, then it will try aggressively prune away the search space.
* Command line: `--optimizer-extra-pruning-depth[=#]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `8`
* Range: `0` to `62`
* Introduced: [MariaDB 10.10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/mariadb-10101-release-notes)

**optimizer\_join\_limit\_pref\_ratio**

* Description:Controls the [optimizer\_join\_limit\_pref\_ratio optimization](../query-optimizations/optimizer_join_limit_pref_ratio-optimization.md).
* Command line: `--optimizer-join-limit-pref-ratio[=#]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0` (Disable)
* Range: `0` to `4294967295`
* Introduced: [MariaDB 10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-20-release-notes), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-10-release-notes), [MariaDB 11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes), [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-4-release-notes), [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes)

#### `optimizer_max_sel_arg_weight`

* Description: This is an actively enforced maximum effective SEL\_ARG tree weight limit. A SEL\_ARG weight is the number of effective "ranges" hanging off this root (that is, merged tree elements are "unmerged" to count the weight). During range analysis, looking for possible index merges, SEL\_ARG graphs related to key ranges in query conditions are being processed. Graphs exceeding this limit will stop keys being 'and'ed and 'or'ed together to form a new larger SEL\_ARG graph. After each 'and' or 'or' process, this maximum weight limit is enforced. It enforces this limit by pruning the key part being used. This key part pruning can be used to limit/disable index merge SEL\_ARG graph construction on overly long query conditions.
* Command line: `--optimizer-max-sel-arg-weight=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `32000`
* Range: `0` to `18446744073709551615`
* Introduced: [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1059-release-notes)

#### `optimizer_max_sel_args`

* Description: The maximum number of SEL\_ARG objects created when optimizing a range. If more objects would be needed, range scans will not be used by the optimizer.
* Command line: `--optimizer-max-sel-args=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `16000`
* Range: `0` to `4294967295`
* Introduced: [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes)

#### `optimizer_prune_level`

* Description:Controls the heuristic(s) applied during query optimization to prune less-promising partial plans from the optimizer search space.
  * `0`: heuristics are disabled and an exhaustive search is performed
  * `1`: the optimizer will use heuristics to prune less-promising partial plans from the optimizer search space
  * `2`: tables using EQ\_REF will be joined together as 'one entity' and the different combinations of these tables will not be considered (from [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010))
* Command line: `--optimizer-prune-level[=#]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2` (>= [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)), `1` (<= [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109))

#### `optimizer_search_depth`

* Description: Maximum search depth by the query optimizer. Smaller values lead to less time spent on execution plans, but potentially less optimal results. If set to `0`, MariaDB will automatically choose a reasonable value. Since the better results from more optimal planning usually offset the longer time spent on planning, this is set as high as possible by default. `63` is a valid value, but its effects (switching to the original find\_best search) are deprecated.
* Command line: `--optimizer-search-depth[=#]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `62`
* Range: `0` to `63`

#### `optimizer_selectivity_sampling_limit`

* Description: Controls number of record samples to check condition selectivity. Only used if `[optimizer_use_condition_selectivity](server-system-variables.md#optimizer_use_condition_selectivity) > 4.`
* Command line: `optimizer-selectivity-sampling-limit[=#]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `10` upwards

#### `optimizer_switch`

* Description: A series of flags for controlling the query optimizer. See [Optimizer Switch](../query-optimizations/optimizer-switch.md) for defaults, and a comparison to MySQL.
* Command line: `--optimizer-switch=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Valid Values:
  * `condition_pushdown_for_derived={on|off}`
  * `condition_pushdown_for_subquery={on|off}`
  * `condition_pushdown_from_having={on|off}`
  * `cset_narrowing={on|off}` - see [Charset Narrowing Optimization](../query-optimizations/charset-narrowing-optimization.md) (>= [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes) and [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes))
  * `default` - set all optimizations to their default values.
  * `derived_merge={on|off}` - see [Derived table merge optimization](../query-optimizations/optimizations-for-derived-tables/derived-table-merge-optimization.md)
  * `derived_with_keys={on|off}` - see [Derived table with key optimization](../query-optimizations/optimizations-for-derived-tables/derived-table-with-key-optimization.md)
  * `duplicateweedout={on|off}`. From [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120).
  * `engine_condition_pushdown={on|off}`. Deprecated in [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes) as engine condition pushdown is now automatically enabled for all engines that support it.
  * `exists_to_in={on|off}` - see [EXISTS-to-IN optimization](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/extended-keys)
  * `extended_keys={on|off}` - see [Extended Keys](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/extended-keys)
  * `firstmatch={on|off}` - see [First Match Strategy](../query-optimizations/optimization-strategies/firstmatch-strategy.md)
  * `hash_join_cardinality={on|off}` - see [hash\_join\_cardinality-optimizer\_switch-flag](../query-optimizations/hash_join_cardinality-optimizer_switch-flag.md) (>= [MariaDB 11.0.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-2-release-notes), [MariaDB 10.11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-3-release-notes), [MariaDB 10.6.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-13-release-notes))
  * `index_condition_pushdown={on|off}` - see [Index Condition Pushdown](../query-optimizations/index-condition-pushdown.md)
  * `index_merge={on|off}`
  * `index_merge_intersection={on|off}`
  * `index_merge_sort_intersection={on|off}` - [more details](../query-optimizations/index_merge-sort_intersection.md)
  * `index_merge_sort_union={on|off}`
  * `index_merge_union={on|off}`
  * `in_to_exists={on|off}` - see [IN-TO-EXISTS transformation](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md#the-in-to-exists-transformation)
  * `join_cache_bka={on|off}` - see [Block-Based Join Algorithms](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms)
  * `join_cache_hashed={on|off}` - see [Block-Based Join Algorithms](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms)
  * `join_cache_incremental={on|off}` - see [Block-Based Join Algorithms](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms)
  * `loosescan={on|off}` - see [LooseScan strategy](../query-optimizations/optimization-strategies/loosescan-strategy.md)
  * `materialization={on|off}` - [Semi-join](../query-optimizations/optimization-strategies/semi-join-materialization-strategy.md) and [non semi-join](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md#materialization-for-non-correlated-in-subqueries) materialization.
  * `mrr={on|off}` - see [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md)
  * `mrr_cost_based={on|off}` - see [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md)
  * `mrr_sort_keys={on|off}` - see [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md)
  * `not_null_range_scan={on|off}` - see [not\_null\_range\_scan optimization](../query-optimizations/not_null_range_scan-optimization.md) ( >= [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes))
  * `optimize_join_buffer_size={on|off}` - see [Block-Based Join Algorithms](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms)
  * `orderby_uses_equalities={on|off}` - if not set, the optimizer ignores equality propagation. See [MDEV-8989](https://jira.mariadb.org/browse/MDEV-8989).
  * `outer_join_with_cache={on|off}` - see [Block-Based Join Algorithms](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms)
  * `partial_match_rowid_merge={on|off}` - see [Non-semi-join subquery optimizations](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md)
  * `partial_match_table_scan={on|off}` - see [Non-semi-join subquery optimizations](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md)
  * `rowid_filter={on|off}` - see [Rowid Filtering Optimization](../query-optimizations/rowid-filtering-optimization.md)
  * `sargable_casefold={on|off}` (>= [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes))
  * `semijoin={on|off}` - see [Semi-join subquery optimizations](../query-optimizations/subquery-optimizations/semi-join-subquery-optimizations.md)
  * `semijoin_with_cache={on|off}` - see [Block-Based Join Algorithms](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms)
  * `split_materialized={on|off}`
  * `subquery_cache={on|off}` - see [subquery cache](../query-optimizations/subquery-optimizations/subquery-cache.md).
  * `table_elimination={on|off}` - see [Table Elimination User Interface](../query-optimizations/table-elimination/table-elimination-user-interface.md)

#### `optimizer_record_context`

* Description: Controls storing of optimizer context of all tables that are referenced in a query.
* Command line: `--optimizer-record-context{=0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `OFF`
* Introduced: [MariaDB 12.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1)

#### `optimizer_trace`

* Description: Controls [tracing of the optimizer](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/mariadb-internals-documentation-optimizer-trace): optimizer\_trace=option=val\[,option=val...], where option is one of {enabled} and val is one of {on, off, default}
* Command line: `--optimizer-trace=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `enabled=off`
* Valid Values: `enabled={on|off|default}`

#### `optimizer_trace_max_mem_size`

* Description: Limits the memory used while tracing a query by specifying the maximum allowed cumulated size, in bytes, of stored [optimizer traces](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/mariadb-internals-documentation-optimizer-trace/optimizer-trace-resources).
* Command line: `--optimizer-trace-max-mem-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1048576`
* Range: `1` to `18446744073709551615`

#### `optimizer_use_condition_selectivity`

* Description: Controls which statistics can be used by the optimizer when looking for\
  the best query execution plan. In most cases, the default value, `4` will be suitable. However, if you are hitting some of the rare cases where this does not work well (see [MDEV-23707](https://jira.mariadb.org/browse/MDEV-23707)), you can usually work around this by setting this variable to `1`.
  * `1` Use selectivity of predicates as in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).
  * `2` Use selectivity of all range predicates supported by indexes.
  * `3` Use selectivity of all range predicates estimated without [histogram](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md).
  * `4` Use selectivity of all range predicates estimated with [histogram](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md).
  * `5` Additionally use selectivity of certain non-range predicates calculated on record sample.
* Command line: `--optimizer-use-condition-selectivity=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4`
* Range: `1` to `5`

#### `pid_file`

* Description: Full path of the process ID file. If [--log-basename](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `pid_file` should be placed after in the config files. Later settings override earlier settings, so `log-basename` will override any earlier log file name settings.
* Command line: `--pid-file=file_name`
* Scope: Global
* Dynamic: No
* Data Type: `file name`

#### `plugin_dir`

* Description: Path to the [plugin](../../../reference/plugins/) directory. For security reasons, either make sure this directory can only be read by the server, or set [secure\_file\_priv](server-system-variables.md#secure_file_priv).
* Command line: `--plugin-dir=path`
* Scope: Global
* Dynamic: No
* Data Type: `directory name`
* Default Value: `BASEDIR/lib/plugin`

#### `plugin_maturity`

* Description: The lowest acceptable [plugin](../../../reference/plugins/) maturity. MariaDB will not load plugins less mature than the specified level.
* Command line: `--plugin-maturity=level`
* Scope: Global
* Dynamic: No
* Type: enum
* Default Value: One less than the server maturity
* Valid Values: `unknown`, `experimental`, `alpha`, `beta`, `gamma`, `stable`

#### `port`

* Description: Port to listen for TCP/IP connections. If set to `0`, will default to, in order of preference, my.cnf, the MYSQL\_TCP\_PORT [environment variable](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-environment-variables.md), /etc/services, built-in default (3306).
* Command line: `--port=#`, `-P`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `3306`
* Range: `0` to `65535`

#### `preload_buffer_size`

* Description: Size in bytes of the buffer allocated when indexes are preloaded.
* Command line: `--preload-buffer-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `32768`
* Range: `1024` to `1073741824`

#### `profiling`

* Description: If set to `1` (`0` is default), statement profiling will be enabled. See [SHOW PROFILES()](../../../reference/sql-statements/administrative-sql-statements/show/show-profiles.md) and [SHOW PROFILE()](../../../reference/sql-statements/administrative-sql-statements/show/show-profile.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `profiling_history_size`

* Description: Number of statements about which profiling information is maintained. If set to `0`, no profiles are stored. See [SHOW PROFILES](../../../reference/sql-statements/administrative-sql-statements/show/show-profiles.md).
* Command line: `--profiling-history-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `15`
* Range: `0` to `100`

#### `progress_report_time`

* Description: Time in seconds between sending [progress reports](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) to the client for time-consuming statements. If set to `0`, progress reporting will be disabled.
* Command line: `--progress-report-time=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `5`
* Range: `0` to `4294967295`

#### `protocol_version`

* Description: The version of the client/server protocol used by the MariaDB server.
* Command line: None
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `10`
* Range: `0` to `4294967295`

#### `proxy_protocol_networks`

* Description: Enable [proxy protocol](../../../clients-and-utilities/server-client-software/client-libraries/proxy-protocol-support.md) for these source networks. The syntax is a comma separated list of IPv4 and IPv6 networks. If the network doesn't contain a mask, it is considered to be a single host. "\*" represents all networks and must be the only directive on the line. String "localhost" represents non-TCP local connections (Unix domain socket, Windows named pipe or shared memory). See [Proxy Protocol Support](../../../clients-and-utilities/server-client-software/client-libraries/proxy-protocol-support.md).
* Command line: `--proxy-protocol-networks=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: (empty)

#### `proxy_user`

* Description: Set to the proxy user account name if the current client is a proxy, else `NULL`.
* Scope: Session
* Dynamic: No
* Data Type: `string`

#### `pseudo_slave_mode`

* Description: For internal use by the server.
* Scope: Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `OFF`

#### `pseudo_thread_id`

* Description: For internal use only.
* Scope: Session
* Dynamic: Yes
* Data Type: `numeric`

#### `query_alloc_block_size`

* Description: Size in bytes of the extra blocks allocated during query parsing and execution (after [query\_prealloc\_size](server-system-variables.md#query_prealloc_size) is used up).
* Command line: `--query-alloc-block-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `BIGINT UNSIGNED`                            &#x20;
* Default Value:&#x20;
  * \>= [MariaDB 11.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-5-release-notes), [MariaDB 10.11.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-11-release-notes), [MariaDB 10.6.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-22-release-notes): `32768`
  * <= [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-4-release-notes), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-10-release-notes), [MariaDB 10.6.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-21-release-notes): `16384`
* Range: `1024` to `4294967295`
* Block size: `1024` &#x20;

#### `query_cache_limit`

* Description: Size in bytes for which results larger than this are not stored in the [query cache](../buffers-caches-and-threads/query-cache.md).
* Command line: `--query-cache-limit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1048576` (1MB)
* Range: `0` to `4294967295`

#### `query_cache_min_res_unit`

* Description: Minimum size in bytes of the blocks allocated for [query cache](../buffers-caches-and-threads/query-cache.md) results.
* Command line: `--query-cache-min-res-unit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4096` (4KB)
* Range - 32 bit: `1024` to `4294967295`
* Range - 64 bit: `1024` to `18446744073709547520`

#### `query_cache_size`

* Description: Size in bytes available to the [query cache](../buffers-caches-and-threads/query-cache.md). About 40KB is needed for query cache structures, so setting a size lower than this will result in a warning. `0`, the default before [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes), effectively disables the query cache.

**Warning:** Starting from [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes), [query\_cache\_type](server-system-variables.md#query_cache_type) is automatically set to ON if the server is started with the query\_cache\_size set to a non-zero (and non-default) value. This will happen even if [query\_cache\_type](server-system-variables.md#query_cache_type) is explicitly set to OFF in the configuration.

* Command line: `--query-cache-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1M` (although frequently given a default value in some setups)
* Valid Values: `0` upwards in units of 1024.

#### `query_cache_strip_comments`

* Description: If set to `1` (`0` is default), the server will strip any comments from the query before searching to see if it exists in the [query cache](../buffers-caches-and-threads/query-cache.md). Multiple space, line feeds, tab and other white space characters will also be removed.
* Command line: `query-cache-strip-comments`
* Scope: Session, Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `query_cache_type`

* Description: If set to `0`, the [query cache](../buffers-caches-and-threads/query-cache.md) is disabled (although a buffer of [query\_cache\_size](server-system-variables.md#query_cache_size) bytes is still allocated). If set to `1` all SELECT queries will be cached unless SQL\_NO\_CACHE is specified. If set to `2` (or `DEMAND`), only queries with the SQL CACHE clause will be cached. Note that if the server is started with the query cache disabled, it cannot be enabled at runtime.

**Warning:** Starting from [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes), query\_cache\_type is automatically set to ON if the server is started with the [query\_cache\_size](server-system-variables.md#query_cache_size) set to a non-zero (and non-default) value. This will happen even if [query\_cache\_type](server-system-variables.md#query_cache_type) is explicitly set to OFF in the configuration.

* Command line: `--query-cache-type=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `OFF`
* Valid Values: `0` or `OFF`, `1` or `ON`, `2` or `DEMAND`

#### `query_cache_wlock_invalidate`

* Description: If set to `0`, the default, results present in the [query cache](../buffers-caches-and-threads/query-cache.md) will be returned even if there's a write lock on the table. If set to `1`, the client will first have to wait for the lock to be released.
* Command line: `--query-cache-wlock-invalidate`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `query_prealloc_size`

* Description: Size in bytes of the persistent buffer for query parsing and execution, allocated on connect and freed on disconnect. Increasing may be useful if complex queries are being run, as this will reduce the need for more memory allocations during query operation. See also [query\_alloc\_block\_size](server-system-variables.md#query_alloc_block_size).
* Command line: `--query-prealloc-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:&#x20;
  * \>= [MariaDB 11.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-5-release-notes), [MariaDB 10.11.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-11-release-notes), [MariaDB 10.6.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-22-release-notes): `32768`
  * <= [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-4-release-notes), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-10-release-notes), [MariaDB 10.6.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-21-release-notes): `24576` &#x20;
* Range: `1024` to `4294967295`

#### `rand_seed1`

* Description: `rand_seed1` and `rand_seed2` facilitate replication of the [RAND()](../../../reference/sql-functions/numeric-functions/rand.md) function. The master passes the value of these to the slaves so that the random number generator is seeded in the same way, and generates the same value, on the slave as on the master.
* Command line: None
* Scope: Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: Varies
* Range: `0` to `18446744073709551615`

#### `rand_seed2`

* Description: See [rand\_seed1](server-system-variables.md#rand_seed1).

#### `range_alloc_block_size`

* Description: Size in bytes of blocks allocated during range optimization. The unit size in 1024.
* Command line: `--range-alloc-block-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4096`
* Range - 32 bit: `4096` to `4294967295`
* Range - 64 bit: `4096` to `18446744073709547520`

#### `read_buffer_size`

* Description: Each thread performing a sequential scan (for MyISAM, Aria and MERGE tables) allocates a buffer of this size in bytes for each table scanned. Increase if you perform many sequential scans. If not in a multiple of 4KB, will be rounded down to the nearest multiple. Also used in ORDER BY's for caching indexes in a temporary file (not temporary table), for caching results of nested queries, for bulk inserts into partitions, and to determine the memory block size of [MEMORY](../../../server-usage/storage-engines/memory-storage-engine.md) tables.
* Command line: `--read-buffer-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `131072`
* Range: `8192` to `2147479552`

#### `read_only`

{% tabs %}
{% tab title="Current" %}
* Description: Do not allow changes to non-temporary tables. Options are: `OFF` — changes allowed; `ON` — Disallow changes for users without the `READ ONLY ADMIN` privilege; `NO_LOCK` — Additionally disallows `LOCK TABLES` and `SELECT ... IN SHARE MODE`; `NO_LOCK_NO_ADMIN` — Disallows also for users with `READ_ONLY ADMIN` privilege. Replication (slave) threads are not affected by this option.
* Command line: `--read-only`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `OFF`
* Valid values: `OFF`, `ON`, `NO_LOCK`, `NO_LOCK_NO_ADMIN`
{% endtab %}

{% tab title="< 12.0" %}
* Description: When set to `1` (`0` is default), no updates are permitted except from users with the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes), the [READ ONLY ADMIN](../../../reference/sql-statements/account-management-sql-statements/grant.md#read_only-admin) privilege, or replica servers updating from a primary. The `read_only` variable is useful for replica servers to ensure no updates are accidentally made outside of what are performed on the primary. Inserting rows to log tables, updates to temporary tables and [OPTIMIZE TABLE](../optimizing-tables/optimize-table.md) or [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md) statements are excluded from this limitation. If `read_only` is set to `1`, then the [SET PASSWORD](../../../reference/sql-statements/account-management-sql-statements/set-password.md) statement is limited only to users with the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes)) or [READ ONLY ADMIN](../../../reference/sql-statements/account-management-sql-statements/grant.md#read_only-admin) privilege (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes)). Attempting to set this variable to `1` will fail if the current session has table locks or transactions pending, while if other sessions hold table locks, the statement will wait until these locks are released before completing. While the attempt to set `read_only` is waiting, other requests for table locks or transactions will also wait until `read_only` has been set. See [Read-Only Replicas](../../standard-replication/read-only-replicas.md) for more. From [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes), the [READ\_ONLY ADMIN](../../../reference/sql-statements/account-management-sql-statements/grant.md#read_only-admin) privilege will allow users granted that privilege to perform writes, even if the `read_only` variable is set. In earlier versions, and until [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-0-release-notes), users with the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) can perform writes while this variable is set.
* Command line: `--read-only`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
{% endtab %}
{% endtabs %}

#### `read_rnd_buffer_size`

* Description: Size in bytes of the buffer used when reading rows from a [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) table in sorted order after a key sort. Larger values improve ORDER BY performance, although rather increase the size by SESSION where the need arises to avoid excessive memory use.
* Command line: `--read-rnd-buffer-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `262144`
* Range: `8200` to `2147483647`

#### `redirect_url`

* Description: URL of another server to redirect clients to. Format should be `{mysql,mariadb}://host [:port]`. Empty string means no redirection. For example `set global redirect_url="mysql://mariadb.org:12345"`. See [Connection Redirection Mechanism in the MariaDB Client/Server Protocol](../../connection-redirection-mechanism-in-the-mariadb-clientserver-protocol.md).
* Command line: `--redirect_url=val`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty
* Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `require_secure_transport`

* Description: When this option is enabled, connections attempted using insecure transport will be rejected. Secure transports are SSL/TLS, Unix sockets or named pipes. Note that [per-account requirements](../../../security/securing-mariadb/encryption/data-in-transit-encryption/securing-connections-for-client-and-server.md#requiring-tls) take precedence.
* Command line: `--require-secure-transport[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes)

#### `rowid_merge_buff_size`

* Description: The maximum size in bytes of the memory available to the Rowid-merge strategy. See [Non-semi-join subquery optimizations](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md#optimizer-control) for more information.
* Command line: `--rowid-merge-buff-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `8388608`
* Range: `0` to `2147483647`

#### `rpl_recovery_rank`

* Description: Unused.
* Removed: [MariaDB 10.1.2](https://github.com/mariadb-corporation/docs-server/blob/test/server/ha-and-performance/optimization-and-tuning/system-variables/broken-reference/README.md)

#### `safe_show_database`

* Description: This variable was removed in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), and has been replaced by the more flexible [SHOW DATABASES](../../../reference/sql-statements/administrative-sql-statements/show/show-databases.md) privilege.
* Command line: `--safe-show-database` (until MySQL 4.1.1)
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `secure_auth`

* Description: Connections will be blocked if they use the [mysql\_old\_password](../../../reference/plugins/authentication-plugins/authentication-plugin-mysql_old_password.md) authentication plugin. The server will also fail to start if the privilege tables are in the old, pre-MySQL 4.1 format. `secure_auth=0` was deprecated in [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes).
* Command line: `--secure-auth`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `secure_file_priv`

* Description: [LOAD DATA](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md), [SELECT ... INTO](../../../reference/sql-statements/data-manipulation/selecting-data/select.md#into) and [LOAD FILE()](../../../reference/sql-functions/string-functions/load_file.md) will only work with files in the specified path. If not set, the default, or set to empty string, the statements will work with any files that can be accessed.
* Command line: `--secure-file-priv=path`
* Scope: Global
* Dynamic: No
* Data Type: `path name`
* Default Value: None

#### `secure_timestamp`

* Description: Restricts direct setting of a session timestamp. Possible levels are:
  * YES - timestamp cannot deviate from the system clock. Intended to prevent tampering with [system versioning](../../../reference/sql-structure/temporal-tables/system-versioned-tables.md) history. Should not be used on replicas, as when a value based on the timestamp is inserted in [statement mode](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging), discrepancies can occur.
  * REPLICATION - replication thread can adjust timestamp to match the primary's
  * SUPER - a user with this privilege and a replication thread can adjust timestamp
  * NO - historical behavior, anyone can modify session timestamp
* Command line: `--secure-timestamp=value`
* Scope: Global
* Dynamic: No
* Data Type: `enum`
* Default Value: `NO`

#### `server_uid`

* Description: Automatically calculated server unique id hash. Added to the [error log](../../../server-management/server-monitoring-logs/error-log.md) to allow one to verify if error reports are from the same server. UID is a base64-encoded SHA1 hash of the MAC address of one of the interfaces, and the tcp port that the server is listening on.
* Command line: None
* Scope: Global
* Dynamic: No
* Data Type: `varchar`
* Default Value: None
* Introduced: [MariaDB 10.5.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10-5-26-release-notes), [MariaDB 10.6.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-19-release-notes), [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-9-release-notes), [MariaDB 11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-3-release-notes), [MariaDB 11.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes), [MariaDB 11.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes)

#### `session_track_schema`

* Description: Whether to track changes to the default schema within the current session.
* Command line: `--session-track-schema={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `session_track_state_change`

* Description: Whether to track changes to the session state.
* Command line: `--session-track-state-change={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `session_track_system_variables`

* Description: Comma-separated list of session system variables for which to track changes. For compatibility with MySQL defaults, this variable should be set to "autocommit, character\_set\_client, character\_set\_connection, character\_set\_results, time\_zone". The `*` character tracks all session variables.
* Command line: `--session-track-system-variables=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value:
  * > \= [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113): `autocommit,character_set_client,character_set_connection,character_set_results,redirect_url,time_zone`
  * <= [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112): `autocommit, character_set_client, character_set_connection, character_set_results, time_zone`

#### `session_track_transaction_info`

* Description: Track changes to the transaction attributes. OFF to disable; STATE to track just transaction state (Is there an active transaction? Does it have any data? etc.); CHARACTERISTICS to track transaction state and report all statements needed to start a transaction with the same characteristics (isolation level, read only/read write,snapshot - but not any work done / data modified within the transaction).
* Command line: `--session-track-transaction-info=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `OFF`
* Valid Values: `OFF`, `STATE`, `CHARACTERISTICS`

#### `shared_memory`

* Description: Windows only, determines whether the server permits shared memory connections. See also [shared\_memory\_base\_name](server-system-variables.md#shared_memory_base_name).
* Scope: Global
* Dynamic: No

#### `shared_memory_base_name`

* Description: Windows only, specifies the name of the shared memory to use for shared memory connection. Mainly used when running more than one instance on the same physical machine. By default the name is `MYSQL` and is case sensitive. See also [shared\_memory](server-system-variables.md#shared_memory).
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `MYSQL`

#### `shutdown_wait_for_slaves`

* Description: When `ON, SHUTDOWN` command runs with implicit `WAIT FOR ALL SLAVES` option. That is, when running `SHUTDOWN`, before killing the binary log dump threads, the server will first kill all client threads and send all binary log events to all connected replicas.
* Scope: Global
* Dynamic: No
* Data Type: `Boolean`
* Default Value: `OFF`

#### `skip_external_locking`

* Description: If this system variable is set, then some kinds of external table locks will be disabled for some [storage engines](../../../server-usage/storage-engines/).
  * If this system variable is set, then the [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) storage engine will not use file-based locks. Otherwise, it will use the [fcntl()](https://linux.die.net/man/2/fcntl) function with the `F_SETLK` option to get file-based locks on Unix, and it will use the [LockFileEx()](https://docs.microsoft.com/en-us/windows/desktop/api/fileapi/nf-fileapi-lockfileex) function to get file-based locks on Windows.
  * If this system variable is set, then the [Aria](../../../server-usage/storage-engines/aria/) storage engine will not lock a table when it decrements the table's in-file counter that keeps track of how many connections currently have the table open. See [MDEV-19393](https://jira.mariadb.org/browse/MDEV-19393) for more information.
  * Note that command line option name is the opposite of the variable name, and the value is the opposite too. `--external-locking=1` means `@@skip_external_locking=0`, and vice versa.
* Command line: `--external-locking`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `1` (for the variable, that is `0` for the command line option)

#### `skip_grant_tables`

* Description: Start without grant tables. This gives all users FULL ACCESS to all tables. Before [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010), available as an [option only](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md). Use [mariadb-admin flush-privileges](../../../clients-and-utilities/legacy-clients-and-utilities/mysqladmin.md), [mariadb-admin reload](../../../clients-and-utilities/legacy-clients-and-utilities/mysqladmin.md) or [FLUSH PRIVILEGES](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) to resume using the grant tables.
* Command line: `--skip-grant-tables`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `skip_name_resolve`

* Description: If set to `ON` (`OFF` is the default), only IP addresses are used for connections. Host names are not resolved. All host values in the GRANT tables must be IP addresses (or localhost). Some container configs explicitly set `skip_name_resolve` to `ON`, rather than leave it as the default, `OFF`.
* Command line: `--skip-name-resolve`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `skip_networking`

* Description: If set to 1, (0 is the default), the server does not listen for TCP/IP connections. All interaction with the server will be through socket files (Unix) or named pipes or shared memory (Windows). It's recommended to use this option if only local clients are permitted to connect to the server.
* Command line: `--skip-networking`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `0`

#### `skip_show_database`

* Description: If set to 1, (0 is the default), only users with the [SHOW DATABASES](../../../reference/sql-statements/administrative-sql-statements/show/show-databases.md) privilege can use the SHOW DATABASES statement to see all database names.
* Command line: `--skip-show-database`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `0`

#### `slow_launch_time`

* Description: Time in seconds. If a thread takes longer than this to launch, the `slow_launch_threads` [server status variable](server-status-variables.md) is incremented.
* Command line: `--slow-launch-time=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2`

#### `slow_query_log`

* Description: If set to 0, the default unless the --slow-query-log option is used, the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) is disabled, while if set to 1 (both global and session variables), the slow query log is enabled. From [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-0-release-notes), an alias for [log\_slow\_query](server-system-variables.md#log_slow_query).
* Command line: `--slow-query-log`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Data Type: `boolean`
* Default Value: `0`
* See also: See [log\_output](server-system-variables.md#log_output) to see how log files are written. If that variable is set to `NONE`, no logs will be written even if slow\_query\_log is set to `1`.

#### `slow_query_log_file`

* Description: Name of the [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) file. From [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), an alias for [log\_slow\_query\_file](server-system-variables.md#log_slow_query_file). If [--log-basename](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `slow_query_log_file` should be placed after in the config files. Later settings override earlier settings, so `log-basename` will override any earlier log file name settings.
* Command line: `--slow-query-log-file=file_name`
* Scope: Global
* Dynamic: Yes
* Data Type: `file name`
* Default Value: `host_name-slow.log`

#### `socket`

* Description: On Unix-like systems, this is the name of the socket file used for local client connections, by default `/tmp/mysql.sock`, often changed by the distribution, for example `/var/lib/mysql/mysql.sock`. On Windows, this is the name of the named pipe used for local client connections, by default `MySQL`. On Windows, this is not case-sensitive.
* Command line: `--socket=name`
* Scope: Global
* Dynamic: No
* Data Type: `file name`
* Default Value: `/tmp/mysql.sock` (Unix), `MySQL` (Windows)

#### `sort_buffer_size`

* Description: Each session performing a sort allocates a buffer with this amount of memory. Not specific to any storage engine. If the status variable [sort\_merge\_passes](server-status-variables.md#sort_merge_passes) is too high, you may need to look at improving your query indexes, or increasing this. Consider reducing where there are many small sorts, such as OLTP, and increasing where needed by session. 16k is a suggested minimum.
* Command line: `--sort-buffer-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `number`
* Default Value: `2M (2097152)` (some distributions increase the default)

#### `sql_auto_is_null`

* Description: If set to 1, the query `SELECT * FROM table_name WHERE auto_increment_column IS NULL` will return an auto-increment that has just been successfully inserted, the same as the LAST\_INSERT\_ID() function. Some ODBC programs make use of this IS NULL comparison.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`

#### `sql_big_selects`

* Description: If set to 0, MariaDB will not perform large SELECTs. See [max\_join\_size](server-system-variables.md#max_join_size) for details. If max\_join\_size is set to anything but DEFAULT, sql\_big\_selects is automatically set to 0. If sql\_big\_selects is again set, max\_join\_size will be ignored.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`

#### `sql_big_tables`

* Description: Old variable, which if set to 1, allows large result sets by saving all temporary sets to disk, avoiding 'table full' errors. No longer needed, as the server now handles this automatically.
  * This is a synonym for [big\_tables](server-system-variables.md#big_tables).
* Command line: `--sql-big-tables`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `sql_buffer_result`

* Description: If set to 1 (0 is default), results from SELECT statements are always placed into temporary tables. This can help the server when it takes a long time to send the results to the client by allowing the table locks to be freed early.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`

#### `sql_if_exists`

* Description: If set to 1, adds an implicit IF EXISTS to ALTER, RENAME and DROP of TABLES, VIEWS, FUNCTIONS and PACKAGES. This variable is mainly used in replication to tag DDLs that can be ignored on the slave if the target table doesn't exist.
* Command line: `--sql-if-exists[={0|1}]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes)

#### `sql_log_off`

* Description: If set to 1 (0 is the default), no logging to the [general query log](../../../server-management/server-monitoring-logs/general-query-log.md) is done for the client. Only clients with the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege can update this variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`

#### `sql_log_update`

* Description: Removed. Use [sql\_log\_bin](server-system-variables.md#sql_log_bin) instead.
* Removed: MariaDB/MySQL 5.5

#### `sql_low_priority_updates`

* Description: If set to 1 (0 is the default), for [storage engines](../../../server-usage/storage-engines/) that use only table-level locking ([Aria](../../../server-usage/storage-engines/aria/), [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/), [MEMORY](../../../server-usage/storage-engines/memory-storage-engine.md) and [MERGE](../../../server-usage/storage-engines/merge.md)), all INSERTs, UPDATEs, DELETEs and LOCK TABLE WRITEs will wait until there are no more SELECTs or LOCK TABLE READs pending on the relevant tables. Set this to 1 if reads are prioritized over writes.
  * This is a synonym for [low\_priority\_updates](server-system-variables.md#low_priority_updates).
* Command line: `--sql-low-priority-updates`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `sql_max_join_size`

* Description: Synonym for [max\_join\_size](server-system-variables.md#max_join_size), the preferred name.
* Deprecated: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `sql_mode`

* Description: Sets the [SQL Mode](../../../server-management/variables-and-modes/sql-mode.md). Multiple modes can be set, separated by a comma.
* Command line: `--sql-mode=value[,value[,value...]]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value:
  * `STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION`
* Valid Values: See [SQL Mode](../../../server-management/variables-and-modes/sql-mode.md) for the full list.

#### `sql_notes`

* Description: If set to 1, the default, [warning\_count](server-system-variables.md#warning_count) is incremented each time a Note warning is encountered. If set to 0, Note warnings are not recorded. [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) has outputs to set this variable to 0 so that no unnecessary increments occur when data is reloaded. See also [note\_verbosity](server-system-variables.md#note_verbosity), which defines which notes should be given. The recommended way, as of [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes), to disable notes is to set `note_verbosity` to "".
* Command line: None
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`

#### `sql_quote_show_create`

* Description: If set to 1, the default, the server will quote identifiers for [SHOW CREATE DATABASE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-database.md), [SHOW CREATE TABLE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) and [SHOW CREATE VIEW](../../../reference/sql-statements/administrative-sql-statements/show/show-create-view.md) statements. Quoting is disabled if set to 0. Enable to ensure replication works when identifiers require quoting.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`

#### `sql_safe_updates`

* Description: If set to 1, UPDATEs and DELETEs must be executed by using an index (simply mentioning an indexed column in a WHERE clause is not enough, optimizer must actually use it) or they must mention an indexed column and specify a LIMIT clause. Otherwise a statement will be aborted. Prevents the common mistake of accidentally deleting or updating every row in a table. Until [MariaDB 10.3.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10311-release-notes), could not be set as a command-line option or in my.cnf.
* Command line: `--sql-safe-updates[={0|1}]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `sql_select_limit`

* Description: Maximum number of rows that can be returned from a SELECT query. Default is the maximum number of rows permitted per table by the server, usually 232-1 or 264-1. Can be restored to the default value after being changed by assigning it a value of DEFAULT. If a SELECT has a LIMIT clause, the LIMIT takes precedence over the value of the variable.
* Command line: None
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `18446744073709551615`

#### `sql_warnings`

* Description: If set to 1, single-row INSERTs will produce a string containing warning information if a warning occurs.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF (0)`

#### `storage_engine`

* Description: See [default\_storage\_engine](server-system-variables.md#default_storage_engine).
* Deprecated: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)
* Remove: [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120)

#### `standard_compliant_cte`

* Description: Allow only standard-compliant [common table expressions](../../../reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/). Prior to [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes), this variable was named `standards_compliant_cte`.
* Command line: `--standard-compliant-cte={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `stored_program_cache`

* Description: Limit to the number of [stored routines](../../../server-usage/stored-routines/) held in the stored procedures and stored functions caches. Each time a stored routine is executed, this limit is first checked, and if the number held in the cache exceeds this, that cache is flushed and memory freed.
* Command line: `--stored-program-cache=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `256`
* Range: `256` to `524288`

#### `strict_password_validation`

* Description: When [password validation](../../../reference/plugins/password-validation-plugins/) plugins are enabled, reject passwords that cannot be validated (passwords specified as a hash). This excludes direct updates to the privilege tables.
* Command line: `--strict-password-validation`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `sync_frm`

* Description: If set to 1, the default, each time a non-temporary table is created, its .frm definition file is synced to disk. Fractionally slower, but safer in case of a crash.
* Command line: `--sync-frm`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `TRUE`

#### `system_time_zone`

* Description: The system time zone is determined when the server starts. The system [time zone](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) is usually read from the operating system's environment but can be overridden by setting the 'TZ' environment variable before starting the server. See [Time Zones: System Time Zone](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md#system-time-zone) for the various ways to change the system time zone. This variable is not the same as the [time\_zone](server-system-variables.md#time_zone) system variable, which is the variable that actually controls a session's active time zone. The system time zone is used for a session when `time_zone` is set to the special value `SYSTEM`.
* Scope: Global
* Dynamic: No
* Data Type: `string`

#### `table_definition_cache`

* Description: Number of table definitions that can be cached. Table definitions are taken from the .frm files, and if there are a large number of tables increasing the cache size can speed up table opening. Unlike the [table\_open\_cache](server-system-variables.md#table_open_cache), as the table\_definition\_cache doesn't use file descriptors, and is much smaller.
* Command line: `--table-definition-cache=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `400`
* Range: `400` to `2097152`

#### `table_lock_wait_timeout`

* Description: Unused, and removed.
* Command line: `--table-lock-wait-timeout=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `50`
* Range: `1` to `1073741824`
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `table_open_cache`

* Description: Maximum number of open tables cached in one table cache instance. See [Optimizing table\_open\_cache](optimizing-table_open_cache.md) for suggestions on optimizing. Increasing table\_open\_cache increases the number of file descriptors required.
* Command line: `--table-open-cache=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2000`
* Range:
  * `1` to `1048576` (1024K)

#### `table_open_cache_instances`

* Description: This system variable specifies the maximum number of table cache instances. MariaDB Server initially creates just a single instance. However, whenever it detects contention on the existing instances, it will automatically create a new instance. When the number of instances has been increased due to contention, it does not decrease again. The default value of this system variable is `8`, which is expected to handle up to 100 CPU cores. If your system is larger than this, then you may benefit from increasing the value of this system variable.
  * Depending on the ratio of actual available file handles, and [table\_open\_cache](server-system-variables.md#table_open_cache) size, the max. instance count may be auto adjusted to a lower value on server startup.
  * The implementation and behavior of this feature is different than the same feature in MySQL 5.6.
  * See [Optimizing table\_open\_cache: Automatic Creation of New Table Open Cache Instances](optimizing-table_open_cache.md#automatic-creation-of-new-table-open-cache-instances) for more information.
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8` (>= [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes))
* Range: `1` to `64`

#### `table_type`

* Description: Removed and replaced by [storage\_engine](server-system-variables.md#storage_engine). Use [default\_storage\_engine](server-system-variables.md#default_storage_engine) instead.

#### `tcp_keepalive_interval`

* Description: The interval, in seconds, between when successive keep-alive packets are sent if no acknowledgement is received. If set to 0, the system dependent default is used.
* Command line: `--tcp-keepalive-interval=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `2147483`

#### `tcp_keepalive_probes`

* Description: The number of unacknowledged probes to send before considering the connection dead and notifying the application layer. If set to 0, a system dependent default is used.
* Command line: `--tcp-keepalive-probes=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `2147483`

#### `tcp_keepalive_time`

* Description: Timeout, in seconds, with no activity until the first TCP keep-alive packet is sent. If set to 0, a system dependent default is used.
* Command line: `--tcp-keepalive-time=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `2147483`

#### `tcp_nodelay`

* Description: Set the TCP\_NODELAY option (disable Nagle's algorithm) on socket.
* Command line: `--tcp-nodelay={0|1}`
* Scope: Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`

#### `thread_cache_size`

* Description: Number of threads server caches for re-use. If this limit hasn't been reached, when a client disconnects, its threads are put into the cache, and re-used where possible. In [MariaDB 10.](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)[MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) and newer the threads are freed after 5 minutes of idle time. Normally this setting has little effect, as the other aspects of the thread implementation are more important, but increasing it can help servers with high volumes of connections per second so that most can use a cached, rather than a new, thread. The cache miss rate can be calculated as the [server status variables](server-status-variables.md) threads\_created/connections. If the [thread pool](../buffers-caches-and-threads/thread-pool/) is active, `thread_cache_size` is ignored. If `thread_cache_size` is set to greater than the value of [max\_connections](server-system-variables.md#max_connections), `thread_cache_size` will be set to the [max\_connections](server-system-variables.md#max_connections) value.
* Command line: `--thread-cache-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `256` (adjusted if thread pool is active)
* Range: `0` to `16384`

#### `thread_concurrency`

* Description: Allows applications to give the system a hint about the desired number of threads. Specific to Solaris only, invokes thr\_setconcurrency(). Deprecated and has no effect from [MariaDB 5.5](https://github.com/mariadb-corporation/docs-server/blob/test/server/ha-and-performance/optimization-and-tuning/system-variables/broken-reference/README.md).
* Command line: `--thread-concurrency=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `10`
* Range: `1` to `512`
* Deprecated: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes)

#### `thread_stack`

* Description: Stack size for each thread. If set too small, limits recursion depth of stored procedures and complexity of SQL statements the server can handle in memory. Also affects limits in the crash-me test.
* Command line: `--thread-stack=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:
  * `299008`
* Range: `131072` to `18446744073709551615`

#### `time_format`

* Description: Unused.
* Removed: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `time_zone`

* Description: The global value determines the default [time zone](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for sessions that connect. The session value determines the session's active [time zone](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md). When it is set to `SYSTEM`, the session's time zone is determined by the [system\_time\_zone](server-system-variables.md#system_time_zone) system variable.
* Command line: `--default-time-zone=string`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `SYSTEM`

#### `timed_mutexes`

* Description: Determines whether [InnoDB](../../../server-usage/storage-engines/innodb/) mutexes are timed. `OFF`, the default, disables mutex timing, while `ON` enables it. See also [SHOW ENGINE](../../../reference/sql-statements/administrative-sql-statements/show/show-engine.md) for more on mutex statistics. Deprecated and has no effect.
* Command line: `--timed-mutexes`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 5.5.39](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5539-release-notes)
* Removed: [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes)

#### `timestamp`

* Description: Sets the time for the client. This will affect the result returned by the [NOW()](../../../reference/sql-functions/date-time-functions/now.md) function, not the [SYSDATE()](../../../reference/sql-functions/date-time-functions/sysdate.md) function, unless the server is started with the [--sysdate-is-now](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option, in which case SYSDATE becomes an alias of NOW, and will also be affected. Also used to get the original timestamp when restoring rows from the [binary log](../../../server-management/server-monitoring-logs/binary-log/).
* Scope: Session
* Dynamic: Yes
* Valid Values: `timestamp_value` (Unix epoch timestamp, not MariaDB timestamp), `DEFAULT`

#### `tmp_disk_table_size`

* Description: Max size for data for an internal temporary on-disk [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) or [Aria](../../../server-usage/storage-engines/aria/) table. These tables are created as part of complex queries when the result doesn't fit into the memory engine. You can set this variable if you want to limit the size of temporary tables created in your temporary directory [tmpdir](server-system-variables.md#tmpdir).
* Command line: `--tmp-disk-table-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `18446744073709551615` (max unsigned integer, no limit)
* Range: `1024` to `18446744073709551615`

#### `tmp_memory_table_size`

* Description: An alias for [tmp\_table\_size](server-system-variables.md#tmp_table_size).
* Command line: `--tmp-memory-table-size=#`

#### `tmp_table_size`

* Description: The largest size for temporary tables in memory (not [MEMORY](../../../server-usage/storage-engines/memory-storage-engine.md) tables) although if [max\_heap\_table\_size](server-system-variables.md#max_heap_table_size) is smaller the lower limit will apply. You can see if it's necessary to increase by comparing the [status variables](server-status-variables.md) `Created_tmp_disk_tables` and `Created_tmp_tables` to see how many temporary tables out of the total created needed to be converted to disk. Often complex GROUP BY queries are responsible for exceeding the limit. Defaults may be different on some systems, see for example [Differences in MariaDB in Debian](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md). From [MariaDB 10.2.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1027-release-notes), [tmp\_memory\_table\_size](server-system-variables.md#tmp_memory_table_size) is an alias.
* Command line: `--tmp-table-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `16777216` (16MB)
* Range:
  * `1024` to `4294967295` (< [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105))
  * `0` to `4294967295` (>= [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes))

#### `tmpdir`

* Description: Directory for storing temporary tables and files. Can specify a list (separated by semicolons in Windows, and colons in Unix) that will then be used in round-robin fashion. This can be used for load balancing across several disks. Note that if the server is a [replication](https://github.com/mariadb-corporation/docs-server/blob/test/server/ha-and-performance/optimization-and-tuning/system-variables/broken-reference/README.md) replica, and [slave\_load\_tmpdir](../../standard-replication/replication-and-binary-log-system-variables.md#slave_load_tmpdir), which overrides `tmpdir` for replicas, is not set, you should not set `tmpdir` to a directory that is cleared when the machine restarts, or else replication may fail.
* Command line: `--tmpdir=path` or `-t path`
* Scope: Global
* Dynamic: No
* Type: directory name/s
* Default:
  * `$TMPDIR` (environment variable) if set
  * otherwise `$TEMP` if set and on Windows
  * otherwise `$TMP` if set and on Windows
  * otherwise `P_tmpdir` (`"/tmp"`) or `C:\TEMP` (unless overridden during buid time)

#### `transaction_alloc_block_size`

* Description: Size in bytes to increase the memory pool available to each transaction when the available pool is not large enough. See [transaction\_prealloc\_size](server-system-variables.md#transaction_prealloc_size).
* Command line: `--transaction-alloc-block-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Type: numeric
* Default Value: `8192`
* Range: `1024` to `134217728` (128M)
* Block Size: `1024`

#### `transaction_isolation`

* Description: The transaction isolation level. See also [SET TRANSACTION ISOLATION LEVEL](../../../reference/sql-statements/transactions/set-transaction.md). Introduced in [MariaDB 11.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-1-release-notes) to replace the [tx\_isolation](server-system-variables.md#tx_isolation) system variable and align the option and the system variable name.
* Command line: `--transaction-isolation=name`
* Scope: Global, Session
* Dynamic: Yes
* Type: enumeration
* Default Value: `REPEATABLE-READ`
* Valid Values: `READ-UNCOMMITTED`, `READ-COMMITTED`, `REPEATABLE-READ`, `SERIALIZABLE`
* Introduced: [MariaDB 11.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-1-release-notes)

#### `transaction_prealloc_size`

* Description: Initial size of a memory pool available to each transaction for various memory allocations. If the memory pool is not large enough for an allocation, it is increased by [transaction\_alloc\_block\_size](server-system-variables.md#transaction_alloc_block_size) bytes, and truncated back to transaction\_prealloc\_size bytes when the transaction is completed. If set large enough to contain all statements in a transaction, extra malloc() calls are avoided.
* Command line: `--transaction-prealloc-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Type: numeric
* Default Value: `4096`
* Range: `1024` to `134217728` (128M)
* Block Size: `1024`

#### `transaction_read_only`

* Description: Default transaction access mode. If set to `OFF`, the default, access is read/write. If set to `ON`, access is read-only. The `SET TRANSACTION` statement can also change the value of this variable. See [SET TRANSACTION](../../../reference/sql-statements/transactions/set-transaction.md) and [START TRANSACTION](../../../reference/sql-statements/transactions/start-transaction.md).
* Command line: None
* Scope: Global, Session
* Dynamic: Yes
* Type: boolean
* Default Value: `OFF`
* Introduced: [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111)

#### `tx_isolation`

* Description: The transaction isolation level. Setting this session variable via `set @@tx_isolation=` will take effect for only the subsequent transaction in the current session, much like [SET TRANSACTION ISOLATION LEVEL](../../../reference/sql-statements/transactions/set-transaction.md). To set for a session, use `SET SESSION tx_isolation` or `SET @@session.tx_isolation`. See [MDEV-31751](https://jira.mariadb.org/browse/MDEV-31751). See also [SET TRANSACTION ISOLATION LEVEL](../../../reference/sql-statements/transactions/set-transaction.md). In [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111), this system variable is deprecated and replaced by [transaction\_isolation](server-system-variables.md#transaction_isolation).
* Command line: `--transaction-isolation=name`
* Scope: Global, Session
* Dynamic: Yes
* Type: enumeration
* Default Value: `REPEATABLE-READ`
* Valid Values: `READ-UNCOMMITTED`, `READ-COMMITTED`, `REPEATABLE-READ`, `SERIALIZABLE`
* Deprecated: [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111)

#### `tx_read_only`

* Description: Default transaction access mode. If set to `OFF`, the default, access is read/write. If set to `ON`, access is read-only. The `SET TRANSACTION` statement can also change the value of this variable. See [SET TRANSACTION](../../../reference/sql-statements/transactions/set-transaction.md) and [START TRANSACTION](../../../reference/sql-statements/transactions/start-transaction.md). In [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111), this system variable is deprecated and replaced by [transaction\_read\_only](server-system-variables.md#transaction_read_only).
* Command line: `--transaction-read-only=#`
* Scope: Global, Session
* Dynamic: Yes
* Type: boolean
* Default Value: `OFF`
* Deprecated: [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111)

#### `unique_checks`

* Description: If set to 0, storage engines can (but are not required to) assume that duplicate keys are not present in input data. If set to 0, inserting duplicates into a `UNIQUE` index can succeed, causing the table to become corrupted. Set to 0 to speed up imports of large tables to InnoDB.
* Scope: Global, Session
* Dynamic: Yes
* Type: boolean
* Default Value: `1`

#### `updatable_views_with_limit`

* Description: Determines whether view updates can be made with an UPDATE or DELETE statement with a LIMIT clause if the view does not contain all primary or not null unique key columns from the underlying table. `0` prohibits this, while `1` permits it while issuing a warning (the default).
* Command line: `--updatable-views-with-limit=#`
* Scope: Global, Session
* Dynamic: Yes
* Type: boolean
* Default Value: `1`

#### `use_stat_tables`

* Description: Controls the use of [engine-independent table statistics](../query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md).
  * `never`: The optimizer will not use data from statistics tables.
  * `complementary`: The optimizer uses data from statistics tables if the same kind of data is not provided by the storage engine.
  * `preferably`: Prefer the data from statistics tables, if it's not available there, use the data from the storage engine.
  * `complementary_for_queries`: Same as `complementary`, but for queries only (to avoid needlessly collecting for [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md)).
  * `preferably_for_queries`: Same as `preferably`, but for queries only (to avoid needlessly collecting for [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md)).
* Command line: `--use-stat-tables=mode`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `preferably_for_queries`

#### `version`

* Description: Server version number. It may also include a suffix with configuration or build information. `-debug` indicates debugging support was enabled on the server, and `-log` indicates at least one of the binary log, general log or [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) are enabled, for example `10.0.1-MariaDB-mariadb1precise-log`. Can be set at startup in order to fake the server version.
* Command line: `-V`, `--version[=name]`
* Scope: Global
* Dynamic: No
* Type: string

#### `version_comment`

* Description: Value of the COMPILATION\_COMMENT option specified by CMake when building MariaDB, for example `mariadb.org binary distribution`.
* Scope: Global
* Dynamic: No
* Type: string

#### `version_compile_machine`

* Description: The machine type or architecture MariaDB was built on, for example `i686`.
* Scope: Global
* Dynamic: No
* Type: string

#### `version_compile_os`

* Description: Operating system that MariaDB was built on, for example `debian-linux-gnu`.
* Scope: Global
* Dynamic: No
* Type: string

#### `version_malloc_library`

* Description: Version of the used malloc library.
* Command line: None
* Scope: Global
* Dynamic: No
* Type: string

#### `version_source_revision`

* Description: Source control revision id for MariaDB source code, enabling one to see exactly which version of the source was used for a build.
* Command line: None
* Scope: Global
* Dynamic: No
* Type: string

#### `wait_timeout`

* Description: Time in seconds that the server waits for a connection to become active before closing it. The session value is initialized when a thread starts up from either the global value, if the connection is non-interactive, or from the [interactive\_timeout](server-system-variables.md#interactive_timeout) value, if the connection is interactive.
* Command line: `--wait-timeout=#`
* Scope: Global, Session
* Dynamic: Yes
* Type: numeric
* Default Value: `28800`
* Range: (Windows): `1` to `2147483`
* Range: (Other): `1` to `31536000`

#### `warning_count`

* Description: Read-only variable indicating the number of warnings, errors and notes resulting from the most recent statement that generated messages. See [SHOW WARNINGS](../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md) for more. Note warnings will only be recorded if [sql\_notes](server-system-variables.md#sql_notes) is true (the default).
* Scope: Session
* Dynamic: No
* Type: numeric

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
