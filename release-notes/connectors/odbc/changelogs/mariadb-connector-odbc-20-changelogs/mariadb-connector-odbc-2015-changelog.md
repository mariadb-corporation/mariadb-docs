# Connector/ODBC 2.0.15 Changelog

The most recent [_**Stable**_](../../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/2.0.15)[Release Notes](../../mariadb-connector-odbc-20-release-notes/mariadb-connector-odbc-2015-release-notes.md)[Changelog](mariadb-connector-odbc-2015-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 23 May 2017

For the highlights of this release, see the [release notes](../../mariadb-connector-odbc-20-release-notes/mariadb-connector-odbc-2015-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-odbc) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #6a1619b](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/6a1619b)\
  2017-05-16 04:44:37 +0200
  * \[[ODBC-97](https://jira.mariadb.org/browse/ODBC-97)] Fix and addition to the old testcase to care about this issue. The problem was that parser would think of \ that it escapes closing quote, even if it was escaped in its turn(i.e. if it represented the character in the string. Also the case of NO\_BACKSLASH\_ESCAPES is now respected.
* [Revision #4b805ec](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/4b805ec)\
  2017-05-15 09:36:34 +0200
  * \[[ODBC-95](https://jira.mariadb.org/browse/ODBC-95)] If any of statements in a batch could not be prepared, application would crash on the attempt to free that statement handle. Fix and testcase
* [Revision #e7276e0](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/e7276e0)\
  2017-05-10 05:19:33 +0200
  * Removed internal function for SQLFetch, using internal function for SQLFetchScroll with SQL\_FETCH\_NEXT instead. Added testcase for SQLFetch with array size > 1. I felt like there could be problems. And just won't hurt to have. Removed FetchType from Stmt handle structure as they weren't used anywhere.
* [Revision #daaf929](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/daaf929)\
  2017-05-03 22:35:16 +0200
  * \[[ODBC-94](https://jira.mariadb.org/browse/ODBC-94)] The driver would crash with ODBCv2 with exotic sqlstate, e.g. OP000, as a result of bad GRANT syntax. The reason was that sqlstate field in MADB\_ERROR struct is array, but connector waited for NULL sqlstate to stop traversing the MADB\_ErrorList array. Testcase has been added. Patch also adds convenience function for tests to check if the server meets some minimum version criteria. Also, we seemingly had problem SQL\_DBMS\_VER info type. The patch fixes that as well.
* [Revision #45a1418](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/45a1418)\
  2017-04-14 14:53:21 +0200
  * Added to cmake config the parameter to specify system name(SYSTEM\_NAME), to be used in the package name.
* [Revision #fd9139d](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/fd9139d)\
  2017-04-07 13:20:13 +0200
  * Small optimization for an array fetch - bind structures are allocated only once now

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
