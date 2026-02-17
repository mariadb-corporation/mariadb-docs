---
description: >-
  Instructions for safely disabling encryption on InnoDB tables, emphasizing the
  critical need to decrypt all tablespaces and redo logs using background
  threads or ALTER TABLE.
---

# InnoDB: Disabling Encryption

## Overview

Decryption for InnoDB is more complex than Aria because it involves background threads and the Redo Log.

This guide covers the process for safely decrypting InnoDB tablespaces, the system tablespace, and the Redo Log.

{% hint style="warning" %}
**Important Safety Precautions**

* Do Not Remove Plugins Early: Keep your Key Management plugin configured and loaded until the very end. If you remove the keys before decryption is complete, the encrypted data will become permanently inaccessible.
* Order Matters: You must decrypt all tablespaces and the Redo Log before disabling the encryption plugin.
{% endhint %}

{% stepper %}
{% step %}
### Disable automatic encryption.

To stop the server from encrypting new tables and to begin the background decryption process for "automatically" encrypted tables (those where `ENCRYPTED=DEFAULT`), update the global system variables.

```sql
-- Disable encryption for new tables and the system tablespace
SET GLOBAL innodb_encrypt_tables = OFF;

-- Enable encryption threads to perform the decryption work
SET GLOBAL innodb_encryption_threads = 4;

-- Force rotation to unencrypted state by setting age to 1
SET GLOBAL innodb_encryption_rotate_key_age = 1;
```

To make these changes persistent, update your [MariaDB configuration file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mysqld]
innodb_encrypt_tables = OFF
innodb_encryption_threads = 4
innodb_encryption_rotate_key_age = 1
```
{% endstep %}

{% step %}
### Decrypt manually encrypted tables.

Tables created with the explicit option `ENCRYPTED=YES` are not always automatically decrypted by background threads. You must manually issue an `ALTER TABLE` statement for these.

#### Identify Manually Encrypted Tables

Run this query to find tables that require manual decryption:

```sql
SELECT TABLE_SCHEMA, TABLE_NAME 
FROM information_schema.TABLES 
WHERE ENGINE='InnoDB' 
  AND (CREATE_OPTIONS LIKE '%ENCRYPTED=YES%' OR CREATE_OPTIONS LIKE '%ENCRYPTION="Y"%');
```

#### Perform Decryption

For each table identified, run:

```sql
ALTER TABLE db_name.table_name ENCRYPTION='N';
```
{% endstep %}

{% step %}
### Decrypt the redo log.

The Redo Log must be decrypted separately. This requires a server restart.

1.  Add the following to your MariaDB configuration file:

    ```ini
    [mysqld]
    innodb_encrypt_log = OFF
    ```
2. Restart the MariaDB Server.&#x20;
3. Upon restart, MariaDB begins writing unencrypted data to the Redo Log.
{% endstep %}

{% step %}
### Monitor and verify decryption status.

Before removing your encryption keys, you must verify that no tablespaces remain encrypted.

#### Check Background Progress

Monitor the `INNODB_TABLESPACES_ENCRYPTION` table. Decryption is complete when the count reaches `0`.

```sql
SELECT COUNT(*) AS "Encrypted_Tablespaces" 
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION 
WHERE ENCRYPTION_SCHEME != 0 OR ROTATING_OR_FLUSHING != 0;
```

#### Verify Individual Tables

Ensure that no tables show encryption in their creation options:

```sql
SELECT TABLE_NAME, CREATE_OPTIONS 
FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'your_database_name';
```
{% endstep %}

{% step %}
### Clean up.

Once the count of encrypted tablespaces is `0` and the Redo Log has been rotated (after restart), you can safely:

1. Remove the Encryption Key Management plugin settings from your configuration file.
2. Restart the MariaDB Server one final time.
{% endstep %}
{% endstepper %}



<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
