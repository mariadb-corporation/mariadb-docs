# Heuristic Recovery with the Transaction Coordinator Log

The transaction coordinator log (tc\_log) is used to coordinate transactions that affect multiple [XA-capable](../../../reference/sql-statements/transactions/xa-transactions.md) [storage engines](../../../server-usage/storage-engines/). One of the main purposes of this log is in crash recovery.

## Modes of Crash Recovery

There are two modes of crash recovery:

* Automatic crash recovery.
* Manual heuristic recovery when [--tc-heuristic-recover](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) is set to some value other than `OFF`.

## Automatic Crash Recovery

Automatic crash recovery occurs during startup when MariaDB needs to recover from a crash and [--tc-heuristic-recover](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) is set to `OFF`, which is the default value.

### Automatic Crash Recovery with the Binary Log-Based Transaction Coordinator Log

If MariaDB needs to perform automatic crash recovery and if the [binary log](../binary-log/) is enabled, then the [error log](../error-log.md) will contain messages like this:

```
[Note] Recovering after a crash using cmdb-mariadb-0-bin
[Note] InnoDB: Buffer pool(s) load completed at 190313 11:24:29
[Note] Starting crash recovery...
[Note] Crash recovery finished.
```

### Automatic Crash Recovery with the Memory-Mapped File-Based Transaction Coordinator Log

If MariaDB needs to perform automatic crash recovery and if the [binary log](../binary-log/) is **not** enabled, then the [error log](../error-log.md) will contain messages like this:

```
[Note] Recovering after a crash using tc.log
[Note] InnoDB: Buffer pool(s) load completed at 190313 11:26:32
[Note] Starting crash recovery...
[Note] Crash recovery finished.
```

## Manual Heuristic Recovery

Manual heuristic recovery occurs when [--tc-heuristic-recover](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) is set to some value other than `OFF`. This might be needed if the server finds prepared transactions during crash recovery that are not in the transaction coordinator log. For example, the [error log](../error-log.md) might contain an error like this:

```sql
[ERROR] Found 1 prepared transactions! It means that mysqld was not shut down properly last time and critical recovery information (last binlog or tc.log file) was manually deleted after a crash. You have to start mysqld with --tc-heuristic-recover switch to commit or rollback pending transactions.
```

When manual heuristic recovery is initiated, MariaDB will ignore information about transactions in the transaction coordinator log during the recovery process. Prepared transactions that are encountered during the recovery process will either be rolled back or committed, depending on the value of [--tc-heuristic-recover](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md).

When manual heuristic recovery is initiated, the [error log](../error-log.md) will contain a message like this:

```
[Note] Heuristic crash recovery mode
```

### Manual Heuristic Recovery with the Binary Log-Based Transaction Coordinator Log

If [--tc-heuristic-recover](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) is set to some value other than `OFF` and if the [binary log](../binary-log/) is enabled, then MariaDB will ignore information about transactions in the [binary log](../binary-log/) during the recovery process. Prepared transactions that are encountered during the recovery process will either be rolled back or committed, depending on the value of [--tc-heuristic-recover](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md).

After the recovery process is complete, MariaDB will create a new empty [binary log](../binary-log/) file, so that the old corrupt ones can be ignored.

### Manual Heuristic Recovery with the Memory-Mapped File-Based Transaction Coordinator Log

If [--tc-heuristic-recover](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) is set to some value other than `OFF` and if the [binary log](../binary-log/) is **not** enabled, then MariaDB will ignore information about transactions in the memory-mapped file defined by the [--log-tc](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option during the recovery process. Prepared transactions that are encountered during the recovery process will either be rolled back or committed, depending on the value of [--tc-heuristic-recover](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
