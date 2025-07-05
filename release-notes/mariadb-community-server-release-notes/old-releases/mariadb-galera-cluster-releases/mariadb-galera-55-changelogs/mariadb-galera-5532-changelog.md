# MariaDB Galera 5.5.32 Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.32) |[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-5532-release-notes.md) |**Changelog** |[Overview of Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 30 Aug 2013

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-5532-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3417](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3417)\
  Tue 2013-08-27 23:40:49 +0300
  * References: [MDEV-4953](https://jira.mariadb.org/browse/MDEV-4953) Calling ha\_start\_of\_new\_statement() for all table handlers under partition engine. This will enable innodb transactions to be declared as read/write.
* [Revision #3416](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3416)\
  Tue 2013-08-27 09:06:04 +0300
  * References [Bug #1216904](https://bugs.launchpad.net/bugs/1216904) - guaranteeing native "create table like.." processing when running without wsrep provider Merged the fix from lp:codership/codership-mysql/5.5-23, rev 3906
* [Revision #3415](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3415)\
  Fri 2013-08-23 12:21:00 +0300
  * References: [Bug #1206129](https://bugs.launchpad.net/bugs/1206129) - Merged revision 3904 from lp:codership/codership-mysql/5.5-23
* [Revision #3414](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3414)\
  Wed 2013-08-21 17:17:30 +0300
  * Merged with lp:codership/codership-mysql/5.5-23, up to revision 3903
* [Revision #3413](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3413)\
  Wed 2013-08-21 16:37:22 +0300
  * References [MDEV-4404](https://jira.mariadb.org/browse/MDEV-4404) - Added log message to catch information of log event corruption
* [Revision #3412](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3412) \[merge]\
  Wed 2013-08-21 16:34:31 +0300
  * Merge with [mariadb 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/mariadb-galera-cluster-releases/mariadb-galera-55-release-notes): `bzr merge lp:maria/5.5 --rtag:mariadb-5.5.32`
  * [Revision #3334.1.504](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.504)\
    Wed 2013-07-17 17:03:59 +0300
    * Revert of marko.makela@oracle.com-20130430103950-j353faze84zzk9xf for xtradb (fix of [bug.php?id=69623](https://bugs.mysql.com/bug.php?id=69623))
  * [Revision #3334.1.503](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.503)\
    Wed 2013-07-17 16:42:13 +0300
    * Fix for [MDEV-4219](https://jira.mariadb.org/browse/MDEV-4219) A simple select query returns random data (upstream bug#68473)
  * [Revision #3334.1.502](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.502) \[merge]\
    Tue 2013-07-16 19:30:39 +0200
    * merge Percona-Server-5.5.32-rel31.0.tar.gz
    * [Revision #0.12.63](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/0.12.63)\
      Tue 2013-07-16 14:55:47 +0200
      * Percona-Server-5.5.32-rel31.0.tar.gz
  * [Revision #3334.1.501](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.501) \[merge]\
    Tue 2013-07-16 19:09:54 +0200
    * mysql-5.5.32 merge
    * [Revision #3077.187.102](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.102)\
      Thu 2013-05-16 17:33:32 +0200
      * Fix for BUG

## 16812255: Removing the `--random-password` option which is supported only for MYSQL server versions 5.6 and above.

```
* [Revision #3077.187.101](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.101)
```

Thu 2013-05-16 10:24:26 +0200

```
  * Changes to verify the solaris upgrade issue.
* [Revision #3077.187.100](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.100)
```

Wed 2013-05-15 16:29:31 +0200

```
  * Fixing the RPM-ULN build issue by ignoring the postinstall_check.sh.
* [Revision #3077.187.99](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.99)
```

Wed 2013-05-15 15:37:20 +0200

```
  * Bug 16812255 - 5.5.32 PKG INSTALLATION FAILED DURING MYSQL_INSTALL_DB EXECUTION
* [Revision #3077.187.98](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.98)
```

Mon 2013-05-13 10:21:09 +0200

```
  * Updated copyright year information
* [Revision #3077.187.97](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.97)
```

Mon 2013-05-13 09:46:44 +0200

```
  * Adding fix for Bug#16798868
* [Revision #3077.187.96](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.96)
```

Wed 2013-05-08 12:08:20 +0200

```
  * Bug#16779374: NEW ERROR MESSAGE ADDED TO 5.5 AFTER 5.6 GA - REUSING NUMBER ALREADY USED BY 5.6
* [Revision #3077.187.95](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.95)
```

Tue 2013-05-07 14:36:46 +0200

```
  * ULN-RPMs bug fix for BR16298542
* [Revision #3077.187.94](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.94)
```

Mon 2013-05-06 20:31:26 +0530

```
  * Bug #16722314 FOREIGN KEY ID MODIFIED DURING EXPORT Bug #16754901 PARS_INFO_FREE NOT CALLED IN DICT_CREATE_ADD_FOREIGN_TO_DICTIONARY
* [Revision #3077.187.93](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.93)
```

Mon 2013-05-06 16:06:32 +0200

```
  * Bug#16757869: INNODB: POSSIBLE REGRESSION IN 5.5.31, BUG#16004999
* [Revision #3077.187.92](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.92)
```

Mon 2013-05-06 15:19:37 +0200

```
  * Updated spec file for Bug16488773
* [Revision #3077.187.91](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.91)
```

Fri 2013-05-03 16:39:17 +0300\
\* [Revision #3077.187.90](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.90) \[merge]\
Tue 2013-04-30 20:40:38 +0200

```
  * merge from mysql-5.1
  * [Revision #2661.848.26](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.26)
```

Tue 2013-04-30 20:39:12 +0200

```
    * Bug#16405422 - RECOVERY FAILURE, ASSERT !RECV_NO_LOG_WRITE
* [Revision #3077.187.89](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.89) [merge]
```

Tue 2013-04-30 22:46:37 +0530

```
  * BUG#16222245 - CRASH WITH EXPLAIN FOR A QUERY WITH LOOSE SCAN FOR GROUP BY, MYISAM
  * [Revision #2661.848.25](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.25)
```

Tue 2013-04-30 22:38:34 +0530

```
    * BUG#16222245 - CRASH WITH EXPLAIN FOR A QUERY WITH LOOSE SCAN FOR GROUP BY, MYISAM
* [Revision #3077.187.88](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.88)
```

Tue 2013-04-30 13:39:50 +0300

```
  * Bug#16720368 INNODB IGNORES *.IBD FILE BREAKAGE AT STARTUP
* [Revision #3077.187.87](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.87)
```

Sat 2013-04-27 16:04:54 +0800

```
  * Bug #13004581 	BLACKHOLE BINARY LOG WITH ROW IGNORES UPDATE AND DELETE STATEMENTS
* [Revision #3077.187.86](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.86)
```

Thu 2013-04-25 11:56:26 +0530

```
  * BUG#16698172-CANNOT DO POINT-IN-TIME RECOVERY FOR SINGLE DATABASE; MYSQLBINLOG
* [Revision #3077.187.85](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.85)
```

Wed 2013-04-24 17:21:42 +0300

```
  * Bug #16680313: CLIENT DOESN'T READ PLUGIN-DIR FROM MY.CNF SET BY MYSQL_READ_DEFAULT_FILE Parsing of the plugin-dir config file option was not working due to a typo. Fixed the typo. No test case can be added due to lack of support for defaults-exitra-file testing in mysql-test-run.pl. Thanks to Sinisa for contributing the fix.
* [Revision #3077.187.84](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.84) [merge]
```

Wed 2013-04-24 13:34:11 +0530

```
  * [Revision #2661.848.24](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.24)
```

Wed 2013-04-24 13:31:10 +0530\
\* [Revision #3077.187.83](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.83) \[merge]\
Wed 2013-04-24 08:48:34 +0200

```
  * Null merge from mysql-5.1 to mysql-5.5
  * [Revision #2661.848.23](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.23)
```

Wed 2013-04-24 08:47:30 +0200

```
    * Bug #15973904 INNODB PARTITION CODE HOLDS LOCK_OPEN AND SLEEPS WHILE OPENING MISSING PARTITION
* [Revision #3077.187.82](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.82)
```

Wed 2013-04-24 08:42:59 +0200

```
  * Merge from mysql-5.1 to mysql-5.5
* [Revision #3077.187.81](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.81) [merge]
```

Mon 2013-04-22 14:30:47 +0200

```
  * Upmerge of the 5.1.69 build
  * [Revision #2661.848.22](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.22)
```

Mon 2013-04-22 14:01:07 +0200

```
    * Merge from mysql-5.1.69-release
* [Revision #3077.187.80](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.80) [merge]
```

Sat 2013-04-20 12:36:11 +0530

```
  * Bug#16073689 : CRASH IN ITEM_FUNC_MATCH::INIT_SEARCH
  * [Revision #2661.848.21](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.21)
```

Sat 2013-04-20 12:28:22 +0530

```
    * Bug#16073689 : CRASH IN ITEM_FUNC_MATCH::INIT_SEARCH
* [Revision #3077.187.79](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.79) [merge]
```

Thu 2013-04-18 12:52:59 +0200

```
  * Merge from mysql-5.5.31-release
* [Revision #3077.187.78](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.78)
```

Wed 2013-04-17 09:26:51 +0200

```
  * Bug#16626742 IN MY_MD5FINAL IN MYSYS/MD5.C, CTX IS NOT PROPERLY ZEROED AS INTENDED
* [Revision #3077.187.77](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.77)
```

Tue 2013-04-16 16:26:45 +0530

```
  * Bug #16632543 - INCORRECT VALUE OF BOGOMIPS IN MYSQLTEST
* [Revision #3077.187.76](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.76) [merge]
```

Tue 2013-04-16 12:17:18 +0200

```
  * Merging the changes for Bug 16633169 - MYSQL.INFO CONTAINS OUTDATED INFORMATION.
  * [Revision #2661.848.20](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.20)
```

Tue 2013-04-16 12:12:18 +0200

```
    * Bug 16633169 - MYSQL.INFO CONTAINS OUTDATED INFORMATION.
* [Revision #3077.187.75](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.75) [merge]
```

Sun 2013-04-14 08:09:56 +0530

```
  * Merge from 5.1 to 5.5
  * [Revision #2661.848.19](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.19)
```

Sun 2013-04-14 07:30:49 +0530

```
    * Bug#16347426:ASSERTION FAILED: (SELECT_INSERT && !TABLES->NEXT_NAME_RESOLUTION_TABLE) || !TAB
* [Revision #3077.187.74](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.74)
```

Fri 2013-04-12 14:18:21 +0530

```
  * BUG#16615117 MYSQLDUMP PRODUCES A CHANGE MASTER STATEMENT WITH A PORT NUMBER ENCLOSED IN QUOTES
* [Revision #3077.187.73](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.73)
```

Fri 2013-04-12 09:39:56 +0200

```
  * Bug#16540042: WRONG QUERY RESULT WHEN USING RANGE OVER PARTIAL INDEX
* [Revision #3077.187.72](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.72)
```

Thu 2013-04-11 10:50:50 +0800

```
  * Bug	:#16005310 FIx bug - INNODB_ROW_LOCK_TIME_MAX SEEMS TO HAVE AN OVERFLOW
* [Revision #3077.187.71](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.71)
```

Wed 2013-04-10 16:43:09 +0200

```
  * Bug#16395606 SCRIPTS MISSING EXECUTE BIT
* [Revision #3077.187.70](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.70)
```

Wed 2013-04-10 11:50:41 +0530

```
  * BUG#16402143 - STACK CORRUPTION IN DBUG_EXPLAIN DESCRIPTION AND FIX: DBUG_EXPLAIN result in buffer overflow when the DEBUG variable values length exceed 255. In _db_explain_ function which call macro str_to_buf incorrectly passes the length of buf avaliable to strnmov as len+1. The fix calculates the avaliable space in buf and passes it to strnxmov.
* [Revision #3077.187.69](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.69) [merge]
```

Tue 2013-04-09 14:03:35 +0530

```
  * local merge.
  * [Revision #2661.848.18](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.18)
```

Tue 2013-04-09 14:00:05 +0530

```
    * Backporting patch for bug#15852074.
* [Revision #3077.187.68](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.68) [merge]
```

Mon 2013-04-08 18:53:24 +0530

```
  * null merge
  * [Revision #2661.848.17](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.17)
```

Mon 2013-04-08 18:48:57 +0530\
\* [Revision #3077.187.67](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.67) \[merge]\
Mon 2013-04-08 18:14:06 +0530

```
  * [Revision #2661.848.16](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.16)
```

Mon 2013-04-08 18:12:39 +0530\
\* [Revision #3077.187.66](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.66)\
Mon 2013-04-08 15:25:45 +0530

```
  * BUG#15978766 - TEST VALGRIND_REPORT FAILS INNODB TESTS
* [Revision #3077.187.65](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.65)
```

Thu 2013-04-04 14:54:16 +0530

```
  * Bug #16401597 - MTR V1 RETURNS INCORRECT PATH TO VARIABLE @@BASEDIR
* [Revision #3077.187.64](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.64)
```

Wed 2013-04-03 18:09:37 +0200

```
  * Bug 16534721 - MYSQL_INSTALL_DB RUNS AGAIN DURING UPGRADE EVEN DATA DIRECTORY EXISTS
* [Revision #3077.187.63](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.63) [merge]
```

Tue 2013-04-02 16:20:49 +0200

```
  * merge 5.1 => 5.5
  * [Revision #2661.848.15](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.15)
```

Tue 2013-04-02 16:05:10 +0200

```
    * Bug#14700180 CRASH IN COPY_FUNCS This is a backport of the fix for Bug#13966809 CRASH IN COPY_FUNCS WHEN GROUPING BY OUTER QUERY BLOB FIELD IN SUBQUERY
* [Revision #3077.187.62](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.62)
```

Tue 2013-04-02 11:14:39 +0200

```
  * Bug#11765629 CMAKE: CAN SUPPRESS INSTALLATION OF SQL-BENCH, BUT NOT MYSQL-TEST
* [Revision #3077.187.61](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.61) [merge]
```

Tue 2013-04-02 11:17:06 +0530

```
  * [Revision #2661.848.14](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.14)
```

Tue 2013-04-02 11:16:26 +0530\
\* [Revision #3077.187.60](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.60) \[merge]\
Mon 2013-04-01 13:45:27 +0530

```
  * [Revision #2661.848.13](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.13)
```

Mon 2013-04-01 12:26:55 +0530\
\* [Revision #3077.187.59](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.59) \[merge]\
Sun 2013-03-31 06:52:16 +0530

```
  * Merge from 5.1 to 5.5
  * [Revision #2661.848.12](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.12)
```

Sun 2013-03-31 06:48:30 +0530

```
    * Bug #16347343 : CRASH, GROUP_CONCAT, DERIVED TABLES
* [Revision #3077.187.58](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.58)
```

Sat 2013-03-30 19:24:54 +0530

```
  * Bug#14261010: ON DUPLICATE KEY UPDATE CRASHES THE SERVER
* [Revision #3077.187.57](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.57) [merge]
```

Fri 2013-03-29 22:11:33 +0530

```
  * Merge from mysql-5.1 to mysql-5.5
  * [Revision #2661.848.11](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.11)
```

Fri 2013-03-29 22:01:10 +0530

```
    * Bug #16244691 SERVER GONE AWAY ERROR OCCURS DEPENDING ON THE NUMBER OF TABLE/KEY RELATIONS
* [Revision #3077.187.56](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.56)
```

Fri 2013-03-29 16:33:33 +0530

```
  * Bug #16402124 - MTR PROCESSES CERTAIN ASSIGNED VARDIR VALUES WRONG
* [Revision #3077.187.55](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.55) [merge]
```

Fri 2013-03-29 15:14:38 +0530

```
  * [Revision #2661.848.10](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.10)
```

Fri 2013-03-29 15:09:14 +0530\
\* [Revision #3077.187.54](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.54)\
Fri 2013-03-29 11:44:42 +0530\
\* [Revision #3077.187.53](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.53)\
Fri 2013-03-29 09:28:31 +0530

```
  * Bug#15948818-SEMI-SYNC ENABLED MASTER CRASHES WHEN EVENT SCHEDULER DROPS EVENTS
* [Revision #3077.187.52](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.52) [merge]
```

Thu 2013-03-28 17:41:22 +0200

```
  * merge
  * [Revision #2661.848.9](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.9)
```

Thu 2013-03-28 17:37:29 +0200

```
    * Addendum #1 to the fix for bug #16451878 : GEOMETRY QUERY CRASHES SERVER
* [Revision #3077.187.51](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.51) [merge]
```

Thu 2013-03-28 19:17:28 +0530

```
  * Merge from 5.1 to 5.5
  * [Revision #2661.848.8](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.8)
```

Thu 2013-03-28 19:11:26 +0530

```
    * BUG#11753852: IF() VALUES ARE EVALUATED DIFFERENTLY IN A REGULAR SQL VS PREPARED STATEMENT
* [Revision #3077.187.50](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.50) [merge]
```

Thu 2013-03-28 14:18:51 +0530

```
  * Merge from mysql-5.1 to mysql-5.5
  * [Revision #2661.848.7](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.7)
```

Thu 2013-03-28 14:14:39 +0530

```
    * Bug#14324766:PARTIALLY WRITTEN INSERT STATEMENT IN BINLOG NO ERRORS REPORTED
* [Revision #3077.187.49](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.49)
```

Thu 2013-03-28 11:47:43 +0530

```
  * Bug #16403186 - MTR ON WINDOWS SHOULD NOT TRY TO START CDB IF RUNNING WITH PARALLEL
* [Revision #3077.187.48](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.48) [merge]
```

Thu 2013-03-28 10:43:50 +0530

```
  * Null merge from mysql-5.1 to mysql-5.5
  * [Revision #2661.848.6](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.6)
```

Thu 2013-03-28 10:42:42 +0530

```
    * Bug #16244691 SERVER GONE AWAY ERROR OCCURS DEPENDING ON THE NUMBER OF TABLE/KEY RELATIONS
* [Revision #3077.187.47](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.47) [merge]
```

Thu 2013-03-28 10:25:23 +0530

```
  * Merge from mysql-5.1 to mysql-5.5
  * [Revision #2661.849.1](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.849.1)
```

Wed 2013-03-27 11:11:38 +0530

```
    * Bug #16244691 SERVER GONE AWAY ERROR OCCURS DEPENDING ON THE NUMBER OF TABLE/KEY RELATIONS
* [Revision #3077.187.46](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.46) [merge]
```

Wed 2013-03-27 16:06:33 +0200

```
  * merge 5.1->5.5
  * [Revision #2661.848.5](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.5)
```

Wed 2013-03-27 16:03:00 +0200

```
    * Bug #16451878: GEOMETRY QUERY CRASHES SERVER
* [Revision #3077.187.45](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.45) [merge]
```

Wed 2013-03-27 11:22:25 +0000

```
  * BUG#16541422: LOG-SLAVE-UPDATES + REPLICATE-WILD-IGNORE-TABLE FAILS FOR USER VARIABLES
  * [Revision #2661.848.4](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.4)
```

Wed 2013-03-27 11:19:29 +0000

```
    * BUG#16541422: LOG-SLAVE-UPDATES + REPLICATE-WILD-IGNORE-TABLE FAILS FOR USER VARIABLES
* [Revision #3077.187.44](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.44) [merge]
```

Wed 2013-03-27 11:59:40 +0530

```
  * Merge from mysql-5.1 to mysql-5.5
  * [Revision #2661.848.3](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.3)
```

Wed 2013-03-27 11:53:01 +0530

```
    * Bug#11829838: ALTER TABLE NOT BINLOGGED WITH `--BINLOG-IGNORE-DB` AND FULLY QUALIFIED TABLE
* [Revision #3077.187.43](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.43) [merge]
```

Tue 2013-03-26 23:11:55 +0200

```
  * merge from 5.1->5.5 repo.
  * [Revision #2661.848.2](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.2) [merge]
```

Tue 2013-03-26 23:10:42 +0200

```
    * merge from 5.1 repo.
* [Revision #3077.187.42](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.42)
```

Tue 2013-03-26 21:45:39 +0200\
\* [Revision #3077.187.41](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.41) \[merge]\
Tue 2013-03-26 20:52:01 +0200

```
  * merge from 5.1
  * [Revision #2661.848.1](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.848.1)
```

Tue 2013-03-26 19:24:01 +0200

```
    * Bug#16541422 LOG-SLAVE-UPDATES + REPLICATE-WILD-IGNORE-TABLE FAILS FOR USER VARIABLES
* [Revision #3077.187.40](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.40) [merge]
```

Tue 2013-03-26 08:24:11 +0100

```
  * NULL merge 5.1 => 5.5
  * [Revision #2661.844.69](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.69)
```

Tue 2013-03-26 08:22:45 +0100

```
    * Bug#62856 Check for "stack overrun" doesn't work with gcc-4.6, server crashes Bug#13243248 CHECK FOR "STACK OVERRUN" DOESN'T WORK WITH GCC-4.6, SERVER CRASHES
* [Revision #3077.187.39](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.39)
```

Mon 2013-03-25 11:27:12 +0530

```
  * BUG#16438800 - SLAVE_MAX_ALLOWED_PACKET NOT HONORED ON SLAVE IO CONNECT
* [Revision #3077.187.38](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.38) [merge]
```

Fri 2013-03-22 20:16:53 +0530

```
  * local merge.
  * [Revision #2661.844.68](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.68)
```

Fri 2013-03-22 20:00:40 +0530

```
    * Bug#12671635 : Updating embedded tests.
* [Revision #3077.187.37](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.37) [merge]
```

Fri 2013-03-22 15:33:59 +0530

```
  * local merge.
  * [Revision #2661.844.67](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.67)
```

Fri 2013-03-22 15:29:57 +0530

```
    * Bug#12671635 : Fixing test cases.
* [Revision #3077.187.36](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.36)
```

Fri 2013-03-22 14:55:30 +0530

```
  * Bug#16500013 : post-fix
* [Revision #3077.187.35](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.35) [merge]
```

Thu 2013-03-21 23:40:25 +0530

```
  * Merge of patch for Bug#12671635 from mysql-5.1.
  * [Revision #2661.844.66](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.66)
```

Thu 2013-03-21 23:36:02 +0530

```
    * Bug#12671635 HELP-TABLEFORMAT DOESN'T MATCH HELP-FILES
* [Revision #3077.187.34](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.34)
```

Thu 2013-03-21 22:51:40 +0530

```
  * Bug#16500013 : ADD VERSION CHECK TO MYSQL_UPGRADE
* [Revision #3077.187.33](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.33)
```

Thu 2013-03-21 11:40:43 +0530

```
  * Bug #16051728 SERVER CRASHES IN ADD_IDENTIFIER ON CONCURRENT ALTER TABLE AND SHOW ENGINE INNOD
* [Revision #3077.187.32](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.32) [merge]
```

Wed 2013-03-20 17:52:15 +0100

```
  * Null merge from 5.1 for permission changes.
  * [Revision #2661.844.65](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.65)
```

Wed 2013-03-20 17:49:30 +0100

```
    * Correcting the permissions of executable files.
* [Revision #3077.187.31](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.31)
```

Wed 2013-03-20 17:50:15 +0100

```
  * Correcting the permissions of the executable files.
* [Revision #3077.187.30](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.30)
```

Tue 2013-03-19 17:09:17 +0100

```
  * Bug#13009341 CRASH IN STR_TO_DATETIME AFTER MISBEHAVING "BLOB" VALUE COMPARISON
* [Revision #3077.187.29](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.29)
```

Wed 2013-03-20 11:20:12 +0100

```
  * Bug#16394084: LOOSE INDEX SCAN WITH QUOTED INT PREDICATE RETURNS RANDOM DATA
* [Revision #3077.187.28](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.28)
```

Tue 2013-03-19 15:08:19 +0100

```
  * Bug#16359402 CRASH WITH AGGREGATES: ASSERTION FAILED: N < M_SIZE
* [Revision #3077.187.27](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.27)
```

Tue 2013-03-19 15:53:48 +0100

```
  * Fix for Bug 16395495 - OLD FSF ADDRESS IN GPL HEADER
* [Revision #3077.187.26](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.26) [merge]
```

Tue 2013-03-19 13:36:34 +0100

```
  * Upmerging the changes for Bug 16395495 from 5.1
  * [Revision #2661.844.64](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.64)
```

Tue 2013-03-19 13:29:12 +0100

```
    * Bug 16395495 - OLD FSF ADDRESS IN GPL HEADER
* [Revision #3077.187.25](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.25)
```

Mon 2013-03-18 17:20:30 +0200

```
  * Fix Bug#16400412 UNNECESSARY DICT_UPDATE_STATISTICS DURING CONCURRENT UPDATES
* [Revision #3077.187.24](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.24) [merge]
```

Tue 2013-03-19 05:35:30 +0100

```
  * Upmerging the changes for Bug 16401147 from 5.1
  * [Revision #2661.844.63](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.63)
```

Tue 2013-03-19 05:19:31 +0100

```
    * Bug 16401147 - CRLF INSTEAD OF LF IN README
* [Revision #3077.187.23](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.23)
```

Tue 2013-03-19 05:24:03 +0100

```
  * Bug 16401147 - CRLF INSTEAD OF LF IN README
* [Revision #3077.187.22](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.22) [merge]
```

Mon 2013-03-18 15:03:54 +0530

```
  * merge from mysql-5.1 to mysql-5.5
  * [Revision #2661.844.62](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.62)
```

Mon 2013-03-18 15:01:16 +0530

```
    * Bug#14771299 OUT-OF-BOUND READS WRITE IN MYSQLBINLOG
* [Revision #3077.187.21](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.21)
```

Mon 2013-03-18 13:48:53 +0530

```
  * Bug #16076289 : BACKPORT FIX FOR BUG #14786792 TO 5.5
* [Revision #3077.187.20](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.20) [merge]
```

Mon 2013-03-18 12:46:06 +0530

```
  * Merge of patch for bug#14685362 from mysql-5.1.
  * [Revision #2661.844.61](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.61)
```

Mon 2013-03-18 12:44:38 +0530

```
    * Bug#14685362 : MEMORY LEAKS IN MYSQL CLIENT IN INTERACTIVE MODE
* [Revision #3077.187.19](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.19) [merge]
```

Fri 2013-03-15 08:57:59 +0530

```
  * Bug#16056813-MEMORY LEAK ON FILTERED SLAVE Null merge from mysql-5.1
  * [Revision #2661.844.60](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.60)
```

Fri 2013-03-15 08:56:20 +0530

```
    * Bug#16056813-MEMORY LEAK ON FILTERED SLAVE
* [Revision #3077.187.18](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.18)
```

Thu 2013-03-14 15:33:25 +0100

```
  * Bug#16359402 CRASH WITH AGGREGATES: ASSERTION FAILED: N < M_SIZE
* [Revision #3077.187.17](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.17) [merge]
```

Thu 2013-03-14 11:22:08 +0300

```
  * 5.1 -> 5.5 merge
  * [Revision #2661.844.59](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.59)
```

Thu 2013-03-14 11:11:17 +0300

```
    * Bug#16075310 SERVER CRASH OR VALGRIND ERRORS IN ITEM_FUNC_GROUP_CONCAT::SETUP AND ::ADD Item_func_group_concat::copy_or_same() creates a copy of original object. It also creates a copy of ORDER structure because ORDER struct elements may be modified in find_order_in_list() called from Item_func_group_concat::setup(). As ORDER copy is created using memcpy, ORDER::next elements point to original ORDER structs. Thus find_order_in_list() called from EXECUTE stmt modifies ordinal ORDER item pointers so they point to runtime items, these items are freed after execution, so original ORDER structure becomes invalid. The fix is to properly update ORDER::next fields so that they point to new ORDER elements.
* [Revision #3077.187.16](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.16) [merge]
```

Wed 2013-03-13 16:29:11 +0530

```
  * BUG#14593883-REPLICATION BREAKS WHEN SET DATA TYPE COLUMNS ARE USED INSIDE A STORED PROCEDURE Merging post-push fix from mysql-5.1
  * [Revision #2661.844.58](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.58)
```

Wed 2013-03-13 16:24:35 +0530

```
    * BUG#14593883-REPLICATION BREAKS WHEN SET DATA TYPE COLUMNS ARE USED INSIDE A STORED PROCEDURE
* [Revision #3077.187.15](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.15)
```

Wed 2013-03-13 11:43:21 +0530

```
  * Bug#16268289 LOCK_REC_VALIDATE_PAGE() MAY DEREFERENCE A POINTER TO A FREED LOCK
* [Revision #3077.187.14](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.14) [merge]
```

Wed 2013-03-13 09:43:50 +0530

```
  * Bug#16084346: SSL_CONNECT_DEBUG.TEST FAILURE IN 5.1
  * [Revision #2661.844.57](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.57)
```

Wed 2013-03-13 09:42:07 +0530\
\* [Revision #3077.187.13](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.13) \[merge]\
Tue 2013-03-12 22:44:32 +0530

```
  * BUG#14593883-REPLICATION BREAKS WHEN SET DATA TYPE COLUMNS ARE USED INSIDE A STORED PROCEDURE
  * [Revision #2661.844.56](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.56)
```

Tue 2013-03-12 22:36:13 +0530

```
    * BUG#14593883-REPLICATION BREAKS WHEN SET DATA TYPE COLUMNS ARE USED INSIDE A STORED PROCEDURE
* [Revision #3077.187.12](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.12)
```

Tue 2013-03-12 13:58:10 +0200

```
  * Bug#16409715 ASSERT SYNC_THREAD_LEVELS_G(ARRAY, LEVEL - 1, TRUE), IBUF, FREE SPACE MANAGEMENT
* [Revision #3077.187.11](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.11) [merge]
```

Tue 2013-03-12 13:57:02 +0200

```
  * Merge mysql-5.1 to mysql-5.5.
  * [Revision #2661.844.55](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.55)
```

Tue 2013-03-12 13:42:12 +0200

```
    * Bug#16463505 PESSIMISTIC PAGE_ZIP_AVAILABLE() MAY CAUSE INFINITE PAGE SPLIT
  * [Revision #2661.844.54](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.54)
```

Tue 2013-03-12 13:37:00 +0200\
\* [Revision #3077.187.10](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.10)\
Mon 2013-03-11 16:46:11 +0100

```
  * Bug#11766815 INVALID SYSTEM CHECK TIME_T_UNSIGNED
* [Revision #3077.187.9](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.9)
```

Mon 2013-03-11 12:03:26 +0530\
\* [Revision #3077.187.8](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.8)\
Fri 2013-03-08 14:55:41 +0530\
\* [Revision #3077.187.7](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.187.7)\
Thu 2013-03-07 14:44:35 +0530

```
  * BUG#16069598 - SERVER CRASH BY NULL POINTER DEREFERENCING IN MEM_HEAP_CREATE_BLOCK()
* [Revision #3077.187.6](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.6)
```

Fri 2013-03-01 13:25:59 +0100

```
  * Bug#11765489 CMAKE BUILD ON MAC OS X DOES NOT DETERMINE CPU TYPE
* [Revision #3077.187.5](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.5)
```

Thu 2013-03-07 12:12:58 +0530

```
  * Bug#16169063: SECURITY CONCERN BECAUSE OF INSUFFICIENT LOGGING
* [Revision #3077.187.4](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.4)
```

Wed 2013-03-06 11:49:57 +0530

```
  * Bug #16133801 UNEXPLAINABLE INNODB UNIQUE INDEX LOCKS ON DELETE + INSERT WITH SAME VALUES
* [Revision #3077.187.3](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.3) [merge]
```

Wed 2013-03-06 06:52:18 +0100

```
  * NULL Merge for release 5.1.69
  * [Revision #2661.844.53](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/2661.844.53)
```

Tue 2013-03-05 16:09:54 +0100

```
    * Raise version number after cloning 5.1.69
* [Revision #3077.187.2](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.2)
```

Tue 2013-03-05 10:47:49 -0500

```
  * Bug#16068056 INNODB CALLS BUF_VALIDATE() TOO OFTEN WITH UNIV_DEBUG
* [Revision #3077.187.1](https://bazaar.launchpad.net/%7Emaria-captains/maria/maria-5.5-galera/revision/3077.187.1)
```

Tue 2013-03-05 12:19:07 +0100

```
  * Raise version number after cloning 5.5.31
```

* [Revision #3334.1.500](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.500) \[merge]\
  Tue 2013-07-16 19:03:06 +0200
  * 5.3 merge
  * [Revision #2502.567.114](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.114) \[merge]\
    Mon 2013-07-15 18:32:25 +0200
    * 5.2 merge
    * [Revision #2502.566.51](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.51)\
      Tue 2013-07-09 22:24:57 +0200
      * [MDEV-4409](https://jira.mariadb.org/browse/MDEV-4409) - Fix deadlock in MySQL key cache code, that can happen if there is a key cache resize running in parallel with an update.
* [Revision #3334.1.499](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.499) \[merge]\
  Tue 2013-07-16 15:59:30 +0400
  * Automatic merge
  * [Revision #3334.36.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.36.1)\
    Tue 2013-07-16 15:57:27 +0400
    * [MDEV-4782](https://jira.mariadb.org/browse/MDEV-4782): Valgrind warnings (Conditional jump or move depends on uninitialised value) with InnoDB, semijoin - in sub\_select(): don't call table->file->position() when reading the first record produced an error.
* [Revision #3334.1.498](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.498)\
  Tue 2013-07-16 17:26:25 +0400
  * Update test results after the last cset.
* [Revision #3334.1.497](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.497)\
  Tue 2013-07-16 10:56:42 +0400
  * [MDEV-4778](https://jira.mariadb.org/browse/MDEV-4778): Incorrect results from Aria/MyISAM SELECT using index with prefix length on TEXT column Backport the fix olav.sandstaa@sun.com-20101102184747-qfuntqwj021imy9r: "Fix for Bug#52660 Perf. regr. using ICP for MyISAM on range queries on an index containing TEXT" (together with further fixes in that code) into MyISAM and Aria.
* [Revision #3334.1.496](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.496)\
  Tue 2013-07-16 09:22:17 +0400
  * [MDEV-4173](https://jira.mariadb.org/browse/MDEV-4173): Wrong result (extra row) with semijoin=on, joins in outer query, LEFT JOIN in the subquery Apply the patch from Patryk Pomykalski: - create\_internal\_tmp\_table\_from\_heap() will now return information whether the last row that we tried to write was a duplicate row. (mysql-5.6 also has this change)
* [Revision #3334.1.495](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.495)\
  Mon 2013-07-15 18:51:52 +0400
  * [MDEV-4536](https://jira.mariadb.org/browse/MDEV-4536), [MDEV-4042](https://jira.mariadb.org/browse/MDEV-4042) - Make JOIN::cleanup(true) also work correctly when the query is KILLed after join optimization was started but before a query plan was produced
* [Revision #3334.1.494](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.494)\
  Thu 2013-07-11 19:27:39 +0400
  * [MDEV-4042](https://jira.mariadb.org/browse/MDEV-4042): Assertion \`table->key\_read == 0' fails in close\_thread\_table on EXPLAIN [MDEV-4536](https://jira.mariadb.org/browse/MDEV-4536): ...sql/sql\_base.cc:1598: bool close\_thread\_table(THD\*, TABLE): Assertion - Make JOIN::cleanup(full=true) always free join optimization tabs.
* [Revision #3334.1.493](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.493)\
  Thu 2013-07-11 15:12:50 +0400
  * [MDEV-4556](https://jira.mariadb.org/browse/MDEV-4556) Server crashes in SEL\_ARG::rb\_insert with index\_merge+index\_merge\_sort\_union, FORCE INDEX - merge\_same\_index\_scans() may put the same SEL\_ARG tree in multiple result plans. make it call incr\_refs() on the SEL\_ARG trees that it does key\_or() on, because key\_or(sel\_arg\_tree\_1, sel\_arg\_tree\_2) call may invalidate SEL\_ARG trees pointed by sel\_arg\_tree\_1 and sel\_arg\_tree\_2.
* [Revision #3334.1.492](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.492) \[merge]\
  Wed 2013-07-10 02:05:06 +0400
  * Merge from 5.3
  * [Revision #2502.567.113](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.113) \[merge]\
    Tue 2013-07-09 11:02:56 +0400
    * Merge from 5.2
    * [Revision #2502.566.50](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.50) \[merge]\
      Tue 2013-07-09 10:54:47 +0400
      * Merge from 5.1
      * [Revision #2502.565.51](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.51)\
        Sat 2013-07-06 15:28:11 +0200
        * Bug #69682 - mysqld crashes after uninstall of plugin with "first" status var
      * [Revision #2502.565.50](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.50)\
        Fri 2013-05-24 17:35:30 +0200
        * [MDEV-4575](https://jira.mariadb.org/browse/MDEV-4575) MySQL client doesn't strip off 5.5.5- prefix while connecting to 10.x server
  * [Revision #2502.567.112](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.112)\
    Fri 2013-07-05 20:45:42 +0200
    * [MDEV-4610](https://jira.mariadb.org/browse/MDEV-4610) SQL query crashes MariaDB with derived\_with\_keys [MDEV-4643](https://jira.mariadb.org/browse/MDEV-4643) MariaDB crashes consistently when trying a SELECT on VIEW with a UNION and an additional JOIN in SELECT
  * [Revision #2502.567.111](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.111)\
    Fri 2013-07-05 17:54:25 +0200
    * [MDEV-4665](https://jira.mariadb.org/browse/MDEV-4665) crash when referencing missing function in a subquery
  * [Revision #2502.567.110](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.110)\
    Fri 2013-07-05 16:02:02 +0200
    * [MDEV-4257](https://jira.mariadb.org/browse/MDEV-4257) Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' fails on FROM subquery with fulltext search, derived\_merge=on
* [Revision #3334.1.491](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.491) \[merge]\
  Mon 2013-07-08 16:49:42 +0400
  * Merging from 5.3
  * [Revision #2502.567.109](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.109)\
    Wed 2013-07-03 09:46:20 +0200
    * [MDEV-4667](https://jira.mariadb.org/browse/MDEV-4667) DATE('string') incompability between mysql and mariadb
* [Revision #3334.1.490](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.490)\
  Thu 2013-07-04 18:37:55 +0300
  * [MDEV-4752](https://jira.mariadb.org/browse/MDEV-4752): Segfault during parsing of illegal query
* [Revision #3334.1.489](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.489)\
  Mon 2013-07-01 17:54:24 +0200
  * [MDEV-4718](https://jira.mariadb.org/browse/MDEV-4718) Test "outfile\_loaddata" fails on bigendian arches (ppc64)
* [Revision #3334.1.488](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.488)\
  Mon 2013-07-01 12:03:10 +0200
  * [MDEV-4670](https://jira.mariadb.org/browse/MDEV-4670) THD::awake bug with my\_sleep call
* [Revision #3334.1.487](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.487)\
  Mon 2013-07-01 12:02:44 +0200
  * [MDEV-4683](https://jira.mariadb.org/browse/MDEV-4683) query start\_time not reset when going to sleep
* [Revision #3334.1.486](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.486) \[merge]\
  Fri 2013-06-28 16:27:22 +0400
  * Merge
  * [Revision #2502.567.108](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.108)\
    Fri 2013-06-28 16:25:06 +0400
    * A clean-up for [MDEV-4634](https://jira.mariadb.org/browse/MDEV-4634)
* [Revision #3334.1.485](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.485) \[merge]\
  Fri 2013-06-28 15:20:40 +0400
  * Merge from 5.3
  * [Revision #2502.567.107](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.107)\
    Fri 2013-06-28 12:00:25 +0400
    * [MDEV-4634](https://jira.mariadb.org/browse/MDEV-4634) Crash in CONVERT\_TZ Item\_func\_min\_max::get\_date() did not check the returned value against the fuzzy\_date flags, so it could return a bad value to the caller that expects a good date (e.h. CONVERT\_TZ).
* [Revision #3334.1.484](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.484)\
  Thu 2013-06-27 14:19:04 +0200
  * [MDEV-4720](https://jira.mariadb.org/browse/MDEV-4720) : fix my\_context.h for use with x32 ABI. Do not use x64 assembler implementation in x32.
* [Revision #3334.1.483](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.483)\
  Sat 2013-06-22 14:02:03 +0200
  * [MDEV-4685](https://jira.mariadb.org/browse/MDEV-4685) Compile error on LFS
* [Revision #3334.1.482](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.482) \[merge]\
  Tue 2013-06-18 13:14:46 +0400
  * Merging [MDEV-4635](https://jira.mariadb.org/browse/MDEV-4635) from 5.3.
  * [Revision #2502.567.106](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.106)\
    Mon 2013-06-17 19:25:55 +0400
    * [MDEV-4635](https://jira.mariadb.org/browse/MDEV-4635) Crash in UNIX\_TIMESTAMP(STR\_TO\_DATE('2020','%Y'))
* [Revision #3334.1.481](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.481)\
  Mon 2013-06-17 19:18:14 +0200
  * [MDEV-4503](https://jira.mariadb.org/browse/MDEV-4503) : Installation fails if TEMP directory contains "" subdirectory.
* [Revision #3334.1.480](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.480)\
  Mon 2013-06-17 17:58:53 +0200
  * unit test case for [MDEV-4576](https://jira.mariadb.org/browse/MDEV-4576)
* [Revision #3334.1.479](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.479)\
  Sun 2013-06-16 22:13:26 +0200
  * [MDEV-4576](https://jira.mariadb.org/browse/MDEV-4576) : Aria storage engine's temporary files might not be deleted (Errcode : 13) See also MySQL Bug #39750 and similar ones.
* [Revision #3334.1.478](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.478)\
  Sat 2013-06-15 14:22:03 +0200
  * [MDEV-4601](https://jira.mariadb.org/browse/MDEV-4601) : Allow MariaDB to be build without non-blocking client.
* [Revision #3334.1.477](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.477) \[merge]\
  Mon 2013-06-17 20:33:36 +0300
  * 5.3 -> 5.5 Merge
  * [Revision #2502.567.105](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.105)\
    Mon 2013-06-17 17:04:51 +0400
    * [MDEV-4651](https://jira.mariadb.org/browse/MDEV-4651) Crash in my\_decimal2decimal in a ORDER BY query
  * [Revision #2502.567.104](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.104)\
    Thu 2013-06-06 23:33:40 +0300
    * [MDEV-4593](https://jira.mariadb.org/browse/MDEV-4593): p\_s: crash in simplify\_joins with delete using subselect from view
* [Revision #3334.1.476](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.476)\
  Sat 2013-06-15 16:02:43 +0200
  * [MDEV-4466](https://jira.mariadb.org/browse/MDEV-4466) Partitioned Aria table created by a previous version is recognized as TEST\_SQL\_DISCOVERY
* [Revision #3334.1.475](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.475)\
  Fri 2013-06-14 14:04:58 +0200
  * [MDEV-4006](https://jira.mariadb.org/browse/MDEV-4006) mysql\_plugin.1 is removed from source which is not necessary
* [Revision #3334.1.474](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.474)\
  Thu 2013-06-13 20:19:32 +0200
  * [MDEV-4578](https://jira.mariadb.org/browse/MDEV-4578) information\_schema.processlist reports incorrect value for Time (2147483647)
* [Revision #3334.1.473](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.473)\
  Thu 2013-06-13 20:19:11 +0200
  * [MDEV-4529](https://jira.mariadb.org/browse/MDEV-4529) Assertion \`tmp->state == 4' fails on mix of INSTALL SONAME / UNINSTALL PLUGIN
* [Revision #3334.1.472](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.472)\
  Thu 2013-06-13 20:18:40 +0200
  * [MDEV-4519](https://jira.mariadb.org/browse/MDEV-4519) SHOW EVENTS and SHOW PROCEDURE STATUS truncate long user names
* [Revision #3334.1.471](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.471)\
  Thu 2013-06-13 15:33:02 +0200
  * [MDEV-4515](https://jira.mariadb.org/browse/MDEV-4515) Long user names are truncated to 48 symbols in error messages
* [Revision #3334.1.470](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.470)\
  Thu 2013-06-13 15:13:13 +0200
  * [MDEV-4444](https://jira.mariadb.org/browse/MDEV-4444) Server crashes with "safe\_mutex: Trying to destroy a mutex share->mutex that was locked" on attempt to recover an archive table
* [Revision #3334.1.469](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.469)\
  Thu 2013-06-13 14:32:57 +0200
  * [MDEV-703](https://jira.mariadb.org/browse/MDEV-703) [Bug #870310](https://bugs.launchpad.net/bugs/870310) - killall -9 in init-script
* [Revision #3334.1.468](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.468)\
  Thu 2013-06-13 14:14:47 +0200
  * [MDEV-4573](https://jira.mariadb.org/browse/MDEV-4573) UNINSTALL PLUGIN misleading error message for non-dynamic plugins
* [Revision #3334.1.467](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.467)\
  Thu 2013-06-13 00:13:23 +0200
  * [MDEV-4614](https://jira.mariadb.org/browse/MDEV-4614) Man pages fixes
* [Revision #3334.1.466](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.466)\
  Wed 2013-06-12 22:12:09 +0200
  * [MDEV-4604](https://jira.mariadb.org/browse/MDEV-4604) Wrong server status when sending out parameters
* [Revision #3334.1.465](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.465)\
  Wed 2013-06-12 20:38:22 +0200
  * [MDEV-4509](https://jira.mariadb.org/browse/MDEV-4509) mysql init script should accept arguments
* [Revision #3334.1.464](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.464)\
  Wed 2013-06-12 20:29:19 +0200
  * [MDEV-4422](https://jira.mariadb.org/browse/MDEV-4422) SHOW PROCESSLIST reference to THD::db not protected against simultaneous updates
* [Revision #3334.1.463](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.463)\
  Tue 2013-06-11 12:53:35 +0200
  * [MDEV-4636](https://jira.mariadb.org/browse/MDEV-4636) use mysql\_cleartext\_plugin from auth\_pam
* [Revision #3334.1.462](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.462)\
  Tue 2013-06-11 11:11:05 +0200
  * [MDEV-4574](https://jira.mariadb.org/browse/MDEV-4574) Missing connection option MYSQL\_ENABLE\_CLEARTEXT\_PLUGIN
* [Revision #3334.1.461](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.461)\
  Mon 2013-06-10 21:45:30 +0200
  * [MDEV-4297](https://jira.mariadb.org/browse/MDEV-4297) `mysql --binary-mode`
* [Revision #3334.1.460](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.460)\
  Wed 2013-06-12 05:09:28 +0400
  * [MDEV-4629](https://jira.mariadb.org/browse/MDEV-4629) MTR tests main.variables and some of sys\_vars.\* fail on 32-bit builds
* [Revision #3334.1.459](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.459)\
  Tue 2013-06-11 13:49:43 +0300
  * Fixed tests that failed on 32 bit because of my earlier fixes of 32 bit limits.
* [Revision #3334.1.458](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.458)\
  Fri 2013-06-07 15:35:13 +0200
  * [MDEV-4468](https://jira.mariadb.org/browse/MDEV-4468) Assertion \`error != 0' fails or timeout occurs on select from a FEDERATED table which points at a non-existent table
* [Revision #3334.1.457](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.457)\
  Fri 2013-06-07 15:34:59 +0200
  * [MDEV-4480](https://jira.mariadb.org/browse/MDEV-4480) Assertion \`inited == NONE' fails on closing a connection with open handler on temporary table
* [Revision #3334.1.456](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.456)\
  Fri 2013-06-07 10:02:50 +0200
  * [MDEV-4564](https://jira.mariadb.org/browse/MDEV-4564) ALTER on a temporary table generates an audit event
* [Revision #3334.1.455](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.455)\
  Sun 2013-06-09 13:26:10 +0300\
  \*
  * Added -Wno-uninitialized to avoid warnings in release builds (uninitalized variables are detected by DBUG builds) - Fixed wrong declaration which cased compile failure on 32 bit
* [Revision #3334.1.454](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.454)\
  Thu 2013-06-06 15:14:23 +0300
  * Fixed some cache variables that could be set to higher value than what the code supported (size\_t) Fixed some cases that didn't work with > 4G buffers. Fixed compiler warnings
* [Revision #3334.1.453](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.453)\
  Wed 2013-06-05 23:53:35 +0300
  * -Run test suite with smaller aria keybuffer size (to make it possible to run more tests in parallel) -Added test and extra code to ensure we don't leave keyread on for a handler table. -Create on disk temporary files always with long data pointers if SQL\_SMALL\_RESULT is not used. This ensures that we can handle temporary files bigger than 4G.
* [Revision #3334.1.452](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.452)\
  Sat 2013-06-01 21:33:26 +0200
  * Fix a compile warning on NetBSD
* [Revision #3334.1.451](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.451)\
  Sat 2013-06-01 21:30:33 +0200
  * [MDEV-4607](https://jira.mariadb.org/browse/MDEV-4607) : libreadline-related compilation problems on NetBSD.
* [Revision #3334.1.450](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.450)\
  Thu 2013-05-30 08:23:49 +0300
  * [MDEV-4520](https://jira.mariadb.org/browse/MDEV-4520): Assertion \`0' fails in Query\_cache::end\_of\_result on concurrent drop event and event executio
* [Revision #3334.1.449](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.449)\
  Tue 2013-05-28 21:25:59 +0200
  * followup for revision 3751 "centos5 gcc 4.1 asm bug" remove the workaround from cmake/os/FreeBSD.cmake
* [Revision #3334.1.448](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.448)\
  Thu 2013-05-23 17:05:31 +0300
  * [MDEV-4520](https://jira.mariadb.org/browse/MDEV-4520): Assertion \`0' fails in Query\_cache::end\_of\_result on concurrent drop event and event execution
* [Revision #3334.1.447](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.447)\
  Wed 2013-05-22 16:44:44 +0200
  * [MDEV-4548](https://jira.mariadb.org/browse/MDEV-4548) - compile sphinx.so/dll and include into packages
* [Revision #3334.1.446](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.446)\
  Mon 2013-05-27 16:35:42 +0200
  * [MDEV-4553](https://jira.mariadb.org/browse/MDEV-4553) - Fixes for compilation under NetBSD.
* [Revision #3334.1.445](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.445)\
  Fri 2013-05-24 14:33:04 +0200
  * [MDEV-4516](https://jira.mariadb.org/browse/MDEV-4516) SELECT from I\_S.QUERY\_CACHE\_INFO produces ER\_UNKNOWN\_ERROR when query cache size is 0
* [Revision #3411](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3411)\
  Wed 2013-08-07 00:17:16 +0300
  * Merged FreeBSD compatibility changes (up to revision 3893 in lp:codership/codership-mysql/5.5-23)
* [Revision #3410](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3410)\
  Mon 2013-08-05 18:01:05 +0300
  * References [Bug #1208493](https://bugs.launchpad.net/bugs/1208493) [MDEV-4830](https://jira.mariadb.org/browse/MDEV-4830) Enabling slave applier thread to send COND\_thread\_count
* [Revision #3409](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3409)\
  Thu 2013-06-20 21:51:11 +0300
  * References [Bug #1193079](https://bugs.launchpad.net/bugs/1193079) - bumped wsrep version to 7.5
* [Revision #3408](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3408)\
  Wed 2013-06-19 10:35:40 +0300
  * References [Bug #1191778](https://bugs.launchpad.net/bugs/1191778) - merged xtrabackup SST fixes from PXC
* [Revision #3407](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3407)\
  Sun 2013-06-16 20:38:02 +0300
  * References [Bug #1134892](https://bugs.launchpad.net/bugs/1134892) - WSREP\_DEBUG\_PRINT was left on by mistake
* [Revision #3406](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3406)\
  Sat 2013-06-15 16:16:38 +0300
  * References [Bug #1087368](https://bugs.launchpad.net/bugs/1087368) - merged fix from wsrep-5.5 branch. Note this is compatible only with new wsrep provider #23 libraries, which understand 'bootstrap' address in connecting.
* [Revision #3405](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3405)\
  Sat 2013-06-15 16:15:45 +0300
  * References: [MDEV-4572](https://jira.mariadb.org/browse/MDEV-4572) - merge with lp:codership-mysql/5.5-23 revisions 3874..3878
* [Revision #3404](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3404)\
  Sat 2013-06-15 16:15:17 +0300
  * References [Bug #1108035](https://bugs.launchpad.net/bugs/1108035) - merged fix from [394](https://bazaar.launchpad.net/~percona-core/percona-xtradb-cluster/release-5.5.31/revision/394)
* [Revision #3403](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3403)\
  Fri 2013-06-14 22:01:18 +0500
  * [MDEV-4656](https://jira.mariadb.org/browse/MDEV-4656) MariaDB-Galera deb packages cannot be built, expected files are missing.
* [Revision #3402](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3402)\
  Thu 2013-06-13 10:22:37 +0300
  * References: [Bug #1182441](https://bugs.launchpad.net/bugs/1182441) - merged fix from revision: [416](https://bazaar.launchpad.net/~percona-core/percona-xtradb-cluster/release-5.5.31/revision/416)
* [Revision #3401](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3401)\
  Thu 2013-06-13 09:55:28 +0300
  * References [Bug #1169326](https://bugs.launchpad.net/bugs/1169326) - merged fix from LP wsrep-5.5-23 Now at revision 3874 in lp:codership/codership-mysql/5.5-23
* [Revision #3400](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3400)\
  Thu 2013-06-13 09:49:48 +0300
  * References: [Bug #1134892](https://bugs.launchpad.net/bugs/1134892) [MDEV-4624](https://jira.mariadb.org/browse/MDEV-4624) - merged fix from LP wsrep-5.5-23
* [Revision #3399](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3399)\
  Thu 2013-06-13 09:44:34 +0300
  * References: [Bug #1187526](https://bugs.launchpad.net/bugs/1187526) - merged fix from wsrep-5.5-23
* [Revision #3398](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3398)\
  Wed 2013-06-12 17:07:48 +0500
  * [MDEV-4600](https://jira.mariadb.org/browse/MDEV-4600) mariadb-galera-server-5.5 on ubuntu has no dependency to galera while debian has. dependency on galera added to the Ubuntu packaging script.
* [Revision #3397](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3397)\
  Mon 2013-05-27 23:03:08 +0300
  * References: [MDEV-3924](https://jira.mariadb.org/browse/MDEV-3924) [Bug #1088267](https://bugs.launchpad.net/bugs/1088267) - merged fix from lp:codership-mysql
* [Revision #3396](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3396)\
  Mon 2013-05-27 22:51:22 +0300
  * References [Bug #1012138](https://bugs.launchpad.net/bugs/1012138) - merged fix from lp:codership-mysql
* [Revision #3395](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3395) \[merge]\
  Sun 2013-05-26 11:26:58 +0300
  * References: [MDEV-4572](https://jira.mariadb.org/browse/MDEV-4572) - merge with [mariaDB 5.5.31](../../release-notes-mariadb-5-5-series/mariadb-5531-release-notes.md) bzr merge lp:maria/5.5 -rtag:mariadb-5.5.31
  * [Revision #3334.1.444](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.444)\
    Tue 2013-05-21 18:56:35 +0200
    * fix for compiled-in FederatedX
  * [Revision #3334.1.443](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.443)\
    Tue 2013-05-21 13:03:37 +0200
    * [MDEV-388](https://jira.mariadb.org/browse/MDEV-388) Creating a federated table with a non-existing server returns a random error code (part 2)
  * [Revision #3334.1.442](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.442) \[merge]\
    Tue 2013-05-21 09:43:34 +0200
    * 5.3 merge
    * [Revision #2502.567.103](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.103)\
      Tue 2013-05-21 09:42:10 +0200
      * fixes for buildbot
  * [Revision #3334.1.441](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.441)\
    Mon 2013-05-20 23:58:44 +0200
    * [MDEV-388](https://jira.mariadb.org/browse/MDEV-388) Creating a federated table with a non-existing server returns a random error code
  * [Revision #3334.1.440](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.440)\
    Mon 2013-05-20 13:41:03 +0200
    * increase MAX\_HA (number of simultaneously installed storage engines) to 64
  * [Revision #3334.1.439](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.439) \[merge]\
    Mon 2013-05-20 12:36:30 +0200
    * 5.3 merge. change maria.distinct to use a function that doesn't require ssl-enabled builds
    * [Revision #2502.567.102](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.102) \[merge]\
      Mon 2013-05-20 11:13:07 +0200
      * 5.2 merge
      * [Revision #2502.566.49](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.49) \[merge]\
        Mon 2013-05-20 10:53:04 +0200
        * 5.1 merge
        * [Revision #2502.565.49](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.49)\
          Sat 2013-05-11 20:23:57 +0300
          * Fixed compiler failure on solaris
        * [Revision #2502.565.48](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.48)\
          Sat 2013-05-11 18:57:06 +0300
          * Fixed compiler warning
        * [Revision #2502.565.47](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.47)\
          Sat 2013-05-11 15:55:11 +0300
          * [MDEV-4280](https://jira.mariadb.org/browse/MDEV-4280): Assertion \`empty\_size == empty\_size\_on\_page' failure in ma\_blockrec.c or ER\_NOT\_KEYFILE on query with DISTINCT and GROUP BY This could happen when using Aria for internal temporary files (default case) and using DISTINCT. \_ma\_scan\_restore\_block\_record() didn't work correctly if there was rows inserted, updated or deleted on the handler between calls to \_ma\_scan\_remember\_block\_record() and \_ma\_scan\_restore\_block\_record(). The effect was that some DISTINCT queries that used remove\_dup\_with\_compare() could fail.
        * [Revision #2502.565.46](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.46)\
          Tue 2013-04-09 09:58:51 +0300
          * [MDEV-4326](https://jira.mariadb.org/browse/MDEV-4326) fix.
      * [Revision #2502.566.48](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.48)\
        Sun 2013-05-19 16:38:56 +0200
        * [MDEV-4544](https://jira.mariadb.org/browse/MDEV-4544) - update MSI to include HeidiSQL 8.0
      * [Revision #2502.566.47](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.47)\
        Sun 2013-05-19 16:22:33 +0200
        * Fix cpack error - safe\_process.pl does not exist anymore.
      * [Revision #2502.566.46](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.46)\
        Wed 2013-05-08 14:32:32 +0200
        * [MDEV-4462](https://jira.mariadb.org/browse/MDEV-4462) mysqld gets SIGFPE when mysql.user table is empty
    * [Revision #2502.567.101](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.101)\
      Fri 2013-05-03 16:07:13 +0300
      * [MDEV-4290](https://jira.mariadb.org/browse/MDEV-4290): Fix agregate function resolution in derived tables (no name resolution over a derived table border)
    * [Revision #2502.567.100](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.100) \[merge]\
      Sun 2013-05-05 05:32:55 +0400
      * Merge
  * [Revision #3334.1.438](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.438)\
    Sun 2013-05-19 17:42:30 +0200
    * remove start menu shortcut to upgrade wizard
  * [Revision #3334.1.437](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.437)\
    Sun 2013-05-19 17:41:22 +0200
    * [MDEV-4544](https://jira.mariadb.org/browse/MDEV-4544) : Update MSI installer to use latest HeidiSQL 8.0
  * [Revision #3334.1.436](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.436)\
    Fri 2013-05-17 10:16:56 +0400
    * Bug#[MDEV-4518](https://jira.mariadb.org/browse/MDEV-4518) Server crashes in is\_white\_space when it's run with query cache, charset ucs2 and collation ucs2\_unicode\_ci
  * [Revision #3334.1.435](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.435)\
    Wed 2013-05-15 16:28:12 +0300\
    \*
    * Solaris fixes: - Fixed that wait\_timeout\_func and wait\_timeout tests works on solaris - We have to compile without NO\_ALARM on Solaris as Solaris doesn't support timeouts on sockets with setsockopt(.. SO\_RCVTIMEO). - Fixed that compile-solaris-amd64-debug works (before that we got a wrong ELF class: ELFCLASS64 on linkage) - Fixed some compiler warnings - Fixed some failing tests
  * [Revision #3334.1.434](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.434)\
    Wed 2013-05-15 02:36:37 +0500
    * [MDEV-4266](https://jira.mariadb.org/browse/MDEV-4266) Server upgrade via apt-get install does not work. Now empty 'highlevel' packages strictly depend on the same versions of files. These are mariadb-server, mariadb-client, mariadb-test
  * [Revision #3334.1.433](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.433)\
    Wed 2013-05-15 02:33:29 +0500
    * [MDEV-4521](https://jira.mariadb.org/browse/MDEV-4521) MBRContains, MBRWithin no longer work with geometries of different type. get\_mm\_leaf function can store all sorts of spatial features in one type of field it receives from an Item\_field. So we just allow that by setting the type of this field to GEOMETRY.
  * [Revision #3334.1.432](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.432)\
    Tue 2013-05-14 18:32:16 +0300
    * When one does 'REPAIR TABLE', update uuid() to the current system
  * [Revision #3334.1.431](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.431)\
    Tue 2013-05-14 14:49:52 +0200
    * Fix test failure in plugins.unix\_socket when running tests as user root.
  * [Revision #3334.1.430](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.430)\
    Mon 2013-05-13 16:11:39 +0200
    * [MDEV-4514](https://jira.mariadb.org/browse/MDEV-4514) After increasing user name length mysql.db is reported broken and event scheduler does not start
  * [Revision #3334.1.429](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.429)\
    Mon 2013-05-13 15:49:48 +0200
    * [MDEV-4505](https://jira.mariadb.org/browse/MDEV-4505) Buffer overrun when processing `--log-bin` parameter without file name
  * [Revision #3334.1.428](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.428)\
    Mon 2013-05-13 15:49:27 +0200
    * [MDEV-4199](https://jira.mariadb.org/browse/MDEV-4199) Installing postfix on CentOS 5.9 requires MariaDB-server
  * [Revision #3334.1.427](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.427)\
    Mon 2013-05-13 15:46:58 +0200
    * fix test cases
  * [Revision #3334.1.426](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.426)\
    Mon 2013-05-13 00:43:46 +0300
    * Fixed [MDEV-4291](https://jira.mariadb.org/browse/MDEV-4291): Assertion \`trid >= info->s->state.create\_trid' failure or data corruption (key points to record outside datafile) on INSERT into an Aria table.
  * [Revision #3334.1.425](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.425)\
    Sun 2013-05-12 11:29:16 +0300
    * [MDEV-3999](https://jira.mariadb.org/browse/MDEV-3999): Valgrind errors 'invalid write' or assorted server crashes on concurrent flow with partitioned Aria tables [MDEV-3989](https://jira.mariadb.org/browse/MDEV-3989): Server crashes on import from MariaDB mysqldump export with partitioned Aria table.
  * [Revision #3334.1.424](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.424)\
    Sat 2013-05-11 20:31:50 +0300
    * Fixed that SHOW PROCESSLIST and information\_schema.processlist uses the right length for user names. Fixed some failing tests
  * [Revision #3334.1.423](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.423)\
    Sat 2013-05-11 12:20:21 +0300
    * [MDEV-4231](https://jira.mariadb.org/browse/MDEV-4231): Possible bug in function \_ma\_apply\_undo\_row\_insert() Added comment to clearify the code.
  * [Revision #3334.1.422](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.422)\
    Thu 2013-05-09 23:25:57 +0200
    * Fix compile error
  * [Revision #3334.1.421](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.421)\
    Thu 2013-05-09 22:21:07 +0200
    * Small mysql\_install\_db.exe fixes - Use lc-messages-dir instead of deprecated `--language` when running mysqld in bootstrap mode. - Add some verbosity to mysql\_install\_db.exe when it runs in course of MSI installation.
  * [Revision #3334.1.420](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.420)\
    Wed 2013-05-08 20:37:17 +0200
    * [MDEV-4206](https://jira.mariadb.org/browse/MDEV-4206) : log all slow statements (do not use filters), if log\_slow\_filter is empty.
  * [Revision #3334.1.419](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.419)\
    Wed 2013-05-08 13:36:17 +0400
    * The bug [MDEV-4489](https://jira.mariadb.org/browse/MDEV-4489) "Replication of big5, cp932, gbk, sjis strings makes wrong values on slave" has been fixed.
  * [Revision #3334.1.418](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.418) \[merge]\
    Wed 2013-05-08 10:12:21 +0200
    * Merge with XtraDB as of Percona-Server-5.5.30-rel30.2
    * [Revision #0.12.62](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/0.12.62)\
      Wed 2013-05-08 09:52:54 +0200
      * Percona-Server-5.5.30-rel30.2.tar.gz
  * [Revision #3334.1.417](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.417)\
    Tue 2013-05-07 18:28:36 +0200
    * centos5 gcc 4.1 asm bug
  * [Revision #3334.1.416](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.416)\
    Tue 2013-05-07 18:26:22 +0200
    * Compilation warnings. openssl compilation problem.
  * [Revision #3334.1.415](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.415) \[merge]\
    Tue 2013-05-07 13:05:09 +0200
    * mysql-5.5.31 merge
    * [Revision #3077.184.104](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.104)\
      Fri 2013-04-12 12:11:38 +0200
      * Updated mysql.spec.sh for rpm-uln
    * [Revision #3077.184.103](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.103)\
      Mon 2013-03-25 13:50:21 +0100
      * Reverted MySQL Release Engineering mail address
    * [Revision #3077.184.102](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.102)\
      Thu 2013-03-21 14:59:57 +0100
      * Added SuSE RPM Build fix
    * [Revision #3077.184.101](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.101)\
      Fri 2013-03-08 15:51:20 +0530
    * [Revision #3077.184.100](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.100) \[merge]\
      Wed 2013-03-06 17:05:32 +0100
      * Added fix for Bug#16445097
      * [Revision #3077.175.120](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.120)\
        Wed 2013-03-06 16:33:26 +0100
        * Added fix for Bug#16445097
    * [Revision #3077.184.99](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.99) \[merge]\
      Tue 2013-03-05 16:34:14 +0100
      * Updated Code for Bug#16235828 and Bug#16298542
      * [Revision #3077.175.119](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.119)\
        Tue 2013-03-05 16:16:34 +0100
        * Updated Code for Bug#16235828
      * [Revision #3077.175.118](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.118)\
        Fri 2013-03-01 14:11:24 +0100
        * Updated mysql.spec.sh file for br16298542
      * [Revision #3077.175.117](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.117)\
        Thu 2013-02-28 14:49:54 +0100
        * Updated release number in mysql.spec.sh file for br16298542
      * [Revision #3077.175.116](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.116)\
        Thu 2013-02-28 14:36:00 +0100
        * Updated mysql.spec.sh file for br16298542
    * [Revision #3077.184.98](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.98) \[merge]\
      Fri 2013-03-01 12:10:09 +0100
      * L0ocal merge
      * [Revision #3077.186.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.186.2)\
        Fri 2013-03-01 15:01:32 +0530
        * BUG#11753923-SQL THREAD CRASHES ON DISK FULL Fixing post push issue Simulator name used needs to be changed to make it work properly.
      * [Revision #3077.186.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.186.1)\
        Thu 2013-02-28 14:52:47 +0100
        * Bug#16385711: HANDLER, CREATE TABLE IF NOT EXISTS, PROBLEM AFTER MYSQL\_HA\_FIND
    * [Revision #3077.184.97](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.97)\
      Thu 2013-02-28 13:19:15 +0100
      * Bug#16414644 ASSERTION FAILED: SIZE == PFS\_ALLOCATED\_MEMORY
    * [Revision #3077.184.96](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.96)\
      Thu 2013-02-28 14:50:42 +0530
    * [Revision #3077.184.95](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.95) \[merge]\
      Thu 2013-02-28 09:54:27 +0530
      * [Revision #2661.844.52](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.52) \[merge]\
        Thu 2013-02-28 09:52:55 +0530
        * [Revision #2661.847.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.847.1)\
          Fri 2012-09-14 19:19:21 +0530
    * [Revision #3077.184.94](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.94) \[merge]\
      Thu 2013-02-28 01:33:00 +0400
      * Manual up-merge (16311231 backport)
      * [Revision #2661.844.51](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.51)\
        Wed 2013-02-27 23:21:34 +0400
        * Bug #16311231: MISSING DATA ON SUBQUERY WITH WHERE + XOR IN IN-CLAUSE USING MYISAM OR MEMORY ENGINE
    * [Revision #3077.184.93](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.93)\
      Wed 2013-02-27 12:44:58 -0600
      * Bug #16305265 HANG IN RENAME TABLE
    * [Revision #3077.184.92](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.92) \[merge]\
      Wed 2013-02-27 10:04:43 +0200
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.844.50](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.50)\
        Wed 2013-02-27 10:00:50 +0200
        * Bug#16400920 INNODB TRIES TO PASS EMPTY BUFFER TO ZLIB, GETS Z\_BUF\_ERROR
    * [Revision #3077.184.91](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.91) \[merge]\
      Tue 2013-02-26 21:29:43 +0530
      * Bug#16372927: STACK OVERFLOW WITH LONG DATABASE NAME IN GRANT STATEMENT
      * [Revision #2661.844.49](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.49)\
        Tue 2013-02-26 21:23:06 +0530
        * Bug#16372927: STACK OVERFLOW WITH LONG DATABASE NAME IN GRANT STATEMENT
    * [Revision #3077.184.90](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.90)\
      Mon 2013-02-25 10:42:40 +0100
      * Bug#16062056 REMOVE THE "DUMMY.BAK" FILE FROM THE TEST DATABASE, AND ADD DB.OPT
    * [Revision #3077.184.89](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.89)\
      Tue 2013-02-26 17:57:05 +0530
      * Bug#14653504 CRASH WHEN TRUNCATING PARTITIONS FROM A VIEW!
    * [Revision #3077.184.88](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.88) \[merge]\
      Tue 2013-02-26 06:35:17 +0100
      * Updated/added copyright headers
      * [Revision #2661.844.48](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.48)\
        Mon 2013-02-25 15:26:00 +0100
        * Updated/added copyright headers.
    * [Revision #3077.184.87](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.87)\
      Mon 2013-02-25 19:37:46 +0530
      * Bug#16103072 TEST MYSQL\_PLUGIN USES UNSAFE WRITE\_FILE TO WRITE TO EXPECT FILE
    * [Revision #3077.184.86](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.86)\
      Mon 2013-02-25 13:45:00 +0100
    * [Revision #3077.184.85](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.85)\
      Mon 2013-02-25 10:28:25 +0530
      * Bug #16044655 CRASH: SETTING DEFAULT VALUE FOR SOME VARIABLES
    * [Revision #3077.184.84](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.84) \[merge]\
      Sat 2013-02-23 10:47:30 +0100
      * Upmerging the changes from 5.1 for copyright changes.
      * [Revision #2661.844.47](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.47)\
        Sat 2013-02-23 10:38:28 +0100
    * [Revision #3077.184.83](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.83)\
      Sat 2013-02-23 10:40:23 +0100
    * [Revision #3077.184.82](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.82)\
      Sat 2013-02-23 00:16:36 +0530
      * Testcase fix for Bug#14147491
    * [Revision #3077.184.81](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.81)\
      Fri 2013-02-22 15:22:15 +0100
      * Bug #13619394 - MAKE TEST FAILS ON MY\_VSNPRINTF
    * [Revision #3077.184.80](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.80) \[merge]\
      Fri 2013-02-22 12:32:29 +0100
      * merge
      * [Revision #3077.185.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.185.1)\
        Wed 2013-02-20 12:41:43 +0100
        * Bug #13071597: MYSQL SERVER COMMUNITY TO ADVANCED USING MSI THE INSTALLER
    * [Revision #3077.184.79](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.79) \[merge]\
      Fri 2013-02-22 15:15:14 +0530
      * Merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.844.46](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.46)\
        Fri 2013-02-22 14:56:17 +0530
        * Bug #14211565 CRASH WHEN ATTEMPTING TO SET SYSTEM VARIABLE TO RESULT OF VALUES()
    * [Revision #3077.184.78](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.78)\
      Wed 2013-02-20 11:24:16 +0100
      * Bug#14300733 CMAKE DOES NOT CHECK FOR ZLIB VERSION
    * [Revision #3077.184.77](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.77)\
      Thu 2013-02-21 12:16:59 +0530
      * Testcase fix for Bug#14147491
    * [Revision #3077.184.76](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.76)\
      Wed 2013-02-20 18:25:18 +0530
      * Testcase fix for BUG#14147491
    * [Revision #3077.184.75](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.75) \[merge]\
      Tue 2013-02-19 14:36:30 +0530
      * Merge from mysq-5.1 to mysql-5.5
      * [Revision #2661.844.45](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.45)\
        Tue 2013-02-19 14:31:11 +0530
        * Bug#11746817:MYSQL\_INSTALL\_DB CREATES WILDCARD GRANTS WHEN HOST HAS '\_' IN THE HOSTNAME
    * [Revision #3077.184.74](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.74) \[merge]\
      Tue 2013-02-19 12:19:10 +0530
      * Bug#16235681: TURN OFF DEFAULT COMPRESSION WHILE USING OPENSSL
      * [Revision #2661.844.44](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.44)\
        Tue 2013-02-19 12:17:31 +0530
        * Bug#16235681: TURN OFF DEFAULT COMPRESSION WHILE USING OPENSSL
    * [Revision #3077.184.73](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.73) \[merge]\
      Tue 2013-02-19 10:59:45 +0530
      * Null merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.844.43](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.43)\
        Tue 2013-02-19 10:55:55 +0530
    * [Revision #3077.184.72](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.72)\
      Tue 2013-02-19 01:58:57 +0530
      * BUG#15965353- RPL.RPL\_ROW\_UNTIL FAILS ON PB2, PLATFORM= MACOSX10.6 X86\_64 MAX
    * [Revision #3077.184.71](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.71) \[merge]\
      Mon 2013-02-18 17:06:00 +0000
      * BUG#13545447: RPL\_ROTATE\_LOGS FAILS DUE TO CONCURRENCY ISSUES IN REP. CODE
      * [Revision #2661.844.42](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.42)\
        Mon 2013-02-18 17:02:26 +0000
        * BUG#13545447: RPL\_ROTATE\_LOGS FAILS DUE TO CONCURRENCY ISSUES IN REP. CODE
    * [Revision #3077.184.70](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.70)\
      Mon 2013-02-18 19:13:06 +0530
      * Bug #12546953 "SHOW VARIABLES LIKE 'DATADIR';" RETURN EMPTY. Problem: =========================================================== If mysqld daemon is started without a `--datadir` option option, and we issue the SHOW VARIABLES LIKE 'DATADIR';SQL command at the client it returns an empty path. This is because mysql\_real\_data\_home\_ptr is being reset to NULL by Sys\_var\_charptr constructor call when the datadir is not given either through configuration file (no-defaults) or through mysqld parameters.
    * [Revision #3077.184.69](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.69)\
      Mon 2013-02-18 11:12:24 +0100
      * BUG#13545447: RPL\_ROTATE\_LOGS FAILS DUE TO CONCURRENCY ISSUES IN REP. CODE Post-push fix, broken build: sql/rpl\_master.cc:1049:70: error: converting ‘false’ to pointer type ‘bool\*’ \[-Werror=conversion-null]
    * [Revision #3077.184.68](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.68)\
      Mon 2013-02-18 11:13:48 +0530
    * [Revision #3077.184.67](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.67) \[merge]\
      Sun 2013-02-17 01:45:10 +0530
      * BUG#15965353- RPL.RPL\_ROW\_UNTIL FAILS ON PB2, PLATFORM= MACOSX10.6 X86\_64 MAX
      * [Revision #2661.844.41](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.41)\
        Sun 2013-02-17 01:42:28 +0530
        * BUG#15965353- RPL.RPL\_ROW\_UNTIL FAILS ON PB2, PLATFORM= MACOSX10.6 X86\_64 MAX
    * [Revision #3077.184.66](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.66) \[merge]\
      Fri 2013-02-15 22:18:37 +0000
      * BUG#13545447: RPL\_ROTATE\_LOGS FAILS DUE TO CONCURRENCY ISSUES IN REP. CODE
      * [Revision #2661.844.40](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.40)\
        Fri 2013-02-15 21:57:35 +0000
        * BUG#13545447: RPL\_ROTATE\_LOGS FAILS DUE TO CONCURRENCY ISSUES IN REP. CODE
    * [Revision #3077.184.65](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.65)\
      Fri 2013-02-15 16:01:37 +0400
      * Bug#16056537: MYSQLD CRASHES IN ITEM\_FUNC\_GET\_USER\_VAR::FIX\_LENGTH\_AND\_DEC()
    * [Revision #3077.184.64](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.64) \[merge]\
      Fri 2013-02-15 12:37:21 +0530
      * Bug#16218104: MYSQL YASSL - LUCKY THIRTEEN: BREAKING THE TLS AND DTLS RECORD PROTOCOLS
      * [Revision #2661.844.39](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.39)\
        Fri 2013-02-15 12:35:54 +0530
        * Bug#16218104: MYSQL YASSL - LUCKY THIRTEEN: BREAKING THE TLS AND DTLS RECORD PROTOCOLS
    * [Revision #3077.184.63](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.63) \[merge]\
      Fri 2013-02-15 00:40:32 +0530
      * BUG#12359942- REPLICATION TEST FROM ENGINE SUITE RPL\_ROW\_UNTIL TIMES OUT
      * [Revision #2661.844.38](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.38)\
        Fri 2013-02-15 00:38:42 +0530
        * BUG#12359942- REPLICATION TEST FROM ENGINE SUITE RPL\_ROW\_UNTIL TIMES OUT
    * [Revision #3077.184.62](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.62)\
      Thu 2013-02-14 17:03:49 +0100
      * Bug#16274455: CAN NOT ACESS PARTITIONED TABLES WHEN DOWNGRADED FROM 5.6.11 TO 5.6.10
    * [Revision #3077.184.61](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.61) \[merge]\
      Thu 2013-02-14 16:35:40 +0530
      * Merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.844.37](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.37)\
        Thu 2013-02-14 16:33:31 +0530
        * For the error code ER\_TOO\_LONG\_IDENT, the identifier is expected in the my\_error call. So removing this line from here.
    * [Revision #3077.184.60](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.60) \[merge]\
      Tue 2013-02-12 15:35:56 +0530
      * Merge from mysql-5.1 to mysql-5.5.
      * [Revision #2661.844.36](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.36)\
        Tue 2013-02-12 14:52:48 +0530
        * Bug #11753153 INNODB GENERATES SYMBOLS THAT ARE TOO LONG, INVALID DDL FROM SHOW CREATE
    * [Revision #3077.184.59](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.59)\
      Mon 2013-02-04 14:09:48 +0100
      * post-push test result update for bug#14521864.
    * [Revision #3077.184.58](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.58) \[merge]\
      Fri 2013-02-08 16:36:47 +0530
      * BUG#16247322-MTR NOT RUNNING SYS\_VARS TEST SUITE FOR 5.1 Null merge from mysql-5.1
      * [Revision #2661.844.35](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.35)\
        Fri 2013-02-08 16:34:32 +0530
        * BUG#16247322-MTR NOT RUNNING SYS\_VARS TEST SUITE FOR 5.1
    * [Revision #3077.184.57](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.57) \[merge]\
      Fri 2013-02-08 15:42:36 +0530
      * BUG#16247322-MTR NOT RUNNING SYS\_VARS TEST SUITE FOR 5.1 Null merge from mysql-5.1
      * [Revision #2661.844.34](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.34)\
        Fri 2013-02-08 15:41:18 +0530
        * BUG#16247322-MTR NOT RUNNING SYS\_VARS TEST SUITE FOR 5.1
    * [Revision #3077.184.56](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.56) \[merge]\
      Fri 2013-02-08 09:33:21 +0200
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.844.33](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.33)\
        Fri 2013-02-08 09:23:12 +0200
        * Add missing linkage specifiers, so that ha\_innodb\_plugin.so will not export internal symbols.
      * [Revision #2661.844.32](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.32)\
        Fri 2013-02-08 09:22:46 +0200
        * Bug#16292043 RACE CONDITION IN SRV\_EXPORT\_INNODB\_STATUS() WHEN ACCESSING PURGE\_SYS->VIEW
    * [Revision #3077.184.55](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.55) \[merge]\
      Thu 2013-02-07 19:46:45 +0200
      * Null-merge from mysql-5.1
      * [Revision #2661.844.31](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.31)\
        Thu 2013-02-07 19:46:08 +0200
        * bug#14163155 COM\_CHANGE\_USER DOESN'T WORK WITH CHARACTER-SET-SERVER=UCS2 IN 5.1 SERVER
    * [Revision #3077.184.54](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.54) \[merge]\
      Thu 2013-02-07 17:08:59 +0100
      * merge 5.1 => 5.5
      * [Revision #2661.844.30](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.30)\
        Thu 2013-02-07 17:05:07 +0100
        * Bug#16192219 CRASH IN TEST\_IF\_SKIP\_SORT\_ORDER ON SELECT DISTINCT WITH ORDER BY
    * [Revision #3077.184.53](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.53) \[merge]\
      Thu 2013-02-07 17:27:32 +0530
      * Bug #16247322 MTR NOT RUNNING SYS\_VARS TEST SUITE FOR 5.1 Null-Merge from mysql-5.5
      * [Revision #2661.844.29](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.29)\
        Thu 2013-02-07 17:23:37 +0530
        * Bug#16247322- MTR NOT RUNNING SYS\_VARS TEST SUITE FOR 5.1
    * [Revision #3077.184.52](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.52)\
      Wed 2013-02-06 13:49:56 -0600
      * Bug#16263506 - INNODB; USE ABORT() ON ALL PLATFORMS INSTEAD OF DEREFERENCING UT\_DBG\_NULL\_PTR The abort() call is standard C but InnoDB only uses it in GCC environments. UT\_DBG\_USE\_ABORT is not defined the code crashed by dereferencing a null pointer instead of calling abort(). Other code throughout MySQL including ndb, sql, mysys and other places call abort() directly.
    * [Revision #3077.184.51](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.51)\
      Wed 2013-02-06 13:52:32 +0530
      * Bug#14711808 MSI INSTALLATION / UPGRADE CAN CORRUPT EXISTING INSTALLATION
    * [Revision #3077.184.50](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.50) \[merge]\
      Wed 2013-02-06 13:04:41 +0530
      * 13625278 5.1 => 5.5
      * [Revision #2661.844.28](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.28)\
        Wed 2013-02-06 13:02:14 +0530
        * BUG #13625278 - PB2 SHOULD PROVIDE MORE USEFUL INFORMATION FOR TIMEOUTS
    * [Revision #3077.184.49](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.49) \[merge]\
      Tue 2013-02-05 21:29:49 +0100
      * Upmerge of the 5.1.68 build
      * [Revision #2661.844.27](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.27) \[merge]\
        Tue 2013-02-05 20:47:45 +0100
        * Merge from mysql-5.1.68-release
    * [Revision #3077.184.48](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.48) \[merge]\
      Tue 2013-02-05 10:50:02 +0100
      * Merge from mysql-5.5.30-release
    * [Revision #3077.184.47](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.47) \[merge]\
      Tue 2013-02-05 13:42:56 +0530
      * 13625278 5.1=> 5.5
      * [Revision #2661.844.26](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.26)\
        Tue 2013-02-05 11:58:21 +0530
        * BUG #13625278 - PB2 SHOULD PROVIDE MORE USEFUL INFORMATION FOR TIMEOUTS
    * [Revision #3077.184.46](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.46)\
      Tue 2013-02-05 11:06:38 +0530
      * BUG#16196591 - CLIENTS CANNOT CONNECT TO MYSQL PROBLEM: When large number of connections are continuously made with wait\_timeout of 600 seconds for some hours, some connections remain after wait\_timeout expired and also new connections get struck under the configuration and the scenario reported in bug#16196591. FIX: The cause of this bug is the issue identified and fixed in the BUG#16088658 in 5.6.Also LOCK\_thread\_count contention issue fixed in BUG#15921866 in 5.6 need to be in 5.5 as well. Since the issue is not reproducible, it has been verified at customer configuration the issue could not be reproduced after a 48-hour test with a non-debug build which includes the above two fixes backported.
    * [Revision #3077.184.45](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.45) \[merge]\
      Mon 2013-02-04 20:41:25 +0530
      * 16190704 5.1 => 5.5 nullmerge
      * [Revision #2661.844.25](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.25)\
        Mon 2013-02-04 20:25:30 +0530
        * Bug #16190704: MTR STILL LOSES THE FAILED RUN LOGS AT RETRY-FAIL
    * [Revision #3077.184.44](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.44)\
      Fri 2013-02-01 09:47:16 -0500
      * Bug#16249505 INNODB REPORTS THAT IT'S GOING TO WAIT FOR I/O BUT THE I/O IS ASYNC
    * [Revision #3077.184.43](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.43)\
      Fri 2013-02-01 19:53:20 +0530
      * BUG #16190704 - MTR STILL LOSES THE FAILED RUN LOGS AT RETRY-FAIL
    * [Revision #3077.184.42](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.42)\
      Fri 2013-02-01 09:49:27 +0530
      * BUG#16207679: MISSING ERROR WHEN RESIGNAL TO MYSQL\_ERROR=5
    * [Revision #3077.184.41](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.41) \[merge]\
      Thu 2013-01-31 09:13:42 +0400
      * Bug #11827369: ASSERTION FAILED: !THD->LEX->CONTEXT\_ANALYSIS\_ONLY Manual up-merge from 5.1 to 5.5.
      * [Revision #2661.844.24](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.24) \[merge]\
        Thu 2013-01-31 08:46:30 +0400
        * Bug #11827369: ASSERTION FAILED: !THD->LEX->CONTEXT\_ANALYSIS\_ONLY
        * [Revision #2661.846.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.846.1)\
          Wed 2013-01-23 09:51:50 +0400
          * Bug #11827369: ASSERTION FAILED: !THD->LEX->CONTEXT\_ANALYSIS\_ONLY
    * [Revision #3077.184.40](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.40) \[merge]\
      Thu 2013-01-31 12:45:08 +0900
      * merge to mysql-5.5 from mysql-5.1
      * [Revision #2661.844.23](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.23)\
        Thu 2013-01-31 12:42:43 +0900
        * Bug #16220051 : INNODB\_BUG12400341 FAILS ON VALGRIND WITH TOO MANY ACTIVE CONCURRENT TRANSACTION innodb\_bug12400341.test is disabled for valgrind daily test. It might be affected by the previous test's undo slots existing, because of slower execution.
    * [Revision #3077.184.39](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.39) \[merge]\
      Thu 2013-01-31 07:06:30 +0530
      * Bug#14096619: UNABLE TO RESTORE DATABASE DUMP
      * [Revision #2661.844.22](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.22)\
        Thu 2013-01-31 06:39:15 +0530
        * Bug#14096619: UNABLE TO RESTORE DATABASE DUMP
    * [Revision #3077.184.38](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.38) \[merge]\
      Wed 2013-01-30 17:51:52 +0100
      * Bug#14521864: MYSQL 5.1 TO 5.5 BUGS PARTITIONING
      * [Revision #2661.844.21](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.21) \[merge]\
        Wed 2013-01-30 15:17:19 +0100
        * [Revision #2661.845.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.845.1)\
          Fri 2013-01-04 18:32:42 +0100
    * [Revision #3077.184.37](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.37)\
      Wed 2013-01-30 14:32:52 +0530
    * [Revision #3077.184.36](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.36)\
      Wed 2013-01-30 10:53:43 +0530
      * Bug#14756795 SELECT FROM NEW INNODB I\_S TABLES CRASHES SERVER WITH `--SKIP-INNODB`
    * [Revision #3077.184.35](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.35) \[merge]\
      Wed 2013-01-30 08:27:33 +0530\
      \*
      * BUG#1608883: KILLING A QUERY INSIDE INNODB CAUSES IT TO EVENTUALLY CRASH WITH AN ASSERTION Null merge from mysql-5.1
      * [Revision #2661.844.20](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.20)\
        Wed 2013-01-30 08:17:24 +0530\
        \*
        * BUG#1608883: KILLING A QUERY INSIDE INNODB CAUSES IT TO EVENTUALLY CRASH WITH AN ASSERTION
    * [Revision #3077.184.34](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.34) \[merge]\
      Tue 2013-01-29 10:06:31 +0530
      * Bug#16208709 - CRASH IN GET\_SEL\_ARG\_FOR\_KEYPART ON SELECT DISTINCT ON COL WITH COMPOSITE INDEX
      * [Revision #2661.844.19](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.19)\
        Tue 2013-01-29 10:05:00 +0530
        * Bug#16208709 - CRASH IN GET\_SEL\_ARG\_FOR\_KEYPART ON SELECT DISTINCT ON COL WITH COMPOSITE INDEX
    * [Revision #3077.184.33](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.33) \[merge]\
      Mon 2013-01-28 19:08:50 +0000
      * BUG#16200555: EMPTY NAME FOR USER VARIABLE IS ALLOWED AND BREAKS STATEMENT BINARY LOGGING
      * [Revision #2661.844.18](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.18)\
        Mon 2013-01-28 19:05:09 +0000
        * BUG#16200555: EMPTY NAME FOR USER VARIABLE IS ALLOWED AND BREAKS STATEMENT BINARY LOGGING
    * [Revision #3077.184.32](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.32)\
      Mon 2013-01-28 20:13:44 +0530
      * Bug#16183892 - INNODB PURGE BUFFERING IS NOT CRASH-SAFE
    * [Revision #3077.184.31](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.31) \[merge]\
      Mon 2013-01-28 14:58:55 +0530
      * Bug#16084594 USER\_VAR ITEM IN 'LOAD FILE QUERY' WAS NOT PROPERLY QUOTED IN BINLOG FILE Merging fix from mysql-5.1
      * [Revision #2661.844.17](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.17)\
        Mon 2013-01-28 14:41:54 +0530
        * Bug#16084594 USER\_VAR ITEM IN 'LOAD FILE QUERY' WAS NOT PROPERLY QUOTED IN BINLOG FILE Problem: In load data file query, User variables are allowed inside "Into\_list" and "Set\_list". These user variables used inside these two lists are not properly guarded with backticks while server is writting into binlog. Hence user variable names like a\` cannot be used in this context.
    * [Revision #3077.184.30](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.30)\
      Sat 2013-01-26 15:03:01 +0530
      * Bug#16056813-MEMORY LEAK ON FILTERED SLAVE
    * [Revision #3077.184.29](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.29) \[merge]\
      Thu 2013-01-24 15:05:15 +0530
      * [Revision #2661.844.16](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.16)\
        Thu 2013-01-24 14:56:12 +0530
        * BUG#11908153 CRASH AND/OR VALGRIND ERRORS IN FIELD\_BLOB::GET\_KEY\_IMAGE
    * [Revision #3077.184.28](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.28) \[merge]\
      Thu 2013-01-24 14:13:42 +0530
      * Bug #11752803 SERVER CRASHES IF MAX\_CONNECTIONS DECREASED BELOW CERTAIN LEVEL
      * [Revision #2661.844.15](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.15)\
        Thu 2013-01-24 14:02:54 +0530
        * Bug #11752803 SERVER CRASHES IF MAX\_CONNECTIONS DECREASED BELOW CERTAIN LEVEL
    * [Revision #3077.184.27](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.27)\
      Thu 2013-01-24 10:35:07 +0530
      * BUG#14798572: REMOVE UNUSED VARIABLE BINLOG\_CAN\_BE\_CORRUPTED FROM MYSQL\_BINLOG\_SEND
    * [Revision #3077.184.26](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.26) \[merge]\
      Wed 2013-01-23 15:00:46 +0900
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.844.14](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.14)\
        Wed 2013-01-23 14:59:36 +0900
        * Bug #16089381 : POSSIBLE NUMBER UNDERFLOW AROUND CALLING PAGE\_ZIP\_EMPTY\_SIZE()
    * [Revision #3077.184.25](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.25) \[merge]\
      Mon 2013-01-21 15:19:18 +0200
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.844.13](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.13)\
        Mon 2013-01-21 14:59:49 +0200
        * Bug#16067973 DROP TABLE SLOW WHEN IT DECOMPRESS COMPRESSED-ONLY PAGES
    * [Revision #3077.184.24](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.24) \[merge]\
      Sat 2013-01-19 06:07:08 +0530
      * BUG#11752707-SLAVE CRASHES IF RBR HAS AS DESTINATION A VIEW RATHER THAN A TABLE. Merging fix from mysql-5.1
      * [Revision #2661.844.12](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.12)\
        Sat 2013-01-19 06:01:46 +0530
        * Bug#11752707-SLAVE CRASHES IF RBR HAS AS DESTINATION A VIEW RATHER THAN A TABLE
    * [Revision #3077.184.23](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.23)\
      Fri 2013-01-18 18:26:02 +0530
      * BUG#11761680 disabled binlog\_spurious\_ddl\_errors on mysql-5.5
    * [Revision #3077.184.22](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.22)\
      Fri 2013-01-18 14:13:59 +0200
    * [Revision #3077.184.21](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.21)\
      Fri 2013-01-18 12:32:37 +0530
      * Description The test, binlog.binlog\_spurious\_ddl\_errors was failing on pb2 at the statement "UNINSTALL PLUGIN example;" with this warning: "Warning 1620 Plugin is busy and will be uninstalled on shutdown "
    * [Revision #3077.184.20](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.20)\
      Thu 2013-01-17 17:30:13 +0200
      * Bug#16138582 MTR\_MEMO\_RELEASE AND DYN\_ARRAY TOGETHER ARE VERY INEFFICIENT
    * [Revision #3077.184.19](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.19) \[merge]\
      Wed 2013-01-16 18:28:28 +0530
      * BUG#14117025: UNABLE TO RESTORE DUMP Null Merge from 5.1 to 5.5
      * [Revision #2661.844.11](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.11)\
        Wed 2013-01-16 18:26:27 +0530
        * BUG#14117025: UNABLE TO RESTORE DUMP Problem: When a view, with a specific character set and collation, is created on another view with a different character set and collation the dump restoration results in an illegal mix of collations error. SOLUTION: To avoid this confusion of collations, the create table datatype being used is hardcoded as "tinyint NOT NULL". This will not matter as the table created will be dropped at runtime and specifically tinyint is used to avoid hitting the row size conflicts.
    * [Revision #3077.184.18](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.18) \[merge]\
      Wed 2013-01-16 15:11:49 +0530
      * Bug#11751794 MYSQL GIVES THE WRONG RESULT WITH SOME SPECIAL USAGE
      * [Revision #2661.844.10](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.10)\
        Wed 2013-01-16 15:03:42 +0530
        * Bug#11751794 MYSQL GIVES THE WRONG RESULT WITH SOME SPECIAL USAGE
    * [Revision #3077.184.17](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.17)\
      Wed 2013-01-16 11:30:34 +0530
    * [Revision #3077.184.16](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.16)\
      Tue 2013-01-15 15:30:26 +0530
      * Bug#11757464:SERVER CRASH IN RECURSIVE CALL WHEN OOM
    * [Revision #3077.184.15](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.15) \[merge]\
      Tue 2013-01-15 14:33:22 +0530
      * Bug#11758009 - UNION EXECUTION ORDER WRONG ?
      * [Revision #2661.844.9](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.9)\
        Tue 2013-01-15 14:24:35 +0530
        * Bug#11758009 - UNION EXECUTION ORDER WRONG ?
    * [Revision #3077.184.14](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.14)\
      Tue 2013-01-15 12:26:49 +0530
    * [Revision #3077.184.13](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.13) \[merge]\
      Mon 2013-01-14 16:51:52 +0530
      * BUG#14303860 - EXECUTING A SELECT QUERY WITH TOO MANY WILDCARDS CAUSES A SEGFAULT Back port from 5.6 and trunk
      * [Revision #2661.844.8](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.8)\
        Mon 2013-01-14 14:59:48 +0530
        * BUG#14303860 - EXECUTING A SELECT QUERY WITH TOO MANY WILDCARDS CAUSES A SEGFAULT
    * [Revision #3077.184.12](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.12)\
      Mon 2013-01-14 10:58:17 +0100
      * Fix for Bug#14636211 WRONG RESULT (EXTRA ROW) ON A FROM SUBQUERY WITH A VARIABLE AND ORDER BY Bug#16035412 MYSQL SERVER 5.5.29 WRONG SORTING USING COMPLEX INDEX
    * [Revision #3077.184.11](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.11) \[merge]\
      Mon 2013-01-14 10:57:04 +0530
      * Merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.844.7](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.7)\
        Mon 2013-01-14 10:49:51 +0530\
        \*
        * BUG#1608883: KILLING A QUERY INSIDE INNODB CAUSES IT TO EVENTUALLY CRASH WITH AN ASSERTION
    * [Revision #3077.184.10](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.10) \[merge]\
      Sat 2013-01-12 11:17:03 +0530
      * BUG#11757250: REPLACE(...) INSIDE A STORED PROCEDURE.
      * [Revision #2661.844.6](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.6)\
        Sat 2013-01-12 11:13:37 +0530
        * BUG#11757250: REPLACE(...) INSIDE A STORED PROCEDURE.
    * [Revision #3077.184.9](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.9) \[merge]\
      Fri 2013-01-11 16:36:44 +0530
      * Bug#15843818 PARTITIONING BY RANGE WITH TO\_DAYS ALWAYS INCLUDES FIRST PARTITION WHEN PRUNING
      * [Revision #2661.844.5](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.5)\
        Fri 2013-01-11 16:27:37 +0530
        * Bug#15843818 PARTITIONING BY RANGE WITH TO\_DAYS ALWAYS INCLUDES FIRST PARTITION WHEN PRUNING
    * [Revision #3077.184.8](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.8) \[merge]\
      Fri 2013-01-11 06:36:53 +0530
      * Merge from 5.1 to 5.5
      * [Revision #2661.844.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.4)\
        Thu 2013-01-10 16:17:13 +0530
        * Bug#11760726: LEFT JOIN OPTIMIZED INTO JOIN LEADS TO INCORRECT RESULTS
    * [Revision #3077.184.7](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.7)\
      Thu 2013-01-10 16:37:20 +0530
      * Bug #14553380 MYSQL C API LIBRARY EXITS AT NET\_CLEAR AT NET\_SERV.CC:223
    * [Revision #3077.184.6](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.6) \[merge]\
      Thu 2013-01-10 14:37:02 +0530
      * Merge from 5.1 to 5.5
      * [Revision #2661.844.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.3)\
        Thu 2013-01-10 14:34:27 +0530
        * Bug#11749556: DEBUG ASSERTION WHEN ACCESSING A VIEW AND AVAILABLE MEMORY IS TOO LOW
    * [Revision #3077.184.5](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.5)\
      Thu 2013-01-10 10:28:04 +0530
      * Bug #16004999 ASSERT STATE == TRX\_STATE\_NOT\_STARTED, UNLOCK\_ROW()
    * [Revision #3077.184.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.4)\
      Thu 2013-01-10 09:00:23 +0530
      * Bug#16064876 MAIN.KILL FAILS OCCASIONALLY ON SOL10 SPARC64
    * [Revision #3077.184.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.3) \[merge]\
      Thu 2013-01-10 10:11:53 +1100
      * Merge from mysql-5.1 to mysql-5.5.
      * [Revision #2661.844.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.2)\
        Thu 2013-01-10 10:01:50 +1100
        * Bug#13997024 SEGV IN SYNC\_ARRAY\_CELL\_PRINT PRINTING OUT LONG SEMAPHORE WAIT DATA
    * [Revision #3077.184.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.2) \[merge]\
      Tue 2013-01-08 13:07:39 +0100
      * Empty version change upmerge
      * [Revision #2661.844.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.844.1)\
        Tue 2013-01-08 12:42:36 +0100
        * Raise version number after cloning 5.1.68
    * [Revision #3077.184.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.184.1)\
      Tue 2013-01-08 07:28:41 +0100
      * Raise version number after cloning 5.5.30
  * [Revision #3334.1.414](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.414)\
    Mon 2013-05-06 16:51:41 +0300
    * If one declared several continue handler for the same condition on different level of stored procedures, all of them where executed. Now we only execute the innermost of them (the most relevant).
  * [Revision #3334.1.413](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.413) \[merge]\
    Sun 2013-05-05 05:38:09 +0400
    * [MDEV-4482](https://jira.mariadb.org/browse/MDEV-4482) fix null-merged to 5.5
    * [Revision #3334.35.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.35.1) \[merge]\
      Sun 2013-05-05 05:29:33 +0400
      * Merge
      * [Revision #2502.577.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.577.1)\
        Sun 2013-05-05 05:27:02 +0400
        * [MDEV-4482](https://jira.mariadb.org/browse/MDEV-4482): main.windows test fails in buildbot with result mismatch - Rollback an earlier patch (was pushed into 5.3 instead of 5.5)
  * [Revision #3334.1.412](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.412) \[merge]\
    Sat 2013-05-04 21:56:45 -0700
    * Merge 5.3->5.5
    * [Revision #2502.567.99](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.99)\
      Fri 2013-05-03 22:46:45 -0700
      * Fixed bug [MDEV-4336](https://jira.mariadb.org/browse/MDEV-4336). When iterating over a list of conditions using List\_iterator the function remove\_eq\_conds should skip all predicates that replace a condition from the list. Otherwise it can come to an infinite recursion.
    * [Revision #2502.567.98](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.98)\
      Fri 2013-05-03 18:45:20 -0700
      * Made consistent handling of the predicates of the form IS NULL in outer joins with that in inner joins. Previously such condition was transformed into the condition = 0 unless the field belonged to an inner table of an outer join. In this case the predicate was interpreted as for any other field. Now if the field in the predicate IS NULL belongs to an inner table of an outer join the predicate is transformed into the disjunction = 0 OR IS NULL. This is fully compatible with the semantics of such predicates in 5.5.
    * [Revision #2502.567.97](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.97)\
      Mon 2013-04-29 20:31:40 -0700
      * Fixed bug [MDEV-4274](https://jira.mariadb.org/browse/MDEV-4274). This bug was the result of incompleteness of the patch for bug [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177). When an OR condition is simplified to a single conjunct it is merged into the embedding AND condition. Multiple equalities are also merged, and any field item involved in those equality should acquire a pointer to a the multiple equality formed by this merge.
  * [Revision #3334.1.411](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.411)\
    Sat 2013-05-04 20:42:43 +0400
    * [MDEV-4071](https://jira.mariadb.org/browse/MDEV-4071): Valgrind warnings 'Invalid read' in subselect\_engine::calc\_const\_tables with ... - Call tmp\_having->update\_used\_tables() _before_ we have call JOIN::cleanup(). Making the call after join::cleanup() is not allowed, because subquery predicate items walk parent join's JOIN\_TAB structures. Which can be invalidated by JOIN::cleanup().
  * [Revision #3334.1.410](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.410)\
    Sat 2013-05-04 21:02:07 +0400
    * [MDEV-389](https://jira.mariadb.org/browse/MDEV-389): Wrong result (missing row) with semijoin, join\_cache\_level>4 ... - Added testcase
  * [Revision #3334.1.409](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.409)\
    Sat 2013-05-04 13:05:24 +0400
    * Update testcase result
  * [Revision #3334.1.408](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.408)\
    Sat 2013-05-04 01:08:20 +0400
    * [MDEV-4270](https://jira.mariadb.org/browse/MDEV-4270): crash in fix\_semijoin\_strategies\_for\_picked\_join\_order - Added testcase
  * [Revision #3334.1.407](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.407)\
    Sat 2013-05-04 00:56:50 +0400
    * [MDEV-621](https://jira.mariadb.org/browse/MDEV-621): [Bug #693329](https://bugs.launchpad.net/bugs/693329) - Assertion \`!is\_interleave\_error' failed on low optimizer\_search\_depth - When restore\_prev\_nj\_state() is called for the table that is the last remaining child of a nested join, do not leave that nested join's bit in join->cur\_embedding\_map.
  * [Revision #3334.1.406](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.406)\
    Fri 2013-05-03 00:10:43 +0400
    * [MDEV-4465](https://jira.mariadb.org/browse/MDEV-4465): Reproducible crash (mysqld got signal 11) in multi\_delete::initialize\_tables... - make multi\_delete::initialize\_tables() take into account that the JOIN structure may have semi-join nests (which are not fully initialized when this function is called, they have tab->table=NULL which caused the crash) - Also checked multi\_update::initialize\_tables(): it has a different logic and needed no fixing.
  * [Revision #3334.1.405](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.405)\
    Tue 2013-04-30 00:29:47 +0200
    * [MDEV-4458](https://jira.mariadb.org/browse/MDEV-4458) - Windows installer does not launch upgrade wizard anymore, even if there are upgradable instances (i.e windows service of lower MariaDB/MySQL version)
  * [Revision #3334.1.404](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.404)\
    Sun 2013-04-28 14:28:46 +0200
    * fix test on Windows
  * [Revision #3334.1.403](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.403)\
    Sat 2013-04-27 23:28:48 -0700
    * Fixed bug [MDEV-4340](https://jira.mariadb.org/browse/MDEV-4340). The function make\_join\_statistics checks whether eq\_ref access uses only constant expressions, and, if this is the case the function performs constant row substitution. The code of this check must take into account hidden components of extended secondary keys.
  * [Revision #3334.1.402](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.402)\
    Thu 2013-04-25 15:11:59 +0200
    * Fix build on Windows
  * [Revision #3334.1.401](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.401)\
    Thu 2013-04-25 13:16:35 +0200
    * Fix unsigned/signed conversion bug in event type during mysql\_binlog\_send().
  * [Revision #3334.1.400](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.400)\
    Mon 2013-04-22 16:22:39 +0200
    * [MDEV-4396](https://jira.mariadb.org/browse/MDEV-4396): Fix sporadic failure of test innodb.innodb\_bug14676111
  * [Revision #3334.1.399](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.399)\
    Fri 2013-04-19 12:50:16 +0200
    * [MDEV-260](https://jira.mariadb.org/browse/MDEV-260) auditing table accesses
  * [Revision #3334.1.398](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.398)\
    Fri 2013-04-19 12:08:55 +0200
    * [MDEV-4398](https://jira.mariadb.org/browse/MDEV-4398) - Change default for innodb\_use\_fallocate to FALSE, due to bugs in older Linux kernels (posix\_fallocate() does not always guarantee that file size is like one specified)
  * [Revision #3334.1.397](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.397)\
    Thu 2013-04-18 22:17:29 +0200
    * [MDEV-4332](https://jira.mariadb.org/browse/MDEV-4332) Increase username length from 16 characters
  * [Revision #3334.1.396](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.396)\
    Wed 2013-04-17 19:42:34 +0200
    * strmake\_buf(X,Y) helper, equivalent to strmake(X,Y,sizeof(X)-1) with a bit of lame protection against abuse.
  * [Revision #3334.1.395](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.395)\
    Tue 2013-04-16 18:52:23 +0200
    * debug\_sync is only available in debug build.
  * [Revision #3334.1.394](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.394)\
    Tue 2013-04-16 17:33:47 +0200
    * Fix race in test case.
  * [Revision #3334.1.393](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.393)\
    Tue 2013-04-16 09:42:09 +0200
    * [MDEV-3882](https://jira.mariadb.org/browse/MDEV-3882): .deb versions lower than upstream repo, causing install failure
  * [Revision #3334.1.392](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.392)\
    Sun 2013-04-14 16:48:16 +0200
    * compiler warnings
  * [Revision #3334.1.391](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.391)\
    Sun 2013-04-14 10:00:42 +0200
    * add missing tests
  * [Revision #3334.1.390](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.390)\
    Fri 2013-04-12 13:19:00 +0300
    * Increase default value of max\_binlog\_cache\_size and max\_binlog\_stmt\_cache\_size to ulonglong\_max. This fixes that by default LOAD DATA INFILE will not generate the error: "Multi-statement transaction required more than 'max\_binlog\_cache\_size' bytes of storage..."
  * [Revision #3334.1.389](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.389)\
    Fri 2013-04-12 01:05:29 +0200
    * complier warnings. hide the redundant condition under #ifdef (because only there it makes any sense)
  * [Revision #3334.1.388](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.388) \[merge]\
    Fri 2013-04-12 01:01:18 +0200
    * 5.3 merge
    * [Revision #2502.567.96](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.96) \[merge]\
      Thu 2013-04-11 19:35:39 +0200
      * 5.2 merge
      * [Revision #2502.566.45](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.45) \[merge]\
        Thu 2013-04-11 19:30:59 +0200
        * 5.1 merge
        * [Revision #2502.565.45](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.45)\
          Sat 2013-04-06 21:29:12 +0200
          * [MDEV-4244](https://jira.mariadb.org/browse/MDEV-4244) \[PATCH] Buffer overruns and use-after-free errors
        * [Revision #2502.565.44](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.44)\
          Thu 2013-04-04 11:35:10 +0200
          * [MDEV-4088](https://jira.mariadb.org/browse/MDEV-4088) Replication 10.0 -> 5.5 fails
    * [Revision #2502.567.95](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.95)\
      Sat 2013-04-06 15:51:08 +0200
      * [MDEV-4244](https://jira.mariadb.org/browse/MDEV-4244) \[PATCH] Buffer overruns and use-after-free errors
    * [Revision #2502.567.94](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.94)\
      Sat 2013-04-06 15:14:46 +0200
      * [MDEV-4316](https://jira.mariadb.org/browse/MDEV-4316) MariaDB server crash with signal 11
    * [Revision #2502.567.93](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.93)\
      Mon 2013-04-08 12:04:28 +0300
      * If a range tree has a branch that is an expensive constant, currently get\_mm\_tree skipped the evaluation of this constant and icorrectly proceeded. The correct behavior is to return a NULL subtree, according to the IF branch being fixed - when it evaluates the constant it returns a value, and doesn't continue further.
    * [Revision #2502.567.92](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.92)\
      Thu 2013-04-04 12:34:31 +0400
      * Update tests results, mysql-test/r/windows.result
  * [Revision #3334.1.387](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.387)\
    Sun 2013-04-07 20:32:39 +0200
    * [MDEV-4356](https://jira.mariadb.org/browse/MDEV-4356) : MariaDB does not start if bind-address gets resolved to more than single IP address.
  * [Revision #3334.1.386](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.386)\
    Sat 2013-04-06 00:36:10 +0200
    * [MDEV-4338](https://jira.mariadb.org/browse/MDEV-4338) - Support FusionIO/directFS atomic writes
  * [Revision #3334.1.385](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.385)\
    Sat 2013-04-06 00:35:45 +0200
    * [MDEV-4338](https://jira.mariadb.org/browse/MDEV-4338) - Support FusionIO/directFS atomic writes
  * [Revision #3334.1.384](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.384)\
    Thu 2013-04-04 11:37:23 +0200
    * compilation warnings
  * [Revision #3334.1.383](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.383)\
    Thu 2013-04-04 11:37:13 +0200
    * fix have\_debug\_sync.inc to be more robust (debug\_sync value can have single quotes)
  * [Revision #3334.1.382](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.382)\
    Thu 2013-04-04 11:05:04 +0200
    * [MDEV-4161](https://jira.mariadb.org/browse/MDEV-4161) Assertion \`status\_var.memory\_used == 0' fails in virtual THD::THD()
  * [Revision #3334.1.381](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.381)\
    Thu 2013-03-28 20:04:14 +0100
    * [MDEV-4243](https://jira.mariadb.org/browse/MDEV-4243) Warnings/errors while compiling with clang
  * [Revision #3334.1.380](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.380) \[merge]\
    Wed 2013-04-03 18:51:29 +0400
    * Merge 5.3 -> 5.5
    * [Revision #2502.567.91](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.91)\
      Mon 2013-04-01 18:03:14 +0400
      * [MDEV-4240](https://jira.mariadb.org/browse/MDEV-4240): [mariadb 5.3.12](../../release-notes-mariadb-5-3-series/mariadb-5312-release-notes.md) using more memory than MySQL 5.1 for an inefficient query - Let index\_merge allocate table handlers on quick select's MEM\_ROOT, not on statement's MEM\_ROOT. This is crucial for big "range checked for each record" queries, where index\_merge can be created and deleted many times during query exection. We should not make O(#rows) allocations on statement's MEM\_ROOT.
    * [Revision #2502.567.90](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.90)\
      Fri 2013-03-29 19:27:06 +0400
      * [MDEV-4335](https://jira.mariadb.org/browse/MDEV-4335): Unexpected results when selecting on information\_schema - When converting a subquery to a semi-join, propagate OPTION\_SCHEMA\_TABLE.
  * [Revision #3334.1.379](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.379)\
    Fri 2013-03-29 17:53:21 +0200
    * Fix for [MDEV-4144](https://jira.mariadb.org/browse/MDEV-4144)
  * [Revision #3334.1.378](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.378)\
    Fri 2013-03-29 14:56:09 +0100
    * [MDEV-4243](https://jira.mariadb.org/browse/MDEV-4243) : remove several clang warnings.
  * [Revision #3334.1.377](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.377) \[merge]\
    Thu 2013-03-28 19:18:36 -0700
    * Merge 5.3->5.5.
    * [Revision #2502.567.89](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.89) \[merge]\
      Wed 2013-03-27 08:58:16 -0700
      * Merge.
      * [Revision #2502.576.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.576.1)\
        Fri 2013-03-22 21:33:06 -0700
        * Fixed bug [MDEV-4318](https://jira.mariadb.org/browse/MDEV-4318). In some cases, when using views the optimizer incorrectly determined possible join orders for queries with nested outer and inner joins. This could lead to invalid execution plans for such queries.
  * [Revision #3334.1.376](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.376) \[merge]\
    Wed 2013-03-27 22:22:52 -0700
    * Merge
    * [Revision #3334.34.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.34.1)\
      Wed 2013-03-27 19:17:32 -0700
      * Fixed bug [MDEV-4311](https://jira.mariadb.org/browse/MDEV-4311) (bug #68749). This bug was introduced by the patch for [WL#3220](https://askmonty.org/worklog/?tid=3220). If the memory allocated for the tree to store unique elements to be counted is not big enough to include all of them then an external file is used to store the elements. The unique elements are guaranteed not to be nulls. So, when reading them from the file we don't have to care about the null flags of the read values. However, we should remove the flag at the very beginning of the process. If we don't do it and if the last value written into the record buffer for the field whose distinct values needs to be counted happens to be null, then all values read from the file are considered to be nulls and are not counted in. The fix does not remove a possible null flag for the read values. Rather it just counts the values in the same way it was done before WL #3220.
  * [Revision #3334.1.375](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.375) \[merge]\
    Wed 2013-03-27 10:03:28 +0100
    * 5.3 merge
    * [Revision #2502.567.88](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.88) \[merge]\
      Tue 2013-03-26 19:09:47 +0100
      * 5.2 merge
      * [Revision #2502.566.44](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.44) \[merge]\
        Tue 2013-03-26 17:39:45 +0100
        * 5.1 merge
        * [Revision #2502.565.43](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.43)\
          Wed 2013-03-20 21:20:51 +0100
          * add 'plugins' suite - empty, but the line `./mtr --suite=main,plugins` will work on all branches.
        * [Revision #2502.565.42](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.42)\
          Tue 2013-03-19 17:25:58 +0400
          * [MDEV-4295](https://jira.mariadb.org/browse/MDEV-4295) Server crashes in get\_point on a query with Area, AsBinary, MultiPoint. Need to check if the number of points is 0 for the polygon.
        * [Revision #2502.565.41](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.41)\
          Tue 2013-03-19 17:16:10 +0400
          * [MDEV-4296](https://jira.mariadb.org/browse/MDEV-4296) Assertion \`n\_linear\_rings > 0' fails in Gis\_polygon::centroid\_xy. Forgotten DBUG\_ASSERT should be replaced with the 'return error'.
        * [Revision #2502.565.40](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.40)\
          Mon 2013-03-18 15:07:52 +0200
          * [MDEV-4269](https://jira.mariadb.org/browse/MDEV-4269) fix. Item\_default\_value inherited form Item\_field so should create temporary table field similary.
        * [Revision #2502.565.39](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.39)\
          Mon 2013-03-18 17:58:00 +0400
          * [MDEV-4252](https://jira.mariadb.org/browse/MDEV-4252) geometry query crashes server. Additional fixes for possible overflows in length-related calculations in 'spatial' implementations. Checks added to the ::get\_data\_size() methods. max\_n\_points decreased to occupy less 2G size. An object of that size is practically inoperable anyway.
        * [Revision #2502.565.38](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.38)\
          Mon 2013-03-18 10:35:03 +0100
          * [MDEV-4289](https://jira.mariadb.org/browse/MDEV-4289) Assertion \`0' fails in make\_sortkey with GROUP\_CONCAT, MAKE\_SET, GROUP BY
        * [Revision #2502.565.37](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.37)\
          Sun 2013-03-10 23:08:05 +0400
          * [MDEV-4252](https://jira.mariadb.org/browse/MDEV-4252) geometry query crashes server. The bug was found by Alyssa Milburn. If the number of points of a geometry feature read from binary representation is greater than 0x10000000, then the (uint32) (num\_points \* 16) will cut the higher byte, which leads to various errors. Fixed by additional check if (num\_points > max\_n\_points).
    * [Revision #2502.567.87](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.87)\
      Tue 2013-03-26 21:47:06 +0400
      * GEOMETRYCOLLECTION EMPTY handling fixed. The get\_mbr() method shouldn't return the error, rather an invalid MBR in this case.
    * [Revision #2502.567.86](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.86)\
      Tue 2013-03-26 13:07:46 +0200
      * [MDEV-4292](https://jira.mariadb.org/browse/MDEV-4292) fix.
    * [Revision #2502.567.85](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.85)\
      Fri 2013-03-22 17:32:27 +0400
      * [MDEV-4310](https://jira.mariadb.org/browse/MDEV-4310) geometry function equals hangs forever. The Geometry::get\_mbr() function can return an error on a bad data. We have to check for that and act respectively.
    * [Revision #2502.567.84](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.84) \[merge]\
      Thu 2013-03-21 11:07:38 +0400
      * Merge
      * [Revision #2502.575.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.575.1)\
        Thu 2013-03-21 11:06:27 +0400
        * [MDEV-4277](https://jira.mariadb.org/browse/MDEV-4277): Crash inside mi\_killed\_in\_mariadb() with myisammrg - Set MI\_INFO::external\_ref for MyISAM tables that are parts of myisamMRG table.
    * [Revision #2502.567.83](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.83)\
      Wed 2013-03-20 16:13:00 +0100
      * [MDEV-4293](https://jira.mariadb.org/browse/MDEV-4293) Valgrind warnings (Conditional jump or move depends on uninitialised value) in remove\_eq\_conds on time functions with NULL argument
    * [Revision #2502.567.82](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.82)\
      Mon 2013-03-18 08:44:24 +0100
      * [MDEV-4283](https://jira.mariadb.org/browse/MDEV-4283) Assertion \`scale <= precision' fails in strings/decimal.c
    * [Revision #2502.567.81](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.81)\
      Sun 2013-03-17 17:44:15 +0100
      * [MDEV-4286](https://jira.mariadb.org/browse/MDEV-4286) Server crashes in Protocol\_text::store, stack smashing detected
    * [Revision #2502.567.80](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.80)\
      Sun 2013-03-17 07:41:22 +0100
      * [MDEV-4281](https://jira.mariadb.org/browse/MDEV-4281) Assertion \`maybe\_null && item->null\_value' fails in make\_sortkey on CASE with different return types, GROUP\_CONCAT, GROUP BY
  * [Revision #3334.1.374](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.374)\
    Tue 2013-03-26 19:17:26 +0100
    * [MDEV-4307](https://jira.mariadb.org/browse/MDEV-4307) Support at least 48 utf8 characters in username in server and PAM
  * [Revision #3334.1.373](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.373)\
    Tue 2013-03-26 17:57:36 +0100
    * fix @@external\_user variable
  * [Revision #3334.1.372](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.372)\
    Mon 2013-03-25 16:38:00 +0100
    * fixes for windows
  * [Revision #3334.1.371](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.371)\
    Wed 2013-03-20 20:56:14 +0100
    * [MDEV-249](https://jira.mariadb.org/browse/MDEV-249) QUERY CACHE INFORMATION
  * [Revision #3334.1.370](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.370)\
    Tue 2013-03-19 15:25:58 +0100
    * extend check\_global\_access() to avoid my\_error when it's not needed (in INFORMATION\_SCHEMA).
  * [Revision #3334.1.369](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.369)\
    Tue 2013-03-26 10:34:21 +0100
    * Fixes for Windows XP
  * [Revision #3334.1.368](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.368)\
    Tue 2013-03-26 08:17:22 +0100
    * [MDEV-4330](https://jira.mariadb.org/browse/MDEV-4330) - get\_tty\_password() does not work if input redirection is used.
  * [Revision #3334.1.367](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.367)\
    Mon 2013-03-25 16:45:24 +0200
    * Patch by Ian Good for [MDEV-4319](https://jira.mariadb.org/browse/MDEV-4319): mysqlbinlog output ambiguous escaping
  * [Revision #3334.1.366](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.366)\
    Sun 2013-03-17 11:41:25 +0100
    * [MDEV-4284](https://jira.mariadb.org/browse/MDEV-4284) Assertion \`cmp\_items\[(uint)cmp\_type]' fails in sql/item\_cmpfunc.cc
  * [Revision #3334.1.365](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.365)\
    Thu 2013-03-14 19:07:20 +0200
    * [MDEV-4272](https://jira.mariadb.org/browse/MDEV-4272) fix.
  * [Revision #3334.1.364](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.364)\
    Thu 2013-03-14 18:39:22 +0200
    * OPTION is now a valid identifier (not a reserved word)
  * [Revision #3334.1.363](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.363)\
    Thu 2013-03-14 16:52:20 +0400
    * [MDEV-4214](https://jira.mariadb.org/browse/MDEV-4214) : main.partition\_rename\_longfilename fails on eCryptFS Adding an include file which checks whether long names are supported
  * [Revision #3334.1.362](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.362)\
    Wed 2013-03-13 22:33:52 +0100
    * [MDEV-4265](https://jira.mariadb.org/browse/MDEV-4265) 5.5 is slower than 5.3 because of many str\_to\_datetime calls
  * [Revision #3334.1.361](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.361)\
    Mon 2013-03-11 21:00:08 +0100
    * fix innodb failures on solaris
  * [Revision #3334.1.360](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.360)\
    Tue 2013-03-12 21:06:46 +0100
    * Fix clang warning (suggest parentheses)
  * [Revision #3334.1.359](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.359)\
    Tue 2013-03-12 20:11:05 +0100
    * [MDEV-4267](https://jira.mariadb.org/browse/MDEV-4267) : do not copy sql\_yacc.cc and sql\_yacc.h from unpacked source tarball into build directory, if usable bison is installed on the build machine.
  * [Revision #3334.1.358](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.358)\
    Tue 2013-03-12 20:09:49 +0100
    * [MDEV-4224](https://jira.mariadb.org/browse/MDEV-4224) : func\_math test fails, when clang 3.0 compiler is used.
  * [Revision #3334.1.357](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.357)\
    Wed 2013-03-06 13:30:40 +0100
    * [MDEV-4249](https://jira.mariadb.org/browse/MDEV-4249) : when autodetecting default client charset on Windows, fallback to GetACP() whenever GetConsoleCP() returns 0 (i.e appkication does not have a console , which is the case for GUI apps, Windows services etc)
* [Revision #3394](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3394)\
  Sat 2013-05-25 12:22:57 +0300
  * References: [MDEV-4572](https://jira.mariadb.org/browse/MDEV-4572) - merge with lp:codership-mysql/5.5-23 revisions 3858..3867
* [Revision #3393](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3393) \[merge]\
  Fri 2013-05-24 15:29:01 +0300
  * References: [MDEV-4572](https://jira.mariadb.org/browse/MDEV-4572) - merge with [mariaDB 5.5.30](../../release-notes-mariadb-5-5-series/mariadb-5530-release-notes.md)
  * [Revision #3334.1.356](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.356)\
    Mon 2013-03-11 13:50:17 +0400
    * The i386 specific code improving character set conversion on the ASCII range was not enabled on x86\_64 machines. Enabling it. Gives up to 18 times conversion performance improvement.
  * [Revision #3334.1.355](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.355) \[merge]\
    Sun 2013-03-10 12:46:56 +0100
    * 5.3->5.5 merge
    * [Revision #2502.567.79](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.79)\
      Fri 2013-03-08 00:25:26 -0800
      * Fixed bug [MDEV-4250](https://jira.mariadb.org/browse/MDEV-4250). This is a bug in the legacy code. It did not manifest itself because it was masked by other bugs that were fixed by the patches for [MDEV-4172](https://jira.mariadb.org/browse/MDEV-4172) and [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177).
    * [Revision #2502.567.78](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.78)\
      Wed 2013-03-06 22:22:24 +0100
      * Fix typo (clang issued warning that =+ was used where += was intended)
    * [Revision #2502.567.77](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.77)\
      Wed 2013-03-06 21:10:58 +0200
      * [MDEV-4241](https://jira.mariadb.org/browse/MDEV-4241) fix.
  * [Revision #3334.1.354](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.354)\
    Fri 2013-03-08 19:09:45 +0100
    * [MDEV-4186](https://jira.mariadb.org/browse/MDEV-4186) Test case main.myisampack fails on ppc32 (only)
  * [Revision #3334.1.353](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.353)\
    Fri 2013-03-08 19:09:15 +0100
    * [MDEV-4175](https://jira.mariadb.org/browse/MDEV-4175) auth\_socket to build on OpenBSD / Bitrig
  * [Revision #3334.1.352](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.352) \[merge]\
    Fri 2013-03-08 19:08:45 +0100
    * merge with XtraDB as of Percona-Server-5.5.30-rel30.1
    * [Revision #0.12.61](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/0.12.61)\
      Fri 2013-03-08 13:13:46 +0100
      * Percona-Server-5.5.30-rel30.1.tar.gz
  * [Revision #3334.1.351](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.351)\
    Wed 2013-03-06 09:38:08 +0100
    * hack in dependencies to imitate mysql-\*.rpm even better
  * [Revision #3334.1.350](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.350)\
    Wed 2013-03-06 09:32:13 +0100
    * [MDEV-4068](https://jira.mariadb.org/browse/MDEV-4068) rpm scriptlet chown command dangerous
  * [Revision #3334.1.349](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.349)\
    Tue 2013-03-05 17:49:37 +0100
    * [MDEV-4066](https://jira.mariadb.org/browse/MDEV-4066) semisync\_master + temporary tables causes memory leaks
  * [Revision #3334.1.348](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.348)\
    Wed 2013-03-06 01:45:25 +0400
    * TODO-424 geometry query crashes server. The bug was found by Alyssa Milburn. If the number of points of a geometry feature read from binary representation is greater than 0x10000000, then the (uint32) (num\_points \* 16) will cut the higher byte, which leads to various errors. Fixed by additional check if (num\_points > max\_n\_points).
  * [Revision #3334.1.347](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.347)\
    Tue 2013-03-05 20:15:36 +0200
    * Fix for assert found by mysql-test-run
  * [Revision #3334.1.346](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.346)\
    Tue 2013-03-05 00:53:18 +0200
    * Fixed issue with LOCK TABLE + ALTER TABLE ENABLE KEYS + SHOW commands.
  * [Revision #3334.1.345](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.345)\
    Mon 2013-03-04 12:49:35 +0100
    * Fix wrong install location for DEB supportfiles.
  * [Revision #3334.1.344](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.344) \[merge]\
    Sat 2013-03-02 14:04:11 -0800
    * Merge
    * [Revision #3334.33.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.33.1)\
      Sat 2013-03-02 12:36:32 -0800
      * Fixed bug [MDEV-4220](https://jira.mariadb.org/browse/MDEV-4220). This bug is a regression bug. The regression was introduced by the patch for [MDEV-3851](https://jira.mariadb.org/browse/MDEV-3851), that tried to weaken the condition when a ref access with an extended key can be converted to an eq\_ref access. The patch incorrectly formed this condition. As a result, while improving performance for some queries, the patch caused worse performance for another queries.
  * [Revision #3334.1.343](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.343)\
    Fri 2013-03-01 20:58:19 +0100
    * [MDEV-4216](https://jira.mariadb.org/browse/MDEV-4216) : export additional functions mysql\_get\_timeout\_value(),mysql\_get\_timeout\_value\_ms(), mysql\_get\_socket() from shared client library. They are documented as part of async API.
  * [Revision #3334.1.342](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.342)\
    Fri 2013-03-01 11:36:15 -0500
    * Removed the obsolete instructions from the MySQL 5.1 manual. Instead provide a link to
  * [Revision #3334.1.341](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.341) \[merge]\
    Fri 2013-03-01 18:09:06 +0200
    * Automatic merge
    * [Revision #3334.32.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.32.3)\
      Fri 2013-03-01 18:01:44 +0200
      * Fixed bug MPDEV-628 / [Bug #989055](https://bugs.launchpad.net/bugs/989055) - Querying myisam table metadata may corrupt the table.
    * [Revision #3334.32.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.32.2)\
      Thu 2013-02-28 16:47:03 +0200
      * Added test case for bug in replace with replication that existed in MySQL 5.1: Replace with an auto\_increment primary key and another unique key didn't replicate correctly with REPLACE
    * [Revision #3334.32.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.32.1)\
      Thu 2013-02-28 08:42:05 +0200
      * Added support for `--crash-script` in mysqld\_safe. Trivial cleanup
  * [Revision #3334.1.340](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.340)\
    Fri 2013-03-01 14:58:19 +0100
    * Fix compile error when building with DBUG, but without DEBUG\_SYNC.
  * [Revision #3334.1.339](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.339) \[merge]\
    Fri 2013-03-01 11:44:10 +0400
    * Merge 5.3->5.5
    * [Revision #2502.567.76](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.76)\
      Fri 2013-03-01 08:23:35 +0400
      * Fix compile error on windows in fix for [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177).
    * [Revision #2502.567.75](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.75) \[merge]\
      Thu 2013-02-28 17:09:56 -0800
      * Merge
      * [Revision #2502.574.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.574.1)\
        Thu 2013-02-28 14:35:46 -0800
        * Fixed bug [MDEV-4209](https://jira.mariadb.org/browse/MDEV-4209) Do not include BLOB fields into the key to access the temporary table created for a materialized view/derived table. BLOB components are not allowed in keys.
  * [Revision #3334.1.338](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.338) \[merge]\
    Thu 2013-02-28 23:56:17 +0100
    * merge with XtraDB as of Percona-Server-5.5.29-rel30.0
    * [Revision #0.12.60](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/0.12.60)\
      Thu 2013-02-28 22:23:45 +0100
      * Percona-Server-5.5.29-rel30.0.tar.gz
  * [Revision #3334.1.337](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.337) \[merge]\
    Thu 2013-02-28 22:47:29 +0100
    * 5.3->5.5 merge
    * [Revision #2502.567.74](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.74) \[merge]\
      Thu 2013-02-28 21:48:47 +0100
      * 5.2 -> 5.3
      * [Revision #2502.566.43](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.43) \[merge]\
        Thu 2013-02-28 19:00:58 +0100
        * 5.1 -> 5.2 merge
        * [Revision #2502.565.36](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.36)\
          Thu 2013-02-28 11:46:35 +0100
          * a simpler fix for MySQL Bug #12408412: GROUP\_CONCAT + ORDER BY + INPUT/OUTPUT SAME USER VARIABLE = CRASH and MySQL Bug#14664077 SEVERE PERFORMANCE DEGRADATION IN SOME CASES WHEN USER VARIABLES ARE USED
        * [Revision #2502.565.35](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.35)\
          Thu 2013-02-28 10:00:07 +0100
          * Fixed BUG#51763 Can't delete rows from MEMORY table with HASH key
        * [Revision #2502.565.34](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.34) \[merge]\
          Thu 2013-02-28 09:58:39 +0100
          * mysql-5.1 merge
          * [Revision #2661.838.56](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.56)\
            Tue 2013-01-08 13:29:11 +0100
            * Applying patch for Bug#67177 Bug#15967374 from Kent
        * [Revision #2502.565.33](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.33)\
          Tue 2013-02-26 21:20:15 +0100
          * [MDEV-4203](https://jira.mariadb.org/browse/MDEV-4203) : fix maria SE repair functions (wrong operator precedence)
        * [Revision #2502.565.32](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.32)\
          Thu 2013-02-21 23:20:26 +0100
          * [MDEV-4194](https://jira.mariadb.org/browse/MDEV-4194): Fix typo (missing comma) in mysys error messages
        * [Revision #2502.565.31](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.31)\
          Thu 2013-02-14 16:27:55 +0400
          * [MDEV-4169](https://jira.mariadb.org/browse/MDEV-4169): mysql-test-run doesn't strip expected warnings (setrlimit)
        * [Revision #2502.565.30](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.30)\
          Fri 2013-02-01 00:09:36 +0200
          * Fix bug [MDEV-641](https://jira.mariadb.org/browse/MDEV-641)
    * [Revision #2502.567.73](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.73)\
      Thu 2013-02-28 09:55:35 -0800
      * Fixed a compile error for some platform.
    * [Revision #2502.567.72](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.72)\
      Sun 2013-02-24 19:16:11 -0800
      * Fixed bug [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177) The function remove\_eq\_cond removes the parts of a disjunction for which it has been proved that they are always true. In the result of this removal the disjunction may be converted into a formula without OR that must be merged into the AND formula that contains the disjunction. The merging of two AND conditions must take into account the multiple equalities that may be part of each of them. These multiple equality must be merged and become part of the and object built as the result of the merge of the AND conditions. Erroneously the function remove\_eq\_cond lacked the code that would merge multiple equalities of the merged AND conditions. This could lead to confusing situations when at the same AND level there were two multiple equalities with common members and the list of equal items contained only some of these multiple equalities. This, in its turn, could lead to an incorrect work of the function substitute\_for\_best\_equal\_field when it tried to optimize ref accesses. This resulted in forming invalid TABLE\_REF objects that were used to build look-up keys when materialized subqueries were exploited.
    * [Revision #2502.567.71](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.71)\
      Thu 2013-02-21 17:13:12 -0800
      * Fixed bug [MDEV-4172](https://jira.mariadb.org/browse/MDEV-4172). This bug in the legacy code could manifest itself in queries with semi-join materialized subqueries. When a subquery is materialized all conditions that are imposed only on the columns belonging to the tables from the subquery are taken into account.The code responsible for subquery optimizations that employes subquery materialization makes sure to remove these conditions from the WHERE conditions of the query obtained after it has transformed the original query into a query with a semi-join. If the condition to be removed is an equality condition it could be added to ON expressions and/or conditions from disjunctive branches (parts of OR conditions) in an attempt to generate better access keys to the tables of the query. Such equalities are supposed to be removed later from all the formulas where they have been added to. However, erroneously, this was not done in some cases when an ON expression and/or a disjunctive part of the OR condition could be converted into one multiple equality. As a result some equality predicates over columns belonging to the tables of the materialized subquery remained in the ON condition and/or the a disjunctive part of the OR condition, and the excuter later, when trying to evaluate them, returned wrong answers as the values of the fields from these equalities were not valid. This happened because any standalone multiple equality (a multiple equality that are not ANDed with any other predicates) lacked the information about equality predicates inherited from upper levels (in particular, inherited from the WHERE condition). The fix adds a reference to such information to any standalone multiple equality.
    * [Revision #2502.567.70](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.70) \[merge]\
      Wed 2013-02-20 19:22:02 -0800
      * Merge.
      * [Revision #2502.573.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.573.1)\
        Wed 2013-02-20 18:01:36 -0800
        * Fixed bug [MDEV-3913](https://jira.mariadb.org/browse/MDEV-3913). The wrong result set returned by the left join query from the bug test case happened due to several inconsistencies and bugs of the legacy mysql code.
    * [Revision #2502.567.69](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.69)\
      Wed 2013-02-13 11:58:16 +0200
      * Fix for [MDEV-4140](https://jira.mariadb.org/browse/MDEV-4140)
    * [Revision #2502.567.68](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.68) \[merge]\
      Tue 2013-02-12 11:49:46 -0800
      * Merge.
      * [Revision #2502.572.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.572.1)\
        Thu 2013-02-07 21:46:02 -0800
        * Fixed bug [MDEV-3995](https://jira.mariadb.org/browse/MDEV-3995). This bug happened because the executor tried to use a wrong TABLE REF object when building access keys. It constructed keys from fields of a materialized table from a ref object created to construct keys from the fields of the underlying base table. This could happen only when materialized table was created for a non-correlated IN subquery and only when the materialized table used for lookups. In this case we are guaranteed to be able to construct the keys from the fields of tables that would be outer tables for the tables of the IN subquery. The patch makes sure that no ref objects constructed from fields of materialized lookup tables are to be used.
    * [Revision #2502.567.67](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.67)\
      Mon 2013-02-11 10:55:58 +0200
      * [MDEV-4123](https://jira.mariadb.org/browse/MDEV-4123) fix.
    * [Revision #2502.567.66](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.66)\
      Mon 2013-02-04 17:35:48 +0200
      * Fix for bug [MDEV-765](https://jira.mariadb.org/browse/MDEV-765) ([Bug #825075](https://bugs.launchpad.net/bugs/825075))
  * [Revision #3334.1.336](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.336)\
    Thu 2013-02-28 20:19:53 +0100
    * revert
  * [Revision #3334.1.335](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.335) \[merge]\
    Thu 2013-02-28 18:42:49 +0100
    * merge with mysql-5.5.30 minus few incorrect or not applicable changesets
    * [Revision #3077.175.115](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.115)\
      Wed 2013-01-16 08:09:26 +0100
      * Removed Conflicts: mysql-libs mysql-libs-advanced from spec file
    * [Revision #3077.175.114](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.114)\
      Tue 2013-01-15 09:56:36 +0100
      * A bit more intelligent processing of .in files in mysql-test/collections
    * [Revision #3077.175.113](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.113)\
      Tue 2013-01-15 08:52:38 +0100
      * Fix for Bug#14636211 WRONG RESULT (EXTRA ROW) ON A FROM SUBQUERY WITH A VARIABLE AND ORDER BY Bug#16035412 MYSQL SERVER 5.5.29 WRONG SORTING USING COMPLEX INDEX
    * [Revision #3077.175.112](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.112) \[merge]\
      Mon 2013-01-07 16:58:02 +0530
      * Null Merge mysql-5.1 to mysql-5.5
      * [Revision #2661.838.55](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.55)\
        Mon 2013-01-07 16:56:16 +0530
        * Post Fix to Bug#14628410 - ASSERTION \`! IS\_SET()' FAILED IN DIAGNOSTICS\_AREA::SET\_OK\_STATUS
    * [Revision #3077.175.111](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.111) \[merge]\
      Mon 2013-01-07 16:19:06 +0530
      * Merge of patch for Bug#16066243 from mysql-5.1.
      * [Revision #2661.838.54](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.54)\
        Mon 2013-01-07 16:16:08 +0530
        * Bug#16066243 PB2 FAILURES I\_MAIN.BUG15912213 AND I\_MAIN.CTYPE\_UTF8 FOR MACOSX10.6 FOR 5.1
    * [Revision #3077.175.110](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.110) \[merge]\
      Fri 2013-01-04 17:34:02 +0530
      * Merge Post Fix for BUG#14628410 from mysql-5.1 to mysql-5.5
      * [Revision #2661.838.53](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.53)\
        Fri 2013-01-04 17:30:39 +0530
        * Post Fix to Bug#14628410 - ASSERTION \`! IS\_SET()' FAILED IN DIAGNOSTICS\_AREA::SET\_OK\_STATUS
    * [Revision #3077.175.109](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.109) \[merge]\
      Fri 2013-01-04 16:42:49 +0530
      * Merge of patch for bug#16066243 from mysql-5.1.
      * [Revision #2661.838.52](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.52)\
        Fri 2013-01-04 16:38:12 +0530
        * Bug#16066243 PB2 FAILURES I\_MAIN.BUG15912213 AND I\_MAIN.CTYPE\_UTF8 FOR MACOSX10.6 FOR 5.1
    * [Revision #3077.175.108](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.108)\
      Fri 2013-01-04 11:48:11 +0530
    * [Revision #3077.175.107](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.107)\
      Thu 2013-01-03 19:19:28 +0530
    * [Revision #3077.175.106](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.106) \[merge]\
      Wed 2013-01-02 18:32:38 +0530
      * BUG#11753923-SQL THREAD CRASHES ON DISK FULL Merging fix from mysql-5.1
      * [Revision #2661.838.51](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.51)\
        Wed 2013-01-02 16:31:58 +0530
        * BUG#11753923-SQL THREAD CRASHES ON DISK FULL Problem:If Disk becomes full while writing into the binlog, then the server instance hangs till someone frees the space. After user frees up the disk space, mysql server crashes with an assert (m\_status != DA\_EMPTY)
    * [Revision #3077.175.105](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.105)\
      Wed 2013-01-02 11:00:55 +0100
      * Bug#16060864 SEGMENTATION FAULT IN PERFORMANCE\_SCHEMA WITH HISTORY SIZE 0
    * [Revision #3077.175.104](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.104)\
      Wed 2013-01-02 06:18:27 +0100
      * Updated Windows MSI package copyright year to 2013
    * [Revision #3077.175.103](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.103) \[merge]\
      Tue 2013-01-01 03:36:10 +0100
      * Updated README and client executables copyright year to 2013
      * [Revision #2661.838.50](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.50)\
        Tue 2013-01-01 03:33:40 +0100
        * Updated README and client executables copyright year to 2013
    * [Revision #3077.175.102](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.102) \[merge]\
      Sat 2012-12-29 23:49:11 +0530
      * [Revision #2661.838.49](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.49)\
        Sat 2012-12-29 23:46:31 +0530
    * [Revision #3077.175.101](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.101) \[merge]\
      Fri 2012-12-28 16:21:07 +0530
      * BUG#14726272- BACKPORT FIX FOR BUG 11746142 TO 5.5 AND 5.1 Merging fix from mysql-5.1
      * [Revision #2661.838.48](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.48)\
        Fri 2012-12-28 16:13:48 +0530
        * BUG#14726272- BACKPORT FIX FOR BUG 11746142 TO 5.5 AND 5.1 Details of BUG#11746142: CALLING MYSQLD WHILE ANOTHER INSTANCE IS RUNNING, REMOVES PID FILE Fix: Before removing the pid file, ensure it was created by the same process, leave it intact otherwise.
    * [Revision #3077.175.100](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.100) \[merge]\
      Thu 2012-12-27 17:36:11 +0530
      * Merge of patch for Bug#16046140 from mysql-5.1.
      * [Revision #2661.838.47](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.47)\
        Thu 2012-12-27 17:33:34 +0530
        * Bug#16046140 BIN/MYSQLD\_SAFE: TEST: ARGUMENT EXPECTED
    * [Revision #3077.175.99](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.99) \[merge]\
      Thu 2012-12-27 02:43:20 +0100
      * merge
      * [Revision #2661.838.46](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.46)\
        Thu 2012-12-27 02:27:00 +0100
        * Bug#14589559 Post push fix for valgrind warnings.
    * [Revision #3077.175.98](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.98) \[merge]\
      Wed 2012-12-26 20:28:10 +0530
      * Merge from 5.1 to 5.5
      * [Revision #2661.838.45](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.45)\
        Wed 2012-12-26 20:21:19 +0530
        * Bug#12347040: MEMORY LEAK IN CONVERT\_TZ COULD POSSIBLY CAUSE DOS ATTACKS
    * [Revision #3077.175.97](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.97) \[merge]\
      Wed 2012-12-26 12:45:46 +0100
      * Upmerge of the 5.1.67 build
      * [Revision #2661.838.44](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.44) \[merge]\
        Wed 2012-12-26 12:42:47 +0100
        * Merge from mysql-5.1.67-release
    * [Revision #3077.175.96](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.96) \[merge]\
      Mon 2012-12-24 16:51:23 +0530
      * Null merge from mysql-5.1 to mysql-5.5.
      * [Revision #2661.838.43](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.43)\
        Mon 2012-12-24 16:49:42 +0530
        * Fixing a pb2 issue. There is some difference in the output in my local machine and pb2 machines in the explain output.
    * [Revision #3077.175.95](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.95) \[merge]\
      Mon 2012-12-24 06:42:02 +0530
      * Merge from 5.1
      * [Revision #2661.838.42](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.42)\
        Mon 2012-12-24 06:39:54 +0530
        * Bug#11757005: UNION CONVERTS UNSIGNED MEDIUMINT AND BIGINT TO SIGNED Problem: When we are joining types (of fields) in case of a union, we usually upgrade the datatypes to the largest present in the query. In case of mediumint, it is not happening. Analysis: When joined with types LONG and LONGLONG, mediumint should get upgraded to LONG and LONGLONG respectively. W.r.t the given query, constant '1' will be created as a LONGLONG internally and SIGNED flag is enabled. As a result, while combining types for the field, LONGLONG along with MEDIUMINT gets converted to LONG first. LONG with MEDIUMINT(of the third select) gets converted to MEDIUMINT. SIGNED FLAG would be that of the first field's. As a result, the final result would be SIGNED MEDIUMINT. Fix: While joining types, MEDIUMINT with LONGLONG and MEDIUMINT with LONG is converted to LONGLONG and LONG respectively. Also, made some changes for FLOAT and DOUBLE.
    * [Revision #3077.175.94](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.94) \[merge]\
      Fri 2012-12-21 10:26:26 +0100
      * merge 5.1 => 5.5
      * [Revision #2661.838.41](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.41)\
        Thu 2012-12-20 10:56:09 +0100
        * Bug#16027468 ADDRESSSANITIZER BUG IN MYSQLTEST
    * [Revision #3077.175.93](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.93)\
      Fri 2012-12-21 09:53:42 +0100
      * Bug#15972635: Incorrect results returned in 32 table join with HAVING
    * [Revision #3077.175.92](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.92) \[merge]\
      Fri 2012-12-21 11:07:05 +0530
      * Bug#14627287 THREAD CACHE - BYPASSES PRIVILEGES merge from 5.1
      * [Revision #2661.838.40](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.40)\
        Fri 2012-12-21 11:04:49 +0530
        * Bug#14627287 THREAD CACHE - BYPASSES PRIVILEGES
    * [Revision #3077.175.91](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.91)\
      Thu 2012-12-20 19:26:20 +0530
      * Bug #13819630 ARCHIVE TABLE WITH 1000+ PARTITIONS CRASHES SERVER ON "DROP TABLE"
    * [Revision #3077.175.90](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.90)\
      Thu 2012-12-20 11:59:36 +0530
      * Bug #14556349 RENAME OF COMPRESSED TABLE AND INSERT BUFFER MERGE CAUSE HANG
    * [Revision #3077.175.89](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.89) \[merge]\
      Wed 2012-12-19 13:25:07 +0100
      * Merge from mysql-5.5.29-release
    * [Revision #3077.175.88](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.88)\
      Wed 2012-12-19 13:46:00 +0200
      * Fix Bug#16021177 DICT\_LOAD\_FOREIGNS() PASSES UNALIGNED MEMORY TO DTUPLE\_CREATE\_FROM\_MEM()
    * [Revision #3077.175.87](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.87) \[merge]\
      Tue 2012-12-18 21:02:56 +0200
      * Merge mysql-5.1 -> mysql-5.5
      * [Revision #2661.838.39](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.39)\
        Tue 2012-12-18 20:55:30 +0200
        * Fix Bug#16000909 MEMORY LEAK, MYSQL\_INPLACE\_ALTER\_TABLE
    * [Revision #3077.175.86](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.86) \[merge]\
      Tue 2012-12-18 22:16:12 +0530
      * BUG#14727815 - CRASH IN PTHREAD\_RWLOCK\_WRLOCK/SRW\_UNLOCK IN QUERY CACHE CODE
      * [Revision #2661.838.38](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.38)\
        Tue 2012-12-18 22:12:56 +0530
        * BUG#14727815 - CRASH IN PTHREAD\_RWLOCK\_WRLOCK/SRW\_UNLOCK IN QUERY CACHE CODE
    * [Revision #3077.175.85](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.85) \[merge]\
      Tue 2012-12-18 16:52:58 +0200
      * Merge mysql-5.1 -> mysql-5.5
      * [Revision #2661.838.37](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.37)\
        Tue 2012-12-18 16:51:41 +0200
        * Fix Bug#13463493 INNODB PLUGIN WERE CHANGED, BUT STILL USE THE SAME VERSION NUMBER 1.0.17
    * [Revision #3077.175.84](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.84)\
      Mon 2012-12-10 09:55:08 +0100
      * Bug#15960005 VALGRIND WARNINGS IN PROCESS\_ARGS
    * [Revision #3077.175.83](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.83)\
      Mon 2012-12-17 23:13:46 +0800
      * Approved by Jimmy and Inaam. rb#1576
    * [Revision #3077.175.82](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.82) \[merge]\
      Fri 2012-12-14 14:01:43 +0400
      * Auto-merge from mysql-5.1.
      * [Revision #2661.838.36](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.36)\
        Fri 2012-12-14 13:55:30 +0400
        * Fix for BUG#15948580 UPDATE\_XML() CRASHES THE SERVER.
    * [Revision #3077.175.81](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.81) \[merge]\
      Fri 2012-12-14 11:29:07 +0500
      * merge from 5.1
      * [Revision #2661.838.35](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.35)\
        Fri 2012-12-14 11:24:57 +0500
        * Bug#14329288 IS THE CALL TO IBUF\_MERGE\_OR\_DELETE\_FOR\_PAGE FROM BUF\_PAGE\_GET\_GEN REDUNDANT?
    * [Revision #3077.175.80](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.80) \[merge]\
      Thu 2012-12-13 20:58:09 +0530
      * Merging from 5.1 to 5.5 for bug#11761752
      * [Revision #2661.838.34](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.34)\
        Thu 2012-12-13 20:33:44 +0530
        * bug#11761752: DO NOT ALLOW USE OF ALTERNATE DATA STREAMS ON NTFS FILESYSTEM.
    * [Revision #3077.175.79](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.79)\
      Thu 2012-12-13 17:12:21 +0200
      * Follow-up fix to Bug#14628410: Remove the Windows InnoDB Plugin specific implementation of innobase\_mysql\_tmpfile() from MySQL 5.5 onwards.
    * [Revision #3077.175.78](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.78) \[merge]\
      Thu 2012-12-13 18:56:47 +0530
      * Merge fix for Bug#14628410 from mysql-5.1 to mysql-5.5
      * [Revision #2661.838.33](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.33)\
        Thu 2012-12-13 18:53:16 +0530
        * Bug#14628410 - ASSERTION \`! IS\_SET()' FAILED IN DIAGNOSTICS\_AREA::SET\_OK\_STATUS
    * [Revision #3077.175.77](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.77) \[merge]\
      Thu 2012-12-13 10:19:14 +0530
      * Bug#15965288: BUFFER OVERFLOW IN YASSL FUNCTION DOPROCESSREPLY()
      * [Revision #2661.838.32](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.32)\
        Thu 2012-12-13 10:17:26 +0530
        * Bug#15965288: BUFFER OVERFLOW IN YASSL FUNCTION DOPROCESSREPLY()
    * [Revision #3077.175.76](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.76)\
      Wed 2012-12-12 22:31:03 +0530
      * Bug#13639125 DELIMITER STRIPS THE NEXT NEW LINE IN A SQL STATEMENT
    * [Revision #3077.175.75](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.75) \[merge]\
      Wed 2012-12-12 15:10:47 +0530
      * upmerge 14737171 5.1=>5.5
      * [Revision #2661.838.31](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.31)\
        Wed 2012-12-12 15:09:31 +0530
        * Bug #14737171:MTR DOES NOT PRESERVE TEST CASE LOGS ON RETRY-FAIL
    * [Revision #3077.175.74](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.74) \[merge]\
      Tue 2012-12-11 22:04:30 +0400
      * Bug #15954872 "MAKE MDL SUBSYSTEM AND TABLE DEFINITION CACHE ROBUST AGAINST BUGS IN CALLERS".
      * [Revision #2661.838.30](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.30)\
        Tue 2012-12-11 22:00:51 +0400
        * Bug #15954872 "MAKE MDL SUBSYSTEM AND TABLE DEFINITION CACHE ROBUST AGAINST BUGS IN CALLERS".
    * [Revision #3077.175.73](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.73) \[merge]\
      Tue 2012-12-11 18:35:52 +0530
      * upmerge 14737171 5.1 => 5.5
      * [Revision #2661.838.29](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.29)\
        Tue 2012-12-11 18:34:04 +0530
        * Bug #14737171: MTR DOES NOT PRESERVE TEST CASE LOGS ON RETRY-FAIL
    * [Revision #3077.175.72](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.72) \[merge]\
      Tue 2012-12-11 11:30:58 +0100
      * Merge ULN RPM stuff to main branch.
      * [Revision #3077.183.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.183.1)\
        Mon 2012-12-10 09:42:18 +0100
        * RPMs for ULN do not build in MySQL 5.6: Patches + libmysqld.so Bug #15972480
    * [Revision #3077.175.71](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.71) \[merge]\
      Tue 2012-12-11 10:51:24 +0530
      * Merging from mysql-5.1 to mysql-5.5.
      * [Revision #2661.838.28](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.28)\
        Tue 2012-12-11 10:11:24 +0530
        * Bug #14200010 NEWLY CREATED TABLE DOESN'T ALLOW FOR LOOSE INDEX SCANS
    * [Revision #3077.175.70](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.70) \[merge]\
      Sun 2012-12-09 17:26:44 +0530
      * BUG#12359942 - REPLICATION TEST FROM ENGINE SUITE RPL\_ROW\_UNTIL TIMES OUT
      * [Revision #2661.838.27](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.27) \[merge]\
        Sun 2012-12-09 17:21:51 +0530
        * BUG#12359942 - REPLICATION TEST FROM ENGINE SUITE PL\_ROW\_UNTIL TIMES OUT
        * [Revision #2661.843.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.843.1)\
          Sun 2012-12-09 15:50:32 +0530
          * BUG#12359942 - REPLICATION TEST FROM ENGINE SUITE RPL\_ROW\_UNTIL TIMES OUT
    * [Revision #3077.175.69](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.69)\
      Fri 2012-12-07 18:26:02 +0530
      * Bug #15930494 MYSQLDUMP TEST SOMETIMES FAILS DUE TO MIXING STDOUT AND STDERR
    * [Revision #3077.175.68](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.68)\
      Fri 2012-12-07 15:41:49 +0530
    * [Revision #3077.175.67](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.67)\
      Thu 2012-12-06 16:53:02 +0530
      * Bug#15912213: BUFFER OVERFLOW IN ACL\_GET()
    * [Revision #3077.175.66](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.66)\
      Thu 2012-12-06 15:59:15 +0600
      * This patch fixes bug#14729757 - MY\_HASH\_SEARCH(\&XID\_CACHE, XID\_STATE->XID.KEY(), XID\_STATE->XID.KEY\_LENGTH())==0
    * [Revision #3077.175.65](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.65)\
      Wed 2012-12-05 20:41:29 +0400
      * Bug #15948123: SERVER WORKS INCORRECT WITH LONG TABLE ALIASES
    * [Revision #3077.175.64](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.64) \[merge]\
      Wed 2012-12-05 19:50:02 +0400
      * Merged fix for bug #15954896 "SP, MULTI-TABLE DELETE AND LONG ALIAS" into 5.5 tree.
      * [Revision #2661.838.26](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.26)\
        Wed 2012-12-05 19:26:56 +0400
        * Bug #15954896 "SP, MULTI-TABLE DELETE AND LONG ALIAS".
    * [Revision #3077.175.63](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.63)\
      Wed 2012-12-05 16:16:32 +0100
    * [Revision #3077.175.62](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.62)\
      Wed 2012-12-05 15:14:08 +0100
      * Remove moot `--unit-test` option for mtr in collections
    * [Revision #3077.175.61](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.61)\
      Wed 2012-12-05 16:53:33 +0400
      * Bug #15948123: SERVER WORKS INCORRECT WITH LONG TABLE ALIASES
    * [Revision #3077.175.60](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.60) \[merge]\
      Wed 2012-12-05 10:24:45 +0530
      * BUG#12359942 - REPLICATION TEST FROM ENGINE SUITE RPL\_ROW\_UNTIL TIMES OUT
      * [Revision #2661.838.25](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.25) \[merge]\
        Wed 2012-12-05 10:17:53 +0530
        * BUG#12359942 - REPLICATION TEST FROM ENGINE SUITE RPL\_ROW\_UNTIL TIMES OUT
        * [Revision #2661.842.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.842.1)\
          Fri 2012-11-30 12:12:33 +0530
          * BUG#12359942 - REPLICATION TEST FROM ENGINE SUITE RPL\_ROW\_UNTIL TIMES OUT
    * [Revision #3077.175.59](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.59)\
      Tue 2012-12-04 16:09:48 +0000
      * Bug#13545447 RPL\_ROTATE\_LOGS FAILS DUE TO CONCURRENCY ISSUES IN REP. CODE
    * [Revision #3077.175.58](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.58)\
      Tue 2012-12-04 18:14:01 +0530
      * BUG#13812374 - RPL.RPL\_REPORT\_PORT FAILS OCCASIONALLY ON PB2
    * [Revision #3077.175.57](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.57)\
      Tue 2012-12-04 12:32:58 +0900
      * UNIV\_DEBUG build of some environments needs #include "read0read.h" for srv0srv.c and trx0rec.c. This is only for mysql-5.5
    * [Revision #3077.175.56](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.56) \[merge]\
      Sat 2012-12-01 09:17:56 +0100
      * merge mysql-5.1 -> mysql-5.5
      * [Revision #2661.838.24](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.24) \[merge]\
        Sat 2012-12-01 09:07:03 +0100
        * merge of bug#14589559 into mysql-5.1
        * [Revision #2661.841.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.841.2)\
          Fri 2012-11-30 16:17:38 +0100
          * bug#14589559: ASSERTION \`FILE\_ENTRY\_BUF\[2] == 0' FAILED IN DEACTIVATE\_DDL\_LOG\_ENTRY
    * [Revision #3077.175.55](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.55) \[merge]\
      Sat 2012-12-01 09:12:05 +0100
      * merge of bug#14589559 to mysql-5.5
      * [Revision #3077.182.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.182.1) \[merge]\
        Thu 2012-10-18 12:27:02 +0200
        * Manual merge of bug#14589559 from mysql-5.1 to 5.5
        * [Revision #2661.841.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.841.1)\
          Thu 2012-10-18 11:59:47 +0200
          * Bug#14589559: ASSERTION \`FILE\_ENTRY\_BUF\[2] == 0' FAILED IN DEACTIVATE\_DDL\_LOG\_ENTRY
    * [Revision #3077.175.54](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.54) \[merge]\
      Sat 2012-12-01 08:06:45 +0800
      * Auto Merge
      * [Revision #2661.838.23](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.23)\
        Sat 2012-12-01 08:04:33 +0800
        * Bug#11764602 ASSERTION IN FORMAT\_DESCRIPTION\_LOG\_EVENT::CALC\_SERVER\_VERSION\_SPLIT
    * [Revision #3077.175.53](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.53) \[merge]\
      Fri 2012-11-30 16:28:58 +0500
      * merge from 5.1
      * [Revision #2661.838.22](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.22)\
        Fri 2012-11-30 16:19:30 +0500
        * Reverting fix for bug#14329288
    * [Revision #3077.175.52](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.52)\
      Thu 2012-11-29 17:21:36 +0100
      * Bug#11754279 SIGNIFICANT INACCURACY IN DECIMAL MULTIPLICATION CALCULATIONS
    * [Revision #3077.175.51](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.51)\
      Thu 2012-11-29 17:33:06 +0530
      * BUG#15888454: SLAVE CRASHES WHEN DML REQUIRES CONVERSION & TABLE HAS LESS COLUMNS THAN MASTER
    * [Revision #3077.175.50](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.50) \[merge]\
      Thu 2012-11-29 17:24:15 +0530
      * Bug#15912213: BUFFER OVERFLOW IN ACL\_GET()
      * [Revision #2661.838.21](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.21)\
        Thu 2012-11-29 17:23:23 +0530
        * Bug#15912213: BUFFER OVERFLOW IN ACL\_GET()
    * [Revision #3077.175.49](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.49)\
      Wed 2012-11-28 19:01:59 +0530
    * [Revision #3077.175.48](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.48) \[merge]\
      Wed 2012-11-28 17:07:02 +0900
      * Bug#59354 : Bug #12659252 : ASSERT !OTHER\_LOCK AT LOCK\_REC\_ADD\_TO\_QUEUE DURING A DELETE OPERATION The converted implicit lock should wait for the prior conflicting lock if found.
      * [Revision #2661.838.20](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.20)\
        Wed 2012-11-28 17:05:23 +0900
        * Bug#59354 : Bug #12659252 : ASSERT !OTHER\_LOCK AT LOCK\_REC\_ADD\_TO\_QUEUE DURING A DELETE OPERATION The converted implicit lock should wait for the prior conflicting lock if found.
    * [Revision #3077.175.47](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.47) \[merge]\
      Wed 2012-11-28 09:03:37 +0200
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.838.19](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.19)\
        Wed 2012-11-28 09:00:24 +0200
        * Bug#14329288 IS THE CALL TO IBUF\_MERGE\_OR\_DELETE\_FOR\_PAGE FROM BUF\_PAGE\_GET\_GEN REDUNDANT?
    * [Revision #3077.175.46](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.46)\
      Mon 2012-11-26 15:14:26 +0100
      * Reinstate install of mysql-test/lib/My/SafeProcess/Base.pm, removed by mistake
    * [Revision #3077.175.45](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.45) \[merge]\
      Mon 2012-11-26 16:16:49 +0530
      * upmerge 5.1 => 5.5
      * [Revision #2661.838.18](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.18)\
        Mon 2012-11-26 16:09:18 +0530
        * Bug #14757120 - SAFE\_PROCESS.CC/SAFE\_PROCESS.PL SHOULD NOT KILL MYSQLD ON SIGSTOP/SIGCONT
    * [Revision #3077.175.44](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.44)\
      Mon 2012-11-26 15:16:23 +0530
      * Added new line at the end to resolve PB2 per push errors.
    * [Revision #3077.175.43](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.43) \[merge]\
      Mon 2012-11-26 15:59:35 +0900
      * Bug #14676249 : ROW\_VERS\_IMPL\_X\_LOCKED\_LOW() MIGHT HIT !BPAGE->FILE\_PAGE\_WAS\_FREED ASSERTION trx\_undo\_prev\_version\_build() should confirm existence of inherited (not-own) external pages.
      * [Revision #2661.838.17](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.17)\
        Mon 2012-11-26 15:57:26 +0900
        * Bug #14676249 : ROW\_VERS\_IMPL\_X\_LOCKED\_LOW() MIGHT HIT !BPAGE->FILE\_PAGE\_WAS\_FREED ASSERTION trx\_undo\_prev\_version\_build() should confirm existence of inherited (not-own) external pages.
    * [Revision #3077.175.42](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.42) \[merge]\
      Wed 2012-11-21 19:14:15 +0530
      * Bug#15883127: PORT FIX FOR BUG #13904906 TO MYSQL 5.1
      * [Revision #2661.838.16](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.16)\
        Wed 2012-11-21 19:12:20 +0530
        * Bug#15883127: PORT FIX FOR BUG #13904906 TO MYSQL 5.1
    * [Revision #3077.175.41](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.41)\
      Tue 2012-11-20 12:37:23 +0000
      * BUG#15891524: RLI\_FAKE MODE IS NOT UNSET AFTER BINLOG REPLAY
    * [Revision #3077.175.40](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.40)\
      Tue 2012-11-20 15:33:45 +0530
      * BUG #15895810 - REQUIRE ADDITIONAL INFORMATION WITH THE `--RESULT-FILE` OPTION OF MTR
    * [Revision #3077.175.39](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.39)\
      Tue 2012-11-20 11:53:54 +0530
      * Bug#14463669 FAILURE TO CORRECTLY PARSE ROUTINES IN MYSQLDUMP OUTPUT
    * [Revision #3077.175.38](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.38)\
      Tue 2012-11-20 11:30:39 +0530
      * Bug#14463669 FAILURE TO CORRECTLY PARSE ROUTINES IN MYSQLDUMP OUTPUT
    * [Revision #3077.175.37](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.37)\
      Mon 2012-11-19 21:41:35 +0530
      * Bug#14463669 FAILURE TO CORRECTLY PARSE ROUTINES IN MYSQLDUMP OUTPUT
    * [Revision #3077.175.36](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.36)\
      Mon 2012-11-19 14:58:51 +0530
      * Bug#14147491 - INFINITE LOOP WHEN OPENING A CORRUPTED TABLE
    * [Revision #3077.175.35](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.35) \[merge]\
      Fri 2012-11-16 15:26:56 +0100
      * Merge
      * [Revision #3077.181.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.181.1) \[merge]\
        Fri 2012-11-16 15:20:53 +0100
        * Merge
        * [Revision #3077.180.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.180.1) \[merge]\
          Fri 2012-11-16 14:32:37 +0100
          * Merge
          * [Revision #3077.179.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.179.1)\
            Thu 2012-11-15 15:52:51 +0100
            * remove usage of `--skip-ndb` from collections - no need to use `--skip-ndb` in collections files anymore, since long but more clear logic after recent mtr.pl fixes. ndb tests are never run in MySQL Server unless explicitly requested - remove sys\_vars.ndb\_log\_update\_as\_write\_basic.test and sys\_vars.ndb\_log\_updated\_only\_basic.result since MySQL Server does not have those options. - Only sys\_vars.have\_ndbcluster\_basic left since MySQL Server has that variable hardcoded.
    * [Revision #3077.175.34](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.34) \[merge]\
      Fri 2012-11-16 09:06:27 -0500
      * merge from 5.1
      * [Revision #2661.838.15](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.15)\
        Fri 2012-11-16 09:02:35 -0500
        * Bug#15859402 INNODB\_BUFFER\_POOL\_READ\_AHEAD\_EVICTED IS INACCURATE
    * [Revision #3077.175.33](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.33) \[merge]\
      Fri 2012-11-16 13:09:44 +0100
      * merge
      * [Revision #2661.838.14](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.14)\
        Tue 2012-11-13 09:21:59 +0100
        * Bug#14845133:
    * [Revision #3077.175.32](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.32) \[merge]\
      Fri 2012-11-16 13:08:07 +0100
      * merge
      * [Revision #3077.178.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.178.1) \[merge]\
        Tue 2012-11-13 14:47:49 +0100
        * manual merge of bug#14845133 mysql-5.1 -> mysql-5.5
        * [Revision #2661.840.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.840.1)\
          Tue 2012-11-13 09:21:59 +0100
          * Bug#14845133:
    * [Revision #3077.175.31](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.31) \[merge]\
      Fri 2012-11-16 14:47:32 +0530
      * Bug#11753779: MAX\_CONNECT\_ERRORS WORKS ONLY WHEN 1ST INC\_HOST\_ERRORS() IS CALLED.
      * [Revision #2661.838.13](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.13)\
        Fri 2012-11-16 14:43:10 +0530
    * [Revision #3077.175.30](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.30) \[merge]\
      Thu 2012-11-15 22:11:03 +0200
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.838.12](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.12)\
        Thu 2012-11-15 22:05:08 +0200
        * Bug#15872736 FAILING ASSERTION
    * [Revision #3077.175.29](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.29) \[merge]\
      Thu 2012-11-15 20:38:04 +0200
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.838.11](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.11)\
        Thu 2012-11-15 20:30:36 +0200
        * Bug#15874001 CREATE INDEX ON A UTF8 CHAR COLUMN FAILS WITH ROW\_FORMAT=REDUNDANT
    * [Revision #3077.175.28](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.28)\
      Thu 2012-11-15 12:27:05 +0530
    * [Revision #3077.175.27](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.27)\
      Wed 2012-11-14 17:17:14 +0000
      * BUG#12669186: AUTOINC VALUE PERSISTENCY BREAKS CERTAIN REPLICATION SCENARIOS
    * [Revision #3077.175.26](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.26)\
      Wed 2012-11-14 17:02:36 +0530
      * BUG#13556107: CHECK AND REPAIR TABLE SHOULD BE MORE ROBUST \[3]
    * [Revision #3077.175.25](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.25)\
      Wed 2012-11-14 16:35:08 +0530
    * [Revision #3077.175.24](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.24) \[merge]\
      Wed 2012-11-14 15:30:23 +0530
      * [Revision #2661.838.10](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.10)\
        Wed 2012-11-14 14:57:28 +0530
    * [Revision #3077.175.23](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.23)\
      Wed 2012-11-14 17:00:41 +0800
      * Fix Bug #14753402 - FAILING ASSERTION: LEN == IFIELD->FIXED\_LEN
    * [Revision #3077.175.22](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.22) \[merge]\
      Wed 2012-11-14 11:02:13 +0530
      * [Revision #2661.838.9](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.9)\
        Wed 2012-11-14 10:40:20 +0530
    * [Revision #3077.175.21](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.21) \[merge]\
      Tue 2012-11-13 19:13:59 +0100
      * Merge
      * [Revision #3077.177.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.177.2)\
        Sun 2012-11-04 22:17:17 +0100
        * mtr.pl - remove unused hack to turn on extra suites based on current directory name - remove 4 your old debug printout of "vardir:"
      * [Revision #3077.177.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.177.1)\
        Sun 2012-11-04 22:11:34 +0100
        * mtr.pl - improve the logic that decides when ndbcluster should be enabled and the extra test suites for MySQL Cluster should be added. Should be consistent and logical now ;)
    * [Revision #3077.175.20](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.20)\
      Mon 2012-11-12 14:24:43 +0200
      * This is a backport of "[WL#5674](https://askmonty.org/worklog/?tid=5674) InnoDB: report all deadlocks (Bug#1784)" from MySQL 5.6 into MySQL 5.5
    * [Revision #3077.175.19](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.19) \[merge]\
      Mon 2012-11-12 22:33:40 +0900
      * Bug #14676111 WRONG PAGE\_LEVEL WRITTEN FOR UPPER THAN FATHER PAGE AT BTR\_LIFT\_PAGE\_UP()
      * [Revision #2661.838.8](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.8)\
        Mon 2012-11-12 22:31:30 +0900
        * Bug #14676111 WRONG PAGE\_LEVEL WRITTEN FOR UPPER THAN FATHER PAGE AT BTR\_LIFT\_PAGE\_UP()
    * [Revision #3077.175.18](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.18)\
      Fri 2012-11-09 15:51:28 +0100
    * [Revision #3077.175.17](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.17)\
      Fri 2012-11-09 19:19:11 +0530
      * Bug#13556000: CHECK AND REPAIR TABLE SHOULD BE MORE ROBUST\[2]
    * [Revision #3077.175.16](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.16) \[merge]\
      Fri 2012-11-09 19:04:59 +0530
      * Null merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.838.7](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.7)\
        Fri 2012-11-09 19:04:01 +0530
        * Bug #14669848 CRASH DURING ALTER MAKES ORIGINAL TABLE INACCESSIBLE
    * [Revision #3077.175.15](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.15) \[merge]\
      Fri 2012-11-09 18:56:20 +0530
      * Merging from mysql-5.1 to mysql-5.5.
      * [Revision #2661.839.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.839.1)\
        Thu 2012-11-08 18:09:13 +0530
        * Bug #14669848 CRASH DURING ALTER MAKES ORIGINAL TABLE INACCESSIBLE
    * [Revision #3077.175.14](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.14) \[merge]\
      Fri 2012-11-09 15:16:49 +0530
      * BUG#11762933: MYSQLDUMP WILL SILENTLY SKIP THE `EVENT` TABLE DATA IF DUMPS MYSQL DATABA Problem: If mysqldump is run without `--events` (or with `--skip-events`) it will not dump the mysql.event table's data. This behaviour is inconsistent with that of `--routines` option, which does not affect the dumping of mysql.proc table. According to the Manual, `--events` (`--skip-events`) defines, if the Event Scheduler events for the dumped databases should be included in the mysqldump output and this has nothing to do with the mysql.event table itself. Solution: A warning has been added when mysqldump is used without `--events` (or with `--skip-events`) and a separate patch with the behavioral change will be prepared for 5.6/trunk.
      * [Revision #2661.838.6](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.6)\
        Fri 2012-11-09 15:15:16 +0530
        * BUG#11762933: MYSQLDUMP WILL SILENTLY SKIP THE `EVENT` TABLE DATA IF DUMPS MYSQL DATABA Problem: If mysqldump is run without `--events` (or with `--skip-events`) it will not dump the mysql.event table's data. This behaviour is inconsistent with that of `--routines` option, which does not affect the dumping of mysql.proc table. According to the Manual, `--events` (`--skip-events`) defines, if the Event Scheduler events for the dumped databases should be included in the mysqldump output and this has nothing to do with the mysql.event table itself. Solution: A warning has been added when mysqldump is used without `--events` (or with `--skip-events`) and a separate patch with the behavioral change will be prepared for 5.6/trunk.
    * [Revision #3077.175.13](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.13)\
      Fri 2012-11-09 14:54:35 +0530
      * BUG#14458232 - CRASH IN THD\_IS\_TRANSACTION\_ACTIVE DURING THREAD POOLING STRESS TEST PROBLEM: Connection stress tests which consists of concurrent kill connections interleaved with mysql ping queries cause the mysqld server which uses thread pool scheduler to crash. FIX: Killing a connection involves shutdown and close of client socket and this can cause EPOLLHUP(or EPOLLERR) events to be to be queued and handled after disarming and cleanup of the connection object (THD) is being done.We disarm the connection by modifying the epoll mask to zero which ensure no events come and release the ownership of waiting thread that collect events and then do the cleanup of THD. object.As per the linux kernel epoll source code ( [eventpoll.c#L1771](https://lxr.linux.no/linux+*/fs/eventpoll.c#L1771)), EPOLLHUP (or EPOLLERR) can't be masked even if we set EPOLL mask to zero. So we disarm the connection and thus prevent execution of any query processing handler/queueing to client ctx. queue by removing the client fd from the epoll set via EPOLL\_CTL\_DEL. Also there is a race condition which involve the following threads: 1) Thread X executing KILL CONNECTION Y and is in THD::awake and using mysys\_var (holding LOCK\_thd\_data). 2) Thread Y in tp\_process\_event executing and is being killed. 3) Thread Z receives KILL flag internally and possible call the tp\_thd\_cleanup function which set thread session variable and changing mysys\_var. The fix for the above race is to set thread session variable under LOCK\_thd\_data. We also do not call THD::awake if we found the thread in the thread list that is to be killed but it's KILL\_CONNECTION flag set thus avoiding any possible concurrent cleanup. This patch is approved by Mikael Ronstrom via email review.
    * [Revision #3077.175.12](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.12) \[merge]\
      Thu 2012-11-08 19:23:54 +0100
      * Merge the ULN RPM fix into main.
      * [Revision #3077.176.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.176.1)\
        Thu 2012-11-08 15:49:28 +0100
        * Building RPMs for ULN:
    * [Revision #3077.175.11](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.11) \[merge]\
      Thu 2012-11-08 15:21:02 +0530
      * Bug#14234028 - CRASH DURING SHUTDOWN WITH BACKGROUND PURGE THREAD
      * [Revision #2661.838.5](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.5)\
        Thu 2012-11-08 15:14:29 +0530
        * Bug#14234028 - CRASH DURING SHUTDOWN WITH BACKGROUND PURGE THREAD
    * [Revision #3077.175.10](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.10) \[merge]\
      Thu 2012-11-08 14:23:02 +0530
      * Bug#11751825 - OPTIMIZE PARTITION RECREATES FULL TABLE INSTEAD JUST PARTITION
      * [Revision #2661.838.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.4)\
        Thu 2012-11-08 14:19:27 +0530
        * Bug#11751825 - OPTIMIZE PARTITION RECREATES FULL TABLE INSTEAD JUST PARTITION
    * [Revision #3077.175.9](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.9)\
      Wed 2012-11-07 20:32:54 +0100
      * Make RPMs for ULN build again.
    * [Revision #3077.175.8](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.8)\
      Wed 2012-11-07 17:45:02 +0100
      * Placement change:
    * [Revision #3077.175.7](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.7)\
      Wed 2012-11-07 19:08:33 +0530
      * Bug#14466617 - INVALID WRITES AND/OR CRASH WITH USER VARIABLES
    * [Revision #3077.175.6](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.6)\
      Wed 2012-11-07 18:41:42 +0530
    * [Revision #3077.175.5](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.5) \[merge]\
      Wed 2012-11-07 09:03:33 +0530
      * Bug #11759445: CAN'T DELETE ROWS FROM MEMORY TABLE WITH HASH KEY.
      * [Revision #2661.838.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.3)\
        Wed 2012-11-07 09:00:17 +0530
        * Bug #11759445: CAN'T DELETE ROWS FROM MEMORY TABLE WITH HASH KEY.
    * [Revision #3077.175.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.4) \[merge]\
      Tue 2012-11-06 18:44:22 +0530
      * Bug#11751825 - OPTIMIZE PARTITION RECREATES FULL TABLE INSTEAD JUST PARTITION
      * [Revision #2661.838.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.2)\
        Tue 2012-11-06 18:35:03 +0530
        * Bug#11751825 - OPTIMIZE PARTITION RECREATES FULL TABLE INSTEAD JUST PARTITION
    * [Revision #3077.175.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.3)\
      Mon 2012-11-05 17:45:13 +0530
    * [Revision #3077.175.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.2) \[merge]\
      Mon 2012-11-05 12:08:05 +0100
      * Version change upmerge - empty
      * [Revision #2661.838.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.838.1)\
        Mon 2012-11-05 11:05:46 +0100
        * Raise version number after cloning 5.1.67
    * [Revision #3077.175.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.175.1)\
      Sat 2012-11-03 05:06:09 +0100
      * Raise version number after cloning 5.5.29
  * [Revision #3334.1.334](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.334)\
    Wed 2013-02-27 10:43:07 +0400
    * [MDEV-4208](https://jira.mariadb.org/browse/MDEV-4208): Test rpl.rpl\_rotate\_purge\_deadlock has incorrect preamble
  * [Revision #3334.1.333](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.333)\
    Sun 2013-02-24 20:05:26 +0100
    * Compilation : fix oqgraph's system check, in case where boost header aren't in standard include directory.
  * [Revision #3334.1.332](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.332)\
    Thu 2013-02-21 22:59:54 +0100
    * [MDEV-4190](https://jira.mariadb.org/browse/MDEV-4190) : Fix system checks for OpenBSD
  * [Revision #3334.1.331](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.331)\
    Thu 2013-02-21 21:46:24 +0100
    * [MDEV-4021](https://jira.mariadb.org/browse/MDEV-4021) : Enable Ctrl-C handler when reading password, on Windows.
  * [Revision #3334.1.330](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.330)\
    Wed 2013-02-20 14:52:43 +0100
    * [MDEV-4181](https://jira.mariadb.org/browse/MDEV-4181) : ensure mysql client's beep works on all Windows systems. Use MessageBeep, which employs sound card, rather than system speaker. The secondary benefit is that one can use volume control for this sound (see MySQL's Bug #17088)
  * [Revision #3334.1.329](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.329)\
    Thu 2013-02-21 01:03:45 +0400
    * [MDEV-3819](https://jira.mariadb.org/browse/MDEV-3819) missing constraints for spatial column types. Checks added to return and error when inappropriate geometry type is stored in a field.
  * [Revision #3334.1.328](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.328)\
    Tue 2013-02-19 23:46:52 +0100
    * [MDEV-4174](https://jira.mariadb.org/browse/MDEV-4174) - Use kqueue for threadpool implementation on more BSD variants than just FreeBSD or OSX - i.e NetBSD, OpenBSD, DragonFly, etc.
  * [Revision #3334.1.327](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.327)\
    Mon 2013-02-18 20:51:36 +0100
    * fix typo
  * [Revision #3334.1.326](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.326)\
    Mon 2013-02-18 20:35:11 +0100
    * [MDEV-4183](https://jira.mariadb.org/browse/MDEV-4183): Export additional symbols from RPMs , compatibly to distribution RPMs. -Ensure that symbols listed in CLIENT\_API\_EXTRA are not thrown away by the linker. -Add THR\_KEY\_mysys to this list, because Fedora18 exports it.
  * [Revision #3334.1.325](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.325)\
    Fri 2013-02-08 22:24:06 +0100
    * [MDEV-4156](https://jira.mariadb.org/browse/MDEV-4156) Test cases query\_cache and query\_cache\_size\_basic fail on 32 bit ppc and s390
  * [Revision #3334.1.324](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.324)\
    Fri 2013-02-08 12:59:54 +0100
    * make rpm packages to respect CMAKE\_INSTALL\_PREFIX
* [Revision #3392](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3392)\
  Tue 2013-05-21 00:10:35 +0300
  * merged in revisions 3853..3857 from lp:codership-mysql/5.5-23
* [Revision #3391](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3391)\
  Tue 2013-03-26 16:40:02 +0200
  * References: [MDEV-4328](https://jira.mariadb.org/browse/MDEV-4328) - avoiding race condition for wsrep\_format\_desc access

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
