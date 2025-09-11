# MariaDB ColumnStore 6.2.2 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 6.2.2 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) . MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the second release in the Enterprise ColumnStore 6 series.

MariaDB Enterprise ColumnStore 6.2.2 was released on 2021-12-13. This release is of General Availability (GA) maturity.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.5-2.

## Notable Changes

* CMAPI 1.6 is now included
  * CMAPI is a REST API for administering MariaDB Enterprise ColumnStore in multi-node topologies.
  * For additional information, see "Release Notes for CMAPI 1.6".
* Performance improvements for query execution ([MCOL-4849](https://jira.mariadb.org/browse/MCOL-4849), [MCOL-4810](https://jira.mariadb.org/browse/MCOL-4810))
  * ColumnStore's ExeMgr process now performs fewer context switches.
  * ColumnStore's PrimProc process now uses less memory.
  * Some internal operations have been improved to use more parallelism.
* JOIN support for columns using increased DECIMAL precision ([MCOL-4173](https://jira.mariadb.org/browse/MCOL-4173))
  * ColumnStore can now JOIN tables on DECIMAL(38) columns.
* Utility to rebuild the Extent Map ([MCOL-312](https://jira.mariadb.org/browse/MCOL-312))
  * The mcsRebuildEM utility is now installed by Enterprise ColumnStore.
  * Enterprise ColumnStore uses the Extent Map to store metadata about the data stored in each extent. There are certain situations when metadata in the Extent Map can become inconsistent with the extents. In these situations, the Extent Map should be rebuilt.
  * When no options are provided, the mcsRebuildEM utility rebuilds the Extent Map. It does not check whether the Extent Map is already consistent with the extents. It rebuilds the Extent Map even if the Extent Map is already consistent.
  * When the -d option is provided, the mcsRebuildEM utility displays what changes it would make to the Extent Map and exits. This option can be used to test the operation without writing changes to disk.
  * When the -s option is provided, the mcsRebuildEM utility displays the current contents of the Extent Map and exits.

## Issues Fixed

### Can result in a hang or crash

* When columnstore\_select\_handler=ON is configured, the server can crash if a SELECT statement uses aggregate functions. ([MCOL-4728](https://jira.mariadb.org/browse/MCOL-4728))

### Can result in unexpected behavior

* The ColumnStore storage engine sometimes attempts to connect to the ExeMgr process on the old primary ColumnStore node after failover. ([MCOL-4920](https://jira.mariadb.org/browse/MCOL-4920))
* cpimport writes output to standard error (stderr) when no error occurs. ([MCOL-4855](https://jira.mariadb.org/browse/MCOL-4855))
* SELECT and UPDATE statements fail when the statement uses the CONVERT\_TZ() function. ([MCOL-1356](https://jira.mariadb.org/browse/MCOL-1356))\
  The following error message would be raised to the client:

```
ERROR 1178 (42000): The storage engine for the table doesn't support IDB-1001: Function 'convert_tz' isn't supported.
```

* SELECT statements sometimes fail when the statement uses the RAND() function ([MCOL-4771](https://jira.mariadb.org/browse/MCOL-4771), [MCOL-4487](https://jira.mariadb.org/browse/MCOL-4487))
  * The following error message would be raised to the client:`<<code>>`\
    ERROR 1815 (HY000): Internal error: IDB-2045: At least one PrimProc closed the connection unexpectedly.\
    <.
* SELECT statements could return wrong results on large tables if the WHERE condition contains varchar\_col < char\_col ([MCOL-4823](https://jira.mariadb.org/browse/MCOL-4823))
* When columnstore\_select\_handler=ON is configured, SELECT statements returns the wrong results if a predicate in the WHERE condition uses an alias that is dependent on the result of a window function. ([MCOL-4719](https://jira.mariadb.org/browse/MCOL-4719))
* The columnstoreAlias.sh script raises an error upon login for single node ColumnStore ([MCOL-4832](https://jira.mariadb.org/browse/MCOL-4832))

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 6.2.2 is provided for:

* CentOS 7 (x86\_64)
* Debian 9 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64)
* Ubuntu 18.04 (x86\_64)
* Ubuntu 20.04 (x86\_64)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
