# Connector/J 1.8.0 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/?showall=1\&tab=connectors)[Release Notes](mariadb-connector-j-180-release-notes.md)[Changelog](../changelogs/1.8/mariadb-connector-j-180-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 11 Feb 2019

MariaDB Connector/J 1.8.0 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release.

NOTE:\
MariaDB Connector/J 1.8.x version is the maintenance version for Java 7. **Support for java 6 is dropped**

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

### Evolutions

Report issue from 2.3.x 2.4.x to 1.8.0:

* \[[CONJ-675](https://jira.mariadb.org/browse/CONJ-675)] permit multiple alternative authentication methods for the same user (future [MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/connectors/java/mariadb-connector-j-18-release-notes/broken-reference/README.md) feature)
* {[CONJ-678](https://jira.mariadb.org/browse/CONJ-678)] permit indication of truststore/keystore type (JKS/PKCS12), then not relying on java default type
* \[[CONJ-378](https://jira.mariadb.org/browse/CONJ-378)] GSSAPI: client can provide SPN
* \[[CONJ-667](https://jira.mariadb.org/browse/CONJ-667)] Support MYSQL\_TYPE\_JSON datatype
* \[[CONJ-652](https://jira.mariadb.org/browse/CONJ-652)] faster results buffering socket available
* \[[CONJ-659](https://jira.mariadb.org/browse/CONJ-659)] improve text performance reading date/time/timestamp resultset
* \[[CONJ-670](https://jira.mariadb.org/browse/CONJ-670)] ability to Refresh SSL certificate
* \[[CONJ-642](https://jira.mariadb.org/browse/CONJ-642)] disable the option "useBulkStmts" by default

### Minor changes

* \[[CONJ-628](https://jira.mariadb.org/browse/CONJ-628)] optimization to read metadata faster
* \[[CONJ-637](https://jira.mariadb.org/browse/CONJ-637)] java.sql.Driver class implement DriverPropertyInfo\[] getPropertyInfo, permitting listing options on querying tools
* \[[CONJ-641](https://jira.mariadb.org/browse/CONJ-641)] update maven test dependencies for java 10 compatibility
* \[[CONJ-643](https://jira.mariadb.org/browse/CONJ-643)] PreparedStatement::getParameterMetaData always returns VARSTRING as type resulting in downstream libraries interpreting values wrongly
* \[[CONJ-623](https://jira.mariadb.org/browse/CONJ-623)] Increase connection logging when Primary node connection fails
* \[[CONJ-384](https://jira.mariadb.org/browse/CONJ-384)] Add option permit having "affected" or "found" rows

h3. Bugfixes

* \[[CONJ-646](https://jira.mariadb.org/browse/CONJ-646)] possible NullPointerException when connection lost to database using aurora configuration with one node
* \[[CONJ-672](https://jira.mariadb.org/browse/CONJ-672)] batch using multi-send can hang when using query timeout
* \[[CONJ-544](https://jira.mariadb.org/browse/CONJ-544)] disable SSL session resumption when using SSL
* \[[CONJ-589](https://jira.mariadb.org/browse/CONJ-589)] correcting Clob.length() for utf8mb4
* \[[CONJ-649](https://jira.mariadb.org/browse/CONJ-649)] datasource connectTimeout URL parameter is not honoured
* \[[CONJ-650](https://jira.mariadb.org/browse/CONJ-650)] Correction on resultset.getObject(columnName, byte\[].class) when value is NULL
* \[[CONJ-665](https://jira.mariadb.org/browse/CONJ-665)] old MySQL (<5.5.3) doesn't support utf8mb4, using utf8 on 3 bytes as connection charset by default
* \[[CONJ-671](https://jira.mariadb.org/browse/CONJ-671)] MariaDb bulk threads occupy full cpu(99%) while db connections broken
* \[[CONJ-673](https://jira.mariadb.org/browse/CONJ-673)] abording a connection while fetching a query still does read whole resultset
* \[[CONJ-669](https://jira.mariadb.org/browse/CONJ-669)] SQLSyntaxErrorException when querying on empty column name
* \[[CONJ-674](https://jira.mariadb.org/browse/CONJ-674)] make dumpQueriesOnException = false by default as per documentation
* \[[CONJ-616](https://jira.mariadb.org/browse/CONJ-616)] correction on possible NPE on getConnection when using failover configuration and master is down, not throwing a proper exception
* \[[CONJ-636](https://jira.mariadb.org/browse/CONJ-636)] Error in batch might throw a NPE and not the proper Exception
* \[[CONJ-624](https://jira.mariadb.org/browse/CONJ-624)] MariaDbPoolDataSource possible NPE on configuration getter
* \[[CONJ-622](https://jira.mariadb.org/browse/CONJ-622)] The option "connectTimeout" must take in account DriverManager.getLoginTimeout() when set
* \[[CONJ-621](https://jira.mariadb.org/browse/CONJ-621)] wrong escaping when having curly bracket in table/field name
* \[[CONJ-618](https://jira.mariadb.org/browse/CONJ-618)] Client preparestatement parsing error on escaped ' / " in query
* \[[CONJ-644](https://jira.mariadb.org/browse/CONJ-644)] small optimization when validating galera connection
* \[[CONJ-625](https://jira.mariadb.org/browse/CONJ-625)] add coverage test
* \[[CONJ-654](https://jira.mariadb.org/browse/CONJ-654)] DatabaseMetaData.getDriverName() returns connector/J with a lowercase c

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
