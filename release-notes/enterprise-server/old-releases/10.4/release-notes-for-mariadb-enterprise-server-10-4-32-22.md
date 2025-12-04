# Release Notes for MariaDB Enterprise Server 10.4.32-22

MariaDB Enterprise Server 10.4.32-22 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4. This release includes a variety of fixes. Users of MariaDB Enterprise Server 10.4.31-21 are encouraged to upgrade. Additional steps are required if upgrading from Enterprise Server 10.4.31-21 to 10.4.32-22.

MariaDB Enterprise Server 10.4.32-22 was released on 2023-12-12.

## Fixed Security Vulnerabilities

| CVE (with cve.org link)                                                         | CVSS base score |
| ------------------------------------------------------------------------------- | --------------- |
| [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084) | 4.9             |

## Notable changes

* CHACHA20-POLY1305 support when WolfSSL is used ([MDEV-31653](https://jira.mariadb.org/browse/MDEV-31653))
* The semi-synchronous replication magic number error "\[ERROR] Read semi-sync reply magic number error" has been improved to show the semi-sync acknowledgment reported with printing the hex-dump of the failing network packet ([MDEV-32365](https://jira.mariadb.org/browse/MDEV-32365))
* Disable TLS v1.0 and 1.1 for MariaDB. TLSv1.1 removed from the default tls\_version system variable. ([MDEV-31369](https://jira.mariadb.org/browse/MDEV-31369))
  * A warning is shown if TLSv1.0 or TLSv1.1 are selected.

### Can result in data loss

* With binary log enabled transactions that are filtered out of binlogging by any of binlog\_{do,ignore}\_db option may be lost in the engine. ([MDEV-29989](https://jira.mariadb.org/browse/MDEV-29989))
* DROP INDEX followed by CREATE INDEX may corrupt data ([MDEV-32132](https://jira.mariadb.org/browse/MDEV-32132))
* Assertion fails in MDL\_context::acquire\_lock upon parallel replication of CREATE SEQUENCE ([MDEV-31792](https://jira.mariadb.org/browse/MDEV-31792))

### Can result in hang or crash

* A hang or crash could be observed in parallel replication of STATEMENT binlog format transactions modifying temporary tables. E.g. witnessed in rpl.rpl\_parallel\_temptable failure. ([MDEV-10356](https://jira.mariadb.org/browse/MDEV-10356))
* A failure that occurs due to unnecessary replication of CACHE INDEX and LOAD INDEX INTO CACHE although this is a local operation. ([MDEV-24912](https://jira.mariadb.org/browse/MDEV-24912))
* Rowid filter does not process a storage engine error correctly. A query that's executing a locking read and is using the Rowid Filter could cause a server crash if it has encountered a Lock Wait Timeout or Deadlock or a similar error when building the Rowid Filter. ([MDEV-25163](https://jira.mariadb.org/browse/MDEV-25163))
* Crash when HAVING in a correlated subquery references columns in the outer query ([MDEV-29731](https://jira.mariadb.org/browse/MDEV-29731))
* Due to a flaw in the SST scripts, it was not possible to execute SST when datadir, or some innodb log directory points to a path that is actually a symlink to the actual data directory. ([MDEV-29893](https://jira.mariadb.org/browse/MDEV-29893))
* Server can crash when a table of type SPIDER starts with a comment string which is not a parameter for SPIDER. ([MDEV-31117](https://jira.mariadb.org/browse/MDEV-31117))
* Node crashes when trying to execute "CREATE TABLE ... WITH SYSTEM VERSIONING AS SELECT ..." ([MDEV-31285](https://jira.mariadb.org/browse/MDEV-31285))
* Lock wait timeout with INSERT-SELECT, autoinc, and statement-based replication ([MDEV-31482](https://jira.mariadb.org/browse/MDEV-31482))
* Too strict assertion which leads to a problem since with the BINLOG statement we can execute binlog events on master also (not only in applier). ([MDEV-31651](https://jira.mariadb.org/browse/MDEV-31651))
* Galera cannot support wsrep\_forced\_binlog\_format=\[MIXED|STATEMENT] during CREATE TABLE AS SELECT. But a crash in the form of an assertion is an overreaction. Now a warning is issued instead. ([MDEV-31660](https://jira.mariadb.org/browse/MDEV-31660))
* When using ROW\_FORMAT=COMPRESSED, the server can crash with the warning "InnoDB: 2048 bytes should have been read. Only 0 bytes read. Retrying for the remaining bytes." in the server log ([MDEV-31875](https://jira.mariadb.org/browse/MDEV-31875))
* Possible server crash when setting SPIDER option spider\_delete\_all\_rows to 0 and delete all rows of a spider table ([MDEV-31996](https://jira.mariadb.org/browse/MDEV-31996))
* Use of nested row constructs in the left expression of an IN subquery should produce an error. Example: (a,(b,c)) IN (SELECT ...). In some degenerate cases, the error was not detected, and this causes a crash at a further stage in query processing. ([MDEV-32320](https://jira.mariadb.org/browse/MDEV-32320))
* A table-less subquery with a LIMIT clause with non-zero offset, like ( SELECT two LIMIT 1 OFFSET 1) can produce unexpected results. If used inside ORDER BY, it can cause a crash. ([MDEV-32324](https://jira.mariadb.org/browse/MDEV-32324))
* Possible crash in the full-text search plugin parser when using FULLTEXT...WITH PARSER. ([MDEV-32578](https://jira.mariadb.org/browse/MDEV-32578))
* Intermittent crashes when using SEQUENCE in combination with Galera ([MDEV-32024](https://jira.mariadb.org/browse/MDEV-32024))
* When two clients execute FLUSH TABLES WITH READ LOCK/UNLOCK TABLES on a Galera node, the node would sometimes get stuck in a paused state. This can cause the next requests to fail. ([MDEV-32282](https://jira.mariadb.org/browse/MDEV-32282))
* Sometimes a node has been dropped from the cluster on startup/shutdown with async replication enabled due to inconsistency issues with the mysql.gtid\_slave\_pos table (between master and replica nodes), because previously this table was not previously replicated within the cluster. ([MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413))
* Server crashes in check\_sequence\_fields upon CREATE TABLE .. SEQUENCE=1 AS SELECT .. ([MDEV-29771](https://jira.mariadb.org/browse/MDEV-29771))
* Crash when searching for the best split of derived table ([MDEV-32064](https://jira.mariadb.org/browse/MDEV-32064))
* When a new user is connecting or a user is changing the password while FLUSH PRIVILEGES is executed, the server can crash (MENT-1707)

### Can result in unexpected behavior

* Prefix keys for CHAR return error "ERROR 1062 (23000): Duplicate entry 'ß' for key 'a'" for MyISAM and Aria when inserting data ([MDEV-30048](https://jira.mariadb.org/browse/MDEV-30048))
* Possible wrong results of DISTINCT with NOPAD collations when SET big\_tables=1; is set ([MDEV-30050](https://jira.mariadb.org/browse/MDEV-30050))
* Missed kill when the SQL thread goes to wait for parallel slave worker queues to drain. KILL query did not affect a replication thread, which remained alive unexpectedly by the user. ([MDEV-29974](https://jira.mariadb.org/browse/MDEV-29974))
* InnoDB tries to purge non-delete-marked records of an index on a virtual column prefix. An error like "InnoDB: tried to purge non-delete-marked record in index b of table test`.`t" is shown in the server log ([MDEV-30024](https://jira.mariadb.org/browse/MDEV-30024))
* lock\_row\_lock\_current\_waits counter in information\_schema.innodb\_metrics may become negative ([MDEV-30658](https://jira.mariadb.org/browse/MDEV-30658))
* SHOW REPLICA STATUS Last\_SQL\_Errno race condition on Errored replica restart. A contradictory YES of slave\_running\_status and an error code in Last\_SQL\_Errno will be shown ([MDEV-31177](https://jira.mariadb.org/browse/MDEV-31177))
* Auto-increment no longer works for explicit FTS\_DOC\_ID ([MDEV-32017](https://jira.mariadb.org/browse/MDEV-32017))
* In some cases, replaying transactions on other MariaDB Enterprise Cluster nodes results in an wrong "Failed to insert streaming client" warning ([MDEV-32051](https://jira.mariadb.org/browse/MDEV-32051))
* Wrong bit encoding using COALESCE ([MDEV-32244](https://jira.mariadb.org/browse/MDEV-32244))
* getting error 'Illegal parameter data types row and bigint for operation '+' ' when using ITERATE in a FOR..DO ([MDEV-32275](https://jira.mariadb.org/browse/MDEV-32275))
* While checking for altered column in foreign key constraints, InnoDB fails to ignore virtual columns ([MDEV-32337](https://jira.mariadb.org/browse/MDEV-32337))
* seconds\_behind\_master is inaccurate for Delayed replication ([MDEV-32265](https://jira.mariadb.org/browse/MDEV-32265))
* The wsrep\_sst\_method variable can be set to an invalid value using the SET statement. ([MDEV-31470](https://jira.mariadb.org/browse/MDEV-31470))
* Misleading help text for mysqlbinlog (mariadb-binlog) -T/--table option ([MDEV-25369](https://jira.mariadb.org/browse/MDEV-25369))
* mbstream breaks page compression on XFS ([MDEV-25734](https://jira.mariadb.org/browse/MDEV-25734))
* MyISAM tables took transactional metadata locks although there were no active transactions. ([MDEV-28820](https://jira.mariadb.org/browse/MDEV-28820))
* "rpm --setugids" breaks PAM authentication ([MDEV-30904](https://jira.mariadb.org/browse/MDEV-30904))
* A multi-row Insert into an empty table fails if the table has a unique index using hash. CHECK TABLE returns with "Table 't1' is marked as crashed and should be repaired" ([MDEV-32015](https://jira.mariadb.org/browse/MDEV-32015))
* wrong table name in InnoDB's "row too big" errors ([MDEV-32128](https://jira.mariadb.org/browse/MDEV-32128))
* Slow log Rows\_examined for the slow\_log can be out of range. In this case the server log includes "(\[ERROR] Unable to write to mysql.slow\_log)" ([MDEV-30820](https://jira.mariadb.org/browse/MDEV-30820))
* An incorrect examined rows number is used in some cases like in the slow query log, with LIMIT ROWS EXAMINED, or with ANALYZE FORMAT=JSON when a query gets executed inside of a function. Each stored function call doubles the current count during processing ([MDEV-31742](https://jira.mariadb.org/browse/MDEV-31742))

### Related to performance

* Optimize is\_file\_on\_ssd() to speedup opening tablespaces on Windows ([MDEV-32228](https://jira.mariadb.org/browse/MDEV-32228))
* Significant slowdown for query with many outer joins ([MDEV-32351](https://jira.mariadb.org/browse/MDEV-32351))
* An incorrect examined rows number is used in some cases like in the slow query log, with LIMIT ROWS EXAMINED, or with ANALYZE FORMAT=JSON when an executed query includes a stored function Each stored function call doubles the current count during processing ([MDEV-32475](https://jira.mariadb.org/browse/MDEV-32475))
* Parallel replication deadlock victim preference code erroneously removed. As a result, parallel slave could retry transaction execution more times than necessary. ([MDEV-31655](https://jira.mariadb.org/browse/MDEV-31655))

### Related to install and upgrade

* mysql\_install\_db doesn't properly grant proxy privileges to all default root user accounts ([MDEV-21194](https://jira.mariadb.org/browse/MDEV-21194))
* The second node cannot be started because Galera SST rsync wants to replicate snapshot directory when datadir is on a NetApp storage with NFS access ([MDEV-31332](https://jira.mariadb.org/browse/MDEV-31332))

## Platforms

In alignment to the enterprise lifecycle, MariaDB Enterprise Server 10.4.32-22 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server are supported on a subset of platforms. See [MariaDB Engineering Policies](https://mariadb.com/engineering-policies) for details.

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
