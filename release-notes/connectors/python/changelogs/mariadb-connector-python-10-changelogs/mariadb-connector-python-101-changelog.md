# Connector/Python 1.0.1 Changelog

{% include "../../../../.gitbook/includes/latest-python.md" %}

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/python-connector/" class="button primary">Download</a> <a href="../../mariadb-connector-python-1-0-release-notes/mariadb-connector-python-1-0-1-release-notes.md" class="button secondary">Release Notes</a> <a href="mariadb-connector-python-101-changelog.md" class="button secondary">Changelog</a> <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/connector-python-guide" class="button secondary">Connector/Python Overview</a>

**Release date:** 18 Aug 2020

For the highlights of this release, see the [release notes](../../mariadb-connector-python-1-0-release-notes/mariadb-connector-python-1-0-1-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-python/) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #16a3882](https://github.com/mariadb-corporation/mariadb-connector-python/commit/16a3882)\
  2020-08-16 17:38:20 +0200
  * Add secur32 and bcrypt for windows static linking (schannel)
* [Revision #d9a5ee4](https://github.com/mariadb-corporation/mariadb-connector-python/commit/d9a5ee4)\
  2020-08-16 16:03:27 +0200
  * Travi fix for 10.1 test: error < 2 result in mariadb.OperationalError
* [Revision #837a36e](https://github.com/mariadb-corporation/mariadb-connector-python/commit/837a36e)\
  2020-08-16 15:10:26 +0200
  * Fix rowcount calculation for emulated bulk operations
* [Revision #ffeb8b9](https://github.com/mariadb-corporation/mariadb-connector-python/commit/ffeb8b9)\
  2020-08-16 13:02:35 +0200
  * Fix exception type check for ed25512 plugin test
* [Revision #c2d96a9](https://github.com/mariadb-corporation/mariadb-connector-python/commit/c2d96a9)\
  2020-08-16 12:01:26 +0200
  * Fix time tests: MYSQL\_TYPE\_TIME will be converted to datetime.timedelta now.
* [Revision #7493324](https://github.com/mariadb-corporation/mariadb-connector-python/commit/7493324)\
  2020-08-16 09:40:10 +0200
  * Fix for [CONPY-99](https://jira.mariadb.org/browse/CONPY-99):
* [Revision #92eaf17](https://github.com/mariadb-corporation/mariadb-connector-python/commit/92eaf17)\
  2020-08-16 07:30:58 +0200
  * Follow up fix for [CONPY-107](https://jira.mariadb.org/browse/CONPY-107):
* [Revision #e078e26](https://github.com/mariadb-corporation/mariadb-connector-python/commit/e078e26)\
  2020-08-15 19:00:40 +0200
  * Fix for [CONPY-107](https://jira.mariadb.org/browse/CONPY-107):
* [Revision #021c4e6](https://github.com/mariadb-corporation/mariadb-connector-python/commit/021c4e6)\
  2020-08-14 19:55:41 +0200
  * Allow different decimal types in executemany():
* [Revision #afea681](https://github.com/mariadb-corporation/mariadb-connector-python/commit/afea681)\
  2020-08-14 16:44:13 +0200
  * Fix for [CONPY-105](https://jira.mariadb.org/browse/CONPY-105): Change behavior of cursor->rowcount and cursor->lastrowid
* [Revision #30d5793](https://github.com/mariadb-corporation/mariadb-connector-python/commit/30d5793)\
  2020-08-14 16:38:19 +0200
  * Followup for fix for [CONPY-106](https://jira.mariadb.org/browse/CONPY-106)
* [Revision #e091edd](https://github.com/mariadb-corporation/mariadb-connector-python/commit/e091edd)\
  2020-08-14 14:44:05 +0200
  * Fix for [CONPY-106](https://jira.mariadb.org/browse/CONPY-106)
* [Revision #588bc01](https://github.com/mariadb-corporation/mariadb-connector-python/commit/588bc01)\
  2020-08-12 16:05:29 +0200
  * Implementation for [CONPY-100](https://jira.mariadb.org/browse/CONPY-100):
* [Revision #cdbb088](https://github.com/mariadb-corporation/mariadb-connector-python/commit/cdbb088)\
  2020-08-12 15:11:29 +0200
  * Fixed build error: Added missing backslash
* [Revision #ab2553a](https://github.com/mariadb-corporation/mariadb-connector-python/commit/ab2553a)\
  2020-08-12 14:59:30 +0200
  * Added test for [CONPY-103](https://jira.mariadb.org/browse/CONPY-103)
* [Revision #0e91d76](https://github.com/mariadb-corporation/mariadb-connector-python/commit/0e91d76)\
  2020-08-12 14:19:02 +0200
  * Fix for [CONPY-102](https://jira.mariadb.org/browse/CONPY-102):
* [Revision #03f283a](https://github.com/mariadb-corporation/mariadb-connector-python/commit/03f283a)\
  2020-08-12 07:31:25 +0200
  * Fix for [CONPY-101](https://jira.mariadb.org/browse/CONPY-101): Negative refcount when executing callproc() method
* [Revision #067a78d](https://github.com/mariadb-corporation/mariadb-connector-python/commit/067a78d)\
  2020-08-10 14:59:16 +0200
  * Fix for CONPY68 (jsonfield returning as bytes):
* [Revision #a749c53](https://github.com/mariadb-corporation/mariadb-connector-python/commit/a749c53)\
  2020-08-07 14:45:50 +0200
  * Fix for [CONPY-98](https://jira.mariadb.org/browse/CONPY-98):
* [Revision #4321164](https://github.com/mariadb-corporation/mariadb-connector-python/commit/4321164)\
  2020-08-07 12:42:32 +0200
  * Added test for [CONPY-91](https://jira.mariadb.org/browse/CONPY-91)
* [Revision #c593136](https://github.com/mariadb-corporation/mariadb-connector-python/commit/c593136)\
  2020-08-06 18:26:44 +0200
  * Fix for [CONPY-95](https://jira.mariadb.org/browse/CONPY-95)
* [Revision #bfd71e2](https://github.com/mariadb-corporation/mariadb-connector-python/commit/bfd71e2)\
  2020-08-06 15:03:48 +0200
  * Fix for [CONPY-94](https://jira.mariadb.org/browse/CONPY-94):
* [Revision #cf90a9d](https://github.com/mariadb-corporation/mariadb-connector-python/commit/cf90a9d)\
  2020-08-06 07:50:45 +0200
  * Fixed identation
* [Revision #9026c1a](https://github.com/mariadb-corporation/mariadb-connector-python/commit/9026c1a)\
  2020-08-05 19:22:35 +0200
  * Fixed built-in help
* [Revision #1a787c2](https://github.com/mariadb-corporation/mariadb-connector-python/commit/1a787c2)\
  2020-08-05 19:19:13 +0200
  * Updated documentation
* [Revision #e3eba3a](https://github.com/mariadb-corporation/mariadb-connector-python/commit/e3eba3a)\
  2020-08-05 19:01:53 +0200
  * Added method pool.close()
* [Revision #01053e0](https://github.com/mariadb-corporation/mariadb-connector-python/commit/01053e0)\
  2020-08-05 18:54:19 +0200
  * Fix for [CONPY-93](https://jira.mariadb.org/browse/CONPY-93):
* [Revision #cf1b461](https://github.com/mariadb-corporation/mariadb-connector-python/commit/cf1b461)\
  2020-07-24 16:54:33 +0200
  * Fix travis build
* [Revision #a9fe837](https://github.com/mariadb-corporation/mariadb-connector-python/commit/a9fe837)\
  2020-07-24 12:33:17 +0200
  * Fixed connection test
* [Revision #29b05e3](https://github.com/mariadb-corporation/mariadb-connector-python/commit/29b05e3)\
  2020-07-24 12:13:31 +0200
  * Various fixes and changes for SQLAlchemy support:
* [Revision #b4a30ba](https://github.com/mariadb-corporation/mariadb-connector-python/commit/b4a30ba)\
  2020-07-22 19:05:54 +0200
  * Fixed version checking for Connector/C:
* [Revision #7d4ff26](https://github.com/mariadb-corporation/mariadb-connector-python/commit/7d4ff26)\
  2020-07-15 18:49:04 +0200
  * Avoid access internal members of the mysql structure:
* [Revision #c6ad169](https://github.com/mariadb-corporation/mariadb-connector-python/commit/c6ad169)\
  2020-07-15 13:28:33 +0200
  * Fix for [CONPY-85](https://jira.mariadb.org/browse/CONPY-85):
* [Revision #92d8c40](https://github.com/mariadb-corporation/mariadb-connector-python/commit/92d8c40)\
  2020-07-07 16:32:27 +0200
  * Merge branch 'master' of [mariadb-connector-python](https://github.com/mariadb-corporation/mariadb-connector-python)
* [Revision #cbee80b](https://github.com/mariadb-corporation/mariadb-connector-python/commit/cbee80b)\
  2020-06-24 14:16:48 +0200
  * Update README.md
* [Revision #ee1e81a](https://github.com/mariadb-corporation/mariadb-connector-python/commit/ee1e81a)\
  2020-07-07 16:29:41 +0200
  * Fix for [CONPY-83](https://jira.mariadb.org/browse/CONPY-83)
* [Revision #fa61a66](https://github.com/mariadb-corporation/mariadb-connector-python/commit/fa61a66)\
  2020-06-24 13:46:24 +0200
  * coverity scan fixes
* [Revision #1a1b033](https://github.com/mariadb-corporation/mariadb-connector-python/commit/1a1b033)\
  2020-06-24 09:03:11 +0200
  * Fix for [CONPY-82](https://jira.mariadb.org/browse/CONPY-82):
* [Revision #2ee51a0](https://github.com/mariadb-corporation/mariadb-connector-python/commit/2ee51a0)\
  2020-06-24 08:58:37 +0200
  * Bumped version number

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
