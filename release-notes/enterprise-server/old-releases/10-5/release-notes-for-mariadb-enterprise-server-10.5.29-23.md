# Release Notes for MariaDB Enterprise Server 10.5.29-23

MariaDB Enterprise Server 10.5.29-23 is a maintenance release of [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/) 10.5. This release includes a variety of fixes.

MariaDB Enterprise Server 10.5.29-23 was released on 11 Jun 2025.

## Fixed Security Vulnerabilities <a href="#fixed-security-vulnerabilities" id="fixed-security-vulnerabilities"></a>

| **CVE (with** [**cve.org**](https://cve.org/) **link)**                        | **CVSS base score** |
| ------------------------------------------------------------------------------ | ------------------- |
| [CVE-2025-30693](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30693) | 5.5                 |
| [CVE-2023-52969](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52969) | 4.9                 |
| [CVE-2023-52970](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52970) | 4.9                 |

## Changes in Storage Engines <a href="#changes-in-storage-engines" id="changes-in-storage-engines"></a>

* This release incorporates MariaDB ColumnStore engine version 5.6.9.

## Notable changes <a href="#notable-changes" id="notable-changes"></a>

* MariaDB effectively running as root CAP\_DAC\_OVERRIDE ([MDEV-36229](https://jira.mariadb.org/browse/MDEV-36229))
* my\_getopt compares option names case sensitively ([MDEV-27126](https://jira.mariadb.org/browse/MDEV-27126))
* [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) updated to [26.4.22](../../../galera-cluster/26.4/26.4.22.md)

## Issues Fixed <a href="#issues-fixed" id="issues-fixed"></a>

### Can result in data loss <a href="#can-result-in-data-loss" id="can-result-in-data-loss"></a>

* Assertion InnoDB searching row in wrong partition for multiple system versioned DELETE with same timestamp and same multistatement transaction ([MDEV-36115](https://jira.mariadb.org/browse/MDEV-36115))

### Can result in hang or crash <a href="#can-result-in-hang-or-crash" id="can-result-in-hang-or-crash"></a>

* ALTER TABLE…SEQUENCE does not work correctly with InnoDB ([MDEV-36038](https://jira.mariadb.org/browse/MDEV-36038))
* Server aborts while deleting the record in spatial index ([MDEV-35420](https://jira.mariadb.org/browse/MDEV-35420))
* Upgrades fail on Windows ([MDEV-36128](https://jira.mariadb.org/browse/MDEV-36128))
* Field pointer may be uninitialized in fill\_record ([MDEV-36181](https://jira.mariadb.org/browse/MDEV-36181))
* Incorrect undo logging for indexes on virtual columns whose index ID does not fit in 32 bits ([MDEV-36613](https://jira.mariadb.org/browse/MDEV-36613))
* With wsrep\_ignore\_apply\_errors = 0, the node crashes due to assertion thd->is\_error() failed in Sql\_cmd\_dml::prepare(), shown in the logs ([MDEV-35946](https://jira.mariadb.org/browse/MDEV-35946))
* In some cases, if there are MDL locks (for example, when LOCK TABLE is executed), a node could get stuck in the system thread due to incorrect handling of metadata locks (MDL) in server code when a transaction was BF aborted. ([MDEV-35941](https://jira.mariadb.org/browse/MDEV-35941))
* Regression after the fix for [MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413) - sometimes the server crashes with an assertion in wsrep::transaction::before\_rollback(), for example when using OPTIMIZE TABLE on an ARIA table with wsrep\_osu\_method=RSU. ([MDEV-32631](https://jira.mariadb.org/browse/MDEV-32631))
* SST failure occurs when gtid\_strict\_mode is enabled under high load, such as OLTP load is active on the primary node. A typical symptom of this error is the presence of the diagnostic "\[ERROR] mariadbd: Error writing file 'binlog'", in the debug version it is also possible to crash on assertion in the wsrep::transaction::before\_rollback() function with the message "Assertion \`state() == s\_executing || state() == s\_preparing || state() == s\_prepared || state() == s\_must\_abort || state() == s\_aborting || state() == s\_cert\_failed || state() == s\_must\_replay' failed". ([MDEV-34891](https://jira.mariadb.org/browse/MDEV-34891))
* In Galera, creating sequence with a small cache leads to signal 6 error: \[ERROR] WSREP: FSM: no such a transition REPLICATING -> COMMITTED. ([MDEV-33850](https://jira.mariadb.org/browse/MDEV-33850))
* Under high load wsrep internal thread may terminate due to memory pressure conditions, but this is not a crash, however in debug version user may encounter assertion in wsrep\_to\_isolation\_begin() function with following message: "int wsrep\_to\_isolation\_begin(THD\*, const char\*, const char\*, const TABLE\_LIST\*, const Alter\_info\*, const key\_array\*, const HA\_CREATE\_INFO\*): Assertion \`(0)' failed." ([MDEV-36116](https://jira.mariadb.org/browse/MDEV-36116))
* Assertion \`commit\_trx' failed in innobase\_commit() (ha\_innodb.cc). An INSERT with sql\_log\_bin=0 is still replicated in Galera (per [MDEV-7205](https://jira.mariadb.org/browse/MDEV-7205)), despite binary logging being disabled. This results in a partial binlog bypass, requiring a two-phase commit (2PC). During 2PC, the INSERT is first prepared (entering the PREPARED state in InnoDB), and on commit, the new assertion from [MDEV-24035](https://jira.mariadb.org/browse/MDEV-24035) fails, causing a crash with "Assertion 'commit\_trx' failed" in logs. ([MDEV-35658](https://jira.mariadb.org/browse/MDEV-35658))
* When a sequence is used and inserts run in parallel on multiple Galera nodes, a transaction may be aborted after passing certification. If it then attempts to roll back, the binlog statement cache—which includes reserved sequence values—may be written prematurely. This causes a crash with the diagnostic "WSREP: FSM: no such a transition REPLICATING -> COMMITTED" in the logs, as the transaction is supposed to replay and only write to the binlog during the final commit. ([MDEV-33589](https://jira.mariadb.org/browse/MDEV-33589))
* corruption when query cache cannot allocate block ([MDEV-34075](https://jira.mariadb.org/browse/MDEV-34075))
* Stack looping and SIGSEGV in Item\_args::walk\_args on UPDATE ([MDEV-31647](https://jira.mariadb.org/browse/MDEV-31647))
* Server crash in find\_field\_in\_tables, Assertion \`name' failed in find\_field\_in\_table\_ref ([MDEV-25012](https://jira.mariadb.org/browse/MDEV-25012))
* Long server\_audit\_file\_path causes buffer overflow ([MDEV-36245](https://jira.mariadb.org/browse/MDEV-36245))
* Server crash when inserting from derived table containing insert target table ([MDEV-32086](https://jira.mariadb.org/browse/MDEV-32086))

### Can result in unexpected behaviour <a href="#can-result-in-unexpected-behaviour" id="can-result-in-unexpected-behaviour"></a>

* Segfault on concurrent ALTER and SELECT for partitioned table ([MDEV-31122](https://jira.mariadb.org/browse/MDEV-31122))
* ST\_PointFromWKB ignores SRID argument and always creates the POINT with 0 for it's SRID ([MDEV-32619](https://jira.mariadb.org/browse/MDEV-32619))
* mariadb-dump used wrong quoting character ([MDEV-36268](https://jira.mariadb.org/browse/MDEV-36268))
* After a corrupted table on one node triggers the cluster to vote to evict a node that failed a transaction, the current master can’t commit any more and hangs. ([MDEV-34998](https://jira.mariadb.org/browse/MDEV-34998), MENT-2081)
* [MDEV-32157](https://jira.mariadb.org/browse/MDEV-32157) intended to fix spider wrapper so that it is case insensitive, among other things. However that fix was incomplete, as the udf spider\_direct\_sql may still require case sensitivity. [MDEV-35807](https://jira.mariadb.org/browse/MDEV-35807) fixes this. ([MDEV-35807](https://jira.mariadb.org/browse/MDEV-35807))
* Creating partitioned tables is disallowed when wsrep\_osu\_method=TOI and wsrep\_strict\_ddl=ON, preventing alteration or deletion of partitioned tables. ([MDEV-27861](https://jira.mariadb.org/browse/MDEV-27861))
* Attempting to create a CONNECT engine table results in "non-InnoDB sequences in Galera cluster" error message in logs due to an incorrect engine check. ([MDEV-35748](https://jira.mariadb.org/browse/MDEV-35748))
* MariaDB Backup returns with an error like "Error on file ./test/t1#P#p513.MYD open during \`test\`.\`t1\` table copy for partitioned MyISAM tables when running out of file handles (MENT-2089)
* User without any privileges to a sequence can read from it and modify it via column default ([MDEV-36413](https://jira.mariadb.org/browse/MDEV-36413))
* User has unauthorized access to a sequence through a view with security invoker ([MDEV-36380](https://jira.mariadb.org/browse/MDEV-36380))

### Unexpected results <a href="#unexpected-results" id="unexpected-results"></a>

* The untested ha\_spider::index\_first\_internal constructs broken queries ([MDEV-36324](https://jira.mariadb.org/browse/MDEV-36324))
* Wrong results from tables with a single record and an aggregate ([MDEV-35238](https://jira.mariadb.org/browse/MDEV-35238))
* Unexpected error 1264 'Out of Range Value for Column' when inserting into ... select ... from a spider table ([MDEV-35874](https://jira.mariadb.org/browse/MDEV-35874))
* group by handler missing constant fields when selecting from a view ([MDEV-36307](https://jira.mariadb.org/browse/MDEV-36307))
* Tests calling the udf spider\_copy\_tables fail with --view-protocol ([MDEV-36335](https://jira.mariadb.org/browse/MDEV-36335))

## Changelog <a href="#changelog" id="changelog"></a>

For the complete list of changes in this release, see the [changelog](changelog-for-mariadb-enterprise-server-10.5.29-23.md).

## Platforms <a href="#platforms" id="platforms"></a>

In alignment to the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.5.28-22 is provided for:

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Red Hat UBI 8 (x86\_64, ARM64)
  * Red Hat UBI 8 is part of the Enterprise Server Docker Image. It does not support MariaDB Enterprise Cluster (Galera) or MariaDB ColumnStore.

Some components of MariaDB Enterprise Server are supported on a subset of platforms. See [MariaDB Engineering Policies](https://mariadb.com/engineering-policies) for details.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
