---
description: >-
  How TideSQL enforces referential integrity inside the engine, the referential
  actions it supports, and the constraint shapes it rejects.
---

# TideSQL Foreign Keys

TideSQL enforces foreign keys inside the engine rather than leaving them to the application. A `FOREIGN KEY` clause is checked on every INSERT, UPDATE, and DELETE, and the constraint is persisted so it survives a restart and shows up in `SHOW CREATE TABLE` and the information schema the same way InnoDB's does. The handler advertises the capability to the server and reports each constraint from both the child and the parent side, which is what lets the server open the child tables a cascade needs.

## Defining a Foreign Key

A foreign key is declared the standard way, and the referenced columns must be the primary key or a `NOT NULL` unique key of the parent table:

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

Composite foreign keys over several columns are supported.

A parent table that is already open when a child constraint is created or dropped picks up the change at its next statement, so the new constraint is enforced at once and a dropped one stops being enforced without reopening the parent.

## Referential Actions

`ON DELETE` and `ON UPDATE` accept `RESTRICT`, `CASCADE`, and `SET NULL`. `RESTRICT` is the default and is also what `NO ACTION` resolves to, matching InnoDB. `CASCADE` propagates the parent's delete or key change down to the children, recursing through further foreign keys. `SET NULL` clears the referencing columns, which requires them to be nullable. `SET DEFAULT` has no action of its own and is checked the same way as `RESTRICT`. A cascade deeper than 15 levels fails with `ER_FK_DEPTH_EXCEEDED` and changes nothing, as in InnoDB.

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

## Self-Referencing Keys

A table may reference itself, as a tree of rows does through a parent id. `ON DELETE CASCADE`, `ON DELETE SET NULL`, `RESTRICT`, and `ON UPDATE CASCADE` all work on such a key:

```sql
CREATE TABLE categories (
  id INT PRIMARY KEY,
  parent_id INT,
  KEY (parent_id),
  FOREIGN KEY (parent_id) REFERENCES categories(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=TIDESDB;
```

`ON UPDATE CASCADE` differs from InnoDB here. InnoDB refuses an update cascade into the same table and treats it as `RESTRICT`, while TideSQL applies it, so the children follow the parent's new key.

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

## Concurrent Writers

A child row and its parent row are different rows, so under snapshot isolation a transaction deleting a parent and one inserting a child of it write no common key, and each one's check reads a snapshot that cannot see the other's uncommitted write. InnoDB closes this with a shared lock the child check takes on the parent row. The engine is lock-free, so it records the same relationship in memory. A child write holds the referenced parent value shared, and a parent delete, or a change to a referenced key, holds it exclusive. Two child writes of the same parent coexist, and of any other pair the second is refused with a deadlock (ERROR 1213) for the application to retry. A parent removed, or a child added, after the transaction's snapshot is refused the same way, and the retry with a fresh snapshot then sees it and gets the ordinary foreign key error. A hold lasts until its transaction ends, and a rollback to a savepoint releases the holds taken after it. Under Galera a child write also certifies a reference to its parent row, so the same race between nodes is caught in certification, as described in [TideSQL Replication and High Availability](tidesql-replication-and-ha.md).

## Restrictions

These constraint shapes are rejected at `CREATE TABLE` and `ALTER TABLE`:

* A foreign key column declared with descending order, because the engine matches child rows against a forward sort key that a descending column would not line up with.
* A foreign key that references a nullable unique key, because the value-only child probe cannot reproduce the null indicator that key stores.
* A foreign key that references parent columns covered only by a plain index, or by no index. InnoDB accepts a plain index there, and TideSQL requires the primary key or a `NOT NULL` unique key.
* A foreign key that references only the leading columns of a composite primary or unique key. The referenced columns must be every column of that key, in the key's column order.
* `SET NULL` on a child column declared `NOT NULL`.
* A reference to a parent table that does not exist, unless `foreign_key_checks` is 0, as in InnoDB.
* A foreign key whose columns are not the leading columns of an index on the child table. MariaDB normally creates that index automatically, so this is rarely hit.

All of these fail the `CREATE TABLE` or `ALTER TABLE` statement with `ER_CANT_CREATE_TABLE` (ERROR 1005) and a message naming the constraint, rather than being silently dropped.

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
