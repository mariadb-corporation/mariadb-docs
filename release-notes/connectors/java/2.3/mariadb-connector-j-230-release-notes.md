# Connector/J 2.3.0 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/2.3.0/)[Release Notes](mariadb-connector-j-230-release-notes.md)[Changelog](../changelogs/2.3/mariadb-connector-j-230-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 7 Sep 2018

MariaDB Connector/J 2.3.0 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

### [CONJ-398](https://jira.mariadb.org/browse/CONJ-398) Improve deadlock debugging capabilities

MariaDB has now 2 new options to permit identifying deadlock :\
New options:

| includeInnodbStatusInDeadlockExceptions | includeThreadDumpInDeadlockExceptions                                                                     |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| includeInnodbStatusInDeadlockExceptions | add "SHOW ENGINE INNODB STATUS" result to exception trace when having a deadlock exception.Default: false |
| includeThreadDumpInDeadlockExceptions   | add thread dump to exception trace when having a deadlock exception.Default: false                        |

### [CONJ-639](https://jira.mariadb.org/browse/CONJ-639) the option "enabledSslProtocolSuites" now include TLSv1.2 by default

previous default value was "TLSv1, TLSv1.1", disabling TLSv1.2 by default, due to a corrected issue ([MDEV-12190](https://jira.mariadb.org/browse/MDEV-12190)) with servers using YaSSL - not openSSL. Server error was .\
Now, the default value is "TLSv1, TLSv1.1, TLSv1.2". So TLSv1.2 can be use directly.\
Connecting MySQL community server use YaSSL without correction, and connection might result in SSLException: "Unsupported record version Unknown-0.0".

### [CONJ-642](https://jira.mariadb.org/browse/CONJ-642) disable the option "useBulkStmts" by default

Using useBulkStmts permit faster batch, but cause one major issue : Batch return -1 = SUCCESS\_NO\_INFO

Different option use this information for optimistic update, and cannot confirm if update succeed or not.\
This option still makes sense, since for big batch is way more faster, but will not be activated by default.

### Minor changes

* \[[CONJ-628](https://jira.mariadb.org/browse/CONJ-628)] optimization to read metadata faster
* \[[CONJ-637](https://jira.mariadb.org/browse/CONJ-637)] java.sql.Driver class implement DriverPropertyInfo\[] getPropertyInfo, permitting listing options on querying tools
* \[[CONJ-639](https://jira.mariadb.org/browse/CONJ-639)] enabledSslProtocolSuites does not include TLSv1.2 by default
* \[[CONJ-641](https://jira.mariadb.org/browse/CONJ-641)] update maven test dependencies for java 10 compatibility
* \[[CONJ-643](https://jira.mariadb.org/browse/CONJ-643)] PreparedStatement::getParameterMetaData always returns VARSTRING as type resulting in downstream libraries interpreting values wrongly

### Bugfixes

* \[[CONJ-616](https://jira.mariadb.org/browse/CONJ-616)] correction on possible NPE on getConnection when using failover configuration and master is down, not throwing a proper exception
* \[[CONJ-636](https://jira.mariadb.org/browse/CONJ-636)] Error in batch might throw a NPE and not the proper Exception

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
