# FOREIGN KEY Constraints

_In MariaDB Server, `FOREIGN KEY` constraints are key elements in defining relationships between InnoDB tables: they ensure referential integrity by maintaining valid associations between rows in parent and child tables. Changes in the parent table can either be restricted or propagated to maintain consistency with child tables._

## Overview

MariaDB Server supports `FOREIGN KEY` constraints to define referential constraints between InnoDB tables:

* Referential constraints allow the database to automatically ensure that each row in the child table is associated with a valid row in the parent table
* If the row in the parent table changes, MariaDB Server can block the change to protect child rows, or propagate the change to the child rows

## Term Definitions

| Term         | Definition                                   |
| ------------ | -------------------------------------------- |
| parent table | A table that has a foreign key.              |
| child table  | A table that is referenced by a foreign key. |

## Uses Cases for Foreign Keys

Foreign keys allow the database to handle certain types of referential constraint checks, so that the application does not have to handle them. As a consequence, application logic can be simplified.

Some example use cases are described below.

### Managing Accounts Use Case

Many different applications have account management features. Foreign keys can be used to simplify certain aspects of managing accounts, such as:

* If an account is deleted, foreign keys can be used to automatically delete data associated with the account.
* If an account is deleted, foreign keys can be used to automatically disassociate its data, so that it is no longer associated with any account.
* If an account's user name or user ID is updated, foreign keys can be used to automatically associate its data with the new user name or user ID.

### Managing Store Inventory Use Case

Foreign keys can also be used to simplify certain aspects of managing a store inventory, such as:

* If a product is deleted, foreign keys can be used to automatically delete data associated with the product, such as reviews and images.
* If a product's name is changed, foreign keys can be used to automatically associate the new name with the product's other data.
* If a customer purchases a product, foreign keys can be used to associate the order with the product.
* If a customer reviews a product, foreign keys can be used to associate the review with the product.

## Operating on InnoDB Tables with Foreign Keys

When an InnoDB table has a foreign key or when it is referenced by a foreign key, InnoDB performs a referential constraint check when certain types of operations try to write to the table. The specific details depend on whether the table is a parent table or a child table.

### Operating on a Parent Table

When an InnoDB table has a foreign key, it is known as a parent table. InnoDB performs referential constraint checks for the following operations on parent tables:

* [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md)
* [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md)

When InnoDB performs a referential constraint check, the outcome depends on several factors. The following table describes the details:

| Operation                                                                                   | Result of Constraint Check                                     | Action              | Consequence                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) | InnoDB finds corresponding rows in the child table             | ON UPDATE RESTRICT  | • Fails with [ER\_ROW\_IS\_REFERENCED\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1451.md) error code                                                                                                          |
| [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) | InnoDB finds corresponding rows in the child table             | ON UPDATE NO ACTION | •. Fails with [ER\_ROW\_IS\_REFERENCED\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1451.md) error code                                                                                                         |
| [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) | InnoDB finds corresponding rows in the child table             | ON UPDATE CASCADE   | • Success. • Row in the parent table is updated. • Corresponding rows in the child table are also updated with the new foreign key value. If the child table has an update trigger, the trigger will not be executed for the update. |
| [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) | InnoDB finds corresponding rows in the child table             | ON UPDATE SET NULL  | • Success. • Row in the parent table is updated. • Corresponding rows in the child table are also updated with NULL. If the child table has an update trigger, the trigger will not be executed for the update.                      |
| [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) | InnoDB does not find any corresponding rows in the child table | NA                  | • Success. • Row in the parent table is updated                                                                                                                                                                                      |
| [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) | InnoDB finds corresponding rows in the child table             | ON DELETE RESTRICT  | • Fails with [ER\_ROW\_IS\_REFERENCED\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1451.md) error code                                                                                                          |
| [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) | InnoDB finds corresponding rows in the child table             | ON DELETE NO ACTION | • Fails with [E](broken-reference/)[ER\_ROW\_IS\_REFERENCED\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1451.md) error code                                                                                    |
| [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) | InnoDB finds corresponding rows in the child table             | ON DELETE CASCADE   | • Success. • Row in the parent table is deleted. • Corresponding rows in the child table are also deleted. If the child table has a delete trigger, the trigger will not be executed for the delete.                                 |
| [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) | InnoDB finds rows in the child table for the row               | ON DELETE SET NULL  | • Success. • Row in the parent table is deleted. • Corresponding rows in the child table are updated with NULL. If the child table has an update trigger, the trigger will not be executed for the update.                           |
| [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) | InnoDB does not find any rows in the child table for the row   | NA                  | • Success. • Row in the parent table is deleted                                                                                                                                                                                      |

### Operating on a Child Table

When an InnoDB table is referenced by a foreign key, it is known as a child table. InnoDB performs referential constraint checks for the following operations on child tables:

* [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md)
* [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md)
* [DROP TABLE](../../reference/sql-statements/data-definition/drop/drop-table.md)

When InnoDB performs a referential constraint check, the outcome depends on several factors. The following table describes the details:

| Operation                                                                                   | Result of Constraint Check                           | Consequence                                                                                                               |
| ------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) | New foreign key value is present in parent table     | Success                                                                                                                   |
| [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) | New foreign key value is not present in parent table | Fails with [ER\_NO\_REFERENCED\_ROW\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1452.md) error code |
| [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) | New foreign key value is NULL                        | Success                                                                                                                   |
| [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) | New foreign key value is present in parent table     | Success                                                                                                                   |
| [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) | New foreign key value is not present in parent table | Fails with [ER\_NO\_REFERENCED\_ROW\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1452.md) error code |
| [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) | New foreign key value is NULL                        | Success                                                                                                                   |
| [DROP TABLE](../../reference/sql-statements/data-definition/drop/drop-table.md)             | Table is referenced by a foreign key                 | Fails with [ER\_NO\_REFERENCED\_ROW\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1452.md) error code |

## Creating InnoDB Tables with a Foreign Key Constraint

Let's create InnoDB tables with a foreign key constraint after confirming that the [default storage engine](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) is InnoDB:

1. Connect to the server using MariaDB Client:

```
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';

+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the sequence and table using the [CREATE DATABASE](../../reference/sql-statements/data-definition/create/create-database.md) statement:

```sql
CREATE DATABASE hq_sales;
```

4. Create the parent table using the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement:

```sql
CREATE TABLE hq_sales.customers (
   customer_id BIGINT AUTO_INCREMENT NOT NULL,
   customer_name VARCHAR(500) NOT NULL,
   customer_email VARCHAR(200),
   PRIMARY KEY(customer_id)
);
```

5. Create the child table using the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT AUTO_INCREMENT NOT NULL,
   branch_id INT NOT NULL,
   customer_id BIGINT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id),
   CONSTRAINT fk_invoices_customers
      FOREIGN KEY (customer_id) REFERENCES hq_sales.customers (customer_id)
      ON DELETE RESTRICT
      ON UPDATE RESTRICT
);
```

6. Insert some rows into the parent table using the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```sql
INSERT INTO hq_sales.customers (customer_id, name)
   VALUES
   (1, 'John Doe'),
   (2, 'Jane Doe');
```

7. Insert a row into the child table for each row in the parent table using the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```sql
INSERT INTO hq_sales.invoices
   (branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, 1, '2020-05-10 12:35:10', 1087.23, 'CREDIT_CARD'),
   (1, 2, '2020-05-10 14:17:32', 1508.57, 'WIRE_TRANSFER');
```

8. Attempt to delete a row from the parent table that has a corresponding row in the child table using the `DELETE` statement:

```sql
DELETE FROM hq_sales.customers
   WHERE customer_id = 1;
```

This will fail with the [ER\_ROW\_IS\_REFERENCED\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1451.md) error code as explained in the Operating on a Parent Table section:

```sql
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails
   (`hq_sales`.`invoices`, CONSTRAINT `fk_invoices_customers`
   FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`))
```

Attempt to insert a row into the child table for a non-existent row in the parent table using the INSERT statement:

```sql
INSERT INTO hq_sales.invoices
   (branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, 3, '2020-05-10 14:25:16', 227.15, 'CASH');
```

This will fail with the [ER\_NO\_REFERENCED\_ROW\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1452.md) error code as explained in the Operating on a Child Table section:

```sql
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails
   (`hq_sales`.`invoices`, CONSTRAINT `fk_invoices_customers`
   FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`))
```

## Adding a Foreign Key Constraint to an InnoDB Table

Let's create InnoDB tables after confirming that the [default storage engine](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) is InnoDB, and then let's add a foreign key constraint between them:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';

+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the sequence and table using the [CREATE DATABASE](../../reference/sql-statements/data-definition/create/create-database.md) statement:

```sql
CREATE DATABASE hq_sales;
```

4. Create the parent table using the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement:

```sql
CREATE TABLE hq_sales.customers (
   customer_id BIGINT AUTO_INCREMENT NOT NULL,
   customer_name VARCHAR(500) NOT NULL,
   customer_email VARCHAR(200),
   PRIMARY KEY(customer_id)
);
```

5. Create the child table using the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT AUTO_INCREMENT NOT NULL,
   branch_id INT NOT NULL,
   customer_id BIGINT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id)
);
```

6. Alter the child table to add the foreign key constraint using the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement:

```sql
ALTER TABLE hq_sales.invoices ADD CONSTRAINT fk_invoices_customers
      FOREIGN KEY (customer_id) REFERENCES hq_sales.customers (customer_id)
      ON DELETE RESTRICT
      ON UPDATE RESTRICT;
```

7. Insert some rows into the parent table using the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```sql
INSERT INTO hq_sales.customers (customer_id, name)
   VALUES
   (1, 'John Doe'),
   (2, 'Jane Doe');
```

8. Insert a row into the child table for each row in the parent table using the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```sql
INSERT INTO hq_sales.invoices
   (branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, 1, '2020-05-10 12:35:10', 1087.23, 'CREDIT_CARD'),
   (1, 2, '2020-05-10 14:17:32', 1508.57, 'WIRE_TRANSFER');
```

9. Attempt to delete a row from the parent table that has a corresponding row in the child table using the [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) statement:

```sql
DELETE FROM hq_sales.customers
   WHERE customer_id = 1;
```

This will fail with the [ER\_ROW\_IS\_REFERENCED\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1451.md) error code as explained in the Operating on a Parent Table section:

```sql
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails
   (`hq_sales`.`invoices`, CONSTRAINT `fk_invoices_customers`
   FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`))
```

10. Attempt to insert a row into the child table for a non-existent row in the parent table using the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```sql
INSERT INTO hq_sales.invoices
   (branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, 3, '2020-05-10 14:25:16', 227.15, 'CASH');
```

This will fail with the [ER\_NO\_REFERENCED\_ROW\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1452.md) error code as explained in the Operating on a Child Table section:

```sql
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails
   (`hq_sales`.`invoices`, CONSTRAINT `fk_invoices_customers`
   FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`))
```

## Dropping a Foreign Key Constraint from an InnoDB Table

Let's drop the foreign key constraint from the child table created in the [Creating InnoDB Tables with a Foreign Key Constraint](foreign-key-constraints.md#creating-innodb-tables-with-a-foreign-key-constraint) section:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Obtain the name of the foreign key constraint by querying the [information\_schema.TABLE\_CONSTRAINTS](../../reference/system-tables/information-schema/information-schema-tables/information-schema-table_constraints-table.md) table:

```sql
SELECT CONSTRAINT_NAME
FROM information_schema.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = 'hq_sales'
AND TABLE_NAME = 'invoices'
AND CONSTRAINT_TYPE = 'FOREIGN KEY';
```

```
+-----------------------+
| CONSTRAINT_NAME       |
+-----------------------+
| fk_invoices_customers |
+-----------------------+
```

3. Drop the foreign key constraint from the child table using the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement:

```sql
ALTER TABLE hq_sales.invoices DROP FOREIGN KEY fk_invoices_customers;
```

## Temporarily Disabling Foreign Key Constraint Checks

When performing bulk data loads, dropping a table, or rebuilding a table, it can improve performance to temporarily disable foreign key constraint checks. Foreign key constraint checks can be temporarily disabled by setting the session value for the `foreign_key_checks` system variable. If foreign key constraint checks are temporarily disabled, then rows can be inserted that violate the constraint, so users must proceed with caution. This feature is most useful when you are loading a data set that is known to be valid.

Let's temporarily disable foreign key constraint checks, and then perform some tasks with the tables created in the [Creating InnoDB Tables with a Foreign Key Constraint](foreign-key-constraints.md#creating-innodb-tables-with-a-foreign-key-constraint) section:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Temporarily disable foreign key constraint checks by setting the [foreign\_key\_checks](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#foreign_key_checks) system variable with the [SET SESSION](../../set-session-authorization.md) statement:

```sql
SET SESSION foreign_key_checks=OFF;
```

3. If you want to test how to introduce inconsistencies, then attempt to delete a row from the parent table that has a corresponding row in the child table using the [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) statement:

```sql
DELETE FROM hq_sales.customers
   WHERE customer_id = 1;
```

This operation would usually fail with the [ER\_NO\_REFERENCED\_ROW](../../reference/error-codes/mariadb-error-codes-1200-to-1299/e1216.md) error code as explained in the Operating on a Parent Table section, but if foreign key constraint checks are disable, then it will succeed.

4. If you want to test how to introduce inconsistencies, then also attempt to insert a row into the child table for a non-existent row in the parent table using the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```sql
INSERT INTO hq_sales.invoices
   (branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, 3, '2020-05-10 14:25:16', 227.15, 'CASH');
```

This operation would usually fail with the [ER\_NO\_REFERENCED\_ROW\_2](../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1452.md) error code as explained in the [Operating on a Child Table](foreign-key-constraints.md#operating-on-a-child-table) section, but if foreign key constraint checks are disable, then it will succeed.

5. Re-enable foreign key constraint checks by setting the [foreign\_key\_checks](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#foreign_key_checks) system variable with the [SET SESSION](../../set-session-authorization.md) statement:

```sql
SET SESSION foreign_key_checks=ON;
```

## Special Cases

### Foreign Key Constraint Namespace

When a foreign key constraint is created without a name, InnoDB implicitly gives it a name in the format:

```
<table_name>_ibfk_<constraint_count>
```

If foreign key constraints are explicitly created with names in the same format, it is possible for collisions to occur during table renames. In that case, the [MariaDB Error Log](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) would contain messages like the following:

```
2021-06-16 11:50:39 139702710404864 [ERROR] InnoDB: Possible reasons:
2021-06-16 11:50:39 139702710404864 [ERROR] InnoDB: (1) Table rename would cause two FOREIGN KEY constraints to have the same internal name in case-insensitive comparison.
2021-06-16 11:50:39 139702710404864 [ERROR] InnoDB: (2) Table `test`.`t3` exists in the InnoDB internal data dictionary though MySQL is trying to rename table `test`.`t2b` to it. Have you deleted the .frm file and not used DROP TABLE?
2021-06-16 11:50:39 139702710404864 [ERROR] InnoDB: If table `test`.`t3` is a temporary table #sql..., then it can be that there are still queries running on the table, and it will be dropped automatically when the queries end. You can drop the orphaned table inside InnoDB by creating an InnoDB table with the same name in another database and copying the .frm file to the current database. Then MySQL thinks the table exists, and DROP TABLE will succeed.
```

## Dependence on an Index

A foreign key constraint requires an index on the column. If a foreign key constraint is added to a column without an index, InnoDB will automatically create an index to enforce the foreign key constraint.

When the [foreign\_key\_checks](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#foreign_key_checks) system variable is disabled, it is possible to drop the index used by a foreign key constraint. When the [foreign\_key\_checks](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#foreign_key_checks) system variable is re-enabled, InnoDB will have no way to enforce the foreign key constraint, so all operations that could potentially violate the foreign key constraint will fail.

{% include "../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
