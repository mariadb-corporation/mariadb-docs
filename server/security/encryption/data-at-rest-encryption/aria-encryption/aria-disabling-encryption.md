---
description: >-
  Instructions for safely disabling encryption on Aria tables, emphasizing the
  need to rebuild tables to an unencrypted state before removing key management
  plugins.
---

# Aria: Disabling Encryption

## Overview

This guide provides instructions for safely disabling encryption for the Aria storage engine, including user-created tables and internal on-disk temporary tables.

To fully disable encryption, you must set the relevant system variables and then rebuild each table to an unencrypted state.

{% hint style="warning" %}
**Important Safety Precautions**

* Do not remove your Encryption Key Management plugin yet. MariaDB must be able to read the existing encrypted data to rewrite it in an unencrypted state.
* Maintain configurations. Keep your key management settings in place until the very last step of the process.
{% endhint %}

{% stepper %}
{% step %}
### Disable encryption for new data.

First, prevent MariaDB from encrypting any new data by updating the global system variables.

#### User-Created Tables

Set `aria_encrypt_tables` to `OFF`. This ensures that any new Aria tables created or existing tables rebuilt from this point forward will be unencrypted.

```sql
SET GLOBAL aria_encrypt_tables = OFF;
```

To make this change persistent across server restarts, add the following to your [MariaDB configuration file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) (for instance, `my.cnf`):

```ini
[mysqld]
aria_encrypt_tables = OFF
```

#### Internal On-Disk Temporary Tables

MariaDB creates internal temporary tables using the Aria engine when `aria_used_for_temp_tables` is set to `ON`. To ensure these are no longer encrypted, set:

```sql
SET GLOBAL encrypt_tmp_disk_tables = OFF;
```
{% endstep %}

{% step %}
### Identify encrypted Aria tables.

Aria does not use background encryption threads (unlike InnoDB). Therefore, tables already on disk will remain encrypted until you manually rebuild them.

Run the following query to identify which tables need to be rebuilt:

```sql
SELECT TABLE_SCHEMA, TABLE_NAME 
FROM information_schema.TABLES 
WHERE ENGINE = 'Aria' 
  AND ROW_FORMAT = 'PAGE' 
  AND TABLE_SCHEMA NOT IN ('information_schema', 'performance_schema', 'sys')
  AND (CREATE_OPTIONS LIKE '%`encrypted`=yes%' OR CREATE_OPTIONS LIKE '%`encrypted`=1%');
```
{% endstep %}

{% step %}
### Rebuild tables to decrypt.

To decrypt the tables identified in the previous step, you must rebuild them using an `ALTER TABLE` statement. This causes MariaDB to rewrite the data (`.MAD`) and index (`.MAI`) files in an unencrypted format.

#### Option A: Manual Rebuild (Single Table)

Use the following statement to rebuild a specific table:

```sql
ALTER TABLE db_name.table_name ENGINE=Aria, ALGORITHM=COPY;
```

#### Option B: Generate Rebuild Statements (Bulk)

You can generate the DDL for all encrypted Aria tables at once using this query:

```sql
SELECT CONCAT('ALTER TABLE `', table_schema, '`.`', table_name, 
              '` ENGINE=Aria, ALGORITHM=COPY;') AS ddl
FROM information_schema.tables
WHERE ENGINE='Aria' 
  AND TABLE_SCHEMA NOT IN ('mysql','information_schema','performance_schema','sys')
  AND (CREATE_OPTIONS LIKE '%`encrypted`=yes%' OR CREATE_OPTIONS LIKE '%`encrypted`=1%');
```
{% endstep %}

{% step %}
### Verify and clean up.

* Verify: Run the query from Step 2 again to ensure no encrypted Aria tables remain.
* Remove Plugins (optional): Once all Aria tables (and any InnoDB tables or binary logs) are decrypted, you can safely remove the Encryption Key Management plugin from your configuration file and restart the server.
{% endstep %}
{% endstepper %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
