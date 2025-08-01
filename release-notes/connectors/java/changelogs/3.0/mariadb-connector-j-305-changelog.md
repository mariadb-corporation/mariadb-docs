# MariaDB Connector/J 3.0.5 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../3.0/mariadb-connector-j-305-release-notes.md)[Changelog](mariadb-connector-j-305-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 25 May 2022

For the highlights of this release, see the [release notes](../../3.0/mariadb-connector-j-305-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #43baaa01](https://github.com/mariadb-corporation/mariadb-connector-j/commit/43baaa01) update CHANGELOG
* [Revision #523e6edb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/523e6edb) Merge branch 'release/3.0.5'
* [Revision #c2f09c7d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c2f09c7d) bump 3.0.5
* [Revision #2bb83ed4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2bb83ed4) \[[CONJ-948](https://jira.mariadb.org/browse/CONJ-948)] adding a technical option 'forceTransactionEnd' to force ROLLBACK/COMMIT commands when not needed
* [Revision #0609c6d9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0609c6d9) \[[CONJ-964](https://jira.mariadb.org/browse/CONJ-964)] adding 'auto' timezone possibility
* [Revision #2ba083c2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2ba083c2) \[[CONJ-950](https://jira.mariadb.org/browse/CONJ-950)] correct ResultSetMetaData.getPrecision() and getColumnType() for TINYTEXT/TEXT/MEDIUMTEXT/LONGTEXT
* [Revision #15d83210](https://github.com/mariadb-corporation/mariadb-connector-j/commit/15d83210) \[[CONJ-949](https://jira.mariadb.org/browse/CONJ-949)] adding mysql TLS client option aliases
* [Revision #5ec75795](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5ec75795) \[misc] remove incorrect public interface
* [Revision #1faa2dcd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1faa2dcd) \[misc] correct test certificates change
* [Revision #0cef81d1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0cef81d1) \[misc] correct cipher limitation test
* [Revision #a6972bad](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a6972bad) \[[CONJ-967](https://jira.mariadb.org/browse/CONJ-967)] callable statement clearParameters() doesn't take in account OUTPUT parameters
* [Revision #89788261](https://github.com/mariadb-corporation/mariadb-connector-j/commit/89788261) \[[CONJ-969](https://jira.mariadb.org/browse/CONJ-969)] statement toString implementation to permit logging purposes
* [Revision #25252fb1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/25252fb1) \[[CONJ-965](https://jira.mariadb.org/browse/CONJ-965)] better error message when not loading serverSslCert file
* [Revision #396ca4a0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/396ca4a0) \[misc] ensure load balance tests for long connections
* [Revision #78e1f694](https://github.com/mariadb-corporation/mariadb-connector-j/commit/78e1f694) \[[CONJ-954](https://jira.mariadb.org/browse/CONJ-954)] support java.time.OffsetDateTime parameters
* [Revision #db861084](https://github.com/mariadb-corporation/mariadb-connector-j/commit/db861084) \[[CONJ-961](https://jira.mariadb.org/browse/CONJ-961)] ensure test statibility (checking @@local\_infile);
* [Revision #2fb59093](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2fb59093) \[[CONJ-961](https://jira.mariadb.org/browse/CONJ-961)] revert allowLocalInfile default for compatibility \* allowLocalInfile default to true \* improve error message when LOAD LOCAL infile command is issued and connector configuration disabled it (allowLocalInfile=fals\
  e) \* ensure that when LOCAL\_INFILE is request by server, command is a LOCAL INFILE command, with file name validation when possible
* [Revision #b7390f71](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b7390f71) \[misc] ensure codec return correct classname
* [Revision #3d777d0e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3d777d0e) \[[CONJ-959](https://jira.mariadb.org/browse/CONJ-959)] support java.time.Instant type
* [Revision #51888054](https://github.com/mariadb-corporation/mariadb-connector-j/commit/51888054) \[[CONJ-962](https://jira.mariadb.org/browse/CONJ-962)] resultset for negative TIME value return erronous LocalDateTime values\
  b939693d \[misc] xpand testing improvement
* [Revision #e15fa25a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e15fa25a) \[[CONJ-956](https://jira.mariadb.org/browse/CONJ-956)] ArrayIndexOutOfBoundsException when alias length > 250
* [Revision #bb30bc30](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bb30bc30) \[[CONJ-958](https://jira.mariadb.org/browse/CONJ-958)] When multiple host without failover prefix, ensure connecting to all host until successfully establish a connection
* [Revision #0231bb7c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0231bb7c) \[[CONJ-947](https://jira.mariadb.org/browse/CONJ-947)] Timestamp encoding loose microsecond precision
* [Revision #01f5a0c3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/01f5a0c3) \[misc] test addition for numeric zerofill
* [Revision #57fd3f36](https://github.com/mariadb-corporation/mariadb-connector-j/commit/57fd3f36) \[misc] ensure windows test stability
* [Revision #953bf303](https://github.com/mariadb-corporation/mariadb-connector-j/commit/953bf303) bump SNAPSHOT version
* [Revision #6f38ec45](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6f38ec45) Merge branch 'master' into develop
* [Revision #95ff722e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/95ff722e) Merge tag '3.0.4' into develop

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
