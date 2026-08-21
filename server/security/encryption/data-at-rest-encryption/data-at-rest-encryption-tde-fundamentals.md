---
description: >-
  The fundamentals of MariaDB data-at-rest encryption (Transparent Data
  Encryption, TDE), which encrypts files on storage.
---

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

{% hint style="info" %}
**Enterprise Server** provides encryption for **Galera Cluster** via GCache.\
How GCache encryption is enabled and disabled is detailed [on this page](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide#data-in-transit-encryption).
{% endhint %}

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
5. Monitoring encryption progress.

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
**Create the key file.**

In this step, we create a key file that fulfills basic requirements. It contains only one unencrypted key, which is good enough to perform the rest of the steps. It is highly recommended, though, to use multiple keys, and to encrypt the key files. See [Creating the Key File](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#creating-the-key-file).

{% hint style="warning" %}
The key file format differs by product and version, so pick the tab that matches the server you're configuring. The optional key version field is only supported as of Enterprise Server 11.8. Using the wrong format makes the server fail to start with `Invalid key` in the [error log](../../../server-management/server-monitoring-logs/error-log.md).
{% endhint %}

{% tabs %}
{% tab title="Community Server (all versions) & Enterprise Server before 11.8" %}
Run these commands to create an `encryption` folder, and a 32 byte (256 bit) long key file within that folder.

{% code overflow="wrap" %}
```bash
mkdir -p /etc/mysql/encryption
echo $(echo -n "1;" ; openssl rand -hex 32) | sudo tee -a /etc/mysql/encryption/keyfile.txt
```
{% endcode %}
{% endtab %}

{% tab title="Enterprise Server 11.8 and later" %}
Run these commands to create an `encryption` folder, and a 32 byte (256 bit) long key file within that folder. The second field is the key version.

{% code overflow="wrap" %}
```bash
mkdir -p /etc/mysql/encryption 
echo $(echo -n "1;1;" ; openssl rand -hex 32) | sudo tee -a /etc/mysql/encryption/keyfile.txt
```
{% endcode %}
{% endtab %}
{% endtabs %}

To keep the keys out of reach of other users on the system, it is highly recommended to encrypt the key file as well. That requires an encryption password, which is a separate file from the key file. See [Encrypting the Key File](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#encrypting-the-key-file), and use the resulting file names in the next step.
{% endstep %}

{% step %}
**Install and enable a key management plugin.**

Add the following to your configuration file (for instance, `my.cnf`), then restart the server so the changes take effect:

{% code overflow="wrap" %}
```ini
[mariadb]
plugin_load_add = file_key_management
file_key_management_filename = /etc/mysql/encryption/keyfile.txt
# The following line is optional but highly recommended.
# If you encrypted the key file in the previous step, point
# file_key_management_filename at the encrypted key file instead, and
# uncomment the next line to point at the encryption password file.
# file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
```
{% endcode %}

This configuration uses the default encryption algorithm, `AES_CBC`.

{% hint style="warning" %}
Do not set [file\_key\_management\_encryption\_algorithm](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#file_key_management_encryption_algorithm) to `AES_CTR` unless you have a reason to. The algorithm is effectively permanent for data already encrypted with it:

* Changing it later makes the server fail to start, reporting the data files as corrupted rather than naming the algorithm as the cause.
* The HashiCorp Key Management and AWS Key Management plugins only support `AES_CBC`, so data encrypted with `AES_CTR` locks you into the File Key Management plugin.

See [Choosing an Encryption Algorithm](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#choosing-an-encryption-algorithm).
{% endhint %}

For details about file name, file key, and encryption algorithm, see [File Key Management Encryption Plugin](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md).
{% endstep %}

{% step %}
**Enable encryption.**

You can encrypt a number of database objects by setting the respective variables:

* InnoDB user tables – [innodb\_encrypt\_tables](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables)
* InnoDB redo log – [innodb\_encrypt\_log](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log)
* InnoDB temporary files – [innodb\_encrypt\_temporary\_tables](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_temporary_tables)\
  MariaDB creates temporary files on disk, for instance, files used for file sorts. It is recommended to encrypt those, too.
* Aria user tables – [aria\_encrypt\_tables](../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_encrypt_tables)
* Aria temporary tables – [encrypt\_tmp\_disk\_tables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_disk_tables)

To configure global encryption for all of those objects, add this to your configuration file (for instance, `my.cnf`), then restart the server:

{% code overflow="wrap" %}
```ini
[mariadb]
innodb_encrypt_tables = ON
innodb_encrypt_log = ON
innodb_encrypt_temporary_tables = ON
aria_encrypt_tables = ON
encrypt_tmp_disk_tables = ON
# Required to encrypt InnoDB tables that already exist. The default is 0,
# which means existing tables are left as they are.
innodb_encryption_threads = 4
```
{% endcode %}

{% hint style="info" %}
[innodb\_encryption\_threads](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) deserves attention on an existing database. The settings above encrypt InnoDB tables that are *created* from now on, but converting tables that already exist is the job of the background encryption threads. The variable defaults to `0`, meaning no threads run, so without it your existing tables stay unencrypted and the next step has no progress to report.

The same applies in reverse when you disable encryption: the threads are what decrypt existing tables. For details, see [InnoDB Background Encryption Threads](innodb-encryption/innodb-background-encryption-threads.md).
{% endhint %}

Alternatively, set it by running the following statements. Remember, though, that the settings do not persist across server restarts. Also note that some of the variables cannot be set at runtime – they have to be set in a configuration file:

{% code overflow="wrap" %}
```sql
SET GLOBAL innodb_encrypt_tables = ON;    -- for InnoDB tables
SET GLOBAL innodb_encryption_threads = 4; -- to convert existing InnoDB tables
SET GLOBAL aria_encrypt_tables = ON;      -- for Aria tables
SET GLOBAL encrypt_tmp_disk_tables = ON;  -- for Aria temporary tables
```
{% endcode %}

{% hint style="info" %}
Particularly InnoDB has more encryption options. You can fine-tune the encryption, for instance, configure encryption threads. Those details are covered [on this page](innodb-encryption/innodb-enabling-encryption.md).
{% endhint %}

{% hint style="info" %}
Setting `innodb_encrypt_tables` to `FORCE` instead of `ON` additionally rejects any attempt to exempt an individual table with `ENCRYPTED=NO`. Use it when you need encryption to be mandatory across the whole instance. It does not change how existing tables are converted — that is the job of the encryption threads described above. Note that it also makes the [per-table exemptions](data-at-rest-encryption-tde-fundamentals.md#manual-control-disabling-encryption) shown later on this page fail.
{% endhint %}
{% endstep %}

{% step %}
**Verify encryption is turned on.**

Make sure that the global encryption you configured is turned on, by issuing this statement:

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

{% step %}
**Monitor encryption progress.**

The previous step confirms that encryption is configured, not that your data is encrypted yet. If the database already contained tables, the background encryption threads work through them after the restart. Monitor how many InnoDB tablespaces are still unencrypted:

{% code overflow="wrap" %}
```sql
SELECT NAME, ENCRYPTION_SCHEME, ROTATING_OR_FLUSHING 
FROM INFORMATION_SCHEMA.INNODB_TABLESPACES_ENCRYPTION 
WHERE ENCRYPTION_SCHEME = 0;
```
{% endcode %}

Encryption is complete once the query returns an empty set. There's no built-in way to monitor the progress for Aria tables.

{% hint style="info" %}
If the result doesn't change, check that [innodb\_encryption\_threads](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) is greater than `0`. With the default of `0`, existing tables are never converted.
{% endhint %}
{% endstep %}
{% endstepper %}

## Disabling Data-at-Rest Encryption

If you determine that encryption is no longer necessary, you can revert the system to an unencrypted state.

### Prerequisites

* Encryption Status: MariaDB Server must currently have data-at-rest encryption enabled and active.
* Key Management Access: You must have the original key management plugin active and the correct keys loaded to facilitate the decryption of the data.
* Sufficient Disk Space: Ensure adequate free space is available to accommodate the rewritten, unencrypted data files.

{% stepper %}
{% step %}
**Decrypt tables.**

Disable global encryption at the storage engine level by issuing these statements. Note that some variables cannot be turned off at runtime – they have to be removed from the server configuration (for instance, `my.cnf`), and require a server restart:

{% code overflow="wrap" %}
```sql
SET GLOBAL innodb_encrypt_tables = OFF;   -- InnoDB tables
SET GLOBAL aria_encrypt_tables = OFF;     -- Aria tables
SET GLOBAL encrypt_tmp_disk_tables = OFF; -- Aria temporary tables
```
{% endcode %}

{% hint style="warning" %}
Decrypting tables that already exist is done by the background encryption threads, so [innodb\_encryption\_threads](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) must be greater than `0` for this to have any effect. With the default of `0`, turning encryption off only stops new data from being encrypted, and the monitoring step below never reports progress:

```sql
SET GLOBAL innodb_encryption_threads = 4;
```
{% endhint %}

{% hint style="info" %}
Any per-table encryption for InnoDB tables explicitly created with `ENCRYPTED=YES` must be manually decrypted using `ALTER TABLE table_name ENCRYPTED=NO`.
{% endhint %}
{% endstep %}

{% step %}
**Disable log and temp encryption.**

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
**Monitor decryption progress.**

You must wait for the background threads to finish decrypting data pages before removing the keys. Monitor the status for InnoDB tables via the Information Schema (there's no built-in way to monitor the status for Aria tables):

```sql
SELECT NAME, ENCRYPTION_SCHEME, ROTATING_OR_FLUSHING 
FROM INFORMATION_SCHEMA.INNODB_TABLESPACES_ENCRYPTION 
WHERE ENCRYPTION_SCHEME != 0;
```

Decryption is complete once the query returns an empty set.

{% hint style="warning" %}
A restore from an encrypted backup isn't possible after removing the keys.
{% endhint %}
{% endstep %}

{% step %}
**Remove the key management plugin.**

Only after all tables and logs are confirmed as unencrypted should you uninstall the encryption plugin and remove its configuration from your `my.cnf` file. For instance, if you're using the [File Key Management Encryption Plugin](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md), uninstall it:

{% code overflow="wrap" %}
```sql
UNINSTALL SONAME 'file_key_management';
```
{% endcode %}

The statement succeeds with a warning:

{% code overflow="wrap" %}
```
+---------+------+----------------------------------------------------+
| Level   | Code | Message                                            |
+---------+------+----------------------------------------------------+
| Warning | 1620 | Plugin is busy and will be uninstalled on shutdown |
+---------+------+----------------------------------------------------+
```
{% endcode %}

{% hint style="info" %}
This warning is expected, and it doesn't indicate that something is still encrypted. While an encryption plugin is installed, the server holds a reference to it, so the plugin can never be unloaded at runtime. It's removed at the next shutdown instead. Because of this, the following step isn't optional: unless you also remove the configuration, the server loads the plugin again on restart.
{% endhint %}

Remove its configuration, then restart the server:

{% code overflow="wrap" %}
```ini
[mariadb]
# Remove or comment out the following line
plugin_load_add = file_key_management
```
{% endcode %}
{% endstep %}

{% step %}
**Verify encryption is turned off.**

Use [the same SQL statement shown above](data-at-rest-encryption-tde-fundamentals.md#verify-encryption-is-turned-on) to verify encryption is turned off.
{% endstep %}
{% endstepper %}

## TDE in Action: Real-World Behavior

Transparent Data Encryption (TDE) is designed to protect data "at rest" while remaining completely invisible to standard SQL operations. With encryption turned on, MariaDB applies encryption to all new tables automatically.

### Automatic Encryption (InnoDB & Aria)

For the subsequent instructions, we use these tables. With encryption turned on, note that they're encrypted without using any special syntax:

```sql
-- Create an InnoDB table
CREATE TABLE sensitive_accounts_innodb (
    id INT PRIMARY KEY,
    account_name VARCHAR(100)
) ENGINE=InnoDB;

-- Create an Aria table
-- Note that the ROW_FORMAT must be PAGE; otherwise, encryption isn't possible
CREATE TABLE sensitive_accounts_aria (
    id INT PRIMARY KEY,
    account_name VARCHAR(100)
) ENGINE=Aria ROW_FORMAT=PAGE;
```

### Verifying Encryption Status

Because InnoDB and Aria handle data differently, you use two different methods to verify their encryption status.

#### For InnoDB

Check the `information_schema` to see the tablespace encryption scheme. If it's set to `1`, the table is encrypted.

```sql
SELECT NAME, ENCRYPTION_SCHEME 
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION 
WHERE NAME LIKE '%sensitive_accounts_innodb%';
```

{% code overflow="wrap" expandable="true" %}
```
+--------------------------------+-------------------+
| NAME                           | ENCRYPTION_SCHEME |
+--------------------------------+-------------------+
| test/sensitive_accounts_innodb |                 1 |
+--------------------------------+-------------------+
```
{% endcode %}

#### For Aria

There's no built-in way to check the encryption status of Aria tables, but you can check the contents of their `.MAD` files (the Aria data files) with commands like `cat`:

{% code overflow="wrap" expandable="true" %}
```
sudo cat /var/lib/mysql/test/sensitive_accounts_aria.MAD | more
```
{% endcode %}

If you see unintelligible output rather than something resembling data, the Aria table is encrypted.

### Transparent Data Access

Whether the table is InnoDB or Aria, the encryption is **transparent**. Standard SQL statements work without modification, as the engine decrypts the data in memory (the Buffer Pool for InnoDB or Page Cache for Aria).

```sql
-- Standard inserts work for both
INSERT INTO sensitive_accounts_innodb VALUES (1, 'Customer InnoDB');
INSERT INTO sensitive_accounts_aria VALUES (1, 'Customer Aria');

-- Standard selects return plain text
SELECT * FROM sensitive_accounts_innodb;
SELECT * FROM sensitive_accounts_aria;
```

### Manual Control: Disabling Encryption

If you need to exempt a specific table from the global encryption policy, use the `ENCRYPTED` attribute.

{% hint style="info" %}
This is only possible for InnoDB tables.
{% endhint %}

#### Decrypting the Tables

Decrypting tables is done with an `ALTER TABLE` statement. For InnoDB tables, you can do this while global InnoDB table encryption is turned on.

{% hint style="info" %}
For Aria tables, you can only do this when global Aria table encryption is turned off.
{% endhint %}

```sql
-- Disable encryption for the InnoDB table
ALTER TABLE sensitive_accounts_innodb ENCRYPTED=NO;
SELECT NAME, ENCRYPTION_SCHEME  FROM information_schema.INNODB_TABLESPACES_ENCRYPTION  
       WHERE NAME LIKE '%sensitive_accounts_innodb%';
+--------------------------------+-------------------+
| NAME                           | ENCRYPTION_SCHEME |
+--------------------------------+-------------------+
| test/sensitive_accounts_innodb |                 0 |
+--------------------------------+-------------------+

-- Disable encryption for the Aria table
-- This is only possible after disabling global Aria encryption
ALTER TABLE sensitive_accounts_aria ENGINE=Aria, ALGORITHM=COPY;
```

#### Reencrypting the Tables

```sql
ALTER TABLE sensitive_accounts_innodb ENCRYPTED=YES;
SELECT NAME, ENCRYPTION_SCHEME  FROM information_schema.INNODB_TABLESPACES_ENCRYPTION  
       WHERE NAME LIKE '%sensitive_accounts_innodb%';
+--------------------------------+-------------------+
| NAME                           | ENCRYPTION_SCHEME |
+--------------------------------+-------------------+
| test/sensitive_accounts_innodb |                 1 |
+--------------------------------+-------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
