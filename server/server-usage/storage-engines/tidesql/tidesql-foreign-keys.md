---
description: >-
  How TideSQL enforces referential integrity inside the engine, the referential
  actions it supports, and the two constraint shapes it rejects.
---

# TideSQL Foreign Keys

TideSQL enforces foreign keys inside the engine rather than leaving them to the application. A `FOREIGN KEY` clause is checked on every INSERT, UPDATE, and DELETE, and the constraint is persisted so it survives a restart and shows up in `SHOW CREATE TABLE` and the information schema the same way InnoDB's does. The handler advertises the capability to the server, so the optimizer and the replication layer treat these tables as referentially constrained.

## Defining a Foreign Key

A foreign key is declared the standard way, and the referenced column must be a primary key or a unique key on the parent table:

```sql
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(100)
) ENGINE=TIDESDB;

CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT,
  total DECIMAL(10,2),
  FOREIGN KEY (customer_id) REFERENCES customers(id)
) ENGINE=TIDESDB;
```

An INSERT or UPDATE on `orders` whose `customer_id` has no matching `customers.id` is rejected with `ER_NO_REFERENCED_ROW_2` (ERROR 1452). A DELETE or key-changing UPDATE on `customers` whose row is still referenced by an order is rejected with `ER_ROW_IS_REFERENCED_2` (ERROR 1451), unless a referential action says otherwise.

Composite foreign keys over several columns are supported, and a table may reference itself.

## Referential Actions

`ON DELETE` and `ON UPDATE` accept `RESTRICT`, `CASCADE`, and `SET NULL`. `RESTRICT` is the default and is also what `NO ACTION` resolves to, matching InnoDB. `CASCADE` propagates the parent's delete or key change down to the children, recursing through further foreign keys. `SET NULL` clears the referencing columns, which requires them to be nullable.

```sql
CREATE TABLE order_items (
  id INT PRIMARY KEY,
  order_id INT,
  sku VARCHAR(40),
  FOREIGN KEY (order_id) REFERENCES orders(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=TIDESDB;
```

Deleting an order now removes its items in the same transaction, and the cascade continues into any table that references `order_items`.

## Referencing a Unique Key

A foreign key may reference a non-nullable unique key, not only the primary key:

```sql
CREATE TABLE products (
  id INT PRIMARY KEY,
  sku VARCHAR(40) NOT NULL UNIQUE
) ENGINE=TIDESDB;

CREATE TABLE stock (
  id INT PRIMARY KEY,
  product_sku VARCHAR(40),
  FOREIGN KEY (product_sku) REFERENCES products(sku)
) ENGINE=TIDESDB;
```

## NULL Referencing Columns

The engine uses `MATCH SIMPLE` semantics. If any column of a composite referencing key is NULL, the row is accepted without a parent lookup, the same rule InnoDB applies. A single nullable referencing column that is NULL therefore never fails the check.

## Restrictions

Two constraint shapes are rejected at `CREATE TABLE` and `ALTER TABLE`:

* A foreign key column declared with descending order, because the engine matches child rows against a forward sort key that a descending column would not line up with.
* A foreign key that references a nullable unique key, because the value-only child probe cannot reproduce the null indicator that key stores.

Both are reported as an unsupported constraint at create time rather than being silently dropped.

## Disabling the Checks

`foreign_key_checks` is honored. Setting it to zero skips both the child-side existence probe and the parent-side reference check, which is what makes a bulk load or an engine conversion possible without ordering the data:

```sql
SET FOREIGN_KEY_CHECKS = 0;
-- load parent and child data in any order
SET FOREIGN_KEY_CHECKS = 1;
```

{% hint style="warning" %}
Re-enabling the checks does not retroactively validate rows written while they were off, so use this only when the data is known to be consistent.
{% endhint %}

## Inspecting Constraints

Foreign keys render in `SHOW CREATE TABLE`, and both directions are reported to the information schema, so `information_schema.KEY_COLUMN_USAGE` and `information_schema.REFERENTIAL_CONSTRAINTS` list them the same way they do for InnoDB tables.

<sub>_This page is licensed: GPLv2_</sub>
