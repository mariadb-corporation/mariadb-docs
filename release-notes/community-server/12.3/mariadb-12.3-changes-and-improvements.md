---
description: >-
  An overview of changes, improvements, and what's new in MariaDB Community
  Server 12.3
---

# MariaDB 12.3 Changes & Improvements

{% include "../../.gitbook/includes/latest-12-3.md" %}

MariaDB 12.3 is a [long term release](../about/release-model.md), maintained until June 2029.

## New Features

* New hash algorithms for `PARTITION BY KEY` ([MDEV-9826](https://jira.mariadb.com/browse/MDEV-9826))
* Add support for Oracle `TO\_DATE()` ([MDEV-19683](https://jira.mariadb.com/browse/MDEV-19683))
* Configurable defaults for `MASTER\_SSL_*` settings for `CHANGE MASTER` ([MDEV-28302](https://jira.mariadb.com/browse/MDEV-28302))
* Hashicorp Plugin: Implement cache flush for forced key rotation ([MDEV-30847](https://jira.mariadb.com/browse/MDEV-30847))
* Fragment ROW replication events larger than `max\_packet\_size` ([MDEV-32570](https://jira.mariadb.com/browse/MDEV-32570))
* Support for cursors on prepared statements ([MDEV-33830](https://jira.mariadb.com/browse/MDEV-33830))
* `SET PATH` statement ([MDEV-34391](https://jira.mariadb.com/browse/MDEV-34391))
* Improving performance of binary logging by removing the need of syncing it ([MDEV-34705](https://jira.mariadb.com/browse/MDEV-34705))
* Implement Global temporary tables ([MDEV-35915](https://jira.mariadb.com/browse/MDEV-35915))
* Optimise reorderable LEFT JOINs ([MDEV-36055](https://jira.mariadb.com/browse/MDEV-36055))
* Support for `IS JSON` predicate ([MDEV-37072](https://jira.mariadb.com/browse/MDEV-37072))
* Allow `UPDATE`/`DELETE` to read from a CTE ([MDEV-37220](https://jira.mariadb.com/browse/MDEV-37220))
* Basic XML data type ([MDEV-37261](https://jira.mariadb.com/browse/MDEV-37261))


## List of All MariaDB 12.3 Releases

| Date        | Release              | Status  | Release Notes              | Changelog                                 |
| ----------- | -------------------- | ------- | -------------------------- | ----------------------------------------- |
| 22 Dec 2025 | MariaDB 12.3 Preview | Preview |                            |                                           |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}
