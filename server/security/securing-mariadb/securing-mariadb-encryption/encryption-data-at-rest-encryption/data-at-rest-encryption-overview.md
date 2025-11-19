# Data-at-Rest Encryption Overview

## Overview

Having tables encrypted makes it almost impossible for someone to access or\
steal a hard disk and get access to the original data. This functionality is also known as "Transparent Data Encryption (TDE)".

This assumes that encryption keys are stored on another system.

Using encryption has an overhead of roughly _3-5%_.

## Which Storage Engines Does MariaDB Encryption Support?

MariaDB encryption is fully supported for the [InnoDB](../../../../server-usage/storage-engines/innodb/) storage engines. Encryption is also supported for the Aria storage engine, but only for tables created with `ROW_FORMAT=PAGE` (the default), and for the binary log (replication log).

MariaDB allows the user to configure flexibly what to encrypt. In or InnoDB, one can choose to encrypt:

* everything — all tablespaces (with all tables) (with [innodb\_encrypt\_tables=1](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables))
* individual tables
* everything, excluding individual tables

Additionally, one can choose to encrypt InnoDB log files (recommended, with [innodb\_encrypt\_log=1](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log)) and InnoDB Temporary Tables (with [innodb\_encrypt\_temporary\_tables=1](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_temporary_tables)).

When [innodb\_encrypt\_log=1](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log) or [innodb\_encrypt\_temporary\_tables=1](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_temporary_tables) an encryption key of 1 must be defined. See [Enabling InnoDB Encryption](../../encryption/data-at-rest-encryption/innodb-encryption/innodb-enabling-encryption.md).

## Limitations

These limitations exist in the data-at-rest encryption implementation:

* Only data and only at rest is encrypted. Metadata (for example `.frm` files) and data sent to the client are not encrypted (but see [Secure Connections](../../encryption/data-in-transit-encryption/)).
* Only the MariaDB server knows how to decrypt the data, in particular
  * [mariadb-binlog](../../../../clients-and-utilities/logging-tools/mariadb-binlog/) can read encrypted binary logs only when --read-from-remote-server is used ([MDEV-8813](https://jira.mariadb.org/browse/MDEV-8813)).
  * [Percona XtraBackup](../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) cannot back up instances that use encrypted InnoDB. However, MariaDB's fork, [MariaDB Backup](../../../../server-usage/backup-and-restore/mariadb-backup/), can back up encrypted instances.
* The [Audit plugin](../../../../reference/plugins/mariadb-audit-plugin/) cannot create encrypted output. Send it to syslog and configure the protection there instead.
* File-based [general query log](../../../../server-management/server-monitoring-logs/general-query-log.md) and [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/) cannot be encrypted ([MDEV-9639](https://jira.mariadb.org/browse/MDEV-9639)).
* The Aria log is not encrypted ([MDEV-8587](https://jira.mariadb.org/browse/MDEV-8587)). This affects only non-temporary Aria tables though.
* The MariaDB [error log](../../../../server-management/server-monitoring-logs/error-log.md) is not encrypted. The error log can contain query text and data in some cases, including crashes, assertion failures, and cases where InnoDB write monitor output to the log to aid in debugging. It can sent to syslog too, if needed.

## Encryption Key Management

MariaDB's data-at-rest encryption requires the use of a [key management and encryption plugin](key-management-and-encryption-plugins/encryption-key-management.md). These plugins are responsible both for the management of encryption keys and for the actual encryption and decryption of data.

MariaDB supports the use of [multiple encryption keys](key-management-and-encryption-plugins/encryption-key-management.md#using-multiple-encryption-keys). Each encryption key uses a 32-bit integer as a key identifier. If the specific plugin supports [key rotation](key-management-and-encryption-plugins/encryption-key-management.md#rotating-keys), then encryption keys can also be rotated, which creates a new version of the encryption key.

How MariaDB manages encryption keys depends on which encryption key management solution you choose. Currently, MariaDB has three options:

* [File Key Management Plugin](../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md)
* [AWS Key Management Plugin](../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md)
* [Hashicorp Key Management Plugin](../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md)

Once you have an key management and encryption plugin set up and configured for your server, you can begin using encryption options to better secure your data.

## Encrypting Data

Encryption occurs whenever MariaDB writes pages to disk. Encrypting table data requires that you install a [key management and encryption plugin](key-management-and-encryption-plugins/encryption-key-management.md), such as the [File Key Management](../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) plugin. Once you have a plugin set up and configured, you can enable encryption for your InnoDB and Aria tables.

### Encrypting Table Data

MariaDB supports data-at-rest encryption for InnoDB and Aria storage engines. Additionally, it supports encrypting the [InnoDB redo log](../../../../server-usage/storage-engines/innodb/innodb-redo-log.md) and internal on-disk temporary tables that use the Aria storage engine..

* [Encrypting Data for InnoDB](../../encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-overview.md)
* [Encrypting Data for Aria](../../encryption/data-at-rest-encryption/aria-encryption/aria-encryption-overview.md)

### Encrypting Temporary Files

MariaDB also creates temporary files on disk. For example, a binary log cache will be written to a temporary file if the binary log cache exceeds [binlog\_cache\_size](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_cache_size) or [binlog\_stmt\_cache\_size](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_stmt_cache_size), and temporary files are also often used for filesorts during query execution. These temporary files can also be encrypted if [encrypt\_tmp\_files=ON](https://mariadb.com/docs/server/server-management/variables-and-modes/server-system-variables#encrypt_tmp_files) is set.

Temporary files created internally by InnoDB, such as those used for merge sorts and row logs can also be encrypted if [innodb\_encrypt\_log=ON](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) is set. These files are encrypted regardless of whether the tables involved are encrypted or not, and regardless of whether [encrypt\_tmp\_files](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_files) is set or not.

### Encrypting Binary Logs

MariaDB can also encrypt [binary logs](../../../../server-management/server-monitoring-logs/binary-log/) (including [relay logs](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md)).

* [Encrypting Binary Logs](../../encryption/data-at-rest-encryption/encrypting-binary-logs.md)

## Encryption and Page Compression

Data-at-rest encryption and [InnoDB page compression](../../../../server-usage/storage-engines/innodb/innodb-page-compression.md) can be used together. When they are used together, data is first compressed, and then it is encrypted. In this case you save space and still have your data protected.

## Thanks

* Tablespace encryption was donated to the MariaDB project by Google.

We are grateful to these companies for their support of MariaDB!

## See Also

* [Encryption functions](../../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/)
* [DES\_DECRYPT()](../../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_decrypt.md)
* [DES\_ENCRYPT()](../../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_encrypt.md)
* A [blog post about table encryption](https://mariadb.com/blog/table-and-tablespace-encryption-mariadb-101/) with benchmark results

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
