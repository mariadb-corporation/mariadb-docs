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

* InnoDB: Fully supported. You can encrypt all tablespaces, individual tables, and the InnoDB redo log. For details, see [InnoDB Encryption](innodb-encryption/).
* Aria: Supported only for tables created with `ROW_FORMAT=PAGE` (the default). For details, see [Aria Encryption](aria-encryption/).
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

{% hint style="info" %}
For the rest of this page, we assume you're using the [File Key Management Encryption Plugin](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md). If you're using a different one, adjust the configuration and SQL statements accordingly.
{% endhint %}

## Enabling Data-at-Rest Encryption

Enabling data-at-rest encryption encompasses these steps:

1. Creating a key file.
2. Installing and enabling a [key management plugin](key-management-and-encryption-plugins/).
3. Enabling encryption for Aria tables, InnoDB tables, or both.
4. Verifying encryption is turned on.

{% hint style="info" %}
The path used in these instructions (`/etc/mysql/encryption/`) is common for most Linux systems. Adjust if your operating system uses a different path.
{% endhint %}

{% hint style="info" %}
MariaDB server must be restarted several times. On most Linux systems, the command for that is `sudo systemctl restart mariadb`. Consult your operating system documentation to find out what your system uses.

If you're getting errors, particularly if MariaDB fails to start, for example due to a configuration issue, inspect the [error log](../../../server-management/server-monitoring-logs/error-log.md). On many modern Linux versions, this can be done using `journalctl`. Example:

{% code overflow="wrap" %}
```bash
sudo journalctl -u mariadb -n 1000 --no-pager | grep ERROR
```
{% endcode %}
{% endhint %}

{% stepper %}
{% step %}
### Create the key file.

In this step, we create a key file that fulfills basic requirements. It contains only one unencrypted key, which is good enough to perform the rest of the steps. It is highly recommended, though, to use multiple keys, and to encrypt those key files. See [Creating the Key File](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#creating-the-key-file).

{% tabs %}
{% tab title="Current Enterprise Server" %}
Run these commands to create an `encryption` folder, and a 32 byte (256 bit) long key file within that folder.

{% code overflow="wrap" %}
```bash
mkdir -p /etc/mysql/encryption 
echo $(echo -n "1;1;" ; openssl rand -hex 32) | sudo tee -a /etc/mysql/encryption/keyfile.txt
```
{% endcode %}
{% endtab %}

{% tab title="Enterprise Server < 11.8 & Community Server" %}
Run these commands to create an `encryption` folder, and a 32 byte (256 bit) long key file within that folder.

{% code overflow="wrap" %}
```bash
mkdir -p /etc/mysql/encryption
echo $(echo -n "1;" ; openssl rand -hex 32) | sudo tee -a /etc/mysql/encryption/keyfile.txt
```
{% endcode %}
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
### Install and enable a key management plugin.

Add the following to your configuration file (for instance, `my.cnf`), then restart the server so the changes take effect:

{% code overflow="wrap" %}
```ini
[mariadb]
plugin_load_add = file_key_management
file_key_management_filename = /etc/mysql/encryption/keyfile.txt
# The following line is optional but highly recommended.
# Uncomment to enable usage of an encrypted key file.
## file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
file_key_management_encryption_algorithm = AES_CTR
```
{% endcode %}

For details about file name, file key, and encryption algorithm, see [File Key Management Encryption Plugin](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md).
{% endstep %}

{% step %}
### Enable encryption.

You can encrypt a number of database objects by setting the respective variables:

* InnoDB user tables – [innodb\_encrypt\_tables](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables)
* InnoDB redo log – [innodb\_encrypt\_log](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log)
* InnoDB temporary files – [encrypt\_temporary\_tables](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_temporary_tables)\
  MariaDB creates temporary files on disk, for instance, files used for file sorts. It is recommended to encrypt those, too.
* Aria user tables – [aria\_encrypt\_tables](../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_encrypt_tables)
* Aria temporary tables – [encrypt\_tmp\_disk\_tables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_disk_tables)

To configure encryption for all of those objects, add this to your configuration file (for instance, `my.cnf`), then restart the server:

{% code overflow="wrap" %}
```ini
[mariadb]
innodb_encrypt_tables = ON
innodb_encrypt_log = ON
encrypt_temporary_tables = ON
aria_encrypt_tables = ON
encrypt_tmp_disk_tables = ON
```
{% endcode %}

Alternatively, set it running the following statements. Remember, though, that the settings do not persist across server restarts. Also note that some of the variables cannot be set at runtime – they have to be set in a configuration file:

{% code overflow="wrap" %}
```sql
SET GLOBAL innodb_encrypt_tables = ON;   -- for InnoDB tables
SET GLOBAL aria_encrypt_tables = ON;     -- for Aria tables
SET GLOBAL encrypt_tmp_disk_tables = ON; -- for Aria temporary tables
```
{% endcode %}

{% hint style="info" %}
Particularly InnoDB has more encryption options. You can fine-tune the encryption (for instance, configuring encryption threads), or encrypt tablespaces.  Those details are covered [on this page](innodb-encryption/innodb-enabling-encryption.md).
{% endhint %}
{% endstep %}

{% step %}
### Verify encryption is turned on.

Make sure that the variables you configured are turned on, by issuing this statement:

{% code overflow="wrap" %}
```sql
SELECT 
 'InnoDB Tables' AS Component, @@innodb_encrypt_tables AS Active
 UNION SELECT 'InnoDB Logs', @@innodb_encrypt_log
 UNION SELECT 'InnoDB Temp', @@innodb_encrypt_temporary_tables
 UNION SELECT 'Aria System', @@aria_encrypt_tables
 UNION SELECT 'Aria Temp', @@encrypt_tmp_disk_tables;
```
{% endcode %}

If encryption of all database objects is successfully enabled, this is the output of the query:

{% code overflow="wrap" %}
```
+---------------+--------+
| Component     | Active |
+---------------+--------+
| InnoDB Tables | ON     |
| InnoDB Logs   | 1      |
| InnoDB Temp   | 1      |
| Aria System   | 1      |
| Aria Temp     | 1      |
+---------------+--------+
```
{% endcode %}
{% endstep %}
{% endstepper %}

## Disabling Data-at-Rest Encryption

If you determine that encryption is no longer necessary, you can revert the system to an unencrypted state.

### Prerequisites

* Encryption Status: MariaDB Enterprise Server must currently have data-at-rest encryption enabled and active.
* Key Management Access: You must have the original key management plugin active and the correct keys loaded to facilitate the decryption of the data.
* Sufficient Disk Space: Ensure adequate free space is available to accommodate the rewritten, unencrypted data files.

{% stepper %}
{% step %}
### Decrypt tables.

Disable encryption at the storage engine level by issuing these statements. Note that some variables cannot be turned off at runtime – they have to be removed from the server configuration (for instance, `my.cnf`), and require a server restart:

{% code overflow="wrap" %}
```sql
SET GLOBAL innodb_encrypt_tables = OFF;   -- InnoDB tables
SET GLOBAL aria_encrypt_tables = OFF;     -- Aria tables
SET GLOBAL encrypt_tmp_disk_tables = OFF; -- Aria temporary tables
```
{% endcode %}

{% hint style="info" %}
Any per-table encryption for tables explicitly created with `ENCRYPTED=YES` must be manually decrypted using `ALTER TABLE table_name ENCRYPTED=NO;`.
{% endhint %}
{% endstep %}

{% step %}
### Disable log and temp encryption.

Update your configuration file (`my.cnf`) to stop encrypting Aria and InnoDB tables, as well as new logs and temporary files:

```ini
[mariadb]
innodb_encrypt_tables = OFF
innodb_encrypt_log = OFF
innodb_encrypt_temporary_tables = OFF
aria_encrypt_tables = OFF
encrypt_tmp_disk_tables = OFF
```
{% endstep %}

{% step %}
### Monitor decryption progress.

You must wait for the background threads to finish decrypting data pages before removing the keys. Monitor the status via the Information Schema:

```sql
SELECT NAME, ENCRYPTION_SCHEME, ROTATING_OR_FLUSHING 
FROM INFORMATION_SCHEMA.INNODB_TABLESPACES_ENCRYPTION 
WHERE ENCRYPTION_SCHEME != 0;
```

{% hint style="warning" %}
A restore from an encrypted backup isn't possible after removing the keys.
{% endhint %}
{% endstep %}

{% step %}
### Remove the key management plugin.

Only after all tables and logs are confirmed as unencrypted should you uninstall the encryption plugin and remove its configuration from your `my.cnf` file. For instance, if you're using the [File Key Management Encryption Plugin](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md), uninstall it:

{% code overflow="wrap" %}
```sql
UNINSTALL SONAME 'file_key_management';
```
{% endcode %}

Remove its configuration, then restart the server:

{% code overflow="wrap" %}
```ini
[mariadb]
# Remove or comment out the following line
plugin_load_add = file_key_management
```
{% endcode %}
{% endstep %}
{% endstepper %}

