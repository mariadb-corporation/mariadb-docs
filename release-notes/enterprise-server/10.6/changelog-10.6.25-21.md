---
description: >-
  MariaDB Enterprise Server 10.6.25-21 is a Stable (GA) maintenance release of
  MariaDB Enterprise Server 10.6, released on 2026-03-17
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.6.25-21

<a href="https://mariadb.com/downloads/enterprise/enterprise-server/" class="button primary">Download</a> <a href="10.6.25-21.md" class="button secondary">Release Notes</a> <a href="changelog-10.6.25-21.md" class="button secondary">Changelog</a> <a href="whats-new.md" class="button secondary">Overview of Enterprise Server 10.6</a>

**Release date:** 17 Mar 2026

## Issues Fixed

* ASCII strings will be sent to client connections slightly faster. ([MDEV-21816](https://jira.mariadb.org/browse/MDEV-21816))
* When installing mysql-selinux RPM it is no longer possible to re-start Galera nodes ([MDEV-38297](https://jira.mariadb.org/browse/MDEV-38297))
* Spider could crash when loop detection variables were artificially manipulated. ([MDEV-38368](https://jira.mariadb.org/browse/MDEV-38368))
* malformed spatial data could've caused a crash inside InnoDB ([MDEV-38372](https://jira.mariadb.org/browse/MDEV-38372))
* Long blob prefix keys could cause a crash in galera. ([MDEV-38374](https://jira.mariadb.org/browse/MDEV-38374))
* Auth Switch with Long Password Corrupts Database Name ([MDEV-38431](https://jira.mariadb.org/browse/MDEV-38431))
* Galera threads time out under heavy load ([MENT-2289](https://jira.mariadb.org/browse/MENT-2289))
* A replica would crash while replicating UPDATE and DELETE DML statements that target a table which previously had a partition that was converted to a separate table via ALTER TABLE .. CONVERT PARTITION .. TO TABLE. For example, if the command looked like ALTER TABLE t1 CONVERT PARTITION p1 TO TABLE t\_new; the replica would crash when trying to update/deleterows in table t1 after running the command. ([MENT-2466](https://jira.mariadb.org/browse/MENT-2466))
* On IA-32 and AMD64 depending on the build options, the server could crash due to an unaligned access when sending data to a client connection. ([MDEV-37148](https://jira.mariadb.org/browse/MDEV-37148))
* ed25519 client authentication plugin would fail to load for anything but mariadb client utility. This has been fixed now. ([MDEV-37527](https://jira.mariadb.org/browse/MDEV-37527))
* When innodb\_buffer\_pool\_size is not large enough to buffer all log records during crash recovery, InnoDB may fail to recover a page from the doublewrite buffer. ([MDEV-37558](https://jira.mariadb.org/browse/MDEV-37558))
* INSERT ... RETURNING exposes columns for which the user lacks SELECT privilege ([MDEV-37950](https://jira.mariadb.org/browse/MDEV-37950))
* Presence of Spider disables "external" XA commit ([MDEV-37972](https://jira.mariadb.org/browse/MDEV-37972))
* Memory leak in innodb.import\_hidden\_fts\_debug ([MDEV-38391](https://jira.mariadb.org/browse/MDEV-38391))
* Fixed crash in Aria when doing a sub transaction like reading an entry from the proc table. ([MENT-2424](https://jira.mariadb.org/browse/MENT-2424))
* With --encrypt-binlog=ON if a node fails to apply a writeset it will crash the whole cluster due to a bug in Galera library encryption handling. Fixed in Galera library. Concerns only Enterprise Server as only it enables Galera encryption, all versions: 10.5, 10.6, 11.4, 11.8 ([MENT-2474](https://jira.mariadb.org/browse/MENT-2474))
* The fix is in galera library and was pushed as part of the duplicate issue MENT-2512 ([MENT-2489](https://jira.mariadb.org/browse/MENT-2489))
* Fixed crash in Aria when doing a sub transaction like reading an entry from the proc table. ([MDEV-23132](https://jira.mariadb.org/browse/MDEV-23132))
* CREATE OR REPLACE ... SELECT where select used functions or sys tables could crash in debug builds. No problems with normal builds ([MDEV-23298](https://jira.mariadb.org/browse/MDEV-23298))
* There was a short gap when mariadb-secure-installation temporary files were potentially openable/readable by an unprivileged user. These files may contain database root password. ([MDEV-28823](https://jira.mariadb.org/browse/MDEV-28823))
* Server crash upon moving InnoDB table with fulltext index between databases ([MDEV-31892](https://jira.mariadb.org/browse/MDEV-31892))
* function VALUE() cloned incorrectly before the fix ([MDEV-36888](https://jira.mariadb.org/browse/MDEV-36888))
* innodb\_undo\_log\_truncate=ON leads to out-of-bounds write ([MDEV-37042](https://jira.mariadb.org/browse/MDEV-37042))
* Bogus \[ERROR] InnoDB: Compressed page checksum mismatch could be reported for ROW\_FORMAT=COMPRESSED tables. ([MDEV-37306](https://jira.mariadb.org/browse/MDEV-37306))
* InnoDB could crash during a workload that is frequently rebuilding or dropping tables by executing statements such as TRUNCATE TABLE, OPTIMIZE TABLE, or DROP TABLE. ([MDEV-37755](https://jira.mariadb.org/browse/MDEV-37755))
* If the server was killed during an operation that creates a .ibd file, such as TRUNCATE TABLE, it could fail to recover. ([MDEV-37994](https://jira.mariadb.org/browse/MDEV-37994))
* If the server was killed during an operation that creates a .ibd file, such as TRUNCATE TABLE, it could fail to recover. ([MDEV-38026](https://jira.mariadb.org/browse/MDEV-38026))
* When an inplace ALTER operation is rolled back, InnoDB drops intermediate tables and their associated FTS internal tables. However, MariaBackup's DDL tracking can incorrectly report this as a backup failure. ([MDEV-38041](https://jira.mariadb.org/browse/MDEV-38041))
* Secondary indexes could be corrupted for InnoDB tables that contain indexed virtual columns. ([MDEV-38140](https://jira.mariadb.org/browse/MDEV-38140))
* Specially crafted packet could cause the server to crash ([MDEV-38242](https://jira.mariadb.org/browse/MDEV-38242))
* The server can hang when data-at-rest encryption is used with multiple encryption threads ([MDEV-38271](https://jira.mariadb.org/browse/MDEV-38271))
* we are trying to push aggregate into WHERE ([MDEV-38487](https://jira.mariadb.org/browse/MDEV-38487))
* SET GLOBAL innodb\_buffer\_pool\_size was prone to hang or crash the server, especially when innodb\_adaptive\_hash\_index was enabled. ([MENT-2545](https://jira.mariadb.org/browse/MENT-2545))

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
