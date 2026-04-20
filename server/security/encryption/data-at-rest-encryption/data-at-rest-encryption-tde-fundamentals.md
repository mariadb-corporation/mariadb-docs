# Data-at-Rest Encryption (TDE) Fundamentals

MariaDB Data-at-Rest Encryption, also known as Transparent Data Encryption (TDE), protects your data by encrypting files directly on the storage media. This ensures that if physical disks or backup files are stolen, the data remains unreadable without the corresponding encryption keys.

## Security Context

### When Encryption Protects Your Data

* Physical Theft: Unauthorized access to hard drives or storage arrays.
* Backup Exposure: If database backups are intercepted or accessed by unauthorized parties.
* Service Provider Access: Preventing infrastructure administrators in cloud or managed environments from viewing sensitive data.

### When Encryption is No Help

* Authorized Access: Users with valid SQL credentials will still see decrypted data; TDE does not replace a robust [User Account Management](../../user-account-management/) strategy.
* Application Vulnerabilities: TDE does not prevent SQL injection or application-level data breaches.
* Data-in-Transit: This feature only secures stored data. Use [TLS/SSL](../tls-and-cryptography-libraries-used-by-mariadb.md) to secure data moving across the network.

### Architecture and Lifecycle

MariaDB performs encryption at the I/O layer. This process is "transparent" because applications and queries do not need to be modified to interact with encrypted data.

Once a [Key Management plugin](key-management-and-encryption-plugins/) is configured, encryption occurs automatically whenever MariaDB writes pages to disk, and decryption occurs when data is read back into memory.

* Write Path: When MariaDB flushes data from the buffer pool to the disk, the data is encrypted.
* Read Path: When MariaDB reads data from the disk into memory, it is decrypted.
* Memory: Data stored in RAM (such as the buffer pool) remains in a decrypted state while in use.

## Storage Engine Support

MariaDB provides flexible control over what is encrypted, though support and requirements vary by component:

* InnoDB: Fully supported. You can encrypt all tablespaces, individual tables, and the InnoDB redo log. For configuration details, see [InnoDB Encryption](innodb-encryption/).
* Aria: Supported only for tables created with `ROW_FORMAT=PAGE` (the default). For configuration details, see [Aria Encryption](aria-encryption/).
* Binary Logs: MariaDB can encrypt binary logs and relay logs to protect the replication pipeline. See [Managing Binary Log Encryption](managing-binary-log-encryption.md).
* Temporary Files: Internal on-disk temporary files can be encrypted by setting `encrypt_tmp_files=ON`.

## Limitations

The following elements are not encrypted by the MariaDB server:

* Metadata: Information in `.frm` files and the system data dictionary.
* Specific Logs: The MariaDB Error Log, General Query Log, and Slow Query Log.
* Aria Control Log: While Aria tables can be encrypted, the Aria storage engine log is not currently encrypted.
* Utilities: Tools like `mariadb-binlog` require the `--read-from-remote-server` flag to read encrypted content.

## Key Management

Encryption requires a key management and encryption plugin. These plugins are responsible for managing the 32-bit integer key identifiers and performing the cryptographic operations. You must install and configure a [Key Management Plugin](key-management-and-encryption-plugins/) before enabling encryption options for storage engines.

## Disabling Data-at-Rest Encryption

If you determine that encryption is no longer necessary, you can revert the system to an unencrypted state.

### Prerequisites

* Encryption Status: MariaDB Enterprise Server must currently have data-at-rest encryption enabled and active.
* Key Management Access: You must have the original key management plugin active and the correct keys loaded to facilitate the decryption of the data.
* Sufficient Disk Space: Ensure adequate free space is available to accommodate the rewritten, unencrypted data files.

#### Step 1: Decrypt Tables

Disable encryption at the storage engine level. For InnoDB, you can disable global encryption by setting:

```sql
SET GLOBAL innodb_encrypt_tables = OFF
```

{% hint style="info" %}
Any per-table encryption for tables explicitly created with `ENCRYPTED=YES` must be manually decrypted using `ALTER TABLE table_name ENCRYPTED=NO;`.
{% endhint %}

#### Step 2: Disable Log and Temp Encryption

Update your configuration file (`my.cnf`) to stop encrypting new logs and temporary files:

```ini
[mariadb]
innodb_encrypt_log = OFF
encrypt_tmp_files = OFF
```

#### Step 3: Monitor Decryption Progress

You must wait for the background threads to finish decrypting data pages before removing the keys. Monitor the status via the Information Schema:

```sql
SELECT NAME, ENCRYPTION_SCHEME, ROTATING_OR_FLUSHING 
FROM INFORMATION_SCHEMA.INNODB_TABLESPACES_ENCRYPTION 
WHERE ENCRYPTION_SCHEME != 0;
```

#### Step 4: Remove the Key Management Plugin

Only after all tables and logs are confirmed as unencrypted should you uninstall the encryption plugin and remove its configuration from your `my.cnf` file.

