# MariaDB Connector/J 1.3.2 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.3.2/)[Release Notes](../../1.3/mariadb-connector-j-132-release-notes.md)[Changelog](mariadb-connector-j-132-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 23 Nov 2015

For the highlights of this release, see the [release notes](../../1.3/mariadb-connector-j-132-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

## Fixes :

* [CONJ-219](https://jira.mariadb.org/browse/CONJ-219) : Correcting Datasource parameter handling. [Revision #da75bf7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/da75bf7) 2015-11-19
* [CONJ-221](https://jira.mariadb.org/browse/CONJ-221) : preparedStatement : Error when using statement setObject(int, object, sqlType) with object with Long type and sql type Types.BIGINT. [Revision #d757fad](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d757fad) 2015-11-19
* [CONJ-220](https://jira.mariadb.org/browse/CONJ-220) : prepareStatement : setCharacterStream and setBlob possible IndexOutOfBoundsException depending on stream length. [Revision #71e319c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/71e319c) 2015-11-20
* [CONJ-223](https://jira.mariadb.org/browse/CONJ-223) : MetaData.getParameterCount() on prepareStatement now return correct result. [Revision #76cfdfe](https://github.com/mariadb-corporation/mariadb-connector-j/commit/76cfdfe) 2015-11-22
* [CONJ-222](https://jira.mariadb.org/browse/CONJ-222) : INSERT ... SELECT are now not rewritten when option rewriteBatchedStatements is set. [Revision #39286a8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/39286a8) 2015-11-22
* Code cleaned to avoid a connection leak
  * [Revision #7900eb9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7900eb9) 2015-11-19
  * [Revision #4cc3c04](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4cc3c04) 2015-11-20
  * [Revision #ba100f3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ba100f3) 2015-11-22

## Misc :

* various test improvements
  * caching maven dependency : [Revision #f76d42f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f76d42f) 2015-11-20
  * avoid downloading JCE for testing SSL : [Revision #aded3fb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/aded3fb) 2015-11-20
  * test code improvement : [Revision #ce02e2a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ce02e2a) 2015-11-20
  * test code improvement : [Revision #c86b0e7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c86b0e7) 2015-11-20
  * avoid race condiction when testing aurora : [Revision #5432632](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5432632) 2015-11-20
  * test correction : [Revision #38fe1bc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/38fe1bc) 2015-11-22
* clean unused code
  * [Revision #cacd7c7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cacd7c7) 2015-11-23

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
