---
description: >-
  Complete Restoring Data from Dump Files Guide guide for MariaDB. Complete
  resource with setup instructions, configuration, usage examples, and best
  practices.
---

# Restoring Data from Dump Files Guide

This guide explains how to restore your MariaDB data from backup files created with `mariadb-dump`. Learn the basic restoration process using the `mariadb` client and a specific technique for selectively restoring a single table while minimizing data loss on other tables.

It's important to understand that `mariadb-dump` is used for creating backup (dump) files, while the `mariadb` client utility is used for restoring data from these files. The dump file contains SQL statements that, when executed, recreate the database structure and/or data.

### Basic Restoration Process

To restore a dump file, you direct the `mariadb` client to execute the SQL statements contained within the file.

```bash
mariadb --user your_username --password < /path/to/your/backupfile.sql
```

* Replace `your_username` with your MariaDB username and `/path/to/your/backupfile.sql` with the actual path to your dump file.
* You will be prompted for the password for `your_username`.
* The `<` symbol is a standard input (STDIN) redirect, feeding the contents of `backupfile.sql` to the `mariadb` client.
*   Often, the dump file itself contains `CREATE DATABASE IF NOT EXISTS` and `USE database_name;` statements, so a specific database doesn't always need to be named on the command line during restore. If your dump file restores to a specific database, ensure that user has permissions to it. If the dump file does _not_ specify a database, you might need to create the database first and then run:

    ```bash
    mariadb --user your_username --password your_database_name < /path/to/your/backupfile.sql
    ```

### Important Considerations Before Restoring

* **Data Overwriting:** Restoring a dump file will execute the SQL statements within it. If the dump file contains `DROP TABLE` and `CREATE TABLE` statements (common for full backups), existing tables with the same names will be dropped and recreated, leading to loss of any data added or changed since the backup was made.
* **Backup Age:** If your dump file is several days old, restoring it entirely could revert all data in the affected tables/databases to that older state. This can be disastrous if only a small portion of data was lost and the rest has been actively updated.

Always ensure you understand the contents of the dump file and the potential impact before initiating a restore, especially on a production system. Consider testing the restore on a non-production environment first if possible.

### Restoring a Single Table Selectively

If only one table has been lost or corrupted and your backup file contains an entire database (or multiple tables), a full restore might overwrite recent, valid data in other tables. Here’s a method to restore only a specific table using a temporary user with restricted privileges:

1. **Create a Temporary User:** Create a MariaDB user specifically for this restore operation.
2.  **Grant Limited Privileges:**

    * Grant this temporary user the minimal privileges needed for the dump file to execute up to the point of restoring your target table. This might be `SELECT` on all tables in the database if the dump file checks other tables, or simply the ability to `USE` the database.
    * Then, grant `ALL PRIVILEGES` (or specific necessary privileges like `CREATE`, `DROP`, `INSERT`, `SELECT`) _only_ on the specific table you want to restore.

    Example SQL to create a temporary user and grant permissions (replace placeholders):

    ```sql
    -- Connect to MariaDB as an administrative user (e.g., root)
    CREATE USER 'admin_restore_temp'@'localhost' IDENTIFIED BY 'its_very_secure_pwd';

    -- Grant general SELECT on the database (might be needed if dump file structure requires it)
    -- Or, if not needed, ensure the user can at least USE the database.
    GRANT SELECT ON your_database_name.* TO 'admin_restore_temp'@'localhost';

    -- Grant full privileges ONLY on the table to be restored
    GRANT ALL PRIVILEGES ON your_database_name.table_to_restore TO 'admin_restore_temp'@'localhost';

    FLUSH PRIVILEGES;
    ```
3.  Restore Using the Temporary User and `--force`:

    Use the mariadb client with the temporary user and the --force option. The --force option tells MariaDB to continue executing statements in the dump file even if some SQL errors occur. Errors will occur for operations on tables where admin\_restore\_temp lacks permissions, but operations on table\_to\_restore (where permissions were granted) should succeed.

    Bash

    ```bash
    mariadb --user admin_restore_temp --password --force your_database_name < /path/to/your/fulldumpfile.sql
    ```

    You will be prompted for the password of `admin_restore_temp`.
4. **Verify Restoration:** Check that `table_to_restore` has been correctly restored.
5.  **Clean Up:** Drop the temporary user once the restoration is confirmed:

    ```sql
    DROP USER 'admin_restore_temp'@'localhost';
    ```

This method helps to isolate the restore operation to the intended table, protecting other data from being inadvertently reverted to an older state.

{% @marketo/form formId="4316" %}
