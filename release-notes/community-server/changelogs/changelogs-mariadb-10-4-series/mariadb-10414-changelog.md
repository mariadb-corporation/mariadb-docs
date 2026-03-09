# MariaDB 10.4.14 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.14/)[Release Notes](../../old-releases/10.4/10.4.14.md)[Changelog](mariadb-10414-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 10 Aug 2020

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.14.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.24](../changelogs-mariadb-10-3-series/mariadb-10324-changelog.md)
* Merge [Revision #ddffcad64c](https://github.com/MariaDB/server/commit/ddffcad64c) 2020-08-06 17:13:02 +0200 - Merge branch '10.3' into 10.4
* [Revision #4ed4cf0238](https://github.com/MariaDB/server/commit/4ed4cf0238)\
  2020-08-04 10:50:06 +0200
  * [MDEV-23358](https://jira.mariadb.org/browse/MDEV-23358) main.upgrade\_[MDEV-19650](https://jira.mariadb.org/browse/MDEV-19650) fails with result difference
* [Revision #8d462523fb](https://github.com/MariaDB/server/commit/8d462523fb)\
  2020-08-04 22:16:45 +0300
  * List of unstable tests for 10.4.14 release
* [Revision #9a156e1a23](https://github.com/MariaDB/server/commit/9a156e1a23)\
  2020-08-04 11:49:52 +0300
  * [MDEV-23345](https://jira.mariadb.org/browse/MDEV-23345) Assertion `not_redundant() == old.not_redundant()`
* Merge [Revision #57325e4706](https://github.com/MariaDB/server/commit/57325e4706) 2020-08-03 14:44:06 +0200 - Merge branch '10.3' into 10.4
* [Revision #706a7101bf](https://github.com/MariaDB/server/commit/706a7101bf)\
  2020-07-16 14:24:30 +0530
  * [MDEV-23089](https://jira.mariadb.org/browse/MDEV-23089) rpl\_parallel2 fails in 10.5
* [Revision #9840bb21ef](https://github.com/MariaDB/server/commit/9840bb21ef)\
  2020-08-03 10:53:06 +0400
  * [MDEV-23366](https://jira.mariadb.org/browse/MDEV-23366) ROUND(18446744073709551615,rand()\*0) returns a wrong result
* [Revision #97f7bfcebc](https://github.com/MariaDB/server/commit/97f7bfcebc)\
  2020-07-28 13:43:25 +0530
  * [MDEV-21017](https://jira.mariadb.org/browse/MDEV-21017): Assertion \`\`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())'`failed or late`ER\_PERIOD\_FIELD\_WRONG\_ATTRIBUTES\` upon attempt to create existing table
* [Revision #00f964ab4d](https://github.com/MariaDB/server/commit/00f964ab4d)\
  2020-08-03 08:01:42 +0400
  * [MDEV-23367](https://jira.mariadb.org/browse/MDEV-23367) ROUND(18446744073709551615,-1) returns a wrong result
* [Revision #3b87a68169](https://github.com/MariaDB/server/commit/3b87a68169)\
  2020-08-02 22:48:53 +0400
  * [MDEV-23368](https://jira.mariadb.org/browse/MDEV-23368) ROUND(18446744073709551615,-11) returns a wrong result
* [Revision #863d5b4f75](https://github.com/MariaDB/server/commit/863d5b4f75)\
  2020-08-02 18:58:01 +0400
  * [MDEV-23350](https://jira.mariadb.org/browse/MDEV-23350) ROUND(bigint\_22\_or\_longer) returns a wrong data type
* Merge [Revision #da78e952fb](https://github.com/MariaDB/server/commit/da78e952fb) 2020-08-01 10:42:19 +0300 - Merge 10.3 into 10.4
* Merge [Revision #4db4b77365](https://github.com/MariaDB/server/commit/4db4b77365) 2020-07-31 18:10:03 +0300 - Merge 10.3 into 10.4
* Merge [Revision #70d4500c00](https://github.com/MariaDB/server/commit/70d4500c00) 2020-07-31 18:09:32 +0300 - Merge 10.3 into 10.4
* Merge [Revision #9216114ce7](https://github.com/MariaDB/server/commit/9216114ce7) 2020-07-31 18:09:08 +0300 - Merge 10.3 into 10.4
* [Revision #dc513dff91](https://github.com/MariaDB/server/commit/dc513dff91)\
  2020-07-31 10:42:44 +0400
  * [MDEV-23351](https://jira.mariadb.org/browse/MDEV-23351) Rounding functions return wrong data types for DATE input
* [Revision #a773d93267](https://github.com/MariaDB/server/commit/a773d93267)\
  2020-07-31 11:10:41 +0200
  * [MDEV-19603](https://jira.mariadb.org/browse/MDEV-19603) [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) does not build on OpenBSD due to the use of libdl
* [Revision #153cd6a27f](https://github.com/MariaDB/server/commit/153cd6a27f)\
  2020-07-23 18:57:40 +0200
  * [MDEV-23237](https://jira.mariadb.org/browse/MDEV-23237) mariadb.sys has too many privileges
* [Revision #78f09b12d3](https://github.com/MariaDB/server/commit/78f09b12d3)\
  2020-07-23 16:17:59 +0200
  * [MDEV-23009](https://jira.mariadb.org/browse/MDEV-23009) SIGSEGV in get\_field from acl\_load (on optimized builds)
* [Revision #a874b6c445](https://github.com/MariaDB/server/commit/a874b6c445)\
  2020-07-30 14:30:21 +0400
  * [MDEV-23337](https://jira.mariadb.org/browse/MDEV-23337) Rounding functions create a wrong data type for integer input
* [Revision #c3958ae407](https://github.com/MariaDB/server/commit/c3958ae407)\
  2020-07-29 12:43:38 +0300
  * Enable test for testing.
* [Revision #6d3186e326](https://github.com/MariaDB/server/commit/6d3186e326)\
  2020-07-29 22:29:43 +0400
  * [MDEV-23323](https://jira.mariadb.org/browse/MDEV-23323) Rounding functions return a wrong data type for a BIT, ENUM, SET argument
* [Revision #92499ae95c](https://github.com/MariaDB/server/commit/92499ae95c)\
  2020-07-29 10:22:17 +0400
  * [MDEV-23320](https://jira.mariadb.org/browse/MDEV-23320) Hex hybrid constants 0xHHHH work badly in rounding functions
* [Revision #423de1e574](https://github.com/MariaDB/server/commit/423de1e574)\
  2020-07-28 09:37:45 +0300
  * [MDEV-23245](https://jira.mariadb.org/browse/MDEV-23245) [MDEV-22898](https://jira.mariadb.org/browse/MDEV-22898) Still getting assertion failure in file data0type.cc line 67
* [Revision #5b3b53ce36](https://github.com/MariaDB/server/commit/5b3b53ce36)\
  2020-07-28 17:32:19 +0400
  * [MDEV-23311](https://jira.mariadb.org/browse/MDEV-23311) CEILING() and FLOOR() convert temporal input to numbers, unlike ROUND() and TRUNCATE()
* [Revision #69cf6302f3](https://github.com/MariaDB/server/commit/69cf6302f3)\
  2020-07-28 14:22:45 +0300
  * galera\_var\_notify\_cmd still hangs.
* [Revision #e08f87d527](https://github.com/MariaDB/server/commit/e08f87d527)\
  2020-07-27 13:00:53 +0200
  * fix obvious bugs hidden by current\_select assigned to builtin select
* [Revision #c6eb21cd87](https://github.com/MariaDB/server/commit/c6eb21cd87)\
  2020-07-24 09:59:38 +0200
  * [MDEV-21998](https://jira.mariadb.org/browse/MDEV-21998): Server crashes in `st_select_lex::add_table_to_list` upon mix of KILL and sequences
* [Revision #fd9ca2a742](https://github.com/MariaDB/server/commit/fd9ca2a742)\
  2020-07-27 15:04:04 +0300
  * [MDEV-23295](https://jira.mariadb.org/browse/MDEV-23295) ROW\_FORMAT mismatch in instant ALTER TABLE
* [Revision #4968fdbcef](https://github.com/MariaDB/server/commit/4968fdbcef)\
  2020-07-26 18:01:12 +0400
  * [MDEV-19918](https://jira.mariadb.org/browse/MDEV-19918) Server hangs or crashes while trying to lock mutex when the mutex was already locked upon startup with server\_audit and orphan records in mysql.plugin.
* [Revision #05d62518fb](https://github.com/MariaDB/server/commit/05d62518fb)\
  2020-07-24 19:34:17 +0300
  * [MDEV-22651](https://jira.mariadb.org/browse/MDEV-22651): Bogus assertion in `dict_table_t::init_instant()`
* [Revision #3d76af0814](https://github.com/MariaDB/server/commit/3d76af0814)\
  2020-07-24 15:17:59 +0300
  * [MDEV-22998](https://jira.mariadb.org/browse/MDEV-22998) Free thd->mem\_root at applier commit or rollback.
* [Revision #468e56bfde](https://github.com/MariaDB/server/commit/468e56bfde)\
  2020-07-24 19:25:32 +0300
  * Add missing includes.
* [Revision #bec81db1c2](https://github.com/MariaDB/server/commit/bec81db1c2)\
  2020-07-24 15:17:35 +0300
  * Update Galera global warning ignore list.
* [Revision #1e2a4ed7ed](https://github.com/MariaDB/server/commit/1e2a4ed7ed)\
  2020-07-23 23:05:47 +0300
  * [MDEV-21718](https://jira.mariadb.org/browse/MDEV-21718) Assertion in `wsrep::client_state::before_command()`
* [Revision #134a6a8d2f](https://github.com/MariaDB/server/commit/134a6a8d2f)\
  2020-07-24 11:56:01 +0300
  * Silence unnecessary warning.
* [Revision #8f3423fb5a](https://github.com/MariaDB/server/commit/8f3423fb5a)\
  2020-07-13 23:02:05 +0300
  * Update wsrep-lib version: improved error logging and diagnostics
* [Revision #95132ade6d](https://github.com/MariaDB/server/commit/95132ade6d)\
  2020-06-23 10:23:40 +0300
  * [MDEV-20928](https://jira.mariadb.org/browse/MDEV-20928) mtr test galera.galera\_var\_innodb\_disallow\_writes test failure
* [Revision #4b4372af6a](https://github.com/MariaDB/server/commit/4b4372af6a)\
  2020-06-02 09:18:59 +0200
  * [MDEV-22458](https://jira.mariadb.org/browse/MDEV-22458): Server with WSREP hangs after INSERT, wrong usage of mutex 'LOCK\_thd\_data' and 'share->intern\_lock' / 'lock->mutex'
* [Revision #6b8b7b1e8c](https://github.com/MariaDB/server/commit/6b8b7b1e8c)\
  2020-06-24 21:56:55 +0200
  * [MDEV-21905](https://jira.mariadb.org/browse/MDEV-21905): Galera test galera\_var\_notify\_cmd causes hang
* [Revision #f843e215f3](https://github.com/MariaDB/server/commit/f843e215f3)\
  2020-07-05 15:21:43 +0300
  * aarch64: use compiler flag outline-atomics if available
* [Revision #c76b45a524](https://github.com/MariaDB/server/commit/c76b45a524)\
  2020-07-06 13:43:30 +0300
  * [MDEV-23249](https://jira.mariadb.org/browse/MDEV-23249): Support aarch64 architecture timer
* [Revision #5f2628d1ee](https://github.com/MariaDB/server/commit/5f2628d1ee)\
  2020-07-22 16:17:53 +0300
  * [MDEV-22778](https://jira.mariadb.org/browse/MDEV-22778) Slow InnoDB shutdown on large instance
* [Revision #ddb8309e8c](https://github.com/MariaDB/server/commit/ddb8309e8c)\
  2020-07-21 10:31:10 +0200
  * [MDEV-21997](https://jira.mariadb.org/browse/MDEV-21997) Server crashes in `LEX::create_item_ident_sp` upon use of unknown identifier
* [Revision #1ca52b969a](https://github.com/MariaDB/server/commit/1ca52b969a)\
  2020-07-22 14:40:56 +0530
  * [MDEV-23254](https://jira.mariadb.org/browse/MDEV-23254) Replace `FSP_FLAGS_HAS_PAGE_COMPRESSION` with `fil_space_t::is_compressed`
* [Revision #8c7f7bae47](https://github.com/MariaDB/server/commit/8c7f7bae47)\
  2020-07-22 08:48:14 +0300
  * Fix regex on test.
* Merge [Revision #b1538f4d60](https://github.com/MariaDB/server/commit/b1538f4d60) 2020-07-21 16:36:47 +0300 - Merge 10.3 into 10.4
* [Revision #fc48c8ff4c](https://github.com/MariaDB/server/commit/fc48c8ff4c)\
  2020-07-20 15:19:25 +0300
  * [MDEV-21953](https://jira.mariadb.org/browse/MDEV-21953) deadlock between BACKUP STAGE BLOCK\_COMMIT and parallel repl.
* [Revision #c4d5b6b157](https://github.com/MariaDB/server/commit/c4d5b6b157)\
  2020-07-20 13:10:22 +0300
  * [MDEV-22899](https://jira.mariadb.org/browse/MDEV-22899) Assertion \`\`field->col->is\_binary() || field->prefix\_len % field->col->mbmaxlen == 0'`failed in`dict\_index\_add\_to\_cache\`
* Merge [Revision #4b959bd8df](https://github.com/MariaDB/server/commit/4b959bd8df) 2020-07-20 15:34:59 +0300 - Merge 10.3 into 10.4
* [Revision #0a7faed75a](https://github.com/MariaDB/server/commit/0a7faed75a)\
  2020-07-20 14:15:56 +0300
  * [MDEV-22771](https://jira.mariadb.org/browse/MDEV-22771) Instant extension of CHAR column is wrongly allowed
* Merge [Revision #956f21c3b0](https://github.com/MariaDB/server/commit/956f21c3b0) 2020-07-16 13:03:29 +0200 - Merge remote-tracking branch 'origin/bb-10.4-[MDEV-21910](https://jira.mariadb.org/browse/MDEV-21910)' into 10.4
* [Revision #6a1713ac17](https://github.com/MariaDB/server/commit/6a1713ac17)\
  2020-06-26 21:40:13 +0300
  * Fix perfschema.nesting test case after fix.
* [Revision #5a7794d3a8](https://github.com/MariaDB/server/commit/5a7794d3a8)\
  2020-05-19 11:12:26 +0300
  * [MDEV-21910](https://jira.mariadb.org/browse/MDEV-21910) Deadlock between BF abort and manual KILL command
* Merge [Revision #3280edda89](https://github.com/MariaDB/server/commit/3280edda89) 2020-07-16 06:57:50 +0300 - Merge 10.3 into 10.4
* [Revision #ced3ec4c9c](https://github.com/MariaDB/server/commit/ced3ec4c9c)\
  2020-07-15 10:26:31 +0300
  * Revert [MDEV-20453](https://jira.mariadb.org/browse/MDEV-20453) (string\_view)
* Merge [Revision #9936cfd531](https://github.com/MariaDB/server/commit/9936cfd531) 2020-07-15 10:17:15 +0300 - Merge 10.3 into 10.4
* [Revision #a7634281aa](https://github.com/MariaDB/server/commit/a7634281aa)\
  2020-07-14 21:11:15 +0300
  * fix header includes
* [Revision #d87006a1c1](https://github.com/MariaDB/server/commit/d87006a1c1)\
  2020-07-14 15:10:54 +0300
  * [MDEV-20453](https://jira.mariadb.org/browse/MDEV-20453) add class similar to `std::string_view` (non owning string reference)
* [Revision #e3a6916895](https://github.com/MariaDB/server/commit/e3a6916895)\
  2020-07-14 13:15:57 +0300
  * remove dead code: fil\_create\_directory\_for\_tablename()
* Merge [Revision #df1846aeea](https://github.com/MariaDB/server/commit/df1846aeea) 2020-07-14 09:36:38 +0200 - Merge branch '10.4-[MDEV-18838](https://jira.mariadb.org/browse/MDEV-18838)' of [mariadb-server](https://github.com/codership/mariadb-server) into 10.4-[MDEV-22966](https://jira.mariadb.org/browse/MDEV-22966)
* [Revision #7b8319f3f1](https://github.com/MariaDB/server/commit/7b8319f3f1)\
  2020-07-01 16:58:59 +0300
  * [MDEV-22966](https://jira.mariadb.org/browse/MDEV-22966)- Hang on galera\_toi\_truncate test case
* [Revision #de20872331](https://github.com/MariaDB/server/commit/de20872331)\
  2020-07-13 16:44:46 +0300
  * [MDEV-22988](https://jira.mariadb.org/browse/MDEV-22988) Corrupted table after DROP INDEX
* [Revision #5d471453ed](https://github.com/MariaDB/server/commit/5d471453ed)\
  2020-07-11 12:54:30 +0300
  * noexcept ilist
* [Revision #873eb4a397](https://github.com/MariaDB/server/commit/873eb4a397)\
  2020-07-10 22:48:35 +0400
  * [MDEV-21385](https://jira.mariadb.org/browse/MDEV-21385) PAM v2 plugin produces lots of zombie processes.
* [Revision #41221091f6](https://github.com/MariaDB/server/commit/41221091f6)\
  2020-07-08 23:25:08 +0300
  * [MDEV-22553](https://jira.mariadb.org/browse/MDEV-22553): Assertion \`\`info->lastpos == (\~ (my\_off\_t) 0)'`failed in`mi\_rkey\`
* [Revision #0d6d801e58](https://github.com/MariaDB/server/commit/0d6d801e58)\
  2020-07-08 13:10:07 +0200
  * [MDEV-23102](https://jira.mariadb.org/browse/MDEV-23102) 10.4 create mariadb.sys user on each update even is the user is not needed
* Merge [Revision #b99fa1e767](https://github.com/MariaDB/server/commit/b99fa1e767) 2020-07-04 22:11:16 +0300 - Merge 10.3 into 10.4
* Merge [Revision #e9f06b19e0](https://github.com/MariaDB/server/commit/e9f06b19e0) 2020-07-03 20:26:09 +0300 - Merge remote-tracking branch 'origin/10.3' into 10.4
* Merge [Revision #1bf863a91a](https://github.com/MariaDB/server/commit/1bf863a91a) 2020-07-03 16:17:59 +0200 - Merge branch '10.4-[MDEV-22222](https://jira.mariadb.org/browse/MDEV-22222)' of [mariadb-server](https://github.com/codership/mariadb-server) into 10.4-[MDEV-22222](https://jira.mariadb.org/browse/MDEV-22222)
* [Revision #2b8b7394a1](https://github.com/MariaDB/server/commit/2b8b7394a1)\
  2020-06-28 23:03:38 +0200
  * [MDEV-22222](https://jira.mariadb.org/browse/MDEV-22222): Assertion \`\`state() == s\_executing || state() == s\_preparing || state() == s\_prepared || state() == s\_must\_abort || state() == s\_aborting || state() == s\_cert\_failed || state() == s\_must\_replay'`failed in`wsrep::transaction::before\_rollback\`
* [Revision #e6595a06d6](https://github.com/MariaDB/server/commit/e6595a06d6)\
  2020-07-03 01:18:51 +0300
  * Don't give errors for default value copy in create\_tmp\_table
* Merge [Revision #5211af1c16](https://github.com/MariaDB/server/commit/5211af1c16) 2020-07-03 00:35:28 +0300 - Merge remote-tracking branch 'origin/10.3' into 10.4
* Merge [Revision #f347b3e0e6](https://github.com/MariaDB/server/commit/f347b3e0e6) 2020-07-02 07:39:33 +0300 - Merge 10.3 into 10.4
* [Revision #b0f836053b](https://github.com/MariaDB/server/commit/b0f836053b)\
  2020-06-23 17:07:03 +0200
  * [MDEV-22983](https://jira.mariadb.org/browse/MDEV-22983): mariadb-backup's --help option disappeared
* [Revision #cc0dca3663](https://github.com/MariaDB/server/commit/cc0dca3663)\
  2020-06-30 18:11:35 +0530
  * [MDEV-22910](https://jira.mariadb.org/browse/MDEV-22910): SIGSEGV in `Opt_trace_context::is_started` & SIGSEGV in `Json_writer::add_table_name` (on optimized builds)
* [Revision #8e8f9671cb](https://github.com/MariaDB/server/commit/8e8f9671cb)\
  2020-06-30 14:03:22 +0200
  * [MDEV-21773](https://jira.mariadb.org/browse/MDEV-21773): added missing include file to mtr tests
* [Revision #59c999fc98](https://github.com/MariaDB/server/commit/59c999fc98)\
  2020-06-30 12:47:05 +0200
  * [MDEV-23052](https://jira.mariadb.org/browse/MDEV-23052) - add mysql\_install\_db.exe test with existing directory.
* [Revision #17ce75b936](https://github.com/MariaDB/server/commit/17ce75b936)\
  2020-06-30 12:45:37 +0200
  * [MDEV-23052](https://jira.mariadb.org/browse/MDEV-23052) mysql\_install\_db.exe can run on existing non-empty directory, and remove it on error
* [Revision #d4d42a6ad0](https://github.com/MariaDB/server/commit/d4d42a6ad0)\
  2020-06-27 17:36:53 +0300
  * Revert "Fix cross-compilation for systemd files"
* [Revision #9fff91b59b](https://github.com/MariaDB/server/commit/9fff91b59b)\
  2020-06-27 17:28:51 +0300
  * Fix cross-compilation for systemd files
* Merge [Revision #141b390d82](https://github.com/MariaDB/server/commit/141b390d82) 2020-06-25 13:06:51 +0200 - Merge branch '10.4-[MDEV-22729](https://jira.mariadb.org/browse/MDEV-22729)-2' into 10.4
* [Revision #7bd11fb46f](https://github.com/MariaDB/server/commit/7bd11fb46f)\
  2020-06-23 12:56:08 +0200
  * [MDEV-22729](https://jira.mariadb.org/browse/MDEV-22729): additional changes after merge
* Merge [Revision #4b4e77db64](https://github.com/MariaDB/server/commit/4b4e77db64) 2020-06-19 18:01:15 +0200 - Merge branch '10.4-[MDEV-22729](https://jira.mariadb.org/browse/MDEV-22729)' of [mariadb-server](https://github.com/codership/mariadb-server) into 10.4-[MDEV-22729](https://jira.mariadb.org/browse/MDEV-22729)-2
* [Revision #ccec6b887b](https://github.com/MariaDB/server/commit/ccec6b887b)\
  2020-05-27 21:21:24 +0300
  * [MDEV-22729](https://jira.mariadb.org/browse/MDEV-22729) fixes for galera.galera\_slave\_replay test
* [Revision #dc68846ec5](https://github.com/MariaDB/server/commit/dc68846ec5)\
  2020-06-24 13:41:52 +0300
  * Disable sporadically failing galera\_toi\_truncate test case
* [Revision #bffa8264aa](https://github.com/MariaDB/server/commit/bffa8264aa)\
  2020-06-24 13:19:56 +0300
  * Stabilize glera\_var\_cluster\_conf\_id test case.
* [Revision #33de71c2f8](https://github.com/MariaDB/server/commit/33de71c2f8)\
  2020-05-19 15:38:34 +0300
  * [MDEV-22632](https://jira.mariadb.org/browse/MDEV-22632) wsrep XID checkpointing can happen out of order for certification failure
* [Revision #b4abe7c91f](https://github.com/MariaDB/server/commit/b4abe7c91f)\
  2020-06-23 23:28:37 +0300
  * [MDEV-22993](https://jira.mariadb.org/browse/MDEV-22993): Crash on EXPLAIN with PUSHED DOWN SELECT and subquery
* [Revision #b80b52394d](https://github.com/MariaDB/server/commit/b80b52394d)\
  2020-06-22 13:25:25 +0300
  * Test case cleanups.
* [Revision #ccc4eb8530](https://github.com/MariaDB/server/commit/ccc4eb8530)\
  2020-05-03 01:05:15 +0300
  * [MDEV-22438](https://jira.mariadb.org/browse/MDEV-22438) add a function similar to `std::make_scope_exit()`
* [Revision #4c3cbe2392](https://github.com/MariaDB/server/commit/4c3cbe2392)\
  2020-05-22 21:15:17 +0530
  * [MDEV-22665](https://jira.mariadb.org/browse/MDEV-22665): Print ranges in the optimizer trace created for non-indexed columns when optimizer\_use\_condition\_selectivity >2
* [Revision #205b0ce6ad](https://github.com/MariaDB/server/commit/205b0ce6ad)\
  2020-06-16 12:02:13 +0300
  * [MDEV-22894](https://jira.mariadb.org/browse/MDEV-22894): mariadb-backup should not read \[mariadb-client] option group from configuration files
* [Revision #0121a9e0bb](https://github.com/MariaDB/server/commit/0121a9e0bb)\
  2020-06-16 11:21:28 +0300
  * [MDEV-18215](https://jira.mariadb.org/browse/MDEV-18215): mariadb-backup does not report unknown command line options
* [Revision #01ed614027](https://github.com/MariaDB/server/commit/01ed614027)\
  2020-06-18 12:13:31 +0300
  * Fix the test mariadb-backup.[MDEV-14447](https://jira.mariadb.org/browse/MDEV-14447)
* [Revision #d33c9ca1b0](https://github.com/MariaDB/server/commit/d33c9ca1b0)\
  2020-06-17 22:03:27 +0530
  * [MDEV-22902](https://jira.mariadb.org/browse/MDEV-22902) Assertion \`\`!page\_has\_siblings(block->frame)'`failed in`btr\_pcur\_store\_position\`
* [Revision #b7324e133f](https://github.com/MariaDB/server/commit/b7324e133f)\
  2020-06-17 19:30:19 +0300
  * Remove redundant code in opt\_range.cc: print\_key\_value()
* [Revision #9c577c2b90](https://github.com/MariaDB/server/commit/9c577c2b90)\
  2020-06-16 21:01:16 +0200
  * [MDEV-22917](https://jira.mariadb.org/browse/MDEV-22917) wolfssl might crash at startup when both SSL and encryption plugin are enabled
* [Revision #a0d598a4d2](https://github.com/MariaDB/server/commit/a0d598a4d2)\
  2020-06-04 18:37:18 +0800
  * [MDEV-22794](https://jira.mariadb.org/browse/MDEV-22794): Avoid potential rollback segment contention with increased scalability through even distribution
* [Revision #592a10d079](https://github.com/MariaDB/server/commit/592a10d079)\
  2020-05-22 22:44:37 +0530
  * [MDEV-22370](https://jira.mariadb.org/browse/MDEV-22370) safe\_mutex: Trying to lock uninitialized mutex at /data/src/10.4-bug/sql/rpl\_parallel.cc, line 470 upon shutdown during FTWRL
* [Revision #0128e13e62](https://github.com/MariaDB/server/commit/0128e13e62)\
  2020-06-15 16:39:41 +0300
  * [MDEV-21759](https://jira.mariadb.org/browse/MDEV-21759) galera.galera\_parallel\_autoinc\_manytrx sporadic failures.
* [Revision #49ac606a75](https://github.com/MariaDB/server/commit/49ac606a75)\
  2020-06-14 22:13:45 +0300
  * Fix include statements in galera\_ipv6\_mariadb-backup\_section and galera\_ipv6\_mariadb-backup MTR tests
* [Revision #9bdf35e90f](https://github.com/MariaDB/server/commit/9bdf35e90f)\
  2020-06-08 11:45:56 +0300
  * [MDEV-18215](https://jira.mariadb.org/browse/MDEV-18215): mariadb-backup does not report unknown command line options [MDEV-21298](https://jira.mariadb.org/browse/MDEV-21298): mariadb-backup doesn't read from the \[mariadbd] and \[mariadbd-X.Y] server option groups from configuration files [MDEV-21301](https://jira.mariadb.org/browse/MDEV-21301): mariadb-backup doesn't read \[mariadb-backup] option group in configuration file
* Merge [Revision #ceaa8b647a](https://github.com/MariaDB/server/commit/ceaa8b647a) 2020-06-14 10:32:09 +0300 - Merge commit 10.3 into 10.4
* [Revision #b58586aae9](https://github.com/MariaDB/server/commit/b58586aae9)\
  2020-06-13 12:49:22 +0200
  * [MDEV-21560](https://jira.mariadb.org/browse/MDEV-21560) Assertion \`\`grant\_table || grant\_table\_role'`failed in`check\_grant\_all\_columns\`
* Merge [Revision #805340936a](https://github.com/MariaDB/server/commit/805340936a) 2020-06-13 19:01:28 +0300 - Merge 10.3 into 10.4
* [Revision #f9e53a659c](https://github.com/MariaDB/server/commit/f9e53a659c)\
  2020-06-12 09:55:38 +0400
  * [MDEV-22499](https://jira.mariadb.org/browse/MDEV-22499) Assertion \`\`(uint) (table\_check\_constraints - share->check\_constraints) == (uint) (share->table\_check\_constraints - share->field\_check\_constraints)'`failed in`TABLE\_SHARE::init\_from\_binary\_frm\_image\`
* [Revision #bf2a244406](https://github.com/MariaDB/server/commit/bf2a244406)\
  2020-06-10 13:55:55 +0400
  * [MDEV-22854](https://jira.mariadb.org/browse/MDEV-22854) Garbage returned with SELECT CASE..DEFAULT(timestamp\_field\_with\_now\_as\_default)
* [Revision #86c50a255a](https://github.com/MariaDB/server/commit/86c50a255a)\
  2020-06-08 14:00:19 +0400
  * [MDEV-22734](https://jira.mariadb.org/browse/MDEV-22734) Assertion \`\`mon > 0 && mon < 13'`failed in`sec\_since\_epoch\`
* Merge [Revision #57022dfb25](https://github.com/MariaDB/server/commit/57022dfb25) 2020-06-08 11:45:28 +0300 - Merge 10.3 into 10.4
* [Revision #eb14e073ea](https://github.com/MariaDB/server/commit/eb14e073ea)\
  2020-06-03 13:36:36 +0530
  * [MDEV-22719](https://jira.mariadb.org/browse/MDEV-22719) Long unique keys are not created when individual key\_part->length < max\_key\_length but SUM(key\_parts->length) > max\_key\_length
* [Revision #e208f91ba8](https://github.com/MariaDB/server/commit/e208f91ba8)\
  2020-05-25 15:29:44 +0530
  * [MDEV-21804](https://jira.mariadb.org/browse/MDEV-21804) Assertion \`\`marked\_for\_read()'`failed upon INSERT into table with long unique blob under`binlog\_row\_image=NOBLOB\`
* Merge [Revision #c7a2fb1e08](https://github.com/MariaDB/server/commit/c7a2fb1e08) 2020-06-06 22:05:32 +0300 - Merge 10.3 into 10.4
* Merge [Revision #9d479e2577](https://github.com/MariaDB/server/commit/9d479e2577) 2020-06-05 18:00:14 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #68d9d512e9](https://github.com/MariaDB/server/commit/68d9d512e9) 2020-06-05 18:05:22 +0300 - Merge 10.3 into 10.4
* [Revision #6404645980](https://github.com/MariaDB/server/commit/6404645980)\
  2020-06-04 19:38:31 +0530
  * [MDEV-21626](https://jira.mariadb.org/browse/MDEV-21626): Optimizer misses the details about the picked join order
* Merge [Revision #8059148154](https://github.com/MariaDB/server/commit/8059148154) 2020-06-03 07:32:09 +0300 - Merge 10.3 into 10.4
* [Revision #95ac790296](https://github.com/MariaDB/server/commit/95ac790296)\
  2020-06-02 21:25:51 +0300
  * [MDEV-22773](https://jira.mariadb.org/browse/MDEV-22773) Assertion `page_get_page_no...` in `btr_pcur_store_position()`
* [Revision #457e3128e0](https://github.com/MariaDB/server/commit/457e3128e0)\
  2020-06-02 21:28:21 +0300
  * Added larger timeout to backup\_stages.test
* Merge [Revision #f1c35a996f](https://github.com/MariaDB/server/commit/f1c35a996f) 2020-06-01 15:43:14 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #6da14d7b4a](https://github.com/MariaDB/server/commit/6da14d7b4a) 2020-05-30 11:04:27 +0300 - Merge 10.3 into 10.4
* [Revision #4783494a5e](https://github.com/MariaDB/server/commit/4783494a5e)\
  2020-05-29 16:18:50 +0300
  * [MDEV-22283](https://jira.mariadb.org/browse/MDEV-22283) Server crashes in key\_copy or unexpected error 156
* Merge [Revision #d74e3a56e7](https://github.com/MariaDB/server/commit/d74e3a56e7) 2020-05-29 13:23:37 +0200 - Merge branch 'codership-10.4-[MDEV-22666](https://jira.mariadb.org/browse/MDEV-22666)-v2' into 10.4
* [Revision #e04999c460](https://github.com/MariaDB/server/commit/e04999c460)\
  2020-05-26 14:01:13 +0200
  * Forgotten include files were added to check the necessary conditions for running the test
* Merge [Revision #98a2c6b69e](https://github.com/MariaDB/server/commit/98a2c6b69e) 2020-05-26 13:54:02 +0200 - Merge branch '10.4-[MDEV-22666](https://jira.mariadb.org/browse/MDEV-22666)-v2' of [mariadb-server](https://github.com/codership/mariadb-server) into codership-10.4-[MDEV-22666](https://jira.mariadb.org/browse/MDEV-22666)-v2
* [Revision #1af6e92f0b](https://github.com/MariaDB/server/commit/1af6e92f0b)\
  2020-05-25 14:23:42 +0300
  * [MDEV-22666](https://jira.mariadb.org/browse/MDEV-22666) galera.MW-328A hang
* [Revision #2fbf751407](https://github.com/MariaDB/server/commit/2fbf751407)\
  2020-05-29 12:00:31 +0300
  * [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456) after-merge fix: Avoid functional change to rw\_lock\_s\_unlock()
* [Revision #57f7b4866f](https://github.com/MariaDB/server/commit/57f7b4866f)\
  2020-05-29 11:45:19 +0300
  * [MDEV-16937](https://jira.mariadb.org/browse/MDEV-16937) Strict SQL with system versioned tables causes issues (10.4)
* [Revision #278facee7c](https://github.com/MariaDB/server/commit/278facee7c)\
  2020-05-28 16:56:37 +0300
  * Added test case for query that was crashing in 10.4.13
* [Revision #ed1434df88](https://github.com/MariaDB/server/commit/ed1434df88)\
  2020-05-27 12:16:58 +0530
  * [MDEV-21787](https://jira.mariadb.org/browse/MDEV-21787) Alter table failure tries to access uninitialized column
* [Revision #fdb37d084b](https://github.com/MariaDB/server/commit/fdb37d084b)\
  2020-05-26 20:25:41 +0530
  * [MDEV-21787](https://jira.mariadb.org/browse/MDEV-21787) Alter table failure tries to access uninitialized column
* [Revision #3ad1af9366](https://github.com/MariaDB/server/commit/3ad1af9366)\
  2020-05-26 16:40:41 +0300
  * [MDEV-22545](https://jira.mariadb.org/browse/MDEV-22545): One more fix: main.perror-win
* [Revision #170487473e](https://github.com/MariaDB/server/commit/170487473e)\
  2020-05-26 15:46:09 +0300
  * After-merge fix: main.perror-win
* Merge [Revision #ca38b6e427](https://github.com/MariaDB/server/commit/ca38b6e427) 2020-05-26 11:54:55 +0300 - Merge 10.3 into 10.4
* [Revision #ea7830eef4](https://github.com/MariaDB/server/commit/ea7830eef4)\
  2020-05-22 16:31:16 +0400
  * [MDEV-14221](https://jira.mariadb.org/browse/MDEV-14221) Assertion \`\`0'`failed in`Item::field\_type\_for\_temporal\_comparison\`
* [Revision #dc22acfdb6](https://github.com/MariaDB/server/commit/dc22acfdb6)\
  2020-05-21 08:34:03 +0200
  * [MDEV-22616](https://jira.mariadb.org/browse/MDEV-22616) CHECK TABLE fails with wsrep\_trx\_fragment\_size > 0 (#1551)
* Merge [Revision #ce1c6dab3a](https://github.com/MariaDB/server/commit/ce1c6dab3a) 2020-05-20 21:15:43 +0530 - [MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451): SIGSEGV in `__memmove_avx_unaligned_erms/memcpy` from `_my_b_write` on `CREATE after RESET MASTER`
* Merge [Revision #b8e694a314](https://github.com/MariaDB/server/commit/b8e694a314) 2020-05-20 17:10:12 +0300 - Merge 10.3 into 10.4
* [Revision #96bc626b8f](https://github.com/MariaDB/server/commit/96bc626b8f)\
  2020-05-20 09:37:05 +0000
  * [MDEV-22631](https://jira.mariadb.org/browse/MDEV-22631) fix
* Merge [Revision #d8dc3c72b6](https://github.com/MariaDB/server/commit/d8dc3c72b6) 2020-05-20 12:25:23 +0300 - Merge 10.3 into 10.4
* Merge [Revision #2bf93a8fd6](https://github.com/MariaDB/server/commit/2bf93a8fd6) 2020-05-19 21:18:15 +0300 - Merge 10.3 into 10.4
* [Revision #6b5f7ddc78](https://github.com/MariaDB/server/commit/6b5f7ddc78)\
  2020-05-19 15:15:52 +0000
  * [MDEV-22636](https://jira.mariadb.org/browse/MDEV-22636) XML output for mtr doesn't work with valgrind option
* [Revision #fa0397849a](https://github.com/MariaDB/server/commit/fa0397849a)\
  2020-05-19 14:07:34 +0300
  * Move c++ code from my\_atomic.h to my\_atomic\_wrapper.h
* [Revision #f7079d295b](https://github.com/MariaDB/server/commit/f7079d295b)\
  2020-05-19 12:40:59 +0400
  * [MDEV-22610](https://jira.mariadb.org/browse/MDEV-22610) Crash in INSERT INTO t1 (VALUES (DEFAULT) UNION VALUES (DEFAULT))
* Merge [Revision #810b7f8ecb](https://github.com/MariaDB/server/commit/810b7f8ecb) 2020-05-19 12:03:12 +0400 - Merge remote-tracking branch 'origin/10.3' into 10.4
* Merge [Revision #faf6d0ef3f](https://github.com/MariaDB/server/commit/faf6d0ef3f) 2020-05-18 15:05:52 +0300 - Merge 10.3 into 10.4
* [Revision #386f168ab3](https://github.com/MariaDB/server/commit/386f168ab3)\
  2020-05-18 14:49:44 +0300
  * [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456) after-merge fix: introduce Atomic\_relaxed
* [Revision #fde94b4cd6](https://github.com/MariaDB/server/commit/fde94b4cd6)\
  2020-05-08 11:35:15 +0300
  * [MDEV-21483](https://jira.mariadb.org/browse/MDEV-21483) : Galera MTR tests failed: galera.MW-328A galera.MW-328B
* [Revision #ea912d1605](https://github.com/MariaDB/server/commit/ea912d1605)\
  2020-05-15 18:35:19 +0200
  * [MDEV-22554](https://jira.mariadb.org/browse/MDEV-22554): galera\_sst\_mariadb-backup fails with "Failed to start mysqld.2"
* [Revision #0a5668f512](https://github.com/MariaDB/server/commit/0a5668f512)\
  2020-05-15 02:37:16 +0530
  * [MDEV-22556](https://jira.mariadb.org/browse/MDEV-22556): Incorrect result for window function when using encrypt-tmp-files=ON
* Merge [Revision #66f1e288a1](https://github.com/MariaDB/server/commit/66f1e288a1) 2020-05-16 07:54:09 +0300 - Merge 10.3 into 10.4
* Merge [Revision #9e6e43551f](https://github.com/MariaDB/server/commit/9e6e43551f) 2020-05-16 07:39:15 +0300 - Merge 10.3 into 10.4
* Merge [Revision #4f29d776c7](https://github.com/MariaDB/server/commit/4f29d776c7) 2020-05-16 06:27:55 +0300 - Merge 10.3 into 10.4
* [Revision #a4996f951d](https://github.com/MariaDB/server/commit/a4996f951d)\
  2020-05-15 16:17:15 +0300
  * [MDEV-22563](https://jira.mariadb.org/browse/MDEV-22563) Segfault on duplicate free of `Item_func_in::array`
* [Revision #72789e4b2b](https://github.com/MariaDB/server/commit/72789e4b2b)\
  2020-05-15 15:14:08 +0300
  * Fixed access to not initalized memory
* [Revision #523d67a272](https://github.com/MariaDB/server/commit/523d67a272)\
  2020-05-14 09:17:14 +0300
  * [MDEV-22494](https://jira.mariadb.org/browse/MDEV-22494) : Galera assertion `lock_sys.mutex.is_owned()` at `lock_trx_handle_wait_low`
* [Revision #3bfe305c5c](https://github.com/MariaDB/server/commit/3bfe305c5c)\
  2020-05-14 15:46:17 +0200
  * [MDEV-22555](https://jira.mariadb.org/browse/MDEV-22555) Windows, packaging: binaries depend on vcruntime140\_1.dll, which is not in MSI
* Merge [Revision #38f6c47f8a](https://github.com/MariaDB/server/commit/38f6c47f8a) 2020-05-13 12:52:57 +0300 - Merge 10.3 into 10.4
* [Revision #9f20968169](https://github.com/MariaDB/server/commit/9f20968169)\
  2020-05-12 19:45:21 +0400
  * [MDEV-20261](https://jira.mariadb.org/browse/MDEV-20261) NULL passed to `String::eq`, SEGV, server crash, regression in 10.4
* Merge [Revision #db537a8372](https://github.com/MariaDB/server/commit/db537a8372) 2020-05-11 21:32:33 +0200 - Merge branch '10.4-release' into 10.4
* [Revision #15502e5e33](https://github.com/MariaDB/server/commit/15502e5e33)\
  2020-05-11 01:00:15 +0200
  * [MDEV-21965](https://jira.mariadb.org/browse/MDEV-21965) main.tls\_version and main.tls\_version1 fail in buildbot on Ubuntu Focal
* [Revision #6e99974d6e](https://github.com/MariaDB/server/commit/6e99974d6e)\
  2020-05-11 12:59:25 -0400
  * bump the VERSION
* [Revision #6adb0d2f7c](https://github.com/MariaDB/server/commit/6adb0d2f7c)\
  2020-05-08 18:20:38 +0200
  * [MDEV-22459](https://jira.mariadb.org/browse/MDEV-22459) pam v2 should log an error if auth\_pam\_tool exec fails
* [Revision #a878344ee5](https://github.com/MariaDB/server/commit/a878344ee5)\
  2020-05-08 09:16:37 +0300
  * [MDEV-21421](https://jira.mariadb.org/browse/MDEV-21421) : Galera test sporadic failure on galera.galera\_as\_slave\_gtid\_myisam: Result length mismatch
* [Revision #057a700a2a](https://github.com/MariaDB/server/commit/057a700a2a)\
  2020-05-07 14:23:33 +0300
  * [MDEV-22466](https://jira.mariadb.org/browse/MDEV-22466) : Galera missing .test or .result files
* [Revision #8d3795f173](https://github.com/MariaDB/server/commit/8d3795f173)\
  2020-05-07 00:53:16 +0200
  * [MDEV-22487](https://jira.mariadb.org/browse/MDEV-22487) WolfSSL - server prints "Please supply a buffer for error string"

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
