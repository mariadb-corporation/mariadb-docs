---
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.6.23-19

<a href="https://mariadb.com/downloads/enterprise/enterprise-server/" class="button primary">Download</a> <a href="10.6.23-19.md" class="button secondary">Release Notes</a> <a href="changelog-10.6.23-19.md" class="button secondary">Changelog</a> <a href="whats-new.md" class="button secondary">Overview of MariaDB Enterprise Server 10.6</a>

MariaDB Enterprise Server 10.6.23-19 is a maintenance release of [MariaDB Enterprise Server 10.6](whats-new.md). For the categorized highlights and other details of this release, see the [release notes](10.6.23-19.md).

MariaDB Enterprise Server 10.6.23-19 was released on&#x20;

## Changes <a href="#changes" id="changes"></a>

* ([MDEV-36536](https://jira.mariadb.org/browse/MDEV-36536)) Add option to not collect statistics for long char/varchars
* ([MDEV-30264](https://jira.mariadb.org/browse/MDEV-30264)) spider\_db\_mbase\_result::fetch\_row() and spider\_db\_mbase\_result::fetch\_row\_from\_result\_buffer() do the same thing
* ([MDEV-30436](https://jira.mariadb.org/browse/MDEV-30436)) some sts and crd functions are almost identical
* ([MENT-2368](https://jira.mariadb.org/browse/MENT-2368)) Cherry-pick MDEV-30711: Crash in add\_keyuses\_for\_splitting(): into 10.6-ES, 11.4-ES
* ([MDEV-37179](https://jira.mariadb.org/browse/MDEV-37179)) Q3 2025 release merge
* ([MENT-2385](https://jira.mariadb.org/browse/MENT-2385)) Cherry-Pick MDEV-29981 to 10.6 ES
* ([MENT-2372](https://jira.mariadb.org/browse/MENT-2372)) cherry-pick the fix for MDEV-37397

## Issues Fixed <a href="#issues-fixed" id="issues-fixed"></a>

* ([MDEV-36852](https://jira.mariadb.org/browse/MDEV-36852)) Adding (with ALTER TABLE) a UNIQUE constraint that is USING HASH to a table with foreign keys could've caused the table to become corrupted.
* ([MDEV-36817](https://jira.mariadb.org/browse/MDEV-36817)) Server crashes in do\_mark\_index\_columns instead of ER\_DUP\_ENTRY on partitioned table
* ([MDEV-33675](https://jira.mariadb.org/browse/MDEV-33675)) Assertion(reclength < vreclength) in setup\_vcols\_for\_repair()
* ([MDEV-29155](https://jira.mariadb.org/browse/MDEV-29155)) CREATE OR REPLACE with self-referencing CHECK hangs forever, cannot be killed
* ([MDEV-25158](https://jira.mariadb.org/browse/MDEV-25158)) Segfault on INTERSECT ALL with UNION in Oracle mode
* ([MDEV-36143](https://jira.mariadb.org/browse/MDEV-36143)) This commit fixes a bug where Aria tables are used in (master->slave1->slave2) and a backup is taken on slave2. In this case it is possible that the replication position in the backup, stored in mysql.gtid\_slave\_pos, will be wrong. This will lead to replication errors if one is trying to use the backup as a new slave.
* ([MDEV-36017](https://jira.mariadb.org/browse/MDEV-36017)) Fatal InnoDB error: Unknown error Temp file write failure
* ([MDEV-30363](https://jira.mariadb.org/browse/MDEV-30363)) InnoDB: Failing assertion: trx->error\_state == DB\_SUCCESS in que\_run\_threads
* ([MDEV-36968](https://jira.mariadb.org/browse/MDEV-36968)) galera\_3nodes.inconsistency\_shutdown test occasionally hangs
* ([MDEV-35523](https://jira.mariadb.org/browse/MDEV-35523)) Server crashes with "WSREP: Unknown writeset version: -1"
* ([MDEV-37123](https://jira.mariadb.org/browse/MDEV-37123)) void srw\_lock\_debug::rd\_lock(): Assertion '!have\_any()' failed.
* ([MDEV-24726](https://jira.mariadb.org/browse/MDEV-24726)) Assertion on compressed varstring as key field in optimizer temporary table
* ([MDEV-36934](https://jira.mariadb.org/browse/MDEV-36934)) semi sync makes the master unresponsive when a replica is stopped
* ([MDEV-37103](https://jira.mariadb.org/browse/MDEV-37103)) InnoDB could crash when innodb\_immediate\_scrub\_data\_uncompressed=ON and innodb\_undo\_log\_truncate=ON were enabled at the same time.
* ([MDEV-21530](https://jira.mariadb.org/browse/MDEV-21530)) json\_extract crashes in Item\_func\_json\_extract::read\_json
* ([MENT-2297](https://jira.mariadb.org/browse/MENT-2297)) Inconsistency detected - create sequence
* ([MENT-2306](https://jira.mariadb.org/browse/MENT-2306)) XA transactions lead to \[ERROR] WSREP: Failed to apply write set
* ([MDEV-36465](https://jira.mariadb.org/browse/MDEV-36465)) MDEV-33813, in 10.6.22, an caused a regressing in that when a disk got full when writing to a MyISAM or Aria table the MariaDB connection would, instead of doing a retry after 60 seconds, hang until the query was killed.
* ([MDEV-36280](https://jira.mariadb.org/browse/MDEV-36280)) ALTER TABLE require ALTER privilege on sequence from DEFAULT value expression
* ([MDEV-37121](https://jira.mariadb.org/browse/MDEV-37121)) A shutdown with innodb\_fast\_shutdown=0 did not free cached change buffer pages.
* ([MDEV-36870](https://jira.mariadb.org/browse/MDEV-36870)) In certain cases privileges on sequences were too restrictive, for example, SELECT on a table might've erroneously required INSERT privilege on a sequences
* ([MDEV-36330](https://jira.mariadb.org/browse/MDEV-36330)) AUTO\_INCREMENT leads to non-serializable on results
* ([MDEV-36858](https://jira.mariadb.org/browse/MDEV-36858)) Fixed a bug in my\_qsort that affects sorting of more than 268,435,456 elements in one call. This affects anyone using a sort buffer of more than 4G.
* ([MDEV-37199](https://jira.mariadb.org/browse/MDEV-37199)) UNIQUE constraint that was USING HASH and UNIQUE constrant WITHOUT OVERLAPS could be violated under heavy load in READ COMMITTED transaction isolation mode.
* ([MDEV-36827](https://jira.mariadb.org/browse/MDEV-36827)) The mariadb-backup --backup --tables-file option did not have the documented effect.
* ([MENT-2324](https://jira.mariadb.org/browse/MENT-2324)) Cherry-pick: UNIQUE KEY USING HASH accepting duplicate records
* ([MENT-2389](https://jira.mariadb.org/browse/MENT-2389)) Sporadic Galera MTR failures on Debian 13 with OpenSSL 3.5.1
* ([MDEV-36337](https://jira.mariadb.org/browse/MDEV-36337)) runtime error: call to function (udf\_example) netaphon through pointer to incorrect function type `char *(*)(st_udf_init *, st_udf_args *, char *, unsigned long *, unsigned char *, unsigned char *)`
* ([MDEV-35009](https://jira.mariadb.org/browse/MDEV-35009)) MSAN: Initialize affected\_rows in SQL service
* ([MDEV-36627](https://jira.mariadb.org/browse/MDEV-36627)) galera.MDEV-29142: certification position less than last commited
* ([MDEV-36512](https://jira.mariadb.org/browse/MDEV-36512)) galera\_3nodes.GCF-354: certification position less than last committed
* ([MDEV-36117](https://jira.mariadb.org/browse/MDEV-36117)) MDL BF-BF conflict on UPDATE/DELETE with DROP/CREATE/ALTER with multi-level foreign key parents
* ([MDEV-36613](https://jira.mariadb.org/browse/MDEV-36613)) Incorrect undo logging for indexes on virtual columns whose index ID does not fit in 32 bits
* ([MDEV-34388](https://jira.mariadb.org/browse/MDEV-34388)) mariadb-backup segfault on 10.4.8 and 11.4.2, under Alpine 3.20, 3.21 and 3.22
* ([MDEV-36304](https://jira.mariadb.org/browse/MDEV-36304)) mariabackup.partial test fails with InnoDB: Missing FILE\_CREATE, FILE\_DELETE or FILE\_MODIFY before FILE\_CHECKPOINT
* ([MDEV-34761](https://jira.mariadb.org/browse/MDEV-34761)) Assertion 'client\_state\_.mode() == wsrep::client\_state::m\_local' failed in int wsrep::transaction::after\_statement(wsrep::unique\_lock[wsrep::mutex](wsrep::mutex)&)
* ([MENT-1524](https://jira.mariadb.org/browse/MENT-1524)) Assertion 'streaming\_context\_.rolled\_back() == false || state() == s\_must\_abort' failed in int wsrep::transaction::certify\_fragment(wsrep::unique\_lock[wsrep::mutex](wsrep::mutex)&)
* ([MDEV-22250](https://jira.mariadb.org/browse/MDEV-22250)) InnoDB: Failing assertion: opt\_no\_lock during mariabackup --backup ... (new)
* ([MDEV-36622](https://jira.mariadb.org/browse/MDEV-36622)) Hang during galera\_evs\_suspect\_timeout test
* ([MDEV-36123](https://jira.mariadb.org/browse/MDEV-36123)) WSREP: MDL BF-BF conflict
* ([MDEV-36628](https://jira.mariadb.org/browse/MDEV-36628)) galera\_vote\_during\_ist test failed
* ([MDEV-36740](https://jira.mariadb.org/browse/MDEV-36740)) galera.galera\_ssl\_upgrade fails due to expired certificate
* ([MENT-2315](https://jira.mariadb.org/browse/MENT-2315)) Memory leak during galera\_xa\_replay\_commit
* ([MENT-2313](https://jira.mariadb.org/browse/MENT-2313)) Memory leak reported when running Galera tests
* ([MENT-1702](https://jira.mariadb.org/browse/MENT-1702)) galera.galera\_nbo\_sst\_slave fails in Jenkins \[nearly] deterministically
* ([MDEV-36328](https://jira.mariadb.org/browse/MDEV-36328)) MSAN: use-of-uninitialized-value in ha\_innobase::records\_in\_range
* ([MDEV-36893](https://jira.mariadb.org/browse/MDEV-36893)) MSAN: THD::reset\_sub\_statement\_state swaps with uninitialized structure
* ([MDEV-36894](https://jira.mariadb.org/browse/MDEV-36894)) MemorySanitizer: use-of-uninitialized-value JSNX::ParseJpath (Connect)
* ([MDEV-36316](https://jira.mariadb.org/browse/MDEV-36316)) Debug MSAN error on InnoDB Bootstrap
* ([MDEV-36327](https://jira.mariadb.org/browse/MDEV-36327)) MSAN use-of-uninitialized-value in i\_s\_sys\_columns\_fill\_table
* ([MDEV-36848](https://jira.mariadb.org/browse/MDEV-36848)) identify tests for not\_msan.inc that could be not\_msan\_big.inc
* ([MDEV-36729](https://jira.mariadb.org/browse/MDEV-36729)) Undefined behaviour: ha\_example plugin show\_func\_example via show\_status\_array for SHOW\_SIMPLE\_FUNC has wrong function defination
* ([MDEV-36882](https://jira.mariadb.org/browse/MDEV-36882)) Inconsistent DBUG\_ASSERT makes GCC 14.2 -Og fail with -Warray-bounds
* ([MDEV-19479](https://jira.mariadb.org/browse/MDEV-19479)) Privileges not applied correctly for sequences when altering a column to take a default value from a sequence
* ([MDEV-35863](https://jira.mariadb.org/browse/MDEV-35863)) innodb.doublewrite\_debug test case fails to start the server
* ([MDEV-36482](https://jira.mariadb.org/browse/MDEV-36482)) Some MemorySanitizer instrumentation was added to aio\_linux::getevent\_thread\_routine().
* ([MDEV-36953](https://jira.mariadb.org/browse/MDEV-36953)) mysql-wsrep#198 test hangs
* ([MDEV-37048](https://jira.mariadb.org/browse/MDEV-37048)) revert MSAN my\_vsnprintf\_ex for double workaround
* ([MDEV-37183](https://jira.mariadb.org/browse/MDEV-37183)) innodb\_immediate\_scrub\_data\_uncompressed=ON may break crash recovery
* ([MDEV-37215](https://jira.mariadb.org/browse/MDEV-37215)) Server crashes upon SELECT .. FOR UPDATE under SERIALIZABLE
* ([MDEV-37203](https://jira.mariadb.org/browse/MDEV-37203)) UBSAN: applying zero offset to null pointer in strings/ctype-uca.inl | my\_uca\_strnncollsp\_onelevel\_utf8mb4 | handler::check\_duplicate\_long\_entries\_update
* ([MDEV-37302](https://jira.mariadb.org/browse/MDEV-37302)) Assertion failure in Table\_triggers\_list::add\_tables\_and\_routines\_for\_triggers upon attempt to insert DEFAULT into non-insertable view
* ([MDEV-37137](https://jira.mariadb.org/browse/MDEV-37137)) release notes from outside MDEV tasks
* ([MDEV-36984](https://jira.mariadb.org/browse/MDEV-36984)) Galera package should use systemd in Fedora
* ([MENT-2378](https://jira.mariadb.org/browse/MENT-2378)) galera\_toi\_ddl\_nonconflicting test failed
* ([MDEV-35108](https://jira.mariadb.org/browse/MDEV-35108)) The galera RPM wasn't buildable on Fedora 41 or later because of changes rpmbuild. The build script has been changed to be compatible with newer rpmbuild behaviour.
* ([MDEV-32368](https://jira.mariadb.org/browse/MDEV-32368)) MariaDB Docker Official Images for the UBI containers have the FIPS openssl module from Red Hat enabled.
* ([MDEV-29157](https://jira.mariadb.org/browse/MDEV-29157)) SELECT using ror\_merged (multi-index) scan could fail with s3 tables with error "Out of memory".
* ([MDEV-32907](https://jira.mariadb.org/browse/MDEV-32907)) spider incorrectly translates sum() query to a column

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
