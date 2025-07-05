# MariaDB Connector/J 2.0.0 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/2.0.0/)[Release Notes](mariadb-connector-j-200-release-notes.md)[Changelog](../changelogs/2.0/mariadb-connector-j-200-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 20 April 2017

MariaDB Connector/J 2.0.0-RC is a [_**RC**_](../../../mariadb-release-criteria.md) _**(Release candidate)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

**Java 8 is now minimum required version.**

### Handle CLIENT\_DEPRECATE\_EOF flag

[CONJ-318](https://jira.mariadb.org/browse/CONJ-318)\
Implement some protocol changes that permit to save some bytes.\
(part of [MDEV-8931](https://jira.mariadb.org/browse/MDEV-8931)).

### handle SERVER\_SESSION\_STATE\_CHANGE status flag

[CONJ-341](https://jira.mariadb.org/browse/CONJ-341)\
With server with version [MariaDB 10.2](../../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md), MySQL 5.7, ensure driver state :

* driver does now always get current database, even when database is changed by query.
* when using rewriteBatchedStatements does return correct autoincrement ids even when session variable @auto\_increment\_increment has change during session.

### improve setQueryTimeout to use SET STATEMENT max\_statement\_time

[CONJ-393](https://jira.mariadb.org/browse/CONJ-393)\
Previous implementation of query timeout handling (using Statement.setQueryTimeout) will create an additional thread with a scheduler.\
When timeout is reached, a temporary connection will be created to permit executing "KILL QUERY ", then closing the temporary connection.\
When query ended before timeout, the scheduled task will be canceled.

If server is > 10.1.2, query timeout will be handle server side using "SET MAX\_STATEMENT\_TIME FOR" command.

### Real cancelling Streaming result sets

[CONJ-315](https://jira.mariadb.org/browse/CONJ-315)\
When closing a Statement that was fetching a result-set (using Statement.setFetchSize) and all rows where not read at the time of closing, a kill query command will be executed on close, to avoid having to parse all remaining results.

### Memory optimization : streaming query

[CONJ-442](https://jira.mariadb.org/browse/CONJ-442)\
Very big command now doesn't use any intermediate buffer. Commands are send directly to socket avoiding using memory, This permit to send very large object (1G) without using any additional memory.

### Faster connection

[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)\
Faster connection : bundle first commands in authentication packet\
Driver execute different command on connection. Those queries are now send using pipeline (all queries are send, then only all results are reads).

New Options :

| usePipelineAuth |
| --------------- |
| usePipelineAuth |

### Performance improvement storing data in resultset

[CONJ-368](https://jira.mariadb.org/browse/CONJ-368)\
Parsing row result optimisation to avoid creating byte array to the maximum for faster results and less memory use.

### Remaining JDBC 4.2 missing implementation :

* [CONJ-414](https://jira.mariadb.org/browse/CONJ-414) - support for large update count \[[CONJ-414](https://jira.mariadb.org/browse/CONJ-414)]
* [CONJ-409](https://jira.mariadb.org/browse/CONJ-409) - PrepareStatement.setObject(...) support for with java 8 temporal object.
* [CONJ-411](https://jira.mariadb.org/browse/CONJ-411) - support for Statement maxFieldSize

### Misc

* [CONJ-443](https://jira.mariadb.org/browse/CONJ-443) - NullpointerException when making concurrent procedure calls
* [CONJ-391](https://jira.mariadb.org/browse/CONJ-391) - Improve connection using SELECT in place of SHOW to avoid creating a mutex server side.
* [CONJ-402](https://jira.mariadb.org/browse/CONJ-402) - tcpKeepAlive option now default to true.
* [CONJ-448](https://jira.mariadb.org/browse/CONJ-448) - QueryException: Incorrect arguments to mysqld\_stmt\_execute on inserting an "emptyString"-Lob with JPA
* [CONJ-451](https://jira.mariadb.org/browse/CONJ-451) - Respect type parameter of ResultSet.getObject with type
* [CONJ-455](https://jira.mariadb.org/browse/CONJ-455) - MetaData : tinyInt1isBit doesn't work properly in TINYINT(1) column that is marked as UNSIGNED
* [CONJ-450](https://jira.mariadb.org/browse/CONJ-450) - NPE on setClientInfo if value is an empty string
* [CONJ-457](https://jira.mariadb.org/browse/CONJ-457) - trustStore : Retain leading slash when trust store beings with 'file:/'
* [CONJ-160](https://jira.mariadb.org/browse/CONJ-160) - ConnectionPool test using hikariCP
* [CONJ-307](https://jira.mariadb.org/browse/CONJ-307) - valid connector java 9 early access
* [CONJ-402](https://jira.mariadb.org/browse/CONJ-402) - make tcpKeepAlive option default to true
* [CONJ-411](https://jira.mariadb.org/browse/CONJ-411) - Implement Statement maxFieldSize
* [CONJ-449](https://jira.mariadb.org/browse/CONJ-449) - Permit CallableStatement streaming

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
