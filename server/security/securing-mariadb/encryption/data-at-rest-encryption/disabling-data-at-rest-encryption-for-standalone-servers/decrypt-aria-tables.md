---
description: >-
  This page describes how to decrypt datdata at resta-at-rest for tables that
  use the Aria storage engine.
---

# Decrypt Aria Tables

If you have Aria tables encrypted, you must first decrypt them:

```sql
ALTER TABLE my_table ENCRYPTED=NO;
```

Repeat this for each Aria table that is encrypted.

{% hint style="info" %}
For more information, refer to  [`MDEV-17268`](https://jira.mariadb.org/browse/MDEV-17268).
{% endhint %}

* **Ensure the server can currently read encrypted data**\
  Keep your key management/encryption plugin configured and loaded so MariaDB can read existing encrypted Aria tables. Don’t remove the plugin yet. [MariaDB](https://mariadb.com/docs/server/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins?utm_source=chatgpt.com)
*   **Turn off Aria encryption for future writes**\
    Set the global variable to off and restart if set in config:

    ```sql
    -- Immediate effect for the running instance
    SET GLOBAL aria_encrypt_tables = OFF;
    ```

    Also set in the option file to persist:

    ```
    [mysqld]
    aria_encrypt_tables=OFF
    ```

    With encryption disabled, any newly **rebuilt** Aria table will be written unencrypted. [MariaDB](https://mariadb.com/kb/en/aria-enabling-encryption/?utm_source=chatgpt.com)
*   **Rebuild Aria tables to rewrite them unencrypted**\
    Rebuilding causes MariaDB to rewrite data and index files (.MAD/.MAI) in the current (now unencrypted) mode. Typical ways to rebuild:

    * `ALTER TABLE t ENGINE=Aria;`
    * `ALTER TABLE t ALGORITHM=COPY;` (forces a copy/rebuild)
    * `OPTIMIZE TABLE t;` (for Aria this rebuilds the table)

    Example (single table):

    ```sql
    ALTER TABLE db1.my_aria_table ENGINE=Aria, ALGORITHM=COPY, LOCK=SHARED;
    ```
*   **Repeat for all Aria tables you want decrypted**\
    Generate statements for every Aria table:

    ```sql
    SELECT CONCAT('ALTER TABLE `', table_schema, '`.`', table_name, 
                  '` ENGINE=Aria, ALGORITHM=COPY;') AS ddl
    FROM information_schema.tables
    WHERE ENGINE='Aria'
      AND table_schema NOT IN ('mysql','information_schema','performance_schema','sys');
    ```

    Review and run the generated DDL. (System tables may use Aria in newer releases—handle with care.) [MariaDB](https://mariadb.com/docs/platform/mariadb-platform-quickstart-guides/security?utm_source=chatgpt.com)
* **Verify and then remove encryption dependencies (optional)**\
  Once all targeted Aria tables are rebuilt and unencrypted, and you have no other encrypted assets relying on the plugin (e.g., InnoDB encryption, binlog encryption), you can remove or disable the key management/encryption plugin.
