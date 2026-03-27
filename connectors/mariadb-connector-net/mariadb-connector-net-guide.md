# MySqlConnector - Recommended ADO.NET Connector for MariaDB

**MySqlConnector is the recommended ADO.NET connector for MariaDB Server.** MySqlConnector is a community-maintained open-source project that provides the best performance, reliability, and compatibility with MariaDB products. 


MySqlConnector is an ADO.NET data provider with support for MariaDB Server. It is licensed under the [MIT License](../mariadb-connector-python/license.md).

* [Installation via NuGet](https://www.nuget.org/packages/MySqlConnector/)
* [Documentation](https://mysql-net.github.io/MySqlConnector/)
* [Version History](https://mysql-net.github.io/MySqlConnector/overview/version-history/)
* [GitHub](https://github.com/mysql-net/MySqlConnector/)
* [On Travis](https://travis-ci.org/mysql-net/MySqlConnector/pull_requests/)

### MariaDB Contributions


#### Recent Major Contributions
* Support [zero-configuration SSL](https://mariadb.org/mission-impossible-zero-configuration-ssl/) with MariaDB: [#1500](https://github.com/mysql-net/MySqlConnector/pull/1500)
  * For MariaDB Server 11.4+
  * Available from version [2.4.0](https://github.com/mysql-net/MySqlConnector/releases/tag/2.4.0)
* Rewrite server redirection logic based on latest MariaDB specification: [#1499](https://github.com/mysql-net/MySqlConnector/pull/1499)
  * For MariaDB Server 11.3+
  * Available from version [2.4.0](https://github.com/mysql-net/MySqlConnector/releases/tag/2.4.0)
* Performance: Avoid SET NAMES commands when not necessary: [#1497](https://github.com/mysql-net/MySqlConnector/pull/1497)
  * For MariaDB Server 11.5+
  * Available from version [2.4.0](https://github.com/mysql-net/MySqlConnector/releases/tag/2.4.0)
* Ensure correct foreign key query using join with table name: [#1600](https://github.com/mysql-net/MySqlConnector/pull/1600), [#1601](https://github.com/mysql-net/MySqlConnector/pull/1601)

#### Performance Optimizations
* Implement faster parsing for result sets with multiple rows: [#1330](https://github.com/mysql-net/MySqlConnector/pull/1330)
* Support per-query variables for CommandBehavior.SchemaOnly and SingleRow: [#1312](https://github.com/mysql-net/MySqlConnector/pull/1312)
* Support skipping metadata for prepared statements with [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106) and later: [#1301](https://github.com/mysql-net/MySqlConnector/pull/1301)
* Available from version [2.3.0](https://github.com/mysql-net/MySqlConnector/releases/tag/2.3.0)
* Small parameter encoding improvements: [#1293](https://github.com/mysql-net/MySqlConnector/pull/1293), [#1294](https://github.com/mysql-net/MySqlConnector/pull/1294), [#1295](https://github.com/mysql-net/MySqlConnector/pull/1295), [#1296](https://github.com/mysql-net/MySqlConnector/pull/1296)

#### Timeout and Command Improvements
* Query timeout using per query variables: [#1304](https://github.com/mysql-net/MySqlConnector/pull/1304)
* Command timeout implementation improvement: [#1336](https://github.com/mysql-net/MySqlConnector/pull/1336)
* Various timeout improvements: [#1337](https://github.com/mysql-net/MySqlConnector/pull/1337)

#### Authentication and Protocol Support
* Support [MariaDB GSSAPI authentication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi): [#577](https://github.com/mysql-net/MySqlConnector/pull/577)
  * Available from version [0.47.0](https://github.com/mysql-net/MySqlConnector/releases/tag/0.47.0)
* Permit multi-authentication: [#1303](https://github.com/mysql-net/MySqlConnector/pull/1303)
* Add a client parameter to specify SSL version(s): [#450](https://github.com/mysql-net/MySqlConnector/pull/450)

#### Version Compatibility
* Support new MariaDB version numbers: [#1259](https://github.com/mysql-net/MySqlConnector/issues/1259)
  * For MariaDB Server 11.0+
  * Available from version [2.2.6](https://github.com/mysql-net/MySqlConnector/releases/tag/2.2.6)
* MariaDB version parsing evolution: [#1311](https://github.com/mysql-net/MySqlConnector/pull/1311)
* Permit real prepared stored procedure: [#1314](https://github.com/mysql-net/MySqlConnector/pull/1314)

{% @marketo/form formId="4316" %}
