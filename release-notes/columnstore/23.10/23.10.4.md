# MariaDB ColumnStore 23.10.4 Release Notes

### Overview

MariaDB Enterprise ColumnStore 23.10.4 is a maintenance release of MariaDB Enterprise ColumnStore. MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 23.10.4 was released on 19 May 2025. This release is of General Availability (GA) maturity. MariaDB Enterprise ColumnStore 23.10.4 is a GA release in the 23.10 series.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.21-17.

### Notable Changes

* New memory consumption accounting mechanism to prevent OOM events-related crashes. ([MCOL-5797](https://jira.mariadb.org/browse/MCOL-5797))
* FROM\_UNIXTIME(negativeDecimal) not behaving as InnoDB ([MCOL-4605](https://jira.mariadb.org/browse/MCOL-4605))
* SEC\_TO\_TIME(wideDecimal) returns 0 in DECIMAL context ([MCOL-4607](https://jira.mariadb.org/browse/MCOL-4607))
* MOD loses precision on huge narrow decimal ([MCOL-4611](https://jira.mariadb.org/browse/MCOL-4611))
* Different results compared to innodb with union all and subselect with null in select and impossible where condition ([MCOL-4942](https://jira.mariadb.org/browse/MCOL-4942))
* cmapi support for log collection ([MCOL-5300](https://jira.mariadb.org/browse/MCOL-5300))
* JSON\_ARRAYAGG in MCS works differently than in InnoDB. ([MCOL-5394](https://jira.mariadb.org/browse/MCOL-5394))
* CLI Startup - Single start command for Single Node ([MCOL-5525](https://jira.mariadb.org/browse/MCOL-5525))
* Alias "mcs CLUSTER" commands to just mcs ([MCOL-5526](https://jira.mariadb.org/browse/MCOL-5526))
* Cmapi (mcs cli) support for columnstore backups ([MCOL-5618](https://jira.mariadb.org/browse/MCOL-5618))
* Improve Client Error Messaging and async broadcasting config. ([MCOL-5638](https://jira.mariadb.org/browse/MCOL-5638))
* CTE/aggreation function give wrong results ([MCOL-5842](https://jira.mariadb.org/browse/MCOL-5842))
* DROP TABLE IF EXISTS should not generate errors for non existing tables ([MCOL-5890](https://jira.mariadb.org/browse/MCOL-5890))
* Disk based GROUP\_CONCAT() ([MCOL-5921](https://jira.mariadb.org/browse/MCOL-5921))
* NULLIF function returns -32768 instead of NULL when querying a Columnstore table ([MCOL-5922](https://jira.mariadb.org/browse/MCOL-5922))
* when a value of a column is empty text ('') the result of group\_concat(json\_object(...)) is null instead of the correct result set ([MCOL-5986](https://jira.mariadb.org/browse/MCOL-5986))

### Issues Fixed

#### Can result in hang or crash

* Creating different keys with cskeys on all nodes can break cluster(key not distributed properly) ([MCOL-5019](https://jira.mariadb.org/browse/MCOL-5019))
* Bitwise aggregation functions do not work with wide decimals (internal error) ([MCOL-5386](https://jira.mariadb.org/browse/MCOL-5386))
* Loss of PrimProc can lead to infinite loop ([MCOL-5396](https://jira.mariadb.org/browse/MCOL-5396))
* GROUP\_CONCAT in query uses enormous amount of RAM causing OOM to kill PrimProc ([MCOL-5852](https://jira.mariadb.org/browse/MCOL-5852))
* mariadbd crashing randomly when running "SELECT calShowPartitions(" ([MCOL-5879](https://jira.mariadb.org/browse/MCOL-5879))
* SubAdapterStep::execute() MCS-2035 Fix Requested ([MCOL-5889](https://jira.mariadb.org/browse/MCOL-5889))
* primproc oversubscribes memory ([MCOL-5918](https://jira.mariadb.org/browse/MCOL-5918))
* primproc 11/SEGV - querying a view ([MCOL-5932](https://jira.mariadb.org/browse/MCOL-5932))
* Fix rollbacks in mcs cli and passing errors during broadcasting config. ([MCOL-5962](https://jira.mariadb.org/browse/MCOL-5962))

#### Related to performance

* Subselect sorting is single-threaded always ([MCOL-5316](https://jira.mariadb.org/browse/MCOL-5316))

### Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 23.10.3 is provided for:

* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)
* Ubuntu 24.04 (x86\_64, ARM64)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
