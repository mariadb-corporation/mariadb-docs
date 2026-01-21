---
description: >-
  Introduction to encrypting Aria tables, covering the necessary system
  variables (`aria_encrypt_tables`, `encrypt_tmp_disk_tables`) and how to verify
  encryption status by inspecting data files.
---

# Aria Encryption Overview

MariaDB can encrypt data in tables that use the [Aria storage engine](../../../../../server-usage/storage-engines/aria/). This includes both user-created tables and internal on-disk temporary tables that use the Aria storage engine. This ensures that your Aria data is only accessible through MariaDB.

For encryption with the InnoDB and XtraDB storage engines, see [Encrypting Data for InnoDB/XtraDB](../innodb-encryption/innodb-encryption-overview.md).

## Basic Configuration

In order to enable encryption for tables using the [Aria storage engine](../../../../../server-usage/storage-engines/aria/), there are a couple server system variables that you need to set and configure. Most users will want to set [aria\_encrypt\_tables](../../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_encrypt_tables) and [encrypt\_tmp\_disk\_tables](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_disk_tables).

Users of data-at-rest encryption will also need to have a [key management and encryption plugin](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) configured. Some examples are [File Key Management Plugin](../key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) and [AWS Key Management Plugin](../key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md).

```
[mariadb]
...

# File Key Management
plugin_load_add = file_key_management
file_key_management_filename = /etc/mysql/encryption/keyfile.enc
file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
file_key_management_encryption_algorithm = AES_CTR

# Aria Encryption
aria_encrypt_tables=ON
encrypt_tmp_disk_tables=ON
```

## Determining Whether a Table is Encrypted

The [InnoDB storage engine](../../../../../server-usage/storage-engines/innodb/) has the [information\_schema.INNODB\_TABLESPACES\_ENCRYPTION table](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_encryption-table.md) that can be used to get information about which tables are encrypted. Aria does not currently have anything like that (see [MDEV-17324](https://jira.mariadb.org/browse/MDEV-17324) about that).

To determine whether an Aria table is encrypted, you currently have to search the data file for some plain text that you know is in the data.

For example, let's say that we have the following table:

```sql
SELECT * FROM db1.aria_tab LIMIT 1;
+----+------+
| id | str  |
+----+------+
|  1 | str1 |
+----+------+
1 row IN SET (0.00 sec
```

Then, we could search the data file that belongs to `db1.aria_tab` for `str1` using a command-line tool, such as [strings](https://linux.die.net/man/1/strings):

```bash
$ sudo strings /var/lib/mysql/db1/aria_tab.MAD | grep "str1"
str1
```

If you can find the plain text of the string, then you know that the table is not encrypted.

## Encryption and the Aria Log

Only Aria tables are currently encrypted. The [Aria log](../../../../../server-usage/storage-engines/aria/aria-faq.md#differences-between-aria-and-myisam) is not yet encrypted. See [MDEV-8587](https://jira.mariadb.org/browse/MDEV-8587) about that.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
