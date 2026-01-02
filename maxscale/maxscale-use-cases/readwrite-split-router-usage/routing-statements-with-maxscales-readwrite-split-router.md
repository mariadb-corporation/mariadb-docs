---
description: >-
  Understand the routing logic of the readwritesplit router. This guide explains
  how MaxScale identifies write statements for the primary and distributes reads
  to replicas.
---

# Routing Statements with MaxScale's Read/Write Split Router

The [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) uses well-defined rules to determine whether a statement can be routed to a replica server, or whether it needs to be routed to the primary server. Application designers must understand these rules to ensure that the router can properly load balance queries.

## Statements Routed to the Primary Server

The following statements are routed to the primary server:

* Queries that write to the database. For example, this includes, but is not limited to, the following statements:
  * [INSERT](../../../server/reference/sql-statements/data-manipulation/inserting-loading-data/insert.md)
  * [INSERT ... RETURNING](../../../server/reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning.md)
  * [UPDATE](../../../server/reference/sql-statements/data-manipulation/changing-deleting-data/update.md)
  * [DELETE](../../../server/reference/sql-statements/data-manipulation/changing-deleting-data/delete.md)
  * [REPLACE](../../../server/reference/sql-statements/data-manipulation/changing-deleting-data/replace.md)
  * [REPLACE ... RETURNING](../../../server/reference/sql-statements/data-manipulation/changing-deleting-data/replacereturning.md)
  * [LOAD DATA INFILE](../../../server/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)
* Queries that modify the database (DDL) For example, this includes, but is not limited to, the following statements:
  * [CREATE DATABASE](../../../server/reference/sql-statements/data-definition/create/create-database.md)
  * [ALTER DATABASE](../../../server/reference/sql-statements/data-definition/alter/alter-database.md)
  * [DROP DATABASE](../../../server/reference/sql-statements/data-definition/drop/drop-database.md)
  * [CREATE TABLE](../../../server/reference/sql-statements/data-definition/create/create-table.md)
  * [ALTER TABLE](../../../server/reference/sql-statements/data-definition/alter/alter-table/)
  * [DROP TABLE](../../../server/reference/sql-statements/data-definition/drop/drop-table.md)
  * [CREATE VIEW](../../../server/server-usage/views/create-view.md)
  * [ALTER VIEW](../../../server/server-usage/views/alter-view.md)
  * [DROP VIEW](../../../server/server-usage/views/drop-view.md)
  * [CREATE SEQUENCE](../../../server/reference/sql-structure/sequences/create-sequence.md)
  * [ALTER SEQUENCE](../../../server/reference/sql-structure/sequences/alter-sequence.md)
  * [DROP SEQUENCE](../../../server/reference/sql-structure/sequences/drop-sequence.md)
  * [CREATE TRIGGER](../../../server/server-usage/triggers-events/triggers/create-trigger.md)
  * [DROP TRIGGER](../../../server/reference/sql-statements/data-definition/drop/drop-trigger.md)
  * [CREATE PROCEDURE](../../../server/server-usage/stored-routines/stored-procedures/create-procedure.md)
  * [ALTER PROCEDURE](../../../server/server-usage/stored-routines/stored-procedures/alter-procedure.md)
  * [DROP PROCEDURE](../../../server/server-usage/stored-routines/stored-procedures/drop-procedure.md)
  * [CREATE FUNCTION](../../../server/reference/sql-statements/data-definition/create/create-function.md)
  * [ALTER FUNCTION](../../../server/reference/sql-statements/data-definition/alter/alter-function.md)
  * [DROP FUNCTION](../../../server/server-usage/stored-routines/stored-functions/drop-function.md)
  * [CREATE USER](../../../server/reference/sql-statements/account-management-sql-statements/create-user.md)
  * [ALTER USER](../../../server/reference/sql-statements/account-management-sql-statements/alter-user.md)
  * [DROP USER](../../../server/reference/sql-statements/account-management-sql-statements/drop-user.md)
  * [CREATE ROLE](../../../server/reference/sql-statements/account-management-sql-statements/create-role.md)
  * [DROP ROLE](../../../server/reference/sql-statements/account-management-sql-statements/drop-role.md)
* Queries within open transactions If the application uses explicit transactions, then all queries within the transaction will be routed to the primary server. Explicit transactions are used in the following cases:
  * When [autocommit](../../../server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) is set to OFF.
  * When [BEGIN](../../../server/reference/sql-statements/transactions/start-transaction.md) is executed.
  * When [START TRANSACTION](../../../server/reference/sql-statements/transactions/start-transaction.md) is executed.

For example, all queries will be routed to the primary server in this case:

```
SET SESSION autocommit=OFF;
SELECT * FROM hq_sales.invoices WHERE branch_id=1;
INSERT INTO hq_sales.invoices
   (customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, '2020-05-10 12:35:10', 1087.23, 'CREDIT_CARD');
COMMIT;
```

And all queries will also be routed to the primary server in this case:

```
BEGIN;
SELECT * FROM hq_sales.invoices WHERE branch_id=1;
INSERT INTO hq_sales.invoices
   (customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, '2020-05-10 12:35:10', 1087.23, 'CREDIT_CARD');
COMMIT;
```

* Queries using stored procedures
* Queries using stored functions
* Queries using user-defined functions (UDF)
* Queries that use temporary tables
* [EXECUTE](../../../server/reference/sql-statements/prepared-statements/execute-statement.md) statements that execute prepared statements

## Statements Routed to a Replica Server

The following statements are routed to a replica server:

* Queries that are read-only For example, this includes, but is not limited to, the following statements:
  * [SELECT](../../../server/reference/sql-statements/data-manipulation/selecting-data/select.md)
* Queries that read system or user-defined variables For example, this includes, but is not limited to, the following statements:
  * [SHOW CHARACTER SET](../../../server/reference/sql-statements/administrative-sql-statements/show/show-character-set.md)
  * [SHOW COLLATION](../../../server/reference/sql-statements/administrative-sql-statements/show/show-collation.md)
  * [SHOW COLUMNS](../../../server/reference/sql-statements/administrative-sql-statements/show/show-columns.md)
  * [SHOW CREATE DATABASE](../../../server/reference/sql-statements/administrative-sql-statements/show/show-create-database.md)
  * [SHOW CREATE FUNCTION](../../../server/reference/sql-statements/administrative-sql-statements/show/show-create-function.md)
  * [SHOW CREATE PROCEDURE](../../../server/reference/sql-statements/administrative-sql-statements/show/show-create-procedure.md)
  * [SHOW CREATE SEQUENCE](../../../server/reference/sql-statements/administrative-sql-statements/show/show-create-sequence.md)
  * [SHOW CREATE TABLE](../../../server/reference/sql-statements/administrative-sql-statements/show/show-create-table.md)
  * [SHOW CREATE TRIGGER](../../../server/reference/sql-statements/administrative-sql-statements/show/show-create-trigger.md)
  * [SHOW CREATE USER](../../../server/reference/sql-statements/administrative-sql-statements/show/show-create-user.md)
  * [SHOW CREATE VIEW](../../../server/reference/sql-statements/administrative-sql-statements/show/show-create-view.md)
  * [SHOW DATABASES](../../../server/reference/sql-statements/administrative-sql-statements/show/show-databases.md)
  * [SHOW ENGINES](../../../server/reference/sql-statements/administrative-sql-statements/show/show-engine.md)
  * [SHOW TABLES](../../../server/reference/sql-statements/administrative-sql-statements/show/show-tables.md)
  * [SHOW VARIABLES](../../../server/reference/sql-statements/administrative-sql-statements/show/show-variables.md)

For example, the following queries would be routed to a replica:

```
SELECT @@global.alter_algorithm;
SELECT @@my_user_var;
SHOW statements
```

* Queries using built-in functions

## Statements Routed to All Servers

The following statements are routed to all servers:

* [SET](../../../server/reference/sql-statements/administrative-sql-statements/set-commands/set.md) statements, including those embedded in read-only statements
* [USE](../../../server/reference/sql-statements/administrative-sql-statements/use-database.md) statements
* [PREPARE](../../../server/reference/sql-statements/prepared-statements/prepare-statement.md) statements that create prepared statements
* Internal client commands, such as `QUIT, PING, STMT RESET, and CHANGE USER`.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
