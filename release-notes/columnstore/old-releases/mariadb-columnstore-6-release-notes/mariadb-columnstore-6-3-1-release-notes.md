# MariaDB ColumnStore 6.3.1 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 6.3.1 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) . MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the fourth release in the Enterprise ColumnStore 6 series.

MariaDB Enterprise ColumnStore 6.3.1 was released on 2022-04-25. This release is of General Availability (GA) maturity.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.7-3.

## Notable Changes

* Deprecated and historical values have been removed from Columnstore.xml ([MCOL-4560](https://jira.mariadb.org/browse/MCOL-4560))
* Performance improvements. ([MCOL-4801](https://jira.mariadb.org/browse/MCOL-4801), [MCOL-4871](https://jira.mariadb.org/browse/MCOL-4871), [MCOL-4809](https://jira.mariadb.org/browse/MCOL-4809), [MCOL-4957](https://jira.mariadb.org/browse/MCOL-4957))

## Issues Fixed

### Can result in a hang or crash

* Segfault in Storage Manager due to thread limits. ([MCOL-3983](https://jira.mariadb.org/browse/MCOL-3983))
* Segfault when using distributed aggregate functions. ([MCOL-4807](https://jira.mariadb.org/browse/MCOL-4807))
* Segfault during cpimport to table with large column count. ([MCOL-4974](https://jira.mariadb.org/browse/MCOL-4974))
* ExeMgr crashes after a large join, resulting in client-side error ERROR 1815 (HY000): Internal error: IDB-2004: Cannot connect to ExeMgr. ([MCOL-4841](https://jira.mariadb.org/browse/MCOL-4841))

### Can result in unexpected behavior

* ROUND() on DOUBLE in case statements in conjunction with subqueries can generate incorrect value. ([MCOL-4940](https://jira.mariadb.org/browse/MCOL-4940))
* CRC32(), when called with two arguments, against a ColumnStore table, returns the wrong value. ([MCOL-4966](https://jira.mariadb.org/browse/MCOL-4966))
* A query with filter condition on subquery with window function can return the wrong result. ([MCOL-4570](https://jira.mariadb.org/browse/MCOL-4570))
* Incorrect help text. ([MCOL-4834](https://jira.mariadb.org/browse/MCOL-4834))

## Related to install and upgrade

* On Debian, non-interactive upgrade complains that /etc/columnstore/Columnstore.xml has been modified since installation. ([MCOL-4928](https://jira.mariadb.org/browse/MCOL-4928))
* Upgrade from ColumnStore 5 to ColumnStore 6 does not restore saved configuration files. ([MCOL-4965](https://jira.mariadb.org/browse/MCOL-4965))
  * Prior to this release, configuration files were saved at uninstall but not restored upon upgrade.
  * With this release, ColumnStore configuration files are properly restored upon reinstall. New parameters, included in the configuration files packaged with the release, will not be merged and must be migrated manually.
  * With this release, when manually upgrading (uninstall and reinstall), the server.cnf is replaced with the packaged copy.
  * With this release, when upgrading by repository, the existing server.cnf is retained.

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 6.3.1 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
* Ubuntu 18.04 (x86\_64)
* Ubuntu 20.04 (x86\_64)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
