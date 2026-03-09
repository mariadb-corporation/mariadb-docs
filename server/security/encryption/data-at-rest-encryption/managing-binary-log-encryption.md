# Managing Binary Log Encryption

MariaDB can encrypt binary logs and relay logs to ensure that data modifications stored on disk are only accessible through the database server.

## Prerequisites

[Binary log](../../../server-management/server-monitoring-logs/binary-log/) and [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) encryption requires a configured [Key Management and Encryption Plugin](key-management-and-encryption-plugins/) (such as [File Key Management](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) or AWS KMS). MariaDB specifically uses encryption key ID 1 for binary logs.

Key management plugin encryption looks like this (depending on the plugin used, and on the operating system the plugin is installed on):

```ini
[mariadb]
# File Key Management
plugin_load_add = file_key_management
file_key_management_filename = /etc/mysql/encryption/keyfile.enc
file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
file_key_management_encryption_algorithm = AES_CTR
```

## Enabling Encryption

Binary log encryption is controlled by the [`encrypt_binlog`](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#encrypt_binlog) system variable.

{% stepper %}
{% step %}
### Stop the MariaDB server.
{% endstep %}

{% step %}
### Edit the configuration file.

Add the following to your [configuration file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) (e.g., `my.cnf`):

```ini
[mariadb]
encrypt_binlog = ON
```
{% endstep %}

{% step %}
### Start the server.
{% endstep %}
{% endstepper %}

From this point forward, all new binary logs are encrypted. To remove old, unencrypted logs, use [`RESET MASTER`](../../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md) or [`PURGE BINARY LOGS`](../../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md).

## Key Rotation

If your key management plugin supports rotation (check [here](key-management-and-encryption-plugins/encryption-key-management.md#encryption-plugins-with-key-rotation-support)), the server can use new key versions for new binary logs. However, unlike InnoDB, binary logs do not have a background re-encryption mechanism. Existing binary log files remain encrypted with the key version used at the time of their creation.

## Reading Encrypted Binary Logs

Because encrypted logs cannot be read directly by standard text editors, you must use the [`mariadb-binlog`](../../../clients-and-utilities/logging-tools/mariadb-binlog/) utility.

### Method 1: Remote Decryption (Recommended)

The most secure method is to have the server stream the decrypted events. This avoids the need to distribute encryption keys to administrative workstations.

```bash
mariadb-binlog --read-from-remote-server --user=root -p binlog.000012 > decrypted.sql
```

### Method 2: Local Decryption

You can decrypt logs locally if the `mariadb-binlog` utility has access to the same key management plugin and key material used by the server.

```bash
mariadb-binlog /var/lib/mysql/binlog.000012 > decrypted.sql
```

## Disabling Encryption

Disabling encryption stops the server from encrypting future logs. It does not decrypt existing files.

{% stepper %}
{% step %}
### Stop the MariaDB server.
{% endstep %}

{% step %}
### Edit the configuration file.

Add the following to your [configuration file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) (e.g., `my.cnf`):

```ini
[mariadb]
encrypt_binlog = OFF
```
{% endstep %}

{% step %}
### Start the server.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Important: Keep your key management plugin loaded as long as you have encrypted binary logs on disk that you may need to read. If the plugin is removed, the server and `mariadb-binlog` will be unable to decrypt those older files.
{% endhint %}

***

## ️Understanding Binlog Encryption

### Behind the Scenes

When starting with binary log encryption, MariaDB Server logs a `Format_descriptor_log_event` and a `START_ENCRYPTION_EVENT`, then encrypts all subsequent events for the binary log.

Each event header and footer are created and processed to produce encrypted blocks. These encrypted blocks are produced before transactions are committed and before the events are flushed to the binary log. As such, they exist in an encrypted state in memory buffers and in the `IO_CACHE` files for user connections.

### Effects of Data-at-Rest Encryption on Replication

When using encrypted binary logs with [replication](../../../ha-and-performance/standard-replication/replication-overview.md), you can have different encryption keys on the master and the replica. The master decrypts encrypted binary log events as it reads them from disk, and before its [binary log dump thread](../../../ha-and-performance/standard-replication/replication-threads.md#binary-log-dump-thread) sends them to the replica, so the replica actually receives the unencrypted binary log events.

To ensure that binary log events are encrypted as they are transmitted between the master and replica, use [TLS with the replication connection](../data-in-transit-encryption/replication-with-secure-connections.md).

### Effects of Data-at-Rest Encryption on mariadb-binlog

[mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) does not have the ability to decrypt encrypted [binary logs](../../../server-management/server-monitoring-logs/binary-log/) on its own (see [MDEV-8813](https://jira.mariadb.org/browse/MDEV-8813)). In order to use `mariadb-binlog` with encrypted [binary logs](../../../server-management/server-monitoring-logs/binary-log/), use the [--read-from-remote-server](../../../clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options.md) command-line option, so that the server can decrypt the [binary logs](../../../server-management/server-monitoring-logs/binary-log/) for `mariadb-binlog`.

