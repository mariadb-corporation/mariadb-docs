---
description: >-
  MariaDB Enterprise Server 11.6.24-20 is a Stable (GA) maintenance release of
  MariaDB Enterprise Server 10.6, released on
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.6.24-20

{% include "../../.gitbook/includes/unreleased-es-10.6.md" %}

<a href="https://mariadb.com/downloads/enterprise/enterprise-server/" class="button primary">Download</a> <a href="10.6.24-20.md" class="button secondary">Release Notes</a> <a href="changelog-10.6.24-20.md" class="button secondary">Changelog</a> <a href="whats-new.md" class="button secondary">Overview of MariaDB Enterprise Server 10.6</a>

MariaDB Enterprise Server 10.6.24-20 is a Stable (GA) maintenance release of [MariaDB Enterprise Server 10.6](whats-new.md). For the categorized highlights and other details of this release, see the [release notes](10.6.24-20.md).

**Release date:**&#x20;

## Changes

* Backport MDEV-9804 "Implement a caching\_sha2\_password plugin" for MariaDB Enterprise Server 10.6 ([MENT-2480](https://jira.mariadb.org/browse/MENT-2480))
* Two new fields are available via SHOW REPLICA STATUS:
  * Connects\_Tried, which provides the number of attempts the replica has made to connect to the primary, and
  * Master\_Retry\_Count, which provides the number of times the replica will attempt to connect to a primary before giving up. ([MENT-2129](https://jira.mariadb.org/browse/MENT-2129))
* Add the server option `--replicate-rewrite-db` to system variables and SHOW REPLICA STATUS (backport of MDEV-15530) ([MENT-2421](https://jira.mariadb.org/browse/MENT-2421))
* Spider dev documentation ([MDEV-30265](https://jira.mariadb.org/browse/MDEV-30265))

## Issues Fixed

* InnoDB could potentially crash if there is any lock conflict on an internal FTS\_%\_CONFIG table of a FULLTEXT INDEX while one of the INFORMATION\_SCHEMA views INNODB\_TRX, INNODB\_LOCKS, or INNODB\_LOCK\_WAITS are being accessed. ([MDEV-36545](https://jira.mariadb.org/browse/MDEV-36545))
* Inconsistency detected - create sequence ([MDEV-37366](https://jira.mariadb.org/browse/MDEV-37366))
* InnoDB could crash during the crash recovery of a corrupted database. ([MDEV-37412](https://jira.mariadb.org/browse/MDEV-37412))
* Galera-26.4.24 fails buid package due to galera\_check timeout on some s390x platforms ([MDEV-37691](https://jira.mariadb.org/browse/MDEV-37691))
* Merge applicable changes from InnoDB 8.4.7 ([MDEV-37922](https://jira.mariadb.org/browse/MDEV-37922))
* very long query cannot be killed quickly ([MDEV-37938](https://jira.mariadb.org/browse/MDEV-37938))
* Item\_func\_hex doesn't check for max\_allowed\_packet ([MDEV-37947](https://jira.mariadb.org/browse/MDEV-37947))
* MDL conflict between XA and DDL in Galera cluster ([MENT-2405](https://jira.mariadb.org/browse/MENT-2405))
* Cherry Pick MDEV-37541 - Race of rolling back and committing transaction to binlog ([MENT-2448](https://jira.mariadb.org/browse/MENT-2448))
* For large transactions (i.e. those whose data exceeds the binlog\_cache\_size limit and spills into tmp files), provides a general performance improvement and fixes a bug that would lead to binlog corruption where the large transaction would have its GTID written into the binary log, without any additional transaction data, if the server's --tmp-dir was full. ([MENT-2451](https://jira.mariadb.org/browse/MENT-2451))
* Cherry-Pick MDEV-37138 "innochecksum misinterprets doublewrite buffer pages" ([MENT-2459](https://jira.mariadb.org/browse/MENT-2459))
* Backport fix for MDEV-36860 to ES 10.6 ([MENT-2463](https://jira.mariadb.org/browse/MENT-2463))
* Backport the fix for MDEV-34744 to Enterprise Server 10.6 ([MENT-2465](https://jira.mariadb.org/browse/MENT-2465))
* Assertion \`table\_share->tmp\_table != NO\_TMP\_TABLE || m\_lock\_type == 1' failed upon REBUILD PARTITION ([MDEV-20498](https://jira.mariadb.org/browse/MDEV-20498))
* Spider: Assertion \`inited==RND' failed in handler::ha\_rnd\_end on DELETE ([MDEV-26540](https://jira.mariadb.org/browse/MDEV-26540))
* Several bugs in SPATIAL INDEX page splitting logic could crash InnoDB if the PRIMARY KEY or the SPATIAL data is variable-length. ([MDEV-27675](https://jira.mariadb.org/browse/MDEV-27675))
* Tested on 10.6.24, the issue is not reproducible anymore. ([MDEV-30456](https://jira.mariadb.org/browse/MDEV-30456))
* InnoDB could crash if the definition of the InnoDB persistent statistics tables were incorrect. ([MDEV-31740](https://jira.mariadb.org/browse/MDEV-31740))
* SIGSEGV in maria\_rtree\_split\_page | maria\_rtree\_add\_key ([MDEV-31766](https://jira.mariadb.org/browse/MDEV-31766))
* Server crash on cleanup of non-fully-constructed-due-to-an-error CTE ([MDEV-32308](https://jira.mariadb.org/browse/MDEV-32308))
* Mariadb server crashed during insert ([MDEV-36134](https://jira.mariadb.org/browse/MDEV-36134))
* Fix for unstable mtr test ([MDEV-36949](https://jira.mariadb.org/browse/MDEV-36949))
* Fixed crashing bug when inserting into a tables with several nextval(sequence) default values. ([MDEV-37172](https://jira.mariadb.org/browse/MDEV-37172))
* The minimum value of the parameter innodb\_ft\_min\_token\_size was increased to 1, similar to the parameter ft\_min\_word\_len. ([MDEV-37423](https://jira.mariadb.org/browse/MDEV-37423))
* Parallel slave worker crashes During Backup at retrying ([MDEV-37453](https://jira.mariadb.org/browse/MDEV-37453))
* decimal\_digits\_t trips GCC -Wconversion ([MDEV-37477](https://jira.mariadb.org/browse/MDEV-37477))
* `mariadb-dump -T` did not encode table names like the server did for `frm` files, so some tables can be created in the server, but not dumped with `mariadb-dump -T`, for example, a table `con` on Windows. ([MDEV-37483](https://jira.mariadb.org/browse/MDEV-37483))
* The parameter innodb\_trx\_rseg\_n\_slots\_debug was removed. ([MDEV-37672](https://jira.mariadb.org/browse/MDEV-37672))
* Most of server Audit v2 tests are disabled and never run ([MENT-1223](https://jira.mariadb.org/browse/MENT-1223))
* The HashiCorp Key Management Plugin has been updated to provide robust stability against Vault communication failures ([MENT-1582](https://jira.mariadb.org/browse/MENT-1582))
  * The plugin is now configured to use cached keys for all communication errors (not just timeouts), ensuring continuous operation when the Vault server is temporarily unreachable.
  * The default setting for using the cache on errors is now ON.
  * The default key cache timeout (hashicorp\_key\_management\_cache\_timeout) has been increased to its maximum practical value (e.g., one year in milliseconds), maximizing key availability in the cache during extended service interruptions.&#x20;
* InnoDB partition table disallow local GTIDs ([MENT-2367](https://jira.mariadb.org/browse/MENT-2367))
* Wrong hardcoded default for GIT\_REMOTE\_ORIGIN\_URL in ES ([MENT-2393](https://jira.mariadb.org/browse/MENT-2393))
* With --encrypt-binlog=ON if a node fails to apply a writeset it will crash the whole cluster due to a bug in Galera library encryption handling. Fixed in Galera library. Concerns only Enterprise Server as only it enables Galera encryption, all versions: 10.5, 10.6, 11.4, 11.8 ([MENT-2474](https://jira.mariadb.org/browse/MENT-2474))
* A misplaced debug assertion could fail due to a race condition. In MariaDB Server 11.8.1, this bug had already been fixed as part of MDEV-35049. ([MDEV-20203](https://jira.mariadb.org/browse/MDEV-20203))
* \#2 Assertion \`binlog\_table\_maps == 0 || locked\_tables\_mode == LTM\_LOCK\_TABLES' failed in THD::reset\_for\_next\_command ([MDEV-22915](https://jira.mariadb.org/browse/MDEV-22915))
* InnoDB could crash after a DROP TABLE, TRUNCATE TABLE, OPTIMIZE TABLE or a table-rebuilding ALTER TABLE if innodb\_adaptive\_hash\_index entries existed in the table. ([MDEV-26599](https://jira.mariadb.org/browse/MDEV-26599))
* Server hang with innodb\_file\_per\_table=0, innodb\_undo\_tablespaces=0 ([MDEV-29930](https://jira.mariadb.org/browse/MDEV-29930))
* Wrong results for self-touching shapes. ([MDEV-31499](https://jira.mariadb.org/browse/MDEV-31499))
* Assertion \`marked\_for\_read()' fails on slave upon RBR with binlog\_row\_image=MINIMAL ([MDEV-31678](https://jira.mariadb.org/browse/MDEV-31678))
* Replicated REPAIR TABLE writes an error in the log when normal REPAIR does not ([MDEV-33184](https://jira.mariadb.org/browse/MDEV-33184))
* Recovery of Aria transactional tables did not work in big-endian machines like s390x and Sparc ([MDEV-34914](https://jira.mariadb.org/browse/MDEV-34914))
* ALTER TABLE could fail to update InnoDB persistent statistics. ([MDEV-35163](https://jira.mariadb.org/browse/MDEV-35163))
* UBSAN: runtime error: load of value 1341112147, which is not a valid value for type 'enum enum\_schema\_tables' in optimize\_for\_get\_all\_tables and get\_all\_tables and on SELECT from I\_S geometry\_columns ([MDEV-35713](https://jira.mariadb.org/browse/MDEV-35713))
* only mtr test has been fixed ([MDEV-36710](https://jira.mariadb.org/browse/MDEV-36710))
* ALTER TABLE tbl\_a ADD PARTITION (PARTITION pt2) MSAN uninitalized read ([MDEV-36723](https://jira.mariadb.org/browse/MDEV-36723))
* galera.galera\_sst\_encrypted LeakSanitizer: detected memory leaks ([MDEV-37206](https://jira.mariadb.org/browse/MDEV-37206))
* SIGSEGV in srv\_printf\_innodb\_monitor ([MDEV-37360](https://jira.mariadb.org/browse/MDEV-37360))
* It appears that some error conditions don't store error information in the Diagnostics\_area.
  * For example when table\_def::compatible\_with() check fails error message is stored in Relay\_log\_info instead.
  * This results in optimistically identical votes and zero error buffer size breaks wsrep-lib logic as it relies on error buffer size to decide whether voting took place.
  * To account for this, first try to obtain error info from Relay\_log\_info, then fallback to Diagnostics\_area. If that fails use some random data to distinguish this condition from success.
  * This requires bumping of the application protocol to 8 since vote message generation algorithm has changed. ([MDEV-37494](https://jira.mariadb.org/browse/MDEV-37494))
* myisamchk -V crashes ([MDEV-37505](https://jira.mariadb.org/browse/MDEV-37505))
* UBSAN: nullptr-with-nonzero-offset/pointer-overflow in row\_log\_apply\_ops ([MDEV-37626](https://jira.mariadb.org/browse/MDEV-37626))
* CHECK TABLE…EXTENDED could flag bogus corruption on a column prefix index. ([MDEV-37659](https://jira.mariadb.org/browse/MDEV-37659))
* During workload after crash recovery, an incorrect (too large) innodb\_buffer\_pool\_pages\_dirty could be reported. ([MDEV-37677](https://jira.mariadb.org/browse/MDEV-37677))
* Lock checks for secondary indexes were unnecessarily accessing some history and could access freed BLOB pages that correspond to column prefixes. ([MDEV-37753](https://jira.mariadb.org/browse/MDEV-37753))
* Backport "Systemd: Restart on OOM" fix to 10.6 ([MDEV-37780](https://jira.mariadb.org/browse/MDEV-37780))
* Spider: XA COMMIT ONE PHASE fails with "This xid does not exist" ([MDEV-37829](https://jira.mariadb.org/browse/MDEV-37829))
* Fixed a problem where the server would crash with a segfault when trying to drop duplicate domain ids in the same command, e.g.
* FLUSH BINARY LOGS DELETE\_DOMAIN\_ID=(0), BINARY LOGS DELETE\_DOMAIN\_ID=(0) ([MDEV-37885](https://jira.mariadb.org/browse/MDEV-37885))
* Threadpool - debug assertion thread\_group->active\_thread\_count >=0, from TP\_connection\_generic::wait\_begin ([MDEV-37902](https://jira.mariadb.org/browse/MDEV-37902))
* Due to the impending EOL of Windows 10 22H2, Windows 11 23H2, this will be the last release supporting these releases.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}

