# Release Notes for MariaDB Enterprise Server 10.3.32-14

MariaDB Enterprise Server 10.3.32-14 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3. This release includes a variety of fixes.

MariaDB Enterprise Server 10.3.32-14 was released on 2021-12-13.

## Fixed Security Vulnerabilities

| CVE (with \[cve.org] link)                                                      | CVSS base score |
| ------------------------------------------------------------------------------- | --------------- |
| [CVE-2022-27385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27385) | 7.5             |
| [CVE-2021-46667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46667) | 7.5             |
| [CVE-2022-31624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31624) | 6.5             |
| [CVE-2021-46662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46662) | 5.5             |
| [CVE-2021-35604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35604) | 5.5             |

## Notable Changes

* Galera updated to 25.3.35
* [Enterprise Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) no longer enables pushdown of UDFs and Stored Functions to the Data Node by default: ([MDEV-26545](https://jira.mariadb.org/browse/MDEV-26545))
  * The default value of [spider\_use\_pushdown\_udf](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables#spider_use_pushdown_udf) has changed from `-1` to `0`
  * In previous releases, Enterprise Spider pushed UDFs and Stored Functions down to the Data Node by default, which could cause query results to be inconsistent.
  * Starting with this release, all UDFs and stored functions are evaluated on the Spider Node by default. If desired, pushdown of UDFs and Stored Functions can be explicitly enabled by setting `spider_use_pushdown_udf=1`. Testing is recommended to confirm that query results are consistent.
* [Performance Schema tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) provide descriptions of each column in the COMMENT column option. ([MDEV-25325](https://jira.mariadb.org/browse/MDEV-25325))

## Issues Fixed

### Can result in a hang or crash

* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md), powered by Galera, can crash on [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) if the table does not have a primary key and if the data for a field exceeds 4096 bytes. ([MDEV-24978](https://jira.mariadb.org/browse/MDEV-24978))
* When an InnoDB tablespace (.ibd) file is imported using [ALTER TABLE .. IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) without a corresponding `.cfg``file, InnoDB causes a server crash. ([MDEV-26131](https://jira.mariadb.org/browse/MDEV-26131), [MDEV-20931](https://jira.mariadb.org/browse/MDEV-20931))`
* When [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table) (or [mariadb-check -o](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/table-tools/mariadb-check)) is executed against an InnoDB table with a `FULLTEXT` index, InnoDB can cause a server crash. ([MDEV-25702](https://jira.mariadb.org/browse/MDEV-25702), MENT-1198)
* Resolving aggregate functions that are used in a view can cause in a crash. ([MDEV-24454](https://jira.mariadb.org/browse/MDEV-24454))
* Executing [CREATE OR REPLACE TABLE AS SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) under [LOCK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/lock-tables) can cause in a crash. ([MDEV-23391](https://jira.mariadb.org/browse/MDEV-23391))
* If two InnoDB tables have a [foreign key](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys) and an operation cascades from the parent table to the child table, an index on a virtual generated column in the child table can become corrupt. ([MDEV-26866](https://jira.mariadb.org/browse/MDEV-26866))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md), powered by Galera, crashes with errors like: \[ERROR] WSREP: Trx 236236 tries to abort slave trx 236238 ([MDEV-25835](https://jira.mariadb.org/browse/MDEV-25835))
* Server crashes when a table uses a sequence as a column default `(DEFAULT NEXT_VALUE(my_seq))` and the table is used concurrently by both a prepared statement and a normal statement. ([MDEV-22785](https://jira.mariadb.org/browse/MDEV-22785))
* MariaDB Enterprise Cluster can crash due to an incorrect conflict resolution on multi-master setup. ([MDEV-25992](https://jira.mariadb.org/browse/MDEV-25992), [MDEV-25114](https://jira.mariadb.org/browse/MDEV-25114))

### Can result in unexpected behavior

* [skip\_networking](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#skip_networking) does not prevent replication. ([MDEV-24969](https://jira.mariadb.org/browse/MDEV-24969))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) joiner node incorrectly uses `localhost` for TLS certificate verification and fails to join cluster when [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) and `encrypt=3` are configured. ([MDEV-26360](https://jira.mariadb.org/browse/MDEV-26360))
* [mariadb --binary-mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/binary) is not able to replay some [mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) outputs if `0` is in the data. ([MDEV-25444](https://jira.mariadb.org/browse/MDEV-25444))
* Memory leak with row-based replication can lead to high memory usage on replica servers. ([MDEV-26712](https://jira.mariadb.org/browse/MDEV-26712))
* [SHOW CREATE VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-view) and [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) generate invalid SQL for some complex views. ([MDEV-26299](https://jira.mariadb.org/browse/MDEV-26299))
* When statement-based or mixed replication is used and a DML statement encounters an error in a transaction that creates or drops a temporary table, non-committed writes to transactional tables can be incorrectly replicated to replica servers. ([MDEV-26833](https://jira.mariadb.org/browse/MDEV-26833))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) joiner node fails to join cluster when [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) and [Backward Compatible SST TLS Mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables) is configured. ([MDEV-26211](https://jira.mariadb.org/browse/MDEV-26211))
* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) does not work correctly for UDF and stored functions if used in a query's `WHERE` conditions. ([MDEV-26545](https://jira.mariadb.org/browse/MDEV-26545))
* On a partitioned [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) table, result of [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) wrongly depends on the partition targeted by the previous `SELECT` ([MDEV-26333](https://jira.mariadb.org/browse/MDEV-26333))
* If an `INVISIBLE` column has a computed default value, an [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) statement that doesn't specify a value for the column causes the default value to be ignored. ([MDEV-25891](https://jira.mariadb.org/browse/MDEV-25891))

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.3.34-15 is provided for:

* CentOS 7 (x86\_64)
* CentOS 8 (x86\_64, ARM64)
* Debian 9 (x86\_64, ARM64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 18.04 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
