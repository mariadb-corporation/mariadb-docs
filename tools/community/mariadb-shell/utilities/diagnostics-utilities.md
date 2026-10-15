---
description: >-
  The util.debug collectors of MariaDB Shell, which package server, shell,
  and host information from MariaDB Server or MySQL Server into a ZIP file
  for troubleshooting and support requests.
---

# Diagnostics Utilities

The `util.debug` object provides three collectors that gather diagnostic information into one ZIP file, for troubleshooting or for attaching to a support request. They work with MariaDB Server and with MySQL Server, and adapt what they collect to the server they're connected to.

| Function | Purpose |
| --- | --- |
| `util.debug.collect_diagnostics()` | A one-time snapshot of the server configuration, status, and schema statistics. |
| `util.debug.collect_high_load_diagnostics()` | Repeated snapshots of performance metrics over a period, for a server that is under heavy load. |
| `util.debug.collect_slow_query_diagnostics()` | Runs one query and collects its execution plan, optimizer trace, and the performance metrics during its execution. |

The details on this page come from the built-in help (`\? util.debug`) and the source of the `debug` plugin.

## Common Behavior

* The collectors need an open global session to MariaDB Server 10.6 or newer, or to MySQL Server 5.7 or newer. Each one opens its own session with the same connection options.
* `path` is the ZIP file to create. If it doesn't end in `.zip`, the extension is added. If it ends in `/` (or `\` on Windows), a file named `mysql-diagnostics-<date>-<time>.zip` is created in that directory. An existing file is never overwritten.
* The ZIP file is created with mode `rw-------` on systems with POSIX permissions, because it can contain configuration details and query text. All entries are stored under one top-level directory named after the file.
* If anything fails during collection, the ZIP file is deleted. The `ignoreErrors` option of `collect_diagnostics()` turns a failing diagnostic query into an `.error` file in the ZIP instead.
* When the session connects to `localhost`, the collectors can also run operating system commands on the database host (the `hostInfo` and `customShell` options). Over TCP to any other host name, including `127.0.0.1`, host information is not collected and `customShell` is refused.

{% hint style="info" %}
MariaDB Server starts with `performance_schema=OFF`; MySQL Server starts with it on. With it off, the collectors still run, but they print a warning and skip everything that comes from the Performance Schema and the `sys` schema: statement, wait, I/O and memory statistics, and the metric deltas of the high load and slow query collectors. Turn it on (`performance_schema=ON` in the server configuration, which needs a restart) before collecting from a MariaDB server you're investigating.
{% endhint %}

The connected account needs broad read access, and `EXECUTE`, `SELECT`, and `CREATE TEMPORARY TABLES` on `sys.*`. On `*.*`, the minimal accounts in the test suite of the collectors have:

| Server | Privileges on `*.*` |
| --- | --- |
| MariaDB Server | `SELECT`, `PROCESS`, `BINLOG MONITOR`, `REPLICATION SLAVE`, `REPLICA MONITOR`, `REPLICATION MASTER ADMIN` |
| MySQL Server | `SELECT`, `PROCESS`, `REPLICATION CLIENT`, `REPLICATION SLAVE` |

A `pfsInstrumentation` value other than `current` also needs the right to update the Performance Schema setup tables. When the binary log is on with a `binlog_format` other than `ROW` (MariaDB Server's default is `MIXED`), the high load and slow query collectors switch `sql_log_bin` off in their session so that the temporary tables of the `sys` procedures they call aren't replicated. That needs `BINLOG ADMIN` on MariaDB Server, and `SYSTEM_VARIABLES_ADMIN` or `SUPER` on MySQL Server. Without it, they print a warning and go on with logging left on on MariaDB Server, and stop on MySQL Server.

## collect\_diagnostics()

```python
util.debug.collect_diagnostics(path[, options])
```

Collects one snapshot of:

* The shell version, the shell options, the host name of the client, and the MariaDB Shell log file.
* Server identity and time settings, global variables, and the error log. See [Server Information](#server-information).
* InnoDB status and metrics, lock information, and the Performance Schema configuration.
* Replication status.
* Schema statistics: tables without a primary key, unused indexes, and stored routine sizes. With `schemaStats`, also the 20 largest tables with their indexes, the tables per storage engine, and all of `information_schema.TABLES`.
* Optionally, the slow query log, and host information.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `schemaStats` | Boolean | `false` | Also collect the full schema statistics. |
| `slowQueries` | Boolean | `false` | Also collect slow query information. Requires `slow_query_log=ON` and `log_output=TABLE`. |
| `innodbMutex` | Boolean | `false` | Also collect `SHOW ENGINE INNODB MUTEX`. This statement can affect the performance of a busy server. |
| `ignoreErrors` | Boolean | `false` | Continue when a diagnostic query fails. |
| `hostInfo` | Boolean | `true` | On `localhost`, run operating system diagnostic commands. See [Host Information](#host-information). |
| `customSql` | list of strings | `[]` | Additional SQL statements to run. Each result is stored in the ZIP file. |
| `customShell` | list of strings | `[]` | Additional operating system commands to run. Only on `localhost`. |
| `allMembers` | Boolean | `false` | Collect from every member of a MySQL InnoDB Cluster. The collector prompts for the password of the account. On a server that isn't an InnoDB Cluster member, including any MariaDB server, the option has no effect and the collector reports that no cluster metadata was found. |

## collect\_high\_load\_diagnostics()

```python
util.debug.collect_high_load_diagnostics(path[, options])
```

Collects general information once, then collects performance metrics several times with a pause in between, so that you can compare the snapshots. The general information includes the shell options, schema statistics, stored routine statistics, the process list, open tables, the error log, slow queries, and the time that a fixed `SELECT BENCHMARK()` loop takes on the server. Each iteration collects InnoDB status, lock, buffer pool, and transaction information, and Performance Schema metrics.

With the defaults, the collection takes about five minutes: two iterations with a pause of 300 seconds.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `iterations` | integer | `2` | Number of metric snapshots. |
| `delay` | integer | `300` | Seconds to wait between snapshots. |
| `pfsInstrumentation` | string | `current` | `current` leaves the Performance Schema configuration as it is. `medium` enables all consumers except the history consumers, and all instruments except `wait/synch/%`. `full` enables all consumers and instruments. The original configuration is restored at the end. More instrumentation gives more detail, at a cost in server performance. |
| `innodbMutex` | Boolean | `false` | Also collect `SHOW ENGINE INNODB MUTEX`. |
| `hostInfo` | Boolean | `true` | On `localhost`, run operating system diagnostic commands. |
| `customSql` | list of strings | `[]` | Additional SQL statements. Prefix a statement with `before:` (the default), `during:`, or `after:` to run it once before the first snapshot, once in each snapshot, or once after the last snapshot. |
| `customShell` | list of strings | `[]` | Additional operating system commands, with the same prefixes as `customSql`. Only on `localhost`. |

## collect\_slow\_query\_diagnostics()

```python
util.debug.collect_slow_query_diagnostics(path, query[, options])
```

Runs `query` once in a separate session, collects metrics in the background while it runs, and adds the following to what `collect_high_load_diagnostics()` collects:

* The `EXPLAIN` and `EXPLAIN FORMAT=JSON` output of the query, and the optimizer trace of the `EXPLAIN`.
* The plan with actual row counts and timings of every step (file `explain_analyze.tsv`). It comes from `ANALYZE FORMAT=JSON` on MariaDB Server, only for a `SELECT` or `WITH` query, and from `EXPLAIN ANALYZE` on MySQL Server 8.0.18 or newer. Both run the query.
* The DDL and statistics of every table that the query references.
* The execution time, the fetch time, the number of rows, and the warnings of the query.

The query really runs, twice: once for the profiled execution and once for the plan with actual timings. Don't pass a statement that changes data unless you intend to change it.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `delay` | integer | `15` | Seconds between the background metric snapshots while the query runs. |
| `pfsInstrumentation` | string | `current` | As for `collect_high_load_diagnostics()`. |
| `innodbMutex` | Boolean | `false` | Also collect `SHOW ENGINE INNODB MUTEX`. |
| `hostInfo` | Boolean | `true` | On `localhost`, run operating system diagnostic commands. |
| `customSql` | list of strings | `[]` | Additional SQL statements, with the `before:`, `during:`, and `after:` prefixes. |
| `customShell` | list of strings | `[]` | Additional operating system commands, with the same prefixes. Only on `localhost`. |

## Server Information

Every collector writes these files for the server it's connected to. The statements behind them differ between the two servers:

* `instance`: host name, port, server ID, version, the server's UTC and local time, time zones, the `sys` schema version, and whether the Performance Schema is on. On MySQL Server it also has the server UUID; MariaDB Server has none.
* `global_variables.tsv`: all global variables. MariaDB Server's come from `information_schema.GLOBAL_VARIABLES`. MySQL Server's come from the Performance Schema, and from 8.0 on they include where each value was set.
* The binary log and replication state, with the `replication_*` tables of the Performance Schema:

  | Server | Files |
  | --- | --- |
  | MariaDB Server | `SHOW_BINARY_LOGS.tsv`, `SHOW_BINLOG_STATUS.tsv`, `SHOW_REPLICA_HOSTS.tsv`, and `SHOW_ALL_REPLICAS_STATUS.tsv`, with every connection of a multi-source replica |
  | MySQL Server | `SHOW_BINARY_LOGS.tsv`, `SHOW_BINARY_LOG_STATUS.tsv`, `SHOW_REPLICAS.tsv`, and `SHOW_REPLICA_STATUS.tsv` (older spellings before 8.2 and 8.0.23), plus the `mysql.slave_master_info` table with the password masked, and `mysql.slave_relay_log_info` |

* Prepared XA transactions, from `XA RECOVER FORMAT='SQL'` on MariaDB Server and `XA RECOVER CONVERT xid` on MySQL Server.
* `error_log`: on `localhost`, a copy of the file that `log_error` names. Over TCP, MySQL Server 8.0.22 or newer serves it from `performance_schema.error_log`, without lines that hold a temporary password. MariaDB Server has no such table, so over TCP the error log isn't collected and the collector asks you to include the file yourself. The same happens when `log_error` is empty and the server logs to its standard error.

A statement that fails with an error, for example a `SHOW` statement that the account has no privilege for, leaves an `.error` file with the error message in place of the result.

## Host Information

With `hostInfo` enabled and a session to `localhost`, the collectors run a fixed set of commands and store their output:

* **Linux:** system and kernel information (`uname`, `lsb_release`, `/proc/cpuinfo`, `/proc/meminfo`), memory, swap, and NUMA statistics, mounts and disks (`df`, `lsblk`, LVM commands), CPU, I/O, and memory sampling over a few seconds (`mpstat`, `iostat`, `vmstat`, `top`), the process list, `sysctl -a`, kernel messages, and `sudo sosreport`. The `sudo` command can prompt for your password.
* **macOS:** `uname`, mounts and disks, `iostat`, `top`, the process list, resource limits, kernel messages, and listening sockets.
* **Windows:** `systeminfo` and an `msinfo32` report.

Commands that aren't installed or aren't permitted record their error and don't stop the collection.

## Command Line Use

All three collectors support [command line integration](../using-mariadb-shell/command-line-integration.md):

```sh
mariadb-shell admin@db1.example.com -- util debug collect-diagnostics /tmp/diag.zip --schema-stats=true
```
