# Federated MariaDB Enterprise Spider Topology Backup and Restore

## Overview

When using Spider in the Federated MariaDB Enterprise Spider topology, backup and restore operations can be performed using MariaDB Backup or MariaDB Dump. These operations must be performed on the Spider Node and the Data Node.

## MariaDB Backup

MariaDB Backup can be used to perform backup operations on Spider deployments.

### Backup Spider with MariaDB Backup

MariaDB Backup can be used to create a physical backup of a Federated MariaDB Enterprise Spider topology. MariaDB Backup must be used to backup the Spider Node and the Data Node. The Spider Node and Data Node must be locked to guarantee that the backups of the Spider Node and Data Node are consistent.

The backup of the Spider Node contains:

* Physical backup for Spider Tables
* Physical backup for tables that use InnoDB, Aria, MyISAM, and MyRocks
* Physical backup for any other database objects on the Spider Node

The backup of the Data Node contains:

* Physical backup for Data Tables
* Physical backup for tables that use InnoDB, Aria, MyISAM, and MyRocks
* Physical backup for any other database objects on the Data Node

The following procedure shows how to take a consistent backup of a Spider Node and a Data Node deployed in a Spider Federated MariaDB Enterprise Spider topology.

1. On the Spider Node and on the Data Node, create a user account to perform the backup using the [CREATE USER](../../../../../../reference/sql-statements/account-management-sql-statements/create-user.md) and [GRANT](../../../../../../reference/sql-statements/account-management-sql-statements/grant.md) statements:

```sql
CREATE USER 'mariadb-backup'@'localhost'
   IDENTIFIED BY 'mb_passwd';

GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR
   ON *.*
   TO 'mariadb-backup'@'localhost';
```

2. On the Data Node, grant the user account Spider uses to operate on the Data Node sufficient privileges to lock the Data Tables using the [GRANT](../../../../../../reference/sql-statements/account-management-sql-statements/grant.md) statement.

For example, on the hq\_server Data Node:

```sql
GRANT LOCK TABLES ON hq_sales.* TO 'spider_user'@'192.0.2.2';
```

3. On the Spider Node, acquire a read lock on Spider Tables using the [LOCK TABLES](../../../../../../reference/sql-statements/transactions/lock-tables.md) statement:

```sql
LOCK TABLES spider_federated_sales.invoices READ;
```

Keep this session open during the rest of the procedure.

The read lock will propagate to the Data Tables on the Data Node. The read locks will prevent the Data Tables from changing during the backup, so the backups of the Spider Node and the Data Node are consistent.

4. On the Data Node, perform the backup using MariaDB Backup:

```bash
$ sudo mariadb-backup --backup \
   --target-dir=/data/backups/full \
   --user=mariadb-backup \
   --password='mb_passwd'
```

5. When the Data Node backup is complete, perform the backup on the Spider Node using MariaDB Backup:

```bash
$ sudo mariadb-backup --backup \
   --target-dir=/data/backups/full \
   --user=mariadb-backup \
   --password='mb_passwd'
```

6. When the Spider Node backup is complete, release the table locks in your original session using the [UNLOCK TABLES](../../../../../../reference/sql-statements/transactions/transactions-unlock-tables.md) statement:

```sql
UNLOCK TABLES;
```

7. On the Spider Node and the Data Node, prepare each of the backups using MariaDB Backup:

```bash
$ sudo mariadb-backup --prepare \
   --target-dir=/data/backups/full
```

The Spider Node and the Data Node now have a complete backup of the data directory. Backups should be tested to confirm they are complete and consistent.

### Restoring Spider with MariaDB Backup

MariaDB Backup can restore a Federated MariaDB Enterprise Spider topology from a backup taken with MariaDB Backup.

1. On the Spider Node and on the Data Node, stop the MariaDB Server process:

```bash
$ sudo systemctl stop mariadb
```

2. On the Spider Node and on the Data Node, empty the data directory:

```bash
$ sudo rm -fr /var/lib/mysql/*
```

3. On the Spider Node and on the Data Node, restore the backup for that server using MariaDB Backup:

```bash
$ sudo mariadb-backup --copy-back \
   --target-dir=/data/backups/full
```

4. On the Spider Node and on the Data Node, confirm that the restored files are owned by the user that owns the MariaDB Server process:

```bash
$ sudo chown -R mysql:mysql /var/lib/mysql
```

5. On the Spider Node and on the Data Node, start the MariaDB Server process:

```bash
$ sudo systemctl start mariadb
```

6. On the Spider Node, query a Spider Table to test it:

```sql
SELECT * FROM spider_hq_sales.invoices;
```

```
+-----------+------------+-------------+----------------------------+---------------+----------------+
| branch_id | invoice_id | customer_id | invoice_date               | invoice_total | payment_method |
+-----------+------------+-------------+----------------------------+---------------+----------------+
|         1 |          1 |           1 | 2020-05-10 12:35:10.000000 |       1087.23 | CREDIT_CARD    |
|         1 |          2 |           2 | 2020-05-10 14:17:32.000000 |       1508.57 | WIRE_TRANSFER  |
|         1 |          3 |           3 | 2020-05-10 14:25:16.000000 |        227.15 | CASH           |
+-----------+------------+-------------+----------------------------+---------------+----------------+
```

## MariaDB Dump

[MariaDB Dump](../../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) generates backup files containing the SQL statements necessary to recreate the database. [MariaDB Dump](../../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) is included with MariaDB Enterprise Server and can be used to backup databases in Spider deployments. The MariaDB Client can then be used to restore databases from a [MariaDB Dump backup](../../../../../../mariadb-quickstart-guides/mariadb-backup-guide.md).

### Backing Up Spider with MariaDB Dump

MariaDB Dump can be used to create a logical backup of a Federated MariaDB Enterprise Spider topology. MariaDB Dump must be used to backup the Spider Node and the Data Node. The Spider Node and Data Node must be locked to guarantee that the backups of the Spider Node and Data Node are consistent.

The backup of the Spider Node contains:

* Table definitions for Spider Tables
* Table definitions for all tables
* Table data for tables that use InnoDB, Aria, MyISAM, and MyRocks
* Definitions for any other user accounts, privileges, views, and triggers on the Spider Node

The backup of the Data Node contains:

* Table definitions for Data Tables
* Table definitions for all tables
* Table data for tables that use InnoDB, Aria, MyISAM, and MyRocks
* Definitions for any other user accounts, privileges, views, and triggers on the Data Node

The following procedure shows how to take a consistent backup of a Spider Node and a Data Node deployed in a Federated MariaDB Enterprise Spider topology.

1. On the Spider Node and on the Data Node, create a user account to perform the backup using the [CREATE USER](../../../../../../reference/sql-statements/account-management-sql-statements/create-user.md) and [GRANT](../../../../../../reference/sql-statements/account-management-sql-statements/grant.md) statements:

```sql
CREATE USER 'mariadb-dump'@'localhost'
   IDENTIFIED BY 'md_passwd';

GRANT SELECT, INSERT, SHOW VIEW, TRIGGER, CREATE, ALTER, EVENT, RELOAD, LOCK TABLES
   ON *.*
   TO 'mariadb-dump'@'localhost';
```

2. On the Data Node, grant the user account Spider uses to operate on the Data Node sufficient privileges to lock the Data Tables using the GRANT statement.

For example, on the hq\_server Data Node:

```sql
GRANT LOCK TABLES ON hq_sales.* TO 'spider_user'@'192.0.2.2';
```

3. On the Spider Node, acquire a read lock on Spider Tables using the LOCK TABLES statement:

```sql
LOCK TABLES spider_federated_sales.invoices READ;
```

Keep this session open during the rest of the procedure.

The read lock will propagate to the Data Tables on the Data Node. The read locks will prevent the Data Tables from receiving any changes during the backup, which ensures the backups of the Spider Node and the Data Node are consistent.

4. On the Data Node, perform the backup using MariaDB Dump:

```bash
$ mariadb-dump \
   --user=mariadb-dump \
   --password='md_passwd' \
   --ssl-verify-server-cert \
   --ssl-ca ~/mariadb_chain.pem \
   --all-databases \
   --single-transaction \
   --default-character-set=utf8mb4 \
   > mariadb_dump.sql
```

5. When the Data Node has been backed up, perform the backup on the Spider Node using MariaDB Dump:

```bash
$ mariadb-dump \
   --user=mariadb-dump \
   --password='md_passwd' \
   --ssl-verify-server-cert \
   --ssl-ca ~/mariadb_chain.pem \
   --all-databases \
   --single-transaction \
   --default-character-set=utf8mb4 \
   > mariadb_dump.sql
```

6. When the Spider Node backup is complete, release the table locks in your original session using the UNLOCK TABLES statement:

```
UNLOCK TABLES;
```

The Spider Node and the Data Node now each have a mariadb\_dump.sql backup file. This backup file contains the SQL statements needed to recreate the schema on the Spider Node and the schema and data on the Data Node. Backups should be tested to confirm they are complete and consistent.

### Restoring Spider from MariaDB Dump

MariaDB Client can restore a Federated MariaDB Enterprise Spider topology from a backup taken with MariaDB Dump backup.

1. Stop all traffic to the Spider Node and the Data Node.
2. On the Spider Node, restore the backup for that server using MariaDB Client:

```bash
$ mariadb \
   --user=mariadb-dump \
   --password='md_passwd' \
   --ssl-verify-server-cert \
   --ssl-ca ~/mariadb_chain.pem \
   --default-character-set=utf8mb4 \
   < mariadb_dump.sql
```

3. On the Data Node, restore the backup for that server using MariaDB Client:

```bash
$ mariadb \
   --user=mariadb-dump \
   --password='md_passwd' \
   --ssl-verify-server-cert \
   --ssl-ca ~/mariadb_chain.pem \
   --default-character-set=utf8mb4 \
   < mariadb_dump.sql
```

On the Spider Node, query a Spider Table to test it:

```sql
SELECT * FROM spider_hq_sales.invoices;
```

```
+-----------+------------+-------------+----------------------------+---------------+----------------+
| branch_id | invoice_id | customer_id | invoice_date               | invoice_total | payment_method |
+-----------+------------+-------------+----------------------------+---------------+----------------+
|         1 |          1 |           1 | 2020-05-10 12:35:10.000000 |       1087.23 | CREDIT_CARD    |
|         1 |          2 |           2 | 2020-05-10 14:17:32.000000 |       1508.57 | WIRE_TRANSFER  |
|         1 |          3 |           3 | 2020-05-10 14:25:16.000000 |        227.15 | CASH           |
+-----------+------------+-------------+----------------------------+---------------+----------------+
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
