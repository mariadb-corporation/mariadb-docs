---
description: >-
  Solutions for common issues such as Error 1005 (Wrong create options) when
  configuring encryption, and handling cases where encryption key IDs are set
  for unencrypted tables.
---

# InnoDB: Encryption Troubleshooting

### Wrong Create Options

With InnoDB tables using encryption, there are several cases where a [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement can throw Error 1005, due to the InnoDB error 140, `Wrong create options`:

```sql
CREATE TABLE `test`.`table1` ( `id` INT(4) PRIMARY KEY , `name` VARCHAR(50));
ERROR 1005 (HY000): Can't create table `test`.`table1` (errno: 140 "Wrong create options")
```

When this occurs, you can usually get more information about the cause of the error by following it with a [SHOW WARNINGS](../../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md) statement.

This error is known to occur in the following cases:

* Encrypting a table by setting the [ENCRYPTED](../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option to `YES` when the [innodb\_file\_per\_table](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) is set to `OFF`.In this case, [SHOW WARNINGS](../../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md) would return the following:

```sql
SHOW WARNINGS;
+---------+------+---------------------------------------------------------------------+
| Level   | Code | Message                                                             |
+---------+------+---------------------------------------------------------------------+
| Warning |  140 | InnoDB: ENCRYPTED requires innodb_file_per_table                    |
| Error   | 1005 | Can't create table `db1`.`tab3` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB     |
+---------+------+---------------------------------------------------------------------+
3 rows in set (0.00 sec)
```

* Encrypting a table by setting the [ENCRYPTED](../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option to `YES`, and the [innodb\_default\_encryption\_key\_id](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id) system variable or the [ENCRYPTION\_KEY\_ID](../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option refers to a non-existent key identifier. In this case, [SHOW WARNINGS](../../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md) would return the following:

```sql
SHOW WARNINGS;
+---------+------+---------------------------------------------------------------------+
| Level   | Code | Message                                                             |
+---------+------+---------------------------------------------------------------------+
| Warning |  140 | InnoDB: ENCRYPTION_KEY_ID 500 not available                         |
| Error   | 1005 | Can't create table `db1`.`tab3` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB     |
+---------+------+---------------------------------------------------------------------+
3 rows in set (0.00 sec)
```

* In some versions, this could happen while creating a table with the [ENCRYPTED](../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT` while the [innodb\_encrypt\_tables](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable is set to `OFF`, and the [innodb\_default\_encryption\_key\_id](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id) system variable or the [ENCRYPTION\_KEY\_ID](../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option are not set to `1`. In this case, [SHOW WARNINGS](../../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md) would return the following:

```sql
SHOW WARNINGS;
+---------+------+---------------------------------------------------------------------+
| Level   | Code | Message                                                             |
+---------+------+---------------------------------------------------------------------+
| Warning |  140 | InnoDB: innodb_encrypt_tables=OFF only allows ENCRYPTION_KEY_ID=1   |
| Error   | 1005 | Can't create table `db1`.`tab3` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB     |
+---------+------+---------------------------------------------------------------------+
3 rows in set (0.00 sec)
```

Creating a table with the [ENCRYPTED](../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT` while the [innodb\_encrypt\_tables](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable is set to `OFF`, and the [innodb\_default\_encryption\_key\_id](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id) system variable or the [ENCRYPTION\_KEY\_ID](../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option are **not** set to `1` no longer fail, and it no longer throws a warning.

For more information, see [MDEV-18601](https://jira.mariadb.org/browse/MDEV-18601).

### Setting Encryption Key ID For an Unencrypted Table

If you set the [ENCRYPTION\_KEY\_ID](../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option for a table that is unencrypted because the [innodb\_encrypt\_tables](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable is set to `OFF` and the [ENCRYPTED](../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT`, then this encryption key ID will be saved in the table's `.frm` file, but the encryption key will not be saved to the table's `.ibd` file.

As a side effect, with the current encryption design, if the [innodb\_encrypt\_tables](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable is later set to `ON`, and InnoDB goes to encrypt the table, then the [InnoDB background encryption threads](innodb-background-encryption-threads.md) will not read this encryption key ID from the `.frm` file. Instead, the threads may encrypt the table with the encryption key with ID `1`, which is internally considered the default encryption key when no key is specified. For example:

```sql
SET GLOBAL innodb_encrypt_tables=OFF;

CREATE TABLE tab1 (
   id INT PRIMARY KEY,
   str VARCHAR(50)
) ENCRYPTION_KEY_ID=100;

SET GLOBAL innodb_encrypt_tables=ON;

SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE NAME='db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 1 |              1 |
+----------+-------------------+----------------+
```

A similar problem is that, if you set the [ENCRYPTION\_KEY\_ID](../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option for a table that is unencrypted because the [ENCRYPTED](../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option is set to `NO`, then this encryption key ID will be saved in the table's `.frm` file, but the encryption key will not be saved to the table's `.ibd` file.

Recent versions of MariaDB will throw warnings in the case where the [ENCRYPTED](../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option is set to `NO`, but they will allow the operation to succeed. For example:

```sql
CREATE TABLE tab1 (
   id INT PRIMARY KEY,
   str VARCHAR(50)
) ENCRYPTED=NO ENCRYPTION_KEY_ID=100;
Query OK, 0 rows affected, 1 warning (0.01 sec)

SHOW WARNINGS;
+---------+------+--------------------------------------------------+
| Level   | Code | Message                                          |
+---------+------+--------------------------------------------------+
| Warning |  140 | InnoDB: ENCRYPTED=NO implies ENCRYPTION_KEY_ID=1 |
+---------+------+--------------------------------------------------+
1 row in set (0.00 sec)
```

However, in this case, if you change the [ENCRYPTED](../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option to `YES` or `DEFAULT` with [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/), then it will actually use the proper key. For example:

```sql
SET GLOBAL innodb_encrypt_tables=ON;

ALTER TABLE tab1 ENCRYPTED=DEFAULT;

SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE NAME = 'db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 1 |            100 |
+----------+-------------------+----------------+
```

For more information, see [MDEV-17230](https://jira.mariadb.org/browse/MDEV-17230), [MDEV-18601](https://jira.mariadb.org/browse/MDEV-18601), and [MDEV-19086](https://jira.mariadb.org/browse/MDEV-19086).

### Tablespaces Created on MySQL 5.1.47 or Earlier

MariaDB's data-at-rest encryption implementation re-used previously unused fields in InnoDB's buffer pool pages to identify the encryption key version and the post-encryption checksum. Prior to MySQL 5.1.48, these unused fields were not initialized in memory due to performance concerns. These fields still had zero values most of the time, but since they were not explicitly initialized, that means that these fields could have occasionally had non-zero values that could have been written into InnoDB's tablespace files. If MariaDB were to encounter an unencrypted page from a tablespace file that was created on an early version of MySQL that also had non-zero values in these fields, then it would mistakenly think that the page was encrypted.

The fix for [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112) changed the way that MariaDB distinguishes between encrypted and unencrypted pages, so that it is less likely to mistake an unencrypted page for an encrypted page.

If [innodb\_checksum\_algorithm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm) is set to `full_crc32` or `strict_full_crc32`, and if the table does not use [ROW\_FORMAT=COMPRESSED](../../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md), then data files are guaranteed to be zero-initialized.

For more information, see [MDEV-18097](https://jira.mariadb.org/browse/MDEV-18097).

### Spatial Indexes

Support for encrypting [spatial indexes](../../../../reference/sql-structure/geometry/spatial-index.md). To enable, set the [innodb\_checksum\_algorithm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm) to `full_crc32` or to `strict_full_crc32`. Note that MariaDB only encrypts spatial indexes when the [ROW\_FORMAT](../../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option is **not** set to [COMPRESSED](../../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md).

For more information, see [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026).

### Managing CPU Usage During InnoDB Encryption Operations

When encryption threads are enabled for InnoDB tables, the system initiates background threads to encrypt existing tablespace pages. During this initial process, you may see significant spikes in CPU and I/O usage. This can occur due to:

* **Periodic key rotation checks** that trigger re‑encryption work.
* **Large datasets** being encrypted, especially if many tables are enabled at once.
* **Clustered environments** such as MariaDB Galera Cluster, where each node performs encryption operations independently.

CPU usage can increase under several conditions. Common contributing factors are included below.

#### Causes of CPU Spikes

CPU usage increases during table encryption due to the following factors:

* **CPU usage spikes after enabling encryption**: This is expected because InnoDB must begin encrypting existing tablespace pages in the background once encryption is turned on. The initial workload is heavy.
* **Increased disk I/O activity**: The process involves reading unencrypted pages, encrypting them, and writing them back as encrypted. This read–encrypt–write cycle generates both CPU load (for encryption) and disk I/O load (for page movement).
* **Background threads encrypting tablespace pages:** InnoDB background threads actively encrypt tablespace pages that were encrypted before encryption was enabled. If too many threads are active or configured aggressively, they compete for CPU resources, causing spikes.
* **Performance degradation during initial encryption**: The initial stage of encrypting large tablespaces is the most resource-intensive phase. Once completed, ongoing CPU usage stabilizes, but during the initial encryption, performance can degrade significantly.

This behavior is normal during the one‑time setup phase when InnoDB begins encrypting existing tablespace pages. However, the impact can be reduced through:

* **Tuning** system variables such as `innodb_encryption_threads`, `innodb_encryption_rotation_iops`, and `innodb_encryption_rotate_key_age`.
* **Monitoring** background encryption activity to check progress and identify bottlenecks.
* **Phased rollout** of encryption, enabling it for a subset of tables at a time rather than all tables at once. See the [Operational Best Practices](innodb-encryption-troubleshooting.md#operational-best-practices) section.

#### Configuration Options

**Monitor Background Encryption Activity**

MariaDB performs encryption in background threads. This helps determine if CPU usage is due to ongoing table encryption or key rotation.&#x20;

Before changing configuration, verify whether background encryption is currently running by executing the following command:

```
SHOW ENGINE INNODB STATUS
```

You can review the encryption activity output.

Additionally, you can check the essential encryption-related status variables, as detailed in [InnoDB: Background Encryption Threads](innodb-background-encryption-threads.md).

#### Disable Key Rotation Checks

The `innodb_encryption_rotate_key_age` system variable manages how often InnoDB checks tablespace pages to determine whether they need to be re‑encrypted with a new key.

Setting this variable to `0` disables automatic key rotation checks if you do not require periodic re-encryption of old pages:

```
SET GLOBAL innodb_encryption_rotate_key_age=0;
```

Once disabled, key rotation checks can significantly reduce CPU usage. See [innodb\_encryption\_rotate\_key\_age](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age).

#### Limit Background Encryption Threads

The `innodb_encryption_threads` system variable controls the number of background encryption threads.

Lowering this value can prevent CPU contention at the cost of slower encryption progress.

```
SET GLOBAL innodb_encryption_threads=2;
```

&#x20;You can maintain the value based on available CPU capacity and workload requirements. See [innodb\_encryption\_threads](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads).

#### Reduce Encryption Rotation IOPS

The `innodb_encryption_rotation_iops` system variable defines the maximum number of I/O operations per second that InnoDB background threads can use for page encryption and key rotation tasks.

**Effect of Lowering the Value:**

* **Reduces CPU usage:** fewer encryption operations are performed per second, lowering the load on CPU resources.
* **Lowers disk pressure:** decreases the number of read/write operations, reducing contention on storage I/O.

```
SET GLOBAL innodb_encryption_rotation_iops=50;
```

Setting a lower value (e.g., 25 or 50) limits the threads, making them read and write data more slowly, reducing both I/O and the associated CPU overhead. See [innodb\_encryption\_rotation\_iops](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotation_iops).

#### Operational Best Practices

In addition to configuration changes, you can also manage encryption more effectively by applying the following operational practices:

* Encrypt table in batches: Instead of enabling encryption for all tables at once, apply it in stages. This allow background encryption to complete for one set of tables and then proceed with more. With this approach, peak CPU and I/O load can be reduced.&#x20;
* Galera Cluster setup considerations:
  * Encryption operations are performed independently on each node
  * Use an odd number of nodes (3, 5, 7) to maintain quorum and prevent split-brain scenarios. See [Weighted Quorum](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-architecture/quorum-control-with-weighted-votes) for details.

## See Also

* [InnoDB Data-at-Rest Encryption](../)
* [InnoDB Background Encryption Threads](innodb-background-encryption-threads.md)
* [InnoDB System Variables](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)
* [Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
