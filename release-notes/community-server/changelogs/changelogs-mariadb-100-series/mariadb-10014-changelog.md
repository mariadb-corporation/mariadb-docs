# MariaDB 10.0.14 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.14)[Release Notes](../../old-releases/10.0/10.0.14.md)[Changelog](mariadb-10014-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 26 Sep 2014

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.14.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4416](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4416)\
  Wed 2014-09-24 15:41:42 +0200
  * [MDEV-6743](https://jira.mariadb.org/browse/MDEV-6743) crash in GROUP\_CONCAT(IF () ORDER BY 1)
* [Revision #4415](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4415)\
  Wed 2014-09-24 17:27:00 +0400
  * [MDEV-6776](https://jira.mariadb.org/browse/MDEV-6776) ujis and eucjmps erroneously accept 0x8EA0 as a valid byte sequence
* [Revision #4414](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4414)\
  Wed 2014-09-24 13:08:47 +0200
  * remove the bug fix for [MDEV-6743](https://jira.mariadb.org/browse/MDEV-6743) "crash in GROUP\_CONCAT(IF () ORDER BY 1)"
* [Revision #4413](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4413) \[merge]\
  Tue 2014-09-23 23:55:29 +0200
  * 5.5 merge
  * [Revision #3413.65.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.31) \[merge]\
    Tue 2014-09-23 23:37:35 +0200
    * merge
    * [Revision #3413.66.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.66.2) \[merge]\
      Tue 2014-09-23 22:03:35 +0200
      * tokudb 7.5.0
    * [Revision #3413.66.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.66.1)\
      Fri 2014-09-19 09:21:51 +0200
      * remove unused (obsolete) declarations from slave.h
  * [Revision #3413.65.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.30)\
    Tue 2014-09-23 13:57:55 +0300
    * Allow tokudb test to pass even if jemalloc is not available.
  * [Revision #3413.65.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.29)\
    Tue 2014-09-23 13:57:29 +0300
    * [MDEV-6743](https://jira.mariadb.org/browse/MDEV-6743) crash in GROUP\_CONCAT(IF () ORDER BY 1)
* [Revision #4412](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4412)\
  Tue 2014-09-23 15:58:54 +0400
  * Adding tests for handling 0x5C as the second byte in a multi-byte sequence, and as a escape character when SET NAMES xxx, character\_set\_connection=binary; for cp932,big5,gbk,sjis
* [Revision #4411](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4411)\
  Mon 2014-09-22 23:25:56 +0300
  * Fixed test failures Added comments Ensure that tokudb test works even if jemalloc is not installed Removed not referenced function Item::remove\_fixed()
* [Revision #4410](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4410) \[merge]\
  Thu 2014-09-18 21:54:45 +0200
  * 5.5 merge
  * [Revision #3413.65.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.28)\
    Thu 2014-09-18 17:00:44 +0200
    * support statically linked jemalloc. use that for release builds
* [Revision #4409](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4409)\
  Thu 2014-09-18 15:24:30 +0200
  * print binlog unsafe errors at log\_warnings level 1, not 2.
* [Revision #4408](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4408)\
  Thu 2014-09-18 12:40:55 +0400
  * [MDEV-6752](https://jira.mariadb.org/browse/MDEV-6752) Trailing incomplete characters are not replaced to question marks on conversion
* [Revision #4407](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4407)\
  Thu 2014-09-18 09:26:30 +0900
  * Merge Spider 3.2.11
* [Revision #4406](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4406)\
  Wed 2014-09-17 19:38:42 +0200
  * fixes for valgrind failures
* [Revision #4405](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4405)\
  Wed 2014-09-17 15:11:24 +0200
  * fix intermittent failures of main.create\_or\_replace test in buildbot
* [Revision #4404](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4404) \[merge]\
  Tue 2014-09-16 14:08:05 +0200
  * merge
  * [Revision #4399.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4399.1.3)\
    Tue 2014-09-16 14:04:50 +0200
    * fixes for test cases
  * [Revision #4399.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4399.1.2) \[merge]\
    Tue 2014-09-16 14:03:17 +0200
    * 5.5 merge
  * [Revision #4399.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4399.1.1) \[merge]\
    Sat 2014-09-13 00:30:46 +0200
    * sphinx 2.1.9
* [Revision #4403](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4403)\
  Tue 2014-09-16 07:37:00 +0300
  * Avoid using log\_sys mutex when printing out show engine innodb status, instead peek (maybe) old data.
* [Revision #4402](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4402) \[merge]\
  Tue 2014-09-16 00:06:05 +0300
  * Auto merge
  * [Revision #4400.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4400.1.3)\
    Tue 2014-09-16 00:00:47 +0300
    * Don't give warning if there are two unique keys used with INSERT .. ON DUPLICATE KEY UPDATE. We should assume that the store engine will report the first duplicate key for this case.
  * [Revision #4400.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4400.1.2)\
    Mon 2014-09-15 23:52:40 +0300
    * Fixed randomly failing test
  * [Revision #4400.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4400.1.1)\
    Mon 2014-09-15 17:11:01 +0300
    * Use LOCK\_show\_status when we add things to all\_status\_vars This was missing in my last commit for fixing possible lockups in SHOW STATUS.
* [Revision #4401](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4401)\
  Mon 2014-09-15 20:33:11 +0400
  * Changes in storage\_engine test suite:
* [Revision #4400](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4400)\
  Sat 2014-09-13 17:15:11 +0400
  * Adding big5, cp932, gbk, sjis tests covering characters that can have 0x5C as the second byte in a multi-byte character.
  * Adding big5 tests covering an unassigned character 0xC840 being stored into char/varchar/text/enum columns.
* [Revision #4399](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4399) \[merge]\
  Fri 2014-09-12 16:44:27 +0200
  * 10.0-connect merge
  * [Revision #3984.2.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.44)\
    Sat 2014-09-06 18:08:28 +0200
    * Fix [MDEV-6624](https://jira.mariadb.org/browse/MDEV-6624) (indexing on void table)
  * [Revision #3984.2.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.43)\
    Fri 2014-09-05 14:18:31 +0200
    * Fix [MDEV-6686](https://jira.mariadb.org/browse/MDEV-6686) (buffer overflow in MakeRecord)
  * [Revision #3984.2.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.42)\
    Tue 2014-09-02 01:40:15 +0200
    * Initialise min/max buffer to 0 to avoid valgrind complaining that uninitialised characters be written in op file.
  * [Revision #3984.2.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.41)\
    Fri 2014-08-29 14:22:25 +0200
    * Avoid uninitialised warning from valgrind
  * [Revision #3984.2.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.40)\
    Wed 2014-08-27 14:56:20 +0200
    * Fix a bug in DOSFAM::OpenTableFile. Bin was not set to TRUE for blocked tables. This caused a CR character to be left in the line and in particular caused the updelx test to fail on Windows.
  * [Revision #3984.2.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.39)\
    Wed 2014-08-27 00:49:07 +0200
    * Fix a test failure. Due to mmap on void file being accepted on Windows while returning an error on Linux. Now accepted on linux.
  * [Revision #3984.2.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.38)\
    Mon 2014-08-25 18:51:53 +0200
    * Adding a test for indexed UPDATE/DELETE added: storage/connect/mysql-test/connect/r/updelx.result storage/connect/mysql-test/connect/t/updelx.inc storage/connect/mysql-test/connect/t/updelx.test
  * [Revision #3984.2.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.37)\
    Mon 2014-08-25 18:34:51 +0200
    * Make storing and sorting values using less memory allocation (while doing indexed UPDATE/DELETE)
  * [Revision #3984.2.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.36)\
    Sun 2014-08-24 11:19:02 +0200
    * Fix a compile error on Linux
  * [Revision #3984.2.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.35)\
    Sat 2014-08-23 19:17:15 +0200
    * Move DataPath from the MYCAT catalog to the ha\_connect handler. Indeed it belongs to each tables and the catalog being share between several instances of CONNECT, when a query implied several tables belonging to different databases, some where pointing on the wrong database. This fix bugs occuring in queries such as: INSERT into db1.t1 select \* from db2.t2; Where the t1 data file was made in db2.
  * [Revision #3984.2.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.34)\
    Fri 2014-08-22 17:30:22 +0200
    * Add a new CONNECT global variable allowing to tell whether or not a temporary file should be used for UPDATE/DELETE of file tables. Also use the "sorted" argument of index\_init to help decide if sorting of positions must be done.
  * [Revision #3984.2.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.33)\
    Fri 2014-08-15 18:05:10 +0200
    * Remove a gcc warning
  * [Revision #3984.2.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.32)\
    Sat 2014-08-16 16:46:35 +0200
    * Modifies the way indexed UPDATE/DELETE are sorted in order to execute them sorted by file position. Firstly a new value is stored in indexes to know if they are sorted, preventing to do the sorting when it is not needed. Secondly, almost all in now done in connect instead of being done by the different file access method classes. This pepares the future use of temporary files for all table types and also fix the bug that was occuring when partially using a multi-column index because of false MRR like call of position followed by unsorted rnd\_pos no more using indexing.
  * [Revision #3984.2.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.31)\
    Fri 2014-08-08 19:53:44 +0200
    * Update part\_file.result to match the test change
  * [Revision #3984.2.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.30)\
    Fri 2014-08-08 19:46:02 +0200
    * Fix [MDEV-6502](https://jira.mariadb.org/browse/MDEV-6502)
* [Revision #4398](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4398)\
  Fri 2014-09-12 16:06:18 +0400
  * [MDEV-6737](https://jira.mariadb.org/browse/MDEV-6737) Stored routines do now work with swe7: "The table mysql.proc is missing, corrupt, or contains bad data" Fixed the bug itself. Also, added "SET NAMES swe7" which was forgotten in the previous commit, so latin1 was actually tested lati1 instead of swe7 in a mistake. Now it tests swe7.
* [Revision #4397](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4397)\
  Fri 2014-09-12 14:49:24 +0300
  * Fixed compiler warnings
* [Revision #4396](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4396)\
  Fri 2014-09-12 14:49:13 +0300
  * Don't use LOCK\_status for the duration of SHOW STATUS because of possible lookups. Instead we use LOCK\_status only to protect summary of thread statistics and use a new mutex, LOCK\_show\_status to protect concurrent SHOW STATUS.
* [Revision #4395](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4395)\
  Fri 2014-09-12 14:45:11 +0300
  * Cleanup of my\_hash\_sort patch
* [Revision #4394](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4394)\
  Fri 2014-09-12 12:57:27 +0400
  * Adding thorough tests covering what happens with escaped sequences in the SQL parser.
* [Revision #4393](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4393)\
  Fri 2014-09-12 03:21:54 +0400
  * Fixes in storage\_engine test suite
* [Revision #4392](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4392) \[merge]\
  Thu 2014-09-11 23:50:31 +0300
  * Automatic merge
  * [Revision #4381.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4381.1.3)\
    Thu 2014-09-11 22:42:35 +0300
    * [MDEV-6255](https://jira.mariadb.org/browse/MDEV-6255) DUPLICATE KEY Errors on SELECT .. GROUP BY that uses temporary and filesort.
  * [Revision #4381.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4381.1.2)\
    Tue 2014-09-09 17:37:08 +0300
    * [MDEV-6698](https://jira.mariadb.org/browse/MDEV-6698): safe\_mutex: Found wrong usage of mutex 'log\_space\_lock' and 'LOCK\_log'
  * [Revision #4381.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4381.1.1)\
    Mon 2014-09-08 20:56:56 +0300
    * Fixed two bugs with CREATE OR REPLACE and LOCK TABLES: [MDEV-6560](https://jira.mariadb.org/browse/MDEV-6560)
* [Revision #4391](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4391) \[merge]\
  Thu 2014-09-11 16:44:16 +0200
  * XtraDB 5.6.20-68.0
  * [Revision #0.12.72](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.72)\
    Thu 2014-09-11 10:15:01 +0200
    * percona-server-5.6.20-68.0
* [Revision #4390](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4390) \[merge]\
  Thu 2014-09-11 16:42:54 +0200
  * InnoDB 5.6.20
  * [Revision #0.49.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.49.6)\
    Thu 2014-09-11 10:13:35 +0200
    * 5.6.20
* [Revision #4389](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4389)\
  Thu 2014-09-11 15:41:30 +0300
  * [MDEV-6729](https://jira.mariadb.org/browse/MDEV-6729): InnoDB: Failing assertion: state == TRX\_STATE\_NOT\_STARTED in file trx0trx.ic line 60
* [Revision #4388](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4388)\
  Wed 2014-09-10 17:45:09 +0200
  * [MDEV-6647](https://jira.mariadb.org/browse/MDEV-6647) MariaDB CLI client doesnt show CREATE INDEX progress
* [Revision #4387](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4387)\
  Wed 2014-09-10 13:22:44 +0200
  * [MDEV-6459](https://jira.mariadb.org/browse/MDEV-6459) max\_relay\_log\_size and sql\_slave\_skip\_counter misbehave on PPC64
* [Revision #4386](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4386)\
  Wed 2014-09-10 13:22:20 +0200
  * [MDEV-6523](https://jira.mariadb.org/browse/MDEV-6523) CONNECT temporary table created
* [Revision #4385](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4385)\
  Wed 2014-09-10 13:22:01 +0200
  * [MDEV-6565](https://jira.mariadb.org/browse/MDEV-6565) search order for my.cnf inconsistent in docs/use, and global override with build-time -DDEFAULT\_SYSCONFDIR is ignored
* [Revision #4384](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4384) \[merge]\
  Wed 2014-09-10 13:10:24 +0200
  * [MDEV-6579](https://jira.mariadb.org/browse/MDEV-6579) IMPORT\_EXECUTABLES feature broken by addition of gen\_pfs\_lex\_token
  * [Revision #4347.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4347.1.2)\
    Fri 2014-08-15 22:54:07 +0100
    * [MDEV-6579](https://jira.mariadb.org/browse/MDEV-6579): Properly handle gen\_pfs\_lex\_token when cross-compiling
* [Revision #4383](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4383)\
  Mon 2014-09-08 12:59:57 +0200
  * compilation fixes for WITH\_ATOMIC\_OPS=rwlocks
* [Revision #4382](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4382)\
  Sun 2014-09-07 22:04:29 +0200
  * typos in cmake -DWITH\_ATOMIC\_OPS=xxx
* [Revision #4381](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4381)\
  Sun 2014-09-07 20:40:36 +0200
  * [MDEV-6638](https://jira.mariadb.org/browse/MDEV-6638) mysql\_options4 symbol missing from libmysqlclient.so.18
* [Revision #4380](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4380)\
  Sun 2014-09-07 20:19:29 +0200
  * compilation failure on x86
* [Revision #4379](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4379)\
  Sun 2014-09-07 20:19:12 +0200
  * [MDEV-6580](https://jira.mariadb.org/browse/MDEV-6580) Assertion \`thd' failed in my\_malloc\_size\_cb\_func upon writing status report into error log
* [Revision #4378](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4378) \[merge]\
  Sun 2014-09-07 20:18:17 +0200
  * [MDEV-6562](https://jira.mariadb.org/browse/MDEV-6562) [MDEV-6410](https://jira.mariadb.org/browse/MDEV-6410) breaks WITHOUT\_SERVER build
  * [Revision #4347.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4347.1.1)\
    Mon 2014-08-11 22:43:29 +0100
    * [MDEV-6562](https://jira.mariadb.org/browse/MDEV-6562): Fix WITHOUT\_SERVER build
* [Revision #4377](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4377)\
  Sat 2014-09-06 09:46:41 +0200
  * [MDEV-6610](https://jira.mariadb.org/browse/MDEV-6610) Assertion \`thd->is\_error() || thd->killed' failed in mysql\_execute\_command on executing an SP with repeated CREATE TABLE .. SELECT
* [Revision #4376](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4376)\
  Sat 2014-09-06 08:33:56 +0200
  * [MDEV-6616](https://jira.mariadb.org/browse/MDEV-6616) Server crashes in my\_hash\_first if shutdown is performed when FLUSH LOGS is running
* [Revision #4375](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4375)\
  Thu 2014-09-04 21:58:48 +0400
  * [MDEV-6695](https://jira.mariadb.org/browse/MDEV-6695) Bad column name for UCS2 string literals The Item\_string constructors called set\_name() on the source string, which was wrong because in case of UCS2/UTF16/UTF32 the source value might be a not well formed string (e.g. have incomplete leftmost character). Now set\_name() is called on str\_value after its copied (with optionally left zero padding) from the source string.
  * [MDEV-6694](https://jira.mariadb.org/browse/MDEV-6694) Illegal mix of collation with a PS parameter Item\_param::convert\_str\_value() did not set repertoire. Introducing a new structure MY\_STRING\_METADATA to collect character length and repertoire of a string in a single loop, to avoid two separate loops. Adding a new class Item\_basic\_value::Metadata as a convenience wrapper around MY\_STRING\_METADATA, to reuse the code between Item\_string and Item\_param.
* [Revision #4374](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4374)\
  Thu 2014-09-04 12:43:41 +0400
  * Creating a new class in\_string::Item\_string\_for\_in\_vector and moving set\_value() from Item\_string to Item\_string\_for\_in\_vector, as set\_value() updates the members incompletely (e.g. does not update max\_length), so it was dangerous to have set\_value() available in Item\_string.
* [Revision #4373](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4373)\
  Thu 2014-09-04 12:15:05 +0400
  * Using more Item\_string\_sys
* [Revision #4372](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4372)\
  Thu 2014-09-04 08:50:06 +0400
  * [MDEV-6044](https://jira.mariadb.org/browse/MDEV-6044) MySQL BUG#12735829 - SPACE() FUNCTION WARNING REFERS TO REPEAT() IN ER\_WARN\_ALLOWED\_PACKET\_OVERFLOWED Merged from 5.6
* [Revision #4371](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4371)\
  Wed 2014-09-03 18:24:31 +0400
  * Adding Item\_string\_sys and Item\_string\_ascii to reduce duplicate code
* [Revision #4370](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4370)\
  Wed 2014-09-03 16:31:47 +0400
  * [MDEV-6688](https://jira.mariadb.org/browse/MDEV-6688) Illegal mix of collation with bit string B'01100001'
* [Revision #4369](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4369)\
  Tue 2014-09-02 14:07:01 +0200
  * [MDEV-6462](https://jira.mariadb.org/browse/MDEV-6462): Slave replicating using GTID doesn't recover correctly when master crashes in the middle of transaction
* [Revision #4368](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4368)\
  Wed 2014-09-03 01:56:21 +0400
  * Moving Item::str\_value from public to protected.
* [Revision #4367](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4367)\
  Wed 2014-09-03 01:47:39 +0400
  * [MDEV-6683](https://jira.mariadb.org/browse/MDEV-6683) A parameter and a string literal with the same values are not recognized as equal by the optimizer
* [Revision #4366](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4366)\
  Tue 2014-09-02 22:04:48 +0400
  * [MDEV-6679](https://jira.mariadb.org/browse/MDEV-6679) Different optimizer plan for "a BETWEEN 'string' AND ?" and "a BETWEEN ? AND 'string'" Item\_string::eq() and Item\_param::eq() in string context behaved differently. Introducing a new class Item\_basic\_value to share the eq() code between literals (Item\_int, Item\_double, Item\_string, Item\_null) and Item\_param.
* [Revision #4365](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4365)\
  Tue 2014-09-02 17:50:09 +0300
  * [MDEV-6682](https://jira.mariadb.org/browse/MDEV-6682) innodb.innodb\_simulate\_comp\_failures\_small is too slow if it's run on a real disk
* [Revision #4364](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4364)\
  Tue 2014-09-02 17:34:29 +0400
  * A clean-up for the previous patch
* [Revision #4363](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4363)\
  Mon 2014-09-01 20:57:32 +0400
  * [MDEV-6661](https://jira.mariadb.org/browse/MDEV-6661) PI() does not work well in UCS2/UTF16/UTF32 context [MDEV-6666](https://jira.mariadb.org/browse/MDEV-6666) Malformed result for CONCAT(utf8\_column, binary\_string)
* [Revision #4362](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4362)\
  Mon 2014-08-25 13:35:33 +0300
  * [MDEV-6590](https://jira.mariadb.org/browse/MDEV-6590): InnoDB recover ends in signal 11
* [Revision #4361](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4361)\
  Thu 2014-08-21 21:25:22 +0200
  * [MDEV-6625](https://jira.mariadb.org/browse/MDEV-6625) SHOW GRANTS for current\_user\_name@wrong\_host\_name
* [Revision #4360](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4360)\
  Sun 2014-08-10 14:36:17 +0200
  * sanity
* [Revision #4359](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4359)\
  Wed 2014-08-20 15:02:10 +0200
  * Fix test case that requires dbug to not fail in release build.
* [Revision #4358](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4358)\
  Wed 2014-08-20 10:59:39 +0200
  * [MDEV-6321](https://jira.mariadb.org/browse/MDEV-6321): close\_temporary\_tables() in format description event not serialised correctly
* [Revision #4357](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4357)\
  Tue 2014-08-19 14:26:42 +0200
  * [MDEV-6321](https://jira.mariadb.org/browse/MDEV-6321): close\_temporary\_tables() in format description event not serialised correctly
* [Revision #4356](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4356)\
  Wed 2014-07-02 12:51:45 +0200
  * [MDEV-6321](https://jira.mariadb.org/browse/MDEV-6321): close\_temporary\_tables() in format description event not serialised correctly
* [Revision #4355](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4355) \[merge]\
  Tue 2014-08-19 21:35:14 +0300
  * Automatic merge from 5.5 Fixed 2 failing tests by replacing result files
  * [Revision #3413.65.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.7)\
    Tue 2014-08-19 19:28:35 +0300
    * [MDEV-6450](https://jira.mariadb.org/browse/MDEV-6450) - MariaDB crash on Power8 when built with advance tool chain
  * [Revision #3413.65.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.6)\
    Wed 2014-08-13 15:46:39 +0200
    * Change a couple of permissions that cause lintian warnings in .deb packaging and don't really hurt to fix.
  * [Revision #3413.65.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.5)\
    Wed 2014-08-13 09:37:12 +0300
    * [MDEV-6546](https://jira.mariadb.org/browse/MDEV-6546): innodb.innodb\_simulate\_comp\_failures\_small fails sporadically
  * [Revision #3413.65.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.4)\
    Tue 2014-08-12 17:12:08 +0200
    * disable still racy tokudb tests
  * [Revision #3413.65.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.3)\
    Tue 2014-08-12 16:39:12 +0200
    * [MDEV-5706](https://jira.mariadb.org/browse/MDEV-5706) MariaDB does not build on hurd-i386
  * [Revision #3413.65.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.2)\
    Tue 2014-08-05 20:22:57 +0200
    * fix tokudb version
  * [Revision #3413.65.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.65.1)\
    Tue 2014-08-12 19:14:52 +0400
    * Increased the version number
* [Revision #4354](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4354)\
  Fri 2014-08-15 11:31:13 +0200
  * [MDEV-6551](https://jira.mariadb.org/browse/MDEV-6551): Some replication errors are ignored if slave\_parallel\_threads > 0
* [Revision #4353](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4353)\
  Thu 2014-08-14 15:38:08 +0300
  * If one uses 3 `--verbose` options to mysql\_upgrade or mysqlcheck one will now get on stdout all ALTER, RENAME and CHECK commands that mysqlcheck executes. If one uses 4 `--verbose` to mysql\_upgrade it will also write out all mysqlcheck commands invoked.
* [Revision #4352](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4352)\
  Thu 2014-08-14 15:36:48 +0300
  * Added Innobase .ic and errmsg-utf8.txt to tagged files Fixed compiler warning
* [Revision #4351](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4351)\
  Wed 2014-08-13 13:34:28 +0200
  * [MDEV-6549](https://jira.mariadb.org/browse/MDEV-6549), failing to update gtid\_slave\_pos for a transaction that was retried.
* [Revision #4350](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4350)\
  Wed 2014-08-13 09:10:56 +0300
  * [MDEV-6546](https://jira.mariadb.org/browse/MDEV-6546): innodb.innodb\_simulate\_comp\_failures\_small fails sporadically
* [Revision #4349](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4349)\
  Tue 2014-08-12 19:16:44 +0400
  * Increased the version number
* [Revision #4348](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4348)\
  Tue 2014-08-12 07:52:19 +0400
  * Recoding feedback\_plugin\_send.result (forgotten in the previous commit).
* [Revision #4347](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4347)\
  Mon 2014-08-11 05:45:45 +0400
  * [MDEV-6274](https://jira.mariadb.org/browse/MDEV-6274) Collation usage statistics Adding collation usage statistics into the feedback plugin I\_S table.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
