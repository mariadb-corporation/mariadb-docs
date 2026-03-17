---
description: >-
  MariaDB Enterprise Server 11.8.6-3 is a Stable (GA) maintenance release of
  MariaDB Enterprise Server 11.8, released on 2026-03-17
hidden: true
---

# Changelog for MariaDB Enterprise Server 11.8.6-3

<a href="https://mariadb.com/downloads/enterprise/enterprise-server/" class="button primary">Download</a> <a href="11.8.6-3.md" class="button secondary">Release Notes</a> <a href="changelog-11.8.6-3.md" class="button secondary">Changelog</a> <a href="whats-new-in-mariadb-enterprise-server-11.8.md" class="button secondary">Overview of Enterprise Server 11.8</a>

**Release date:** 17 Mar 2026

## Issues Fixed

* ASCII strings will be sent to client connections slightly faster. ([MDEV-21816](https://jira.mariadb.org/browse/MDEV-21816))
* This bug happens when using galera, max\_tmp\_session\_space\_usage and a transaction that uses temporary file of a size between 'binlog-cache-size' (default 32K) and 64K followed by a change user command. Can be avoided by setting max\_tmp\_session\_space\_usage=0. ([MDEV-37808](https://jira.mariadb.org/browse/MDEV-37808))
* In multi-threaded write-heavy workloads, buf\_pool.flush\_list\_mutex could become a point of contention. ([MDEV-38069](https://jira.mariadb.org/browse/MDEV-38069))
* A large number of joins in a SELECT can crash the server ([MDEV-38168](https://jira.mariadb.org/browse/MDEV-38168))
* The HashiCorp Vault key management plugin has been updated to improve availability during intermittent network or server issues. Previously, the plugin only allowed the use of cached keys if a connection timed out. This behavior has been broadened and made the default to prevent MariaDB Server interruptions.
* Expanded Error Handling: The plugin now treats common connectivity issues—such as “connection refused,” “no route to host,” and “internal server error”—the same as a timeout. This ensures the server continues to function using cached keys if the Vault server is briefly unreachable.
* Updated Defaults:  ([MDEV-38203](https://jira.mariadb.org/browse/MDEV-38203))
  * The option to use cached values during communication errors is now enabled by default.
  * The cache timeout is now defaulting to the maximum value.
* Restore of dumped databases can fail with ERROR 1100 if constraints are in place ([MDEV-38216](https://jira.mariadb.org/browse/MDEV-38216))
* The authentication plugin caching\_sha2\_password can crash on large packets ([MDEV-38365](https://jira.mariadb.org/browse/MDEV-38365))
* Spider could crash when loop detection variables were artificially manipulated. ([MDEV-38368](https://jira.mariadb.org/browse/MDEV-38368))
* malformed spatial data could've caused a crash inside InnoDB ([MDEV-38372](https://jira.mariadb.org/browse/MDEV-38372))
* Long blob prefix keys could cause a crash in galera. ([MDEV-38374](https://jira.mariadb.org/browse/MDEV-38374))
* Auth Switch with Long Password Corrupts Database Name ([MDEV-38431](https://jira.mariadb.org/browse/MDEV-38431))
* mariadb-dump --dir doesn't convert db names ([MDEV-38498](https://jira.mariadb.org/browse/MDEV-38498))
* Server crashes in setup\_returning\_fields upon 2nd execution of multi-table-styled DELETE from a view ([MDEV-38620](https://jira.mariadb.org/browse/MDEV-38620))
* Galera threads time out under heavy load ([MENT-2289](https://jira.mariadb.org/browse/MENT-2289))
* In case if the view mysql.user was created (e.g. in 10.6) with a server with an unexpected character\_set\_client or collation\_connection, e.g. utf8mb3 and utf8mb3\_general\_ci, mysql\_upgrade does not fix it to the expected latin1 and latin1\_swedish\_ci. ([MENT-2523](https://jira.mariadb.org/browse/MENT-2523))
* Wrong variable name in the configuration leads Galera to think SST/IST failed, at next restart will request a full SST ([MDEV-31517](https://jira.mariadb.org/browse/MDEV-31517))
* Server can crash when JSON\_SCHEMA\_VALID() is used ([MDEV-33640](https://jira.mariadb.org/browse/MDEV-33640))
* Sequence Fails with Galera Version 26.4.16 and later in the Presence of enabled streaming replication ([MDEV-34124](https://jira.mariadb.org/browse/MDEV-34124))
* When fields of columns defined as GENERATED ALWAYS AS are getting updated by INSERT from SELECT, the server can crash ([MDEV-34984](https://jira.mariadb.org/browse/MDEV-34984))
* Wrong warning (Errcode: 2 "No such file or directory") shown by SHOW WARNING when a partitioned table is changed with ALTER. Only "ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE" should be shown ([MDEV-35562](https://jira.mariadb.org/browse/MDEV-35562))
* On an error in CREATE TEMPORARY TABLE ... SELECT, InnoDB had internally aborted a transaction, while the server thought the transaction still existed. This caused various inconsistencies in binlog, disappeared savepoints, etc. This was fixed differently in different versions. In 10.11.16, 11.4.10, 11.8.6 the transaction is consistently and completely rolled back if CREATE TEMPORARY TABLE ... SELECT fails with an error. In 12.3.1 there is no rollback at all. ([MDEV-36787](https://jira.mariadb.org/browse/MDEV-36787))
* On IA-32 and AMD64 depending on the build options, the server could crash due to an unaligned access when sending data to a client connection. ([MDEV-37148](https://jira.mariadb.org/browse/MDEV-37148))
* A default value cannot be removed with ALTER and DROP DEFAULT default if the column is defined with NOT NULL ([MDEV-37275](https://jira.mariadb.org/browse/MDEV-37275))
* Incorrect results for INTERSECT ALL in ORACLE mode ([MDEV-37325](https://jira.mariadb.org/browse/MDEV-37325))
* When using UPDATE in a BEFORE trigger, the server can crash ([MDEV-37341](https://jira.mariadb.org/browse/MDEV-37341))
* Allow execution of multi-update/multi-delete queries within the storage engines. ([MDEV-37484](https://jira.mariadb.org/browse/MDEV-37484))
* Crash with low @@optimizer\_max\_sel\_arg\_weight and optimizer\_trace=on. ([MDEV-37510](https://jira.mariadb.org/browse/MDEV-37510))
* ed25519 client authentication plugin would fail to load for anything but mariadb client utility. This has been fixed now. ([MDEV-37527](https://jira.mariadb.org/browse/MDEV-37527))
* When innodb\_buffer\_pool\_size is not large enough to buffer all log records during crash recovery, InnoDB may fail to recover a page from the doublewrite buffer. ([MDEV-37558](https://jira.mariadb.org/browse/MDEV-37558))
* For large transactions (i.e. those whose data exceeds the binlog\_cache\_size limit and spills into tmp files), provides a general performance improvement and fixes a bug that would lead to binlog corruption where the large transaction would have its GTID written into the binary log, without any additional transaction data, if the server's --tmp-dir was full. ([MDEV-37662](https://jira.mariadb.org/browse/MDEV-37662))
* INSERT ... RETURNING exposes columns for which the user lacks SELECT privilege ([MDEV-37950](https://jira.mariadb.org/browse/MDEV-37950))
* Presence of Spider disables "external" XA commit ([MDEV-37972](https://jira.mariadb.org/browse/MDEV-37972))
* Galera cluster crashes when granting permission to non existing user after setting max\_error\_count and wsrep\_ignore\_apply\_errors to zero ([MDEV-37991](https://jira.mariadb.org/browse/MDEV-37991))
* Intermittent Replication Failure on a multi-table DELETE ([MDEV-38003](https://jira.mariadb.org/browse/MDEV-38003))
* Inconsistent results for make\_set of cast ([MDEV-38233](https://jira.mariadb.org/browse/MDEV-38233))
* wrong result with index\_merge\_sort\_intersection and rowid\_filter=on ([MDEV-38327](https://jira.mariadb.org/browse/MDEV-38327))
* Memory leak in innodb.import\_hidden\_fts\_debug ([MDEV-38391](https://jira.mariadb.org/browse/MDEV-38391))
* `SHOW FUNCTION CODE package_func` crashes on the second execution ([MDEV-38451](https://jira.mariadb.org/browse/MDEV-38451))
* Potentially incorrect result with having reference to group by item. ([MDEV-38473](https://jira.mariadb.org/browse/MDEV-38473))
* Under some circumstances, some read operations could unnecessarily wait for an InnoDB log write. ([MDEV-38589](https://jira.mariadb.org/browse/MDEV-38589))
* Unexpected `Data too long` error on subselect as a multiplication argument ([MDEV-38626](https://jira.mariadb.org/browse/MDEV-38626))
* In case if the view mysql.user was created (e.g. in 10.6) with a server with an unexpected character\_set\_client or collation\_connection, e.g. utf8mb3 and utf8mb3\_general\_ci, mysql\_upgrade does not fix it to the expected latin1 and latin1\_swedish\_ci. ([MDEV-38698](https://jira.mariadb.org/browse/MDEV-38698))
* With --encrypt-binlog=ON if a node fails to apply a writeset it will crash the whole cluster due to a bug in Galera library encryption handling. Fixed in Galera library. Concerns only Enterprise Server as only it enables Galera encryption, all versions: 10.5, 10.6, 11.4, 11.8 ([MENT-2474](https://jira.mariadb.org/browse/MENT-2474))
* JSON\_UNQUOTE returns incorrect results depending on the collation ([MDEV-14301](https://jira.mariadb.org/browse/MDEV-14301))
* An issue is fixed which could result in server hangs when a replica internally scans its mysql.gtid\_slave\_pos table contents. ([MDEV-20586](https://jira.mariadb.org/browse/MDEV-20586))
* Fixed crash in Aria when doing a sub transaction like reading an entry from the proc table. ([MDEV-23132](https://jira.mariadb.org/browse/MDEV-23132))
* CREATE OR REPLACE ... SELECT where select used functions or sys tables could crash in debug builds No problems with normal builds ([MDEV-23298](https://jira.mariadb.org/browse/MDEV-23298))
* Unexpected success and result set upon erroneous JSON\_VALUE call ([MDEV-25148](https://jira.mariadb.org/browse/MDEV-25148))
* OPTIMIZE table not replicating ([MDEV-26618](https://jira.mariadb.org/browse/MDEV-26618))
* There was a short gap when mariadb-secure-installation temporary files were potentially openable/readable by an unprivileged user. These files may contain database root password. ([MDEV-28823](https://jira.mariadb.org/browse/MDEV-28823))
* An unresolvable outer reference can cause a server to crash. ([MDEV-31632](https://jira.mariadb.org/browse/MDEV-31632))
* Server crash upon moving InnoDB table with fulltext index between databases ([MDEV-31892](https://jira.mariadb.org/browse/MDEV-31892))
* Segfault when preparing unreferenced select in recursive CTE ([MDEV-32299](https://jira.mariadb.org/browse/MDEV-32299))
* ST\_OVERLAPS returns true despite dim(originalInput1) ≠ dim(originalInput2) ([MDEV-35765](https://jira.mariadb.org/browse/MDEV-35765))
* With DEFAULT() in the WHERE clause and with nested views, the server can crash ([MDEV-36686](https://jira.mariadb.org/browse/MDEV-36686))
* function VALUE() cloned incorrectly before the fix ([MDEV-36888](https://jira.mariadb.org/browse/MDEV-36888))
* innodb\_undo\_log\_truncate=ON leads to out-of-bounds write ([MDEV-37042](https://jira.mariadb.org/browse/MDEV-37042))
* prohibited semijoin with rownum correctly process in HAVING rownum. ([MDEV-37157](https://jira.mariadb.org/browse/MDEV-37157))
* Bogus \[ERROR] InnoDB: Compressed page checksum mismatch could be reported for ROW\_FORMAT=COMPRESSED tables. ([MDEV-37306](https://jira.mariadb.org/browse/MDEV-37306))
* Allow users with non-SELECT privileges to see rows in `INFORMATION_SCHEMA.TRIGGERS` table. `ACTION_CONDITION`, `ACTION_STATEMENT` and `DEFINER` columns are `NULL` unless the user is the owner of the schema or has `TRIGGER` privilege. ([MDEV-37474](https://jira.mariadb.org/browse/MDEV-37474))
* An empty value inserted for an ENUM column if a BEFORE trigger is used ([MDEV-37481](https://jira.mariadb.org/browse/MDEV-37481))
* InnoDB could crash during a workload that is frequently rebuilding or dropping tables by executing statements such as TRUNCATE TABLE, OPTIMIZE TABLE, or DROP TABLE. ([MDEV-37755](https://jira.mariadb.org/browse/MDEV-37755))
* unexpected type changing after changing AVG to MAX ([MDEV-37888](https://jira.mariadb.org/browse/MDEV-37888))
* Crash on reading corrupted view frm file ([MDEV-37920](https://jira.mariadb.org/browse/MDEV-37920))
* The CHECK TABLE command can be executed by users with the table-level CREATE but not with a global CREATE privilege ([MDEV-37971](https://jira.mariadb.org/browse/MDEV-37971))
* sys.ps\_setup\_save does not restore SQL\_LOG\_BIN after error, causes replication discrepancy ([MDEV-37979](https://jira.mariadb.org/browse/MDEV-37979))
* If the server was killed during an operation that creates a .ibd file, such as TRUNCATE TABLE, it could fail to recover. ([MDEV-37994](https://jira.mariadb.org/browse/MDEV-37994))
* (Column) CHECK constraints can cause CREATE TABLE (SELECT) queries to fail ([MDEV-37998](https://jira.mariadb.org/browse/MDEV-37998))
* crash when reading a corrupted view frm file ([MDEV-38001](https://jira.mariadb.org/browse/MDEV-38001))
* Inconsistent behaviors when casting into time ([MDEV-38006](https://jira.mariadb.org/browse/MDEV-38006))
* If the server was killed during an operation that creates a .ibd file, such as TRUNCATE TABLE, it could fail to recover. ([MDEV-38026](https://jira.mariadb.org/browse/MDEV-38026))
* Userstat Plugin CPU\_TIME much higher than BUSY\_TIME ([MDEV-38028](https://jira.mariadb.org/browse/MDEV-38028))
* When an inplace ALTER operation is rolled back, InnoDB drops intermediate tables and their associated FTS internal tables. However, MariaBackup's DDL tracking can incorrectly report this as a backup failure. ([MDEV-38041](https://jira.mariadb.org/browse/MDEV-38041))
* Server crashes after INSERT.. ON duplicate KEY UPDATE i = DEFAULT; ([MDEV-38096](https://jira.mariadb.org/browse/MDEV-38096))
* Sever shutdown prevented by RocksDB setting rocksdb\_pause\_background\_work ([MDEV-38110](https://jira.mariadb.org/browse/MDEV-38110))
* event scheduler spams the error log ([MDEV-38124](https://jira.mariadb.org/browse/MDEV-38124))
* Secondary indexes could be corrupted for InnoDB tables that contain indexed virtual columns. ([MDEV-38140](https://jira.mariadb.org/browse/MDEV-38140))
* Poor cost calculations for index access cause bad query plans for big VARCHARs ([MDEV-38164](https://jira.mariadb.org/browse/MDEV-38164))
* On Unix-like systems, mariadb-dump --dir can fail due to access permission issue, when server and mariadb-dump run as different OS users. This can happen even if the OS users are in the same group, or mariadb-dump is ran as "root" OS user. ([MDEV-38226](https://jira.mariadb.org/browse/MDEV-38226))
* Selectivity sampling for LIKE %foo% not done when the table has no sargable conditions ([MDEV-38240](https://jira.mariadb.org/browse/MDEV-38240))
* Specially crafted packet could cause the server to crash ([MDEV-38242](https://jira.mariadb.org/browse/MDEV-38242))
* The server can hang when data-at-rest encryption is used with multiple encryption threads ([MDEV-38271](https://jira.mariadb.org/browse/MDEV-38271))
* Inconsistent results for NULLIF function ([MDEV-38283](https://jira.mariadb.org/browse/MDEV-38283))
* JSON\_SCHEMA\_VALID() crashes with a long enum ([MDEV-38356](https://jira.mariadb.org/browse/MDEV-38356))
* parsec client plugin is now compiled and packaged on Windows. ([MDEV-38360](https://jira.mariadb.org/browse/MDEV-38360))
* Clustered PK not used for Loose Index Scan optimization ([MDEV-38426](https://jira.mariadb.org/browse/MDEV-38426))
* we are trying to push aggregate into WHERE ([MDEV-38487](https://jira.mariadb.org/browse/MDEV-38487))
* An issue is fixed where GRANT EXECUTE ON PROCEDURE would fail on the master, but would still be replicated and executed successfully on the slave. ([MDEV-38506](https://jira.mariadb.org/browse/MDEV-38506))
* MariaDB sometimes reports "index is corrupted" for encrypted Aria tables, but this appears to be a false positive caused by an off-by-one check in the encryption post-read hook ([MDEV-38707](https://jira.mariadb.org/browse/MDEV-38707))
* Fix MASTER\_SSL\_VERIFY\_SERVER\_CERT not usable as an unquoted identifier, unlike other CHANGE MASTER keys ([MDEV-38194](https://jira.mariadb.org/browse/MDEV-38194))

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
