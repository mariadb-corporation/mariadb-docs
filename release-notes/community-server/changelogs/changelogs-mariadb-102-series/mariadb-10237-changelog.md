# MariaDB 10.2.37 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download 10.2.37](https://downloads.mariadb.org/mariadb/10.2.37/)[Release Notes](../../old-releases/10.2/10.2.37.md)[Changelog](mariadb-10237-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 22 Feb 2021

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.37.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #ce3a2a688d](https://github.com/MariaDB/server/commit/ce3a2a688d)\
  2021-02-18 14:20:48 +0100
  * make @@wsrep\_provider and @@wsrep\_notify\_cmd read-only
* [Revision #cbbbdb9c3b](https://github.com/MariaDB/server/commit/cbbbdb9c3b)\
  2021-02-18 12:16:11 +0100
  * don't allocate 64K on the stack
* [Revision #e7d9c1d498](https://github.com/MariaDB/server/commit/e7d9c1d498)\
  2021-02-05 18:33:36 +0100
  * Fix connect engine ppc64 fail
* [Revision #dc31627c2d](https://github.com/MariaDB/server/commit/dc31627c2d)\
  2021-02-05 11:24:05 +0100
  * Fix of connect engine crashes
* [Revision #c04ae0d365](https://github.com/MariaDB/server/commit/c04ae0d365)\
  2021-02-03 15:35:32 +0100
  * Fix of crashes of connect engine.
* [Revision #87bf594bc5](https://github.com/MariaDB/server/commit/87bf594bc5)\
  2021-02-03 10:44:44 +0100
  * Fix of random crashes of connect engine (probably depend on addresses used)-
* [Revision #716b0b44f8](https://github.com/MariaDB/server/commit/716b0b44f8)\
  2021-02-02 10:49:13 +0100
  * Fix compiler warnings of the new connect engine.
* [Revision #b3cecb7bfc](https://github.com/MariaDB/server/commit/b3cecb7bfc)\
  2021-02-02 10:37:54 +0100
  * Revert "Fix of warnings on aarch64 like:"
* Merge [Revision #7f7e66147d](https://github.com/MariaDB/server/commit/7f7e66147d) 2021-02-02 10:36:46 +0100 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #571294f954](https://github.com/MariaDB/server/commit/571294f954)\
  2021-02-02 00:03:07 +0100
  * Fix failed test bson and xml
* [Revision #c2aecb0575](https://github.com/MariaDB/server/commit/c2aecb0575)\
  2021-01-30 12:07:37 +0100
  * Fix failed test bson and xml
* [Revision #7ab30f5d95](https://github.com/MariaDB/server/commit/7ab30f5d95)\
  2021-01-29 15:45:08 +0100
  * Update bson\_get\_item
* [Revision #848a1a613c](https://github.com/MariaDB/server/commit/848a1a613c)\
  2021-01-28 19:54:24 +0100
  * Fix decimal problems in bson udf's
* [Revision #7edd4294be](https://github.com/MariaDB/server/commit/7edd4294be)\
  2021-01-28 01:02:29 +0100
  * Continue BSON development
* [Revision #ff5186fd2b](https://github.com/MariaDB/server/commit/ff5186fd2b)\
  2021-01-29 19:31:07 +0200
  * List of unstable tests for 10.2.37 release
* [Revision #4a41712866](https://github.com/MariaDB/server/commit/4a41712866)\
  2021-01-28 23:29:43 +0200
  * Skip TokuDB within autobake-deb.sh
* [Revision #9c84852809](https://github.com/MariaDB/server/commit/9c84852809)\
  2021-01-29 12:42:34 +0100
  * fix of warning on windows
* [Revision #496f7090a8](https://github.com/MariaDB/server/commit/496f7090a8)\
  2021-01-29 12:35:17 +0100
  * Fix of warnings on aarch64 like: bson.cpp:1775:3: error: case label value is less than minimum value for type \[-Werror] case TYPE\_NULL: bson.cpp:1776:7: error: statement will never be executed \[-Werror=switch-unreachable] b = true;
* [Revision #40868c4765](https://github.com/MariaDB/server/commit/40868c4765)\
  2021-01-28 18:30:32 +0100
  * fix warnings returned by gcc v10.0
* Merge [Revision #8b4d92aa4c](https://github.com/MariaDB/server/commit/8b4d92aa4c) 2021-01-29 12:03:11 +0100 - Merge remote-tracking branch 'connect/10.2' 10.2
* [Revision #9a07f30ba2](https://github.com/MariaDB/server/commit/9a07f30ba2)\
  2021-01-20 19:19:54 +0100
  * Fix some Json and Bson bugs
* [Revision #1d627ce47c](https://github.com/MariaDB/server/commit/1d627ce47c)\
  2021-01-13 00:23:08 +0100
  * Fix failed test
* [Revision #c9b5e5286b](https://github.com/MariaDB/server/commit/c9b5e5286b)\
  2021-01-12 22:28:44 +0100
  * Fix failed test
* [Revision #347bce0201](https://github.com/MariaDB/server/commit/347bce0201)\
  2021-01-12 18:25:41 +0100
  * Remove static linkage to cpprestsdk when it is installed
* [Revision #70cfeb9bc9](https://github.com/MariaDB/server/commit/70cfeb9bc9)\
  2021-01-10 02:23:11 +0100
  * Re-include BSON into CMakeLists.txt
* [Revision #251a55dcb4](https://github.com/MariaDB/server/commit/251a55dcb4)\
  2021-01-10 01:05:38 +0100
  * Remove changes to CMakeLists.txt that cause compile error
* [Revision #02bb11709d](https://github.com/MariaDB/server/commit/02bb11709d)\
  2021-01-10 00:14:37 +0100
  * add the test on REST
* [Revision #8f34d45404](https://github.com/MariaDB/server/commit/8f34d45404)\
  2021-01-08 22:18:52 +0100
  * Add the new BSON temporary type for testing
* [Revision #cba46c9912](https://github.com/MariaDB/server/commit/cba46c9912)\
  2020-12-31 15:43:52 +0100
  * Fix jfile\_convert crash on error.
* [Revision #a35424829a](https://github.com/MariaDB/server/commit/a35424829a)\
  2020-12-26 19:44:38 +0100
  * Continue BSON implementation + fix create modified ha\_connect.cc
* [Revision #2113cab7ec](https://github.com/MariaDB/server/commit/2113cab7ec)\
  2020-12-22 22:50:12 +0100
  * Make REST tables default file name. Commit before continuing BSON development
* [Revision #24c18ce892](https://github.com/MariaDB/server/commit/24c18ce892)\
  2020-12-18 18:59:52 +0100
  * Fix json parser (void objects not recognized)
* [Revision #a786741000](https://github.com/MariaDB/server/commit/a786741000)\
  2020-12-17 13:58:13 +0100
  * Fix crash with JsonContains UDF + BSON development
* [Revision #ceacffbb3b](https://github.com/MariaDB/server/commit/ceacffbb3b)\
  2020-12-15 12:28:03 +0100
  * Fix pretty=2 Tabjson bug on INSERT. Occuring when inserting more than one line in one statement
* [Revision #aa10789f47](https://github.com/MariaDB/server/commit/aa10789f47)\
  2020-12-11 16:34:50 +0100
  * BSON development
* [Revision #4eeadedc77](https://github.com/MariaDB/server/commit/4eeadedc77)\
  2020-12-09 00:55:06 +0100
  * Fix json\_bjson (s was erase by Json\_Subset)
* [Revision #871532c3b9](https://github.com/MariaDB/server/commit/871532c3b9)\
  2020-12-08 01:15:40 +0100
  * Continue BSON implementation
* [Revision #c05b1288fd](https://github.com/MariaDB/server/commit/c05b1288fd)\
  2020-12-04 23:21:59 +0100
  * Remove a push warning causing failing assert. Modified storage/connect/filamap.cpp
* [Revision #4b6d661c7f](https://github.com/MariaDB/server/commit/4b6d661c7f)\
  2020-12-02 00:35:58 +0100
  * Fix failed compile modified storage/connect/ha\_connect.cc
* [Revision #7d439334ff](https://github.com/MariaDB/server/commit/7d439334ff)\
  2020-12-01 20:57:05 +0100
  * Fix failed compile modified storage/connect/ha\_connect.cc and mycat.cc
* [Revision #4e8af8a664](https://github.com/MariaDB/server/commit/4e8af8a664)\
  2020-12-01 19:30:56 +0100
  * Fix memory leak for the JSON table type (and continue BSON implementatio)
* [Revision #950bf6ab53](https://github.com/MariaDB/server/commit/950bf6ab53)\
  2020-11-27 10:25:47 +0100
  * Begin implementation of BSON
* [Revision #b656d3d333](https://github.com/MariaDB/server/commit/b656d3d333)\
  2020-11-25 17:42:01 +0100
  * Desesperatly trying to stop compiling failures
* [Revision #dc8f914c38](https://github.com/MariaDB/server/commit/dc8f914c38)\
  2020-11-25 12:56:45 +0100
  * Remove based enum not accepted by most gcc compilers
* [Revision #dae4bd0b36](https://github.com/MariaDB/server/commit/dae4bd0b36)\
  2020-11-21 23:14:06 +0100
  * Fix xml.test failure. Fix compile error modified json.h
* [Revision #477b5256dd](https://github.com/MariaDB/server/commit/477b5256dd)\
  2020-11-21 21:52:48 +0100
  * Fix some test failure
* [Revision #038381e110](https://github.com/MariaDB/server/commit/038381e110)\
  2020-11-20 15:21:06 +0100
  * Fix compile error. Modified json.cpp
* [Revision #a526965c61](https://github.com/MariaDB/server/commit/a526965c61)\
  2020-11-20 12:17:50 +0100
  * delete bld2
* [Revision #eb21ac65c1](https://github.com/MariaDB/server/commit/eb21ac65c1)\
  2020-11-20 11:43:39 +0100
  * ???
* [Revision #000268d46f](https://github.com/MariaDB/server/commit/000268d46f)\
  2020-11-19 19:05:04 +0100
  * Fix some json discovery problems. Modified tabjson.cpp tabjson.h
* [Revision #da10bf2d56](https://github.com/MariaDB/server/commit/da10bf2d56)\
  2020-11-18 16:10:23 +0100
  * remove large file
* Merge [Revision #9055db73d5](https://github.com/MariaDB/server/commit/9055db73d5) 2020-11-18 14:37:44 +0100 - Commit new source and all recent changes.
* [Revision #8771390dfd](https://github.com/MariaDB/server/commit/8771390dfd)\
  2020-11-14 18:28:16 +0100
  * Change cURL option from > to -o. modified storage/connect/tabrest.cpp
* [Revision #9193ceb2c4](https://github.com/MariaDB/server/commit/9193ceb2c4)\
  2020-11-13 19:42:56 +0100
  * Fix getting proper table type in discovery. modified storage/connect/ha\_connect.cc
* [Revision #17ea1efe0a](https://github.com/MariaDB/server/commit/17ea1efe0a)\
  2020-11-11 17:41:11 +0100
  * Fix using a null pointer. modified storage/connect/tabrest.cpp
* [Revision #8c617e9901](https://github.com/MariaDB/server/commit/8c617e9901)\
  2020-11-11 12:55:07 +0100
  * Add getting REST query answer via curl. modified storage/connect/tabrest.cpp
* [Revision #878065b4df](https://github.com/MariaDB/server/commit/878065b4df)\
  2020-11-08 14:25:35 +0100
  * Fix compile error (sign-compare) Modified jsonudf.cpp jsonudf.h
* [Revision #73850edd04](https://github.com/MariaDB/server/commit/73850edd04)\
  2020-11-08 12:14:33 +0100
  * Re-fix compile error (conversion-null) Modified json.cpp
* [Revision #90405763cf](https://github.com/MariaDB/server/commit/90405763cf)\
  2020-11-07 23:58:57 +0100
  * Re-fix compile error (sign-unsign) Modified filamtxt.cpp
* [Revision #8985933881](https://github.com/MariaDB/server/commit/8985933881)\
  2020-11-07 23:22:28 +0100
  * Re-fix compile error (sign-unsign) Modified filamtxt.cpp
* [Revision #fb86a496c0](https://github.com/MariaDB/server/commit/fb86a496c0)\
  2020-11-07 22:36:50 +0100
  * Re-fix compile error (overloaded-virtual)
* [Revision #e4294729d4](https://github.com/MariaDB/server/commit/e4294729d4)\
  2020-11-07 19:50:29 +0100
  * Fix compile error (overloaded-virtual)
* [Revision #3ad6c0ef8a](https://github.com/MariaDB/server/commit/3ad6c0ef8a)\
  2020-11-07 16:33:01 +0100
  * Fix compile error. Modified ha\_connect.cc
* [Revision #46edfd6338](https://github.com/MariaDB/server/commit/46edfd6338)\
  2020-11-07 15:40:46 +0100
  * Getting text of json items now includes all array members
* [Revision #d3372258b0](https://github.com/MariaDB/server/commit/d3372258b0)\
  2020-11-06 15:34:13 +0100
  * Update tests to cope with changes
* [Revision #a4e999eec5](https://github.com/MariaDB/server/commit/a4e999eec5)\
  2020-11-05 23:04:37 +0100
  * Try to fix failing tests
* [Revision #addb28f62d](https://github.com/MariaDB/server/commit/addb28f62d)\
  2020-11-05 22:14:01 +0100
  * Try to fix failing tests
* [Revision #ecb00f3cd8](https://github.com/MariaDB/server/commit/ecb00f3cd8)\
  2020-11-05 19:13:26 +0100
  * Try to fix failing tests
* [Revision #a13642a82f](https://github.com/MariaDB/server/commit/a13642a82f)\
  2020-11-04 16:33:10 +0100
  * Try to fix that F..k gcc operator delete error
* [Revision #6a94ad98fb](https://github.com/MariaDB/server/commit/6a94ad98fb)\
  2020-11-04 15:46:02 +0100
  * Fix crash on Json date columns
* [Revision #49428c8fa6](https://github.com/MariaDB/server/commit/49428c8fa6)\
  2020-11-04 11:36:29 +0100
  * Fix compile error on LINUX (no suitable operator delete)
* [Revision #78ccc605a5](https://github.com/MariaDB/server/commit/78ccc605a5)\
  2020-11-03 23:19:22 +0100
  * Fix compile error on LINUX (LARGE\_INTEGER)
* [Revision #28af4212b6](https://github.com/MariaDB/server/commit/28af4212b6)\
  2020-11-03 18:40:28 +0100
  * Implementation of the Json BJSON representation. VAL structures replace VALUE classes in binary trees. These parsed binary trees are swapped and saved on file Swapping is to replace pointers by offsets to make it portable. In restoring, class pointers to functions are realloced on place. Making BJSON files is done by the new UDF function jfile\_bjson.
* [Revision #17867608a2](https://github.com/MariaDB/server/commit/17867608a2)\
  2021-01-29 11:18:06 +0100
  * ASAN heap-use-after-free in Item\_exists\_subselect::is\_top\_level\_item
* [Revision #33ede50f20](https://github.com/MariaDB/server/commit/33ede50f20)\
  2021-01-28 20:46:13 +0300
  * [MDEV-22251](https://jira.mariadb.org/browse/MDEV-22251): get\_key\_scans\_params: Conditional jump or move depends on uninitialised value
* [Revision #3a89ae3364](https://github.com/MariaDB/server/commit/3a89ae3364)\
  2021-01-28 11:22:54 +0100
  * last CC 3.1
* [Revision #20f6c403eb](https://github.com/MariaDB/server/commit/20f6c403eb)\
  2021-01-28 10:31:57 +0200
  * [MDEV-20717](https://jira.mariadb.org/browse/MDEV-20717) : Plugin system variables and activation options can break "mysqld --wsrep\_recover"
* [Revision #dd0b844a9c](https://github.com/MariaDB/server/commit/dd0b844a9c)\
  2021-01-27 17:11:49 +0200
  * [MDEV-24699](https://jira.mariadb.org/browse/MDEV-24699): Added wait condition to make sure table t2 is replicated to node\_1.
* [Revision #3edad54298](https://github.com/MariaDB/server/commit/3edad54298)\
  2021-01-25 19:01:06 -0800
  * [MDEV-24131](https://jira.mariadb.org/browse/MDEV-24131): unittest stacktrace-t fails to compile (OpenBSD)
* [Revision #75546dfbb1](https://github.com/MariaDB/server/commit/75546dfbb1)\
  2021-01-27 12:49:30 +0200
  * [MDEV-24704](https://jira.mariadb.org/browse/MDEV-24704) : Galera test failure on galera.galera\_nopk\_unicode
* [Revision #cbc75e9948](https://github.com/MariaDB/server/commit/cbc75e9948)\
  2021-01-21 11:34:05 +0530
  * [MDEV-20939](https://jira.mariadb.org/browse/MDEV-20939): Race condition between mysqldump import and InnoDB persistent statistics calculation
* [Revision #5fd3c7471e](https://github.com/MariaDB/server/commit/5fd3c7471e)\
  2021-01-27 16:43:29 +0200
  * [MDEV-24709](https://jira.mariadb.org/browse/MDEV-24709) Assertion !recv\_no\_ibuf\_operations failed in ibuf\_page\_low()
* [Revision #5b93a483e4](https://github.com/MariaDB/server/commit/5b93a483e4)\
  2021-01-27 15:11:38 +0200
  * [MDEV-24184](https://jira.mariadb.org/browse/MDEV-24184) preparation: InnoDB RENAME TABLE recovery failure
* [Revision #900a14754a](https://github.com/MariaDB/server/commit/900a14754a)\
  2021-01-26 14:21:33 +0200
  * Fix wsrep.variables
* [Revision #8cdeee177d](https://github.com/MariaDB/server/commit/8cdeee177d)\
  2021-01-20 09:38:20 +0200
  * [MDEV-24509](https://jira.mariadb.org/browse/MDEV-24509) : Warning: Memory not freed: 56 on SET @@global.wsrep\_sst\_auth
* [Revision #cc2d6d1bb2](https://github.com/MariaDB/server/commit/cc2d6d1bb2)\
  2021-01-25 18:12:34 +1100
  * [MDEV-20939](https://jira.mariadb.org/browse/MDEV-20939): Race condition between mysqldump import and InnoDB persistent
* [Revision #c58d2c941c](https://github.com/MariaDB/server/commit/c58d2c941c)\
  2021-01-22 16:03:07 +1100
  * [MDEV-20939](https://jira.mariadb.org/browse/MDEV-20939): Race condition between mysqldump import and InnoDB persistent statistics calculation
* [Revision #1a99958545](https://github.com/MariaDB/server/commit/1a99958545)\
  2021-01-22 13:43:06 +0100
  * mtr: --client-gdb=''
* [Revision #29bbcac0ee](https://github.com/MariaDB/server/commit/29bbcac0ee)\
  2021-01-20 18:22:38 +0100
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* [Revision #5d1db34585](https://github.com/MariaDB/server/commit/5d1db34585)\
  2021-01-20 15:22:26 +0100
  * cleanup: void hton::abort\_transaction()
* [Revision #6a1cb449fe](https://github.com/MariaDB/server/commit/6a1cb449fe)\
  2021-01-18 18:02:16 +0100
  * cleanup: remove slave background thread, use handle\_manager thread instead
* [Revision #990eb09333](https://github.com/MariaDB/server/commit/990eb09333)\
  2021-01-18 18:01:17 +0100
  * cleanup: fix and generalize handle\_manager thread
* [Revision #4a7e62296a](https://github.com/MariaDB/server/commit/4a7e62296a)\
  2021-01-18 11:22:48 +0100
  * don't allow `KILL QUERY ID USER xxx`
* [Revision #59e6d14c47](https://github.com/MariaDB/server/commit/59e6d14c47)\
  2020-11-05 13:37:35 +1100
  * [MDEV-24122](https://jira.mariadb.org/browse/MDEV-24122): on previously MySQL-5.7 datadirs, adjust mysql.user column order
* [Revision #0d9c9f49bd](https://github.com/MariaDB/server/commit/0d9c9f49bd)\
  2021-01-21 18:40:03 +0100
  * reenable rpl\_spec\_variables.test
* [Revision #7d52888149](https://github.com/MariaDB/server/commit/7d52888149)\
  2021-01-22 08:34:09 +0200
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659) : Update Galera disabled.def file
* [Revision #103200b380](https://github.com/MariaDB/server/commit/103200b380)\
  2021-01-22 16:41:40 +1100
  * [MDEV-24557](https://jira.mariadb.org/browse/MDEV-24557): Logical dump of MySQL users via MariaDB's mariadb-dump generates invalid commands
* [Revision #63db583158](https://github.com/MariaDB/server/commit/63db583158)\
  2021-01-22 16:31:18 +1100
  * man/mysqldump.1: typos INSERT INFO -> INTO
* [Revision #29d9897fe2](https://github.com/MariaDB/server/commit/29d9897fe2)\
  2016-06-22 15:52:07 +0200
  * [MDEV-10272](https://jira.mariadb.org/browse/MDEV-10272): add master host/port info to slave thread exit messages
* [Revision #eb75e8705d](https://github.com/MariaDB/server/commit/eb75e8705d)\
  2021-01-07 17:34:57 +0530
  * [MDEV-8134](https://jira.mariadb.org/browse/MDEV-8134): The relay-log is not flushed after the slave-relay-log.999999 showed
* [Revision #53acd1c1d8](https://github.com/MariaDB/server/commit/53acd1c1d8)\
  2021-01-21 16:20:57 +1100
  * maria: ma\_recovery cppcheck va\_start called twice
* [Revision #f2fea295b4](https://github.com/MariaDB/server/commit/f2fea295b4)\
  2021-01-21 16:46:59 +1100
  * ucs2: cppcheck - add va\_end
* [Revision #b22285e482](https://github.com/MariaDB/server/commit/b22285e482)\
  2021-01-19 08:02:37 -0800
  * [MDEV-16940](https://jira.mariadb.org/browse/MDEV-16940) Server crashes in unsafe\_key\_update upon attempt to update view through 2nd execution of SP
* [Revision #3caccc7bcd](https://github.com/MariaDB/server/commit/3caccc7bcd)\
  2021-01-19 14:36:36 +0200
  * Update InnoDB version number to 5.7.33
* [Revision #48ac7e1a42](https://github.com/MariaDB/server/commit/48ac7e1a42)\
  2021-01-19 11:53:22 +0200
  * [MDEV-24609](https://jira.mariadb.org/browse/MDEV-24609): innodb\_io\_capacity can exceed innodb\_io\_capacity\_max
* [Revision #959dfac4d0](https://github.com/MariaDB/server/commit/959dfac4d0)\
  2021-01-19 15:29:03 +0400
  * [MDEV-19723](https://jira.mariadb.org/browse/MDEV-19723) Assertion `je->state == JST_KEY' failed while SELECT ST_GEOMFROMGEOJSON() and Assertion` !mysql\_bin\_log.is\_open() || thd.is\_current\_stmt\_binlog\_format\_row()'
* [Revision #775aa6f08a](https://github.com/MariaDB/server/commit/775aa6f08a)\
  2021-01-19 14:25:51 +0300
  * [MDEV-24403](https://jira.mariadb.org/browse/MDEV-24403) Segfault on CREATE TABLE with explicit FTS\_DOC\_ID\_INDEX by multiple fields
* [Revision #82d39d4374](https://github.com/MariaDB/server/commit/82d39d4374)\
  2021-01-18 15:18:33 +0530
  * [MDEV-24491](https://jira.mariadb.org/browse/MDEV-24491) db\_name mismatch happens during virtual column computation
* [Revision #479b4214fa](https://github.com/MariaDB/server/commit/479b4214fa)\
  2021-01-11 15:23:09 +0530
  * [MDEV-24547](https://jira.mariadb.org/browse/MDEV-24547) Update fails when online alter does rollback due to MDL time out
* [Revision #94890a749a](https://github.com/MariaDB/server/commit/94890a749a)\
  2020-12-18 00:28:38 +0530
  * [MDEV-24179](https://jira.mariadb.org/browse/MDEV-24179): Assertion \`m\_status == DA\_ERROR || m\_status == DA\_OK || m\_status == DA\_OK\_BULK' failed in Diagnostics\_area::message()
* [Revision #beaea31ab1](https://github.com/MariaDB/server/commit/beaea31ab1)\
  2020-12-09 21:53:18 +0200
  * [MDEV-23851](https://jira.mariadb.org/browse/MDEV-23851) BF-BF Conflict issue because of UK GAP locks
* [Revision #cf6114ebea](https://github.com/MariaDB/server/commit/cf6114ebea)\
  2021-01-13 08:32:10 +0200
  * [MDEV-24432](https://jira.mariadb.org/browse/MDEV-24432) : galera.galera\_fk\_cascade\_delete\_debug MTR failed: query 'reap' failed: 1205: Lock wait timeout exceeded
* [Revision #9e3aa83f01](https://github.com/MariaDB/server/commit/9e3aa83f01)\
  2021-01-12 17:00:00 +0200
  * [MDEV-24443](https://jira.mariadb.org/browse/MDEV-24443) : galera.lp1376747-4 MTR fails: Result length mismatch
* [Revision #db9b54f163](https://github.com/MariaDB/server/commit/db9b54f163)\
  2021-01-14 18:06:41 +0100
  * [MDEV-12908](https://jira.mariadb.org/browse/MDEV-12908) binlog\_encryption.binlog\_xa\_recover, binlog.binlog\_xa\_recover failed in bb with extra checkpoint
* [Revision #c89f37983e](https://github.com/MariaDB/server/commit/c89f37983e)\
  2021-01-14 08:57:24 +0200
  * [MDEV-21478](https://jira.mariadb.org/browse/MDEV-21478) fixup: Avoid a memory leak
* [Revision #ea9cd97f85](https://github.com/MariaDB/server/commit/ea9cd97f85)\
  2021-01-13 18:55:56 +0200
  * [MDEV-24536](https://jira.mariadb.org/browse/MDEV-24536) innodb\_idle\_flush\_pct has no effect
* [Revision #25db70f912](https://github.com/MariaDB/server/commit/25db70f912)\
  2021-01-13 18:54:53 +0200
  * Fix innodb.innodb\_mysql
* [Revision #9e4a5a81fc](https://github.com/MariaDB/server/commit/9e4a5a81fc)\
  2021-01-13 16:16:13 +0700
  * [MDEV-24208](https://jira.mariadb.org/browse/MDEV-24208) SHOW RELAYLOG EVENTS command is not supported in the prepared statement protocol yet
* [Revision #ab271ee7e2](https://github.com/MariaDB/server/commit/ab271ee7e2)\
  2021-01-12 14:25:55 +0530
  * [MDEV-23826](https://jira.mariadb.org/browse/MDEV-23826): ORDER BY in view definition leads to wrong result with GROUP BY on query using view
* [Revision #3b94309a6c](https://github.com/MariaDB/server/commit/3b94309a6c)\
  2021-01-12 11:17:37 +0530
  * [MDEV-23753](https://jira.mariadb.org/browse/MDEV-23753): SIGSEGV in Column\_stat::store\_stat\_fields
* [Revision #a216672dab](https://github.com/MariaDB/server/commit/a216672dab)\
  2021-01-10 21:20:51 +0100
  * [MDEV-16341](https://jira.mariadb.org/browse/MDEV-16341) Wrong length for USER columns in performance\_schema tables
* [Revision #ad9a140d9b](https://github.com/MariaDB/server/commit/ad9a140d9b)\
  2021-01-10 20:35:27 +0100
  * [MDEV-14884](https://jira.mariadb.org/browse/MDEV-14884) Failed to enable encryption of temporary files in [mariadb 10.3.3](../../old-releases/10.3/10.3.3.md)
* [Revision #0d8bd7cc3a](https://github.com/MariaDB/server/commit/0d8bd7cc3a)\
  2021-01-10 00:57:02 +0100
  * [MDEV-18428](https://jira.mariadb.org/browse/MDEV-18428) Memory: If transactional=0 is specified in CREATE TABLE, it is not possible to ALTER TABLE
* [Revision #6f707430e5](https://github.com/MariaDB/server/commit/6f707430e5)\
  2021-01-09 18:48:16 +0100
  * cleanup: copy RAII helpers from 10.5, cleanup test
* [Revision #4568a72ce4](https://github.com/MariaDB/server/commit/4568a72ce4)\
  2021-01-10 01:31:38 +0100
  * don't do a warning for bad table options in replication slave thread
* [Revision #674be2fd82](https://github.com/MariaDB/server/commit/674be2fd82)\
  2021-01-09 18:52:33 +0100
  * [MDEV-18428](https://jira.mariadb.org/browse/MDEV-18428) Memory: If transactional=0 is specified in CREATE TABLE, it is not possible to ALTER TABLE
* [Revision #22b171d304](https://github.com/MariaDB/server/commit/22b171d304)\
  2021-01-09 17:56:33 +0100
  * [MDEV-17852](https://jira.mariadb.org/browse/MDEV-17852) Altered connection limits for user have no effect
* [Revision #fc0d9a470c](https://github.com/MariaDB/server/commit/fc0d9a470c)\
  2021-01-09 17:00:04 +0100
  * [MDEV-22966](https://jira.mariadb.org/browse/MDEV-22966) Server crashes or hangs with SET ROLE when started with skip-grant-tables
* [Revision #69f1adaa55](https://github.com/MariaDB/server/commit/69f1adaa55)\
  2021-01-09 16:56:35 +0100
  * main.skip\_grants cleanup
* [Revision #63f9192787](https://github.com/MariaDB/server/commit/63f9192787)\
  2021-01-07 19:37:47 +0100
  * [MDEV-17251](https://jira.mariadb.org/browse/MDEV-17251) SHOW STATUS unnecessary calls calc\_sum\_of\_all\_status
* [Revision #4c448836d4](https://github.com/MariaDB/server/commit/4c448836d4)\
  2021-01-05 18:10:04 +0100
  * [MDEV-12161](https://jira.mariadb.org/browse/MDEV-12161) Can't specify collation for virtual columns
* [Revision #9b750dcbd8](https://github.com/MariaDB/server/commit/9b750dcbd8)\
  2021-01-11 13:21:42 +0100
  * [MDEV-23536](https://jira.mariadb.org/browse/MDEV-23536) Race condition between KILL and transaction commit
* [Revision #66f4900b51](https://github.com/MariaDB/server/commit/66f4900b51)\
  2021-01-11 13:16:38 +0100
  * Revert "[MDEV-23536](https://jira.mariadb.org/browse/MDEV-23536) : Race condition between KILL and transaction commit"
* [Revision #fdc4b7a6b2](https://github.com/MariaDB/server/commit/fdc4b7a6b2)\
  2020-12-15 16:28:42 +0530
  * [MDEV-21478](https://jira.mariadb.org/browse/MDEV-21478) Inplace ALTER fails to report error when FTS\_DOC\_ID with wrong data type is added
* [Revision #3b548d3bbf](https://github.com/MariaDB/server/commit/3b548d3bbf)\
  2021-01-09 18:34:28 +0100
  * [MDEV-24554](https://jira.mariadb.org/browse/MDEV-24554) Do not use verisign server for authenticode timestamping
* [Revision #775fccea0c](https://github.com/MariaDB/server/commit/775fccea0c)\
  2020-12-17 14:20:23 +0200
  * [MDEV-23536](https://jira.mariadb.org/browse/MDEV-23536) : Race condition between KILL and transaction commit
* [Revision #18254c18d9](https://github.com/MariaDB/server/commit/18254c18d9)\
  2021-01-08 16:14:26 +0200
  * Cleanup: Remove unused symbol QUE\_THR\_PROCEDURE\_WAIT
* [Revision #61a362c949](https://github.com/MariaDB/server/commit/61a362c949)\
  2021-01-08 22:09:26 +1000
  * fixup [MDEV-17556](https://jira.mariadb.org/browse/MDEV-17556): fix mroonga
* [Revision #cd1e5d65c6](https://github.com/MariaDB/server/commit/cd1e5d65c6)\
  2021-01-08 08:10:18 +0200
  * [MDEV-19838](https://jira.mariadb.org/browse/MDEV-19838) fixup: clang -Wunused-const-variable
* [Revision #e25623e78a](https://github.com/MariaDB/server/commit/e25623e78a)\
  2020-12-29 13:38:16 +1000
  * [MDEV-17556](https://jira.mariadb.org/browse/MDEV-17556) Assertion \`bitmap\_is\_set\_all(\&table->s->all\_set)' failed
* [Revision #f319c4265f](https://github.com/MariaDB/server/commit/f319c4265f)\
  2021-01-06 19:55:55 +0200
  * [MDEV-19442](https://jira.mariadb.org/browse/MDEV-19442) add-on
* [Revision #51b7438d23](https://github.com/MariaDB/server/commit/51b7438d23)\
  2020-12-30 23:32:31 +0200
  * [MDEV-24482](https://jira.mariadb.org/browse/MDEV-24482): Added wait condition to make sure table t1 is replicated to node\_2.
* [Revision #06644f704a](https://github.com/MariaDB/server/commit/06644f704a)\
  2020-12-30 22:52:13 +0200
  * [MDEV-24465](https://jira.mariadb.org/browse/MDEV-24465): Added wait condition to make sure table t1 is replicated to node\_2.
* [Revision #1284e6c30d](https://github.com/MariaDB/server/commit/1284e6c30d)\
  2020-12-30 22:42:34 +0200
  * [MDEV-24464](https://jira.mariadb.org/browse/MDEV-24464): Added wait condition to make sure table t1 is replicated to node\_2.
* [Revision #9de9e0c781](https://github.com/MariaDB/server/commit/9de9e0c781)\
  2020-12-30 21:13:17 +0200
  * [MDEV-24447](https://jira.mariadb.org/browse/MDEV-24447): Added wait condition to make sure table t1 is replicated to node\_2.
* [Revision #cd529ae8ef](https://github.com/MariaDB/server/commit/cd529ae8ef)\
  2020-12-30 20:51:55 +0200
  * [MDEV-24462](https://jira.mariadb.org/browse/MDEV-24462): Added wait condition to make sure table t1 is replicated to node\_2.
* [Revision #608b0ee52e](https://github.com/MariaDB/server/commit/608b0ee52e)\
  2020-12-31 18:15:31 +0530
  * [MDEV-23033](https://jira.mariadb.org/browse/MDEV-23033): All slaves crash once in 24 hours and loop restart with signal 11
* [Revision #25db9ffa8b](https://github.com/MariaDB/server/commit/25db9ffa8b)\
  2021-01-04 14:57:15 +0530
  * [MDEV-23875](https://jira.mariadb.org/browse/MDEV-23875) is failing to build on windows.
* [Revision #4f5d5a7857](https://github.com/MariaDB/server/commit/4f5d5a7857)\
  2020-12-28 21:27:27 +0530
  * [MDEV-23875](https://jira.mariadb.org/browse/MDEV-23875): select into outfile not respect UMASK and UMASK\_DIR
* [Revision #78292047a4](https://github.com/MariaDB/server/commit/78292047a4)\
  2020-12-28 15:12:32 +0400
  * [MDEV-19442](https://jira.mariadb.org/browse/MDEV-19442) server\_audit plugin doesn't consider proxy users in server\_audit\_excl\_users/server\_audit\_incl\_users.
* [Revision #5b9ee8d819](https://github.com/MariaDB/server/commit/5b9ee8d819)\
  2020-12-28 12:06:22 +0200
  * [MDEV-24449](https://jira.mariadb.org/browse/MDEV-24449) Corruption of system tablespace or last recovered page
* [Revision #8e3e87d2fc](https://github.com/MariaDB/server/commit/8e3e87d2fc)\
  2020-12-08 18:02:42 +0200
  * [MDEV-23851](https://jira.mariadb.org/browse/MDEV-23851) [MDEV-24229](https://jira.mariadb.org/browse/MDEV-24229) BF-BF conflict issues
* [Revision #1e9af7996e](https://github.com/MariaDB/server/commit/1e9af7996e)\
  2020-12-24 22:15:40 +0100
  * Fix [MDEV-21958](https://jira.mariadb.org/browse/MDEV-21958) code to be working with not 64 MAX\_INDEXES
* [Revision #8d8370e31d](https://github.com/MariaDB/server/commit/8d8370e31d)\
  2020-12-22 19:22:41 +0300
  * Forgot to add this change to previous cset
* [Revision #df4f4bd84a](https://github.com/MariaDB/server/commit/df4f4bd84a)\
  2020-12-22 19:17:20 +0300
  * [MDEV-24444](https://jira.mariadb.org/browse/MDEV-24444): ASAN use-after-poison in Item\_func\_in::get\_func\_mm\_tree with NOT IN
* [Revision #dfe8ef8bd8](https://github.com/MariaDB/server/commit/dfe8ef8bd8)\
  2020-04-21 18:40:15 +0200
  * [MDEV-22630](https://jira.mariadb.org/browse/MDEV-22630) mysql\_upgrade ([MariaDB 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md).X --> [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md).X) does not fix auth\_string to change it to authentication\_string
* [Revision #6f40d5c8d6](https://github.com/MariaDB/server/commit/6f40d5c8d6)\
  2020-12-16 20:12:04 +0100
  * Item\_func\_like::walk() was ignoring escape\_item
* [Revision #59211ab7b9](https://github.com/MariaDB/server/commit/59211ab7b9)\
  2020-12-15 00:16:21 +0100
  * [MDEV-24346](https://jira.mariadb.org/browse/MDEV-24346) valgrind error in main.precedence
* [Revision #a587ded283](https://github.com/MariaDB/server/commit/a587ded283)\
  2020-12-14 18:25:08 +0100
  * [MDEV-24346](https://jira.mariadb.org/browse/MDEV-24346) valgrind error in main.precedence
* [Revision #5785de72ac](https://github.com/MariaDB/server/commit/5785de72ac)\
  2020-12-16 19:35:24 +0100
  * Item\_func\_like calls escape\_item->fix\_fields() twice
* [Revision #d1e9a4c15c](https://github.com/MariaDB/server/commit/d1e9a4c15c)\
  2020-12-19 09:41:14 +0200
  * [MDEV-23065](https://jira.mariadb.org/browse/MDEV-23065) : Crash after setting wsrep\_on to ON dynamically and reconnect
* [Revision #4e43e2f92d](https://github.com/MariaDB/server/commit/4e43e2f92d)\
  2020-12-03 15:30:35 +0100
  * [MDEV-22008](https://jira.mariadb.org/browse/MDEV-22008) rpl.rpl\_semi\_sync fails in bb, [MDEV-24418](https://jira.mariadb.org/browse/MDEV-24418) reenable binlog\_truncate\_innodb and binlog\_spurious\_ddl\_errors, rpl\_parallel\_retry fails in bb
* [Revision #83d2e0841e](https://github.com/MariaDB/server/commit/83d2e0841e)\
  2020-12-17 02:41:17 +1000
  * [MDEV-24041](https://jira.mariadb.org/browse/MDEV-24041) Generated column DELETE with FOREIGN KEY crash InnoDB
* [Revision #25d6f634b8](https://github.com/MariaDB/server/commit/25d6f634b8)\
  2020-12-17 10:09:16 -0800
  * [MDEV-20751](https://jira.mariadb.org/browse/MDEV-20751) Permission Issue With Nested CTEs
* [Revision #2cb5fb6019](https://github.com/MariaDB/server/commit/2cb5fb6019)\
  2020-12-02 17:28:49 +0200
  * [MDEV-24327](https://jira.mariadb.org/browse/MDEV-24327) wsrep XID checkpointing order with log\_slave\_updates=OFF
* [Revision #a244be7044](https://github.com/MariaDB/server/commit/a244be7044)\
  2020-12-16 09:11:11 -0800
  * [MDEV-23406](https://jira.mariadb.org/browse/MDEV-23406) Signal 8 in maria\_create after recursive cte query
* [Revision #719da2c4cc](https://github.com/MariaDB/server/commit/719da2c4cc)\
  2020-12-15 16:46:58 +0300
  * [MDEV-22810](https://jira.mariadb.org/browse/MDEV-22810) mariadb-backup does not honor open\_files\_limit from option during backup prepare
* [Revision #aebb111269](https://github.com/MariaDB/server/commit/aebb111269)\
  2020-12-16 10:26:29 +1100
  * [MDEV-21958](https://jira.mariadb.org/browse/MDEV-21958): postfix - result of range\_mrr\_icp
* [Revision #2c4761ccc1](https://github.com/MariaDB/server/commit/2c4761ccc1)\
  2020-11-09 19:21:07 +1100
  * [MDEV-24172](https://jira.mariadb.org/browse/MDEV-24172): innodb stats table last\_update is TIMESTAMP
* [Revision #dc62a67ed3](https://github.com/MariaDB/server/commit/dc62a67ed3)\
  2020-12-15 18:05:59 +0200
  * [MDEV-24414](https://jira.mariadb.org/browse/MDEV-24414) Update and enable galera.galera\_defaults
* [Revision #066212d16c](https://github.com/MariaDB/server/commit/066212d16c)\
  2020-12-15 14:38:30 +0300
  * [MDEV-21958](https://jira.mariadb.org/browse/MDEV-21958): Query having many NOT-IN clauses running forever
* [Revision #ac9c6f53a5](https://github.com/MariaDB/server/commit/ac9c6f53a5)\
  2020-10-27 11:49:17 +0100
  * [MDEV-24034](https://jira.mariadb.org/browse/MDEV-24034) Policy CMP0075 is not set during compile
* [Revision #74223c33d1](https://github.com/MariaDB/server/commit/74223c33d1)\
  2020-08-04 13:21:54 +0530
  * [MDEV-23209](https://jira.mariadb.org/browse/MDEV-23209): Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed in Diagnostics\_area::set\_ok\_status on INSERT
* [Revision #5f4d351d7f](https://github.com/MariaDB/server/commit/5f4d351d7f)\
  2020-09-17 19:05:08 +0530
  * [MDEV-22422](https://jira.mariadb.org/browse/MDEV-22422): Assertion \`! is\_set()' failed in Diagnostics\_area::set\_eof\_status
* [Revision #384f107ae5](https://github.com/MariaDB/server/commit/384f107ae5)\
  2020-12-14 15:06:42 +1100
  * [MDEV-21646](https://jira.mariadb.org/browse/MDEV-21646): postfix - my\_addr\_resolve: static Dl\_info info
* [Revision #4fa44c584c](https://github.com/MariaDB/server/commit/4fa44c584c)\
  2020-12-11 19:35:38 +0100
  * [MDEV-24331](https://jira.mariadb.org/browse/MDEV-24331) mysqldump fails with "Got error: 1356" if the database contains a view with a subquery
* [Revision #79fd338e6c](https://github.com/MariaDB/server/commit/79fd338e6c)\
  2020-12-10 09:19:03 +0100
  * [MDEV-23942](https://jira.mariadb.org/browse/MDEV-23942) mariadb-10.5.6/storage/connect/plugutil.cpp:380: bad width ?
* [Revision #493c7d34cb](https://github.com/MariaDB/server/commit/493c7d34cb)\
  2020-11-23 14:10:44 +0100
  * [MDEV-24194](https://jira.mariadb.org/browse/MDEV-24194) View definition corruption
* [Revision #f6e91552f0](https://github.com/MariaDB/server/commit/f6e91552f0)\
  2020-11-11 15:51:18 +0100
  * [MDEV-4677](https://jira.mariadb.org/browse/MDEV-4677) GROUP\_CONCAT not showing any output with group\_concat\_max\_len >= 4Gb
* [Revision #e189faf0b3](https://github.com/MariaDB/server/commit/e189faf0b3)\
  2020-11-11 13:23:39 +0100
  * document that a fulltext parser plugin can replace mysql\_add\_word callback
* [Revision #aeb561cf3e](https://github.com/MariaDB/server/commit/aeb561cf3e)\
  2020-11-11 12:30:17 +0100
  * tests for YEAR(N)
* [Revision #ba33d4753e](https://github.com/MariaDB/server/commit/ba33d4753e)\
  2020-11-11 12:19:20 +0100
  * cleanup: type\_year test formatting
* [Revision #589479b3ec](https://github.com/MariaDB/server/commit/589479b3ec)\
  2020-11-10 20:30:50 +0100
  * [MDEV-14836](https://jira.mariadb.org/browse/MDEV-14836) Assertion \`m\_status == DA\_ERROR' failed in Diagnostics\_area::sql\_errno upon query from I\_S with LIMIT ROWS EXAMINED
* [Revision #b31912fd35](https://github.com/MariaDB/server/commit/b31912fd35)\
  2020-11-03 23:38:31 +0100
  * [MDEV-24033](https://jira.mariadb.org/browse/MDEV-24033): SIGSEGV in memcmp\_avx2\_movbe from queue\_insert | SIGSEGV in memcmp\_avx2\_movbe from native\_compare
* [Revision #59bbe873d4](https://github.com/MariaDB/server/commit/59bbe873d4)\
  2020-11-03 19:07:16 +0100
  * Revert "[MDEV-24033](https://jira.mariadb.org/browse/MDEV-24033): SIGSEGV in memcmp\_avx2\_movbe from queue\_insert | SIGSEGV in memcmp\_avx2\_movbe from native\_compare"
* [Revision #f99abb45c5](https://github.com/MariaDB/server/commit/f99abb45c5)\
  2020-12-09 20:15:29 +0300
  * [MDEV-17573](https://jira.mariadb.org/browse/MDEV-17573) Assertion in federatedx on multi-update
* [Revision #a3f7f2334a](https://github.com/MariaDB/server/commit/a3f7f2334a)\
  2020-12-08 11:13:36 -0800
  * [MDEV-24019](https://jira.mariadb.org/browse/MDEV-24019) Assertion is hit for query using recursive CTE with no default DB
* [Revision #2db6eb1429](https://github.com/MariaDB/server/commit/2db6eb1429)\
  2020-12-04 14:20:52 -0800
  * [MDEV-22781](https://jira.mariadb.org/browse/MDEV-22781) CREATE VIEW containing WITH clause Signal 11
* [Revision #f924a3bd6c](https://github.com/MariaDB/server/commit/f924a3bd6c)\
  2020-12-01 15:40:44 +0100
  * [MDEV-24139](https://jira.mariadb.org/browse/MDEV-24139): CHECK\_CLAUSE field in INFORMATION\_SCHEMA.CHECK\_CONSTRAINTS truncate check constraints expressions
* [Revision #eb7b14ec9a](https://github.com/MariaDB/server/commit/eb7b14ec9a)\
  2020-03-05 16:40:29 +0100
  * [MDEV-21367](https://jira.mariadb.org/browse/MDEV-21367): mysqld\_safe log don't log to err.log
* [Revision #a82209ca31](https://github.com/MariaDB/server/commit/a82209ca31)\
  2020-11-23 21:33:03 +0100
  * [MDEV-24177](https://jira.mariadb.org/browse/MDEV-24177) && [MDEV-24178](https://jira.mariadb.org/browse/MDEV-24178)
* [Revision #50d7eddc3d](https://github.com/MariaDB/server/commit/50d7eddc3d)\
  2020-12-04 08:50:20 -0800
  * [MDEV-24314](https://jira.mariadb.org/browse/MDEV-24314) Unexpected error message when selecting from view that uses mergeable derived table
* [Revision #1eb59c307d](https://github.com/MariaDB/server/commit/1eb59c307d)\
  2020-12-04 11:46:47 +0200
  * [MDEV-24340](https://jira.mariadb.org/browse/MDEV-24340) Unique final message of InnoDB during shutdown
* [Revision #178d32f03b](https://github.com/MariaDB/server/commit/178d32f03b)\
  2020-12-01 14:13:05 +0400
  * [MDEV-24318](https://jira.mariadb.org/browse/MDEV-24318) server\_audit doesn't respect filters for PROXY\_CONNECT events.
* [Revision #e6b3e38d62](https://github.com/MariaDB/server/commit/e6b3e38d62)\
  2020-08-20 16:49:40 +0300
  * [MDEV-22929](https://jira.mariadb.org/browse/MDEV-22929) mariadb-backup option to report and/or continue when corruption is encountered
* [Revision #828471cbf8](https://github.com/MariaDB/server/commit/828471cbf8)\
  2020-11-30 15:29:32 +0200
  * MDEV 15532 Assertion \`!log->same\_pk' failed in row\_log\_table\_apply\_delete
* [Revision #37352c4b55](https://github.com/MariaDB/server/commit/37352c4b55)\
  2020-11-27 18:23:59 +0200
  * Disable mysqldump-system.test if auth socket plugin is not dynamic
* [Revision #1ccd1daaff](https://github.com/MariaDB/server/commit/1ccd1daaff)\
  2020-11-26 12:43:23 +0100
  * [MDEV-24289](https://jira.mariadb.org/browse/MDEV-24289): show grants missing with grant option
* [Revision #5991bd6215](https://github.com/MariaDB/server/commit/5991bd6215)\
  2020-11-25 16:01:38 +0300
  * [MDEV-24275](https://jira.mariadb.org/browse/MDEV-24275) InnoDB persistent stats analyze forces full scan forcing lock crash
* [Revision #10eaa43f86](https://github.com/MariaDB/server/commit/10eaa43f86)\
  2020-11-25 13:13:47 +0200
  * Skip main.lock\_view for cmake -DPLUGIN\_PERFSCHEMA=NO
* [Revision #1c9833c511](https://github.com/MariaDB/server/commit/1c9833c511)\
  2020-11-25 10:54:38 +0200
  * Cleanup: row\_log\_free()
* [Revision #fa6d710b85](https://github.com/MariaDB/server/commit/fa6d710b85)\
  2020-11-18 17:47:39 +0200
  * [MDEV-24097](https://jira.mariadb.org/browse/MDEV-24097) node restart overlaps with earlier still ongoing SST process
* [Revision #fe56e0e342](https://github.com/MariaDB/server/commit/fe56e0e342)\
  2020-11-19 12:33:43 +0200
  * [MDEV-22136](https://jira.mariadb.org/browse/MDEV-22136) : wsrep\_restart\_slave = 1 does not always work
* [Revision #1248c654c4](https://github.com/MariaDB/server/commit/1248c654c4)\
  2020-11-18 13:21:19 -0800
  * [MDEV-19179](https://jira.mariadb.org/browse/MDEV-19179) Regression: SELECT ... UNION ... with inconsistent column names fails
* [Revision #bbbab8215f](https://github.com/MariaDB/server/commit/bbbab8215f)\
  2020-11-09 08:26:08 +0000
  * [MDEV-24100](https://jira.mariadb.org/browse/MDEV-24100) Failed to read test report file: Invalid byte 2 of 3-byte UTF-8 sequence.
* [Revision #ce0cb6a4f6](https://github.com/MariaDB/server/commit/ce0cb6a4f6)\
  2020-11-17 15:07:37 +0200
  * [MDEV-24188](https://jira.mariadb.org/browse/MDEV-24188) fixup: Correct the FindBlockX predicate
* [Revision #6628435e94](https://github.com/MariaDB/server/commit/6628435e94)\
  2020-11-17 14:28:30 -0800
  * [MDEV-24220](https://jira.mariadb.org/browse/MDEV-24220) Server crash in base\_list\_iterator::next or in TABLE\_LIST::is\_recursive\_with\_tables
* [Revision #ceef26cf86](https://github.com/MariaDB/server/commit/ceef26cf86)\
  2020-11-17 15:49:36 +0300
  * MyRocks: Bare Windows compatibility: use rmdir built-in, not "rm -rf"
* [Revision #ab4f743610](https://github.com/MariaDB/server/commit/ab4f743610)\
  2020-11-17 08:52:47 +0200
  * [MDEV-24169](https://jira.mariadb.org/browse/MDEV-24169) : Galera test failure on galera\_rsu\_simple
* [Revision #bca683e895](https://github.com/MariaDB/server/commit/bca683e895)\
  2020-11-17 08:51:04 +0200
  * [MDEV-24166](https://jira.mariadb.org/browse/MDEV-24166) : Galera test failure on galera\_toi\_alter\_auto\_increment
* [Revision #0bde52e6a8](https://github.com/MariaDB/server/commit/0bde52e6a8)\
  2020-11-17 08:36:38 +0200
  * [MDEV-24164](https://jira.mariadb.org/browse/MDEV-24164) : Galera test failure on galera\_fk\_cascade\_delete
* [Revision #9b30212f15](https://github.com/MariaDB/server/commit/9b30212f15)\
  2020-11-13 18:15:04 +1100
  * [MDEV-24161](https://jira.mariadb.org/browse/MDEV-24161): shortcut OQGRAPH dependency checks if disabled
* [Revision #c8be6aafb9](https://github.com/MariaDB/server/commit/c8be6aafb9)\
  2020-11-14 09:55:09 +0100
  * Fix to make it compiling on new ubuntu.
* [Revision #bb328a2a27](https://github.com/MariaDB/server/commit/bb328a2a27)\
  2020-11-13 20:12:29 +0200
  * [MDEV-24188](https://jira.mariadb.org/browse/MDEV-24188) Hang in buf\_page\_create() after reusing a previously freed page
* [Revision #190e8a4c2a](https://github.com/MariaDB/server/commit/190e8a4c2a)\
  2020-11-10 16:02:30 -0800
  * [MDEV-23619](https://jira.mariadb.org/browse/MDEV-23619) MariaDB crash on WITH RECURSIVE UNION ALL (CTE) query
* [Revision #984a06db2c](https://github.com/MariaDB/server/commit/984a06db2c)\
  2020-11-12 13:04:39 +0530
  * [MDEV-4633](https://jira.mariadb.org/browse/MDEV-4633): multi\_source.simple test fails sporadically
* Merge [Revision #dd33a70dad](https://github.com/MariaDB/server/commit/dd33a70dad) 2020-11-11 18:31:42 +0200 - Merge mariadb-10.2.36 into 10.2
* [Revision #15550ed3a4](https://github.com/MariaDB/server/commit/15550ed3a4)\
  2020-11-11 10:17:22 -0500
  * bump the VERSION
* [Revision #d6ee28582a](https://github.com/MariaDB/server/commit/d6ee28582a)\
  2020-11-11 08:16:06 +0200
  * Cleanup: Remove dict\_space\_is\_empty(), dict\_space\_get\_id()
* [Revision #7b7e5922af](https://github.com/MariaDB/server/commit/7b7e5922af)\
  2020-11-10 13:49:01 +0200
  * [MDEV-24156](https://jira.mariadb.org/browse/MDEV-24156) trx\_undo\_left() fails to prevent overflow
* [Revision #bd528b0c93](https://github.com/MariaDB/server/commit/bd528b0c93)\
  2020-11-10 09:47:29 +0200
  * [MDEV-24182](https://jira.mariadb.org/browse/MDEV-24182) ibuf\_merge\_or\_delete\_for\_page() contains dead code
* [Revision #cd927dd345](https://github.com/MariaDB/server/commit/cd927dd345)\
  2020-11-09 11:58:49 +0100
  * [MDEV-23769](https://jira.mariadb.org/browse/MDEV-23769): MTR can abort before it prints the test result summary
* [Revision #5171ab808c](https://github.com/MariaDB/server/commit/5171ab808c)\
  2020-11-10 07:56:04 +0200
  * [MDEV-24171](https://jira.mariadb.org/browse/MDEV-24171) index\_online\_log is instrumented as rw-lock, not mutex
* [Revision #d01a034ac6](https://github.com/MariaDB/server/commit/d01a034ac6)\
  2020-11-09 15:50:37 +0200
  * [MDEV-7620](https://jira.mariadb.org/browse/MDEV-7620): Remove the data structures
* [Revision #c048053c8a](https://github.com/MariaDB/server/commit/c048053c8a)\
  2020-10-29 15:20:48 +0100
  * [MDEV-23103](https://jira.mariadb.org/browse/MDEV-23103) rpl.rpl\_gtid\_delete\_domain failed in buildbot
* [Revision #8ba641a676](https://github.com/MariaDB/server/commit/8ba641a676)\
  2020-11-03 10:56:50 -0500
  * bump the VERSION
* [Revision #97f3207cf3](https://github.com/MariaDB/server/commit/97f3207cf3)\
  2020-11-02 14:18:49 +0100
  * Fix MTR test galera.galera\_trigger
* [Revision #94859d985e](https://github.com/MariaDB/server/commit/94859d985e)\
  2020-11-03 08:49:10 +0200
  * Clean up wsrep.variables
* [Revision #3fe306c891](https://github.com/MariaDB/server/commit/3fe306c891)\
  2020-11-02 16:01:32 +0200
  * fixup a593e03d58f922a99ba49de1bec6810fc7e9874f: nullptr
* [Revision #8036d0a359](https://github.com/MariaDB/server/commit/8036d0a359)\
  2020-11-02 14:19:21 +0200
  * [MDEV-22387](https://jira.mariadb.org/browse/MDEV-22387): Do not violate attribute((nonnull))
* Merge [Revision #d2fab68667](https://github.com/MariaDB/server/commit/d2fab68667) 2020-11-02 14:17:15 +0200 - Merge bb-10.2-release into 10.2
* [Revision #ff0b6122a1](https://github.com/MariaDB/server/commit/ff0b6122a1)\
  2020-11-02 14:16:55 +0200
  * [MDEV-23630](https://jira.mariadb.org/browse/MDEV-23630) fixup: main.mysqldump result
* [Revision #a593e03d58](https://github.com/MariaDB/server/commit/a593e03d58)\
  2020-10-30 21:25:25 +0300
  * Add dbug\_print\_sel\_arg() debugging help function
* [Revision #d6ea03fa94](https://github.com/MariaDB/server/commit/d6ea03fa94)\
  2020-08-30 10:53:20 +1000
  * [MDEV-23630](https://jira.mariadb.org/browse/MDEV-23630): mysqldump logically dump system table information
* [Revision #c790218612](https://github.com/MariaDB/server/commit/c790218612)\
  2020-10-29 22:29:50 +0100
  * Fix RPM packaging on cmake 3.18+

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
