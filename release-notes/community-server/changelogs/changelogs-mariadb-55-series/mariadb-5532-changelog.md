# MariaDB 5.5.32 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.32) | [Release Notes](../../old-releases/5.5/5.5.32.md) | **Changelog** | \[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 18 Jul 2013

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.32.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3838](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3838)\
  Wed 2013-07-17 17:03:59 +0300
  * Revert of marko.makela@oracle.com-20130430103950-j353faze84zzk9xf for xtradb (fix of [MySQL Bug #69623](https://bugs.mysql.com/bug.php?id=69623))
* [Revision #3837](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3837)\
  Wed 2013-07-17 16:42:13 +0300
  * Fix for [MDEV-4219](https://jira.mariadb.org/browse/MDEV-4219) A simple select query returns random data (upstream [MySQL Bug #68473](https://bugs.mysql.com/bug.php?id=68473))
* [Revision #3836](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3836) \[merge]\
  Tue 2013-07-16 19:30:39 +0200
  * merge Percona-Server-5.5.32-rel31.0.tar.gz
  * [Revision #0.12.63](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.63)\
    Tue 2013-07-16 14:55:47 +0200
    * Percona-Server-5.5.32-rel31.0.tar.gz
* [Revision #3835](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3835) \[merge]\
  Tue 2013-07-16 19:09:54 +0200
  * mysql-5.5.32 merge
  * [Revision #3077.187.102](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.102)\
    Thu 2013-05-16 17:33:32 +0200
    * Fix for bug#16812255: Removing the `--random-password` option which is supported only for MYSQL server versions 5.6 and above.
  * [Revision #3077.187.101](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.101)\
    Thu 2013-05-16 10:24:26 +0200
    * Changes to verify the solaris upgrade issue.
  * [Revision #3077.187.100](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.100)\
    Wed 2013-05-15 16:29:31 +0200
    * Fixing the RPM-ULN build issue by ignoring the postinstall\_check.sh.
  * [Revision #3077.187.99](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.99)\
    Wed 2013-05-15 15:37:20 +0200
    * Bug 16812255 - 5.5.32 pkg installation failed during MYSQL\_INSTALL\_DB execution
  * [Revision #3077.187.98](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.98)\
    Mon 2013-05-13 10:21:09 +0200
    * Updated copyright year information
  * [Revision #3077.187.97](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.97)\
    Mon 2013-05-13 09:46:44 +0200
    * Adding fix for Bug#16798868
  * [Revision #3077.187.96](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.96)\
    Wed 2013-05-08 12:08:20 +0200
    * Bug#16779374: new error message added to 5.5 after 5.6 GA - reusing number already used by 5.6
  * [Revision #3077.187.95](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.95)\
    Tue 2013-05-07 14:36:46 +0200
    * ULN-RPMs bug fix for BR16298542
  * [Revision #3077.187.94](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.94)\
    Mon 2013-05-06 20:31:26 +0530
    * Bug #16722314 foreign key id modified during export Bug #16754901 PARS\_INFO\_FREE not called in DICT\_CREATE\_ADD\_FOREIGN\_TO\_DICTIONARY
  * [Revision #3077.187.93](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.93)\
    Mon 2013-05-06 16:06:32 +0200
    * Bug#16757869: InnoDB: possible regression in 5.5.31, BUG#16004999
  * [Revision #3077.187.92](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.92)\
    Mon 2013-05-06 15:19:37 +0200
    * Updated spec file for Bug#16488773
  * [Revision #3077.187.91](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.91)\
    Fri 2013-05-03 16:39:17 +0300
  * [Revision #3077.187.90](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.90) \[merge]\
    Tue 2013-04-30 20:40:38 +0200
    * merge from mysql-5.1
    * [Revision #2661.848.26](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.26)\
      Tue 2013-04-30 20:39:12 +0200
      * Bug#16405422 - recovery failure, assert !RECV\_NO\_LOG\_WRITE
  * [Revision #3077.187.89](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.89) \[merge]\
    Tue 2013-04-30 22:46:37 +0530
    * BUG#16222245 - crash with explain for a query with loose scan for group by, MyISAM
    * [Revision #2661.848.25](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.25)\
      Tue 2013-04-30 22:38:34 +0530
      * BUG#16222245 - crash with explain for a query with loose scan for group by, MyISAM
  * [Revision #3077.187.88](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.88)\
    Tue 2013-04-30 13:39:50 +0300
    * Bug#16720368 InnoDB ignores \*.IBD file breakage at startup
  * [Revision #3077.187.87](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.87)\
    Sat 2013-04-27 16:04:54 +0800
    * Bug #13004581 blackhole binary log with row ignores update and delete statements
  * [Revision #3077.187.86](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.86)\
    Thu 2013-04-25 11:56:26 +0530
    * BUG#16698172-cannot do point-in-time recovery for single database; mysqlbinlog
  * [Revision #3077.187.85](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.85)\
    Wed 2013-04-24 17:21:42 +0300
    * Bug #16680313: client doesn't read plugin-dir from my.cnf set by MYSQL\_READ\_DEFAULT\_FILE Parsing of the plugin-dir config file option was not working due to a typo. Fixed the typo. No test case can be added due to lack of support for defaults-exitra-file testing in mysql-test-run.pl. Thanks to Sinisa for contributing the fix.
  * [Revision #3077.187.84](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.84) \[merge]\
    Wed 2013-04-24 13:34:11 +0530
    * [Revision #2661.848.24](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.24)\
      Wed 2013-04-24 13:31:10 +0530
  * [Revision #3077.187.83](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.83) \[merge]\
    Wed 2013-04-24 08:48:34 +0200
    * Null merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.23](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.23)\
      Wed 2013-04-24 08:47:30 +0200
      * Bug #15973904 InnoDB partition code holds lock\_open and sleeps while opening missing partition
  * [Revision #3077.187.82](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.82)\
    Wed 2013-04-24 08:42:59 +0200
    * Merge from mysql-5.1 to mysql-5.5
  * [Revision #3077.187.81](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.81) \[merge]\
    Mon 2013-04-22 14:30:47 +0200
    * Upmerge of the 5.1.69 build
    * [Revision #2661.848.22](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.22)\
      Mon 2013-04-22 14:01:07 +0200
      * Merge from mysql-5.1.69-release
  * [Revision #3077.187.80](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.80) \[merge]\
    Sat 2013-04-20 12:36:11 +0530
    * Bug#16073689 : crash in ITEM\_FUNC\_MATCH::INIT\_SEARCH
    * [Revision #2661.848.21](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.21)\
      Sat 2013-04-20 12:28:22 +0530
      * Bug#16073689 : crash in ITEM\_FUNC\_MATCH::INIT\_SEARCH
  * [Revision #3077.187.79](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.79) \[merge]\
    Thu 2013-04-18 12:52:59 +0200
    * Merge from mysql-5.5.31-release
  * [Revision #3077.187.78](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.78)\
    Wed 2013-04-17 09:26:51 +0200
    * Bug#16626742 in MY\_MD5FINAL in MYSYS/MD5.C, CTX is not properly zeroed as intended
  * [Revision #3077.187.77](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.77)\
    Tue 2013-04-16 16:26:45 +0530
    * Bug #16632543 - incorrect value of bogomips in mysqltest
  * [Revision #3077.187.76](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.76) \[merge]\
    Tue 2013-04-16 12:17:18 +0200
    * Merging the changes for Bug 16633169 - MYSQL.INFO contains outdated information.
    * [Revision #2661.848.20](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.20)\
      Tue 2013-04-16 12:12:18 +0200
      * Bug 16633169 - MYSQL.INFO contains outdated information.
  * [Revision #3077.187.75](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.75) \[merge]\
    Sun 2013-04-14 08:09:56 +0530
    * Merge from 5.1 to 5.5
    * [Revision #2661.848.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.19)\
      Sun 2013-04-14 07:30:49 +0530
      * Bug#16347426:assertion failed: (SELECT\_INSERT && !TABLES->NEXT\_NAME\_RESOLUTION\_TABLE) || !TAB
  * [Revision #3077.187.74](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.74)\
    Fri 2013-04-12 14:18:21 +0530
    * BUG#16615117 mysqldump produces a change master statement with a port number enclosed in quotes
  * [Revision #3077.187.73](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.73)\
    Fri 2013-04-12 09:39:56 +0200
    * Bug#16540042: wrong query result when using range over partial index
  * [Revision #3077.187.72](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.72)\
    Thu 2013-04-11 10:50:50 +0800
    * Bug :#16005310 Fix bug - innodb\_row\_lock\_time\_max seems to have an overflow
  * [Revision #3077.187.71](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.71)\
    Wed 2013-04-10 16:43:09 +0200
    * Bug#16395606 scripts missing execute bit
  * [Revision #3077.187.70](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.70)\
    Wed 2013-04-10 11:50:41 +0530
    * BUG#16402143 - stack corruption in dbug\_explain description and fix: DBUG\_EXPLAIN result in buffer overflow when the DEBUG variable values length exceed 255. In _db\_explain_ function which call macro str\_to\_buf incorrectly passes the length of buf avaliable to strnmov as len+1. The fix calculates the avaliable space in buf and passes it to strnxmov.
  * [Revision #3077.187.69](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.69) \[merge]\
    Tue 2013-04-09 14:03:35 +0530
    * local merge.
    * [Revision #2661.848.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.18)\
      Tue 2013-04-09 14:00:05 +0530
      * Backporting patch for bug#15852074.
  * [Revision #3077.187.68](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.68) \[merge]\
    Mon 2013-04-08 18:53:24 +0530
    * null merge
    * [Revision #2661.848.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.17)\
      Mon 2013-04-08 18:48:57 +0530
  * [Revision #3077.187.67](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.67) \[merge]\
    Mon 2013-04-08 18:14:06 +0530
    * [Revision #2661.848.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.16)\
      Mon 2013-04-08 18:12:39 +0530
  * [Revision #3077.187.66](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.66)\
    Mon 2013-04-08 15:25:45 +0530
    * BUG#15978766 - test valgrind\_report fails innodb tests
  * [Revision #3077.187.65](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.65)\
    Thu 2013-04-04 14:54:16 +0530
    * Bug #16401597 - mtr v1 returns incorrect path to variable @@basedir
  * [Revision #3077.187.64](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.64)\
    Wed 2013-04-03 18:09:37 +0200
    * Bug 16534721 - mysql\_install\_db runs again during upgrade even data directory exists
  * [Revision #3077.187.63](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.63) \[merge]\
    Tue 2013-04-02 16:20:49 +0200
    * merge 5.1 => 5.5
    * [Revision #2661.848.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.15)\
      Tue 2013-04-02 16:05:10 +0200
      * Bug#14700180 crash in COPY\_FUNCS This is a backport of the fix for Bug#13966809 crash in copy\_funcs when grouping by outer query blob field in subquery
  * [Revision #3077.187.62](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.62)\
    Tue 2013-04-02 11:14:39 +0200
    * Bug#11765629 cmake: can suppress installation of sql-bench, but not mysql-test
  * [Revision #3077.187.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.61) \[merge]\
    Tue 2013-04-02 11:17:06 +0530
    * [Revision #2661.848.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.14)\
      Tue 2013-04-02 11:16:26 +0530
  * [Revision #3077.187.60](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.60) \[merge]\
    Mon 2013-04-01 13:45:27 +0530
    * [Revision #2661.848.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.13)\
      Mon 2013-04-01 12:26:55 +0530
  * [Revision #3077.187.59](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.59) \[merge]\
    Sun 2013-03-31 06:52:16 +0530
    * Merge from 5.1 to 5.5
    * [Revision #2661.848.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.12)\
      Sun 2013-03-31 06:48:30 +0530
      * Bug #16347343 : crash, group\_concat, derived tables
  * [Revision #3077.187.58](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.58)\
    Sat 2013-03-30 19:24:54 +0530
    * Bug#14261010: on duplicate key update crashes the server
  * [Revision #3077.187.57](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.57) \[merge]\
    Fri 2013-03-29 22:11:33 +0530
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.11)\
      Fri 2013-03-29 22:01:10 +0530
      * Bug #16244691 server gone away error occurs depending on the number of table/key relations
  * [Revision #3077.187.56](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.56)\
    Fri 2013-03-29 16:33:33 +0530
    * Bug #16402124 - mtr processes certain assigned vardir values wrong
  * [Revision #3077.187.55](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.55) \[merge]\
    Fri 2013-03-29 15:14:38 +0530
    * [Revision #2661.848.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.10)\
      Fri 2013-03-29 15:09:14 +0530
  * [Revision #3077.187.54](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.54)\
    Fri 2013-03-29 11:44:42 +0530
  * [Revision #3077.187.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.53)\
    Fri 2013-03-29 09:28:31 +0530
    * Bug#15948818-semi-sync enabled master crashes when event scheduler drops events
  * [Revision #3077.187.52](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.52) \[merge]\
    Thu 2013-03-28 17:41:22 +0200
    * merge
    * [Revision #2661.848.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.9)\
      Thu 2013-03-28 17:37:29 +0200
      * Addendum #1 to the fix for bug #16451878 : geometry query crashes server
  * [Revision #3077.187.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.51) \[merge]\
    Thu 2013-03-28 19:17:28 +0530
    * Merge from 5.1 to 5.5
    * [Revision #2661.848.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.8)\
      Thu 2013-03-28 19:11:26 +0530
      * BUG#11753852: if() values are evaluated differently in a regular sql vs prepared statement
  * [Revision #3077.187.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.50) \[merge]\
    Thu 2013-03-28 14:18:51 +0530
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.7)\
      Thu 2013-03-28 14:14:39 +0530
      * Bug#14324766:partially written insert statement in binlog no errors reported
  * [Revision #3077.187.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.49)\
    Thu 2013-03-28 11:47:43 +0530
    * Bug #16403186 - mtr on windows should not try to start cdb if running with parallel
  * [Revision #3077.187.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.48) \[merge]\
    Thu 2013-03-28 10:43:50 +0530
    * Null merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.6)\
      Thu 2013-03-28 10:42:42 +0530
      * Bug #16244691 server gone away error occurs depending on the number of table/key relations
  * [Revision #3077.187.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.47) \[merge]\
    Thu 2013-03-28 10:25:23 +0530
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.849.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.849.1)\
      Wed 2013-03-27 11:11:38 +0530
      * Bug #16244691 server gone away error occurs depending on the number of table/key relations
  * [Revision #3077.187.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.46) \[merge]\
    Wed 2013-03-27 16:06:33 +0200
    * merge 5.1->5.5
    * [Revision #2661.848.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.5)\
      Wed 2013-03-27 16:03:00 +0200
      * Bug #16451878: geometry query crashes server
  * [Revision #3077.187.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.45) \[merge]\
    Wed 2013-03-27 11:22:25 +0000
    * BUG#16541422: log-slave-updates + replicate-wild-ignore-table fails for user variables
    * [Revision #2661.848.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.4)\
      Wed 2013-03-27 11:19:29 +0000
      * BUG#16541422: log-slave-updates + replicate-wild-ignore-table fails for user variables
  * [Revision #3077.187.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.44) \[merge]\
    Wed 2013-03-27 11:59:40 +0530
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.3)\
      Wed 2013-03-27 11:53:01 +0530
      * Bug#11829838: alter table not binlogged with `--binlog-ignore-db` and fully qualified table
  * [Revision #3077.187.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.43) \[merge]\
    Tue 2013-03-26 23:11:55 +0200
    * merge from 5.1->5.5 repo.
    * [Revision #2661.848.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.2) \[merge]\
      Tue 2013-03-26 23:10:42 +0200
      * merge from 5.1 repo.
  * [Revision #3077.187.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.42)\
    Tue 2013-03-26 21:45:39 +0200
  * [Revision #3077.187.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.41) \[merge]\
    Tue 2013-03-26 20:52:01 +0200
    * merge from 5.1
    * [Revision #2661.848.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.1)\
      Tue 2013-03-26 19:24:01 +0200
      * Bug#16541422 log-slave-updates + replicate-wild-ignore-table fails for user variables
  * [Revision #3077.187.40](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.40) \[merge]\
    Tue 2013-03-26 08:24:11 +0100
    * NULL merge 5.1 => 5.5
    * [Revision #2661.844.69](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.69)\
      Tue 2013-03-26 08:22:45 +0100
      * Bug#62856 Check for "stack overrun" doesn't work with gcc-4.6, server crashes Bug#13243248 CHECK FOR "STACK OVERRUN" DOESN'T WORK WITH GCC-4.6, SERVER CRASHES
  * [Revision #3077.187.39](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.39)\
    Mon 2013-03-25 11:27:12 +0530
    * BUG#16438800 - slave\_max\_allowed\_packet not honored on slave io connect
  * [Revision #3077.187.38](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.38) \[merge]\
    Fri 2013-03-22 20:16:53 +0530
    * local merge.
    * [Revision #2661.844.68](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.68)\
      Fri 2013-03-22 20:00:40 +0530
      * Bug#12671635 : Updating embedded tests.
  * [Revision #3077.187.37](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.37) \[merge]\
    Fri 2013-03-22 15:33:59 +0530
    * local merge.
    * [Revision #2661.844.67](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.67)\
      Fri 2013-03-22 15:29:57 +0530
      * Bug#12671635 : Fixing test cases.
  * [Revision #3077.187.36](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.36)\
    Fri 2013-03-22 14:55:30 +0530
    * Bug#16500013 : post-fix
  * [Revision #3077.187.35](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.35) \[merge]\
    Thu 2013-03-21 23:40:25 +0530
    * Merge of patch for Bug#12671635 from mysql-5.1.
    * [Revision #2661.844.66](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.66)\
      Thu 2013-03-21 23:36:02 +0530
      * Bug#12671635 HELP-TABLEFORMAT DOESN'T MATCH HELP-FILES
  * [Revision #3077.187.34](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.34)\
    Thu 2013-03-21 22:51:40 +0530
    * Bug#16500013 : ADD VERSION CHECK TO MYSQL\_UPGRADE
  * [Revision #3077.187.33](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.33)\
    Thu 2013-03-21 11:40:43 +0530
    * Bug #16051728 server crashes in add\_identifier on concurrent alter table and show engine innod
  * [Revision #3077.187.32](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.32) \[merge]\
    Wed 2013-03-20 17:52:15 +0100
    * Null merge from 5.1 for permission changes.
    * [Revision #2661.844.65](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.65)\
      Wed 2013-03-20 17:49:30 +0100
      * Correcting the permissions of executable files.
  * [Revision #3077.187.31](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.31)\
    Wed 2013-03-20 17:50:15 +0100
    * Correcting the permissions of the executable files.
  * [Revision #3077.187.30](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.30)\
    Tue 2013-03-19 17:09:17 +0100
    * Bug#13009341 crash in str\_to\_datetime after misbehaving "blob" value comparison
  * [Revision #3077.187.29](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.29)\
    Wed 2013-03-20 11:20:12 +0100
    * Bug#16394084: loose index scan with quoted int predicate returns random data
  * [Revision #3077.187.28](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.28)\
    Tue 2013-03-19 15:08:19 +0100
    * Bug#16359402 crash with aggregates: assertion failed: n < m\_size
  * [Revision #3077.187.27](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.27)\
    Tue 2013-03-19 15:53:48 +0100
    * Fix for Bug 16395495 - old fsf address in gpl header
  * [Revision #3077.187.26](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.26) \[merge]\
    Tue 2013-03-19 13:36:34 +0100
    * Upmerging the changes for Bug 16395495 from 5.1
    * [Revision #2661.844.64](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.64)\
      Tue 2013-03-19 13:29:12 +0100
      * Bug 16395495 - old fsf address in gpl header
  * [Revision #3077.187.25](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.25)\
    Mon 2013-03-18 17:20:30 +0200
    * Fix Bug#16400412 unnecessary dict\_update\_statistics during concurrent updates
  * [Revision #3077.187.24](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.24) \[merge]\
    Tue 2013-03-19 05:35:30 +0100
    * Upmerging the changes for Bug 16401147 from 5.1
    * [Revision #2661.844.63](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.63)\
      Tue 2013-03-19 05:19:31 +0100
      * Bug 16401147 - crlf instead of lf in readme
  * [Revision #3077.187.23](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.23)\
    Tue 2013-03-19 05:24:03 +0100
    * Bug 16401147 - crlf instead of lf in readme
  * [Revision #3077.187.22](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.22) \[merge]\
    Mon 2013-03-18 15:03:54 +0530
    * merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.844.62](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.62)\
      Mon 2013-03-18 15:01:16 +0530
      * Bug#14771299 out-of-bound reads write in mysqlbinlog
  * [Revision #3077.187.21](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.21)\
    Mon 2013-03-18 13:48:53 +0530
    * Bug #16076289 : backport fix for bug #14786792 to 5.5
  * [Revision #3077.187.20](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.20) \[merge]\
    Mon 2013-03-18 12:46:06 +0530
    * Merge of patch for bug#14685362 from mysql-5.1.
    * [Revision #2661.844.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.61)\
      Mon 2013-03-18 12:44:38 +0530
      * Bug#14685362 : memory leaks in mysql client in interactive mode
  * [Revision #3077.187.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.19) \[merge]\
    Fri 2013-03-15 08:57:59 +0530
    * Bug#16056813-memory leak on filtered slave null merge from mysql-5.1
    * [Revision #2661.844.60](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.60)\
      Fri 2013-03-15 08:56:20 +0530
      * Bug#16056813-memory leak on filtered slave
  * [Revision #3077.187.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.18)\
    Thu 2013-03-14 15:33:25 +0100
    * Bug#16359402 crash with aggregates: assertion failed: n < m\_size
  * [Revision #3077.187.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.17) \[merge]\
    Thu 2013-03-14 11:22:08 +0300
    * 5.1 -> 5.5 merge
    * [Revision #2661.844.59](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.59)\
      Thu 2013-03-14 11:11:17 +0300
      * Bug#16075310 server crash or valgrind errors in item\_func\_group\_concat::setup and ::ADD Item\_func\_group\_concat::copy\_or\_same() creates a copy of original object. It also creates a copy of ORDER structure because ORDER struct elements may be modified in find\_order\_in\_list() called from Item\_func\_group\_concat::setup(). As ORDER copy is created using memcpy, ORDER::next elements point to original ORDER structs. Thus find\_order\_in\_list() called from EXECUTE stmt modifies ordinal ORDER item pointers so they point to runtime items, these items are freed after execution, so original ORDER structure becomes invalid. The fix is to properly update ORDER::next fields so that they point to new ORDER elements.
  * [Revision #3077.187.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.16) \[merge]\
    Wed 2013-03-13 16:29:11 +0530
    * BUG#14593883-replication breaks when set data type columns are used inside a stored procedure merging post-push fix from mysql-5.1
    * [Revision #2661.844.58](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.58)\
      Wed 2013-03-13 16:24:35 +0530
      * BUG#14593883-replication breaks when set data type columns are used inside a stored procedure
  * [Revision #3077.187.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.15)\
    Wed 2013-03-13 11:43:21 +0530
    * Bug#16268289 lock\_rec\_validate\_page() may dereference a pointer to a freed lock
  * [Revision #3077.187.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.14) \[merge]\
    Wed 2013-03-13 09:43:50 +0530
    * Bug#16084346: ssl\_connect\_debug.test failure in 5.1
    * [Revision #2661.844.57](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.57)\
      Wed 2013-03-13 09:42:07 +0530
  * [Revision #3077.187.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.13) \[merge]\
    Tue 2013-03-12 22:44:32 +0530
    * BUG#14593883-replication breaks when set data type columns are used inside a stored procedure
    * [Revision #2661.844.56](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.56)\
      Tue 2013-03-12 22:36:13 +0530
      * BUG#14593883-replication breaks when set data type columns are used inside a stored procedure
  * [Revision #3077.187.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.12)\
    Tue 2013-03-12 13:58:10 +0200
    * Bug#16409715 assert sync\_thread\_levels\_g(array, level - 1, true), ibuf, free space management
  * [Revision #3077.187.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.11) \[merge]\
    Tue 2013-03-12 13:57:02 +0200
    * Merge mysql-5.1 to mysql-5.5.
    * [Revision #2661.844.55](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.55)\
      Tue 2013-03-12 13:42:12 +0200
      * Bug#16463505 pessimistic page\_zip\_available() may cause infinite page split
    * [Revision #2661.844.54](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.54)\
      Tue 2013-03-12 13:37:00 +0200
  * [Revision #3077.187.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.10)\
    Mon 2013-03-11 16:46:11 +0100
    * Bug#11766815 invalid system check time\_t\_unsigned
  * [Revision #3077.187.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.9)\
    Mon 2013-03-11 12:03:26 +0530
  * [Revision #3077.187.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.8)\
    Fri 2013-03-08 14:55:41 +0530
  * [Revision #3077.187.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.7)\
    Thu 2013-03-07 14:44:35 +0530
    * BUG#16069598 - server crash by null pointer dereferencing in mem\_heap\_create\_block()
  * [Revision #3077.187.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.6)\
    Fri 2013-03-01 13:25:59 +0100
    * Bug#11765489 cmake build on mac os x does not determine cpu type
  * [Revision #3077.187.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.5)\
    Thu 2013-03-07 12:12:58 +0530
    * Bug#16169063: security concern because of insufficient logging
  * [Revision #3077.187.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.4)\
    Wed 2013-03-06 11:49:57 +0530
    * Bug #16133801 unexplainable innodb unique index locks on delete + insert with same values
  * [Revision #3077.187.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.3) \[merge]\
    Wed 2013-03-06 06:52:18 +0100
    * NULL Merge for release 5.1.69
    * [Revision #2661.844.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.844.53)\
      Tue 2013-03-05 16:09:54 +0100
      * Raise version number after cloning 5.1.69
  * [Revision #3077.187.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.2)\
    Tue 2013-03-05 10:47:49 -0500
    * Bug#16068056 innodb calls buf\_validate() too often with univ\_debug
  * [Revision #3077.187.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.187.1)\
    Tue 2013-03-05 12:19:07 +0100
    * Raise version number after cloning 5.5.31
* [Revision #3834](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3834) \[merge]\
  Tue 2013-07-16 19:03:06 +0200
  * 5.3 merge
  * [Revision #2502.567.114](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.114) \[merge]\
    Mon 2013-07-15 18:32:25 +0200
    * 5.2 merge
    * [Revision #2502.566.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.51)\
      Tue 2013-07-09 22:24:57 +0200
      * [MDEV-4409](https://jira.mariadb.org/browse/MDEV-4409) - Fix deadlock in MySQL key cache code, that can happen if there is a key cache resize running in parallel with an update.
* [Revision #3833](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3833) \[merge]\
  Tue 2013-07-16 15:59:30 +0400
  * Automatic merge
  * [Revision #3831.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3831.1.1)\
    Tue 2013-07-16 15:57:27 +0400
    * [MDEV-4782](https://jira.mariadb.org/browse/MDEV-4782): Valgrind warnings (Conditional jump or move depends on uninitialised value) with InnoDB, semijoin - in sub\_select(): don't call table->file->position() when reading the first record produced an error.
* [Revision #3832](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3832)\
  Tue 2013-07-16 17:26:25 +0400
  * Update test results after the last cset.
* [Revision #3831](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3831)\
  Tue 2013-07-16 10:56:42 +0400
  * [MDEV-4778](https://jira.mariadb.org/browse/MDEV-4778): Incorrect results from Aria/MyISAM SELECT using index with prefix length on TEXT column Backport the fix olav.sandstaa@sun.com-20101102184747-qfuntqwj021imy9r: "Fix for Bug#52660 Perf. regr. using ICP for MyISAM on range queries on an index containing TEXT" (together with further fixes in that code) into MyISAM and Aria.
* [Revision #3830](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3830)\
  Tue 2013-07-16 09:22:17 +0400
  * [MDEV-4173](https://jira.mariadb.org/browse/MDEV-4173): Wrong result (extra row) with semijoin=on, joins in outer query, LEFT JOIN in the subquery Apply the patch from Patryk Pomykalski: - create\_internal\_tmp\_table\_from\_heap() will now return information whether the last row that we tried to write was a duplicate row. (mysql-5.6 also has this change)
* [Revision #3829](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3829)\
  Mon 2013-07-15 18:51:52 +0400
  * [MDEV-4536](https://jira.mariadb.org/browse/MDEV-4536), [MDEV-4042](https://jira.mariadb.org/browse/MDEV-4042) - Make JOIN::cleanup(true) also work correctly when the query is KILLed after join optimization was started but before a query plan was produced
* [Revision #3828](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3828)\
  Thu 2013-07-11 19:27:39 +0400
  * [MDEV-4042](https://jira.mariadb.org/browse/MDEV-4042): Assertion `table->key_read == 0' fails in close_thread_table on EXPLAIN [MDEV-4536](https://jira.mariadb.org/browse/MDEV-4536): ...sql/sql_base.cc:1598:` bool close\_thread\_table(THD\*, TABLE\*\*)\`: Assertion - Make JOIN::cleanup(full=true) always free join optimization tabs.
* [Revision #3827](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3827)\
  Thu 2013-07-11 15:12:50 +0400
  * [MDEV-4556](https://jira.mariadb.org/browse/MDEV-4556) Server crashes in SEL\_ARG::rb\_insert with index\_merge+index\_merge\_sort\_union, FORCE INDEX - merge\_same\_index\_scans() may put the same SEL\_ARG tree in multiple result plans. make it call incr\_refs() on the SEL\_ARG trees that it does key\_or() on, because key\_or(sel\_arg\_tree\_1, sel\_arg\_tree\_2) call may invalidate SEL\_ARG trees pointed by sel\_arg\_tree\_1 and sel\_arg\_tree\_2.
* [Revision #3826](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3826) \[merge]\
  Wed 2013-07-10 02:05:06 +0400
  * Merge from 5.3
  * [Revision #2502.567.113](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.113) \[merge]\
    Tue 2013-07-09 11:02:56 +0400
    * Merge from 5.2
    * [Revision #2502.566.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.50) \[merge]\
      Tue 2013-07-09 10:54:47 +0400
      * Merge from 5.1
      * [Revision #2502.565.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.51)\
        Sat 2013-07-06 15:28:11 +0200
        * Bug #69682 - mysqld crashes after uninstall of plugin with "first" status var
      * [Revision #2502.565.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.50)\
        Fri 2013-05-24 17:35:30 +0200
        * [MDEV-4575](https://jira.mariadb.org/browse/MDEV-4575) MySQL client doesn't strip off 5.5.5- prefix while connecting to 10.x server
  * [Revision #2502.567.112](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.112)\
    Fri 2013-07-05 20:45:42 +0200
    * [MDEV-4610](https://jira.mariadb.org/browse/MDEV-4610) SQL query crashes MariaDB with derived\_with\_keys [MDEV-4643](https://jira.mariadb.org/browse/MDEV-4643) MariaDB crashes consistently when trying a SELECT on VIEW with a UNION and an additional JOIN in SELECT
  * [Revision #2502.567.111](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.111)\
    Fri 2013-07-05 17:54:25 +0200
    * [MDEV-4665](https://jira.mariadb.org/browse/MDEV-4665) crash when referencing missing function in a subquery
  * [Revision #2502.567.110](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.110)\
    Fri 2013-07-05 16:02:02 +0200
    * [MDEV-4257](https://jira.mariadb.org/browse/MDEV-4257) Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' fails on FROM subquery with fulltext search, derived\_merge=on
* [Revision #3825](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3825) \[merge]\
  Mon 2013-07-08 16:49:42 +0400
  * Merging from 5.3
  * [Revision #2502.567.109](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.109)\
    Wed 2013-07-03 09:46:20 +0200
    * [MDEV-4667](https://jira.mariadb.org/browse/MDEV-4667) DATE('string') incompability between mysql and mariadb
* [Revision #3824](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3824)\
  Thu 2013-07-04 18:37:55 +0300
  * [MDEV-4752](https://jira.mariadb.org/browse/MDEV-4752): Segfault during parsing of illegal query
* [Revision #3823](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3823)\
  Mon 2013-07-01 17:54:24 +0200
  * [MDEV-4718](https://jira.mariadb.org/browse/MDEV-4718) Test "outfile\_loaddata" fails on bigendian arches (ppc64)
* [Revision #3822](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3822)\
  Mon 2013-07-01 12:03:10 +0200
  * [MDEV-4670](https://jira.mariadb.org/browse/MDEV-4670) THD::awake bug with my\_sleep call
* [Revision #3821](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3821)\
  Mon 2013-07-01 12:02:44 +0200
  * [MDEV-4683](https://jira.mariadb.org/browse/MDEV-4683) query start\_time not reset when going to sleep
* [Revision #3820](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3820) \[merge]\
  Fri 2013-06-28 16:27:22 +0400
  * Merge
  * [Revision #2502.567.108](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.108)\
    Fri 2013-06-28 16:25:06 +0400
    * A clean-up for [MDEV-4634](https://jira.mariadb.org/browse/MDEV-4634)
* [Revision #3819](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3819) \[merge]\
  Fri 2013-06-28 15:20:40 +0400
  * Merge from 5.3
  * [Revision #2502.567.107](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.107)\
    Fri 2013-06-28 12:00:25 +0400
    * [MDEV-4634](https://jira.mariadb.org/browse/MDEV-4634) Crash in CONVERT\_TZ Item\_func\_min\_max::get\_date() did not check the returned value against the fuzzy\_date flags, so it could return a bad value to the caller that expects a good date (e.h. CONVERT\_TZ).
* [Revision #3818](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3818)\
  Thu 2013-06-27 14:19:04 +0200
  * [MDEV-4720](https://jira.mariadb.org/browse/MDEV-4720) : fix my\_context.h for use with x32 ABI. Do not use x64 assembler implementation in x32.
* [Revision #3817](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3817)\
  Sat 2013-06-22 14:02:03 +0200
  * [MDEV-4685](https://jira.mariadb.org/browse/MDEV-4685) Compile error on LFS
* [Revision #3816](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3816) \[merge]\
  Tue 2013-06-18 13:14:46 +0400
  * Merging [MDEV-4635](https://jira.mariadb.org/browse/MDEV-4635) from 5.3.
  * [Revision #2502.567.106](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.106)\
    Mon 2013-06-17 19:25:55 +0400
    * [MDEV-4635](https://jira.mariadb.org/browse/MDEV-4635) Crash in UNIX\_TIMESTAMP(STR\_TO\_DATE('2020','%Y'))
* [Revision #3815](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3815)\
  Mon 2013-06-17 19:18:14 +0200
  * [MDEV-4503](https://jira.mariadb.org/browse/MDEV-4503) : Installation fails if TEMP directory contains "" subdirectory.
* [Revision #3814](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3814)\
  Mon 2013-06-17 17:58:53 +0200
  * unit test case for [MDEV-4576](https://jira.mariadb.org/browse/MDEV-4576)
* [Revision #3813](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3813)\
  Sun 2013-06-16 22:13:26 +0200
  * [MDEV-4576](https://jira.mariadb.org/browse/MDEV-4576) : Aria storage engine's temporary files might not be deleted (Errcode : 13) See also MySQL Bug #39750 and similar ones.
* [Revision #3812](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3812)\
  Sat 2013-06-15 14:22:03 +0200
  * [MDEV-4601](https://jira.mariadb.org/browse/MDEV-4601) : Allow MariaDB to be build without non-blocking client.
* [Revision #3811](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3811) \[merge]\
  Mon 2013-06-17 20:33:36 +0300
  * 5.3 -> 5.5 Merge
  * [Revision #2502.567.105](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.105)\
    Mon 2013-06-17 17:04:51 +0400
    * [MDEV-4651](https://jira.mariadb.org/browse/MDEV-4651) Crash in my\_decimal2decimal in a ORDER BY query
  * [Revision #2502.567.104](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.104)\
    Thu 2013-06-06 23:33:40 +0300
    * [MDEV-4593](https://jira.mariadb.org/browse/MDEV-4593): p\_s: crash in simplify\_joins with delete using subselect from view
* [Revision #3810](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3810)\
  Sat 2013-06-15 16:02:43 +0200
  * [MDEV-4466](https://jira.mariadb.org/browse/MDEV-4466) Partitioned Aria table created by a previous version is recognized as TEST\_SQL\_DISCOVERY
* [Revision #3809](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3809)\
  Fri 2013-06-14 14:04:58 +0200
  * [MDEV-4006](https://jira.mariadb.org/browse/MDEV-4006) mysql\_plugin.1 is removed from source which is not necessary
* [Revision #3808](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3808)\
  Thu 2013-06-13 20:19:32 +0200
  * [MDEV-4578](https://jira.mariadb.org/browse/MDEV-4578) information\_schema.processlist reports incorrect value for Time (2147483647)
* [Revision #3807](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3807)\
  Thu 2013-06-13 20:19:11 +0200
  * [MDEV-4529](https://jira.mariadb.org/browse/MDEV-4529) Assertion \`tmp->state == 4' fails on mix of INSTALL SONAME / UNINSTALL PLUGIN
* [Revision #3806](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3806)\
  Thu 2013-06-13 20:18:40 +0200
  * [MDEV-4519](https://jira.mariadb.org/browse/MDEV-4519) SHOW EVENTS and SHOW PROCEDURE STATUS truncate long user names
* [Revision #3805](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3805)\
  Thu 2013-06-13 15:33:02 +0200
  * [MDEV-4515](https://jira.mariadb.org/browse/MDEV-4515) Long user names are truncated to 48 symbols in error messages
* [Revision #3804](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3804)\
  Thu 2013-06-13 15:13:13 +0200
  * [MDEV-4444](https://jira.mariadb.org/browse/MDEV-4444) Server crashes with "safe\_mutex: Trying to destroy a mutex share->mutex that was locked" on attempt to recover an archive table
* [Revision #3803](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3803)\
  Thu 2013-06-13 14:32:57 +0200
  * [MDEV-703](https://jira.mariadb.org/browse/MDEV-703) [Bug #870310](https://bugs.launchpad.net/bugs/870310) - killall -9 in init-script
* [Revision #3802](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3802)\
  Thu 2013-06-13 14:14:47 +0200
  * [MDEV-4573](https://jira.mariadb.org/browse/MDEV-4573) UNINSTALL PLUGIN misleading error message for non-dynamic plugins
* [Revision #3801](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3801)\
  Thu 2013-06-13 00:13:23 +0200
  * [MDEV-4614](https://jira.mariadb.org/browse/MDEV-4614) Man pages fixes
* [Revision #3800](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3800)\
  Wed 2013-06-12 22:12:09 +0200
  * [MDEV-4604](https://jira.mariadb.org/browse/MDEV-4604) Wrong server status when sending out parameters
* [Revision #3799](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3799)\
  Wed 2013-06-12 20:38:22 +0200
  * [MDEV-4509](https://jira.mariadb.org/browse/MDEV-4509) mysql init script should accept arguments
* [Revision #3798](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3798)\
  Wed 2013-06-12 20:29:19 +0200
  * [MDEV-4422](https://jira.mariadb.org/browse/MDEV-4422) SHOW PROCESSLIST reference to THD::db not protected against simultaneous updates
* [Revision #3797](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3797)\
  Tue 2013-06-11 12:53:35 +0200
  * [MDEV-4636](https://jira.mariadb.org/browse/MDEV-4636) use mysql\_cleartext\_plugin from auth\_pam
* [Revision #3796](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3796)\
  Tue 2013-06-11 11:11:05 +0200
  * [MDEV-4574](https://jira.mariadb.org/browse/MDEV-4574) Missing connection option MYSQL\_ENABLE\_CLEARTEXT\_PLUGIN
* [Revision #3795](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3795)\
  Mon 2013-06-10 21:45:30 +0200
  * [MDEV-4297](https://jira.mariadb.org/browse/MDEV-4297) `mysql --binary-mode`
* [Revision #3794](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3794)\
  Wed 2013-06-12 05:09:28 +0400
  * [MDEV-4629](https://jira.mariadb.org/browse/MDEV-4629) MTR tests main.variables and some of sys\_vars.\* fail on 32-bit builds
* [Revision #3793](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3793)\
  Tue 2013-06-11 13:49:43 +0300
  * Fixed tests that failed on 32 bit because of my earlier fixes of 32 bit limits.
* [Revision #3792](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3792)\
  Fri 2013-06-07 15:35:13 +0200
  * [MDEV-4468](https://jira.mariadb.org/browse/MDEV-4468) Assertion \`error != 0' fails or timeout occurs on select from a FEDERATED table which points at a non-existent table
* [Revision #3791](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3791)\
  Fri 2013-06-07 15:34:59 +0200
  * [MDEV-4480](https://jira.mariadb.org/browse/MDEV-4480) Assertion \`inited == NONE' fails on closing a connection with open handler on temporary table
* [Revision #3790](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3790)\
  Fri 2013-06-07 10:02:50 +0200
  * [MDEV-4564](https://jira.mariadb.org/browse/MDEV-4564) ALTER on a temporary table generates an audit event
* [Revision #3789](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3789)\
  Sun 2013-06-09 13:26:10 +0300\
  \*
  * Added -Wno-uninitialized to avoid warnings in release builds (uninitalized variables are detected by DBUG builds) - Fixed wrong declaration which cased compile failure on 32 bit
* [Revision #3788](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3788)\
  Thu 2013-06-06 15:14:23 +0300
  * Fixed some cache variables that could be set to higher value than what the code supported (size\_t) Fixed some cases that didn't work with > 4G buffers. Fixed compiler warnings
* [Revision #3787](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3787)\
  Wed 2013-06-05 23:53:35 +0300
  * -Run test suite with smaller aria keybuffer size (to make it possible to run more tests in parallel) -Added test and extra code to ensure we don't leave keyread on for a handler table. -Create on disk temporary files always with long data pointers if SQL\_SMALL\_RESULT is not used. This ensures that we can handle temporary files bigger than 4G.
* [Revision #3786](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3786)\
  Sat 2013-06-01 21:33:26 +0200
  * Fix a compile warning on NetBSD
* [Revision #3785](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3785)\
  Sat 2013-06-01 21:30:33 +0200
  * [MDEV-4607](https://jira.mariadb.org/browse/MDEV-4607) : libreadline-related compilation problems on NetBSD.
* [Revision #3784](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3784)\
  Thu 2013-05-30 08:23:49 +0300
  * [MDEV-4520](https://jira.mariadb.org/browse/MDEV-4520): Assertion \`0' fails in Query\_cache::end\_of\_result on concurrent drop event and event executio
* [Revision #3783](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3783)\
  Tue 2013-05-28 21:25:59 +0200
  * followup for revision 3751 "centos5 gcc 4.1 asm bug" remove the workaround from cmake/os/FreeBSD.cmake
* [Revision #3782](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3782)\
  Thu 2013-05-23 17:05:31 +0300
  * [MDEV-4520](https://jira.mariadb.org/browse/MDEV-4520): Assertion \`0' fails in Query\_cache::end\_of\_result on concurrent drop event and event execution
* [Revision #3781](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3781)\
  Wed 2013-05-22 16:44:44 +0200
  * [MDEV-4548](https://jira.mariadb.org/browse/MDEV-4548) - compile sphinx.so/dll and include into packages
* [Revision #3780](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3780)\
  Mon 2013-05-27 16:35:42 +0200
  * [MDEV-4553](https://jira.mariadb.org/browse/MDEV-4553) - Fixes for compilation under NetBSD.
* [Revision #3779](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3779)\
  Fri 2013-05-24 14:33:04 +0200
  * [MDEV-4516](https://jira.mariadb.org/browse/MDEV-4516) SELECT from I\_S.QUERY\_CACHE\_INFO produces ER\_UNKNOWN\_ERROR when query cache size is 0

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
