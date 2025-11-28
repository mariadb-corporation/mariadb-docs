# mariadb-dump

The `mariadb-dump` client is a backup program originally written by Igor Romanenko.

{% hint style="info" %}
Previously, the client used to be called `mysqldump`, and can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows. From MariaDB 11.0, the symlink `mysqldump` is deprecated and removed from the `mariadb` Docker Official Image.
{% endhint %}

{% tabs %}
{% tab title="Current" %}
`mariadb-dump` generates a command at the beginning of the dump to enable \[sandbox]\(../mariadb-client/mariadb-command line-client.md#-sandbox) mode. This command cannot be interpreted by earlier versions of the \[MariaDB command line client]\(../mariadb-client/mariadb-command line-client.md) or by MySQL's command line client, and the client generates an error if used against the versions that do not support it. This does not affect other methods of importing the data.
{% endtab %}

{% tab title="< 11.4.2 / 11.2.4 / 11.1.5 / 11.0.6 / 10.11.8 / 10.6.18 / 10.5.25" %}
N/A
{% endtab %}
{% endtabs %}

The `mariadb-dump` client can be used to dump a database or a collection of databases for backup or transfer to another database server (not necessarily MariaDB or MySQL). The dump typically contains SQL statements to create the table, populate it, or both. Also, `mariadb-dump` can also be used to generate files in CSV, other delimited text, or XML format.

{% hint style="info" %}
If you are doing a backup on the server and your tables all are [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/) tables, consider using [mariadb-hotcopy](mariadb-hotcopy.md) instead, because it can accomplish faster backups and faster restores.
{% endhint %}

`mariadb-dump` dumps triggers along with tables, as these are part of the table definition. However, [stored procedures](../../server-usage/stored-routines/stored-procedures/), [views](../../server-usage/views/), and [events](../../server-usage/triggers-events/event-scheduler/events.md) are not dumped, and need extra parameters to be recreated explicitly (for example, `--routines` and `--events`). [Procedures](../../server-usage/stored-routines/stored-procedures/) and [functions](../../server-usage/stored-routines/stored-functions/) are also part of the system tables (for example, [mysql.proc](../../reference/system-tables/the-mysql-database-tables/mysql-proc-table.md)).

`mariadb-dump` supports the [enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT](../../ha-and-performance/standard-replication/enhancements-for-start-transaction-with-consistent-snapshot.md#mariadb-dump).

## Performance

`mariadb-dump` usually doesn't consume much CPU resources on modern hardware, as by default it uses a single thread. This method is good for a heavily loaded server.

Disk input/outputs per second (IOPS), can, however, increase for multiple reasons. When you back up on the same device as the database, this produces unnecessary random IOPS. The dump is done sequentially, on a per-table basis, causing a full table scan and many buffer page misses on tables that are not fully cached in memory.

It's recommended that you back up from a network location to remove disk IOPS on the database server, but it is vital to use a separate network card to keep network bandwidth available for regular traffic.

Although `mariadb-dump` by default preserves your resources for regular spindle disks and low-core hardware, this doesn't mean that concurrent dumps cannot benefit from hardware architecture like SAN, flash storage, low write workload. The backup time would benefit from a tool such as MyDumper.

## Usage

There are four general ways to invoke `mariadb-dump`:

```bash
shell> mariadb-dump [options] db_name [tbl_name ...]
shell> mariadb-dump [options] --databases db_name ...
shell> mariadb-dump [options] --all-databases
shell> mariadb-dump [options] --system=[option_list]
```

If you do not name any tables after specifying `db_name` , or if you use the `--databases` or `--all-databases` option, entire databases are dumped.

`mariadb-dump` does not dump the `INFORMATION_SCHEMA` (or `PERFORMANCE_SCHEMA`, if enabled) database by default. MariaDB dumps the `INFORMATION_SCHEMA` if you name it explicitly on the command line, although you must also use the `--skip-lock-tables` option.

To see a list of the options your version of `mariadb-dump` supports, execute `mariadb-dump --help`.

## Row by Row vs. Buffering

`mariadb-dump` can retrieve and dump table contents row by row, or it can retrieve the entire content from a table and buffer it in memory before dumping it. Buffering in memory can be a problem if you are dumping large tables. To dump tables row by row, use the `--quick` option (or `--opt`, which enables `--quick`). The `--opt` option (and hence `--quick`) is enabled by default, so to enable memory buffering, use `--skip-quick`.

## mysql.transaction\_registry\_table

`mariadb-dump` includes logic to cater for the [mysql.transaction\_registry table](../../reference/system-tables/the-mysql-database-tables/mysql-transaction_registry-table.md).

## Old Versions of MySQL

If you are using a recent version of `mariadb-dump` to generate a dump to be reloaded into a very old MySQL server, you should _not_ use the `--opt` or `--extended-insert` option. Use `--skip-opt` instead.

## Options

`mariadb-dump` supports the following options:

### Scope

#### --all

Deprecated. Use --create-options instead.

#### -A, --all-databases

Dump all the databases. This is the same as `--databases` with all databases selected.

#### -Y, --all-tablespaces

Dump all the tablespaces.

#### -y, --no-tablespaces

Do not dump any tablespace information.

### Other Options

#### --add-drop-database

Add a [DROP DATABASE](../../reference/sql-statements/data-definition/drop/drop-database.md) before each create. Typically used in conjunction with the `--all-databases` or `--databases` option, because no [CREATE DATABASE](../../reference/sql-statements/data-definition/create/create-database.md) statements are written, unless one of those options is specified.

#### --add-drop-table

Add a [DROP TABLE](../../reference/sql-statements/data-definition/drop/drop-table.md) before each create.

#### --add-drop-trigger

Add a [DROP TRIGGER](../../reference/sql-statements/data-definition/drop/drop-trigger.md) statement before each [CREATE TRIGGER](../../server-usage/triggers-events/triggers/create-trigger.md).

#### --add-locks

Add locks around [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statements, which results in faster inserts when the dump file is reloaded. Use --skip-add-locks to disable.

#### --allow-keywords

Allow creation of column names that are keywords. This works by prefixing each column name with the table name.

#### --apply-slave-statements

Adds [STOP SLAVE](../../reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) prior to [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) and [START SLAVE](../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) to bottom of dump.

#### --as-of=name

Dump [system versioned table](../../reference/sql-structure/temporal-tables/system-versioned-tables.md) as of specified timestamp. Argument is interpreted according to the `--tz-utc` setting. Table structures are always dumped as of current timestamp. This option is available from MariaDB 10.7.

#### --character-sets-dir=name

Directory for [character set](../../reference/data-types/string-data-types/character-sets/) files.

#### -i, --comments

Write additional information in the dump file such as program version, server version, and host. Disable with `--skip-comments`.

#### --compact

Give less verbose output (useful for debugging). Disables structure comments and header/footer constructs. Enables the `--skip-add-drop-table`, `--skip-add-locks`, `--skip-comment`s, `--skip-disable-keys`, and `--skip-set-charset` options.

#### --compatible=name

Change the dump to be compatible with a given mode. By default tables are dumped in a format optimized for MariaDB and MySQL. Legal modes are: ansi, `mysql323`, `mysql40`, `postgresql`, `oracle`, `mssql`, `db2`, `maxdb`, `no_key_options`, `no_table_options`, and `no_field_options`. You can use several modes, separated by commas. This option does not guarantee compatibility with other servers. It only enables those SQL mode values that are available for making dump output more compatible. For example, `--compatible=oracle` does not map data types to Oracle types or use Oracle comment syntax.

#### -c, --complete-insert

Use complete [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statements that include column names.

#### -C, --compress

Use compression in server/client protocol. Both client and server must support compression for this to work.

#### --copy-s3-tables

By default, [S3](../../server-usage/storage-engines/s3-storage-engine/) tables are ignored. With this option set, the result file will contain a `CREATE` statement for a similar [Aria](../../server-usage/storage-engines/aria/) table, followed by the table data and ending with an ` ALTER TABLE`` `` `_`table`_` `` ``ENGINE=S3 `.

#### -a, --create-options

Include all MariaDB and/or MySQL specific create options in `CREATE TABLE` statements. Use `--skip-create-options` to disable.

#### -B, --databases

Dump several databases. Normally, `mariadb-dump` treats the first name argument on the command line as a database name and following names as table names. With this option, it treats all name arguments as database names. [CREATE DATABASE](../../reference/sql-statements/data-definition/create/create-database.md) and [USE](../../reference/sql-statements/administrative-sql-statements/use-database.md) statements are included in the output before each new database.

#### -#, --debug\[=#]

If using a debug version of MariaDB, write a debugging log. A typical `debug_options` string is `d:t:o,file_name`. The default value is `d:t:o,/tmp/mysqldump.trace`. If using a non-debug version, `mariadb-dump` will catch this and exit.

#### --debug-check

Check memory and open file usage at exit.

#### --debug-info

Print some debug info at exit.

#### --default-auth=_name_

Default authentication client-side plugin to use.

#### --default-character-set=_name_

Set the default [character set](../../reference/data-types/string-data-types/character-sets/) to _name_. If no character set is specified, `mariadb-dump` uses utf8mb4.

#### --defaults-extra-file=_name_

Read the file _name_ after the global files are read. Must be given as the first argument.

#### --defaults-file=_name_

Only read default options from the given file _name_. Must be given as the first argument.

#### --defaults-group-suffix=_str_

Also read groups with a suffix of _str_. For example, since `mariadb-dump` normally reads the `[client]` and `[mariadb-dump]` (or `[mysqldump]`) groups, `--defaults-group-suffix=`_`x`_ would cause it to also read the groups `[mariadb-dump_`_`x`_`]` (or `[mysqldump_`_`x`_`]`) and `[client_`_`x`_`]`.

#### --delayed-insert

Insert rows with [INSERT DELAYED](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) instead of [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md).

#### --delete-master-logs

On a primary replication server, delete the binary logs by sending a [PURGE BINARY LOGS](../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md) statement to the server after performing the dump operation. This option automatically enables `--master-data=2`.

#### --dir

Parallel dump of multiple databases. Works just like `--tab`, with regard to output (sql file for table definition and tab-separated for data, same options, for example, `--parallel`). It also allows the `--databases` and `--all-databases` options. When `--dir` is used, it creates the directory structure in the output directory pointed to by `--dir`. For every database to be dumped, there is a directory with the database name. All options that `--tab` supports are also supported by `--dir`, in particular `--parallel`. This option is available from MariaDB 11.5.

#### -K, --disable-keys

'` /*!40000 ALTER TABLE`` `` `_`tb_name`_` ``DISABLE KEYS`` `_`/;` and `'/`_` !40000 ALTER TABLE`` `` `_`tb_name`_` `` ``ENABLE KEYS */; ` are written to the output. This makes loading the dump file faster, because the indexes are created after all rows are inserted. This option is effective only for non-unique indexes of MyISAM tables. Disable with `--skip-disable-keys`.

#### --dump-date

If the `--comments` option and this option are given, `mariadb-dump` produces a comment at the end of the dump of the following form: ` -- Dump completed on`` `` `_`date`_. However, the date causes dump files taken at different times to appear to be different, even if the data are otherwise identical. `--dump-date` and `--skip-dump-date` control whether the date is added to the comment. The default is `--dump-date` (include the date in the comment). `--skip-dump-date` suppresses date printing.

#### -H, --dump-history

Dump tables with [history](../../reference/sql-structure/temporal-tables/system-versioned-tables.md). This option is available from MariaDB 10.11. Until this option was introduced, `mariadb-dump` could not read historical rows from versioned tables, and so historical data would not be backed up.

#### --dump-slave\[=value]

Used for producing a dump file from a replica server that can be used to set up another replica server with the same primary. Causes the [binary log](../../server-management/server-monitoring-logs/binary-log/) position and filename of the primary to be appended to the dumped data output. Setting the value to `1` (the default) prints it as a [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command in the dumped data output; if set to `2`, that command is prefixed with a comment symbol. This option will turn on `--lock-all-tables`, unless `--single-transaction` is specified, too (in which case a global read lock is only taken a short time at the beginning of the dump. Make sure to read about `--single-transaction` below). In all cases, any action on logs happens at the exact moment of the dump. This option automatically turns off `--lock-tables`.

{% tabs %}
{% tab title="Current" %}
This option pauses any running SQL threads during the dump.
{% endtab %}

{% tab title="< 10.11" %}
This option stops any running SQL threads before the dump, and restarts **all stopped IO and SQL** threads after completion.
{% endtab %}
{% endtabs %}

#### -E, --events

Include [Event Scheduler events](../../server-usage/triggers-events/event-scheduler/) for the dumped databases in the output.

#### -e, --extended-insert

Use multiple-row [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) syntax that include several values lists. This results in a smaller dump file and speeds up inserts when the file is reloaded. Defaults to `ON`; use `--skip-extended-insert` to disable.

#### --fields-terminated-by=_string_

Fields in the output file are terminated by the given _string_. Used with the `--tab` option and has the same meaning as the corresponding `FIELDS` clause for [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md).

#### --fields-enclosed-by=_character_

Fields in the output file are enclosed by the given _character_. Used with the `--tab` option and has the same meaning as the corresponding `FIELDS` clause for [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md).

#### --fields-optionally-enclosed-by=_character_

Fields in the output file are optionally enclosed by the given _character_. Used with the `--tab` option and has the same meaning as the corresponding `FIELDS` clause for [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md).

#### --fields-escaped-by=_character_

Fields in the output file are escaped by the given _character_. Used with the --tab option and has the same meaning as the corresponding `FIELDS` clause for [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md).

#### --first-slave

Removed in MariaDB 5.5. Use `--lock-all-tables` instead.

#### -F, --flush-logs

Flush the MariaDB server log files before starting the dump. This option requires the [RELOAD privilege](../../reference/sql-statements/account-management-sql-statements/grant.md#reload). If you use this option in combination with the `--databases=` or `--all-databases` option, the logs are flushed for each database dumped. The exception is when using `--lock-all-tables` or `--master-data`: In this case, the logs are flushed only once, corresponding to the moment all tables are locked. If you want your dump and the log flush to happen at the same exact moment, you should use `--flush-logs` together with either `--lock-all-tables` or `--master-data`.

#### --flush-privileges

Send a [FLUSH PRIVILEGES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) statement to the server after dumping the [mysql database](../../reference/system-tables/the-mysql-database-tables/). This option should be used any time the dump contains the mysql database and any other database that depends on the data in the mysql database for proper restoration.

#### -f, --force

Continue even if an SQL error occurs during a table dump.One use for this option is to cause mariadb-dump to continue executing even when it encounters a view that has become invalid because the definition refers to a table that has been dropped. Without `--force` in this example, mariadb-dump exits with an error message. With `--force`, mariadb-dump prints the error message, but it also writes an SQL comment containing the view definition to the dump output and continues executing.

#### --gtid

Used together with `--master-data` and `--dump-slave` to more conveniently set up a new [GTID](../../ha-and-performance/standard-replication/gtid.md) replica. It causes those options to output SQL statements that configure the replica to use the [global transaction ID](../../ha-and-performance/standard-replication/gtid.md) to connect to the primary instead of old-style filename/offset positions. The old-style positions are still included in comments when --gtid is used; likewise the GTID position is included in comments even if `--gtid` is not used.

#### -?, --help

Display a help message and exit.

#### --hex-blob

Dump binary strings in hexadecimal format (for example, ´abc´ becomes 0x616263). The affected data types are [BINARY](../../reference/data-types/string-data-types/binary.md), [VARBINARY](../../reference/data-types/string-data-types/varbinary.md), the [BLOB](../../reference/data-types/string-data-types/blob.md) types, and [BIT](../../reference/data-types/numeric-data-types/bit.md).

#### -h name, --host=_host_

Connect to and dump data from the MariaDB or MySQL server on the given _host_. The default host is `localhost`.

#### --ignore-database=_database_

Do not dump the specified _database_. To specify more than one database to ignore, use the directive multiple times, once for each database. Only takes effect when used together with `--all-databases` or `-A`.

#### --ignore-table=_table_

Do not dump the specified _table_. To specify more than one table to ignore, use the directive multiple times, once for each table. Each table must be specified with both database and table names, for example, `--ignore-table=`_`database.table`_. This option also can be used to ignore views.

#### --ignore-table-data=_table_

Do not dump the specified _table_ data (only the structure). To specify more than one table to ignore, use the directive multiple times, once for each table. Each table must be specified with both database and table names. See also `--no-data`.

#### --include-master-host-port

Add the `MASTER_HOST` and `MASTER_PORT` options for the [CHANGE MASTER TO](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement when using the `--dump-slave` option for a replica dump.

#### --insert-ignore

Insert rows with `INSERT IGNORE` instead of `INSERT`.

#### --lines-terminated-by=_string_

Lines in the output file are terminated by the given _string_. This option is used with the `--tab` option and has the same meaning as the corresponding `LINES` clause for [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md).

#### -x, --lock-all-tables

Lock all tables across all databases. This is achieved by acquiring a global read lock for the duration of the whole dump by executing [FLUSH TABLES WITH READ LOCK](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md). This option automatically turns off\
`--single-transaction` and `--lock-tables`.

#### -l, --lock-tables

For each dumped database, lock all tables to be dumped before dumping them. The tables are locked with `READ LOCAL` to allow concurrent inserts in the case of [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/) tables. For transactional tables such as [InnoDB](../../server-usage/storage-engines/innodb/), `--single-transaction` is a much better option than `--lock-tables` because it does not need to lock the tables at all. Because `--lock-tables` locks tables for each database separately, this option does not guarantee that the tables in the dump file are logically consistent between databases. Tables in different databases may be dumped in completely different states. Use `--skip-lock-tables` to disable.

#### --log-error=_file_

Log warnings and errors by appending them to the named _file_. The default is no logging.

#### --log-queries

When restoring the dump, if logging is turned on, the server logs queries to the general and [slow query log](../../server-management/server-monitoring-logs/slow-query-log/). Defaults to `ON`; use `--skip-log-queries` to disable.

#### --master-data\[=#]

Causes the [binary log](../../server-management/server-monitoring-logs/binary-log/) position and filename to be appended to the output, useful for dumping a primary replication server to produce a dump file that can be used to set up another server as a replica of the primary. These are the primary server coordinates from which the replica should start replicating after you load the dump file into the replica.

If the option is set to `1` (the default), print it as a [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command; if set to `2`, that command is prefixed with a comment symbol. This `--master-data` option turns `--lock-all-tables` on, unless `--single-transaction` is specified, too. In all cases, any action on logs will happen at the exact moment of the dump. This option automatically turns `--lock-tables` off. In all cases, any action on logs happens at the exact moment of the dump. It is also possible to set up a replica by dumping an existing replica of the primary. To do this, use the following procedure on the existing replica:

{% stepper %}
{% step %}
Stop the SQL thread of the replica and get its current status.

```sql
STOP SLAVE SQL_THREAD;
SHOW REPLICA STATUS;
```
{% endstep %}

{% step %}
From the output of the `SHOW REPLICA STATUS` statement, the binary log coordinates of the primary server from which the new replica should start replicating are the values of the `Relay_Master_Log_File` and `Exec_Master_Log_Pos` fields. Denote those values as `file_name` and `file_pos`.
{% endstep %}

{% step %}
Dump the replica server.

```bash
mariadb-dump --master-data=2 --all-databases > dumpfile
```
{% endstep %}

{% step %}
Restart the replica.

```sql
START REPLICA;
```
{% endstep %}

{% step %}
On the new replica, load the dump file.

```
mariadb < dumpfile
```
{% endstep %}

{% step %}
On the new replica, set the replication coordinates to those of the primary server obtained earlier.

```sql
CHANGE MASTER TO 
       MASTER_LOG_FILE = ´file_name´, 
       MASTER_LOG_POS = file_pos;
```

The `CHANGE MASTER TO` statement might also need other parameters, such as `MASTER_HOST` to point the replica to the correct primary server host. Add any such parameters as necessary.
{% endstep %}
{% endstepper %}

#### --max-allowed-packet=\#

The maximum packet length to send to or receive from server. The maximum is 1GB.

#### --max-statement-time=\#

Sets the maximum time any statement can run before being timed out by the server. Default value is `0` (no limit).

#### --net-buffer-length=\#

The initial buffer size for client/server TCP/IP and socket communication. This can be used to limit the size of rows in the dump. When creating multiple-row `INSERT` statements (as with the `--extended-insert` or `--opt` option), `mariadb-dump` creates rows up to `net_buffer_length` length.

#### --no-autocommit

Enclose the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statements for each dumped table within [SET autocommit = 0](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) and [COMMIT](../../reference/sql-statements/transactions/commit.md) statements. `ON` by default from MariaDB 11.8 to allow faster data loading by InnoDB, writing only one undo log for the whole operation.

#### -n, --no-create-db

This option suppresses the [CREATE DATABASE ... IF EXISTS](../../reference/sql-statements/data-definition/create/create-database.md) statement that normally is output for each dumped database if `--all-databases` or `--databases` is given.

#### -t, --no-create-info

Do not write [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statements which re-create each dumped table.

#### -d, --no-data

Do not write any table row information (that is, do not dump table contents). This is useful if you want to dump only the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement for the table (for example, to create an empty copy of the table by loading the dump file). See also `--ignore-table-data`.

#### --no-data-med

Do not dump rows for engines that manage external data (for instance, [MRG\_MyISAM](../../server-usage/storage-engines/merge.md), MRG\_ISAM, [CONNECT](../../server-usage/storage-engines/connect/), [OQGRAPH](../../server-usage/storage-engines/oqgraph-storage-engine/oqgraph-overview.md), [Spider](../../server-usage/storage-engines/spider/), VP, [Federated](../../server-usage/storage-engines/federatedx-storage-engine/)). This option is enabled by default. If you want to dump data for these engines, you need to set `--no-data-med=0`.

#### --no-defaults

Don't read default options from any option file. Must be given as the first argument.

#### -N, --no-set-names

Suppress the `SET NAMES` statement. This has the same effect as `--skip-set-charset`.

#### --opt

This option is shorthand. It is the same as specifying `--add-drop-table`, `--add-locks`, `--create-options`, `--quick`, `--extended-insert`, `--lock-tables`, `--set-charset`, and `--disable-keys`. Enabled by default, disable with `--skip-opt`. It should give you a fast dump operation and produce a dump file that can be reloaded into a MariaDB server quickly. The `--opt` option is enabled by default. Use `--skip-opt` to disable it. See the discussion at the beginning of this section for information about selectively enabling or disabling a subset of the options affected by `--opt`.

#### --order-by-primary

Sorts each table's rows by primary key, or first unique key, if such a key exists. This is useful when dumping a [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/) table to be loaded into an [InnoDB](../../server-usage/storage-engines/innodb/) table, but will make the dump itself take considerably longer.

#### --order-by-size

Dump each table according to their size, smallest first. Useful when using --single-transaction on tables which get truncated/altered often. The assumption here is that smaller tables get truncated more often, and by dumping those first, this reduces the chance that a --single-transaction dump will fail with 'Table definition has changed, please retry transaction'. This option is available from MariaDB 10.9.1.

#### -j, --parallel=\#

Number of dump table jobs executed in parallel (only for use with the `--tab` option). Testing indicates that performance can be increased (dump time decreased) up to 4 times on smaller size dumps, when the database fits into memory. There is a point at which the disk becomes the bottleneck, after which adding more parallel jobs does not bring better performance. From MariaDB 11.4.1.

#### -p\[_password_], --password=_password_

The _password_ to use when connecting to the server. If you use the short option form (`-p`), you cannot have a space between the option and the password. If you omit the password value following the `--password` or `-p` option on the command line, `mariadb-dump` prompts for one. Specifying a password on the command line should be considered insecure. You can use an option file to avoid giving the password on the command line.

#### -W, --pipe

On Windows, connect to the server via a named pipe. This option applies only if the server supports named-pipe connections.

#### --plugin-dir

Directory for client-side plugins.

#### -P _port_, --port=_port_

The TCP/IP _port number_ to use for the connection.

#### --print-defaults

Print the program argument list and exit. Must be given as the first argument.

#### --protocol=name

The connection protocol to use for connecting to the server (`TCP`, `SOCKET`, `PIPE`, `MEMORY`). It is useful when the other connection parameters normally would cause a protocol to be used other than the one you want.

#### -q, --quick

This option is useful for dumping large tables. It forces `mariadb-dump` to retrieve rows for a table from the server a row at a time and to then dump the results directly to stdout rather than retrieving the entire row set and buffering it in memory before writing it out. Defaults to `ON`, use `--skip-quick` to disable.

#### -Q, --quote-names

Quote identifiers (such as database, table, and column names) within backtick (`` ` ``) characters. If the `ANSI_QUOTES` SQL mode is enabled, identifiers are quoted with (`"`) characters. This option is enabled by default. It can be disabled with `--skip-quote-names`, but this option should be given after any option such as `--compatible` that may enable `--quote-names`.

#### --replace

Use [REPLACE INTO](../../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md) statements instead of [INSERT INTO](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statements.

#### -r, --result-file=_file_

Direct output to a given _file_. This option should be used on Windows, to prevent newline (`\n`) characters from being converted to `\r\n` carriage return/newline sequences. The result file is created and its previous contents overwritten, even if an error occurs while generating the dump.

#### -R, --routines

Include stored routines ([procedures](../../server-usage/stored-routines/stored-procedures/) and [functions](../../server-usage/stored-routines/stored-functions/)) for the dumped databases in the output. Use of this option requires the SELECT privilege for the [mysql.proc](../../reference/system-tables/the-mysql-database-tables/mysql-proc-table.md) table. The output generated using --routines contains [CREATE PROCEDURE](../../server-usage/stored-routines/stored-procedures/create-procedure.md) and [CREATE FUNCTION](../../reference/sql-statements/data-definition/create/create-function.md) statements to re-create the routines. However, these statements do not include attributes such as the routine creation and modification timestamps. This means that when the routines are reloaded, they are created with the timestamps equal to the reload time.If you require routines to be re-created with their original timestamp attributes, do not use `--routines`. Instead, dump and reload the contents of the [mysql.proc](../../reference/system-tables/the-mysql-database-tables/mysql-proc-table.md) table directly, using a MariaDB account which has appropriate privileges for the mysql database.

#### --set-charset

Add `'SET NAMES default_character_set'` to the output in order to set the [character set](../../reference/data-types/string-data-types/character-sets/). Enabled by default; suppress with `--skip-set-charset`.

#### -O, --set-variable=_variable_

Change the value of a _variable_. This option is deprecated; you can set variables directly with `--`_`variable-name`_`=`_`value`_.

#### --shared-memory-base-name

Shared-memory name to use for Windows connections using shared memory to a local server (started with the `--shared-memory` option). Case-sensitive. Defaults to `MYSQL`.

#### --single-transaction

This option sends a [START TRANSACTION](../../reference/sql-statements/transactions/start-transaction.md) SQL statement to the server before dumping data. It is useful only with transactional tables such as [InnoDB](../../server-usage/storage-engines/innodb/), because then it dumps the consistent state of the database at the time when `BEGIN` was issued, without blocking any applications. When using this option, you should keep in mind that only InnoDB tables are dumped in a consistent state. The single-transaction feature depends not only on the engine being transactional and capable of `REPEATABLE-READ`, but also on `START TRANSACTION WITH CONSISTENT SNAPSHOT`. The dump is not guaranteed to be consistent for other storage engines. For example, any [TokuDB](../../server-usage/storage-engines/legacy-storage-engines/tokudb/), [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/) or [MEMORY](../../server-usage/storage-engines/memory-storage-engine.md) tables dumped while using this option may still change state. While a `--single-transaction` dump is in process, to ensure a valid dump file (correct table contents and binary log coordinates), no other connection should use the following statements: [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/), [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md), [DROP TABLE](../../reference/sql-statements/data-definition/drop/drop-table.md), [RENAME TABLE](../../reference/sql-statements/data-definition/rename-table.md), or [TRUNCATE TABLE](../../reference/sql-statements/table-statements/truncate-table.md). A consistent read is not isolated from those statements, so use of them on a table to be dumped can cause the `SELECT` (performed by mariadb-dump to retrieve the table contents) to obtain incorrect contents or fail. The `--single-transaction` option and the `--lock-tables` option are mutually exclusive, because [LOCK TABLES](../../reference/sql-statements/transactions/lock-tables.md) causes any pending transactions to be committed implicitly. So this option automatically turns off `--lock-tables`. To dump large tables, you should combine the `--single-transaction` option with `--quick`.

#### --skip-add-locks

Disable the `--add-locks` option.

#### --skip-comments

Disable the `--comments` option.

#### --skip-disable-keys

Disable the `--disable-keys` option.

#### --skip-extended-insert

Disable the `--extended-insert` option.

#### --skip-opt

Disable the `--opt` option (disables `--add-drop-table`, `--add-locks`, `--create-options`, `--quick`, `--extended-insert`, `--lock-tables`, `--set-charset`, and `--disable-keys`).

#### --skip-quick

Disable the `--quick` option.

#### --skip-quote-name

Disable the `--quote-names` option.

#### --skip-set-charset

Disable the `--set-charset` option.

#### --skip-triggers

Disable the `--triggers` option.

#### --skip-tz-utc

Disable the `--tz-utc` option.

#### -S name, --socket={_socket|named-pipe}_

For connections to localhost, the Unix _socket file_ to use, or, on Windows, the name of the _named pipe_ to use.

#### --ssl

Enables [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). TLS is also enabled even without setting this option when certain other TLS options are set. The `--ssl` option does not enable [verifying the server certificate](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, the user must specify the `--ssl-verify-server-cert` option.

#### --ssl-ca=_pem-file_

Defines a path to a _PEM file_ that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option implies the `--ssl` option.

#### --ssl-capath=_pem-directory_

Defines a _path to a directory that contains one or more PEM files_ that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option is only supported if the client was built with OpenSSL or yaSSL. If the client was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. This option implies the `--ssl` option.

#### --ssl-cert=_certificate-file_

Defines a path to the _X509 certificate file_ to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the `--ssl` option.

#### --ssl-cipher=_cipher-list_

_List of permitted ciphers_ or cipher suites to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option implies the `--ssl` option.

#### --ssl-crl=_pem-file_

Defines a _path to a PEM file_ that should contain one or more revoked X509 certificates to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL or Schannel. If the client was built with yaSSL or GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

#### --ssl-crlpath=_pem-directory_

Defines a _path to a directory that contains one or more PEM files_ that should each contain one revoked X509 certificate to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL. If the client was built with yaSSL, GnuTLS, or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

#### --ssl-key=_private-key_

Defines a _path to a private key file_ to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the `--ssl` option.

#### --ssl-verify-server-cert

Enables [server certificate verification](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default.

#### --system=_option_\[,_option_]]

Dump the database's system tables in a logical form. With this option, the [mysql database](../../reference/system-tables/the-mysql-database-tables/) tables are dumped as [CREATE USER](../../reference/sql-statements/account-management-sql-statements/create-user.md), [CREATE SERVER](../../reference/sql-statements/data-definition/create/create-server.md) and other forms of logical portable SQL statements. The option values here are from the set of `all`, `users`, `plugins`, `udfs`, `servers`, `stats`, `timezones`.

#### -T, --tab=_name_

Produce tab-separated text-format data files. With this option, for each dumped table, `mariadb-dump` creates a `tbl_name.sql` file containing the `CREATE TABLE` statement that creates the table, and a `tbl_name.txt` file containing the table's data. The option value is the directory in which to write the files. Note: This option can only be used when `mariadb-dump` is run on the same machine as the `mariadbd` server. You must have the `FILE` privilege, and the server must have permission to write files in the directory that you specify. By default, the `.txt` data files are formatted using tab characters between column values, and a newline at the end of each line. The format can be specified explicitly using the `--fields-`_`xxx`_ and `--lines-terminated-by` options. Column values are converted to the character set specified by the `--default-character-set` option.

#### --tables

This option overrides the `--databases` (`-B`) option. `mariadb-dump` regards all name arguments following the option as table names.

#### --tls-version=_protocol_

This option accepts a _comma-separated list of TLS protocol versions_. A TLS protocol version will only be enabled if it is present in this list. All other TLS protocol versions will not be permitted. See [Secure Connections Overview: TLS Protocol Versions](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#tls-protocol-versions) for more information.

#### --triggers

Include [triggers](../../server-usage/triggers-events/triggers/) for each dumped table in the output. This option is enabled by default; disable it with `--skip-triggers`.

#### --tz-utc

This option enables [TIMESTAMP](../../reference/data-types/date-and-time-data-types/timestamp.md) columns to be dumped and reloaded between servers in different time zones. mariadb-dump sets its connection time zone to UTC and adds `SET TIME_ZONE=´+00:00´` to the dump file. Without this option, `TIMESTAMP` columns are dumped and reloaded in the time zones local to the source and destination servers, which can cause the values to change if the servers are in different time zones. `--tz-utc` also protects against changes due to daylight saving time. `--tz-utc` is enabled by default. To disable it, use `--skip-tz-utc`.

#### -u _username_, --user=_username_

The MariaDB _user name_ to use when connecting to the server.

#### -v, --verbose

Verbose mode. Print more information about what the program is doing during various stages.

#### -V, --version

Output version information and exit.

#### -w _condition_, --where=_condition_

Dump only rows selected by the given _`WHERE` condition_. Quotes around the condition are mandatory if it contains spaces or other characters that are special to your command interpreter. Example:\
`--where="user = ´jimf´" -w"userid > 1" -w"userid < 1"` .

#### -L, --wildcards

Usage of wildcards in the table/database name. Without the `--databases` option, wildcards can be used only in tables names. From [MariaDB 12.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1).

#### -X, --xml

Dump a database as well-formed XML.

### Group Options

Some `mariadb-dump` options are shorthand for groups of other options:

* Use of `--opt` is the same as specifying`--add-drop-table`, `--add-locks`,`--create-options`, `--disable-keys`,`--extended-insert`, `--lock-tables`,`--quick`, and `--set-charset`. All of the\
  options that `--opt` stands for also are on by default because `--opt` is on by default.
* Use of `--compact` is the same as specifying`--skip-add-drop-table`,`--skip-add-locks`, `--skip-comments`,`--skip-disable-keys`, and`--skip-set-charset` options.

To reverse the effect of a group option, uses its `--skip-xxx` form (`--skip-opt` or `--skip-compact`). It\
is also possible to select only part of the effect of a group option by following it with options that enable or disable specific features. Here are some examples:

* To select the effect of `--opt` except for some features, use the `--skip` option for each feature. To disable extended inserts and memory buffering, use `--opt--skip-extended-insert` `--skip-quick`.\
  (Actually, `--skip-extended-insert--skip-quick` is sufficient because`--opt` is on by default.)
* To reverse `--opt` for all features except index disabling and table locking, use `--skip-opt--disable-keys` `--lock-tables`.

When you selectively enable or disable the effect of a group option, the order is important, because options are processed first to last. For example,`--disable-keys` `--lock-tables--skip-opt` would not have the intended effect; it is the same as `--skip-opt` by itself.

### Special Characters in Option Values

Some options, like `--lines-terminated-by`, accept a string. The string can be quoted, if necessary. For example, on Unix systems this is the option to enclose fields within double quotes:

```
--fields-enclosed-by='"'
```

An alternative is to specify the hexadecimal value of a character. For example, the following syntax works on any platform:

```
--fields-enclosed-by=0x22
```

## Option Files

In addition to reading options from the command line, `mariadb-dump` can also read options from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadb-dump` in an option file, then it is ignored.

The following options relate to how MariaDB command line tools handles option files. They must be given as the first argument on the command line:

| Option                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| --print-defaults          | Print the program argument list and exit.                                           |
| --no-defaults             | Don't read default options from any option file.                                    |
| --defaults-file=#         | Only read default options from the given file #.                                    |
| --defaults-extra-file=#   | Read this file after the global files are read.                                     |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |

`mariadb-dump` is linked with [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/mariadb-connector-c-guide). However, MariaDB Connector/C does not handle the parsing of option files for this client. That is performed by the server option file parsing code. See [MDEV-19035](https://jira.mariadb.org/browse/MDEV-19035) for more information.

#### Option Groups

`mariadb-dump` reads options from the following [option groups](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group             | Description                                                                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[mysqldump]      | Options read by mariadb-dump, which includes both MariaDB Server and MySQL Server.                                                                                              |
| \[mariadb-dump]   | Options read by `mariadb-dump`.                                                                                                                                                 |
| \[client]         | Options read by all MariaDB and MySQL client programs, which includes both MariaDB and MySQL clients. For example, mysqldump.                                                   |
| \[client-server]  | Options read by all MariaDB [client programs](../) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[client-mariadb] | Options read by all MariaDB client programs.                                                                                                                                    |

## NULL, ´NULL´, and Empty Values in XML

For a column named `column_name`, the `NULL` value, an empty string, and the string value `´NULL´` are distinguished from one another in the output generated by this option as follows.

| Value                   | XML Representation                            |
| ----------------------- | --------------------------------------------- |
| `NULL` (unknown value)  | `<field name="column_name" xsi:nil="true" />` |
| `''` (empty string)     | `<field name="column_name"></field>`          |
| `'NULL'` (string value) | `<field name="column_name">NULL</field>`      |

The output from the mariadb client when run using the `--xml` option also follows the preceding rules.

XML output from mariadb-dump includes the XML namespace, as shown here :

```xml
shell> mariadb-dump --xml -u root world City
<?xml version="1.0"?>
<mariadb-dump xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<database name="world">
<table_structure name="City">
<field Field="ID" Type="int(11)" Null="NO" Key="PRI" Extra="auto_increment" />
<field Field="Name" Type="char(35)" Null="NO" Key="" Default="" Extra="" />
<field Field="CountryCode" Type="char(3)" Null="NO" Key="" Default="" Extra="" />
<field Field="District" Type="char(20)" Null="NO" Key="" Default="" Extra="" />
<field Field="Population" Type="int(11)" Null="NO" Key="" Default="0" Extra="" />
<key Table="City" Non_unique="0" Key_name="PRIMARY" Seq_in_index="1" Column_name="ID"
Collation="A" Cardinality="4079" Null="" Index_type="BTREE" Comment="" />
<options Name="City" Engine="MyISAM" Version="10" Row_format="Fixed" Rows="4079"
Avg_row_length="67" Data_length="273293" Max_data_length="18858823439613951"
Index_length="43008" Data_free="0" Auto_increment="4080"
Create_time="2007-03-31 01:47:01" Update_time="2007-03-31 01:47:02"
Collation="latin1_swedish_ci" Create_options="" Comment="" />
</table_structure>
<table_data name="City">
<row>
<field name="ID">1</field>
<field name="Name">Kabul</field>
<field name="CountryCode">AFG</field>
<field name="District">Kabol</field>
<field name="Population">1780000</field>
</row>
...
<row>
<field name="ID">4079</field>
<field name="Name">Rafah</field>
<field name="CountryCode">PSE</field>
<field name="District">Rafah</field>
<field name="Population">92020</field>
</row>
</table_data>
</database>
</mariadb-dump>
```

## Restoring Dumps

To restore a backup created with `mariadb-dump`, use the \[mariadb client]\(../mariadb-client/mariadb-command line-client.md) to import the dump:

```bash
mariadb db_name < backup-file.sql
```

## Variables

You can also set the following variables (`--variable-name=value`) and boolean options `{FALSE|TRUE}` by using:

| Name                          | Default Values                                |
| ----------------------------- | --------------------------------------------- |
| all                           | TRUE                                          |
| all-databases                 | FALSE                                         |
| all-tablespaces               | FALSE                                         |
| no-tablespaces                | FALSE                                         |
| add-drop-database             | FALSE                                         |
| add-drop-table                | TRUE                                          |
| add-drop-trigger              | FALSE                                         |
| add-locks                     | TRUE                                          |
| allow-keywords                | FALSE                                         |
| apply-slave-statements        | FALSE                                         |
| as-of                         | (No default value)                            |
| character-sets-dir            | (No default value)                            |
| comments                      | TRUE                                          |
| compatible                    | (No default value)                            |
| compact                       | FALSE                                         |
| complete-insert               | FALSE                                         |
| compress                      | FALSE                                         |
| copy-s3-tables                | FALSE                                         |
| create-options                | TRUE                                          |
| databases                     | FALSE                                         |
| debug-check                   | FALSE                                         |
| debug-info                    | FALSE                                         |
| default-character-set         | utf8mb4                                       |
| delayed-insert                | FALSE                                         |
| delete-master-logs            | FALSE                                         |
| disable-keys                  | TRUE                                          |
| events                        | FALSE                                         |
| extended-insert               | TRUE                                          |
| fields-terminated-by          | (No default value)                            |
| fields-enclosed-by            | (No default value)                            |
| fields-optionally-enclosed-by | (No default value)                            |
| fields-escaped-by             | (No default value)                            |
| flush-logs                    | FALSE                                         |
| flush-privileges              | FALSE                                         |
| force                         | FALSE                                         |
| hex-blob                      | FALSE                                         |
| host                          | (No default value)                            |
| include-master-host-port      | FALSE                                         |
| insert-ignore                 | FALSE                                         |
| lines-terminated-by           | (No default value)                            |
| lock-all-tables               | FALSE                                         |
| lock-tables                   | TRUE                                          |
| log-error                     | (No default value)                            |
| log-queries                   | TRUE                                          |
| master-data                   | 0                                             |
| max\_allowed\_packet          | 16777216                                      |
| net-buffer-length             | 1046528                                       |
| no-autocommit                 | TRUE (> MariaDB 11.7), FALSE (< MariaDB 11.8) |
| no-create-db                  | FALSE                                         |
| no-create-info                | FALSE                                         |
| no-data                       | FALSE                                         |
| no-data-med                   | TRUE                                          |
| order-by-primary              | FALSE                                         |
| port                          | 0                                             |
| quick                         | TRUE                                          |
| quote-names                   | TRUE                                          |
| replace                       | FALSE                                         |
| routines                      | FALSE                                         |
| set-charset                   | TRUE                                          |
| single-transaction            | FALSE                                         |
| dump-date                     | TRUE                                          |
| socket                        | No default value)                             |
| ssl                           | FALSE                                         |
| ssl-ca                        | (No default value)                            |
| ssl-capath                    | (No default value)                            |
| ssl-cert                      | (No default value)                            |
| ssl-cipher                    | (No default value)                            |
| ssl-key                       | (No default value)                            |
| ssl-verify-server-cert        | FALSE                                         |
| system                        | (No default value)                            |
| tab                           | (No default value)                            |
| triggers                      | TRUE                                          |
| tz-utc                        | TRUE                                          |
| user                          | (No default value)                            |
| verbose                       | FALSE                                         |
| where                         | (No default value)                            |
| plugin-dir                    | (No default value)                            |
| default-auth                  | (No default value)                            |

## Examples

A common use of `mariadb-dump` is making a backup of an entire database:

```bash
shell> mariadb-dump db_name > backup-file.sql
```

You can load the dump file back into the server like this:

```bash
shell> mariadb db_name < backup-file.sql
```

Or like this:

```bash
shell> mariadb -e "source /path-to-backup/backup-file.sql" db_name
```

`mariadb-dump` is also very useful for populating databases by copying data from one MariaDB server to another:

```bash
shell> mariadb-dump --opt db_name | mariadb --host=remote_host -C db_name
```

It is possible to dump several databases with one command:

```bash
shell> mariadb-dump --databases db_name1 [db_name2 ...] > my_databases.sql
```

To dump all databases, use the `--all-databases` option:

```bash
shell> mariadb-dump --all-databases > all_databases.sql
```

For InnoDB tables, `mariadb-dump` provides a way of making an online backup:

```bash
shell> mariadb-dump --all-databases --single-transaction all_databases.sql
```

This backup acquires a global read lock on all tables (using`FLUSH TABLES WITH READ LOCK`) at the beginning of the dump. As soon as this lock has been acquired, the binary log coordinates are read and the lock is released. If long updating statements are running when the `FLUSH` statement is issued, the MariaDB server may get stalled until those statements finish. After that, the dump becomes lock free and does not disturb reads and writes on the tables. If the update statements that the MariaDB server receives are short (in terms of execution time), the initial lock period should not be noticeable, even with many updates.

For point-in-time recovery (also known as “roll-forward,” when you need to restore an old backup and replay the changes that happened since that backup), it is often useful to rotate the [binary log](../../server-management/server-monitoring-logs/binary-log/) or at least know the binary log coordinates to which the dump corresponds:

```bash
shell> mariadb-dump --all-databases --master-data=2 > all_databases.sql
```

Or:

```bash
shell> mariadb-dump --all-databases --flush-logs --master-data=2 > all_databases.sql
```

The `--master-data` and `--single-transaction` options can be used simultaneously, which provides a convenient way to make an online backup suitable for use prior to point-in-time recovery if tables are\
stored that use the InnoDB storage engine.

## See Also

* [mariadb-backup](../../server-usage/backup-and-restore/mariadb-backup/)
* [MariaDB point-in-time recovery](https://www.youtube.com/watch?v=ezHmnNmmcDo) (video)
* [MariaDB Enterprise Backup](../../server-usage/backup-and-restore/backup-and-restore-with-mariadb-enterprise-server/mariadb-enterprise-backup.md)
* [Upgrading to a newer major version of MariaDB](https://www.youtube.com/watch?v=1kLIXN2DoEo) (video)
* [MariaDB dump file compatibility change](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/manual-sst-of-galera-cluster-node-with-mariadb-backup) (blog, 2024)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
