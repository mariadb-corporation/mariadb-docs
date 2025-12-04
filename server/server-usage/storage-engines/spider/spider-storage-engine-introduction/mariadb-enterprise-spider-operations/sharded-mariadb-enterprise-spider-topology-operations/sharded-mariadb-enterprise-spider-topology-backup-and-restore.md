# Sharded MariaDB Enterprise Spider Topology Backup and Restore

## Overview

When using Spider in the Sharded MariaDB Enterprise Spider topology, backup and restore operations can be performed using [MariaDB Backup](../../../../../backup-and-restore/mariadb-backup/mariadb-backup-overview.md) or [MariaDB Dump](../../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md). These operations must be performed on the Spider Node as well as on each Data Node.

## MariaDB Backup

MariaDB Backup can be used to perform backup operations on Spider deployments.

### Backup Spider with MariaDB Backup

[MariaDB Backup](../../../../../backup-and-restore/mariadb-backup/) can be used to create a physical backup of a Sharded MariaDB Enterprise Spider topology. MariaDB Backup must be used to backup the Spider Node and all Data Nodes. The Spider Node and Data Nodes must be locked to guarantee that the backups of the Spider Node and Data Nodes are consistent.

The backup of the Spider Node contains:

* Physical backup for Spider Tables
* Physical backup for tables that use InnoDB, Aria, MyISAM, and MyRocks
* Physical backup for any other database objects on the Spider Node

The backups of the Data Nodes contain:

* Physical backup for Data Tables
* Physical backup for tables that use InnoDB, Aria, MyISAM, and MyRocks
* Physical backup for any other database objects on the Data Node

The following procedure shows how to take a consistent backup of a Spider Node and Data Nodes deployed in a Sharded MariaDB Enterprise Spider topology.

1. On the Spider Node and on each Data Node, create a user account to perform the backup using the [CREATE USER](../../../../../../reference/sql-statements/account-management-sql-statements/create-user.md) and [GRANT](../../../../../../reference/sql-statements/account-management-sql-statements/grant.md) statements.

For MariaDB Enterprise Server 10.5 and later:

```sql
CREATE USER 'mariadb-backup'@'localhost'
   IDENTIFIED BY 'mb_passwd';

GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR
   ON *.*
   TO 'mariadb-backup'@'localhost';
```

2. On each Data Node, grant the user account Spider uses when operating on Data Nodes sufficient privileges to lock any Data Tables using the [GRANT](../../../../../../reference/sql-statements/account-management-sql-statements/grant.md) statement.

For example, on the hq\_server Data Node:

```sql
GRANT LOCK TABLES ON hq_sales.* TO 'spider_user'@'192.0.2.2';
```

On the eastern\_server Data Node:

```sql
GRANT LOCK TABLES ON eastern_sales.* TO 'spider_user'@'192.0.2.2';
```

On the western\_server Data Node:

```sql
GRANT LOCK TABLES ON western_sales.* TO 'spider_user'@'192.0.2.2';
```

3. On the Spider Node, acquire a read lock on Spider Tables using the LOCK TABLES statement:

```sql
LOCK TABLES spider_sharded_sales.invoices READ;
```

Keep this session open during the rest of the procedure.

The read lock will propagate to the Data Tables on each Data Node as well. The read locks will prevent the Data Tables from changing during the backup, so the backups on the Spider Node and Data Nodes are consistent.

4. On each Data Node, perform the backup using [MariaDB Backup](../../../../../backup-and-restore/mariadb-backup/mariadb-backup-options.md) .

With MariaDB Backup 10.5 and later, use the mariadb-backup command:

```bash
$ sudo mariadb-backup --backup \
   --target-dir=/data/backups/full \
   --user=mariadb-backup \
   --password='mb_passwd'
```

5. On the Spider Node, after backing up each Data Node, perform a backup with [MariaDB Backup](../../../../../backup-and-restore/mariadb-backup/mariadb-backup-overview.md) .

With MariaDB Backup 10.5 and later, use the mariadb-backup command:

```bash
$ sudo mariadb-backup --backup \
   --target-dir=/data/backups/full \
   --user=mariadb-backup \
   --password='mb_passwd'
```

6. On the Spider Node, after the backup is complete, in your original session, use the [UNLOCK TABLES](../../../../../../reference/sql-statements/transactions/transactions-unlock-tables.md) statement to release the table locks:

```sql
UNLOCK TABLES;
```

7. On the Spider Node and each of the Data Nodes, prepare each of the backups using MariaDB Backup.

With MariaDB Backup 10.5 and later, use the mariadb-backup command:

```bash
$ sudo mariadb-backup --prepare \
   --target-dir=/data/backups/full
```

The Spider Node and Data Nodes now each have a complete backup of the data directory. Backups should be tested to confirm they are complete and consistent.

## Restore Spider with MariaDB Backup

[MariaDB Backup](../../../../../backup-and-restore/mariadb-backup/mariadb-backup-overview.md) can restore a Sharded MariaDB Enterprise Spider topology from a backup taken with MariaDB Backup.

1. On the Spider Node and on each Data Node, stop the MariaDB Server process:

```bash
$ sudo systemctl stop mariadb
```

2. On the Spider Node and on each Data Node, empty the data directory:

```bash
$ sudo rm -fr /var/lib/mysql/*
```

3. On the Spider Node and on each Data Node, restore the backup for that server using MariaDB Backup.

With MariaDB Backup 10.5 and later, use the mariadb-backup command:

```bash
$ sudo mariadb-backup --copy-back \
   --target-dir=/data/backups/full
```

4. On the Spider Node and on each Data Node, confirm that the restored files are owned by the user that owns the MariaDB Server process:

```bash
$ sudo chown -R mysql:mysql /var/lib/mysql
```

5. On the Spider Node and on each Data Node, start the MariaDB Server process:

```bash
$ sudo systemctl start mariadb
```

6. On the Spider Node, query a Spider Table to test it:

```sql
SELECT * FROM spider_sharded_sales.invoices;
```

```
+-----------+------------+-------------+----------------------------+---------------+----------------+
| branch_id | invoice_id | customer_id | invoice_date               | invoice_total | payment_method |
+-----------+------------+-------------+----------------------------+---------------+----------------+
|         1 |          1 |           1 | 2020-05-10 12:35:10.000000 |       1087.23 | CREDIT_CARD    |
|         1 |          2 |           2 | 2020-05-10 14:17:32.000000 |       1508.57 | WIRE_TRANSFER  |
|         1 |          3 |           3 | 2020-05-10 14:25:16.000000 |        227.15 | CASH           |
|         2 |          1 |           2 | 2020-05-10 12:31:00.000000 |       1351.04 | CREDIT_CARD    |
|         2 |          2 |           2 | 2020-05-10 12:45:27.000000 |        162.11 | WIRE_TRANSFER  |
|         2 |          3 |           4 | 2020-05-10 13:11:23.000000 |        350.00 | CASH           |
|         3 |          1 |           5 | 2020-05-10 12:31:00.000000 |        111.50 | CREDIT_CARD    |
|         3 |          2 |           8 | 2020-05-10 12:45:27.000000 |       1509.23 | WIRE_TRANSFER  |
|         3 |          3 |           3 | 2020-05-10 13:11:23.000000 |       3301.66 | CASH           |
+-----------+------------+-------------+----------------------------+---------------+----------------+
```

## MariaDB Dump

[MariaDB Dump](../../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) generates backup files containing the SQL statements necessary to recreate the database. MariaDB Dump is included with MariaDB Server and can be used to backup databases in Spider deployments. The MariaDB Client can then be used to restore databases from a MariaDB Dump backup.

### Backup Spider with MariaDB Dump

[MariaDB Dump](../../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) can be used to create a logical backup of a Sharded MariaDB Enterprise Spider topology. MariaDB Dump must be used to backup the Spider Node and all Data Nodes. The Spider Node and Data Nodes must be locked to guarantee that the backups of the Spider Node and Data Nodes are consistent.

The backup of the Spider Node contains:

* Table definitions for Spider Tables
* Table definitions for all tables
* Table data for tables that use InnoDB, Aria, MyISAM, and MyRocks
* Definitions for any other user accounts, privileges, views, and triggers on the Spider Node

The backups of the Data Nodes contain:

* Table definitions for Data Tables
* Table definitions for all tables
* Table data for tables that use InnoDB, Aria, MyISAM, and MyRocks
* Definitions for any other user accounts, privileges, views, and triggers on the Data Node

The following procedure shows how to take a consistent backup of a Spider Node and Data Nodes deployed in a Sharded MariaDB Enterprise Spider topology.

1. On the Spider Node and on each Data Node, create a user account to perform the backup using the [CREATE USER](../../../../../../reference/sql-statements/account-management-sql-statements/create-user.md) and [GRANT](../../../../../../reference/sql-statements/account-management-sql-statements/grant.md) statements:

```sql
CREATE USER 'mariadb-dump'@'localhost'
   IDENTIFIED BY 'md_passwd';

GRANT SELECT, INSERT, SHOW VIEW, TRIGGER, CREATE, ALTER, EVENT, RELOAD, LOCK TABLES
   ON *.*
   TO 'mariadb-dump'@'localhost';
```

2. On each Data Node, grant the user account Spider uses to operate on the Data Nodes sufficient privileges to lock any Data Tables using the GRANT statement.

For example, on the hq\_server Data Node:

```sql
GRANT LOCK TABLES ON hq_sales.* TO 'spider_user'@'192.0.2.2';
```

On the `eastern_server` Data Node:

```sql
GRANT LOCK TABLES ON eastern_sales.* TO 'spider_user'@'192.0.2.2';
```

On the `western_server` Data Node:

```sql
GRANT LOCK TABLES ON western_sales.* TO 'spider_user'@'192.0.2.2';
```

3. On the Spider Node, acquire a read lock on Spider Tables using the [LOCK TABLES](../../../../../../reference/sql-statements/transactions/lock-tables.md) statement:

```sql
LOCK TABLES spider_sharded_sales.invoices READ;
```

Keep this session open during the rest of the procedure.

The read lock will propagate to the Data Tables on each Data Node as well. The read locks will prevent the Data Tables from changing during the backup, so the backups of the Spider Node and Data Nodes are consistent.

4. On each Data Node, perform the backup using MariaDB Dump.\
   With MariaDB Dump 10.5 and later, use the mariadb-dump command:

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

5. On the Spider Node, once the Data Nodes are backed up, perform a backup using MariaDB Dump.

With MariaDB Dump 10.5 and later, use the mariadb-dump command:

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

6. On the Spider Node, after the backups are complete, in your original session use the [UNLOCK TABLES](../../../../../../reference/sql-statements/transactions/transactions-unlock-tables.md) statement to release the table locks:

```sql
UNLOCK TABLES;
```

The Spider Node and the Data Node now each have a mariadb\_dump.sql backup file. This backup file contains the SQL statements needed to recreate the schema on the Spider Node and the schema and data on the Data Nodes. Backups should be tested to confirm they are complete and consistent.

## Restore Spider from MariaDB Dump

MariaDB Client can restore a Sharded MariaDB Enterprise Spider topology from a backup taken with [MariaDB Dump](../../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) backup.

1. Stop all traffic to the Spider Node and each Data Node.
2. On the Spider Node, restore the backup for that server using MariaDB Client.

With MariaDB Client 10.5 and later, use the mariadb command:

```bash
$ mariadb \
   --user=mariadb-dump \
   --password='md_passwd' \
   --ssl-verify-server-cert \
   --ssl-ca ~/mariadb_chain.pem \
   --default-character-set=utf8mb4 \
   < mariadb_dump.sql
```

3. On the Data Node, restore the backup for that server using MariaDB Client.

With MariaDB Client 10.5 and later, use the mariadb command:

```bash
$ mariadb \
   --user=mariadb-dump \
   --password='md_passwd' \
   --ssl-verify-server-cert \
   --ssl-ca ~/mariadb_chain.pem \
   --default-character-set=utf8mb4 \
   < mariadb_dump.sql
```

4. On the Spider Node, query a Spider Table to test it:

```sql
SELECT * FROM spider_sharded_sales.invoices;
```

```
+-----------+------------+-------------+----------------------------+---------------+----------------+
| branch_id | invoice_id | customer_id | invoice_date               | invoice_total | payment_method |
+-----------+------------+-------------+----------------------------+---------------+----------------+
|         1 |          1 |           1 | 2020-05-10 12:35:10.000000 |       1087.23 | CREDIT_CARD    |
|         1 |          2 |           2 | 2020-05-10 14:17:32.000000 |       1508.57 | WIRE_TRANSFER  |
|         1 |          3 |           3 | 2020-05-10 14:25:16.000000 |        227.15 | CASH           |
|         2 |          1 |           2 | 2020-05-10 12:31:00.000000 |       1351.04 | CREDIT_CARD    |
|         2 |          2 |           2 | 2020-05-10 12:45:27.000000 |        162.11 | WIRE_TRANSFER  |
|         2 |          3 |           4 | 2020-05-10 13:11:23.000000 |        350.00 | CASH           |
|         3 |          1 |           5 | 2020-05-10 12:31:00.000000 |        111.50 | CREDIT_CARD    |
|         3 |          2 |           8 | 2020-05-10 12:45:27.000000 |       1509.23 | WIRE_TRANSFER  |
|         3 |          3 |           3 | 2020-05-10 13:11:23.000000 |       3301.66 | CASH           |
+-----------+------------+-------------+----------------------------+---------------+----------------+
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
