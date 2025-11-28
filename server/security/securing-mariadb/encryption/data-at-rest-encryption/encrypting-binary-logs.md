# Encrypting Binary Logs

MariaDB Server can encrypt the server's [binary logs](../../../../server-management/server-monitoring-logs/binary-log/) and [relay logs](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md). This ensures that your binary logs are only accessible through MariaDB.

## Basic Configuration

Since [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes), MariaDB can also encrypt [binary logs](../../../../server-management/server-monitoring-logs/binary-log/) (including [relay logs](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md)). Encryption of binary logs is configured by the [encrypt\_binlog](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#encrypt_binlog) system variable.

Users of data-at-rest encryption will also need to have a [key management and encryption plugin](../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) configured. Some examples are the [File Key Management Plugin](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) and [AWS Key Management Plugin](key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md).

```
[mariadb]
...

# File Key Management
plugin_load_add = file_key_management
file_key_management_filename = /etc/mysql/encryption/keyfile.enc
file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
file_key_management_encryption_algorithm = AES_CTR

# Binary Log Encryption
encrypt_binlog=ON
```

## Encryption Keys

[Key management and encryption plugins](../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) support [using multiple encryption keys](../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#using-multiple-encryption-keys). Each encryption key can be defined with a different 32-bit integer as a key identifier.

MariaDB uses the encryption key with ID 1 to encrypt [binary logs](../../../../server-management/server-monitoring-logs/binary-log/).

### Key Rotation

Some [key management and encryption plugins](../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) allow you to automatically rotate and version your encryption keys. If a plugin supports key rotation, and if it rotates the encryption keys, then InnoDB's [background encryption threads](innodb-encryption/innodb-background-encryption-threads.md) can re-encrypt InnoDB pages that use the old key version with the new key version. However, the binary log does **not** have a similar mechanism, which means that existing binary logs remain encrypted with the older key version, but new binary logs will be encrypted with the new key version. For more information, see [MDEV-20098](https://jira.mariadb.org/browse/MDEV-20098).

In order for key rotation to work, both the backend key management service (KMS) and the corresponding [key management and encryption plugin](../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) have to support key rotation. See [Encryption Key Management: Support for Key Rotation in Encryption Plugins](../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#support-for-key-rotation-in-encryption-plugins) to determine which plugins currently support key rotation.

## Enabling Encryption

Encryption of binary logs can be enabled by following the process:

* First, stop the server.
* Then, set [encrypt\_binlog=ON](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#encrypt_binlog) in the MariaDB configuration file.
* Then, start the server.

From that point forward, any new [binary logs](../../../../server-management/server-monitoring-logs/binary-log/) will be encrypted. To delete old unencrypted [binary logs](../../../../server-management/server-monitoring-logs/binary-log/), you can use [RESET MASTER](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md) or [PURGE BINARY LOGS](../../../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md).

## Disabling Encryption

Encryption of [binary logs](../../../../server-management/server-monitoring-logs/binary-log/) can be disabled by following the process:

* First, stop the server.
* Then, set [encrypt\_binlog=OFF](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#encrypt_binlog) in the MariaDB configuration file.
* Then, start the server.

From that point forward, any new [binary logs](../../../../server-management/server-monitoring-logs/binary-log/) will be unencrypted. If you would like the server to continue to have access to old encrypted [binary logs](../../../../server-management/server-monitoring-logs/binary-log/), then make sure to keep your [key management and encryption plugin](../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) loaded.

## Understanding Binlog Encryption

When starting with binary log encryption, MariaDB Server logs a `Format_descriptor_log_event` and a `START_ENCRYPTION_EVENT`, then encrypts all subsequent events for the binary log.

Each event's header and footer are created and processed to produce encrypted blocks. These encrypted blocks are produced before transactions are committed and before the events are flushed to the binary log. As such, they exist in an encrypted state in memory buffers and in the `IO_CACHE` files for user connections.

### Effects of Data-at-Rest Encryption on Replication

When using encrypted binary logs with [replication](../../../../ha-and-performance/standard-replication/replication-overview.md), it is completely supported to have different encryption keys on the master and slave. The master decrypts encrypted binary log events as it reads them from disk, and before its [binary log dump thread](../../../../ha-and-performance/standard-replication/replication-threads.md#binary-log-dump-thread) sends them to the slave, so the slave actually receives the unencrypted binary log events.

If you want to ensure that binary log events are encrypted as they are transmitted between the master and slave, then you will have to use [TLS with the replication connection](../data-in-transit-encryption/replication-with-secure-connections.md).

### Effects of Data-at-Rest Encryption on mariadb-binlog

[mariadb-binlog](../../../../clients-and-utilities/logging-tools/mariadb-binlog/) does not currently have the ability to decrypt encrypted [binary logs](../../../../server-management/server-monitoring-logs/binary-log/) on its own (see [MDEV-8813](https://jira.mariadb.org/browse/MDEV-8813) about that). In order to use mariadb-binlog with encrypted [binary logs](../../../../server-management/server-monitoring-logs/binary-log/), you have to use the [--read-from-remote-server](../../../../clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options.md) command-line option, so that the server can decrypt the [binary logs](../../../../server-management/server-monitoring-logs/binary-log/) for mariadb-binlog.

Note, using the `--read-from-remote-server` option on versions of the `mariadb-binlog` utility that do not have the [MDEV-20574](https://jira.mariadb.org/browse/MDEV-20574) fix (<=[MariaDB 10.4.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1049-release-notes), [MariaDB 10.3.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10319-release-notes), [MariaDB 10.2.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10228-release-notes)) can corrupt binlog positions when the binary log is encrypted.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
