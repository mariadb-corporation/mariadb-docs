---
description: >-
  Complete MariaDB Connector/J guide for Java. Complete JDBC driver reference
  for connections, prepared statements, and transactions for production use.
---

# About MariaDB Connector/J Guide

## What is MariaDB Connector/J?

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/cE4eh1fj6G5Yt6gTKoau/" %}

<p align="center"><a href="https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector/" class="button primary">Download MariaDB Connector/J</a> <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/java/all-releases" class="button secondary">List of MariaDB Connector/J Releases</a></p>

MariaDB Connector/J is used to connect applications developed in Java to MariaDB and MySQL databases using the standard JDBC API. The library is LGPL licensed.

MariaDB Connector/J is a Type 4 JDBC driver. It was developed specifically as a lightweight JDBC connector for use with MariaDB and MySQL database servers. It was originally based on the Drizzle JDBC code with numerous additions and bug fixes.

### Server Compatibility

MariaDB Connector/J is compatible with all MariaDB and MySQL server versions.

{% hint style="info" %}
MariaDB Connector/J releases older than 1.2.0 may be compatible with server versions older than MySQL 5.5, but those MariaDB Connector/J releases aren't supported anymore.
{% endhint %}

### Java Compatibility

To determine which MariaDB Connector/J release series would be best to use for each Java version, please see the following table:

| Java Version(s)                            | Recommended MariaDB Connector/J Release Series                                | JDBC Version |
| ------------------------------------------ | ----------------------------------------------------------------------------- | ------------ |
| Java 25, Java 21, Java 17                  | MariaDB Connector/J 4.0                                                       | JDBC 4.5     |
| Java 25, Java 21, Java 17, Java 11, Java 8 | MariaDB Connector/J 3.5, 3.4, 3.3\[1] | JDBC 4.5     |

1. see parsec authentication restriction

MariaDB Connector/J 4.0 requires Java 17 or later. Applications that run on Java 8 or Java 11 must use the 3.x release series.

## Installing MariaDB Connector/J

MariaDB Connector/J can be installed using [Maven](https://maven.apache.org/what-is-maven.html), [Gradle](https://gradle.org/), or by manually putting the `.jar` file in your [CLASSPATH](https://docs.oracle.com/javase/tutorial/essential/environment/paths.html). See [Installing MariaDB Connector/J](../installing-mariadb-connectorj.md) for more information.

MariaDB Connector/J `.jar` files and source code tarballs can be downloaded from the following URL:

* [#jar](https://mariadb.com/downloads/#connectors)
* [#source tar](https://github.com/mariadb-corporation/mariadb-connector-j/releases)
* [#github](https://github.com/mariadb-corporation/mariadb-connector-j/)

### Installing Dependencies

MariaDB Connector/J 4.0 has no required dependency: Unix domain sockets and Windows named pipes use the JDK implementation.

With MariaDB Connector/J 3.x, JNA (net.java.dev.jna:jna) and JNA-PLATFORM (net.java.dev.jna:jna-platform) 4.2.1 or greater are also needed when you would like to connect to the server with Unix sockets or windows pipes.

## Using the Driver

The following subsections show the formatting of JDBC connection strings for MariaDB and MySQL database servers. Additionally, sample code is provided that demonstrates how to connect to one of these servers and create a table.

## Getting a New Connection

There are two standard ways to get a connection:

### **Using DriverManager**

The preferred way to get a connection with MariaDB Connector/J is to use the [DriverManager](https://docs.oracle.com/javase/8/docs/api/java/sql/DriverManager.html) class.\
When the `DriverManager` class is used to locate and load MariaDB Connector/J, the application needs no further configuration. The `DriverManager` class will automatically load MariaDB Connector/J and allow it to be used in the same way as any other JDBC driver.

For example:

```java
Connection connection = DriverManager.getConnection("jdbc:mariadb://localhost:3306/DB?user=root&password=myPassword");
```

{% hint style="info" %}
The legacy way of loading a JDBC driver also still works for MariaDB Connector/J. e.g.: `Class.forName("org.mariadb.jdbc.Driver")`
{% endhint %}

#### **jdbc:mysql scheme compatibility**

MariaDB Connector/J 3.0 only accepts `jdbc:mariadb:` as the protocol in connection strings by default. When both MariaDB Connector/J and the MySQL drivers are found in the class-path, using `jdbc:mariadb:` as the protocol helps to ensure that Java chooses MariaDB Connector/J.

Connector/J still allows `jdbc:mysql:` as the protocol in connection strings when the `permitMysqlScheme` option is set. For example:

`jdbc:mysql://HOST/DATABASE?permitMysqlScheme`

(2.x version did permit connection URLs beginning with both `jdbc:mariadb` and `jdbc:mysql`)

### **Using a Pool**

Another way to get a connection with MariaDB Connector/J is to use a connection pool.

MariaDB Connector/J provides 2 different Datasource pool implementations:

* `MariaDbDataSource`: The basic implementation. It creates a new connection each time the `getConnection()` method is called.
* `MariaDbPoolDataSource`: A connection pool implementation. It maintains a pool of connections, and when a new connection is requested, one is borrowed from the pool.

#### **Internal Pool**

The driver's internal pool configuration provides a very fast pool implementation and deals with the issues most of the java pool have:

* 2 different connection states cleaning after release
* deals with non-activity (connections in the pool will be released if not used after some time, avoiding the issue created when the server closes the connection after @wait\_timeout is reached).

See the [pool documentation](../pool-datasource-implementation.md) for more information.

#### **External pool**

When using an external connection pool, the MariaDB Driver class `org.mariadb.jdbc.Driver` must be configured.

Example using hikariCP JDBC connection pool :

```java
final HikariDataSource ds = new HikariDataSource();
        ds.setMaximumPoolSize(20);
        ds.setDriverClassName("org.mariadb.jdbc.Driver");
        ds.setJdbcUrl("jdbc:mariadb://localhost:3306/db");
        ds.addDataSourceProperty("user", "root");
        ds.addDataSourceProperty("password", "myPassword");
        ds.setAutoCommit(false);
```

Please note that the driver class provided by MariaDB Connector/J **is not `com.mysql.jdbc.Driver` but `org.mariadb.jdbc.Driver`**!

The `org.mariadb.jdbc.MariaDbDataSource` class can be used when the pool datasource configuration only permits the java.sql.Datasource implementation.

## Connection Strings

The format of the JDBC connection string is:

```java
jdbc:mariadb:[replication:|loadbalance:|sequential:|load-balance-read:]//<hostDescription>[,<hostDescription>...]/[database][?<key1>=<value1>[&<key2>=<value2>]]
```

HostDescription:

```java
<host>[:<portnumber>]  or address=(host=<host>|localSocket=<socket>|pipe=<namedpipe>)[(port=<portnumber>)][(type=(master|replica|slave))][(sslMode=disable|trust|verify-ca|verify-full|allow)]
```

Some notes about this:

* The host must be a DNS name or IP address.
* If the host is an IPv6 address, then it must be inside square brackets.
* The default port is `3306`.
* The default type is `master`.
* If the failover and load-balancing mode is set to `replication`, then the connector assumes that the first host is master, and the others are replicas by default, if their types are not explicitly mentioned.
* aurora failover prefix is available on 2.x version.
* A detailed host description option supersedes a global option description
* sslMode, pipe and localSocket are available since 3.4.1 version
* the `allow` sslMode value is available since 3.5.11 and 4.0.0
* Before 4.0.0, when a host name resolves to several addresses, the connector tries only one of them: the first address the JVM returns, which is an IPv4 address by default, or an IPv6 address when the JVM runs with `-Djava.net.preferIPv6Addresses=true`. If that address is unreachable, for example because IPv4 traffic is blocked, the connection to that host fails without trying the other addresses. Since 4.0.0, the connector tries each resolved address in turn, starting with the address that last connected, within the [connectTimeout](connection-parameters.md#connecttimeout) budget.

Examples:

* `localhost:3306`
* `[2001:0660:7401:0200:0000:0000:0edf:bdd7]:3306`
* `somehost.com:3306`
* `address=(host=localhost)(port=3306)(type=master)`

The `jdbc:mariadb:sequential:address=(localSocket=/socket)(sslMode=disable),10.0.0.1:3306/DB?sslMode=verify-full` connection string will permit to connect to local unix socket if available, or to host 10.0.0.1 using SSL if not.

## Failover and Load-Balancing Modes

Failover and Load-Balancing Modes were introduced in [MariaDB Connector/J 1.2.0.](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.0)

### **sequential**

* Description: This mode supports connection failover in a multi-master environment, such as MariaDB Galera Cluster. This mode does not support load-balancing reads on replicas. The connector will try to connect to hosts in the order in which they were declared in the connection URL, so the first available host is used for all queries.

For example, let's say that the connection URL is the following: `jdbc:mariadb:sequential:host1,host2,host3/testdb`When the connector tries to connect, it will always try host1 first. If that host is not available, then it will try host2. etc. When a host fails, the connector will try to reconnect to hosts in the same order.

* Introduced: 1.3.0

### **loadbalance**

* Description: This mode supports connection load-balancing in a multi-master environment, such as MariaDB Galera Cluster. This mode does not support load-balancing reads on replicas. The connector performs load-balancing for all queries by randomly picking a host from the connection URL for each connection, so queries will be load-balanced as a result of the connections getting randomly distributed across all hosts. Before 2.4.2, this option was named `failover` - alias still exist for compatibility -
* Introduced: 1.2.0

### **replication**

* Description: This mode supports connection failover in a primary-replica environment, such as a MariaDB Replication cluster. The mode supports environments with one or more masters. This mode does support load-balancing reads on replicas if the connection is set to read-only before executing the read. The connector performs load-balancing by randomly picking a replica from the connection URL to execute read queries for a connection
* Introduced: 1.2.0

### **load-balance-read**

* Description: When running a multi-master cluster (i.e. Galera), writing to more than one node can lead to optimistic locking errors ("deadlocks"). Writing concurrently to multiple nodes also doesn't bring a whole lot of performance, due to having to (synchronously) replicate to all nodes anyway. This mode supports connection failover in a multi-master environment, such as MariaDB Galera Cluster. This mode does support load-balancing reads on replicas. The connector will try to connect to primary hosts in the order in which they were declared in the connection URL, so the first available host is used for all queries.

For example, let's say that the connection URL is the following: `jdbc:mariadb:load-balance-read:primary1,primary2,address=(host=replica1)(type=replica),address=(host=replica2)(type=replica)/DB`When the connector tries to connect, it will always try primary1 first. If that host is not available, then it will try primary2. etc. When a primary host fails, the connector will try to reconnect to hosts in the same order.For replica hosts, the connector performs load-balancing for all queries by randomly picking a replica host from the connection URL for each connection, so queries will be load-balanced as a result of the connections getting randomly distributed across all replica hosts.

* Introduced: 3.5.1

### **aurora**

* Description: This mode supports connection failover in an Amazon Aurora cluster. This mode does support load-balancing reads on replica instances if the connection is set to read-only before executing the read. The connector performs load-balancing by randomly picking a replica instance to execute read queries for a connection
* Introduced: 1.2.0 and not supported anymore since 3.0 version

{% hint style="danger" %}
driver 3.0 is a complete rewrite of the connector. Specific support for aurora has not been implemented in 3.0, since it relies on pipelining. Aurora is not compatible with pipelining.\
Issues for Aurora were piling up without the community proposing any PR for them and without access for us to test those modifications. (2.x version has a 5 years support).
{% endhint %}

See [failover description](../failover-and-high-availability-with-mariadb-connector-j.md) for more information.

## Optional URL Parameters

The connection string options are described in [MariaDB Connector/J Connection Parameters](connection-parameters.md).

## JDBC API Implementation Notes

Notes on how the driver implements the JDBC API, such as time zone handling, streaming result sets, and `LOAD DATA LOCAL INFILE`, are in [MariaDB Connector/J JDBC API Implementation Notes](jdbc-api-implementation-notes.md).

## Usage Examples

The following code provides a basic example of how to connect to a MariaDB or MySQL server and create a table.

### **Creating a Table on a MariaDB or MySQL Server**

```java
Connection  connection = DriverManager.getConnection("jdbc:mariadb://localhost:3306/test", "username", "password");
Statement stmt = connection.createStatement();
stmt.executeUpdate("CREATE TABLE a (id int not null primary key, value varchar(20))");
stmt.close();
connection.close();
```

## Services

The driver can be extended with credential, authentication, and SSL factory services. See [MariaDB Connector/J Services](services.md).

## **Easy to use logging**

In MariaDB Connector/J 3.0, logging can now be enabled at runtime. Connector/J uses the slf4j API if it is installed. Otherwise, Connector/J uses the JDK logger / console.

logger name is "org.mariadb.jdbc".

Connector/J supports the following Java logging levels:

| Log Levels   | Description            |
| ------------ | ---------------------- |
| INFO         | Logs connection errors |
| DEBUG/FINE   | Logs SQL statements    |
| TRACE/FINEST | Logs network exchanges |

{% hint style="danger" %}
Be careful with "trace" level, purpose is to log all exchanges with server.\
This means huge amount of data.\
Bad configuration can lead to problems, like quickly filling the disk.
{% endhint %}

Example of configuring "trace" level on driver for logback: file logback.xml in src/main/resources/

```xml
<?xml version="1.0" encoding="UTF-8"?>

<configuration>

    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <pattern>%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <logger name="org.mariadb.jdbc" level="trace" additivity="false">
        <appender-ref ref="STDOUT"/>
    </logger>

    <root level="error">
        <appender-ref ref="STDOUT"/>
    </root>

</configuration>
```

Example of generated logs :

```
11:47:04.613 [main] TRACE o.m.j.c.socket.impl.PacketWriter - send: conn=17532 (M)
+--------------------------------------------------+
|  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+--------------------------------------------------+------------------+
| 09 00 00 00 03 53 45 4C  45 43 54 20 31          | .....SELECT 1    |
+--------------------------------------------------+------------------+

11:47:04.613 [main] TRACE o.m.j.c.socket.impl.PacketReader - read: conn=17532 (M)
+--------------------------------------------------+
|  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+--------------------------------------------------+------------------+
| 01 00 00 01 01                                   | .....            |
+--------------------------------------------------+------------------+

11:47:04.613 [main] TRACE o.m.j.c.socket.impl.PacketReader - read: conn=17532 (M)
+--------------------------------------------------+
|  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+--------------------------------------------------+------------------+
| 18 00 00 02 03 64 65 66  00 00 00 01 31 00 00 0C | .....def....1... |
| 3F 00 01 00 00 00 03 81  00 00 00 00             | ?...........     |
+--------------------------------------------------+------------------+
```

## Continuous Integration and Automated Tests

For MariaDB Connector/J's continuous integration and automated test results, please see [MariaDB Connector/J's Travis CI](https://app.travis-ci.com/github/mariadb-corporation/mariadb-connector-j).

## Reporting Bugs

If you find a bug, please report it via the [CONJ project](https://jira.mariadb.org/projects/CONJ/issues) on [MariaDB's Jira bug tracker](https://jira.mariadb.org).

## Source Code

The source code is available at the [mariadb-connector-j repository](https://github.com/MariaDB/mariadb-connector-j) on GitHub.

## License

GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

For licensing questions, see the [Licensing FAQ](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/faq/licensing-questions/licensing-faq).

## Upgrading

For the default and behavior changes between release series, see [Upgrading MariaDB Connector/J](upgrading-mariadb-connector-j.md).

## F.A.Q.

**Error "Could not read resultset: unexpected end of stream, read 0 bytes from 4"**

There is an issue communicating with the server.

Most of the time this will be caused by reading a query that has a large resultset; the server usually expects clients to read off the result set relatively quickly. The [net\_write\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#net_write_timeout) server variable controls this behavior (defaults to 60s). If the client doesn't read the whole resultset in that amount of time, the server will discard the connection.\
If you don't expect results to be handled in this amount of time there is another possibility:

* You can use the query "SET STATEMENT net\_write\_timeout=10000 FOR XXX" with XXX being your "normal" query. This will indicate that specifically for this query, [net\_write\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#net_write_timeout) will be set to a longer time (10000 in this example).
* for older servers, a specific query will have to temporarily set net\_write\_timeout ("SET STATEMENT net\_write\_timeout=..."), and set it back afterward.
* if your application usually uses a lot of long queries with fetch size, the connection can be set using the "sessionVariables=net\_write\_timeout=xxx" option.

### **How to Do a Lightweight Ping / Avoid Mass "select 1"**

* Connection.isValid() is a good approach.
* Connection.isValid() is doing a ping (ping in mysql protocol, not network ping).
* Connection pool using JDBC4 Validation are using automatically this Connection.isValid()

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
