# MariaDB ColumnStore 6.2.3 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/columnstore/mariadb-columnstore-6-release-notes/MariaDB_Enterprise_ColumnStore/README.md) 6.2.3 is a maintenance release of MariaDB Enterprise ColumnStore. MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the third release in the Enterprise ColumnStore 6 series.

MariaDB Enterprise ColumnStore 6.2.3 was released on 2022-02-23. This release is of General Availability (GA) maturity.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.5-2 and MariaDB Enterprise Server 10.6.7-3.

## Notable Changes

* CMAPI 1.6.2 was originally included
* CMAPI 1.6.3 is now included
  * CMAPI is a REST API for administering MariaDB Enterprise ColumnStore in multi-node topologies.
  * For additional information, see "Release Notes for CMAPI 1.6.2" and "Release Notes for CMAPI 1.6.3".
  * Added encrypted password support for the cross engine join user. ([MCOL-4946](https://jira.mariadb.org/browse/MCOL-4946))

## Issues Fixed

### Can result in unexpected behavior

* UPDATE with cross engine IN subquery produced unexpected results. ([MCOL-4868](https://jira.mariadb.org/browse/MCOL-4868))
* Error can arise with cross engine JOIN: Internal error: CrossEngineStep::execute() caught getSignedNullValue(): got bad column width (4) ([MCOL-4874](https://jira.mariadb.org/browse/MCOL-4874))
* IN operation doesn't respect COLLATE ([MCOL-4899](https://jira.mariadb.org/browse/MCOL-4899))
* Slower than expected bulk insertion. ([MCOL-4912](https://jira.mariadb.org/browse/MCOL-4912))
* A ColumnStore process thread read call could last indefinitely. ([MCOL-4927](https://jira.mariadb.org/browse/MCOL-4927))
* With this release, if no data appears when a ColumnStore process thread makes a read call, the thread logs an error, closes the socket, and proceeds.
* Prior to this release, a ColumnStore process thread would synchronously wait for data to appear in the socket.
* QueryStats does not automatically log each query to calGetTrace() results. ([MCOL-4944](https://jira.mariadb.org/browse/MCOL-4944))
* With this release, when QueryStats is enabled, queries are automatically logged to infinidb\_querystats.querystats
* Prior to this release, it was necessary to execute SELECT calGetTrace(1) to log queries even with QueryStats enabled.

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 6.2.3 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
* Ubuntu 18.04 (x86\_64)
* Ubuntu 20.04 (x86\_64)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
