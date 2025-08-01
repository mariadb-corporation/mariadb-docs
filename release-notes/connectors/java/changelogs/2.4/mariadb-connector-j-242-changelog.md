# MariaDB Connector/J 2.4.2 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../2.4/mariadb-connector-j-242-release-notes.md)[Changelog](mariadb-connector-j-242-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 17 Jun 2019

For the highlights of this release, see the [release notes](../../2.4/mariadb-connector-j-242-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #c9a86cf7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c9a86cf7) - bump 2.4.2
* [Revision #fc4a288a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fc4a288a) - \[[CONJ-706](https://jira.mariadb.org/browse/CONJ-706)] revert correction that has to be done in 2.5.0, not in 2.4.x
* [Revision #b8721c9b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b8721c9b) - \[[CONJ-714](https://jira.mariadb.org/browse/CONJ-714)] regression connection on galera in detached state
* [Revision #8b42ad0d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8b42ad0d) - \[[CONJ-708](https://jira.mariadb.org/browse/CONJ-708)] 'failover' HA option name is misleading, correction to loadbalance Adding failover alias for compatibility
* [Revision #71d84eaa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/71d84eaa) - \[misc] correcting aurora tests
* [Revision #72dbca95](https://github.com/mariadb-corporation/mariadb-connector-j/commit/72dbca95) - \[misc] revert allowLocalInfile default change - testing change: password testing more complex for server with password complexity - localsocket test correction
* [Revision #cd98b413](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cd98b413) - \[misc] revert allowLocalInfile default change
* [Revision #4db628c4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4db628c4) - \[[CONJ-703](https://jira.mariadb.org/browse/CONJ-703)] osgi optional package correction
* [Revision #eb4326cd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eb4326cd) - \[misc] tagging 2.4.2
* [Revision #f3869d82](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f3869d82) - \[misc] removing unnecessary tar created when pushlishing artifact
* [Revision #6e60e687](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6e60e687) - \[misc] correcting test since default timeout can be set to 30s
* [Revision #9035adcd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9035adcd) - \[[CONJ-712](https://jira.mariadb.org/browse/CONJ-712)] test-cases addition
* [Revision #cb3eae0e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cb3eae0e) - \[[CONJ-712](https://jira.mariadb.org/browse/CONJ-712)] on rewritten batch (RewriteBatchedStatements), handle single query and in case of no change, return array of 0 change.
* [Revision #6be24455](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6be24455) - Update CmdInformationBatch.java
* [Revision #f9f7a22b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f9f7a22b) - Update CmdInformationBatch.java
* [Revision #aa1ade75](https://github.com/mariadb-corporation/mariadb-connector-j/commit/aa1ade75) - Update CmdInformationBatch.java
* [Revision #53ef73d4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/53ef73d4) - Update CmdInformationBatch.java
* [Revision #19a5a47c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/19a5a47c) - \[[CONJ-711](https://jira.mariadb.org/browse/CONJ-711)] Xid format correction when formatId is unsigned
* [Revision #e6d43b85](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e6d43b85) - \[[CONJ-710](https://jira.mariadb.org/browse/CONJ-710)] Throw complete stackTrace when having an exception on XA Commands
* [Revision #2878feb9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2878feb9) - \[misc] correcting failover testing on kill
* [Revision #cabf6928](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cabf6928) - \[[CONJ-700](https://jira.mariadb.org/browse/CONJ-700)] autoReconnect testing with maxscale correction
* [Revision #5f646978](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5f646978) - \[[CONJ-707](https://jira.mariadb.org/browse/CONJ-707)] failover might throw an unexpected exception with using "failover"/"sequential" configuration on socket error
* [Revision #4828841e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4828841e) - \[[CONJ-700](https://jira.mariadb.org/browse/CONJ-700)] autoReconnect option correction when no failover correcting maxAllowedPacket reconnection if error was prevented
* [Revision #c0532acd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c0532acd) - \[[CONJ-700](https://jira.mariadb.org/browse/CONJ-700)] autoReconnect option correction when no failover
* [Revision #913a912b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/913a912b) - \[[CONJ-706](https://jira.mariadb.org/browse/CONJ-706)] getGeneratedKey implementation correction for multiple result for one query
* [Revision #857debfb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/857debfb) - \[misc] fixed org.mariadb.jdbc.MariaDbConnection.includeThreadsTraces to use a right option includeThreadDumpInDeadlockExceptions (instead of includeInnodbStatusInDeadlockExceptions)
* [Revision #2f29c818](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2f29c818) - \[misc] correcting batch tests (runLongTest)
* [Revision #e02ac06c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e02ac06c) - Bug 421129: \[MariaDB Connector J] Should clear AbstractQueryProtocol::localInfileInputStream field after set MariaDbStatement.setLocalInfileInputStream if throw exception
* [Revision #e89de36b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e89de36b) - bug425232 \[MariaDB Connector J] runLongTest system property does not work
* [Revision #44d76c57](https://github.com/mariadb-corporation/mariadb-connector-j/commit/44d76c57) - \[misc] correcting appveyor configuration script (link to archive)
* [Revision #0b8eb5cc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0b8eb5cc) - \[misc] changing appveyor testing to use archive repo, to ensure that server binary is available
* [Revision #47f6285d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/47f6285d) - bug 405078 remove checking innodb\_log\_file\_size condition when decide checkMaxAllowedPacketMore

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
