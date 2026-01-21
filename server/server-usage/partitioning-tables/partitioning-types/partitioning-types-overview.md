---
description: >-
  An introduction to the various partitioning strategies available in MariaDB,
  helping you choose the right method for your data distribution needs.
---

# Partitioning Types Overview

A partitioning type determines how a partitioned table's rows are distributed across partitions. Some partition types require the user to specify a partitioning expression that determines in which partition a row are stored.

The size of individual partitions depends on the partitioning type. Read and write performance are affected by the partitioning expression. Therefore, these choices should be made carefully.

## Partitioning Types

MariaDB supports the following partitioning types:

* [RANGE](range-partitioning-type.md)
* [LIST](list-partitioning-type.md)
* [RANGE COLUMNS and LIST COLUMNS](range-columns-and-list-columns-partitioning-types.md)
* [HASH](hash-partitioning-type.md)
* [LINEAR HASH](linear-hash-partitioning-type.md)
* [KEY](key-partitioning-type.md)
* [LINEAR KEY](linear-key-partitioning-type.md)
* [SYSTEM\_TIME](../../../reference/sql-structure/temporal-tables/system-versioned-tables.md)

## See Also

* [Partitioning Overview](../partitioning-overview.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
