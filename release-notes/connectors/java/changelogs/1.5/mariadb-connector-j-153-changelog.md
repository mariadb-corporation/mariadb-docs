# MariaDB Connector/J 1.5.3 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.3/)[Release Notes](../../1.5/mariadb-connector-j-153-release-notes.md)[Changelog](mariadb-connector-j-153-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 4 Oct 2016

For the highlights of this release, see the [release notes](../../1.5/mariadb-connector-j-153-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #ed1c4f5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ed1c4f5) - \[misc] release 1.5.3
* [Revision #236e935](https://github.com/mariadb-corporation/mariadb-connector-j/commit/236e935) - \[[CONJ-358](https://jira.mariadb.org/browse/CONJ-358)] correcting SSL certificates tests
* [Revision #edd02c9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/edd02c9) - \[[CONJ-358](https://jira.mariadb.org/browse/CONJ-358)] add option "keyPassword" to permit using private key with password that differ from keyStore password
* [Revision #9563566](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9563566) - \[[CONJ-342](https://jira.mariadb.org/browse/CONJ-342)] Empty clientCertificateKeyStoreUrl option correction \[[CONJ-356](https://jira.mariadb.org/browse/CONJ-356)] secure connection : use KeyStore private key and associate public keys certificates only
* [Revision #3b87fa2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3b87fa2) - \[misc] checkstyle correction
* [Revision #a21d179](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a21d179) - \[misc] deleting COM\_MULTI not accurate test
* [Revision #2210c07](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2210c07) - \[[CONJ-354](https://jira.mariadb.org/browse/CONJ-354)] Streaming issue when using procedures in PrepareStatement/Statement + faster Connection.prepareStatement()
* [Revision #1ba15a7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1ba15a7) - \[misc] add changelog informations
* [Revision #019b38b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/019b38b) - \[misc] adding javadoc and openJdk 1.7
* [Revision #3501460](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3501460) - \[[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)] cancelling COM\_MULTI implementation
* [Revision #26ed0fd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/26ed0fd) - \[[CONJ-352](https://jira.mariadb.org/browse/CONJ-352)] metadata correction on getPrecision() for numeric fields
* [Revision #9b6c660](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9b6c660) - \[[CONJ-351](https://jira.mariadb.org/browse/CONJ-351)] IBM JRE compatibility
* [Revision #eed86a6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eed86a6) - \[[CONJ-345](https://jira.mariadb.org/browse/CONJ-345)] Test PREPARE fallback
* [Revision #c119221](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c119221) - \[misc] ensure that new logging trace packet doesn't log authentication datas
* [Revision #f0da48e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f0da48e) - \[misc] Connection.setSchema(string) not permit now as JDBC required will silently ignore this request, not throw exception
* [Revision #02bf215](https://github.com/mariadb-corporation/mariadb-connector-j/commit/02bf215) - \[misc] changing version to 1.5.3-SNAPSHOT
* [Revision #40183b7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/40183b7) - \[misc] deallocate query using compression correction and test correction
* [Revision #b18f5a8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b18f5a8) - \[[CONJ-350](https://jira.mariadb.org/browse/CONJ-350)] Make server prepare fallback to client prepare if query cannot be prepare
* [Revision #f40876b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f40876b) - Merge branch 'feature/[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)' into develop
* [Revision #05dea4a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/05dea4a) - \[[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)] adding additional tests
* [Revision #77142e8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/77142e8) - \[[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)] checkstyle correction
* [Revision #ee33c46](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ee33c46) - \[[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)] error message correction
* [Revision #efffcc6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/efffcc6) - \[[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)] fix packet size when using compression
* [Revision #7a32338](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7a32338) - \[[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)] remove 10.2 test temporary (waiting for 10.2.2 release = beta) and minor performance improvement
* [Revision #3461c49](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3461c49) - \[[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)] COM\_MULTI text protocol correction
* [Revision #07efb85](https://github.com/mariadb-corporation/mariadb-connector-j/commit/07efb85) - \[misc] unix case correction
* [Revision #3efa05e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3efa05e) - \[misc] correction rewrite on multiple queries generatedKeys
* [Revision #a5eec72](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a5eec72) - \[[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)] test correction using same data
* [Revision #d5c11f8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d5c11f8) - \[[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)] correction logging when using binary protocol
* [Revision #53f861b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/53f861b) - Merge branch 'develop' of [mariadb-connector-j](https://github.com/MariaDB/mariadb-connector-j) into feature/[CONJ-296](https://jira.mariadb.org/browse/CONJ-296)
* [Revision #d842b77](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d842b77) - \[misc] correction buffer length for read logging
* [Revision #22f6ef4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/22f6ef4) - \[misc] batch COM\_MULTI implementation

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
