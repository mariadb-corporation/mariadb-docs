---
description: >-
  An overview of changes, improvements, and what's new in MariaDB Community
  Server 13.1
---

# MariaDB 13.1 Changes & Improvements

{% include "../../.gitbook/includes/latest-13.1.md" %}

MariaDB 13.1 is a [rolling release](../about/release-model.md). It is an evolution of [MariaDB 13.0](../13.0/mariadb-13.0-changes-and-improvements.md) with many entirely new features.

## New Features

 * Support for JSON operators `column->path` and `column->>path` ([MDEV-13594](https://jira.mariadb.org/browse/MDEV-13594))
 * DENY clause for access control a.k.a. "negative grants" ([MDEV-14443](https://jira.mariadb.org/browse/MDEV-14443))
 * Auto-adding new partitions for `PARTITION BY RANGE` ([MDEV-15621](https://jira.mariadb.org/browse/MDEV-15621))
 * Improve error reporting of mysqlbinlog when used with `--flashback` ([MDEV-20749](https://jira.mariadb.org/browse/MDEV-20749))
 * Locking full table scan fails to use table-level locking ([MDEV-24813](https://jira.mariadb.org/browse/MDEV-24813))
 * Add formatted column support to `JSON_TABLE` ([MDEV-25727](https://jira.mariadb.org/browse/MDEV-25727))
 * Ignored domain ids skip validation when connecting to a master ([MDEV-28213](https://jira.mariadb.org/browse/MDEV-28213))
 * The default `utf8` character set is now `utf8mb4` ([MDEV-30041](https://jira.mariadb.org/browse/MDEV-30041))
 * New statement `CREATE TRIGGER FOR { STARTUP | SHUTDOWN }` ([MDEV-30645](https://jira.mariadb.org/browse/MDEV-30645))
 * Optional lengths for string types: `VARCHAR[(N)]` ([MDEV-31414](https://jira.mariadb.org/browse/MDEV-31414))
 * `mariadbd --validate-config` to check the configuration for validity without starting the server ([MDEV-31527](https://jira.mariadb.org/browse/MDEV-31527))
 * `mariadb-dump` no longer includes generated column values in a dump ([MDEV-32362](https://jira.mariadb.org/browse/MDEV-32362))
 * `NEW` and `OLD` in a trigger can be used as row variables ([MDEV-34723](https://jira.mariadb.org/browse/MDEV-34723))
 * `INFORMATION_SCHEMA.VECTOR_INDEXES` provides information about vector indexes ([MDEV-34805](https://jira.mariadb.org/browse/MDEV-34805))
 * `parsec_iterations` session variables allows to set the number of PBKDF2 rounds for PARSEC plugin ([MDEV-35254](https://jira.mariadb.org/browse/MDEV-35254))
 * `ADAPTIVE_HASH_INDEX = { YES | NO | DEFAULT }` can specify per InnoDB table whether to use AHI ([MDEV-37070](https://jira.mariadb.org/browse/MDEV-37070))
 * XMLISVALID() schema validation function ([MDEV-37262](https://jira.mariadb.org/browse/MDEV-37262))
 * `AND`/`OR` can now short-circuit the execution for any argument not in a strictly left-to-right fashion ([MDEV-37713](https://jira.mariadb.org/browse/MDEV-37713), [MDEV-37714](https://jira.mariadb.org/browse/MDEV-37714))
 * `XXH3`, `XXH32`, `XXH64`, `XXH128` family of hash functions ([MDEV-38180](https://jira.mariadb.org/browse/MDEV-38180))
 * Adaptive hash index statistics is shown in ANALYZE FORMAT=JSON ([MDEV-38305](https://jira.mariadb.org/browse/MDEV-38305))
 * Optimizer Context Recorder to record the optimizer data and then analyze query optimization on another server instance ([MDEV-38701](https://jira.mariadb.org/browse/MDEV-38701))
 * `innodb_tablespace_size_warning_threshold` and `innodb_tablespace_size_warning_pct` variables to get a warning when InnoDB tablespace is getting close to full (before it's 100% full and the service is disrupted) ([MDEV-38936](https://jira.mariadb.org/browse/MDEV-38936))
 * MEMORY tables support variable-length data types, `VARCHAR` and `TEXT`/`BLOB` ([MDEV-38975](https://jira.mariadb.org/browse/MDEV-38975))
 * Local routine variables usable in `PREPARE`/`EXECUTE`/`DEALLOCATE` and `OPEN ... FOR` ([MDEV-39022](https://jira.mariadb.org/browse/MDEV-39022))
 * Package-wide TYPE declarations ([MDEV-39587](https://jira.mariadb.org/browse/MDEV-39587))
 * CHECK TABLE supports MEMORY tables ([MDEV-40030](https://jira.mariadb.org/browse/MDEV-40030))
 * `slave_skip_errors` variable can be modified without server restart ([MDEV-7394](https://jira.mariadb.org/browse/MDEV-7394))

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
