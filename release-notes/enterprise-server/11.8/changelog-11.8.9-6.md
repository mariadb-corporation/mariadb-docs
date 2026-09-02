---
description: >-
  MariaDB Enterprise Server 11.8.9-6 is a Stable (GA) maintenance release of
  MariaDB Enterprise Server 11.8, released on TBD
hidden: true
---

# Changelog for MariaDB Enterprise Server 11.8.9-6

<a href="https://mariadb.com/downloads/enterprise/enterprise-server/" class="button primary">Download</a> <a href="11.8.9-6.md" class="button secondary">Release Notes</a> <a class="button secondary">Changelog</a> <a href="whats-new.md" class="button secondary">Overview of Enterprise Server 11.8</a>

<!-- TODO(DOCS-6574): set the release date at publish time. TODO-6192's stated dates
     (internal 30 Jul 2026, public 3 Aug 2026) have both passed; the working date is
     "ASAP". Update here AND in the frontmatter description. -->
**Release date:** TBD

## Issues Fixed

* MariaDB 11.4 Audit Plugin Changes server_audit_syslog_ident from Hyphen (-) to Underscore (_) ([MENT-2862](https://jira.mariadb.org/browse/MENT-2862))
* ALTER TABLE ... AUTO_INCREMENT = NN; should return a Warning if it can not use the provided value ([MDEV-33660](https://jira.mariadb.org/browse/MDEV-33660))
* The rsync SST method of Galera worked incorrectly if innodb_log_group_home_dir or aria_log_dir_path were not the same as datadir at the SST donor node; this release has a fix for the rsync SST script to support varying data directory locations ([MDEV-36677](https://jira.mariadb.org/browse/MDEV-36677))
* A potential deadlock happening when MariaDB sequence operation is replicated as part of Galera streaming replication has been fixed ([MDEV-38869](https://jira.mariadb.org/browse/MDEV-38869))
* Flaky binlog.binlog_gtid_index test ([MDEV-39779](https://jira.mariadb.org/browse/MDEV-39779))
* InnoDB could fail to recover after being killed in a DDL operation. ([MDEV-40728](https://jira.mariadb.org/browse/MDEV-40728))
* When executing crash recovery in multiple batches, InnoDB may fail to extend a file and crash on a subsequent write to it ([MDEV-40756](https://jira.mariadb.org/browse/MDEV-40756))
* CREATE TABLE AS SELECT did not replicate correctly in Galera. ([MDEV-40929](https://jira.mariadb.org/browse/MDEV-40929))
* An ALTER TABLE on a system-versioned table that contains virtual columns and a fulltext index could crash. ([MDEV-40985](https://jira.mariadb.org/browse/MDEV-40985))
* Validation during json normalization has bee made inline for increased performance. ([MDEV-40174](https://jira.mariadb.org/browse/MDEV-40174))
* btr_page_reorganize_low() uses the buffer pool just to obtain a scratch block ([MDEV-40408](https://jira.mariadb.org/browse/MDEV-40408))
* rpl.rpl_gtid_crash fails due to salve Failed to sync with master ([MDEV-40575](https://jira.mariadb.org/browse/MDEV-40575))
* Fix ROLLUP query results with empty result set.  Patch by Jaeheon Shim. ([MDEV-40698](https://jira.mariadb.org/browse/MDEV-40698))
* Redundant calls to convert implicit record locks to explicit ones when table S-lock is held ([MDEV-40805](https://jira.mariadb.org/browse/MDEV-40805))
* Large memory allocations use MAP_NORESERVE where available (Linux and Illumos) to ensure that large memory mappings (e.g. 8TiB on default innodb_buffer_pool_size_max) do not result in memory actually being reserved (which it is by default on Illumos). --large-page memory behaviour isn't changed. ([MDEV-40921](https://jira.mariadb.org/browse/MDEV-40921))
* Assertion `bitmap_is_set_all(&table->s->all_set)' fails on slave with binlog_row_image=MINIMAL ([MDEV-39774](https://jira.mariadb.org/browse/MDEV-39774))

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
