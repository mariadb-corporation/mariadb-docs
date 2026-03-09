# MariaDB 10.2.1 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.1)[Release Notes](../../old-releases/10.2/10.2.1.md)[Changelog](mariadb-1021-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 4 Jul 2016

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.1.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #b258f91](https://github.com/MariaDB/server/commit/b258f91)\
  2016-07-02 12:22:58 +0200
  * fix ALTER TABLE .. DROP CONSTRAINT IF NOT EXISTS
* [Revision #5c764a0](https://github.com/MariaDB/server/commit/5c764a0)\
  2016-07-02 14:52:20 +0200
  * clarify ER\_CANT\_DROP\_FIELD\_OR\_KEY
* [Revision #5e3a1ea](https://github.com/MariaDB/server/commit/5e3a1ea)\
  2016-07-02 04:04:22 +0300
  * Post-commit text fix for embedded: 12d75e6121 - new thread stack size
* [Revision #1d2fa98](https://github.com/MariaDB/server/commit/1d2fa98)\
  2016-07-02 03:26:32 +0300
  * Post-commit test fixes
* [Revision #06acd7a](https://github.com/MariaDB/server/commit/06acd7a)\
  2016-07-01 21:49:01 +0200
  * don't save vcol flags in frm
* [Revision #c3e0638](https://github.com/MariaDB/server/commit/c3e0638)\
  2016-07-01 21:47:40 +0200
  * cannot use item->const\_item() in open\_table\_from\_share()
* [Revision #12d75e6](https://github.com/MariaDB/server/commit/12d75e6)\
  2016-07-01 21:50:00 +0200
  * increase stack size for labrador
* [Revision #675d8a9](https://github.com/MariaDB/server/commit/675d8a9)\
  2016-07-01 21:45:57 +0400
  * Removing the "thd" argument from Item::create\_field\_for\_create\_select().
* [Revision #ffac854](https://github.com/MariaDB/server/commit/ffac854)\
  2016-07-01 16:44:17 +0200
  * [MDEV-8989](https://jira.mariadb.org/browse/MDEV-8989) ORDER BY optimizer ignores equality propagation
* [Revision #76f492e](https://github.com/MariaDB/server/commit/76f492e)\
  2016-06-30 23:56:18 -0400
  * Post-merge: Update test results
* [Revision #932646b](https://github.com/MariaDB/server/commit/932646b) 2016-06-30 16:38:05 +0200 - Merge branch '10.1' into 10.2
* [Revision #0bb30f3](https://github.com/MariaDB/server/commit/0bb30f3)\
  2016-06-30 07:51:10 +0200
  * refresh 32bit rdiffs
* [Revision #20dbfbb](https://github.com/MariaDB/server/commit/20dbfbb)\
  2016-06-29 20:18:04 +0200
  * vcols: store flags first
* [Revision #8f9530a](https://github.com/MariaDB/server/commit/8f9530a)\
  2016-06-29 18:55:14 +0200
  * revert second lookahead in the lexer
* [Revision #80de816](https://github.com/MariaDB/server/commit/80de816)\
  2016-06-29 17:59:42 +0200
  * test for ALTER TABLE ... SET DEFAULT
* [Revision #3687ede](https://github.com/MariaDB/server/commit/3687ede)\
  2016-06-29 14:59:33 +0200
  * clarify the order of evaluation for INSERT
* [Revision #f93a2a3](https://github.com/MariaDB/server/commit/f93a2a3)\
  2016-06-29 21:27:34 +0200
  * various cleanups
* [Revision #047d762](https://github.com/MariaDB/server/commit/047d762)\
  2016-06-29 10:02:02 +0200
  * move all new 10.2 error codes to start from 4000
* [Revision #5f22379](https://github.com/MariaDB/server/commit/5f22379)\
  2016-06-27 23:23:43 +0200
  * fix for CREATE ... ( ... DEFAULT const\_expr ... )
* [Revision #7039077](https://github.com/MariaDB/server/commit/7039077)\
  2016-06-29 21:18:32 +0200
  * change vcol->non\_deterministic to vcol->flags
* [Revision #0a056c9](https://github.com/MariaDB/server/commit/0a056c9)\
  2016-06-27 19:22:09 +0200
  * better ER\_VIRTUAL\_COLUMN\_FUNCTION\_IS\_NOT\_ALLOWED
* [Revision #1b4f096](https://github.com/MariaDB/server/commit/1b4f096)\
  2016-06-27 15:25:49 +0200
  * fix grammar for "DEFAULT (SELECT 1)" not be a syntax error
* [Revision #ed77ee1](https://github.com/MariaDB/server/commit/ed77ee1)\
  2016-06-26 22:42:48 +0200
  * cleanup: change Item::walk() to take void\* not uchar\*
* [Revision #e8bdb73](https://github.com/MariaDB/server/commit/e8bdb73)\
  2016-06-26 20:50:28 +0200
  * function DEFAULT(x) now works for expression defaults
* [Revision #3205da7](https://github.com/MariaDB/server/commit/3205da7)\
  2016-06-26 20:44:32 +0200
  * cleanup default.test
* [Revision #519e244](https://github.com/MariaDB/server/commit/519e244)\
  2016-06-26 16:34:37 +0200
  * tests for auto-generated constraint names
* [Revision #99e48cb](https://github.com/MariaDB/server/commit/99e48cb)\
  2016-06-26 15:46:36 +0200
  * restore ER\_VIEW\_CHECK\_FAILED to be different from ER\_CONSTRAINT\_FAILED
* [Revision #c87e002](https://github.com/MariaDB/server/commit/c87e002)\
  2016-06-26 13:37:27 +0200
  * str2decimal: don't return a negative zero
* [Revision #da372fb](https://github.com/MariaDB/server/commit/da372fb)\
  2016-06-25 23:02:32 +0200
  * ull2dec: exact calculation of the precision
* [Revision #4dcbb77](https://github.com/MariaDB/server/commit/4dcbb77)\
  2016-06-29 21:10:35 +0200
  * parentheses in default
* [Revision #b3e11d3](https://github.com/MariaDB/server/commit/b3e11d3)\
  2016-06-15 18:24:05 +0400
  * Adding a comment why we need column\_default\_non\_parenthesized\_expr (a new rule in sql\_yacc.yy)
* [Revision #fb67cde](https://github.com/MariaDB/server/commit/fb67cde)\
  2016-06-24 23:42:35 +0200
  * Use default character set for expressions
* [Revision #8f22612](https://github.com/MariaDB/server/commit/8f22612)\
  2016-06-10 14:09:05 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT ENCRYPT(), SHA(), SHA2(), AES\_ENCRYPT(), AES\_DECRYPT(), DES\_ENCRYPT(), DES\_DECRYPT()
* [Revision #ca8950c](https://github.com/MariaDB/server/commit/ca8950c)\
  2016-06-10 12:32:20 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT CRC32(), MD5(), FROM\_BASE64(), TO\_BASE64(), HEX(), UNHEX(), ENCODE(), DECODE(), PASSWORD(), COMPRESS(), UNCOMPRESS(), UNCOMPRESSED\_LENGTH().
* [Revision #f9cdc74](https://github.com/MariaDB/server/commit/f9cdc74)\
  2016-06-10 12:18:20 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT UUID(), UUID\_SHORT()
* [Revision #6c62611](https://github.com/MariaDB/server/commit/6c62611)\
  2016-06-10 12:10:17 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT Miscelaneous functions: BENCHMARK(), SLEEP(), ROW\_COUNT(), FOUND\_ROWS(), GET\_LOCK(), RELEASE\_LOCK(), IS\_USED\_LOCK(), IS\_FREE\_LOCK(), MASTER\_POS\_WAIT(), MASTER\_GTID\_WAIT(), BINLOG\_GTID\_POS(), ST\_GIS\_DEBUG(), DECODE\_HISTOGRAM(),
* [Revision #2654eab](https://github.com/MariaDB/server/commit/2654eab)\
  2016-06-10 11:34:31 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT Miscelaneous functions: LIKE\_RANGE\_MIN(), LIKE\_RANGE\_MAX(), WEIGHT\_STRING(), GET\_FORMAT(), FORMAT(), LOAD\_FILE().
* [Revision #111c0f1](https://github.com/MariaDB/server/commit/111c0f1)\
  2016-06-10 10:36:48 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT Metadata functions
* [Revision #a3e756c](https://github.com/MariaDB/server/commit/a3e756c)\
  2016-06-10 10:23:46 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT Dynamic column functions
* [Revision #b5870a5](https://github.com/MariaDB/server/commit/b5870a5)\
  2016-06-10 10:02:07 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT Functions DATABASE() and USER().
* [Revision #5ba196c](https://github.com/MariaDB/server/commit/5ba196c)\
  2016-06-10 09:05:03 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT INET4/INET6 functions
* [Revision #6cb4731](https://github.com/MariaDB/server/commit/6cb4731)\
  2016-06-10 09:39:50 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT - INT result functions - CAST variants: COLLATE, BINARY, CONVERT(..USING)
* [Revision #778a1a4](https://github.com/MariaDB/server/commit/778a1a4)\
  2016-06-09 16:42:49 +0400
  * More test for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT UDF
* [Revision #582ee39](https://github.com/MariaDB/server/commit/582ee39)\
  2016-06-09 16:29:06 +0400
  * More tests for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT Numeric functions with string input
* [Revision #f9fb646](https://github.com/MariaDB/server/commit/f9fb646)\
  2016-06-09 16:21:38 +0400
  * More tests for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT Boolean predicates
* [Revision #e779088](https://github.com/MariaDB/server/commit/e779088)\
  2016-06-09 15:59:49 +0400
  * More tests for [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT XML functions
* [Revision #11ff901](https://github.com/MariaDB/server/commit/11ff901)\
  2016-06-09 12:34:04 +0400
  * More tests for [MDEV-7563](https://jira.mariadb.org/browse/MDEV-7563) Support CHECK constraint Adding tests for cast, bit functions, string functions.
* [Revision #ba6646f](https://github.com/MariaDB/server/commit/ba6646f)\
  2016-06-09 15:45:50 +0400
  * More tests for [MDEV-7563](https://jira.mariadb.org/browse/MDEV-7563) Support CHECK constraint: GIS functions
* [Revision #3f32bf6](https://github.com/MariaDB/server/commit/3f32bf6)\
  2016-06-24 23:57:27 +0200
  * More tests for "[MDEV-7563](https://jira.mariadb.org/browse/MDEV-7563) Support CHECK constraint".
* [Revision #11debf6](https://github.com/MariaDB/server/commit/11debf6)\
  2016-06-24 23:57:12 +0200
  * Adding more tests for "[MDEV-7563](https://jira.mariadb.org/browse/MDEV-7563) Support CHECK constraint":
* [Revision #d99994a](https://github.com/MariaDB/server/commit/d99994a)\
  2016-06-08 10:34:37 +0300
  * Ensure we print the most importaint violating function
* [Revision #2fe8dd0](https://github.com/MariaDB/server/commit/2fe8dd0)\
  2016-06-25 20:55:43 +0200
  * various cleanups
* [Revision #db7edfe](https://github.com/MariaDB/server/commit/db7edfe)\
  2016-06-29 09:14:22 +0200
  * [MDEV-7563](https://jira.mariadb.org/browse/MDEV-7563) Support CHECK constraint as in (or close to) SQL Standard [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT
* [Revision #23d03a1](https://github.com/MariaDB/server/commit/23d03a1)\
  2016-06-27 15:41:51 +0200
  * parse negative numbers into one item
* [Revision #60916a8](https://github.com/MariaDB/server/commit/60916a8)\
  2016-05-28 01:15:39 +0300
  * Simplify THD::decide\_logging\_format() Fixed some test for future when DELETE will not trigger row based replication
* [Revision #6c17332](https://github.com/MariaDB/server/commit/6c17332)\
  2016-06-30 00:16:10 +0200
  * Part of [MDEV-10134](https://jira.mariadb.org/browse/MDEV-10134) Add full support for DEFAULT
* [Revision #3aadba1](https://github.com/MariaDB/server/commit/3aadba1)\
  2016-06-14 21:29:16 +0200
  * compilation warning
* [Revision #afbd28a](https://github.com/MariaDB/server/commit/afbd28a)\
  2016-06-29 18:25:51 +0400
  * Preparing the CAST(..AS \[UN]SIGNED) related code to fix a number of bugs easier ([MDEV-8919](https://jira.mariadb.org/browse/MDEV-8919), [MDEV-10304](https://jira.mariadb.org/browse/MDEV-10304), [MDEV-10305](https://jira.mariadb.org/browse/MDEV-10305), [MDEV-10307](https://jira.mariadb.org/browse/MDEV-10307))
* [Revision #8bec974](https://github.com/MariaDB/server/commit/8bec974)\
  2016-06-26 20:46:40 +0300
  * Follow-up #2 for [MDEV-6720](https://jira.mariadb.org/browse/MDEV-6720) (enable connection log in mysqltest by default)
* [Revision #4dc5075](https://github.com/MariaDB/server/commit/4dc5075)\
  2016-06-24 02:25:14 +0300
  * Fixed compiler warnings and test failures found by buildbot Fixed ccfilter to detect errors where the column is included in the error message
* [Revision #ec38c7e](https://github.com/MariaDB/server/commit/ec38c7e)\
  2016-06-19 15:07:03 +0300
  * [MDEV-10219](https://jira.mariadb.org/browse/MDEV-10219) rpl.rpl\_parallel\_temptable failed in buildbot: Assertion \`!table || !table->in\_use || table->in\_use == \_current\_thd()' failed
* [Revision #838205f](https://github.com/MariaDB/server/commit/838205f)\
  2016-06-19 15:06:10 +0300
  * Fixed compiler warnings and test failures found by buildbot
* [Revision #34eb10e](https://github.com/MariaDB/server/commit/34eb10e)\
  2016-06-18 14:28:34 +0300
  * [MDEV-10138](https://jira.mariadb.org/browse/MDEV-10138) Support for decimals up to 38 digits
* [Revision #e4062d4](https://github.com/MariaDB/server/commit/e4062d4)\
  2016-06-18 13:14:06 +0300
  * Fixed compiler warnings Added my\_global.h to PerconeFT to avoid "error \<my\_config.h> MUST be included first"
* [Revision #cc3190e](https://github.com/MariaDB/server/commit/cc3190e)\
  2016-06-19 20:30:03 +0300
  * Follow-up for [MDEV-6720](https://jira.mariadb.org/browse/MDEV-6720) (enable connection log in mysqltest by default)
* [Revision #5b008d4](https://github.com/MariaDB/server/commit/5b008d4) 2016-06-14 16:43:08 +0400 - Merge pull request #181 from ottok/ok-debpkg-10.2
* [Revision #effbe7d](https://github.com/MariaDB/server/commit/effbe7d)\
  2016-06-08 14:14:42 +0300
  * General spell fixing in comments and strings
* [Revision #9f9eb68](https://github.com/MariaDB/server/commit/9f9eb68)\
  2016-06-13 19:50:45 +0200
  * [MDEV-10098](https://jira.mariadb.org/browse/MDEV-10098) main.create\_delayed fails with ps-protocol: assertion \`global\_status\_var.global\_memory\_used >= 0' failed
* [Revision #e65703c](https://github.com/MariaDB/server/commit/e65703c)\
  2016-06-13 19:44:20 +0200
  * cleanup
* [Revision #b2ae32a](https://github.com/MariaDB/server/commit/b2ae32a)\
  2016-06-10 17:05:29 -0400
  * [MDEV-5535](https://jira.mariadb.org/browse/MDEV-5535): Cannot reopen temporary table
* [Revision #e2087c6](https://github.com/MariaDB/server/commit/e2087c6)\
  2016-06-10 16:58:08 -0400
  * [MDEV-5535](https://jira.mariadb.org/browse/MDEV-5535): Cannot reopen temporary table
* [Revision #7305be2](https://github.com/MariaDB/server/commit/7305be2)\
  2016-06-10 16:19:59 -0400
  * [MDEV-5535](https://jira.mariadb.org/browse/MDEV-5535): Cannot reopen temporary table
* [Revision #5475111](https://github.com/MariaDB/server/commit/5475111)\
  2016-06-10 14:54:24 -0400
  * [MDEV-5535](https://jira.mariadb.org/browse/MDEV-5535): Cannot reopen temporary table
* [Revision #78d4276](https://github.com/MariaDB/server/commit/78d4276)\
  2016-06-10 14:52:41 -0400
  * Some trivial changes.
* [Revision #7ecb304](https://github.com/MariaDB/server/commit/7ecb304)\
  2016-06-10 17:37:12 +0400
  * Code cleanups
* [Revision #2dee76f](https://github.com/MariaDB/server/commit/2dee76f)\
  2016-06-09 00:00:44 +0200
  * [MDEV-9518](https://jira.mariadb.org/browse/MDEV-9518) Increase the range for INFORMATION\_SCHEMA.MEMORY\_USED column
* [Revision #dc08c3b](https://github.com/MariaDB/server/commit/dc08c3b)\
  2016-06-08 17:36:16 +0200
  * [MDEV-10180](https://jira.mariadb.org/browse/MDEV-10180) main.events\_restart fails on valgrind builder: void THD::inc\_thread\_count(): Assertion \`!abort\_loop' failed.
* [Revision #9de6708](https://github.com/MariaDB/server/commit/9de6708)\
  2016-05-03 12:21:17 +0400
  * [MDEV-9857](https://jira.mariadb.org/browse/MDEV-9857) - CACHE\_LINE\_SIZE in innodb should be 128 on POWER
* [Revision #49ad084](https://github.com/MariaDB/server/commit/49ad084)\
  2016-04-01 11:31:53 +1100
  * Few improvements related to CPU cache line size and padding:
* [Revision #935033a](https://github.com/MariaDB/server/commit/935033a)\
  2016-06-05 11:24:10 +0200
  * fix wsrep test crashes on startup
* [Revision #4a0612e](https://github.com/MariaDB/server/commit/4a0612e)\
  2016-05-11 19:28:58 +0200
  * stop binlog background thread together with others
* [Revision #562c1df](https://github.com/MariaDB/server/commit/562c1df)\
  2016-05-14 13:22:47 +0200
  * cleanup: thread\_count
* [Revision #7425610](https://github.com/MariaDB/server/commit/7425610)\
  2016-05-09 18:30:22 +0200
  * decrement thead\_count _after_ THD is destroyed
* [Revision #74aef87](https://github.com/MariaDB/server/commit/74aef87)\
  2016-05-09 16:37:50 +0200
  * fix the method name
* [Revision #725ce0f](https://github.com/MariaDB/server/commit/725ce0f)\
  2016-05-08 22:16:44 +0200
  * THD:: cleanup() must be where it used to
* [Revision #69da361](https://github.com/MariaDB/server/commit/69da361)\
  2016-04-11 08:18:21 +0200
  * reset @@TIMESTAMP for COM\_CHANGE\_USER
* [Revision #4aacb20](https://github.com/MariaDB/server/commit/4aacb20)\
  2016-04-10 08:05:06 +0200
  * fix XID comparison
* [Revision #89685d5](https://github.com/MariaDB/server/commit/89685d5)\
  2016-04-07 19:51:40 +0300
  * Reuse THD for new user connections
* [Revision #54f3e18](https://github.com/MariaDB/server/commit/54f3e18) 2016-06-02 11:43:50 +0300 - Merge pull request #179 from grooverdan/10.2-remove\_btr\_search\_n\_succ\_AND\_hash\_fail
* [Revision #a0b11b9](https://github.com/MariaDB/server/commit/a0b11b9)\
  2016-06-02 17:03:31 +1000
  * Remove btr\_search\_n\_succ and btr\_search\_n\_hash\_fail counters
* [Revision #54332b2](https://github.com/MariaDB/server/commit/54332b2)\
  2016-06-02 10:00:00 +0400
  * Adding more tests for VIEWs with UNION.
* [Revision #3a7bc23](https://github.com/MariaDB/server/commit/3a7bc23)\
  2016-06-01 13:29:40 +0200
  * [MDEV-9154](https://jira.mariadb.org/browse/MDEV-9154) : Remove workarounds (mainly dynamic function loading) for running obsolete versions of Windows
* [Revision #22ede74](https://github.com/MariaDB/server/commit/22ede74)\
  2016-06-01 20:21:36 +0200
  * fix compile error - inconsistent use of 'struct' and 'class' for TDC\_element
* [Revision #23fed78](https://github.com/MariaDB/server/commit/23fed78)\
  2016-06-01 13:15:38 -0400
  * [MDEV-6368](https://jira.mariadb.org/browse/MDEV-6368): assertion xid\_seqno > trx\_sys\_cur\_xid\_seqno (postfix)
* [Revision #d6d4011](https://github.com/MariaDB/server/commit/d6d4011)\
  2016-06-01 17:54:23 +0400
  * Move wait\_for\_mdl\_deadlock\_detector() call to tc\_remove\_table()
* [Revision #41dc2fc](https://github.com/MariaDB/server/commit/41dc2fc)\
  2016-06-01 17:12:38 +0400
  * Move table cache private functions out of header
* [Revision #f7048e9](https://github.com/MariaDB/server/commit/f7048e9)\
  2016-05-12 16:29:17 +0400
  * Move common code to a separate function
* [Revision #2864164](https://github.com/MariaDB/server/commit/2864164)\
  2016-06-01 15:31:26 +0400
  * [MDEV-10101](https://jira.mariadb.org/browse/MDEV-10101) Wrong error message of SELECT 1 UNION (SELECT 1 FROM t1 GROUP BY 1 WITH ROLLUP)
* [Revision #caee832](https://github.com/MariaDB/server/commit/caee832)\
  2016-06-01 14:29:20 +0400
  * [MDEV-10124](https://jira.mariadb.org/browse/MDEV-10124) Incorrect usage of CUBE/ROLLUP and ORDER BY with GROUP\_CONCAT(a ORDER BY a)
* [Revision #de7eafc](https://github.com/MariaDB/server/commit/de7eafc)\
  2016-05-31 20:37:00 -0400
  * [MDEV-6368](https://jira.mariadb.org/browse/MDEV-6368): assertion xid\_seqno > trx\_sys\_cur\_xid\_seqno
* [Revision #eb86c32](https://github.com/MariaDB/server/commit/eb86c32)\
  2016-05-30 00:13:57 +0300
  * Increase the version number
* [Revision #7013f86](https://github.com/MariaDB/server/commit/7013f86)\
  2016-05-30 00:12:50 +0300
  * Follow-up for the previous commit - result change for a big test
* [Revision #7166069](https://github.com/MariaDB/server/commit/7166069)\
  2016-02-25 14:55:04 +0100
  * [MDEV-3944](https://jira.mariadb.org/browse/MDEV-3944): Allow derived tables in VIEWS
* [Revision #1f89ea8](https://github.com/MariaDB/server/commit/1f89ea8)\
  2016-05-25 18:36:51 +0400
  * sql\_yacc.yy: Removing union\_opt. Using /_empty_/, union\_list, union\_order\_or\_limit instead. This is to get rid of lex->current\_select->braces easier (separately in union\_list and in union\_order\_or\_limit)
* [Revision #971538f](https://github.com/MariaDB/server/commit/971538f)\
  2016-05-25 11:00:06 +0400
  * Adding various tests for combinations of UNION, ROLLUP, GROUP\_CONCAT, for better coverage.
* [Revision #2fc6e79](https://github.com/MariaDB/server/commit/2fc6e79)\
  2016-05-25 06:47:09 +0400
  * Recording test results forgotten in 9a25c01f7848324dd63c64ea4e1c86ef1cebfbc8 [MDEV-10102](https://jira.mariadb.org/browse/MDEV-10102) Disallow CREATE VIEW .. PROCEDURE ANALYSE() syntactically
* [Revision #804b00e](https://github.com/MariaDB/server/commit/804b00e)\
  2016-05-24 18:23:18 +0400
  * An sql\_yacc.yy clean-up - Moving opt\_union\_order\_or\_limit inside union\_opt, as it's not used in other places any more. - Changing union\_opt to have no type. Earlier (before all [MDEV-8909](https://jira.mariadb.org/browse/MDEV-8909) dependency tasks) it had the type, and it's return value was used to generate errors. Now union\_opt does not need a return value because the grammar disallows ORDER and LIMIT clauses in wrong context.
* [Revision #c80c3f6](https://github.com/MariaDB/server/commit/c80c3f6)\
  2016-05-24 18:05:38 +0400
  * [MDEV-10109](https://jira.mariadb.org/browse/MDEV-10109) Disallow syntactically INSERT .. SELECT .. {ORDER BY ..| LIMIT ..} .. UNION ..
* [Revision #ea9a393](https://github.com/MariaDB/server/commit/ea9a393)\
  2016-05-24 14:18:46 +0400
  * [MDEV-10103](https://jira.mariadb.org/browse/MDEV-10103) Disallow syntactically UNION SELECT .. PROCEDURE ANALYSE()
* [Revision #9a25c01](https://github.com/MariaDB/server/commit/9a25c01)\
  2016-05-23 16:25:51 +0400
  * [MDEV-10102](https://jira.mariadb.org/browse/MDEV-10102) Disallow CREATE VIEW .. PROCEDURE ANALYSE() syntactically
* [Revision #4c0e296](https://github.com/MariaDB/server/commit/4c0e296)\
  2016-05-23 10:54:09 +0400
  * [MDEV-10051](https://jira.mariadb.org/browse/MDEV-10051) Fix subselect to return a syntax error instead of "Incorrect usage of UNION and LIMIT"
* [Revision #a999acf](https://github.com/MariaDB/server/commit/a999acf)\
  2016-05-21 16:52:12 +0400
  * [MDEV-10095](https://jira.mariadb.org/browse/MDEV-10095) Fix derived tables to return a syntax error instead of "Illegal usage of UNION and LIMIT"
* [Revision #349da1d](https://github.com/MariaDB/server/commit/349da1d)\
  2016-05-21 00:27:57 +0400
  * sql\_yacc.yy: Removing unnecessary init\_nested\_join() and end\_nested\_join() from select\_derived\_init.
* [Revision #c44b2e6](https://github.com/MariaDB/server/commit/c44b2e6)\
  2016-05-20 20:05:03 +0400
  * A derived\_query\_specification clean-up (to simplify further [MDEV-8909](https://jira.mariadb.org/browse/MDEV-8909) changes)
* [Revision #485ece6](https://github.com/MariaDB/server/commit/485ece6)\
  2016-05-16 16:32:45 +0200
  * [MDEV-8429](https://jira.mariadb.org/browse/MDEV-8429): Change binlog\_checksum default to match MySQL 5.6.6+
* [Revision #f6a7c1c](https://github.com/MariaDB/server/commit/f6a7c1c)\
  2016-05-20 09:21:07 +0400
  * [MDEV-10080](https://jira.mariadb.org/browse/MDEV-10080) Derived tables allow double LIMIT clause
* [Revision #c9629da](https://github.com/MariaDB/server/commit/c9629da)\
  2016-05-19 18:57:23 +0400
  * This patch is a cleanup simplifying upcoming "[MDEV-8909](https://jira.mariadb.org/browse/MDEV-8909) union parser cleanup" changes.
* [Revision #50a17de](https://github.com/MariaDB/server/commit/50a17de)\
  2016-05-09 15:26:18 +0200
  * [MDEV-9947](https://jira.mariadb.org/browse/MDEV-9947): COM\_MULTI united response
* [Revision #e7ff281](https://github.com/MariaDB/server/commit/e7ff281)\
  2016-05-17 15:27:10 +0400
  * [MDEV-6353](https://jira.mariadb.org/browse/MDEV-6353) my\_ismbchar() and my\_mbcharlen() refactoring
* [Revision #7e66a24](https://github.com/MariaDB/server/commit/7e66a24)\
  2016-05-17 13:41:39 +0400
  * [MDEV-10079](https://jira.mariadb.org/browse/MDEV-10079) sql\_yacc.yy: Remove non-parenthesized SELECT from table\_ref
* [Revision #971d777](https://github.com/MariaDB/server/commit/971d777)\
  2016-05-17 11:18:59 +0400
  * sql\_yacc.yy: Adding a helper rule get\_select\_lex\_derived, to simplify further [MDEV-8909](https://jira.mariadb.org/browse/MDEV-8909) refactoring.
* [Revision #c322e3f](https://github.com/MariaDB/server/commit/c322e3f)\
  2016-05-17 09:58:45 +0400
  * [MDEV-10078](https://jira.mariadb.org/browse/MDEV-10078) sql\_yacc.yy: Remove non-parenthesized SELECT from table\_factor
* [Revision #a742f8e](https://github.com/MariaDB/server/commit/a742f8e) 2016-05-16 20:19:48 -0700 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #1f4f729](https://github.com/MariaDB/server/commit/1f4f729)\
  2016-05-16 14:50:21 +0400
  * sql\_yacc.yy cleanup, to simplify further changes for [MDEV-8909](https://jira.mariadb.org/browse/MDEV-8909). - Moving "SELECT\_SYM select\_init2\_derived opt\_table\_expression" from query\_term into a new separate rule query\_specification, and using query\_specification in the beginning of query\_term. - query\_term now does not have a %type, query\_specification has a %type instead. This removes duplicate code that returns Lex->current\_select->master\_unit()->first\_select();
* [Revision #4a8d377](https://github.com/MariaDB/server/commit/4a8d377)\
  2016-05-16 20:19:04 -0700
  * Fixed bug [MDEV-10058](https://jira.mariadb.org/browse/MDEV-10058).
* [Revision #b799449](https://github.com/MariaDB/server/commit/b799449)\
  2016-05-14 15:37:14 +0000
  * attempt to fix debian build (gssapi plugins require 10.1 client or server instead of 10.2
* [Revision #81b4c53](https://github.com/MariaDB/server/commit/81b4c53)\
  2016-05-13 16:26:07 +0400
  * sql\_yacc.yy: adding a new rule union\_head\_non\_top, to reuse some code between select\_derived\_union and query\_expression\_body. An upcoming patch for [MDEV-10035](https://jira.mariadb.org/browse/MDEV-10035) will also reuse union\_head\_non\_top.
* [Revision #ba50085](https://github.com/MariaDB/server/commit/ba50085)\
  2016-05-12 13:42:58 +0200
  * Fix of PSI & COM\_MULTI
* [Revision #53775a9](https://github.com/MariaDB/server/commit/53775a9)\
  2016-05-13 10:38:09 +0400
  * sql\_yacc.yy: - Moving select\_options\_and\_item\_list from select\_init2 to select\_init and view\_select\_aux - Renaming select\_init2 to select\_init3 This will simplify upcoming sql\_yacc.yy fixes (e.g. [MDEV-10035](https://jira.mariadb.org/browse/MDEV-10035), [MDEV-8909](https://jira.mariadb.org/browse/MDEV-8909)).
* [Revision #47a7c31](https://github.com/MariaDB/server/commit/47a7c31)\
  2016-05-10 16:18:03 +0400
  * close\_open\_tables() is not meaningful anymore
* [Revision #1c68b9e](https://github.com/MariaDB/server/commit/1c68b9e)\
  2016-05-10 14:23:30 +0400
  * [MDEV-505](https://jira.mariadb.org/browse/MDEV-505) - feature request: add \H option for mysql client prompt
* [Revision #eca0607](https://github.com/MariaDB/server/commit/eca0607)\
  2016-03-08 22:43:14 +0200
  * [MDEV-505](https://jira.mariadb.org/browse/MDEV-505): feature request: add \H option for mysql client prompt
* [Revision #f2afeb3](https://github.com/MariaDB/server/commit/f2afeb3)\
  2016-05-10 13:30:37 +0400
  * Renaming query\_specification to query\_term, to make the sql\_yacc.yy grammar closer the grammar in the SQL Standard: - is only a SELECT followed by , and . - While includes SELECT queries and derived tables.\
    Revision #6122673\
    2016-05-10 11:48:01 +0400\
    MDEV-10036 sql\_yacc.yy: Split select\_part2 to disallow syntactically bad constructs with INTO, PROCEDURE, UNION MDEV-10037 UNION with LIMIT ROWS EXAMINED does not require parentheses\
    Revision #c0a59b4\
    2016-05-06 11:42:48 +0400\
    MDEV-10030 sql\_yacc.yy: Split table\_expression and remove PROCEDURE from create\_select, select\_paren\_derived, select\_derived2, query\_specification\
    Revision #7905ea8\
    2016-05-05 11:20:37 +0400\
    MDEV-6720 - enable connection log in mysqltest by default\
    Revision #c788a13\
    2016-05-01 19:10:51 +0300\
    Drop old not used mysql.ndb\_binlog\_index if exists\
    Revision #5a7374d\
    2016-05-01 19:10:13 +0300\
    Fixed test cases that broke because we now print changing of connections - Don't log connection creation in galera\_connect.inc\
    Revision #4f1c81d\
    2016-04-29 18:39:18 +0200\
    after-merge: simplify, fix a bug\
    Revision #aed1485\
    2016-04-29 09:22:24 +1000\
    MDEV-9758: correct test case\
    Revision #84b0ac6\
    2016-04-29 09:19:34 +1000\
    Whitespace fix for mysql\_checksum\_table function\
    Revision #1ba90ce\
    2016-03-21 08:58:39 +1100\
    MDEV-9758: correct checksum on non-continious blocks\
    Revision #51a6629\
    2016-03-18 11:50:41 +1100\
    CHECKSUM TABLE to calculate in multiple column chunks\
    Revision #8b94aec\
    2016-04-27 21:50:54 +0200\
    Fix connect2 test, simulated errors do not work with thread cache\
    Revision #6345cd4\
    2016-04-28 21:22:09 +0200\
    Fix compile errors\
    Revision #636bb59\
    2016-04-28 17:15:38 +0300\
    Final fixes for Memory\_used - Change some static variables to dynamic to ensure that we don't do any memory allocations before server starts or stops - Print more memory information on SIGHUP. Fixed output. - Write out if memory was lost if run with --debug-at-exit - Fixed wrong #ifdef in sql\_cache.cc\
    Revision #32d3d9f\
    2016-04-28 16:59:53 +0300\
    Fixed compiler warning\
    Revision #9c84637 2016-04-28 16:59:33 +0300 - Merge commit 'd5822a3ad0657040114cdc185c6387b9eb3a12b2' into 10.2\
    Revision #fabeab7\
    2016-04-28 11:28:02 +0300\
    Cleanups - Avoid some realloc() during startup - Ensure that file\_key\_management\_plugin frees it's memory early, even if it's linked statically. - Fixed compiler warnings from unused variables and missing destructors - Fixed wrong indentation\
    Revision #dafed5b\
    2016-04-26 09:34:38 -0700\
    Removed some dead code that appeared in the merge for MDEV-8646.\
    Revision #7db337e 2016-04-20 10:56:59 -0700 - Merge branch '10.2' of github.com:MariaDB/server into 10.2\
    Revision #308cee5\
    2016-04-19 15:37:05 -0700\
    Fixed bug MDEV-9931.\
    Revision #3b6a64c\
    2016-04-20 10:55:53 -0700\
    Fixed bug MDEV-9937.\
    Revision #4b8e54b\
    2016-04-17 13:25:05 -0700\
    MDEV-7885, MDEV-8857: Add testcases

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
