---
description: >-
  An overview of changes, improvements, and what's new in MariaDB Community
  Server 13.1
---

# MariaDB 13.1 Changes & Improvements

{% include "../../.gitbook/includes/latest-13.1.md" %}

MariaDB 13.1 is a [rolling release](../about/release-model.md). It is an evolution of [MariaDB 13.0](../13.0/mariadb-13.0-changes-and-improvements.md) with many entirely new features.

## New Features

 * Support for JSON operators column->path and column->>path ([MDEV-13594](https://jira.mariadb.org/browse/MDEV-13594))
 * DENY clause for access control a.k.a. "negative grants" ([MDEV-14443](https://jira.mariadb.org/browse/MDEV-14443))
 * Implement interval partitioning similar to Oracle ([MDEV-15621](https://jira.mariadb.org/browse/MDEV-15621))
 * Improve error reporting of mysqlbinlog when used with --flashback ([MDEV-20749](https://jira.mariadb.org/browse/MDEV-20749))
 * Locking full table scan fails to use table-level locking ([MDEV-24813](https://jira.mariadb.org/browse/MDEV-24813))
 * Add formatted column support to JSON_TABLE ([MDEV-25727](https://jira.mariadb.org/browse/MDEV-25727))
 * A slave's ignored domain ids should not be validated when connecting to a master ([MDEV-28213](https://jira.mariadb.org/browse/MDEV-28213))
 * SST fails when table is defined with DATA DIRECTORY='/path/to' and datafile is larger than datadir space ([MDEV-29909](https://jira.mariadb.org/browse/MDEV-29909))
 * don't set utf8_is_utf8mb3 by default in the old-mode ([MDEV-30041](https://jira.mariadb.org/browse/MDEV-30041))
 * CREATE TRIGGER FOR { STARTUP | SHUTDOWN } ([MDEV-30645](https://jira.mariadb.org/browse/MDEV-30645))
 * Implement optional lengths for string types ([MDEV-31414](https://jira.mariadb.org/browse/MDEV-31414))
 * Add a variable and flag to check the configuration without actually starting the server ([MDEV-31527](https://jira.mariadb.org/browse/MDEV-31527))
 * Omit generated column values from mariadb-dump dumps ([MDEV-32362](https://jira.mariadb.org/browse/MDEV-32362))
 * NEW and OLD in a trigger as row variables ([MDEV-34723](https://jira.mariadb.org/browse/MDEV-34723))
 * provide various information about vector indexes ([MDEV-34805](https://jira.mariadb.org/browse/MDEV-34805))
 * PARSEC plugin should allow DBAs to specify number of iterations ([MDEV-35254](https://jira.mariadb.org/browse/MDEV-35254))
 * Implement table options to enable/disable features ([MDEV-37070](https://jira.mariadb.org/browse/MDEV-37070))
 * XMLISVALID() schema validation function ([MDEV-37262](https://jira.mariadb.org/browse/MDEV-37262))
 * Missed optimization opportunities of "TRUE OR any_expr" in SELECT clause ([MDEV-37713](https://jira.mariadb.org/browse/MDEV-37713))
 * Missed optimization opportunities of "FALSE and any_expr" ([MDEV-37714](https://jira.mariadb.org/browse/MDEV-37714))
 * Optional_metadata_fields Replace std::vector with MariaDB Types ([MDEV-38144](https://jira.mariadb.org/browse/MDEV-38144))
 * Add XXH hash function ([MDEV-38180](https://jira.mariadb.org/browse/MDEV-38180))
 * Expose adaptive hash index statistics in ANALYZE FORMAT=JSON ([MDEV-38305](https://jira.mariadb.org/browse/MDEV-38305))
 * Optimizer Trace Replay: Q1 2026 Dev Sprint Work 1 ([MDEV-38701](https://jira.mariadb.org/browse/MDEV-38701))
 * Proactive handling of InnoDB tablespace full condition ([MDEV-38936](https://jira.mariadb.org/browse/MDEV-38936))
 * BLOBs in MEMORY (HEAP) ([MDEV-38975](https://jira.mariadb.org/browse/MDEV-38975))
 * Add `LOCAL spvar` syntax for prepared statements and SYS_REFCURSORs ([MDEV-39022](https://jira.mariadb.org/browse/MDEV-39022))
 * resolveip: Replace deprecated network functions with modern equivalents ([MDEV-39169](https://jira.mariadb.org/browse/MDEV-39169))
 * MySQL Compatibility for Parenthesised SELECT INTO Statements ([MDEV-39176](https://jira.mariadb.org/browse/MDEV-39176))
 * Package-wide TYPE for variable declarations ([MDEV-39587](https://jira.mariadb.org/browse/MDEV-39587))
 * Add support for CHECK TABLE to memory tables ([MDEV-40030](https://jira.mariadb.org/browse/MDEV-40030))
 * slave_skip_errors currently read only, change to writable when slaves stopped ([MDEV-7394](https://jira.mariadb.org/browse/MDEV-7394))

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
