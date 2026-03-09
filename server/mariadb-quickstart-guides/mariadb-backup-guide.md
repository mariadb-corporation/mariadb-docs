---
description: >-
  Complete MariaDB backup and recovery guide. Complete resource for backup
  methods, mariabackup usage, scheduling, and restoration for production use.
---

# Making Backups with mariadb-dump Guide

This guide explains how to use the `mariadb-dump` utility to create essential backup (dump) files of your MariaDB data. Learn to effectively back up all databases, specific databases, or individual tables, ensuring your data is protected and can be restored when needed.

### About `mariadb-dump`

`mariadb-dump` is a command-line utility included with MariaDB for creating logical backups of your databases. It was previously known as `mysqldump`, which often still works as a symbolic link.

**Key Advantages:**

* **No Server Shutdown:** Backups can be performed while the MariaDB server is running.
* **SQL Output:** It generates a `.sql` file (a "dump file") containing SQL statements (`CREATE TABLE`, `INSERT`, etc.) necessary to reconstruct the databases and data.

All `mariadb-dump` commands are executed from your system's command-line shell, not within the `mariadb` client.

### Backing Up All Databases

To export all databases managed by your MariaDB server:

```bash
mariadb-dump --user=admin_backup --password --lock-tables --all-databases > /data/backup/dbs_alldatabases.sql
```

* `--user=admin_backup`: Specifies the MariaDB user performing the backup (this user needs appropriate privileges, typically at least `SELECT` and `LOCK TABLES`).
* `--password`: Prompts for the user's password. For use in scripts where prompting is not possible, you can use `--password=yourpassword` (note the absence of a space and the security implication of having the password in a script or command history).
* `--lock-tables` (or `-x`): Locks all tables across all databases before starting the backup to ensure data consistency. The lock is released once the dump is complete for each table. For transactional tables like InnoDB, using `--single-transaction` is often preferred as it provides a consistent snapshot without prolonged locking of all tables.
* `--all-databases` (or `-A`): Specifies that all databases should be dumped.
* `>` `/data/backup/dbs_alldatabases.sql`: Redirects the output (the SQL statements) to the specified file. Ensure the path exists and the user running the command has write permissions.

**Commonly Used Option for Efficiency:**

* `--extended-insert` (or `-e`): Creates `INSERT` statements that include multiple rows per statement. This generally results in a smaller dump file and faster restores. This option is often enabled by default but can be explicitly stated.

**Example with long options and password in script:**

```bash
mariadb-dump --user=admin_backup --password=yoursecurepassword --lock-tables --extended-insert --all-databases > /data/backup/dbs_alldatabases.sql
```

### Backing Up a Single Database

Backing up databases individually can result in smaller, more manageable dump files and allow for more flexible backup schedules.

```bash
mariadb-dump --user=admin_backup --password --lock-tables --extended-insert --databases your_database_name > /data/backup/your_database_name.sql
```

* `--databases` (or `-B`): Followed by the name of the database to dump.
*   To back up multiple specific databases, list their names separated by spaces after the `--databases` option:

    ```bash
    mariadb-dump --user=admin_backup --password --lock-tables --extended-insert --databases db1_name db2_name > /data/backup/selected_databases.sql
    ```

### Backing Up Specific Tables

For very large databases, or if only certain tables change frequently, you might back up individual tables.

```bash
mariadb-dump --user=admin_backup --password --lock-tables --extended-insert your_database_name table_name1 table_name2 > /data/backup/your_database_name_selected_tables.sql
```

* First, specify the database name (`your_database_name`).
* Then, list one or more table names (`table_name1`, `table_name2`) separated by spaces.
* Note that the `--databases` option is _not_ used when dumping specific tables in this manner.

### Important Considerations and Best Practices

* **User Privileges:** The MariaDB user specified with `--user` needs at least `SELECT` privileges for the tables being dumped. `LOCK TABLES` privilege is needed if using `--lock-tables`. `RELOAD` or `FLUSH_TABLES` might be needed for options like `--flush-logs` or `--master-data`. For `--single-transaction`, `PROCESS` and `RELOAD` might be required. A user with global `SELECT`, `LOCK TABLES`, `SHOW VIEW`, `EVENT`, and `TRIGGER` privileges is often used for backups.
*   **Consistency with InnoDB:** For databases primarily using InnoDB tables, consider using the `--single-transaction` option instead of `--lock-tables`. This option starts a transaction before dumping and reads data from a consistent snapshot without locking the tables for extended periods, allowing concurrent reads and writes.Bash

    ```
    mariadb-dump --user=admin_backup --password --single-transaction --extended-insert --databases your_innodb_database > /data/backup/your_innodb_database.sql
    ```
* **Practice Makes Perfect:** `mariadb-dump` is powerful but can have many options. Practice using it on a test database or server to become comfortable with its usage and to verify that your backup strategy works as expected.
* **Test Your Backups:** Regularly test your backup files by restoring them to a non-production environment to ensure they are valid and can be used for recovery.
* **Restoration:** To learn how to restore data from these dump files, see the "[Data Restoration Guide](mariadb-restore-guide.md)".
* **Security:** Store backup files in a secure location. If passwords are included in scripts, ensure the script files have restricted permissions.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
