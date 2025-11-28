# MariaDB 10.5.23 Release Notes

{% include "../../../.gitbook/includes/latest-10-5.md" %}

<a href="https://downloads.mariadb.org/mariadb/10.5.23/" class="button primary">Download</a> <a href="mariadb-10-5-23-release-notes.md" class="button secondary">Release Notes</a> <a href="../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-23-changelog.md" class="button secondary">Changelog</a> <a href="what-is-mariadb-105.md" class="button secondary">Overview of 10.5</a>

**Release date:** 13 Nov 2023

[MariaDB 10.5](what-is-mariadb-105.md) is a previous _stable_ series of MariaDB, [maintained until](https://mariadb.org/about/#maintenance-policy) June 2025. It is an evolution of [MariaDB 10.4](../release-notes-mariadb-10-4-series/what-is-mariadb-104.md) with several entirely new features not found anywhere else and with backported and reimplemented features from MySQL.

[MariaDB 10.5.23](mariadb-10-5-23-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

Thanks, and enjoy MariaDB!

## Notable Items

### InnoDB

* [DROP INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-index) followed by [CREATE INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-index) may corrupt data ([MDEV-32132](https://jira.mariadb.org/browse/MDEV-32132))
* ROW\_FORMAT=COMPRESSED table: InnoDB: 2048 bytes should have been read. Only 0 bytes read. ([MDEV-31875](https://jira.mariadb.org/browse/MDEV-31875))
* Server aborts during alter operation when table doesn't have foreign index ([MDEV-32527](https://jira.mariadb.org/browse/MDEV-32527))
* row\_merge\_fts\_doc\_tokenize() handles FTS plugin parser inconsistently ([MDEV-32578](https://jira.mariadb.org/browse/MDEV-32578))
* InnoDB: tried to purge non-delete-marked record of an index on a virtual column prefix ([MDEV-30024](https://jira.mariadb.org/browse/MDEV-30024))
* lock\_row\_lock\_current\_waits counter in information\_schema.innodb\_metrics may become negative ([MDEV-30658](https://jira.mariadb.org/browse/MDEV-30658))
* SET GLOBAL innodb\_max\_purge\_lag\_wait=… hangs if innodb\_read\_only=ON ([MDEV-31813](https://jira.mariadb.org/browse/MDEV-31813))
* Auto-increment no longer works for explicit FTS\_DOC\_ID ([MDEV-32017](https://jira.mariadb.org/browse/MDEV-32017))
* Assertion \`pos < table->n\_def' failed in dict\_table\_get\_nth\_col ([MDEV-32337](https://jira.mariadb.org/browse/MDEV-32337))
* innochecksum man pages seem to be inconsistent with the binary (10.2.25) ([MDEV-20583](https://jira.mariadb.org/browse/MDEV-20583))
* innodb\_compression\_algorithm=0 (none) increments Innodb\_num\_pages\_page\_compression\_error ([MDEV-30825](https://jira.mariadb.org/browse/MDEV-30825))
* wrong table name in innodb's "row too big" errors ([MDEV-32128](https://jira.mariadb.org/browse/MDEV-32128))
* Optimize is\_file\_on\_ssd() to speedup opening tablespaces on Windows ([MDEV-32228](https://jira.mariadb.org/browse/MDEV-32228))
* Race condition between page write completion and log checkpoint ([MDEV-32511](https://jira.mariadb.org/browse/MDEV-32511))
* After crash recovery, Checksum mismatch + Failing assertion: !i || prev\_id + 1 == space\_id, ([MDEV-31851](https://jira.mariadb.org/browse/MDEV-31851))
* Deadlock due to log\_free\_check(), involving trx\_purge\_truncate\_rseg\_history() and trx\_undo\_assign\_low() ([MDEV-32049](https://jira.mariadb.org/browse/MDEV-32049))
* Write-ahead logging is broken for freed pages ([MDEV-32552](https://jira.mariadb.org/browse/MDEV-32552))
* X-lock on supremum for prepared transaction for RR ([MDEV-30165](https://jira.mariadb.org/browse/MDEV-30165))

### Optimizer

* Crash when HAVING in a correlated subquery references columns in the outer query ([MDEV-29731](https://jira.mariadb.org/browse/MDEV-29731))
* Server crashes at TABLE::add\_tmp\_key ([MDEV-32320](https://jira.mariadb.org/browse/MDEV-32320))
* Server crashes inside filesort at my\_decimal::to\_binary ([MDEV-32324](https://jira.mariadb.org/browse/MDEV-32324))
* Assertion \`bitmap\_is\_set(\&m\_part\_info->read\_partitions, m\_part\_spec.start\_part)' failed in ha\_partition::handle\_ordered\_index\_scan ([MDEV-24283](https://jira.mariadb.org/browse/MDEV-24283))
* Crash when searching for the best split of derived table ([MDEV-32064](https://jira.mariadb.org/browse/MDEV-32064))
* Test case from opt\_tvc.test fails with statement memory protection ([MDEV-32225](https://jira.mariadb.org/browse/MDEV-32225))
* Significant slowdown for query with many outer joins ([MDEV-32351](https://jira.mariadb.org/browse/MDEV-32351))
* test\_if\_skip\_sort\_order() should catch the join types JT\_EQ\_REF, JT\_CONST and JT\_SYSTEM and skip sort order for these ([MDEV-32475](https://jira.mariadb.org/browse/MDEV-32475))

### Replication

* rpl.rpl\_parallel\_temptable failure due to incorrect commit optimization of temptables ([MDEV-10356](https://jira.mariadb.org/browse/MDEV-10356))
* Lock wait timeout with INSERT-SELECT, autoinc, and statement-based replication ([MDEV-31482](https://jira.mariadb.org/browse/MDEV-31482))
* strings/ctype-ucs2.c:2336: my\_vsnprintf\_utf32: Assertion \`(n % 4) == 0' failed in my\_vsnprintf\_utf32 on INSERT ([MDEV-32249](https://jira.mariadb.org/browse/MDEV-32249))
* Assertion fails in MDL\_context::acquire\_lock upon parallel replication of CREATE SEQUENCE ([MDEV-31792](https://jira.mariadb.org/browse/MDEV-31792))
* SHOW SLAVE STATUS Last\_SQL\_Errno Race Condition on Errored Slave Restart ([MDEV-31177](https://jira.mariadb.org/browse/MDEV-31177))
* seconds\_behind\_master is inaccurate for Delayed replication ([MDEV-32265](https://jira.mariadb.org/browse/MDEV-32265))
* detailize the semisync replication magic number error ([MDEV-32365](https://jira.mariadb.org/browse/MDEV-32365))
* Parallel replication deadlock victim preference code errorneously removed ([MDEV-31655](https://jira.mariadb.org/browse/MDEV-31655))

### [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/)

* [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) updated to 26.4.16
* Assertion \`state() == s\_executing || state() == s\_prepared || state() == s\_committing || state() == s\_must\_abort || state() == s\_replaying' failed. ([MDEV-24912](https://jira.mariadb.org/browse/MDEV-24912))
* Assertion \`state() == s\_executing || state() == s\_preparing || state() == s\_prepared || state() == s\_must\_abort || state() == s\_aborting || state() == s\_cert\_failed || state() == s\_must\_replay' failed ([MDEV-31285](https://jira.mariadb.org/browse/MDEV-31285))
* wsrep\_sst\_mariadb-backup not working on FreeBSD ([MDEV-31467](https://jira.mariadb.org/browse/MDEV-31467))
* Galera library 26.4.16 fails with every server version ([MDEV-32024](https://jira.mariadb.org/browse/MDEV-32024))
* Galera node remains paused after interleaving FTWRLs ([MDEV-32282](https://jira.mariadb.org/browse/MDEV-32282))
* Failed to insert streaming client ([MDEV-32051](https://jira.mariadb.org/browse/MDEV-32051))
* When set at runtime, [wsrep\_sst\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) accepts any value ([MDEV-31470](https://jira.mariadb.org/browse/MDEV-31470))
* galera needs packaging script changes to successfully build ([MDEV-32642](https://jira.mariadb.org/browse/MDEV-32642))
* replication breaks when using optimistic replication and replica is a galera node ([MDEV-31833](https://jira.mariadb.org/browse/MDEV-31833))
* McAfee database vulnerability scan caused MariaDB crash with signal 6 (system abort) ([MDEV-27004](https://jira.mariadb.org/browse/MDEV-27004))

### Data Definition

* MariaDB crash on calling function ([MDEV-23902](https://jira.mariadb.org/browse/MDEV-23902))
* ASAN errors in grn\_obj\_unlink / ha\_mroonga::clear\_indexes upon index operations ([MDEV-31970](https://jira.mariadb.org/browse/MDEV-31970))
* vcol circular references lead to stack overflow ([MDEV-31112](https://jira.mariadb.org/browse/MDEV-31112))

### Scripts and Clients

* [mariadb-binlog -T/--table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options) (mysqlbinlog) option ([MDEV-25369](https://jira.mariadb.org/browse/MDEV-25369))
* [mariadb-admin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/mariadb-admin) (mysqladmin) wrong error with [simple\_password\_check](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin) ([MDEV-22418](https://jira.mariadb.org/browse/MDEV-22418))
* [mariadb-install-db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-install-db) shows warning on missing directory $pamtooldir/auth\_pam\_tool\_dir ([MDEV-32142](https://jira.mariadb.org/browse/MDEV-32142))
* main.mysql\_client\_test, main.mysql\_client\_test\_comp failed on ASAN build with error: 5888, status: 23, errno: 2 ([MDEV-19369](https://jira.mariadb.org/browse/MDEV-19369))
* [mariadb-install-db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-install-db) (mysql\_install\_db) doesn't properly grant [proxy privileges](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#proxy-privileges) to all default root user accounts ([MDEV-21194](https://jira.mariadb.org/browse/MDEV-21194))

### Tests

* main.events\_stress or events.events\_stress fails with view-protocol ([MDEV-31455](https://jira.mariadb.org/browse/MDEV-31455))
* main.delete\_use\_source fails (hangs) with view-protocol ([MDEV-31457](https://jira.mariadb.org/browse/MDEV-31457))
* main.sum\_distinct-big and main.merge-big fail with timeout with view-protocol ([MDEV-31465](https://jira.mariadb.org/browse/MDEV-31465))
* main.secure\_file\_priv\_win fails with 2nd execution PS protocol ([MDEV-32023](https://jira.mariadb.org/browse/MDEV-32023))
* Windows : mtr output on is messed up with large MTR\_PARALLEL ([MDEV-32387](https://jira.mariadb.org/browse/MDEV-32387))
* main.mysql\_client\_test\_comp failed in buildbot, error on exec ([MDEV-16641](https://jira.mariadb.org/browse/MDEV-16641))
* main.order\_by\_pack\_big fails with view-protocol ([MDEV-31460](https://jira.mariadb.org/browse/MDEV-31460))

### mariadb-backup

* mariadb-backup full backup failed with InnoDB: Failing assertion: success in storage/innobase/fil/fil0fil.cc line 657 ([MDEV-18200](https://jira.mariadb.org/browse/MDEV-18200))
* mbstream breaks page compression on XFS ([MDEV-25734](https://jira.mariadb.org/browse/MDEV-25734))

### Character Sets, Data Types, Collations

* Prefix keys for CHAR work differently for MyISAM vs InnoDB ([MDEV-30048](https://jira.mariadb.org/browse/MDEV-30048))
* Inconsistent results of DISTINCT with NOPAD ([MDEV-30050](https://jira.mariadb.org/browse/MDEV-30050))
* Assertion \`(length % 4) == 0' failed in my\_lengthsp\_utf32 on INSERT ([MDEV-28835](https://jira.mariadb.org/browse/MDEV-28835))
* Compressed varchar values lost on joins when sorting on columns from joined table(s) ([MDEV-31724](https://jira.mariadb.org/browse/MDEV-31724))
* UBSAN shift exponent X is too large for 64-bit type 'long long int' in sql/field.cc ([MDEV-32226](https://jira.mariadb.org/browse/MDEV-32226))
* Wrong bit encoding using COALESCE ([MDEV-32244](https://jira.mariadb.org/browse/MDEV-32244))

### Spider

* Spider UBSAN runtime error: applying non-zero offset x to null pointer in st\_spider\_param\_string\_parse::restore\_delims ([MDEV-31117](https://jira.mariadb.org/browse/MDEV-31117))
* Segfault when setting spider\_delete\_all\_rows to 0 and delete all rows of a spider table, ASAN heap-use-after-free in spider\_db\_delete\_all\_rows ([MDEV-31996](https://jira.mariadb.org/browse/MDEV-31996))
* ASAN errors in spider\_fields::free\_conn\_holder or spider\_create\_group\_by\_handler ([MDEV-28998](https://jira.mariadb.org/browse/MDEV-28998))
* ASAN: heap-buffer-overflow & stack-buffer-overflow in `spider_db_mbase_row::append_to_str` | SIGSEGV's in `memmove_avx_unaligned_erms` from memcpy in `Binary_string::q_append`, in `Static_binary_string::q_append` and `my_strntoull10rnd_8bit` | Unknown error 12801 ([MDEV-29502](https://jira.mariadb.org/browse/MDEV-29502))

### General

* [binlog\_do\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_do_db) option breaks importing sql dumps ([MDEV-29989](https://jira.mariadb.org/browse/MDEV-29989))
* Crashes in MDL\_key::mdl\_key\_init with lower-case-table-names=2 ([MDEV-32025](https://jira.mariadb.org/browse/MDEV-32025))
* getting error 'Illegal parameter data types row and bigint for operation '+' ' when using ITERATE in a FOR..DO ([MDEV-32275](https://jira.mariadb.org/browse/MDEV-32275))
* Assertion \`arena\_for\_set\_stmt== 0' failed in LEX::set\_arena\_for\_set\_stmt upon SET STATEMENT ([MDEV-17711](https://jira.mariadb.org/browse/MDEV-17711))
* main.mysqlcheck fails on ARM with ASAN use-after-poison in my\_mb\_wc\_filename ([MDEV-26494](https://jira.mariadb.org/browse/MDEV-26494))
* main.delayed fails with wrong error code or timeout when executed after main.deadlock\_ftwrl ([MDEV-27523](https://jira.mariadb.org/browse/MDEV-27523))
* Assertion failed: !pfs->m\_idle || (state == PSI\_SOCKET\_STATE\_ACTIVE) ([MDEV-28561](https://jira.mariadb.org/browse/MDEV-28561))
* MyISAM wrong server status flags ([MDEV-28820](https://jira.mariadb.org/browse/MDEV-28820))
* Server crashes in check\_sequence\_fields upon CREATE TABLE .. SEQUENCE=1 AS SELECT .. ([MDEV-29771](https://jira.mariadb.org/browse/MDEV-29771))
* slow log Rows\_examined out of range ([MDEV-30820](https://jira.mariadb.org/browse/MDEV-30820))
* "`rpm --setugids`" breaks PAM authentication ([MDEV-30904](https://jira.mariadb.org/browse/MDEV-30904))
* incorrect examined rows in case of stored function usage ([MDEV-31742](https://jira.mariadb.org/browse/MDEV-31742))
* Compilation failing on MacOS (unknown warning option -Wno-unused-but-set-variable) ([MDEV-31890](https://jira.mariadb.org/browse/MDEV-31890))
* Server crash upon inserting into Mroonga table with compressed column ([MDEV-31966](https://jira.mariadb.org/browse/MDEV-31966))
* hash unique corrupts index on virtual blobs ([MDEV-32012](https://jira.mariadb.org/browse/MDEV-32012))
* insert into an empty table fails with hash unique ([MDEV-32015](https://jira.mariadb.org/browse/MDEV-32015))
* Valgrind/MSAN warnings in dynamic\_column\_update\_move\_left ([MDEV-32140](https://jira.mariadb.org/browse/MDEV-32140))
* Memory leak showed in [MDEV-6146](https://jira.mariadb.org/browse/MDEV-6146) test suite ([MDEV-32223](https://jira.mariadb.org/browse/MDEV-32223))
* Test from subselect.test fails with statement memory protection ([MDEV-32245](https://jira.mariadb.org/browse/MDEV-32245))
* Memory leak when executing PS for query with IN subquery ([MDEV-32369](https://jira.mariadb.org/browse/MDEV-32369))
* Allow the setting of Auto\_increment on FK referenced columns ([MDEV-32018](https://jira.mariadb.org/browse/MDEV-32018))
* mariadb-upgrade fails with sql\_safe\_updates = on ([MDEV-29914](https://jira.mariadb.org/browse/MDEV-29914))
* Assertion \`!(thd->server\_status & (1U | 8192U))' failed in MDL\_context::release\_transactional\_locks ([MDEV-32541](https://jira.mariadb.org/browse/MDEV-32541))
* Information schema leaks table names and structure to unauthorized users ([MDEV-32500](https://jira.mariadb.org/browse/MDEV-32500))
* Missing CHACHA20-POLY1305 support in WolfSSL ([MDEV-31653](https://jira.mariadb.org/browse/MDEV-31653))
* incorrect error about cyclic reference about JSON type virtual column ([MDEV-32586](https://jira.mariadb.org/browse/MDEV-32586))
* Disable TLS v1.0 and 1.1 for MariaDB ([MDEV-31369](https://jira.mariadb.org/browse/MDEV-31369))
* Better indication of refusing to start because of ProtectHome ([MDEV-25177](https://jira.mariadb.org/browse/MDEV-25177))
* Database upgrade fails: slow\_log table ([MDEV-27757](https://jira.mariadb.org/browse/MDEV-27757))
* myrocks\_hotbackup.1 and test suite files installed when engine is disabled ([MDEV-29993](https://jira.mariadb.org/browse/MDEV-29993))
* client\_ed25519.dll isn't inluded for HeidiSQL. ([MDEV-31315](https://jira.mariadb.org/browse/MDEV-31315))
* Assertion \`!m\_null\_value' failed in int FixedBinTypeBundle::cmp\_item\_fbt::compare or in cmp\_item\_inet6::compare ([MDEV-27207](https://jira.mariadb.org/browse/MDEV-27207))
* type\_test.type\_test\_double fails with 'NUMERIC\_SCALE NULL' ([MDEV-22243](https://jira.mariadb.org/browse/MDEV-22243))
* LeakSanitizer errors in get\_quick\_select or Assertion \`status\_var.local\_memory\_used == 0 || !debug\_assert\_on\_not\_freed\_memory' failed ([MDEV-32476](https://jira.mariadb.org/browse/MDEV-32476))
* Update signal hander user info more compassion and correct url ([MDEV-32535](https://jira.mariadb.org/browse/MDEV-32535))

### Docker Official Images

* Invert single and double quotes for sql command definitions in [healthcheck.sh](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/using-healthcheck-sh) due to failure under [sql\_mode=ANSI\_QUOTES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode#ansi_quotes) - contribution by Dominik Häckel
* [healthcheck.sh](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/using-healthcheck-sh) --no-defaults behaviour was corrected - reported by Dominik Häckel
* Added /docker-entrypoint-init.d for tar{,compression} from [mariadb-backup](../../../mariadb-community-server-release-notes/mariadb-10-5-series/broken-reference/) - [instructions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/docker-official-image-frequently-asked-questions#how-do-i-create-a-mariadb-backup-of-the-data)
* Refactor `docker_mariadb_init` in the entrypoint for extending the MariaDB image
* CIS failure due to world-writable directory /var/run/mysqld, added sticky bit - reported by @ollie1
* Add [PROXY privileges](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#proxy-privileges) for root@MARIADB\_ROOT\_HOST - reported by Matthieu Gusmini
* [healthcheck.sh](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/using-healthcheck-sh) added --galera\_online test, to match what the [mariadb-operator](https://github.com/mariadb-operator/mariadb-operator) does.

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084)

## Changelog

For a complete list of changes made in [MariaDB 10.5.23](mariadb-10-5-23-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-23-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.5.23](mariadb-10-5-23-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-1-3-11-0-4-10-11-6-10-10-7-10-6-16-10-5-23-10-4-32-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
