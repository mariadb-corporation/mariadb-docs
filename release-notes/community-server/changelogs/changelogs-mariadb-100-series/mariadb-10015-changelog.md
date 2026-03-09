# MariaDB 10.0.15 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.15)[Release Notes](../../old-releases/10.0/10.0.15.md)[Changelog](mariadb-10015-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 25 Nov 2014

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.15.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4506](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4506) \[merge]\
  Fri 2014-11-21 20:20:39 +0100
  * 5.5 merge
  * [Revision #3413.67.51](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.51)\
    Fri 2014-11-21 13:32:53 +0200
    * Forgot to add test file.
  * [Revision #3413.67.50](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.50)\
    Fri 2014-11-21 15:23:18 +0400
    * [MDEV-7026](https://jira.mariadb.org/browse/MDEV-7026) - Race in InnoDB/XtraDB mutex implementation can stall or hang the server
  * [Revision #3413.67.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.49)\
    Fri 2014-11-21 13:27:36 +0200
    * [MDEV-7084](https://jira.mariadb.org/browse/MDEV-7084): innodb index stats inadequate using constant innodb\_stats\_sample\_pages
* [Revision #4505](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4505) \[merge]\
  Fri 2014-11-21 08:50:44 +0100
  * Merge
  * [Revision #4500.1.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.30)\
    Fri 2014-11-21 00:02:24 +0100
    * after merge fixes:
  * [Revision #4500.1.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.29) \[merge]\
    Thu 2014-11-20 17:39:11 +0100
    * 10.0-mroonga
    * [Revision #4426.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426.1.9)\
      Tue 2014-11-04 00:40:20 +0900
      * cmake: use "mroonga" instead of "ha\_mroonga" for plugin name
    * [Revision #4426.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426.1.8)\
      Tue 2014-11-04 00:09:16 +0900
      * remove needless source tree
    * [Revision #4426.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426.1.7) \[merge]\
      Tue 2014-11-04 00:07:26 +0900
      * Merge from trunk
  * [Revision #4500.1.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.28) \[merge]\
    Thu 2014-11-20 17:29:21 +0100
    * 10.0-connect
    * [Revision #4439.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.21)\
      Sun 2014-11-16 20:14:36 +0100\
      \*
      * Commit resolved conflicted files
    * [Revision #4439.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.20)\
      Sun 2014-11-16 01:16:51 +0100\
      \*
      * Remove gcc warning (no previous declaration of msglang)
    * [Revision #4439.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.19)\
      Sat 2014-11-15 18:28:24 +0100\
      \*
      * Implement the NEWMSG and XMSG methods They are still experimental and should not be used in production.
    * [Revision #4439.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.18)\
      Sun 2014-11-09 14:18:44 +0100\
      \*
      * FIX ftell error when the line endings do not match the declared or default ending. Also takes care of files having mixed line endings. This is done by never using text mode for streams and handle the line endings in reading and writing. ([MDEV-7030](https://jira.mariadb.org/browse/MDEV-7030))
    * [Revision #4439.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.17)\
      Sat 2014-11-08 16:44:52 +0100\
      \*
      * Compile protect against not fully implemented optione XMSG and NEWMSG
    * [Revision #4439.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.16)\
      Sat 2014-11-08 16:29:16 +0100\
      \*
      * fix typo error
    * [Revision #4439.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.15)\
      Sat 2014-11-08 13:35:03 +0100\
      \*
      * Calculate next position in filamap without assuming ENDING option is true.
    * [Revision #4439.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.14)\
      Sat 2014-11-01 17:08:39 +0100\
      \*
      * Fix [MDEV-6988](https://jira.mariadb.org/browse/MDEV-6988) and [MDEV-6994](https://jira.mariadb.org/browse/MDEV-6994)
    * [Revision #4439.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.13)\
      Fri 2014-10-31 13:58:43 +0100\
      \*
      * Add the new files to the source list
    * [Revision #4439.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.12)\
      Fri 2014-10-31 12:43:55 +0100\
      \*
      * Adding the VIR table type implementation files
    * [Revision #4439.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.11)\
      Fri 2014-10-31 12:28:07 +0100\
      \*
      * Add new table type VIR and virtual index
    * [Revision #4439.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.10)\
      Fri 2014-10-24 19:22:05 +0200
      * Fix a bug in XCOL tables. When a row was filtered internally the XColumn was not reset causing rows to be lost.
    * [Revision #4439.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.9)\
      Fri 2014-10-24 16:21:39 +0200\
      \*
      * Fix bug: Server crash when using a special column in XCOL tables
    * [Revision #4439.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.8)\
      Wed 2014-10-22 13:51:33 +0200\
      \*
      * Remove some gcc warnings
    * [Revision #4439.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.7)\
      Wed 2014-10-22 12:02:46 +0200\
      \*
      * Fix (gcc error) passing cmd instead of cmd.Getstr() to htrc
    * [Revision #4439.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.6)\
      Tue 2014-10-21 17:29:51 +0200\
      \*
      1. Handling string memory allocation with a new STRING class. This is only the beginning. Defining the STRING class and begining to use it (MYSQL)
    * [Revision #4439.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.5) \[merge]\
      Tue 2014-10-14 17:52:20 +0200\
      \*
      * Commit merged change removed: extra/yassl/certs/dsa512.der extra/yassl/certs/dsa512.pem
    * [Revision #4439.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.4)\
      Tue 2014-10-14 16:42:22 +0200\
      \*
      * Add Sergei fix to enable loading OEM table libs
  * [Revision #4500.1.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.27) \[merge]\
    Thu 2014-11-20 17:09:51 +0100
    * pcre-8.36
    * [Revision #0.66.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.66.3)\
      Tue 2014-11-18 18:07:55 +0100
      * 8.36
  * [Revision #4500.1.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.26) \[merge]\
    Thu 2014-11-20 17:05:13 +0100
    * XtraDB 5.6.21-70.0
    * [Revision #0.12.73](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.73)\
      Tue 2014-11-18 18:11:15 +0100
      * 5.6.21-70.0
  * [Revision #4500.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.25) \[merge]\
    Thu 2014-11-20 16:59:22 +0100
    * InnoDB 5.6.21
    * [Revision #0.49.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.49.7)\
      Tue 2014-11-18 17:41:12 +0100
      * 5.6.21
  * [Revision #4500.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.24) \[merge]\
    Thu 2014-11-20 16:53:12 +0100
    * sphinx 2.2.6
    * [Revision #0.47.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.47.5)\
      Tue 2014-11-18 18:10:29 +0100
      * 2.2.6
  * [Revision #4500.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.23) \[merge]\
    Thu 2014-11-20 16:27:16 +0100
    * 5.5 merge
    * [Revision #3413.67.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.48)\
      Thu 2014-11-20 16:11:30 +0100
      * followup: disable openssl\_6975.test as appropriate
    * [Revision #3413.67.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.47)\
      Wed 2014-11-19 22:04:51 +0100
      * Fix YaSSL on windows
    * [Revision #3413.67.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.46)\
      Wed 2014-11-19 18:54:02 +0100
      * [MDEV-6975](https://jira.mariadb.org/browse/MDEV-6975) Implement TLS protocol
  * [Revision #4500.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.22) \[merge]\
    Thu 2014-11-20 16:07:34 +0100
    * 5.5 merge
    * [Revision #3413.67.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.45)\
      Wed 2014-11-19 20:27:34 +0200
      * [MDEV-7084](https://jira.mariadb.org/browse/MDEV-7084): innodb index stats inadequate using constant innodb\_stats\_sample\_pages
  * [Revision #4500.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.21) \[merge]\
    Thu 2014-11-20 15:26:31 +0100
    * 5.5 merge
    * [Revision #3413.67.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.44)\
      Wed 2014-11-19 13:56:46 +0100
      * [MDEV-7026](https://jira.mariadb.org/browse/MDEV-7026): Race in InnoDB/XtraDB mutex implementation can stall or hang the server.
  * [Revision #4500.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.20) \[merge]\
    Wed 2014-11-19 17:23:39 +0100
    * 5.5 merge
    * [Revision #3413.67.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.43)\
      Wed 2014-11-19 00:19:52 +0100
      * openssl-poodle\_6975.test: don't run it for older OpenSSL versions
    * [Revision #3413.67.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.42)\
      Tue 2014-11-18 17:57:06 +0100
      * [MDEV-6975](https://jira.mariadb.org/browse/MDEV-6975) Implement TLS protocol
    * [Revision #3413.67.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.41)\
      Tue 2014-11-18 17:56:58 +0100
      * new mysqltest connect option SSL-CIPHER=xxxx
    * [Revision #3413.67.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.40)\
      Tue 2014-11-18 17:56:49 +0100
      * improve OpenSSL error reporting
    * [Revision #3413.67.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.39) \[merge]\
      Tue 2014-11-18 17:54:00 +0100
      * TokuDB 7.5.3
      * [Revision #0.28.1710](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.28.1710) \[merge]\
        Fri 2014-11-14 13:10:22 -0500
        * Merge branch 'master' into releases/tokudb-7.5
        * [Revision #0.79.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.33)\
          Fri 2014-11-14 13:10:07 -0500
          * DB-754 build with bundled jemalloc
      * [Revision #0.28.1709](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.28.1709) \[merge]\
        Thu 2014-11-13 10:53:37 -0500
        * Merge branch 'master' into releases/tokudb-7.5
        * [Revision #0.79.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.32)\
          Thu 2014-11-13 10:53:22 -0500
          * DB-759 test and fix alter table bug with cardinality data
        * [Revision #0.79.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.31)\
          Wed 2014-11-12 21:06:51 -0500
          * DB-759 fix tokudb::alter\_card to copy ALL of the cardinality data not just the low byte
        * [Revision #0.79.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.30)\
          Wed 2014-11-12 18:30:16 -0500
          * increase test coverage of the cardinality code
        * [Revision #0.79.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.29)\
          Wed 2014-11-12 14:36:08 -0500
          * speed up tokudb handler unit tests
        * [Revision #0.79.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.28)\
          Wed 2014-11-12 08:38:04 -0500
          * speed up tokudb handler unit tests
      * [Revision #0.28.1708](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.28.1708) \[merge]\
        Mon 2014-11-10 16:37:45 -0500
        * Merge branch 'master' into releases/tokudb-7.5
        * [Revision #0.79.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.27)\
          Mon 2014-11-10 16:34:55 -0500
          * speed up tokudb handler unit tests
      * [Revision #0.28.1707](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.28.1707) \[merge]\
        Sat 2014-11-08 14:35:15 -0500
        * Merge branch 'master' into releases/tokudb-7.5
        * [Revision #0.79.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.26)\
          Sat 2014-11-08 10:36:33 -0500
          * DB-757 compute cardinality when alter table analyze partition is run
        * [Revision #0.79.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.25)\
          Sat 2014-11-08 08:59:55 -0500
          * DB-756 set cardinality data for partitioned tokudb tables
        * [Revision #0.79.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.24)\
          Fri 2014-11-07 13:39:32 -0500
          * DB-742 set tokudb version for tokudb builds
      * [Revision #0.28.1706](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.28.1706) \[merge]\
        Thu 2014-11-06 06:12:06 -0500
        * Merge branch 'master' into releases/tokudb-7.5
        * [Revision #0.79.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.23)\
          Wed 2014-11-05 11:24:27 -0500
          * DB-754 include my\_config.h first for [mariadb 5.5.40](../../old-releases/5.5/5.5.40.md)
      * [Revision #0.28.1705](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.28.1705) \[merge]\
        Wed 2014-11-05 09:28:29 -0500
        * Merge branch 'master' into releases/tokudb-7.5
        * [Revision #0.79.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.22)\
          Wed 2014-11-05 04:15:43 -0500
          * DB-730 build tokudb without XA
        * [Revision #0.79.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.79.21)\
          Mon 2014-11-03 15:03:57 -0500
          * mark 5585.test as a big test
    * [Revision #3413.67.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.38) \[merge]\
      Tue 2014-11-18 17:36:51 +0100
      * 5.3 merge
      * [Revision #2502.594.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.594.4)\
        Sat 2014-11-15 21:30:16 +0400
        * [MDEV-6883](https://jira.mariadb.org/browse/MDEV-6883) ST\_WITHIN crashes server if (0,0) is matched to POLYGON((0 0)). Fixed the case when a polygon contains a single-point ring.
    * [Revision #3413.67.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.37)\
      Tue 2014-11-18 15:43:01 +0100
      * [MDEV-7028](https://jira.mariadb.org/browse/MDEV-7028) mysql\_config produces invalid cflags (was: udf\_example.c couldn't compile)
    * [Revision #3413.67.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.36)\
      Tue 2014-11-18 15:42:48 +0100
      * [MDEV-4513](https://jira.mariadb.org/browse/MDEV-4513) Valgrind warnings (Conditional jump or move depends on uninitialised value) in inflate on UNCOMPRESS
    * [Revision #3413.67.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.35)\
      Tue 2014-11-18 15:42:40 +0100
      * [MDEV-7113](https://jira.mariadb.org/browse/MDEV-7113) difference between check\_vcol\_func\_processor and check\_partition\_func\_processor [MDEV-6789](https://jira.mariadb.org/browse/MDEV-6789) segfault in Item\_func\_from\_unixtime::get\_date on updating table with virtual columns
    * [Revision #3413.67.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.34)\
      Tue 2014-11-18 15:42:32 +0100
      * [MDEV-3940](https://jira.mariadb.org/browse/MDEV-3940) Server crash or assertion \`item->type() == Item::STRING\_ITEM' failure on LOAD DATA through a view with statement binary logging
    * [Revision #3413.67.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.33)\
      Tue 2014-11-18 15:42:25 +0100
      * [MDEV-6854](https://jira.mariadb.org/browse/MDEV-6854) Typo in cmake/plugin.cmake
    * [Revision #3413.67.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.32)\
      Mon 2014-11-10 19:17:39 +0100
      * [MDEV-6862](https://jira.mariadb.org/browse/MDEV-6862) "#error \<my\_config.h>" and third-party libraries
    * [Revision #3413.67.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.31)\
      Sat 2014-11-08 19:54:42 +0100
      * [MDEV-6179](https://jira.mariadb.org/browse/MDEV-6179): dynamic columns functions/cast()/convert() doesn't play nice with CREATE/ALTER TABLE
    * [Revision #3413.67.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.30)\
      Mon 2014-11-17 20:28:18 +0400
      * Re-enabling tests disabled due to [MDEV-5266](https://jira.mariadb.org/browse/MDEV-5266) and MySQL:65225 (fixed now)
    * [Revision #3413.67.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.29)\
      Mon 2014-11-17 20:10:57 +0400
      * Sporadic failure in storage\_engine/trx.xa\_recovery test
    * [Revision #3413.67.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.28)\
      Mon 2014-11-17 17:24:04 +0400
      * [MDEV-6865](https://jira.mariadb.org/browse/MDEV-6865) Merge Bug#18935421 RPAD DIES WITH CERTAIN PADSTR INTPUTS..
    * [Revision #3413.67.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.27)\
      Sat 2014-11-15 22:18:33 +0100
      * [MDEV-6868](https://jira.mariadb.org/browse/MDEV-6868): MariaDB server crash ( select with union and order by with subquery )
    * [Revision #3413.67.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.26) \[merge]\
      Thu 2014-11-13 14:15:59 +0300
      * Merge 5.3->5.5
      * [Revision #2502.594.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.594.3)\
        Thu 2014-11-13 14:12:41 +0300
        * [MDEV-7068](https://jira.mariadb.org/browse/MDEV-7068): MRR accessing uninitialised bytes, test case failure main.innodb\_mrr Backport to 5.3: - Don't call index\_reader->interrupt\_read() if the index reader has returned all rows that matched its keys.
    * [Revision #3413.67.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.25)\
      Thu 2014-11-13 13:56:35 +0300
      * [MDEV-7068](https://jira.mariadb.org/browse/MDEV-7068): MRR accessing uninitialised bytes, test case failure main.innodb\_mrr - Don't call index\_reader->interrupt\_read() if the index reader has returned all rows that matched its keys.
    * [Revision #3413.67.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.24)\
      Thu 2014-11-13 11:24:19 +0200
      * [MDEV-7100](https://jira.mariadb.org/browse/MDEV-7100): InnoDB error monitor might unnecessary wait log\_sys mutex
    * [Revision #3413.67.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.23)\
      Thu 2014-11-13 10:04:45 +0100
      * [MDEV-7103](https://jira.mariadb.org/browse/MDEV-7103): Sporadic test falure in rpl.rpl\_parallel\_show\_binlog\_events\_purge\_logs
    * [Revision #3413.67.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.22)\
      Wed 2014-11-12 11:10:13 +0100
      * [MDEV-7089](https://jira.mariadb.org/browse/MDEV-7089): Test failures in main.failed\_auth\_unixsocket and plugins.unix\_socket depending on environment
    * [Revision #3413.67.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.21)\
      Mon 2014-11-10 18:08:17 +0400
      * [MDEV-7019](https://jira.mariadb.org/browse/MDEV-7019) String::chop() is wrong and may potentially crash (MySQL bug#56492) Merging a fix from the upstream.
    * [Revision #3413.67.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.20)\
      Mon 2014-11-03 15:43:44 +0200
      * [MDEV-7017](https://jira.mariadb.org/browse/MDEV-7017): Add function to print semaphore waits
  * [Revision #4500.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.19)\
    Wed 2014-11-19 00:19:17 +0100
    * [MDEV-6984](https://jira.mariadb.org/browse/MDEV-6984) Can't migrate from MySQL 5.6.21 to MariaDB 10
  * [Revision #4500.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.18)\
    Tue 2014-11-18 22:27:31 +0100
    * [MDEV-4285](https://jira.mariadb.org/browse/MDEV-4285) Server crashes in ptr\_compare on NOW and CAST in ORDER BY
  * [Revision #4500.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.17)\
    Tue 2014-11-18 22:27:26 +0100
    * debian packaging: add mroonga and example engines
  * [Revision #4500.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.16)\
    Tue 2014-11-18 22:27:03 +0100
    * mroonga/groonga: remove unused packaging data and bundled software
  * [Revision #4500.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.15)\
    Tue 2014-11-18 22:26:25 +0100
    * mroonga/groonga: disable building of unnecessary or unsupported components
  * [Revision #4500.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.14)\
    Tue 2014-11-18 22:26:20 +0100
    * mroonga/groonga: CMakeLists.txt
  * [Revision #4500.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.13)\
    Tue 2014-11-18 22:26:14 +0100
    * [MDEV-6794](https://jira.mariadb.org/browse/MDEV-6794) XtraDB no longer using UNIQUE as clustered index when PK missing
  * [Revision #4500.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.12)\
    Tue 2014-11-18 22:26:09 +0100
    * two more unused error messages
  * [Revision #4500.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.11)\
    Tue 2014-11-18 22:26:04 +0100
    * [MDEV-4399](https://jira.mariadb.org/browse/MDEV-4399) mysql\_secure\_installation reports error in find\_mysql\_client
  * [Revision #4500.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.10)\
    Tue 2014-11-18 22:25:59 +0100
    * [MDEV-6779](https://jira.mariadb.org/browse/MDEV-6779) Help file problems in 10.0.13
  * [Revision #4500.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.9)\
    Tue 2014-11-18 22:25:52 +0100
    * [MDEV-6779](https://jira.mariadb.org/browse/MDEV-6779) Help file problems in 10.0.13
  * [Revision #4500.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.8)\
    Tue 2014-11-18 22:25:47 +0100
    * [MDEV-6805](https://jira.mariadb.org/browse/MDEV-6805) one can set character\_set\_client to utf32
  * [Revision #4500.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.7)\
    Tue 2014-11-18 22:25:41 +0100
    * [MDEV-6785](https://jira.mariadb.org/browse/MDEV-6785) Wrong result on 2nd execution of PS with aggregate function, FROM SQ or MERGE view
  * [Revision #4500.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.6)\
    Tue 2014-11-18 22:25:33 +0100
    * [MDEV-6880](https://jira.mariadb.org/browse/MDEV-6880) Can't define CURRENT\_TIMESTAMP as default value for added column
  * [Revision #4500.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.5)\
    Tue 2014-11-18 22:25:27 +0100
    * [MDEV-7087](https://jira.mariadb.org/browse/MDEV-7087) main.stat\_tables-enospc fails in buildbot on a valgrind build
  * [Revision #4500.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.4)\
    Tue 2014-11-18 22:25:20 +0100
    * [MDEV-7078](https://jira.mariadb.org/browse/MDEV-7078) rpl.rpl\_\*mixing\_engines tests fail in buildbot
  * [Revision #4500.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.3)\
    Thu 2014-11-13 13:40:19 +0100
    * [MDEV-7003](https://jira.mariadb.org/browse/MDEV-7003) test-alter-table crashes debug build due to double free of plugin
  * [Revision #4500.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.2)\
    Thu 2014-11-13 13:40:11 +0100
    * [MDEV-6849](https://jira.mariadb.org/browse/MDEV-6849) ON UPDATE CURRENT\_TIMESTAMP doesn't always work
  * [Revision #4500.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500.1.1)\
    Tue 2014-11-11 10:39:35 +0100
    * sql\_update.cc: always update default fields _after_ compare\_record()
* [Revision #4504](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4504)\
  Wed 2014-11-19 17:14:49 +0300
  * [MDEV-7118](https://jira.mariadb.org/browse/MDEV-7118): Anemometer stop working after upgrade to from...
* [Revision #4503](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4503)\
  Wed 2014-11-19 14:34:49 +0400
  * [MDEV-7074](https://jira.mariadb.org/browse/MDEV-7074) multi\_source.simple test fails in buildbot
* [Revision #4502](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4502)\
  Wed 2014-11-19 12:08:35 +0400
  * [MDEV-6993](https://jira.mariadb.org/browse/MDEV-6993) Bad results with join comparing DECIMAL and ENUM/SET columns
* [Revision #4501](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4501)\
  Wed 2014-11-19 10:33:49 +0400
  * [MDEV-6978](https://jira.mariadb.org/browse/MDEV-6978) Bad results with join comparing case insensitive VARCHAR/ENUM/SET expression to a \_bin ENUM column
* [Revision #4500](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4500)\
  Tue 2014-11-18 23:15:54 +0400
  * [MDEV-6991](https://jira.mariadb.org/browse/MDEV-6991) GROUP\_MIN\_MAX optimization is erroneously applied in some cases
* [Revision #4499](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4499)\
  Tue 2014-11-18 16:33:29 +0400
  * [MDEV-6950](https://jira.mariadb.org/browse/MDEV-6950) Bad results with joins comparing DATE/DATETIME and INT/DECIMAL/DOUBLE/ENUM/VARCHAR columns [MDEV-6971](https://jira.mariadb.org/browse/MDEV-6971) Bad results with joins comparing TIME and DOUBLE/DECIMAL columns Disallow using indexes on non-temporal columns to optimize ref access, range access and table elimination when the counterpart's cmp\_type is TIME\_RESULT, e.g.: SELECT \* FROM t1 WHERE indexed\_int\_column=time\_expression; Only index on a temporal column can be used to optimize temporal comparison operations.
* [Revision #4498](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4498)\
  Tue 2014-11-18 13:07:37 +0400
  * [MDEV-7086](https://jira.mariadb.org/browse/MDEV-7086) main.ctype\_cp932 fails in buildbot on a valgrind build Removing a redundant and wrong condition which could access beyond the pattern string range.
* [Revision #4497](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4497)\
  Mon 2014-11-17 17:13:30 +0100
  * [MDEV-7116](https://jira.mariadb.org/browse/MDEV-7116): Dynamic column hangs/segfaults
* [Revision #4496](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4496)\
  Mon 2014-11-17 12:42:02 +0100
  * [MDEV-7121](https://jira.mariadb.org/browse/MDEV-7121): Parallel slave may hang if master crashes in the middle of writing transaction to binlog
* [Revision #4495](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4495)\
  Mon 2014-11-17 12:41:44 +0100
  * [MDEV-7079](https://jira.mariadb.org/browse/MDEV-7079): rpl.rpl\_parallel\_temptable fails in valgrind builder
* [Revision #4494](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4494)\
  Mon 2014-11-17 08:53:42 +0100
  * [MDEV-7080](https://jira.mariadb.org/browse/MDEV-7080): rpl.rpl\_gtid\_crash fails sporadically in buildbot
* [Revision #4493](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4493)\
  Fri 2014-11-14 09:13:13 +0200
  * [MDEV-7083](https://jira.mariadb.org/browse/MDEV-7083): sys\_vars.innodb\_sched\_priority\* tests fail in buildbot on work-amd64-valgrind
* [Revision #4492](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4492)\
  Thu 2014-11-13 11:01:31 +0100
  * [MDEV-6917](https://jira.mariadb.org/browse/MDEV-6917): Parallel replication: "Commit failed due to failure of an earlier commit on which this one depends", but no prior failure seen
* [Revision #4491](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4491)\
  Thu 2014-11-13 10:46:09 +0100
  * [MDEV-7065](https://jira.mariadb.org/browse/MDEV-7065): Incorrect relay log position in parallel replication after retry of transaction
* [Revision #4490](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4490)\
  Thu 2014-11-13 10:31:20 +0100
  * [MDEV-6775](https://jira.mariadb.org/browse/MDEV-6775): Wrong binlog order in parallel replication: Intermediate commit
* [Revision #4489](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4489)\
  Thu 2014-11-13 10:20:48 +0100
  * [MDEV-6680](https://jira.mariadb.org/browse/MDEV-6680): Performance of domain\_parallel replication is disappointing
* [Revision #4488](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4488)\
  Thu 2014-11-13 10:09:46 +0100
  * [MDEV-6718](https://jira.mariadb.org/browse/MDEV-6718): Server crashed in Gtid\_log\_event::Gtid\_log\_event with parallel replication
* [Revision #4487](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4487)\
  Thu 2014-11-13 09:56:28 +0100
  * [MDEV-7102](https://jira.mariadb.org/browse/MDEV-7102): Incorrect PSI\_stage\_info message in SHOW PROCESSLIST during parallel replication
* [Revision #4486](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4486)\
  Thu 2014-11-13 09:49:33 +0100
  * Fix a confusing error message in the testsuite
* [Revision #4485](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4485)\
  Thu 2014-11-13 09:49:07 +0100
  * [MDEV-6775](https://jira.mariadb.org/browse/MDEV-6775): Wrong binlog order in parallel replication
* [Revision #4484](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4484)\
  Thu 2014-11-13 09:20:40 +0100
  * Revert incorrect/redundant fix for old BUG#34656
* [Revision #4483](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4483)\
  Thu 2014-11-13 09:19:12 +0100
  * [MDEV-7101](https://jira.mariadb.org/browse/MDEV-7101): SAFE\_MUTEX lock order warning when reusing wait\_for\_commit mutex
* [Revision #4482](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4482)\
  Thu 2014-11-13 13:24:26 +0200
  * [MDEV-7035](https://jira.mariadb.org/browse/MDEV-7035): Remove innodb\_io\_capacity setting depending on setting of innodb\_io\_capacity\_max
* [Revision #4481](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4481)\
  Thu 2014-11-13 12:00:57 +0200
  * [MDEV-7100](https://jira.mariadb.org/browse/MDEV-7100): InnoDB error monitor might unnecessary wait log\_sys mutex
* [Revision #4480](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4480)\
  Thu 2014-11-13 11:05:22 +0200
  * [MDEV-7083](https://jira.mariadb.org/browse/MDEV-7083): sys\_vars.innodb\_sched\_priority\* tests fail in buildbot on work-amd64-valgrind.
* [Revision #4479](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4479)\
  Wed 2014-11-12 16:14:08 +0200
  * [MDEV-7070](https://jira.mariadb.org/browse/MDEV-7070): rpl.rpl\_innodb\_bug68220 fails in buildbot
* [Revision #4478](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4478)\
  Wed 2014-11-12 06:27:56 +0400
  * [MDEV-7073](https://jira.mariadb.org/browse/MDEV-7073) main.information\_schema and main.information\_schema\_all\_engines fail in buildbot on a build without perfschema
* [Revision #4477](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4477)\
  Wed 2014-11-12 05:56:45 +0400
  * [MDEV-7072](https://jira.mariadb.org/browse/MDEV-7072) mroonga/wrapper.version\_56\_or\_later\_performance\_schema fails in buildbot on a build without perfschema
* [Revision #4476](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4476)\
  Wed 2014-11-12 05:52:53 +0400
  * [MDEV-7071](https://jira.mariadb.org/browse/MDEV-7071) Spider tests fail due to an unknown option --skip-performance-schema on a build without perfschema
* [Revision #4475](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4475)\
  Wed 2014-11-12 05:40:21 +0400
  * [MDEV-7075](https://jira.mariadb.org/browse/MDEV-7075) perfschema.mks\_timer-6258 test not skipped on builds without perfschema
* [Revision #4474](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4474)\
  Tue 2014-11-11 19:59:31 +0300
  * Fix buildbot failure: make selectivity.test and selectivity\_innodb.test work when table names are case-insensitive.
* [Revision #4473](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4473)\
  Mon 2014-11-10 16:43:27 +0400
  * [MDEV-6965](https://jira.mariadb.org/browse/MDEV-6965) non-captured group \2 in regexp\_replace
* [Revision #4472](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4472)\
  Mon 2014-11-03 15:47:57 +0200
  * [MDEV-4396](https://jira.mariadb.org/browse/MDEV-4396): Fix innodb.innodb\_bug14676111 test.
* [Revision #4471](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4471) \[merge]\
  Mon 2014-11-03 17:47:37 +0100
  * [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) merge
* [Revision #4470](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4470)\
  Sun 2014-11-02 01:08:09 +0400
  * [MDEV-7001](https://jira.mariadb.org/browse/MDEV-7001) Bad result for NOT NOT STRCMP('a','b') and NOT NOT NULLIF(2,3) The bug is not very important per se, but it was helpful to move Item\_func\_strcmp out of Item\_bool\_func2 (to Item\_int\_func), for the purposes of "[MDEV-4912](https://jira.mariadb.org/browse/MDEV-4912) Add a plugin to field types (column types)".
* [Revision #4469](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4469)\
  Wed 2014-10-29 22:12:31 -0400
  * [MDEV-6939](https://jira.mariadb.org/browse/MDEV-6939) : Dots in file names of configuration files
* [Revision #4468](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4468)\
  Wed 2014-10-29 22:05:46 -0400
  * mysys/mf\_fn\_ext.c: typos & indents
* [Revision #4467](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4467) \[merge]\
  Wed 2014-10-29 15:20:46 +0300
  * Merge
  * [Revision #3413.65.61](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.61) \[merge]\
    Wed 2014-10-29 13:30:18 +0300
    * Merge
    * [Revision #2502.594.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.594.2) \[merge]\
      Wed 2014-10-29 01:48:18 +0300
      * Merge
    * [Revision #2502.594.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.594.1)\
      Tue 2014-10-14 19:11:39 -0700
      * Fixed bug [MDEV-6705](https://jira.mariadb.org/browse/MDEV-6705).
  * [Revision #3413.65.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.60) \[merge]\
    Wed 2014-10-29 13:22:48 +0300
    * Merge 5.3->5.5
    * [Revision #2502.567.241](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.241)\
      Wed 2014-10-29 01:46:05 +0300
      * [MDEV-6879](https://jira.mariadb.org/browse/MDEV-6879): Dereference of NULL primary\_file->table in DsMrr\_impl::get\_disk\_sweep\_mrr\_cost()
    * [Revision #2502.567.240](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.240)\
      Wed 2014-10-29 01:37:58 +0300
      * [MDEV-6878](https://jira.mariadb.org/browse/MDEV-6878): Use of uninitialized saved\_primary\_key in Mrr\_ordered\_index\_reader::resume\_read()
    * [Revision #2502.567.239](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.239)\
      Wed 2014-10-29 01:20:45 +0300
      * [MDEV-6888](https://jira.mariadb.org/browse/MDEV-6888): Query spends a long time in best\_extension\_by\_limited\_search with mrr enabled
* [Revision #4466](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4466)\
  Tue 2014-10-28 22:31:52 -0700
  * Fixed bug [MDEV-6843](https://jira.mariadb.org/browse/MDEV-6843).
* [Revision #4465](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4465) \[merge]\
  Tue 2014-10-28 16:31:26 -0700
  * Merge
  * [Revision #4446.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4446.1.1)\
    Tue 2014-10-28 14:33:31 -0700
    * Fixed bug [MDEV-6325](https://jira.mariadb.org/browse/MDEV-6325).
* [Revision #4464](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4464)\
  Mon 2014-10-27 16:58:16 +0200
  * [MDEV-6759](https://jira.mariadb.org/browse/MDEV-6759): innodb valgrind failures
* [Revision #4463](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4463)\
  Mon 2014-10-27 11:03:17 +0200
  * Fix test failure.
* [Revision #4462](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4462)\
  Sun 2014-10-26 07:29:37 +0200
  * [MDEV-6925](https://jira.mariadb.org/browse/MDEV-6925): Remove bad "" operators.
* [Revision #4461](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4461)\
  Sun 2014-10-26 07:22:51 +0200
  * [MDEV-6926](https://jira.mariadb.org/browse/MDEV-6926): innodb\_rows\_updated is misleading on slav
* [Revision #4460](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4460)\
  Sat 2014-10-25 09:24:39 +0300
  * [MDEV-6930](https://jira.mariadb.org/browse/MDEV-6930): Make innodb\_max\_dirty\_pages\_pct my.cnf variable a double
* [Revision #4459](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4459)\
  Sat 2014-10-25 08:21:52 +0300
  * [MDEV-6927](https://jira.mariadb.org/browse/MDEV-6927): Share more structures
* [Revision #4458](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4458)\
  Fri 2014-10-24 22:26:31 +0300
  * [MDEV-6928](https://jira.mariadb.org/browse/MDEV-6928): Add trx pointer to struct mtr\_t
* [Revision #4457](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4457)\
  Fri 2014-10-24 22:02:54 +0300
  * [MDEV-6937](https://jira.mariadb.org/browse/MDEV-6937): buf\_flush\_LRU() does not return correct number in case of compressed pages
* [Revision #4456](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4456)\
  Fri 2014-10-24 18:58:04 +0300
  * [MDEV-6931](https://jira.mariadb.org/browse/MDEV-6931): Page cleaner should do LRU flushing regardless of server activity
* [Revision #4455](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4455)\
  Fri 2014-10-24 17:56:04 +0300
  * [MDEV-6933](https://jira.mariadb.org/browse/MDEV-6933): Spurious lock\_wait\_timeout\_thread wakeup in lock\_wait\_suspend\_thread()
* [Revision #4454](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4454)\
  Fri 2014-10-24 17:11:09 +0300
  * [MDEV-6934](https://jira.mariadb.org/browse/MDEV-6934): os\_event\_wait\_time\_low(): wait time calculation is messed up
* [Revision #4453](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4453) \[merge]\
  Fri 2014-10-24 10:01:01 +0400
  * Merged mroonga updates.
  * [Revision #4426.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426.1.6)\
    Fri 2014-10-24 06:37:53 +0900
    * Disable foreign\_key\_create test.
* [Revision #4452](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4452)\
  Thu 2014-10-23 12:31:13 +0400
  * Better comments
* [Revision #4451](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4451) \[merge]\
  Wed 2014-10-22 18:33:49 +0400
  * Merged mroonga updates.
  * [Revision #4426.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426.1.5)\
    Thu 2014-10-23 00:31:01 +0900
    * Skip Mroonga if platform is big endian. Remove last test disabling.
* [Revision #4450](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4450) \[merge]\
  Tue 2014-10-21 22:20:21 +0400
  * Merged mroonga updates.
  * [Revision #4426.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426.1.4)\
    Wed 2014-10-22 03:43:19 +0900
    * Disable tests for Power8.
* [Revision #4449](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4449) \[merge]\
  Tue 2014-10-21 10:52:55 +0400
  * Merge mroonga.
  * [Revision #4426.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426.1.3)\
    Tue 2014-10-21 04:51:38 +0900
    * Update Mroonga to the latest version on 2014-10-21T04:51:38+0900
  * [Revision #4426.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426.1.2) \[merge]\
    Tue 2014-10-21 01:56:56 +0900
    * Merge from trunk
* [Revision #4448](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4448) \[merge]\
  Tue 2014-10-21 00:02:24 +0400
  * Merge
  * [Revision #4445.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4445.1.1)\
    Mon 2014-10-20 23:35:34 +0400
    * [MDEV-6879](https://jira.mariadb.org/browse/MDEV-6879): Dereference of NULL primary\_file->table in DsMrr\_impl::get\_disk\_sweep\_mrr\_cost()
* [Revision #4447](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4447)\
  Mon 2014-10-20 16:42:00 +0400
  * [MDEV-6649](https://jira.mariadb.org/browse/MDEV-6649) Different warnings for TIME and TIME(N) when @@old\_mode=zero\_date\_time\_cast
* [Revision #4446](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4446)\
  Thu 2014-10-16 22:58:08 +0400
  * [MDEV-6879](https://jira.mariadb.org/browse/MDEV-6879): Dereference of NULL primary\_file->table in DsMrr\_impl::get\_disk\_sweep\_mrr\_cost()
* [Revision #4445](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4445)\
  Thu 2014-10-16 17:57:13 +0400
  * [MDEV-6878](https://jira.mariadb.org/browse/MDEV-6878): Use of uninitialized saved\_primary\_key in Mrr\_ordered\_index\_reader::resume\_read()
* [Revision #4444](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4444) \[merge]\
  Mon 2014-10-13 12:31:55 +0400
  * Merge 10.0-connect -> 10.0
  * [Revision #4439.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.3)\
    Sun 2014-10-12 15:46:31 +0200\
    \*
    * Remove one gcc warning
  * [Revision #4439.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.2)\
    Sun 2014-10-12 12:05:05 +0200\
    \*
    * Fix null handling for date columns (see [MDEV-6744](https://jira.mariadb.org/browse/MDEV-6744))
  * [Revision #4439.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.1)\
    Fri 2014-10-10 13:27:52 +0200\
    \*
    * Fix a regression error from regarding Header as Boolean from some table types. Was added to ha\_connect::GetBooleanOption (otherwise ignored)
* [Revision #4443](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4443) \[merge]\
  Sat 2014-10-11 12:52:55 +0200
  * merge
  * [Revision #4441.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4441.1.2)\
    Sat 2014-10-11 09:09:18 +0200
    * compilation failure: ha\_cassandra
  * [Revision #4441.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4441.1.1) \[merge]\
    Fri 2014-10-10 20:59:06 +0200
    * merge
    * [Revision #4435.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4435.1.1) \[merge]\
      Thu 2014-10-09 10:30:11 +0200
      * 5.5.40+ merge
      * [Revision #3413.65.59](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.59)\
        Wed 2014-10-08 15:21:48 +0200
        * compilation fix for perl-Net-HandlerSocket
      * [Revision #3413.65.58](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.58)\
        Wed 2014-10-08 18:10:31 +0400
        * Backport from 10.0:
      * [Revision #3413.65.57](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.57)\
        Wed 2014-10-08 09:35:00 +0200
        * remove mariadb.pc file again, it cannot be added in a GA version
      * [Revision #3413.65.56](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.56)\
        Wed 2014-10-08 09:24:41 +0200
        * don't run privilege checking tests in embedded
      * [Revision #3413.65.55](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.55)\
        Wed 2014-10-08 00:46:10 +0200
        * decimal: _correct_ implementation of ROUND\_UP at last
      * [Revision #3413.65.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.54)\
        Wed 2014-10-08 00:45:56 +0200
        * include mariadb.pc in debian builds
      * [Revision #3413.65.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.53)\
        Wed 2014-10-08 00:45:41 +0200
        * jemalloc compatibility
      * [Revision #3413.65.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.52) \[merge]\
        Wed 2014-10-08 00:44:37 +0200
        * XtraDB 5.5.40-36.1
        * [Revision #0.48.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.48.6)\
          Tue 2014-10-07 21:41:48 +0200
          * percona-server-5.5.40-36.1
      * [Revision #3413.65.51](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.51)\
        Tue 2014-10-07 19:38:45 +0200
        * [MDEV-6781](https://jira.mariadb.org/browse/MDEV-6781): bug with query cache when using views
      * [Revision #3413.65.50](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.50)\
        Tue 2014-10-07 16:21:53 +0200
        * packaging issues: \* skip debian 44\_scriptsmysql\_configlibs.dpatch it does not apply anymore (and anyway it would not work for a static library) \* fix the path for install(mariadb.pc)
      * [Revision #3413.65.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.49)\
        Tue 2014-10-07 11:55:39 +0200
        * [MDEV-5553](https://jira.mariadb.org/browse/MDEV-5553) A view or procedure with a non existing definer can block "SHOW TABLE STATUS" with an unclear error message
      * [Revision #3413.65.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.48)\
        Tue 2014-10-07 10:54:14 +0200
        * [MDEV-4813](https://jira.mariadb.org/browse/MDEV-4813) Replication fails on updating a MEMORY table with an index using btree
      * [Revision #3413.65.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.47)\
        Tue 2014-10-07 10:53:43 +0200
        * fixes for decimal type
      * [Revision #3413.65.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.46)\
        Tue 2014-10-07 10:53:06 +0200
        * post-merge fixes
      * [Revision #3413.65.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.45) \[merge]\
        Mon 2014-10-06 20:06:39 +0200
        * XtraDB 5.5.39-36.0
        * [Revision #0.48.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.48.5)\
          Mon 2014-10-06 19:56:00 +0200
          * percona-server-5.5.39-36.0
      * [Revision #3413.65.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.44) \[merge]\
        Mon 2014-10-06 19:53:55 +0200
        * mysql-5.5.40
        * [Revision #3077.204.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.27)\
          Mon 2014-09-08 11:33:55 +0200
          * Adding patch for security bug 19471516
        * [Revision #3077.204.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.26)\
          Fri 2014-09-05 08:37:21 +0200
          * Applying the patch to remove [WL#7219](https://askmonty.org/worklog/?tid=7219) which was by mistake included by the dev team.
        * [Revision #3077.204.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.25)\
          Tue 2014-08-26 14:01:38 +0200
          * Renaming the enterprise packages to commercial
        * [Revision #3077.204.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.24)\
          Sat 2014-08-23 08:59:03 +0530
          * Bug#19370676 : YASSL PRE-AUTH BUFFER OVERFLOW WHEN CLIENT LIES ABOUT SUITE\_LEN\_ and Bug#19355577 : YASSL PRE-AUTH BUFFER OVERFLOW WHEN CLIENT LIES ABOUT COMP\_LEN\_
        * [Revision #3077.204.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.23)\
          Thu 2014-08-21 16:42:04 +0200
          * Bug#18928848 II. MALLOC OF UNINITIALIZED MEMORY SIZE
        * [Revision #3077.204.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.22) \[merge]\
          Wed 2014-08-20 09:46:38 +0200
          * Add my.cnf.d to regular rpm for EL7 build
          * [Revision #3077.205.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.205.7)\
            Tue 2014-08-12 19:37:49 +0200
            * Corrected typo
          * [Revision #3077.205.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.205.6)\
            Tue 2014-08-12 18:55:05 +0200
            * Experimental testing
          * [Revision #3077.205.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.205.5)\
            Tue 2014-08-12 18:26:46 +0200
            * Experimental testing for patch
          * [Revision #3077.205.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.205.4)\
            Tue 2014-08-12 16:53:31 +0200
            * Added my.cnf.d directory, removed mysql-5.5-libmysqlclient-symbols.patch
          * [Revision #3077.205.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.205.3)\
            Tue 2014-08-12 14:32:16 +0200
            * Add patch mysql-5.5-libmysqlclient-symbols.patch for el7
        * [Revision #3077.204.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.21)\
          Tue 2014-08-12 17:16:51 +0530
          * Bug #11755818 : LIKE DOESN'T MATCH WHEN CP932\_BIN/SJIS\_BIN COLLATIONS ARE USED.
        * [Revision #3077.204.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.20) \[merge]\
          Wed 2014-08-06 09:56:37 +0200\
          \*
          * Merge from mysql-5.5.39-ol7-release branch - Reverted version variable
          * [Revision #3077.205.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.205.2)\
            Mon 2014-08-04 15:56:19 +0200
            * Updated for el7 regular rpms
          * [Revision #3077.205.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.205.1)\
            Thu 2014-07-24 11:37:40 +0200
            * Bug#19223915 Provide mysql-compat-server dependencies
        * [Revision #3077.204.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.19)\
          Wed 2014-08-06 09:51:20 +0800
          * Remove unstable test case innodb\_bug18942294, approved by Jimmy over IM.
        * [Revision #3077.204.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.18)\
          Fri 2014-08-01 17:09:55 +0530
          * Bug #18415196 MYSQL\_UPGRADE DUPLICATE KEY ERROR FOR MYSQL.USER FOR 5.5.35+, 5.6.15+, 5.7.3+
        * [Revision #3077.204.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.17)\
          Fri 2014-08-01 14:18:28 +0530
          * Bug #18415196 MYSQL\_UPGRADE DUPLICATE KEY ERROR FOR MYSQL.USER FOR 5.5.35+, 5.6.15+, 5.7.3+
        * [Revision #3077.204.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.16) \[merge]\
          Thu 2014-07-31 12:30:05 +0200
          * Merge from mysql-5.5.39-release
        * [Revision #3077.204.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.15)\
          Thu 2014-07-31 12:52:49 +0300
          * Bug #18384260: MULTIPLE SECURITY ISSUES IN CERTIFICATE VALIDATION
        * [Revision #3077.204.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.14)\
          Mon 2014-07-28 11:19:19 +0400
        * [Revision #3077.204.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.13)\
          Mon 2014-07-21 11:26:50 +0530
          * Bug #17297324 GLIBC DOUBLE FREE OR CORRUPTION WHEN KILLING CLIENT; CTRL+C
        * [Revision #3077.204.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.12)\
          Thu 2014-07-17 11:21:18 +0530
          * Bug#14757009: WHEN THE GENERAL\_LOG IS A SOCKET AND THE READER GOES AWAY, MYSQL QUITS WORKING.
        * [Revision #3077.204.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.11) \[merge]\
          Wed 2014-07-09 12:39:19 +0200
          * Bug#19172145 - Remove perl(GD) and dtrace dependencies and bench fix
        * [Revision #3077.204.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.10)\
          Wed 2014-07-09 10:11:38 +0200
          * Bug #19149091 5.5 BUILD BREAKS ON LINUX IF SUN DTRACE IS INSTALLED
        * [Revision #3077.204.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.9)\
          Wed 2014-07-09 15:41:13 +0800
        * [Revision #3077.204.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.8)\
          Tue 2014-07-08 15:10:15 +0800
          * BUG#18942294 - SEGV IN DICT\_FIND\_TABLE\_BY\_SPACE TRYING TO MARK SPACE CORRUPT IN RECOVERY
        * [Revision #3077.204.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.7)\
          Mon 2014-07-07 12:05:30 +0200
          * Bug#18935421 RPAD DIES WITH CERTAIN PADSTR INTPUTS....
        * [Revision #3077.204.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.6)\
          Fri 2014-07-04 03:29:34 +0530
          * [WL#7219](https://askmonty.org/worklog/?tid=7219): Implement audit filter
        * [Revision #3077.204.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.5)\
          Thu 2014-07-03 14:12:02 +0530
          * Bug#18469276: MOD FOR SMALL DECIMALS FAILS
        * [Revision #3077.204.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.4)\
          Thu 2014-07-03 10:13:29 +0530
          * Bug #19140907 DUPLICATES IN UNIQUE SECONDARY INDEX BECAUSE OF FIX OF BUG#68021
        * [Revision #3077.204.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.3)\
          Wed 2014-07-02 14:52:52 +0530
          * Bug#17873011 NO DEPRECATION WARNING FOR THREAD\_CONCURRENCY
        * [Revision #3077.204.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.2)\
          Wed 2014-07-02 10:45:22 +0200
          * BUG#18779944: MYSQLDUMP BUFFER OVERFLOW
        * [Revision #3077.204.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.204.1)\
          Tue 2014-07-01 08:31:52 +0200
          * Raise version number after cloning 5.5.39
      * [Revision #3413.65.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.43)\
        Fri 2014-10-03 23:04:25 +0200
        * [MDEV-6743](https://jira.mariadb.org/browse/MDEV-6743) crash in GROUP\_CONCAT(IF () ORDER BY 1)
      * [Revision #3413.65.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.42)\
        Thu 2014-10-02 16:58:26 +0200
        * [MDEV-5749](https://jira.mariadb.org/browse/MDEV-5749) Please add a .pc file to MariaDB for easy use via pkg-config
      * [Revision #3413.65.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.41)\
        Thu 2014-10-02 13:52:51 +0200
        * [MDEV-6461](https://jira.mariadb.org/browse/MDEV-6461) mysqld should not trap SIGTSTP if running with --gdb/--debug-gdb
      * [Revision #3413.65.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.40)\
        Thu 2014-10-02 13:47:52 +0200
        * [MDEV-6550](https://jira.mariadb.org/browse/MDEV-6550) Missing dependency on Debian 7 (Wheezy) installation package
      * [Revision #3413.65.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.39)\
        Thu 2014-10-02 12:57:20 +0200
        * [MDEV-5707](https://jira.mariadb.org/browse/MDEV-5707) MTR fails on kfreebsd
      * [Revision #3413.65.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.38)\
        Thu 2014-10-02 11:58:24 +0200
        * [MDEV-6528](https://jira.mariadb.org/browse/MDEV-6528) review debian patches for mysql
      * [Revision #3413.65.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.37)\
        Thu 2014-10-02 11:58:13 +0200
        * [MDEV-6800](https://jira.mariadb.org/browse/MDEV-6800) auth\_socket plugin fails to build on OpenBSD with [MariaDB 10.0.14](../../old-releases/10.0/10.0.14.md)
      * [Revision #3413.65.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.36)\
        Thu 2014-10-02 11:57:40 +0200
        * [MDEV-5120](https://jira.mariadb.org/browse/MDEV-5120) Test suite test maria-no-logging fails
      * [Revision #3413.65.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.35)\
        Thu 2014-09-25 19:00:41 +0200
        * update tokudb version in CMakeLists.txt, disable unstable tokudb tests
      * [Revision #3413.65.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.34)\
        Fri 2014-10-03 15:07:53 +0400
        * [MDEV-6592](https://jira.mariadb.org/browse/MDEV-6592) Assertion \`ltime->day == 0' failed with TIMESTAMP, MAKETIME
      * [Revision #3413.65.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.33)\
        Thu 2014-09-25 10:43:11 +0400
        * [MDEV-6774](https://jira.mariadb.org/browse/MDEV-6774) - Deadlock between SELECT, DROP TABLE, SHOW STATUS and SET @@global.log\_output
      * [Revision #3413.65.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.32)\
        Thu 2014-09-18 19:45:06 +0400
        * [MDEV-6749](https://jira.mariadb.org/browse/MDEV-6749) - Deadlock between GRANT/REVOKE, SELECT FROM I\_S.COLUMNS, SET slow\_query\_log and failed connection attempt
* [Revision #4442](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4442)\
  Fri 2014-10-10 23:52:47 +0400
  * [MDEV-6519](https://jira.mariadb.org/browse/MDEV-6519): Assertion \`join->best\_read < double(...)' failed after adding a key to a TokuDB table...
* [Revision #4441](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4441)\
  Mon 2014-10-06 15:08:47 +0400
  * [MDEV-6442](https://jira.mariadb.org/browse/MDEV-6442): Assertion \`join->best\_read < double(...)' failed with optimizer\_use\_condition\_selectivity >=3
* [Revision #4440](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4440)\
  Fri 2014-10-10 17:08:12 +0400
  * [MDEV-6738](https://jira.mariadb.org/browse/MDEV-6738): use\_stat\_table + histograms crashing optimizer - When EITS code calls store\_key\_image\_to\_rec(), it should follow its calling convention (which is counter-intuitive)
* [Revision #4439](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439) \[merge]\
  Fri 2014-10-10 13:18:03 +0400
  * Merge 10.0-connect -> 10.0
  * [Revision #4424.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4424.1.1)\
    Thu 2014-10-09 17:23:37 +0200\
    \*
    * in CheckCond change strcat to strncat to avoid the case of non zero terminated string.
* [Revision #4438](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4438) \[merge]\
  Fri 2014-10-10 13:16:41 +0400
  * Merge 10.0-mroonga -> 10.0
  * [Revision #4426.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426.2.1) \[merge]\
    Fri 2014-10-03 09:47:41 +0400
    * Merge 10.0-mroonga -> 10.0
    * [Revision #4426.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426.1.1)\
      Fri 2014-10-03 11:30:53 +0900
      * fix Windows build disabling position
* [Revision #4437](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4437)\
  Thu 2014-10-09 12:25:45 +0400
  * Fixed mroonga build failure on Power8: define generic gcc version of GRN\_SET\_64BIT.
* [Revision #4436](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4436)\
  Mon 2014-10-06 15:29:22 +0400
  * [MDEV-6442](https://jira.mariadb.org/browse/MDEV-6442): Assertion \`join->best\_read < double(...)' failed with optimizer\_use\_condition\_selectivity >=3
* [Revision #4435](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4435)\
  Sun 2014-10-05 22:07:28 +0200
  * fix failing rpl.rpl\_user\_variables
* [Revision #4434](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4434)\
  Sun 2014-10-05 22:07:19 +0200
  * fix main.mysqldump test failing after Mroonga merge.
* [Revision #4433](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4433)\
  Sat 2014-10-04 20:43:39 +0200
  * fix out-of-source builds
* [Revision #4432](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4432)\
  Sat 2014-10-04 15:27:08 +0200
  * increase version
* [Revision #4431](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4431)\
  Sat 2014-10-04 15:26:04 +0200
  * xtradb/innodb: fix to compile with VS 2008
* [Revision #4430](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4430)\
  Tue 2014-09-30 17:06:02 +0200
  * cleanup: an outbreak of templatonia cured.
* [Revision #4429](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4429)\
  Tue 2014-09-30 15:57:38 +0200
  * fix more sql\_command\_flags: SQLCOM\_ASSIGN\_TO\_KEYCACHE should not be CF\_AUTO\_COMMIT\_TRANS SQLCOM\_PRELOAD\_KEYS should not be CF\_AUTO\_COMMIT\_TRANS SQLCOM\_INSTALL\_PLUGIN should need CF\_AUTO\_COMMIT\_TRANS SQLCOM\_UNINSTALL\_PLUGIN should need CF\_AUTO\_COMMIT\_TRANS
* [Revision #4428](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4428)\
  Tue 2014-09-30 15:55:02 +0200
  * BUG#13627921 - MISSING FLAGS IN SQL\_COMMAND\_FLAGS MAY LEAD TO REPLICATION PROBLEMS
* [Revision #4427](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4427)\
  Fri 2014-10-03 17:38:46 +0400
  * [MDEV-6533](https://jira.mariadb.org/browse/MDEV-6533) - MySQL Bug#72718 - CACHE\_LINE\_SIZE in innodb should be 128 on POWER
* [Revision #4426](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4426) \[merge]\
  Thu 2014-10-02 15:48:20 +0400
  * Merge 10.0-mroonga -> 10.0
  * [Revision #4410.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4410.1.2)\
    Thu 2014-10-02 14:58:57 +0400\
    \*
    * Changing Mroonga maturnity from STABLE to BETA - removing libmysql/libmysql.version from .bzrignore, as we don't have this file any more
  * [Revision #4410.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4410.1.1)\
    Sun 2014-09-21 00:33:45 +0900
    * Update Mroonga to the latest version on 2014-09-21T00:33:44+0900
* [Revision #4425](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4425)\
  Wed 2014-10-01 13:03:50 +0300
  * Fixed compiler warning. Now [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) compiles without warnings for me. (Except Instantiation notices from oqgraph that I don't know what to do with)
* [Revision #4424](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4424) \[merge]\
  Wed 2014-10-01 11:16:50 +0400
  * Merge 10.0-connect -> 10.0
  * [Revision #3984.2.51](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.51)\
    Tue 2014-09-30 12:59:24 +0200
    * Fix [MDEV-6802](https://jira.mariadb.org/browse/MDEV-6802) in a clean way. Add an union in the PARM structure to contain int values Use a cast to ptrdiff\_t in MAPFAM/MXPFAM::InitDelete required by some compilers
  * [Revision #3984.2.50](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.50)\
    Tue 2014-09-30 01:25:53 +0200
    * Add #include needed by GCC to declare uintptr\_t
  * [Revision #3984.2.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.49)\
    Tue 2014-09-30 00:53:00 +0200
    * Fix all compiler issues on FreeBSD clang.
  * [Revision #3984.2.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.48)\
    Mon 2014-09-29 14:42:50 +0200
    * fix [MDEV-6802](https://jira.mariadb.org/browse/MDEV-6802): MPXFAM::GetNextPos redefined
  * [Revision #3984.2.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.47)\
    Sat 2014-09-27 12:26:36 +0200
    * Add some new tests
  * [Revision #3984.2.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.46)\
    Sat 2014-09-27 12:09:37 +0200
    * Fix: Crash of an XCOL table when the Colname column size is too small. Was because of buffer overrun in XCLCOL::ReadColumn. The Cbuf buffer was unconditionally filled Now it is limited to its size. This happened because this buffer was allocated according to the XCOL column size. It is now allocated according to the source column size.
  * [Revision #3984.2.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.45)\
    Wed 2014-09-17 00:51:40 +0200\
    \*
    * Fix a compile error ([MDEV-6723](https://jira.mariadb.org/browse/MDEV-6723))
* [Revision #4423](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4423)\
  Wed 2014-10-01 11:13:11 +0400
  * Tests connect.odbc\_postgresql and connect.odbc\_oracle failed after revision 4363 (fixes for [MDEV-6661](https://jira.mariadb.org/browse/MDEV-6661) and [MDEV-6666](https://jira.mariadb.org/browse/MDEV-6666)).
* [Revision #4422](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4422) \[merge]\
  Tue 2014-09-30 20:43:14 +0300
  * Auto merge
  * [Revision #4419.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4419.1.2)\
    Tue 2014-09-30 20:31:14 +0300
    * [MDEV-5120](https://jira.mariadb.org/browse/MDEV-5120) Test suite test maria-no-logging fails
  * [Revision #4419.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4419.1.1)\
    Tue 2014-09-30 20:12:59 +0300
    * Fixed warnings
* [Revision #4421](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4421)\
  Tue 2014-09-30 21:28:36 +0400
  * [MDEV-6808](https://jira.mariadb.org/browse/MDEV-6808), part#2.
* [Revision #4420](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4420)\
  Tue 2014-09-30 21:11:03 +0400
  * [MDEV-6808](https://jira.mariadb.org/browse/MDEV-6808): [MariaDB 10.0.13](../../old-releases/10.0/10.0.13.md) crash with optimizer\_use\_condition\_selectivity > 1
* [Revision #4419](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4419)\
  Fri 2014-09-26 18:48:40 +0400
  * [MDEV-6799](https://jira.mariadb.org/browse/MDEV-6799): Crash in field\_conv, memcpy\_field\_possible - Fix the crash, dont call from->type() at the start of the function because it might be unsafe. - Unfortunately there is no testcase - And this is also the reason we can't fix it properly (it should be safe to call from->type() here).
* [Revision #4418](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4418)\
  Thu 2014-09-25 19:12:52 +0400
  * [MDEV-6788](https://jira.mariadb.org/browse/MDEV-6788): The variable 'role' is being used without being initialized at sql\_acl.cc:8840
* [Revision #4417](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4417)\
  Thu 2014-09-25 18:16:29 +0400
  * [MDEV-6788](https://jira.mariadb.org/browse/MDEV-6788): The variable 'role' is being used without being initialized at sql\_acl.cc:8840

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
