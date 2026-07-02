---
description: >-
  Create SPATIAL (R-tree) indexes on geometry columns in MyISAM, Aria, and
  InnoDB tables.
---

# SPATIAL INDEX

## Description

On [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/), [Aria](../../../server-usage/storage-engines/aria/) and [InnoDB](../../../server-usage/storage-engines/innodb/) tables, MariaDB can create spatial indexes (an R-tree index) using syntax similar to that for creating regular indexes, but extended with the `SPATIAL` keyword. Columns in spatial indexes must be declared `NOT NULL`.

Spatial indexes can be created when the table is created, or added after the fact:

```sql
CREATE TABLE geom (g GEOMETRY NOT NULL, SPATIAL INDEX(g));
```

```sql
ALTER TABLE geom ADD SPATIAL INDEX(g);
```

```sql
CREATE SPATIAL INDEX sp_index ON geom (g);
```

`SPATIAL INDEX` creates an `R-tree` index. For storage engines that support non-spatial indexing of spatial columns, the engine creates a `B-tree` index. A `B-tree` index on spatial values is useful for\
exact-value lookups, but not for range scans.

For more information on indexing spatial columns, see [CREATE INDEX](../../sql-statements/data-definition/create/create-index.md).

To drop spatial indexes, use [ALTER TABLE](../../sql-statements/data-definition/alter/alter-table/) or [DROP INDEX](../../sql-statements/data-definition/drop/drop-index.md):

```sql
ALTER TABLE geom DROP INDEX g;
```

```sql
DROP INDEX sp_index ON geom;
```

### Data-at-Rest Encryption

If [innodb\_checksum\_algorithm](../../../clients-and-utilities/administrative-tools/innochecksum.md) is set to `full_crc32` or `strict_full_crc32`, and if the table does not use [ROW\_FORMAT=COMPRESSED](../../../server-usage/storage-engines/innodb/innodb-row-formats/), InnoDB spatial indexes are encrypted if the table is encrypted.

See [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026) for more information.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
