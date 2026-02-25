---
description: >-
  Instructions for enabling the binary log using the --log-bin option and
  configuring the log file basename and index file.
---

# Activating the Binary Log

## Turning on Binary Logging

To enable binary logging, start the server with the [--log-bin](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin) option. Alternatively, add this to the [configuration file](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) (for instance, `my.cnf`), then restart the server:

```ini
[client-server]
log_bin
```

Optionally, you can specify a **basename** (with or without a path). If you don't, MariaDB assigns a default basename (for instance, `c525d37c-b2ff-4543-b06f-87012d142d44-bin)`, derived from the UUID or hostname of the computer the server runs on. To the basename, file extensions are added, determining the nature of the log files. See [this section](activating-the-binary-log.md#log-file-organization) for details.

{% include "../../../.gitbook/includes/innodb-based-binlog-from-12.3.md" %}

On server start, you can set a basename (in the example, with a path) like this:

```bash
mariadbd --log-bin=/var/log/mariadb/mariadb-logs
```

The following applies:

* If you specify a binary log basename with an extension (for example `.log`), the extension is silently ignored.
* If you don't specify a path with the basename, the server logs into _`datadir` ._ (_`Datadir`_ is determined by the value of the [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) system variable.)
* If you don't specify a basename, it is strongly recommended to use  [`--log-basename`](../../starting-and-stopping-mariadb/mariadbd-options.md#log-basename) or to ensure that [replication](../../../ha-and-performance/standard-replication/) doesn't stop if the hostname of the computer changes.

## Verifying Logging is On

Once `log-bin` or `log_bin` is configured and the server has been restarted, binary logging is enabled. To verify that, issue this statement:

```sql
SHOW VARIABLES LIKE 'log_bin';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | ON    |
+---------------+-------+
```

## Viewing Log Files

{% include "../../../.gitbook/includes/innodb-based-binlog-from-12.3.md" %}

To view the log files created by the server, issue this statement:

```sql
SHOW BINARY LOGS;
+-------------------------------------------------+-----------+
| Log_name                                        | File_size |
+-------------------------------------------------+-----------+
| c525d37c-b2ff-4543-b06f-87012d142d44-bin.000001 |       437 |
| c525d37c-b2ff-4543-b06f-87012d142d44-bin.000002 |       433 |
+-------------------------------------------------+-----------+
```

To see which log file is currently used, issue this statement:

```sql
SHOW BINLOG STATUS \G
*************************** 1. row ***************************
            File: c525d37c-b2ff-4543-b06f-87012d142d44-bin.000002
        Position: 433
    Binlog_Do_DB: 
Binlog_Ignore_DB: 
```

To find out where log files are stored, issue this statement:

{% code overflow="wrap" %}
```sql
SHOW VARIABLES LIKE 'log_bin_basename' \G
*************************** 1. row ***************************
Variable_name: log_bin_basename
        Value: /opt/homebrew/var/mysql/c525d37c-b2ff-4543-b06f-87012d142d44-bin
```
{% endcode %}

* `/opt/homebrew/var/mysql/` is the **storage location**.
* `c525d37c-b2ff-4543-b06f-87012d142d44-bin` is the **basename** of the binary log files.

## Log File Organization

{% include "../../../.gitbook/includes/innodb-based-binlog-from-12.3.md" %}

Knowing the **basename**, you can view the log files on the file system, too. Change directory (`cd`) to the **storage location**, and issue this command:

```bash
ls -1 c525d37c-b2ff-4543-b06f-87012d142d44-bin.*
c525d37c-b2ff-4543-b06f-87012d142d44-bin.000001
c525d37c-b2ff-4543-b06f-87012d142d44-bin.000001.idx
c525d37c-b2ff-4543-b06f-87012d142d44-bin.000002
c525d37c-b2ff-4543-b06f-87012d142d44-bin.000002.idx
c525d37c-b2ff-4543-b06f-87012d142d44-bin.index
```

* **The binary log index** is the file containing an `.index` extension. It is a plain-text file, containing a master list of the binary log files, in order.\
  By default, the name of the index file is _basename.index_. This can be overridden with the [`--log-bin-index`](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_index) option.
* **The binary log files** have an extension using consecutive numbers, starting with `.000001`. (The higher the number, the newer the log file is.)
* **The binary log files for** [**GTID binlog indexing**](../../../ha-and-performance/standard-replication/gtid.md#binlog-indexing) (available from MariaDB 11.4) have an `.idx` extension.

A new binary log file with a new extension (number) is created:

* Every time the server starts.
* When the logs are flushed with a [`FLUSH LOGS`](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) statement.
* When the maximum size for a binary log file is reached. (This is determined by [max\_binlog\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#max_binlog_size).)

## Turning off Logging per Session

Clients with the [BINLOG ADMIN](../../../reference/sql-statements/account-management-sql-statements/grant.md#binlog-admin) privilege can disable and re-enable binary logging for the current session by setting the [sql\_log\_bin](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sql_log_bin) variable:

```sql
SET sql_log_bin = 0; -- turns off logging
SET sql_log_bin = 1; -- turns on logging
```

## Reading Log Files

{% include "../../../.gitbook/includes/innodb-based-binlog-from-12.3.md" %}

Log files, with the exception of the _index_ log file, are binary-encoded. To display them in a human-readable format, change directory to the [storage location](activating-the-binary-log.md#viewing-log-files) of the log files, and issue this [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) command:

```bash
mariadb-binlog c525d37c-b2ff-4543-b06f-87012d142d44-bin.000001
/*!50530 SET @@SESSION.PSEUDO_SLAVE_MODE=1*/;
/*!40019 SET @@session.max_delayed_threads=0*/;
/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;
DELIMITER /*!*/;
# at 4
#260205 17:13:09 server id 1  end_log_pos 256 CRC32 0x59977cc7 	Start: binlog v 4, server v 12.1.2-MariaDB-log created 260205 17:13:09 at startup
ROLLBACK/*!*/;
…
```

To store that output permanently (for instance, for later processing), issue a command like this:

```bash
mariadb-binlog c525d37c-b2ff-4543-b06f-87012d142d44-bin.000001 > binlog.sql
```

## Log File Security

{% include "../../../.gitbook/includes/innodb-based-binlog-from-12.3.md" %}

Since it's trivial to [read logs files as plain text](activating-the-binary-log.md#reading-log-files), to store that output permanently, and even to use it to import logged data into another database server, ensure that the [storage location](activating-the-binary-log.md#viewing-log-files) is safe. Binary logs are effectively a mirrored copy of your data. If you have encrypted or sensitive data in your tables, it is sitting in those logs in a plain (or easily decodable) format.

Because binary logs capture every data modification (including sensitive personal info or password hashes), they must be treated with the same level of security as the database files themselves.

### File-System Permissions (Least Privilege)

The directory containing binary logs should be restricted at the OS[^1] level.

* Ownership: Files should be owned strictly by the `mysql` (or `mariadb`) system user.
* Permissions: Ensure directory permissions are set (typically `700` or `750`) so that non-privileged users on the server cannot list or read the files.

### Encryption at Rest

If your disk is compromised or a backup of the logs is stolen, raw binary logs are vulnerable.

* MariaDB Encryption: Enable the built-in MariaDB transparent encryption for binary logs. This ensures that even if someone copies the `.000001` file, they cannot decode it without the encryption keys.
* See detailed instructions for [encrypting binary logs](../../../security/encryption/data-at-rest-encryption/managing-binary-log-encryption.md).

### Secure Transport

When binary logs are used for replication (sending data from a primary to a replica server):

* SSL/TLS: Always use encrypted connections for replication traffic to prevent "sniffing" of the log data as it moves across the network.

### Sanitization of Backups

Logs are often backed up alongside data.

* Redaction: Be mindful that logs converted to `.sql` files for auditing (see [example above](activating-the-binary-log.md#reading-log-files)) are now plain text and need to be deleted or encrypted immediately after use.
* Retention: Implement an automated purge policy (`expire_logs_days`) to ensure sensitive data does not persist on disk longer than legally or operationally required.

## Binary Log Format

There are three formats for the binary log. The default is [mixed logging](binary-log-formats.md#mixed-logging), which is a mix of [statement-based](binary-log-formats.md#statement-based-logging) and [row-based logging](binary-log-formats.md#row-based-logging). See [Binary Log Formats](binary-log-formats.md) for a detailed discussion.

## See Also

* [Setting sql\_log\_bin](../../../reference/sql-statements/administrative-sql-statements/set-commands/set-sql_log_bin.md)
* [PURGE LOGS](../../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md) - Delete logs
* [FLUSH LOGS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) - Close and rotate logs
* [GTID binlog indexing](../../../ha-and-performance/standard-replication/gtid.md#binlog-indexing)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: Operating system, like Linux, Windows, or macOS
