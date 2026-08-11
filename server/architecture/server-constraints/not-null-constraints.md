# NOT NULL Constraints

_When creating a table, you can define a column with a `NOT NULL` constraint to prevent null values. This constraint ensures data integrity by guaranteeing that a column must always contain a value. If an attempt is made to insert or update a row with a null value in a `NOT NULL` column, the operation will be rejected, thus maintaining the integrity of the database._

## Overview

MariaDB Server supports `NOT NULL` constraints to ensure that a column's value is not set to `NULL`:

When a column is declared with a `NOT NULL` constraint, Enterprise Server rejects operations that would write a NULL value to the column

## CREATE TABLE

### CREATE TABLE and NOT NULL Constraints

With MariaDB Server, the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement can be used to create a new table with a `NOT NULL` constraint on one or more columns:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY (invoice_id)
);
```

## ALTER TABLE

### ALTER TABLE .. MODIFY COLUMN .. NOT NULL

With MariaDB Server, the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement can be used to add the `NOT NULL` constraint to a column using the `MODIFY COLUMN` clause:

```sql
ALTER TABLE hq_sales.invoices
   MODIFY COLUMN customer_id INT NOT NULL;
ALTER TABLE .. MODIFY COLUMN .. NULL
```

With MariaDB Server, the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement can be used to remove the `NOT NULL` constraint from a column using the `MODIFY COLUMN` clause:

```sql
ALTER TABLE hq_sales.invoices
   MODIFY COLUMN customer_id INT NULL;
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
