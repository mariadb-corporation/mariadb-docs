# MariaDB Connector/J 2.7.1 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../2.7/mariadb-connector-j-271-release-notes.md)[Changelog](mariadb-connector-j-271-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 23 Nov 2020

For the highlights of this release, see the [release notes](../../2.7/mariadb-connector-j-271-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #a01e7aaa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a01e7aaa) - Merge branch 'release/2.7.1'
* [Revision #dddc1b40](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dddc1b40) - bump 2.7.1 version
* [Revision #f281de76](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f281de76) - \[misc] travis SkySQL HA testing addition
* [Revision #13c01758](https://github.com/mariadb-corporation/mariadb-connector-j/commit/13c01758) - \[misc] removing JDK 12 on travis (not available anymore)
* [Revision #090d921a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/090d921a) - \[misc] correct prepare cache statement ensuring reusing cache.
* [Revision #c26c1623](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c26c1623) - \[[CONJ-838](https://jira.mariadb.org/browse/CONJ-838)] replace 'slave' terminology by 'replica'
* [Revision #b8378d03](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b8378d03) - Merge branch 'master' into develop
* [Revision #86418697](https://github.com/mariadb-corporation/mariadb-connector-j/commit/86418697) - added osgi related packege imports for gss
* [Revision #2af5b1a2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2af5b1a2) - \[[CONJ-839](https://jira.mariadb.org/browse/CONJ-839)] batch exception message correction when with option `rewriteBatchedStatements`
* [Revision #29df5f5a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/29df5f5a) - \[misc] ensure test before will be executed before test class
* [Revision #37fde5fc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/37fde5fc) - \[misc] test correction for maxscale and SkySQL environment
* [Revision #cb926cdc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cb926cdc) - \[misc] enable load local infile test for [MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/connectors/java/changelogs/mariadb-connector-j-27-changelogs/broken-reference/README.md)+
* [Revision #d633c8df](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d633c8df) - \[[CONJ-842](https://jira.mariadb.org/browse/CONJ-842)] Byte array parameters are not send as long data
* [Revision #256fa8f1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/256fa8f1) - \[misc] added benchmark description
* [Revision #0ebe5eab](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0ebe5eab) - \[[CONJ-843](https://jira.mariadb.org/browse/CONJ-843)] ParameterMetaData::getParameterType for CallableStatement parameter BINARY type now return 'BINARY'
* [Revision #fd276551](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fd276551) - \[[CONJ-841](https://jira.mariadb.org/browse/CONJ-841)] ResultSetMetaData::getColumnTypeName() returns incorrect type name for LONGTEXT
* [Revision #bb602eb7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bb602eb7) - \[misc] test small correction
* [Revision #884e7b9c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/884e7b9c) - \[[CONJ-842](https://jira.mariadb.org/browse/CONJ-842)] Byte array parameters are not send as long data
* [Revision #8cafdf94](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8cafdf94) - \[misc] benchmark correction
* [Revision #4ed97b2e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4ed97b2e) - \[misc] adding benchmark
* [Revision #49f3d2a3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/49f3d2a3) - \[misc] permit providing test parameter from System properties
* [Revision #efb19400](https://github.com/mariadb-corporation/mariadb-connector-j/commit/efb19400) - \[[CONJ-837](https://jira.mariadb.org/browse/CONJ-837)] prepared statement cache leak on Resultset CONCUR\_UPDATABLE concurrency
* [Revision #15af61a6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/15af61a6) - \[misc] junit version bump
* [Revision #b84c27de](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b84c27de) - \[misc] appveyor server msi retrival, follow redirection
* [Revision #5c9d7fe9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5c9d7fe9) - \[[CONJ-834](https://jira.mariadb.org/browse/CONJ-834)] use of BULK is conditionned to server 10.2.7+ version, not capability
* [Revision #1646a5ff](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1646a5ff) - \[misc] small simplification of MariaXaResource XID generation
* [Revision #08779406](https://github.com/mariadb-corporation/mariadb-connector-j/commit/08779406) - set 2.7.1 SNAPSHOT version
* [Revision #8427aed6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8427aed6) - Merge tag '2.7.0' into develop

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
