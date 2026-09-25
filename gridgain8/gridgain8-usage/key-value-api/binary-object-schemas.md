---
description: >-
  Understand how GridGain generates binary object schemas and how to modify them safely when changing SQL tables or Java classes.
---

# Binary Object Schemas

## Overview

Data in GridGain is stored as key-value pairs, with both the key and value represented as binary objects. This data structure is similar to a map or a JSON document and allows for efficient storage and retrieval of data

Every time you add or removes columns in SQL tables, a new schema is generated. Objects in the cache are stored in binary object format, and every entry is matched to a schema. Schemas belongs to the cluster, not to a particular table.

Some old entries may not have a schema (for example, if it was deleted), in which case all new fields will return a NULL value. After any modification to these entries (for example, updating the fields or reinserting), the old entry will be moved to the new schema.

GridGain uses two schemas for data storage: binary object schema that is based on java class fields and [SQL table schema](../sql/schemas.md) that is based on the table columns. The SQL schema maps to the Binary Object schema by creating field mappings. For example, SQL field A is mapped to a Binary Object field A. While the names of SQL and Binary Object fields are usually the same, they do not have to be.

It is possible to have some Binary Object columns that are not mapped to any SQL columns. In this case, the Binary Object column will not be accessible via SQL.

## Modifying Binary Object Schemas

Cache configurations generally cannot be changed after the caches are created, including table definitions. Changing XML configuration or Java classes that were used to create the cache will have no effect. The only changes allowed at runtime are the changes introduced by using SQL DDL, for example by using `ALTER TABLE` statements.

You can also deploy a new version of the Java classes. Adding new fields will not cause issues, but some changes are not be supported, such as changing field types or deleting key fields.Unsupported cases include:

- Changing an existing field type;
- Removing fields from a Java class, especially if those fields are part of a PK, affinity fields or indexes, or do not align to the SQL schema.

If you need to perform the above actions, the cache must be recreated. If you change the class field type, the class metadata must also be cleared.

In this case you should follow the steps below (should be done before deploying new version of the class):

- Export cache values to a different table or cache to make sure the values are safe. You can skip the field you are going to change:

  ```sql
  INSERT INTO NEW_TABLE (A,B,C) SELECT A,B,C FROM OLD_TABLE
  ```

  {% hint style="info" %}
  Do not use `KEY_TYPE` and `VALUE_TYPE` for `NEW_TABLE` (these values can be binary objects).
  {% endhint %}
- Safely destroy the cache.
- Make sure Data Center replication is stopped for the cache on the sender and receiver sides. Otherwise, your replication will have issues because you will only have a cache on one side. See [Managing and Monitoring Replication](../../gridgain8-management/data-center-replication/managing-and-monitoring.md#pausing-and-resuming-replication) for instructions on managing replication.
- Use the following command to check the current state of the partitions for the cache:

  {% hint style="info" %}
  If any data node is down, and you see that some partition is lost, you need to start those nodes and reset the state of the partition.
  {% endhint %}

  ```bash
  control.sh --cache distribution null "Test"
  ```

  {% hint style="info" %}
  Make sure to perform this and subsequent operations on a stable cluster that is not performing rebalancing.
  {% endhint %}
- Destroy the cache by using any API.
- Check metadata for cache Key/Value types and remove it. Make sure that this class was only used by the removed cache.

  Check that the required type exists. For example, for the class `models.TestValue`, you can see that after cache removal, metadata for these values remains:

  ```bash
  control.sh --meta details --typeName models.TestValue
  ```
- Restart the JVM and deploy a new version of the class that has a field with a different type.
- Recreate the cache and use the backup cache for restoring the old data.

## Examples

### Adding a column

Column is added to the schema automatically.

```sql
ALTER TABLE T ADD COLUMN FOO INT
```

### Dropping a column from SQL only

Column is removed from the SQL table, but column data is kept in key-value schema.

```sql
ALTER TABLE T DROP COLUMN FOO
```

### Dropping a column from SQL and deleting data

First you scan the table and remove the data, then you change the schema. This way no data is left in key-value schema.

```sql
>UPDATE T SET FOO=NULL
>ALTER TABLE T DROP COLUMN FOO
```

### Adding index

Adding index automatically updates both schemas.

```sql
CREATE INDEX IDX
```

### Dropping index

Once index is dropped it is automatically cleaned up in background.

```sql
DROP INDEX IDX
```

### Renaming a column

To rename the column:

- Add a new column;
- Copy the data from the old column to the new column;
- Drop the old column.

The old column’s data is simultaneously removed, and the old column is then dropped.

```sql
ALTER TABLE T ADD COLUMN NEW_COL INT
UPDATE T SET NEW_COL=OLD_COL, OLD_COL=NULL
ALTER TABLE T DROP COLUMN OLD_COL
```

### Increasing column size

Column size change is not supported directly, but can be achieved with two statements. Since both `DROP` and `ADD` are metadata-only changes, both statements execute instantly.

```sql
ALTER TABLE T DROP COLUMN FOO
ALTER TABLE T ADD COLUMN FOO VARCHAR(20)
```

### Decreasing column size

Column size change isn’t supported directly, but can be achieved with three statements.

Since the size is being decreased, the data needs to also be altered beforehand with an additional step.

```sql
UPDATE T SET FOO=LEFT(FOO, 10)
ALTER TABLE T DROP COLUMN FOO
ALTER TABLE T ADD COLUMN FOO VARCHAR(10)
```

### Changing column type

Column type change isn’t supported directly. To change the type of a column, there are two options:

#### Copy data to a different table

Create a new table and copy the data there. This allows to keep the data and change the type of the column as required, but the table name will change.

```sql
CREATE TABLE T_VER_2 (...)
INSERT INTO T_VER_2 (SELECT * FROM T)
DROP TABLE T
```

#### Drop existing table and recreate it

Drop the existing table with its data, and cleanup the metadata. Then,
restore the data from a different source.

```sql
DROP TABLE T
control.sh --meta remove --typeName T
CREATE TABLE T (...)
```

### Renaming a table

Table rename isn’t supported directly. To rename a table, create a new table and copy the data to it.

```sql
CREATE TABLE T_VER_2 (...)
INSERT INTO T_VER_2 (SELECT * FROM T)
DROP TABLE T
```

### Unexpected migration

Any unexpected migration that cannot be done with other tools can always be handled by creating a new table and moving the data from the old table to the new one. This can be done fully without downtime.

```sql
CREATE TABLE T_VER_2 (...)
INSERT INTO T_VER_2 (SELECT * FROM T)
DROP TABLE T
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
