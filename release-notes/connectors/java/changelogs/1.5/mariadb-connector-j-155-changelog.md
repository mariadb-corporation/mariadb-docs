# MariaDB Connector/J 1.5.5 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.5/)[Release Notes](../../1.5/mariadb-connector-j-155-release-notes.md)[Changelog](mariadb-connector-j-155-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 9 Nov 2016

For the highlights of this release, see the [release notes](../../1.5/mariadb-connector-j-155-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #28d17a3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/28d17a3) - Merge remote-tracking branch 'origin/master'
* [Revision #015a2ae](https://github.com/mariadb-corporation/mariadb-connector-j/commit/015a2ae) - \[misc] checkstyle correction + version tag
* [Revision #6444c43](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6444c43) - Merge pull request #91 from nokia/bug/[CONJ-362](https://jira.mariadb.org/browse/CONJ-362)
* [Revision #27146f6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/27146f6) - \[misc] changing version to 1.5.5
* [Revision #58aefef](https://github.com/mariadb-corporation/mariadb-connector-j/commit/58aefef) - \[[CONJ-386](https://jira.mariadb.org/browse/CONJ-386)] add test that reproduced hang on aurora using useBatchMultiSendOption
* [Revision #a30783c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a30783c) - \[[CONJ-386](https://jira.mariadb.org/browse/CONJ-386)] disabling useBatchMultiSend option for Aurora
* [Revision #12f0b06](https://github.com/mariadb-corporation/mariadb-connector-j/commit/12f0b06) - \[[CONJ-383](https://jira.mariadb.org/browse/CONJ-383)] handle OldAuthSwitchRequest
* [Revision #1c90aa6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1c90aa6) - \[misc] adding connection thread id when throwing exception
* [Revision #4a641bd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4a641bd) - Merge branch 'feature/[CONJ-381](https://jira.mariadb.org/browse/CONJ-381)' into develop
* [Revision #0d61c3a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0d61c3a) - \[[CONJ-381](https://jira.mariadb.org/browse/CONJ-381)] correcting test for mysql compatibility
* [Revision #6190081](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6190081) - \[[CONJ-385](https://jira.mariadb.org/browse/CONJ-385)] stored procedure call getUpdateCount() regression
* [Revision #a4eeb01](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a4eeb01) - \[misc] SSL request packet follow protocol description
* [Revision #6d016c1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6d016c1) - \[[CONJ-337](https://jira.mariadb.org/browse/CONJ-337)] correcting appveyor badge
* [Revision #76b87e9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/76b87e9) - \[misc] permitting local infile tests on windows and unix
* [Revision #c2c0b7f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c2c0b7f) - \[misc] simplify local infile test
* [Revision #2dfd490](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2dfd490) - \[[CONJ-337](https://jira.mariadb.org/browse/CONJ-337)] Change jna exception catch to prevent maven jna multiple version incompatibility
* [Revision #92c7ac2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/92c7ac2) - \[[CONJ-337](https://jira.mariadb.org/browse/CONJ-337)] add github appveyor badge
* [Revision #de90faa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/de90faa) - \[misc] handling case of jna is present, but not jna-platform when used on windows
* [Revision #ac91863](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ac91863) - Merge branch 'feature/[CONJ-337](https://jira.mariadb.org/browse/CONJ-337)' into develop
* [Revision #a8f8ab9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a8f8ab9) - \[[CONJ-382](https://jira.mariadb.org/browse/CONJ-382)] avoid connection leak if max\_connections is reached
* [Revision #cd96e6c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cd96e6c) - \[[CONJ-381](https://jira.mariadb.org/browse/CONJ-381)] metadata precision, scale and length correction
* [Revision #4a52270](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4a52270) - \[[CONJ-379](https://jira.mariadb.org/browse/CONJ-379)] Metadata TINYTEXT type return wrong (Types.LONGVARCHAR instead of Types.VARCHAR)
* [Revision #e6c3b02](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e6c3b02) - \[[CONJ-375](https://jira.mariadb.org/browse/CONJ-375)] LOAD DATA LOCAL INFILE correction using compression when compression ratio isn't reached
* [Revision #04830c5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/04830c5) - \[misc] checkStyle correction
* [Revision #01ad520](https://github.com/mariadb-corporation/mariadb-connector-j/commit/01ad520) - \[[CONJ-375](https://jira.mariadb.org/browse/CONJ-375)] LOAD DATA LOCAL INFILE correction for file length > 16mb
* [Revision #3180799](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3180799) - \[[CONJ-376](https://jira.mariadb.org/browse/CONJ-376)] Permit protocol compression only if server permit it - mascale compatibility
* [Revision #ade39ab](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ade39ab) - \[[CONJ-337](https://jira.mariadb.org/browse/CONJ-337)] checkStyle correction
* [Revision #566e81e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/566e81e) - \[[CONJ-337](https://jira.mariadb.org/browse/CONJ-337)] add appveyor CI
* [Revision #441ce87](https://github.com/mariadb-corporation/mariadb-connector-j/commit/441ce87) - Fixing NPE due to incorrect use of CopyOnWriteArrayList
* [Revision #73071ec](https://github.com/mariadb-corporation/mariadb-connector-j/commit/73071ec) - Merge branch 'feature/[CONJ-370](https://jira.mariadb.org/browse/CONJ-370)' into develop
* [Revision #32e49de](https://github.com/mariadb-corporation/mariadb-connector-j/commit/32e49de) - Merge branch 'develop' into feature/[CONJ-370](https://jira.mariadb.org/browse/CONJ-370)
* [Revision #708c011](https://github.com/mariadb-corporation/mariadb-connector-j/commit/708c011) - Merge branch 'feature/[CONJ-369](https://jira.mariadb.org/browse/CONJ-369)' into develop
* [Revision #4ff3402](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4ff3402) - \[[CONJ-369](https://jira.mariadb.org/browse/CONJ-369)] correction for 10.2 server compatibility
* [Revision #1e1bafb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1e1bafb) - \[[CONJ-369](https://jira.mariadb.org/browse/CONJ-369)] Encoding correction on clob column with useServerPrepStmts set to true
* [Revision #7c1fa1b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7c1fa1b) - \[[CONJ-370](https://jira.mariadb.org/browse/CONJ-370)] SSL coherence : use KeyStore default property when not using keyStore option
* [Revision #ba35d54](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ba35d54) - \[misc] better memory release for result set, avoiding the need of major garbage collection
* [Revision #a69ab38](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a69ab38) - \[misc] minor performance improvement reading BIGINT with getInt() / getLong()
* [Revision #df2bbb7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/df2bbb7) - \[misc] add more informative message for streaming result set
* [Revision #45bc83c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/45bc83c) - \[misc] revert correction for BigInt parsing
* [Revision #bb0276f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bb0276f) - \[misc] minor performance improvement
* [Revision #7f44c9a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7f44c9a) - \[documentation] improve resultSet streaming description
* [Revision #41899a4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/41899a4) - Merge branch 'develop' of [mariadb-connector-j](https://github.com/MariaDB/mariadb-connector-j) into develop
* [Revision #4cc5513](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4cc5513) - Merge pull request #89 from lhost/develop

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
