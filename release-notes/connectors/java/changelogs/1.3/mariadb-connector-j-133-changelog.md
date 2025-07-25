# MariaDB Connector/J 1.3.3 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.3.3/)[Release Notes](../../1.3/mariadb-connector-j-133-release-notes.md)[Changelog](mariadb-connector-j-133-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 8 Dec 2015

For the highlights of this release, see the [release notes](../../1.3/mariadb-connector-j-133-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

## Fixes

* [CONJ-225](https://jira.mariadb.org/browse/CONJ-225) : ResultSet.getString correction for prepareStatement.
  * [Revision #455f36f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/455f36f) 2015-11-30
  * [Revision #fce8e4c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fce8e4c) 2015-11-30
* [CONJ-226](https://jira.mariadb.org/browse/CONJ-226) : PreparedStatement return NULL When TIME column value=00:00:00. [Revision #528fa17](https://github.com/mariadb-corporation/mariadb-connector-j/commit/528fa17) 2015-11-30
* [CONJ-227](https://jira.mariadb.org/browse/CONJ-227) : Mariadb alias in url connection string wasn't working in HA mode. [Revision #4a5b824](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4a5b824) 2015-11-30
* [CONJ-228](https://jira.mariadb.org/browse/CONJ-228) : Handle unsigned numeric data.
  * [Revision #cf73089](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cf73089) 2015-12-03
  * [Revision #e9c756d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e9c756d) 2015-12-04
* [CONJ-224](https://jira.mariadb.org/browse/CONJ-224) : Metadata driver version. [Revision #749bca5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/749bca5) 2015-12-04
* [CONJ-229](https://jira.mariadb.org/browse/CONJ-229) : Host is not mandatory for named pipe connection. [Revision #43de452](https://github.com/mariadb-corporation/mariadb-connector-j/commit/43de452) 2015-12-02
* [CONJ-179](https://jira.mariadb.org/browse/CONJ-179) : Statement.getMoreResults() was returning wrong value. [Revision #76cfdfe](https://github.com/mariadb-corporation/mariadb-connector-j/commit/76cfdfe) 2015-11-22
  * [Revision #41598be](https://github.com/mariadb-corporation/mariadb-connector-j/commit/41598be) 2015-11-24
  * [Revision #9cc948e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9cc948e) 2015-11-24

## Misc

* various improvements
  * replace stringbuffer with stringbuilder : [Revision #7ea4ffc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7ea4ffc) 2015-11-30
  * Fix unit of default value of retriesAllDown in the documentation : [Revision #480465b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/480465b) 2015-11-30
  * delete test logging dependency, since it cause error on travis with openjdk : [Revision #f1a8e1c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f1a8e1c) 2015-12-05
  * delete test with race condition
    * [Revision #b597835](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b597835) 2015-12-05
    * [Revision #9494c97](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9494c97) 2015-12-07

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
