# MariaDB Connector/J 1.1.9 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.1.9/)[Release Notes](../../1.1/mariadb-connector-j-119-release-notes.md)[Changelog](mariadb-connector-j-119-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-connector-j/README.md)

**Release date:** 18 Jun 2015

For the highlights of this release, see the [release notes](../../1.1/mariadb-connector-j-119-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #fae71ea](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fae71ea)\
  2015-06-04 13:20:03 +0200
  * [CONJ-152](https://jira.mariadb.org/browse/CONJ-152) - rewriteBatchedStatements and multiple executeBatch error
* [Revision #59f3d68](https://github.com/mariadb-corporation/mariadb-connector-j/commit/59f3d68)\
  2015-05-29 16:18:32 -0700
  * fix for max\_allowed\_packet check. also remove some obsolete stuff . also, remove batch rewrites for prepared statements, it does not work as it is written
* [Revision #fb16405](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fb16405)\
  2015-05-29 17:04:50 +0200
  * Merge remote-tracking branch 'origin/master' into [CONJ-152](https://jira.mariadb.org/browse/CONJ-152)
* [Revision #308382b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/308382b)\
  2015-05-29 17:03:30 +0200
  * [CONJ-152](https://jira.mariadb.org/browse/CONJ-152) - rewriteBatchedStatements and multiple executeBatch error
* [Revision #a7b3241](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a7b3241)\
  2015-05-29 16:10:30 +0200
  * Merge pull request #13 from MariaDB/[CONJ-151](https://jira.mariadb.org/browse/CONJ-151)
* [Revision #a163bdb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a163bdb)\
  2015-05-29 16:06:33 +0200
  * [CONJ-151](https://jira.mariadb.org/browse/CONJ-151) - performance degraded after upgrading from 1.1.7 to 1.1.8
* [Revision #4b460e6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4b460e6)\
  2015-05-28 22:56:09 +0200
  * Create README.md
* [Revision #6ea6c1e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6ea6c1e)\
  2015-05-28 18:06:22 +0200
  * Perf amelioration
* [Revision #8f88239](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8f88239)\
  2015-05-28 16:15:14 +0200
  * [CONJ-156](https://jira.mariadb.org/browse/CONJ-156) - SecurityManager used the good way [CONJ-157](https://jira.mariadb.org/browse/CONJ-157) - batch rewrite correction [CONJ-158](https://jira.mariadb.org/browse/CONJ-158) - Test longBlog corrected
* [Revision #a812c75](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a812c75)\
  2015-05-28 16:06:29 +0200
  * [CONJ-156](https://jira.mariadb.org/browse/CONJ-156) - SecurityManager used the good way [CONJ-157](https://jira.mariadb.org/browse/CONJ-157) - batch rewrite correction [CONJ-158](https://jira.mariadb.org/browse/CONJ-158) - Test longBlog corrected
* [Revision #9fc77b2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9fc77b2)\
  2015-05-20 11:29:02 +0200
  * Merge pull request #8 from rasmushoj/master
* [Revision #a798ed3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a798ed3)\
  2015-05-20 09:36:29 +0300
  * Fixed failing test cases
* [Revision #b4c9b59](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b4c9b59)\
  2015-05-20 09:34:03 +0300
  * Revert "Merge branch 'rasmus-failover'"
* [Revision #5900322](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5900322)\
  2015-05-20 09:31:20 +0300
  * Merge branch 'rasmus-failover'
* [Revision #ea70a96](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ea70a96)\
  2015-05-20 09:30:14 +0300
  * Fixed failing test cases
* [Revision #c49eb6c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c49eb6c)\
  2015-05-19 17:01:30 +0300
  * Merge branch 'master' into rasmus-failover
* [Revision #6442bce](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6442bce)\
  2015-05-19 16:57:25 +0300
  * Merge pull request #1 from MariaDB/master
* [Revision #53c792f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/53c792f)\
  2015-05-19 16:40:32 +0300
  * Merge pull request #7 from roidelapluie/master
* [Revision #40b2cdb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/40b2cdb)\
  2015-05-19 16:36:38 +0300
  * Removed prints and added ignore for lastPacketFailedTest
* [Revision #f449adc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f449adc)\
  2015-05-19 14:06:43 +0200
  * Fix hostname in new ConnectionPoolTest
* [Revision #e62c4f4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e62c4f4)\
  2015-05-19 11:17:36 +0300
  * Merge pull request #6 from roidelapluie/master
* [Revision #5e12a2f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5e12a2f)\
  2015-05-18 23:07:20 +0300
  * Merge branch 'rasmus-test-case-fixes'
* [Revision #6d9804a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6d9804a)\
  2015-05-18 23:07:08 +0300
  * Correcting merge conflict in JDBCUrl
* [Revision #af0aef1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/af0aef1)\
  2015-05-18 22:44:38 +0300
  * Merge branch 'packet-not-received'
* [Revision #68b55be](https://github.com/mariadb-corporation/mariadb-connector-j/commit/68b55be)\
  2015-05-18 22:38:10 +0300
  * Added tests for connection pooling and timeouts
* [Revision #713720e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/713720e)\
  2015-05-18 18:42:22 +0200
  * add documentation + better search loop for aurora
* [Revision #0c26bdd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0c26bdd)\
  2015-05-18 18:11:58 +0200
  * add documentation
* [Revision #4267224](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4267224)\
  2015-05-14 18:23:03 +0200
  * Add parameters to tests so they can be run against a MariaDB server different than LocalHost.
* [Revision #9376624](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9376624)\
  2015-05-17 17:59:31 +0200
  * Failover handling
* [Revision #ccd0a21](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ccd0a21)\
  2015-05-07 10:47:27 +0300
  * Merge branch 'master' into rasmus-failover
* [Revision #a077f2d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a077f2d)\
  2015-05-07 10:42:33 +0300
  * Test cases stubs for failover
* [Revision #dd389d5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dd389d5)\
  2015-04-17 16:36:39 -0700
  * merge conflict
* [Revision #090bd2e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/090bd2e)\
  2015-04-17 16:10:29 -0700
  * Merge pull request #5 from MariaDB/[CONJ-149](https://jira.mariadb.org/browse/CONJ-149)
* [Revision #cde290d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cde290d)\
  2015-04-17 16:09:40 -0700
  * merge conflict
* [Revision #aef4f57](https://github.com/mariadb-corporation/mariadb-connector-j/commit/aef4f57)\
  2015-04-17 16:00:48 -0700
  * [CONJ-149](https://jira.mariadb.org/browse/CONJ-149) ResultSetMetaData.getTableName returns table alias instead of real table name
* [Revision #270b0e4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/270b0e4)\
  2015-04-17 14:51:50 -0700
  * Merge pull request #4 from MariaDB/rasmusj-testcases
* [Revision #1111466](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1111466)\
  2015-04-17 14:50:43 -0700
  * Fixing test cases
* [Revision #cbb6522](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cbb6522)\
  2015-04-17 14:35:55 -0700
  * Merge pull request #3 from MariaDB/[CONJ-142](https://jira.mariadb.org/browse/CONJ-142)
* [Revision #fc2d417](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fc2d417)\
  2015-04-17 14:33:48 -0700
  * [CONJ-142](https://jira.mariadb.org/browse/CONJ-142): Using a semicolon in a string with "rewriteBatchedStatements=true" fails
* [Revision #f7b8ad3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f7b8ad3)\
  2015-04-17 09:41:50 -0700
  * Merge pull request #2 from MariaDB/[CONJ-150](https://jira.mariadb.org/browse/CONJ-150)
* [Revision #62ef042](https://github.com/mariadb-corporation/mariadb-connector-j/commit/62ef042)\
  2015-04-17 09:39:12 -0700
  * [CONJ-150](https://jira.mariadb.org/browse/CONJ-150) Fixes to JDBC URL
* [Revision #edef9c0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/edef9c0)\
  2015-04-14 11:11:41 -0700
  * Merge branch 'rasmus-test-case-fixes' into rasmus-failover
* [Revision #869cbdf](https://github.com/mariadb-corporation/mariadb-connector-j/commit/869cbdf)\
  2015-04-14 11:10:15 -0700
  * some gitignore change by eclipse
* [Revision #830e29c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/830e29c)\
  2015-04-13 12:35:47 +0300
  * [CONJ-142](https://jira.mariadb.org/browse/CONJ-142): Using a semicolon in a string with "rewriteBatchedStatements=true" fails
* [Revision #d4e01e2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d4e01e2)\
  2015-04-11 10:21:39 +0300
  * Added functions for checking for super privileges and local connections
* [Revision #b534523](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b534523)\
  2015-04-10 13:00:00 +0300
  * Connection corrections in test cases
* [Revision #964d222](https://github.com/mariadb-corporation/mariadb-connector-j/commit/964d222)\
  2015-04-10 12:46:18 +0300
  * Test cases connection corrections and marking test cases for being skipped properly
* [Revision #5c05e1e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5c05e1e)\
  2015-04-10 00:43:51 +0300
  * Marking skipped tests as skipped
* [Revision #0be2d6b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0be2d6b)\
  2015-04-10 00:34:25 +0300
  * Fixed mdev3916 test case
* [Revision #b31fb95](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b31fb95)\
  2015-04-10 00:17:23 +0300
  * Parsing of JDBC url did not work
* [Revision #16842b2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/16842b2)\
  2015-01-30 15:52:03 +0100
  * Added github support for pom.xml
* [Revision #d44dcf2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d44dcf2)\
  2015-01-30 14:20:03 +0100
  * Forced line endings to eol=lf
* [Revision #c52acdb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c52acdb)\
  2015-01-30 14:19:04 +0100
  * Migrated from Bazaar to Git.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
