---
description: >-
  MariaDB Enterprise ColumnStore locking: lockless reads, table locks for
  writes, and write metadata locks during cpimport bulk loads, designed to
  minimize blocking on analytics.
---

# MariaDB Enterprise Columnstore Locking

## Overview

MariaDB Enterprise ColumnStore minimizes locking for analytical workloads, bulk data loads, and online schema changes.

## Lockless Reads

MariaDB Enterprise ColumnStore supports lockless reads.

## Locking for Writes

MariaDB Enterprise ColumnStore requires a table lock for write operations.

## Locking for Data Loading

MariaDB Enterprise ColumnStore requires a write metadata lock (MDL) on the table when a bulk data load is performed with [cpimport](../clients-and-tools/data-import/mariadb-enterprise-columnstore-data-loading-with-cpimport.md).

When a bulk data load is running:

* Read queries will not be blocked.
* Write queries and concurrent bulk data loads on the same table will be blocked until the bulk data load operation is complete, and the write metadata lock on the table has been released.
* The write metadata lock (MDL) can be monitored with the [METADATA\_LOCK\_INFO plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/metadata-lock-info-plugin).

For additional information, see "[MariaDB Enterprise ColumnStore Data Loading](../clients-and-tools/data-import/)".

## Online Schema Changes

MariaDB Enterprise ColumnStore supports online schema changes, so that supported DDL operations can be performed without blocking reads. The supported DDL operations only require a write metadata lock (MDL) on the target table.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
