---
description: >-
  Understand the performance implications and best practices for replicating
  tables without primary keys when using row-based logging, including how to
  avoid full table scans.
---

# Row-based Replication With No Primary Key

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

MariaDB improves on row-based [replication](./) (see [binary log formats](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md)) of tables which have no primary key but do have some other index. This is based in part on the original Percona patch `row_based_replication_without_primary_key.patch`, with some additional
fixes and enhancements.

When row-based replication is used with [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) or [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md), the replica needs to locate each replicated row based on the value in columns. If the table contains at least one index; an index lookup will be used (otherwise a table scan is needed for each row, which is extremely inefficient for all but the smallest table and generally to be avoided).

In MariaDB, the slave will try to choose a good index among any available:

* The primary key is used, if there is one.
* Else, the first unique index without `NULL`-able columns is used, if there is
  one.
* Else, a choice is made among any normal indexes on the table (e.g. a [FULLTEXT](../optimization-and-tuning/optimization-and-indexes/full-text-indexes/) index is not considered).

The choice of which of several non-unique indexes to use is based on the
cardinality of indexes; the one that is most selective (has the smallest average number of rows per distinct tuple of column values) is preferred. Note that for this choice to be effective, for most storage engines (like MyISAM, InnoDB) it is necessary to make sure [ANALYZE TABLE](../../reference/sql-statements/table-statements/analyze-table.md) has been run on the slave, otherwise statistics about index cardinality is not available. In the absence of index cardinality, the first unique index is chosen, if any, else the first non-unique index.

{% hint style="info" %}
[Conflict Detection and Resolution (CDR) triggers](conflict-detection-and-resolution-triggers.md), added in MariaDB Enterprise Server 12.3 (beta), require the replicated table to have a `PRIMARY KEY`. On a table without one, a conflicting row event is never routed to a CDR trigger, and the applier raises its usual error instead.
{% endhint %}

## See Also

* [Binary Log Formats](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md)
* [Conflict Detection and Resolution (CDR) Triggers](conflict-detection-and-resolution-triggers.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
