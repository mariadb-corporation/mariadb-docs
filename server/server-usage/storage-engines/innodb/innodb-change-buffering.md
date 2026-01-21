---
description: >-
  Learn about the change buffer, an optimization that delays secondary index
  writes to reduce I/O overhead for non-unique index modifications.
---

# InnoDB Change Buffering

{% hint style="warning" %}
The change buffer has been disabled by default from [MariaDB 10.5.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10515-release-notes), [MariaDB 10.6.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1067-release-notes), [MariaDB 10.7.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1073-release-notes) and [MariaDB 10.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1082-release-notes) ([MDEV-27734](https://jira.mariadb.org/browse/MDEV-27734)), was deprecated and ignored from [MariaDB 10.9.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/mariadb-1090-release-notes) ([MDEV-27735](https://jira.mariadb.org/browse/MDEV-27735)), and was removed in [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes) ([MDEV-29694](https://jira.mariadb.org/browse/MDEV-29694)).
{% endhint %}

Benchmarks attached to [MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514) show that the change buffer sometimes reduces performance, and in the best case seem to bring a few per cent improvement to throughput. However, such improvement could come with a price: If the buffered changes are never merged ([MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514), motivated by the reduction of random crashes and the removal of an innodb\_force\_recovery option that can inflict further corruption), then the InnoDB system tablespace can grow out of control ([MDEV-21952](https://jira.mariadb.org/browse/MDEV-21952)).

`INSERT`, `UPDATE`, and `DELETE` statements can be particularly heavy operations to perform, as all indexes need to be updated after each change. For this reason these changes are often buffered.

Pages are modified in the [buffer pool](innodb-buffer-pool.md), and not immediately on disk. After all the records that cover the changes to a data page have been written to the InnoDB redo log, the changed page may be written (''flushed'') to a data file. Pages that have been modified in memory and not yet flushed are called dirty pages.

The Change Buffer is an optimization that allows some data to be modified even though the data page does not exist in the buffer pool. Instead of modifying the data in its final destination, we would insert a record into a special Change Buffer that resides in the system tablespace. When the page is read into the buffer pool for any reason, the buffered changes are applied to it.

The Change Buffer only contains changes to secondary index leaf pages.

In the days of old, only inserted rows could be buffered, so this buffer was called _Insert Buffer_. The old name still appears in several places, for example in the output of [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md).

Inserts to `UNIQUE` secondary indexes cannot be buffered unless [unique\_checks=0](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#unique_checks) is used. This may sometimes allow duplicates to be inserted into the `UNIQUE` secondary index. Much of the time, the `UNIQUE` constraint would be checked because the change buffer could only be used if the index page is not located in the buffer pool.

When rows are deleted, a flag is set, thus rows are not immediately deleted. Delete-marked records may be purged after the transaction has been committed and any read views that were created before the commit have been closed. Delete-mark and purge buffering of any secondary indexes is allowed.

`ROLLBACK` never makes use of the change buffer; it would force a merge of any changes that were buffered during the execution of the transaction.

The Change Buffer is an optimization because:

* Some random-access page reads are transformed into modifications of change buffer pages.
* A change buffer page can be modified several times in memory and be flushed to disk only once.
* Dirty pages are flushed together, so the number of IO operations is lower.

If the server crashes or is shut down, the Change Buffer might not be empty. The Change Buffer resides in the InnoDB system tablespace, covered by the write-ahead log, so they can be applied at server restart. A shutdown with [innodb\_fast\_shutdown=0](innodb-system-variables.md#innodb_fast_shutdown) will merge all buffered changes.

There is no background task that merges the change buffer to the secondary index pages. Changes are only merged on demand.

{% hint style="warning" %}
The Change Buffer was removed in [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110) because it has been a prominent source of corruption bugs that have been extremely hard to reproduce.
{% endhint %}

The main server system variable here is [innodb\_change\_buffering](innodb-system-variables.md#innodb_change_buffering), which determines which form of change buffering, if any, to use.

The following settings are available:

* inserts
  * Only buffer insert operations
* deletes
  * Only buffer delete operations
* changes
  * Buffer both insert and delete operations
* purges
  * Buffer the actual physical deletes that occur in the background
* all
  * Buffer inserts, deletes and purges. Default setting from [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) until [MariaDB 10.5.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10514-release-notes), [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1066-release-notes), [MariaDB 10.7.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1072-release-notes) and [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1081-release-notes).
* none
  * Don't buffer any operations. Default from [MariaDB 10.5.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10515-release-notes), [MariaDB 10.6.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1067-release-notes), [MariaDB 10.7.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1073-release-notes) and [MariaDB 10.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1082-release-notes).

Modifying the value of this variable only affects the buffering of new operations. The merging of already buffered changes is not affected.

The [innodb\_change\_buffer\_max\_size](innodb-system-variables.md#innodb_change_buffer_max_size) system variable determines the maximum size of the change buffer, expressed as a percentage of the buffer pool.

## See Also

* [InnoDB Buffer Pool](innodb-buffer-pool.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
