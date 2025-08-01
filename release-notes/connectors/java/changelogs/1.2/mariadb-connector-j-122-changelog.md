# MariaDB Connector/J 1.2.2 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.2.2/)[Release Notes](../../1.2/mariadb-connector-j-122-release-notes.md)[Changelog](mariadb-connector-j-122-changelog.md)[Connector/J Overview](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/about-mariadb-connector-j)

**Release date:** 10 Sep 2015

For the highlights of this release, see the\[release notes]\(https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/connectors/java/mariadb-connector-j-12-release-notes/mariadb-connector-j-122-release-notes

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

**This version has changed some dependencies :**

* logging now uses SLF4J.
* commons-dbcp is now used only when testing, and there is no more need to import it.[About the MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-connector-j/README.md) page.
* [CONJ-188](https://jira.mariadb.org/browse/CONJ-188) : Default pool framework initialisation - [Revision #0447a87](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0447a87) 2015-08-09
* [CONJ-184](https://jira.mariadb.org/browse/CONJ-184) : SSL Tests Not Run on Travis-CI
  * [Revision #ec8dc4a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ec8dc4a) 2015-08-08
  * [Revision #faff539](https://github.com/mariadb-corporation/mariadb-connector-j/commit/faff539) 2015-08-08
  * [Revision #95f6f7c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/95f6f7c) 2015-08-08
  * [Revision #007d35e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/007d35e) 2015-08-08
  * [Revision #b7d165b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b7d165b) 2015-08-08
  * [Revision #78a27e3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/78a27e3) 2015-08-09
  * [Revision #9d5e465](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9d5e465) 2015-08-09
  * [Revision #0b11f8e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0b11f8e) 2015-09-02
* [CONJ-178](https://jira.mariadb.org/browse/CONJ-178) : Change Apache DBCP scope to test in pom - [Revision #0100777](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0100777) 2015-08-07
* [CONJ-176](https://jira.mariadb.org/browse/CONJ-176) : Permit use of multiple SSL certificate - [Revision #a9be62f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a9be62f) 2015-08-01
* [CONJ-175](https://jira.mariadb.org/browse/CONJ-175) : Add allowLocalInfile parameter to allow /disable file upload - [Revision #1a28083](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1a28083) 2015-08-01
* [CONJ-172](https://jira.mariadb.org/browse/CONJ-172) : Return from result set not checked creating connection - [Revision #297b234](https://github.com/mariadb-corporation/mariadb-connector-j/commit/297b234) 2015-07-21
* [CONJ-171](https://jira.mariadb.org/browse/CONJ-171) : Removed Sometimes Unnecessary String Instantiation That Can Cause Thread Blocking - [Revision #04f17cc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/04f17cc) 2015-07-29
* [CONJ-168](https://jira.mariadb.org/browse/CONJ-168) : Rewritten batch insert can fail if the first value isn't a parameter - [Revision #58b62cc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/58b62cc) 2015-07-21
* [CONJ-167](https://jira.mariadb.org/browse/CONJ-167) : Driver is throwing IllegalArgumentException instead of returning null
  * [Revision #7b629cd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7b629cd) 2015-07-21
  * [Revision #4419ac0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4419ac0) 2015-07-21
* [CONJ-163](https://jira.mariadb.org/browse/CONJ-163) : make column label name display instead column name when useOldAliasMetadataBehavior option true - [Revision #afa24ed](https://github.com/mariadb-corporation/mariadb-connector-j/commit/afa24ed) 2015-07-22
* [CONJ-141](https://jira.mariadb.org/browse/CONJ-141) : Batch Statement Rewrite: Support for ON DUPLICATE KEY - [Revision #1bfe353](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1bfe353) 2015-07-22
* TRAVIS : amelioration of continious integration\
  2015-07-22
  * [Revision #f77ea51](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f77ea51)\
    2015-07-23
  * [Revision #54e624d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/54e624d)\
    2015-07-23
  * [Revision #af1b810](https://github.com/mariadb-corporation/mariadb-connector-j/commit/af1b810)\
    2015-08-04
  * [Revision #7f794e7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7f794e7)\
    2015-08-04
  * [Revision #a26013e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a26013e)
* MISC : Change SSLSocketFactory.createSocket to use autoClose=true - [Revision #159d791](https://github.com/mariadb-corporation/mariadb-connector-j/commit/159d791) 2015-08-01
* MISC : Change scope of dbcp to test - [Revision #9b60ba7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9b60ba7) 2015-08-07
* MISC : adding automatic release deployement script - [Revision #73bd695](https://github.com/mariadb-corporation/mariadb-connector-j/commit/73bd695) 2015-09-02

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
