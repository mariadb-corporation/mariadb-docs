---
description: >-
  An overview of supported online schema change operations in InnoDB, detailing
  which DDL statements can be performed without locking the table.
---

# Schema Changes

## Overview

In MariaDB Enterprise Server, InnoDB supports many different schema change operations. Many of the operations can be performed online with concurrent DML using little or no locking.

## DDL Statements

InnoDB schema changes are performed using the following DDL statements:

* [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/)
* [CREATE INDEX](../../../../../reference/sql-statements/data-definition/create/create-index.md)
* [CREATE SPATIAL INDEX](../../../../../reference/sql-statements/data-definition/create/create-index.md)
* [CREATE UNIQUE INDEX](../../../../../reference/sql-statements/data-definition/create/create-index.md)
* [DROP INDEX](../../../../../reference/sql-statements/data-definition/drop/drop-index.md)
* [RENAME TABLE](../../../../../reference/sql-statements/data-definition/rename-table.md)

## About InnoDB Schema Changes and Online DDL

InnoDB schema changes and online DDL are performed with a wide range of statements:

Each operation supports a subset of the following algorithms: `INSTANT, NOCOPY, INPLACE, or COPY`.

By default, InnoDB will use the most efficient algorithm supported by an operation. This behavior can be changed by using the `ALGORITHM` clause with the [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement or by changing the value of the alter\_algorithm system variable.

Each operation supports a subset of the following locking strategies: `NONE, SHARED, or EXCLUSIVE`.

By default, InnoDB will use the most permissive locking strategy supported by an operation. This behavior can be changed by using the LOCK clause with the [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement.

| Feature                                              | Detail | Resources                                                                                   |
| ---------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------- |
| Operations support instant algorithm                 | Yes    | [InnoDB Schema Changes with the INSTANT Algorithm](schema-changes-innodb-schema-changes.md) |
| Operations support no-copy algorithm                 | Yes    | [InnoDB Schema Changes with the NOCOPY Algorithm](schema-changes-innodb-schema-changes.md)  |
| Operations support in-place algorithm                | Yes    | InnoDB Schema Changes with the INPLACE Algorithm                                            |
| Adding a column                                      | Yes    |                                                                                             |
| Dropping a column                                    | Yes    |                                                                                             |
| Reordering columns                                   | Yes    |                                                                                             |
| Changing a column to NULL                            | Yes    |                                                                                             |
| Changing a column to NOT NULL                        | Yes    |                                                                                             |
| Adding a new ENUM option                             | Yes    |                                                                                             |
| Adding a new SET option                              | Yes    |                                                                                             |
| Adding system versioning                             | Yes    |                                                                                             |
| Removing system versioning                           | Yes    |                                                                                             |
| Setting a column's DEFAULT                           | Yes    |                                                                                             |
| Removing a column's DEFAULT                          | Yes    |                                                                                             |
| Adding a primary key                                 | Yes    |                                                                                             |
| Dropping a primary key                               | Yes    |                                                                                             |
| Adding an index                                      | Yes    |                                                                                             |
| Dropping an index                                    | Yes    |                                                                                             |
| Adding a foreign key                                 | Yes    |                                                                                             |
| Dropping a foreign key                               | Yes    |                                                                                             |
| Setting the next AUTO\_INCREMENT value               | Yes    |                                                                                             |
| Setting the row format                               | Yes    |                                                                                             |
| Setting the block size for the Compressed row format | Yes    |                                                                                             |
| Enabling page compression                            | Yes    |                                                                                             |
| Setting the page compression level                   | Yes    |                                                                                             |
| Disabling page compression                           | Yes    |                                                                                             |
| Enabling data-at-rest encryption                     | Yes    |                                                                                             |
| Setting the encryption key ID                        | Yes    |                                                                                             |
| Disabling data-at-rest encryption                    | Yes    |                                                                                             |
| Adding a constraint                                  | Yes    |                                                                                             |
| Dropping a constraint                                | Yes    |                                                                                             |
| Rebuilding the table                                 | Yes    |                                                                                             |
| Renaming the table                                   | Yes    |                                                                                             |
