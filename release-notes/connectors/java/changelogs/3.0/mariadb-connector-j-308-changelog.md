# MariaDB Connector/J 3.0.8 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../3.0/mariadb-connector-j-308-release-notes.md)[Changelog](mariadb-connector-j-308-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 20 Sep 2022

For the highlights of this release, see the[release notes](../../3.0/mariadb-connector-j-308-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #e60dd939](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e60dd939) - \[misc] parsing correction after #9a972b12
* [Revision #f5fc5632](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f5fc5632) - bump 3.0.8
* [Revision #506ab967](https://github.com/mariadb-corporation/mariadb-connector-j/commit/506ab967) - \[misc] javadoc addition
* [Revision #57a5f067](https://github.com/mariadb-corporation/mariadb-connector-j/commit/57a5f067) - \[misc] client side prepare parameter setting avoiding null check for primitive parameter
* [Revision #7b9458c0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7b9458c0) - \[misc] update mysql connector version
* [Revision #0e4dbecb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0e4dbecb) - \[[CONJ-1010](https://jira.mariadb.org/browse/CONJ-1010)] improve client side prepared parameter substitution
* [Revision #be083fe1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/be083fe1) - \[misc] test correction for NULL geometry value
* [Revision #1e5f510d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1e5f510d) - \[misc] socket flushing correction
* [Revision #9a972b12](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9a972b12) - \[misc] small performance enhancement using fastpath
* [Revision #f07e2324](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f07e2324) - \[[CONJ-1008](https://jira.mariadb.org/browse/CONJ-1008)] better default value for socket option useReadAheadInput
* [Revision #781fb1df](https://github.com/mariadb-corporation/mariadb-connector-j/commit/781fb1df) - \[misc] small performance enhancement
* [Revision #6e58d7d1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6e58d7d1) - \[misc] adding [MariaDB 10.9](../../../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md) to test suite
* [Revision #dfba0add](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dfba0add) - \[[CONJ-996](https://jira.mariadb.org/browse/CONJ-996)] ensure BatchUpdateException inherit SQLState & vendorCode from the cause SQL exception
* [Revision #ea4f4355](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ea4f4355) - \[[CONJ-1007](https://jira.mariadb.org/browse/CONJ-1007)] ensure unix socket testing depending on test configuration
* [Revision #b3193726](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b3193726) - \[[CONJ-1007](https://jira.mariadb.org/browse/CONJ-1007)] ensure not leaking unix file descriptor
* [Revision #745ba2b7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/745ba2b7) - \[[CONJ-1002](https://jira.mariadb.org/browse/CONJ-1002)] connection ignore database on second reconnection when setting database using Connection.setCatalog()
* [Revision #956e9c0c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/956e9c0c) - \[misc] ensure setCatalog(null) behavior
* [Revision #10210fe6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/10210fe6) - \[misc] test correction for windows
* [Revision #f631c4e2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f631c4e2) - \[misc] Leaking socket file descriptors when using unix domain sockets when path doesn't exist
* [Revision #55e3c2aa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/55e3c2aa) - \[misc] code style correction
* [Revision #042158d6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/042158d6) - \[[CONJ-1003](https://jira.mariadb.org/browse/CONJ-1003)] ensure testing result on test suite
* [Revision #398c3a7d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/398c3a7d) - \[[CONJ-1003](https://jira.mariadb.org/browse/CONJ-1003)] "mariadb:replication:" was always using first replica
* [Revision #78bc75eb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/78bc75eb) - \[[CONJ-1006](https://jira.mariadb.org/browse/CONJ-1006)] disabling cachePrepStmts correction for MySQL
* [Revision #f814c80d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f814c80d) - \[misc] MariaDB benchmark common test suite implementation
* [Revision #aa3ee5bb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/aa3ee5bb) - Merge branch 'develop' of [mariadb-connector-j](https://github.com/mariadb-corporation/mariadb-connector-j) into develop
* [Revision #38235f1b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/38235f1b) - \[misc] test suite stability improvement when using maxscale
* [Revision #e697ef35](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e697ef35) - \[misc] result-set array grown small improvement
* [Revision #8765f310](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8765f310) - \[misc] permit caching\_Sha256 testing on windows
* [Revision #921debb0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/921debb0) - \[[CONJ-1006](https://jira.mariadb.org/browse/CONJ-1006)] reset failover NPE when cachePrepStmts is disable
* [Revision #0f6ba26d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0f6ba26d) - \[[CONJ-1006](https://jira.mariadb.org/browse/CONJ-1006)] disabling cachePrepStmts with useServerPrepStmts might result in Exception
* [Revision #9ffd90ef](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9ffd90ef) - bump 3.0.8-SNAPSHOT
* [Revision #609fe993](https://github.com/mariadb-corporation/mariadb-connector-j/commit/609fe993) - \[[CONJ-999](https://jira.mariadb.org/browse/CONJ-999)] setting createDatabaseIfNotExist option use on read-only server will refuse connection
* [Revision #2a1f7d51](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2a1f7d51) - \[[CONJ-997](https://jira.mariadb.org/browse/CONJ-997)] test suite correction to support galera
* [Revision #5c697f4c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5c697f4c) - \[[CONJ-997](https://jira.mariadb.org/browse/CONJ-997)] correcting use of galeraAllowedState

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
