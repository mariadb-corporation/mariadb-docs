# MariaDB Connector/J 1.3.5 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.3.5/)[Release Notes](../../1.3/mariadb-connector-j-135-release-notes.md)[Changelog](mariadb-connector-j-135-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 09 Feb 2016

For the highlights of this release, see the [release notes](../../1.3/mariadb-connector-j-135-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

### Major

* [CONJ-243](https://jira.mariadb.org/browse/CONJ-243) : correction getString on tinyInt false value. [Revision #01ff2ef](https://github.com/mariadb-corporation/mariadb-connector-j/commit/01ff2ef) 2016-01-12

### Minor

* failover : Assure connection when a failover append during connection initialization : [Revision #9f0b051](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9f0b051) 2016-01-12
* [CONJ-245](https://jira.mariadb.org/browse/CONJ-245): Check connection status before executing query
  * [Revision #d6581e8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d6581e8) 2016-01-12
  * [Revision #7851cf1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7851cf1) 2016-01-13
* Connection.prepareStatement() taking column indexes or names return generated keys [Revision #6d84426](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6d84426) 2016-01-12

## Behavior change

* [CONJ-246](https://jira.mariadb.org/browse/CONJ-246): permit aurora single node cluster. [Revision #336eca8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/336eca8) 2016-01-12

## Misc

* test correction :
  * [Revision #51d5797](https://github.com/mariadb-corporation/mariadb-connector-j/commit/51d5797) 2016-01-12
  * [Revision #e6675e9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e6675e9) 2016-01-13

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
