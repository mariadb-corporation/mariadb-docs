---
description: >-
  An overview of changes, improvements, and what's new in MariaDB Community
  Server 13.0
---

# MariaDB 13.0 Changes & Improvements

{% include "../../.gitbook/includes/latest-13.0.md" %}

MariaDB 13.0 is a [rolling release](../about/release-model.md). It is an evolution of [MariaDB 12.3](../12.3/mariadb-12.3-changes-and-improvements.md) with several entirely new features.

## New Features

* Add support for `TYPE .. IS REF CURSOR` ([MDEV-10152](https://jira.mariadb.org/browse/MDEV-10152))
* One can specify timestamp format for the audit plugin log ([MDEV-18386](https://jira.mariadb.org/browse/MDEV-18386))
* Atomic `CREATE OR REPLACE TABLE` ([MDEV-25292](https://jira.mariadb.org/browse/MDEV-25292))
* `INFORMATON_SCHEMA.SYSTEM_VARIABLES` shows if a variable is deprecated ([MDEV-35369](https://jira.mariadb.org/browse/MDEV-35369))
* `INFORMATON_SCHEMA.STATISTICS` and `INFORMATON_SCHEMA.COLUMNS` shows engine specific create options ([MDEV-36444](https://jira.mariadb.org/browse/MDEV-36444))
* Optimizer Trace includes used optimizer statistics ([MDEV-36511](https://jira.mariadb.org/browse/MDEV-36511))
* New `innodb_log_archive` variable makes InnoDB to preserve WAL instead of overwriting it in a ring buffer ([MDEV-37949](https://jira.mariadb.org/browse/MDEV-37949))
* New `QB_NAME()` optimizer hint ([MDEV-38045](https://jira.mariadb.org/browse/MDEV-38045))
* Support `RECORD` in routine parameters and function `RETURN` clause ([MDEV-38768](https://jira.mariadb.org/browse/MDEV-38768))
* Reversed executable comments ([MDEV-7381](https://jira.mariadb.org/browse/MDEV-7381))

## Notable Items

* `CHANGE MASTER` now resets `Master_Server_Id` in `SHOW SLAVES STATUS` ([MDEV-15327](https://jira.mariadb.org/browse/MDEV-15327))
* Faster unique indexes over `CHAR` columns in MEMORY tables (incl. temporary tables) ([MDEV-21543](https://jira.mariadb.org/browse/MDEV-21543))
* `PERFORMANCE_SCHEMA` now uses `XXH3_128` hash for digest. Looks like MD5, but much faster and no problems in FIPS mode. ([MDEV-31669](https://jira.mariadb.org/browse/MDEV-31669))
* `binlog_row_event_max_size` default value was increased to 64k ([MDEV-37608](https://jira.mariadb.org/browse/MDEV-37608))
* `default_master_connection` can now be set on global level ([MDEV-9247](https://jira.mariadb.org/browse/MDEV-9247))


{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
