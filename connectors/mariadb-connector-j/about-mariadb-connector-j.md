# About MariaDB Connector/J Guide

## What is MariaDB Connector/J?

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/cE4eh1fj6G5Yt6gTKoau/" %}

<p align="center"><a href="https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector/" class="button primary">Download MariaDB Connector/J</a> <a href="mariadb-connector-j-releases.md" class="button secondary">List of MariaDB Connector/J Releases</a></p>

MariaDB Connector/J is used to connect applications developed in Java to MariaDB and MySQL databases using the standard JDBC API. The library is LGPL licensed.

MariaDB Connector/J is a Type 4 JDBC driver. It was developed specifically as a lightweight JDBC connector for use with MariaDB and MySQL database servers. It was originally based on the Drizzle JDBC code with numerous additions and bug fixes.

### Server Compatibility

MariaDB Connector/J is compatible with all MariaDB and MySQL server versions.

{% hint style="info" %}
MariaDB Connector/J releases older than 1.2.0 may be compatible with server versions older than MySQL 5.5, but those MariaDB Connector/J releases aren't supported anymore.
{% endhint %}

### Java Compatibility

To determine which MariaDB Connector/J release series would be best to use for each Java version, please see the following table:

| Java Version(s)                   | Recommended MariaDB Connector/J Release Series                                | JDBC Version |
| --------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| Java 21, Java 17, Java 11, Java 8 | MariaDB Connector/J 3.5, 3.4, 3.3\[[1](about-mariadb-connector-j.md#_note-0)] | JDBC 4.2     |
| Java 17, Java 11, Java 8          | MariaDB Connector/J 2.7                                                       | JDBC 4.2     |

1. [↑](about-mariadb-connector-j.md#_ref-0) see parsec authentication restriction

## Installing MariaDB Connector/J

MariaDB Connector/J can be installed using [Maven](https://maven.apache.org/what-is-maven.html), [Gradle](https://gradle.org/), or by manually putting the `.jar` file in your [CLASSPATH](https://docs.oracle.com/javase/tutorial/essential/environment/paths.html). See [Installing MariaDB Connector/J](installing-mariadb-connectorj.md) for more information.

MariaDB Connector/J `.jar` files and source code tarballs can be downloaded from the following URL:

* [#jar](https://mariadb.com/downloads/#connectors)
* [#source tar](https://github.com/mariadb-corporation/mariadb-connector-j/releases)
* [#github](https://github.com/mariadb-corporation/mariadb-connector-j/)

### Installing Dependencies

JNA (net.java.dev.jna:jna) and JNA-PLATFORM (net.java.dev.jna:jna-platform) 4.2.1 or greater are also needed when you would like to connect to the server with Unix sockets or windows pipes.

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

See the [pool documentation](pool-datasource-implementation.md) for more information.

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

Please note that the driver class provided by MariaDB Connector/J \*\*is not `com.mysql.jdbc.Driver` but \`org.mariadb.jdbc.Driver!

The `org.mariadb.jdbc.MariaDbDataSource` class can be used when the pool datasource configuration only permits the java.sql.Datasource implementation.

## Connection Strings

The format of the JDBC connection string is:

```java
jdbc:mariadb:[replication:|loadbalance:|sequential:|load-balance-read:]//<hostDescription>[,<hostDescription>...]/[database][?<key1>=<value1>[&<key2>=<value2>]]
```

HostDescription:

```java
<host>[:<portnumber>]  or address=(host=<host>|localSocket=<socket>|pipe=<namedpipe>)[(port=<portnumber>)][(type=(master|replica|slave))][(sslMode=disable|trust|verify-ca|verify-full)]
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

Examples:

* `localhost:3306`
* `[2001:0660:7401:0200:0000:0000:0edf:bdd7]:3306`
* `somehost.com:3306`
* `address=(host=localhost)(port=3306)(type=master)`

The `jdbc:mariadb:sequential:address=(localSocket=/socket)(sslMode=disable),10.0.0.1:3306/DB?sslMode=verify-full` connection string will permit to connect to local unix socket if available, or to host 10.0.0.1 using SSL if not.

## Failover and Load-Balancing Modes

Failover and Load-Balancing Modes were introduced in [MariaDB Connector/J 1.2.0.](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes)

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

See [failover description](failover-and-high-availability-with-mariadb-connector-j.md) for more information.

## Optional URL Parameters

General remark: Unknown options are accepted and silently ignored.

The following options are currently supported.

### Essential Parameters


#### **allowLocalInfile**

* Description: Permit loading data from file. see [LOAD DATA LOCAL INFILE](about-mariadb-connector-j.md#load-data-infile). Having this option enable can impact batch performance. Disabling it can permit some batch improvement
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.2.1

#### **connectTimeout**

* Description: The connect timeout value, in milliseconds, or zero for no timeout
* Data Type: `integer`
* Default Value: `30 000`
* Introduced: 1.1.8

#### **initSql**

* Description: permit to execute commands at connection creation. Multiple commands can be passed. example: initSql=SET @myVar='YourVar';SET @myVar2='YourVar2'.
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.0.0

#### **password**

* Description: password
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.0.0

#### **user**

* Description: Username.
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.0.0

#### **useServerPrepStmts**

*   Description: The **Text protocol** (default) is a universally safe option that works reliably in all situations. The **Binary protocol** (`useServerPrepStmts=true`) can offer performance benefits, but its impact depends on whether the prepared statement cache is used:

    * **Cache miss:** Preparing before execution adds overhead, potentially causing up to \~50% performance loss.
    * **Cache hit:** Can improve performance by around 5–10%, though the gain is often small since most queries have simple execution plans.

    The actual benefit depends entirely on your query patterns.

    Starting with **MariaDB 10.6** ([MDEV-19237](https://jira.mariadb.org/browse/MDEV-19237)), the server can skip resending metadata for result-set–returning SQL commands when `useServerPrepStmts` is enabled and the metadata hasn’t changed. This eliminates unnecessary network traffic and metadata parsing, which can yield **significant improvements (around 10–30%)**—especially when metadata is large compared to the result set itself.

    **Recommendation:**\
    If you are using [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/10-6) or later and your application runs mostly repeated queries (not constantly changing), enabling the Binary protocol with `useServerPrepStmts` is generally recommended.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.3.0

### TLS Parameters

more information on [Using TLS/SSL with MariaDB java connector](using-tls-ssl-with-mariadb-java-connector.md)

#### **sslMode**

* Description: Enables SSL/TLS in a specific mode. this option replaces the deprecated options: `disableSslHostnameVerification`, `trustServerCertificat`e, `useSsl`
* Data Type: `string`
* Default Value: `disable`
* Valid Values:
  * disable: Do not use SSL/TLS (alias 'false', '0')
  * trust: Only use SSL/TLS for encryption. Do not perform certificate or hostname verification. (alias 'required')
  * verify-ca: Use SSL/TLS for encryption and perform certificates verification, but do not perform hostname verification. (alias 'verify\_ca')
  * verify-full: Use SSL/TLS for encryption, certificate verification, and hostname verification (alias 'verify\_identity', 'true', '1')
* Introduced: 3.0.0

#### **serverSslCert**

* Description: |Permits providing the server's certificate in DER form, or the server's CA certificate. The server will be added to trustStore. This permits a self-signed certificate to be trusted.Can be used in one of 3 forms : \* `serverSslCert=/path/to/cert.pem` (full path to certificate)\* `serverSslCert=classpath:relative/cert.pem` (relative to current classpath)\* or as verbatim DER-encoded certificate string "------BEGIN CERTIFICATE-----"
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.0

#### **keyStore**

* Description: File path of the keyStore file that contains the client private keycontains store and associate certificates (similar to java System property "javax.net.ssl.keyStore", but ensure that only the private key's entries are used).
* Data Type: `string`
* Default Value: `null`
* Alias: clientCertificateKeyStoreUrl
* Introduced: 1.1.1

#### **keyStorePassword**

* Description: Password for the client certificate keyStore (similar to java System property "javax.net.ssl.keyStorePassword")
* Data Type: `string`
* Default Value: `null`
* Alias: clientCertificateKeyStorePassword
* Introduced: 1.3.4

#### **enabledSslCipherSuites**

* Description: Force TLS/SSL cipher (comma separated list). Example : "`TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_DHE_DSS_WITH_AES_256_GCM_SHA384`"
* Data Type: `string`
* Default Value: `use JRE ciphers`
* Introduced: 1.5.0

#### **enabledSslProtocolSuites**

* Description: Force TLS/SSL protocol to a specific set of TLS versions (comma separated list). Example : "`TLSv1`,`TLSv1.1`,`TLSv1.2`
* Data Type: `string`
* Default Value: `use JRE default`
* Alias: enabledSSLProtocolSuites
* Introduced: 1.5.0

#### **disableSslHostnameVerification**

* Description: _deprecated, use `sslMode` instead_ When using ssl, the driver checks the hostname against the server's identity as presented in the server's certificate (checking alternative names or the certificate CN) to prevent man-in-the-middle attacks. This option permits deactivating this validation. Hostname verification is disabled when the trustServerCertificate option is set
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.1.0
* Deprecated: 3.0.0

#### **useSsl**

* Description: _deprecated, use sslMode instead_ Force [SSL/TLS on connection](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview)(useSSL can be used as alias).
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.0
* Deprecated: 3.0.0

#### **trustServerCertificate**

* Description: _deprecated, use sslMode instead_ When using SSL/TLS, do not check server's certificate
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.1
* Deprecated: 3.0.0


### Pool Parameters

See the [pool documentation](pool-datasource-implementation.md) for pool configuration.

#### **pool**

* Description: Use pool. This option is useful only if not using a DataSource object, but only a connection object
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.2.0

#### **poolName**

* Description: Pool name that permits identifying threads.default: auto-generated as MariaDb-pool-
* Data Type: `string`
* Default Value: `MariaDB-pool`
* Introduced: 2.2.0

#### **maxPoolSize**

* Description: The maximum number of physical connections that the pool should contain
* Data Type: `integer`
* Default Value: `8`
* Introduced: 2.2.0

#### **minPoolSize**

* Description: When connections are removed due to not being used for longer than "maxIdleTime", connections are closed and removed from the pool. "minPoolSize" indicates the number of physical connections the pool should keep available at all times. Should be less or equal to maxPoolSize.
* Data Type: `integer`
* Default Value: `maxPoolSize value`
* Introduced: 2.2.0

#### **poolValidMinDelay**

* Description: When asking a connection to pool, the pool will validate the connection state. "poolValidMinDelay" permits disabling this validation if the connection has been borrowed recently avoiding useless verifications in case of frequent reuse of connections. 0 means validation is done each time the connection is asked. In milleseconds.
* Data Type: `integer`
* Default Value: `1000`
* Introduced: 2.2.0

#### **maxIdleTime**

* Description: The maximum amount of time in seconds that a connection can stay in the pool when not used. This value must always be below @wait\_timeout value - 45s
* Data Type: `integer`
* Default Value: `600` minimum value is 60 seconds
* Introduced: 2.2.0

#### **useResetConnection**

* Description: When a connection is closed() (given back to pool), the pool resets the connection state. Setting this option, the prepare command will be deleted, session variables changed will be reset, and user variables will be destroyed when the server permits it (>= MySQL 5.7.3), permitting saving memory on the server if the application make extensive use of variables
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.2.0

#### **registerJmxPool**

* Description: Register JMX monitoring pools
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 2.2.0


### Infrequently Used Parameters

#### **allowMultiQueries**

* Description: permit multi-queries like `insert into ab (i) values (1); insert into ab (i) values (2)`.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.0.0

#### **allowPublicKeyRetrieval**

* Description: Authorize client to retrieve RSA server public key when serverRsaPublicKeyFile is not set (for sha256\_password and caching\_sha2\_password authentication password)
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.5.0

#### **autocommit**

* Description: Set default autocommit value on connection initialization.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 2.2.0

#### **blankTableNameMeta**

* Description: Resultset metadata getTableName always return blank. This option is mainly for ORACLE db compatibility.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.4.3

#### **cacheCallableStmts**

* Description:enable/disable callable Statement cache
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.4.0

#### **cachedCodecs**

* Description: permit to enable/disable caching of codecs (FIELD encoder/decoder).
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.5.4

#### **cachePrepStmts**

* Description: Enable caching of PREPARE commands using an LRU (Least Recently Used) cache to prevent redundant command preparation. Note that in versions prior to 3.x, this cache was only activated when the useServerPrepStmts option was enabled.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.3.0

#### **connectionAttributes**

* Description: When performance\_schema is active, permit to send server some client information in a key;value pair format (example: connectionAttributes=key1:value1,key2,value2).Those informations can be retrieved on server within tables performance\_schema.session\_connect\_attrs and performance\_schema.session\_account\_connect\_attrs.This can permit from server an identification of client/application
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.4.0

#### **connectionCollation**

* Description: Connector force `utf8mb4` charset at connection. Indicate what utf8mb4 collation to use if set. if not set, the server default collation for `utf8mb4` will be used. Useful only for the server before [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11-4), because then a better solution would be to set `character_set_collations`
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.5.0

#### **createDatabaseIfNotExist**

* Description: the specified database in the url will be created if nonexistent.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.7

#### **credentialType**

* Description: Indicate the credential plugin type to use. Plugin must be present in classpath
* Data Type: `string`
* Default Value: `null`
* Introduced: 2.5.0

#### **defaultFetchSize**

* Description: The driver will call setFetchSize(n) with this value on all newly-created Statements
* Data Type: `integer`
* Default Value: `0`
* Introduced: 2.4.2

#### **disconnectOnExpiredPasswords**

* Description: On the connection creation, indicate behavior when password is expired. When true (default) throw an expired password error. When false, the connection succeed in "sandbox" mode, only queries related to password change are allowed.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 3.5.2

#### **dumpQueriesOnException**

* Description: If set to 'true', an exception is thrown during query execution containing a query string. This is useful in development, but can lead to security issue if logs are available.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.0

#### **galeraAllowedState**

* Description: Usually, Connection.isValid just send an empty packet to server, and server send a small response to ensure connectivity. When this option is set, connector will ensure Galera server state "wsrep\_local\_state" correspond to allowed values (separated by comma). example "4,5", recommended is "4". see [galera state to know more](https://galeracluster.com/library/documentation/node-states.html#node-state-changes)
* Data Type: `string`
* Default Value: `null`
* Introduced: 2.2.5

#### **includeInnodbStatusInDeadlockExceptions**

* Description: add "SHOW ENGINE INNODB STATUS" result to exception trace when having a deadlock exception.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.3.0

#### **includeThreadDumpInDeadlockExceptions**

* Description: add thread dump to exception trace when having a deadlock exception.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.3.0

#### **localSocket**

* Description: Permits connecting to the database via Unix domain socket, if the server allows it. The value is the path of Unix domain socket (i.e "socket" database parameter : select @@socket) .
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.1.4

#### **localSocketAddress**

* Description: Hostname or IP address to bind the connection socket to a local (UNIX domain) socket.
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.1.7

#### **maxQuerySizeToLog**

* Description: Only the first characters corresponding to this options size will be displayed in logs
* Data Type: `integer`
* Default Value: `1024`
* Introduced: 1.5.0

#### **metaExportedKeys**

* Description: Possible implementation `DatabaseMetadata.getExportedKey`. Either use `INFORMATION_SCHEMA` or `SHOW CREATE TABLE` to retrieve metadata information. When set to "auto", the method will automatically choose between the `INFORMATION_SCHEMA` approach or the `SHOW CREATE` implementation based on whether the database server is running locally or remotely. Possible values: "UseInformationSchema", "UseShowCreate", or "auto".
* Data Type: `string`
* Default Value: `auto`
* Introduced: 3.5.4

#### **oldModeNoPrecisionTimestamp**

* Description: When enabled, Timestamps string representation will be compatible with 2.7's behavior (fractional part will only be displayed if required, not according to timestamp precision) .
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.5.3

#### **permitMysqlScheme**

* Description: when added to connection string, permit `jdbc:mysql:` prefix in connection string
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.0.0

#### **permitNoResults**

* Description: Indicate if Statement/PreparedStatement.executeQuery for command that produce no result will return an exception or just an empty result-set. When enabled, command not returning no data will end returning an empty result-set, when disabled, command not returning no data will end throwing an exception
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 3.5.2

#### **pinGlobalTxToPhysicalConnection**

* Description: When set, commands with a specific XID will reuse the previous connection used for this XID.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.4.1

#### **pipe**

* Description: On Windows, specify named pipe name to connect (windows equivalent of unix socket)
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.1.3

#### **prepStmtCacheSize**

* Description: When cachePrepStmts is enabled, this value indicates the prepared statement cache size.
* Data Type: `integer`
* Default Value: `250`
* Introduced: 1.3.0

#### **restrictedAuth**

* Description: permits to restrict authentication plugins (comma separated). For example, the following connection string only allows the mysql\_native\_password and client\_ed25519 client authentication plugins:`jdbc:mariadb:HOST/DATABASE?restrictedAuth=mysql_native_password,client_ed25519`. If not set, permit all authentication plugins.
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.0.0

#### **returnMultiValuesGeneratedIds**

* Description: for connector 2.x compatibility only, getGeneratedKeys() will then returns all ids of multi-value inserts. This is not compatible with galera servers
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.3.2

#### **rewriteBatchedStatements**

* Description: For insert queries, rewrite batchedStatement to execute in a single executeQuery.
    * example: 'insert into ab (i) values (?)' with first batch values = 1, second = 2 will be rewritten as 'insert into ab (i) values (1), (2)'.
    * When enabled, the `useServerPrepStmts` option will be forced to false
* Data Type: `boolean`
* Default Value: `false`
* Introduced: since 1.1.8, on 3 version since 3.5.6

#### **serverRsaPublicKeyFile**

* Description: Indicate path to RSA server public key file for sha256\_password and caching\_sha2\_password authentication password
* Data Type: `string`
* Default Value: `null`
* Introduced: 2.5.0

#### **servicePrincipalName**

* Description: When using [GSSAPI authentication](gssapi-authentication-with-mariadb-connector-j.md), use this value as the Service Principal Name (SPN) instead of the one defined for the user account on the database server.
* Data Type: `string`
* Default Value: `null`
* Introduced: 2.4.0

#### **sessionVariables**

* Description: = pairs separated by comma, mysql session variables, set upon establishing successful connection.
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.1.4

#### **socketFactory**

* Description: to use a custom socket factory, set it to the full name of the class that implements javax.net.SocketFactory
* Introduced: 1.1.0

#### **socketTimeout**

* Description: Defined the network socket timeout (SO\_TIMEOUT) in milliseconds. Value of 0 disables this timeout. If the goal is to set a timeout for all queries, the server has permitted a solution to limit the query time by setting a system variable, [max\_statement\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_statement_time). The advantage is that the connection then is still usable.
* Data Type: `integer`
* Default Value: `0`
* Introduced: 1.1.7

#### **tcpAbortiveClose**

* Description: This option can be used in environments where connections are created and closed in rapid succession. Often, it is not possible to create a socket in such an environment after a while, since all local "ephemeral" ports are used up by TCP connections in TCP\_WAIT state. Using tcpAbortiveClose works around this problem by resetting TCP connections (abortive or hard close) rather than doing an orderly close. It is accomplished by using socket.setSoLinger(true,0) for abortive close.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.1

#### **tcpKeepAlive**

* Description: Sets corresponding option on the connection socket. Default to true since 3.0.0 (was false before)
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.0.0

#### **tcpKeepCount**

* Description: Permit to set socket option TCP\_KEEPCOUNT (only if java 11+)
* Data Type: `integer`
* Default Value: `0`
* Introduced: 3.0.0

#### **tcpKeepIdle**

* Description: Permit to set socket option TCP\_KEEPIDLE (only if java 11+)
* Data Type: `integer`
* Default Value: `0`
* Introduced: 3.0.0

#### **tcpKeepInterval**

* Description: Permit to set socket option TCP\_KEEPINTERVAL (only if java 11+)
* Data Type: `integer`
* Default Value: `0`
* Introduced: 3.0.0

#### **tinyInt1isBit**

* Description: Datatype mapping flag, handle MySQL Tiny as BIT(boolean).
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.0.0

#### **tlsSocketType**

* Description: Indicate the TLS org.mariadb.jdbc.tls.TlsSocketPlugin plugin type to use. Plugin must be present in classpath
* Data Type: `string`
* Default Value: `null`
* Introduced: 2.5.0

#### **transactionReplay**

* Description: Enables transaction caching. If a failover occurs before a transaction is committed or rolled back, the transaction's cached statements are re-executed on the new primary server. Connector/J requires that applications only use idempotent queries. If the number of statements in the transaction cache exceeds transactionReplaySize, caching will be disabled until the transaction is committed or rolled back.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.0.0

#### **transactionReplaySize**

* Description: Sets the number of statements that should be saved in the transaction cache when transactionReplay is enabled.
* Data Type: `integer`
* Default Value: `64`
* Introduced: 3.0.0

#### **trustStore**

* Description: File path of the trustStore file (similar to java System property "javax.net.ssl.trustStore"). (legacy alias trustCertificateKeyStoreUrl)Use the specified file for trusted root certificates.When set, overrides serverSslCert. (see trustStorePassword in case if a jks truststore with a password)
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.5.0 (or 1.3.4 in 1.x, 2.0.0 in 2.x)

#### **trustStorePassword**

* Description: Password for the trusted root certificate file (similar to java System property "javax.net.ssl.trustStorePassword").(legacy alias trustCertificateKeyStorePassword).
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.5.0 (or 1.3.4 in 1.x, 2.0.0 in 2.x)

#### **trustStoreType**

* Description: Indicate trust store type (JKS/PKCS12). default is null, then using java default type.(legacy alias trustCertificateKeystoreType).
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.5.0 (or 2.4.0 in 2.x)

#### **useBulkStmts**

* Description: Use dedicated COM\_STMT\_BULK\_EXECUTE protocol for batch insert when possible. (batch without Statement.RETURN\_GENERATED\_KEYS and streams) to have faster batch.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 3.0.0 (was false since version >= 2.3.0)

#### **useCatalogTerm**

* Description: "schema" and "database" are server synonymous. Connector historically get/set database using Connection.setCatalog()/getCatalog(), setSchema()/getSchema() being no-op. Setting option useCatalogTerm to "schema" will change that behavior to use Schema in place of Catalog. Affected changes : database change will be done with either Connection.setCatalog()/getCatalog() or Connection.setSchema()/getSchema(), 2: DatabaseMetadata methods that use catalog or schema filtering, 3: ResultsetMetadata getCatalogName/getSchemaName
* Data Type: `string`
* Default Value: `CATALOG`
* Introduced: 3.2.0

#### **useCompression**

* Description: Compresses the exchange with the database through gzip. This permits better performance when the database is not in the same location.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.0.0

#### **useMysqlMetadata**

* Description: [databaseMetaData.getDatabaseProductName()](https://docs.oracle.com/en/java/javase/11/docs/api/java.sql/java/sql/DatabaseMetaData.html#getDatabaseProductName\(\)) return "MariaDB" or "MySQL" according to server type
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.4.0

#### **useReadAheadInput**

* Description: Use a buffered inputSteam that read socket available data
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 2.4.0

#### **usePipelineAuth**

* Description: Not compatible with aurora\*During connection, different queries are executed. When option is active those queries are send using pipeline (all queries are send, then only all results are reads), permitting faster connection creation.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.6.0

#### **yearIsDateType**

* Description: returns Year as date type, rather than numerical.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.0.0



### **Removed options**

<table><thead><tr><th width="275">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>allowMasterDownConnection</code></td><td>When the replication Failover and Load Balancing Mode is in use, allow the creation of connections when the master is down. If no masters are available, then the default connection will be a replica, and Connection.isReadOnly() will return true. Default: false. Since 2.2.0, removed in 3.0.0</td></tr><tr><td><code>interactiveClient</code></td><td>Session timeout is defined by the <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#wait_timeout">wait_timeout</a> server variable. Setting interactiveClient to true will tell the server to use the <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables">interactive_timeout</a> server variable.Default: false. Since 1.1.7</td></tr><tr><td><code>assureReadOnly</code></td><td>When this parameter is enabled, when a failover and load balancing mode is in use and a read-only connection is made to a host, ensure that this connection is in read-only mode by setting the session to read-only. Default to false. Since 1.3.0, removed in 3.0.0</td></tr><tr><td><code>autoReconnect</code></td><td>If this parameter is enabled and Failover and Load Balancing Mode is not in use, the connector will simply try to reconnect to its host after a failure. This is referred to as Basic Failover. If this parameter is enabled and Failover and Load Balancing Mode is in use, the connector will blacklist the failed host and try to connect to a different host of the same type. This is referred to as Standard Failover. Default is false.since 1.1.7, removed in 3.0.0</td></tr><tr><td><code>callableStmtCacheSize</code></td><td>This sets the number of callable statements that the driver will cache per VM if "cacheCallableStmts" is enabled.Default: true. Since 1.4.0, removed in 3.0.0</td></tr><tr><td><code>enablePacketDebug</code></td><td>Driver will save the last 16 MySQL packet exchanges (limited to first 1000 bytes). Hexadecimal value of those packets will be added to stacktrace when an IOException occur.This option has no impact on performance but driver will then take 16kb more memory.Default: false. Since 1.6.0, 2.0.1, removed in 3.0.0</td></tr><tr><td><code>failoverLoopRetries</code></td><td>When the connector is searching silently for a valid host, this parameter defines the maximum number of connection attempts the connector will make before throwing an exception.This parameter differs from the "retriesAllDown" parameter because this silent search is used in situations where the connector can temporarily workaround the problem, such as by using the master connection to execute reads when the replica connection fails.Default: 120.since 1.2.0, removed in 3.0.0</td></tr><tr><td><code>jdbcCompliantTruncation</code></td><td>Truncation error ("Data truncated for column '%' at row %", "Out of range value for column '%' at row %") will be thrown as an error, and not as a warning.Default: true. Since 1.4.0</td></tr><tr><td><code>keyPassword</code></td><td>Password for the private key in client certificate keyStore. (only needed if private key password differ from keyStore password).Since 1.5.3, removed in 3.0.0</td></tr><tr><td><code>loadBalanceBlacklistTimeout</code></td><td>When a connection fails, this host will be blacklisted for the amount of time defined by this parameter.When connecting to a host, the driver will try to connect to a host in the list of non-blacklisted hosts and, only if none are found, attempt blacklisted ones.This blacklist is shared inside the classloader.Default: 50 seconds.since 1.2.0, removed in 3.0.0</td></tr><tr><td><code>log</code></td><td>Enable log information. require Slf4j version > 1.4 dependency.Log level correspond to Slf4j logging implementationDefault: false. Since 1.5.0, removed in 3.0.0</td></tr><tr><td><code>passwordCharacterEncoding</code></td><td>Indicate password encoding charset. Charset value must be a <a href="https://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html">Java charset</a>. Example : "UTF-8" Default: null (= platform's default charset) . Since 1.5.9, removed in 3.0.0</td></tr><tr><td><code>prepStmtCacheSqlLimit</code></td><td>if useServerPrepStmts = true, defined queries larger than this size will not be cached. Default: 2048. Since 1.3.0</td></tr><tr><td><code>profileSql</code></td><td>log query execution time.Default: false. Since 1.5.0, removed in 3.0.0</td></tr><tr><td><code>slowQueryThresholdNanos</code></td><td>Will log query with execution time superior to this value (if defined )Default: 1024. Since 1.5.0, removed in 3.0.0</td></tr><tr><td><code>retriesAllDown</code></td><td>When the connector is performing a failover and all hosts are down, this parameter defines the maximum number of connection attempts the connector will make before throwing an exception.Default: 120 seconds.since 1.2.0, removed in 3.0.0</td></tr><tr><td><code>serverTimezone</code></td><td>Defines the server time zone.to use only if the jre server has a different time implementation of the server.(best to have the same server time zone when possible).since 1.1.7, removed in 3.0.0</td></tr><tr><td><code>sharedMemory</code></td><td>Permits connecting to the database via shared memory, if the server allows it. The value is the base name of the shared memory.since 1.1.4, removed in 3.0.0</td></tr><tr><td><code>staticGlobal</code></td><td>Indicates the values of the global variables <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_allowed_packet">max_allowed_packet</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#wait_timeout">wait_timeout</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#autocommit">autocommit</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables">auto_increment_increment</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#time_zone">time_zone</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#system_time_zone">system_time_zone</a> and <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tx_isolation">tx_isolation</a>) won't be changed, permitting the pool to create new connections faster.Default: false. Since 2.2.0, removed in 3.0.0</td></tr><tr><td><code>tcpNoDelay</code></td><td>Sets corresponding option on the connection socket.since 1.0.0, removed in 3.0.0</td></tr><tr><td><code>tcpRcvBuf</code></td><td>set buffer size for TCP buffer (SO_RCVBUF).since 1.0.0, removed in 3.0.0</td></tr><tr><td><code>tcpSndBuf</code></td><td>set buffer size for TCP buffer (SO_SNDBUF).since 1.0.0, removed in 3.0.0</td></tr><tr><td><code>trackSchema</code></td><td>Permit to disabled "session_track_schema" setting when server has CLIENT_SESSION_TRACK capabilityDefault: True. Since 2.5.4, removed in 3.0.0</td></tr><tr><td><code>useBatchMultiSend</code></td><td><em>Not compatible with aurora</em> Driver will can send queries by batch. If set to false, queries are sent one by one, waiting for the result before sending the next one. If set to true, queries will be sent by batch corresponding to the useBatchMultiSendNumber option value (default 100) or according to the <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_allowed_packet">max_allowed_packet</a> server variable if the packet size does not permit sending as many queries. Results will be read later, avoiding a lot of network latency when the client and server aren't on the same host. This option is mainly effective when the client is distant from the server. More information <a href="option-batchmultisend-description.md">here</a> Default: true (false if using aurora failover) . Since 1.5.0, removed in 3.0.0</td></tr><tr><td><code>useBatchMultiSendNumber</code></td><td>When option useBatchMultiSend is active, indicate the maximum query send in a row before reading results.Default: 100. Since 1.5.0</td></tr><tr><td><code>useFractionalSeconds</code></td><td>Correctly handle subsecond precision in timestamps (feature available with <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3">MariaDB 5.3</a> and later). May confuse 3rd party components (Hibernated).Default: true. Since 1.0.0</td></tr><tr><td><code>useOldAliasMetadataBehavior</code></td><td>Metadata ResultSetMetaData.getTableName() returns the physical table name. "useOldAliasMetadataBehavior" permits activating the legacy code that sends the table alias if set. Default: false. Since 1.1.9</td></tr><tr><td><code>validConnectionTimeout</code></td><td>When multiple hosts are configured, the connector verifies that the connections haven't been lost after this much time in seconds has elapsed.When this parameter is set to 0, no verification will be done. Default:120 secondssince 1.2.0, removed in 3.0.0</td></tr></tbody></table>

## JDBC API Implementation Notes

### Size consideration

GSSAPI in windows isn't well supported in java, causing recurrent issues. Since 3.1, waffle-jna is marked as a dependency to provide good GSSAPI support without problems. This has the drawback to make connector and dependencies to a size of around 4Mb.

If size is important, the dependency can be removed, the connector working great, just will have some limitation using GSSAPI on windows :

this can be done like this:

* using maven

```xml
<dependency>
	<groupId>org.mariadb.jdbc</groupId>
	<artifactId>mariadb-java-client</artifactId>
	<version>3.1.0</version>
        <exclusions>
          <exclusion>
            <groupId>com.github.waffle</groupId>
            <artifactId>waffle-jna</artifactId>
          </exclusion>
      </exclusions> 
</dependency>
```

* using graddle:

```xml
dependencies {
    implementation('org.mariadb.jdbc:mariadb-java-client:3.1.0') {
        exclude group: 'com.github.waffle', module: 'waffle-jna'
    }
}
```

### Parsec authentication

Since 3.5.1, parsec authentication is implemented in connector. This requires java 15+ (to use java native ed25519 Algorithm implementation).

In order to use parsec authentication with previous version of java, BouncyCastle is required as dependency:

```xml
<dependency>
            <groupId>org.bouncycastle</groupId>
            <artifactId>bcpkix-jdk18on</artifactId>
            <version>1.78.1</version>
        </dependency>
```

### Timezone consideration

#### **The Ideal Scenario**

The simplest approach to avoid time zone headaches is for the client and server to operate in the same time zone.

#### **Java Connector Timezone Options**

There are 3 options that control timestamps behavior in the java connector:

* connectionTimeZone: (LOCAL | SERVER | ) - This option defines the connection's time zone. LOCAL retrieves the JVM's default time zone, SERVER fetches the server's global time zone upon connection creation, and allows specifying a server time zone without requesting it during connection establishment.
* forceConnectionTimeZoneToSession: (true | false) - This setting dictates whether the connector enforces the connection time zone for the session.
* preserveInstants: (true | false) - This option controls whether the connector converts Timestamp values to the connection's time zone.

#### **Recommendation**

By default, the connector adopts the JVM's default time zone. If the client and server reside in different time zones, it's recommended to configure the connection time zone to match the JVM's default by setting forceConnectionTimeZoneToSession to true.\
This ensures proper operation of time functions.

(This isn’t the default behavior because there is a server Requirements to set tzinfo depending on the JVM's time zones)

#### **TIMESTAMP vs. DATETIME: Know the Difference**

Just like Java's Instant and LocalDateTime, server-side TIMESTAMP and DATETIME fields serve distinct purposes. One represents a specific point in time (a moment), while the other doesn't.

* TIMESTAMP: This represents an exact moment on the timeline, expressed using the connection's time zone. When stored, it gets converted to UTC (Coordinated Universal Time) for consistency. Upon retrieval, it's converted back to the connection's time zone for display.
* DATETIME: This combines date and time-of-day information but doesn't represent a specific moment.

#### **The Misuse of DATETIME:**

Due to its wider range, DATETIME is sometimes mistakenly used to store a specific point in time. While this might work if the client and server share the same time zone, it creates problems when they differ.

#### **A (Discouraged) Workaround:**

While using DATETIME instead of TIMESTAMP is generally discouraged, a specific combination of settings ("preserveInstants=true\&connectionTimeZone=SERVER") can force all Java Timestamp exchanges to be converted to the connection's time zone during storage and retrieval. However, this approach is not recommended for long-term solutions.

#### **Compatibility with Older Connectors (Pre-3.4):**

The MariaDB Connector/J versions before 3.4 offered a single "timezone" option. While this functionality remains compatible, it's now separated into two distinct settings: connectionTimeZone and forceConnectionTimeZoneToSession. Here's a breakdown of how the old option translates to the new ones:\
"timezone=America/Los\_Angeles" is equivalent to "connectionTimeZone=America/Los\_Angeles\&forceConnectionTimeZone=true

To mimic the behavior of the "useLegacyDatetimeCode=false" option from MariaDB 2.x, you can set the following combination: “connectionTimeZone=SERVER\&preserveInstants=true”

Note: Unlike the MySQL Connector, the MariaDB Connector/J defaults connectionTimeZone to LOCAL (JVM's default) instead of SERVER.

### "LOAD DATA INFILE"

{% hint style="info" %}
LOAD DATA INFILE was the fastest way to load data. Now the fastest way is the standard JDBC executeBatch() when option 'useBulkStmts' is enabled
{% endhint %}

The fastest way to load lots of data is using [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile). However, using "LOAD DATA LOCAL INFILE" (ie: loading a file from the client) may be a security problem if someone can execute a query from the client, he can have access to any file on the client (according to the rights of the user running the client process).

A specific option "allowLocalInfile" (default to true) can disable this functionality on the client side.\
The global variable [local\_infile](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#local_infile) can disable LOAD DATA LOCAL INFILE on the server side.

You can provide custom stream as well using a specific setLocalInfileInputStream

```xml
Statement statement = connection.createStatement();
        org.mariadb.jdbc.Statement mariaDbStatement =
            statement.unwrap(org.mariadb.jdbc.Statement.class);
        mariaDbStatement.setLocalInfileInputStream(in);

        String sql =
            "LOAD DATA LOCAL INFILE 'notUsed'"
                + " INTO TABLE myTable "
                + " FIELDS TERMINATED BY '\\t' ENCLOSED BY ''"
                + " ESCAPED BY '\\\\' LINES TERMINATED BY '\\n'";
        statement.execute(sql);
```

Contrary to mysql connector, `setLocalInfileInputStream` value can only be used for next execution.

### Set a Query Timeout

Driver follow the JDBC specifications, permitting `Statement.setQueryTimeout()` for a particular statement.

If the goal is to set a timeout for all queries, the server permits a [limiting query time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements) by setting the system variable [max\_statement\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_statement_time).

This solution will handle query timeout better (and faster) than java solutions (JPA2, "javax.persistence.query.timeout", Pools integrated solution like tomcat jdbc-pool "queryTimeout"...).

Option "sessionVariables" permit to set this system variable easily :\
Example :

```java
#will set a maximum query timeout of 10 seconds for this connection
jdbc:mariadb://localhost/db?user=user&sessionVariables=max_statement_time=10
```

### Streaming Result Sets

By default, `Statement.executeQuery()` will read the full result set from the server. With large result sets, this will require large amounts of memory.

To avoid using too much memory, rather use Statement.setFetchSize(int numberOfRowInMemory) to indicate the number of rows that will be stored in memory\
Example :\
using `Statement.setFetchSize(1000)` indicates that 1000 rows will be stored in memory.\
So, when the query has executed, 1000 rows will be in memory. After 1000 `ResultSet.next()`, the next 1000 rows will be stored in memory, and so on.

{% hint style="danger" %}
If another query is run on same connection while the resultset has not been completly read, the connector will fetch all remaining rows before executing the query. This can lead to still needing lots of memory. Recommendation is then to use another connection for simultaneous operations.
{% endhint %}

Note that the server usually expects clients to read off the result set relatively quickly. The [net\_write\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#net_write_timeout) server variable controls this behavior (defaults to 60s).\
If you don't expect results to be handled in this amount of time there is a different possibility:

* With you can use the query "SET STATEMENT net\_write\_timeout=10000 FOR XXX" with XXX your "normal" query. This will indicate that specifically for this query, [net\_write\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#net_write_timeout) will be set to a longer time (10000 in this example).
* for older servers, a specific query will have to temporarily set net\_write\_timeout ("SET STATEMENT net\_write\_timeout=..."), and set it back afterward.
* if your application usually uses a lot of long queries with fetch size, the connection can be set using the option "sessionVariables=net\_write\_timeout=xxx"

Even using setFetchSize, the server will send all results to the client.

If another query is executed on the same connection when a streaming resultset has not been fully read, the connector will put the whole remaining streaming resultset in memory in order to execute the next query. This can lead to OutOfMemoryError if not handled.

Before version 1.4.0, the only accepted value for fetch size was `Statement.setFetchSize(Integer.MIN_VALUE)` (equivalent to `Statement.setFetchSize(1)`). This value is still accepted for compatibility reasons, but rather use `Statement.setFetchSize(1)`, since according to JDBC the value must be >= 0.

### Prepared Statements

The driver uses server prepared statements as a standard to communicate with the database (since 1.3.0). If the "allowMultiQueries" options are set to true, the driver will only use text protocol. Prepared statements (parameter substitution) is handled by the driver, on the client side.

### CallableStatement

Callable statement implementation won't need to access the stored procedure metadata ([mysql.proc](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-proc-table)) table if both of the following are true

* CallableStatement.getMetadata() is not used
* Parameters are accessed by index, not by name

When possible, following the two rules above provides both better speed and\
eliminates concerns about SELECT privileges on the [mysql.proc](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-proc-table) table.

### Generated keys limitation

Java permit retrieving last generated keys,using [Statement.getGeneratedKeys()](https://docs.oracle.com/en/java/javase/11/docs/api/java.sql/java/sql/Statement.html#getGeneratedKeys\(\)).

Example:

```
Statement stmt = sharedConn.createStatement();
    stmt.execute(
            "INSERT INTO executeGenerated(t2) values (100)", Statement.RETURN_GENERATED_KEYS);
    ResultSet rs = stmt.getGeneratedKeys();
    rs.next();
    System.out.println(rs.getInt(1));
```

Only the first generated key will be returned, meaning that for multi-insert the generated key retrieved will correspond to the first generated value of the command.

If retrieving all generated values for multiple insert is needed, please use [INSERT...RETURNING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning) command (since [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/10-5)).

### Optional JDBC Classes

The following optional interfaces are implemented by the org.mariadb.jdbc.MariaDbDataSource class : `javax.sql.DataSource`, `javax.sql.ConnectionPoolDataSource`, `javax.sql.XADataSource`

careful : `org.mariadb.jdbc.MySQLDataSource` doesn't exist anymore and should be replaced with `org.mariadb.jdbc.MariaDbDataSource` since v1.3.0

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

The driver implements 3 kinds of services:

* Credential service: permit giving credential
* Authentication service: permit adding client authentication plugins.
* SSL factory service: custom TSL implementation

### Credential service

Credentials are usually set using user/password in the connection string or by using DriverManager.getConnection(String url, String user, String password).

Credential plugins permit to provide credential information from other means. Those plugins have to be activated setting option `credentialType` to designated plugin.

The driver has 3 default plugins :

#### **AWS IAM**

This permits AWS database IAM authentication. The plugin generate a token using IAM credential and region. Token is valid for 15 minutes and cached for 10 minutes.

To use this credential authentication, com.amazonaws:aws-java-sdk-rds dependency must be registred in classpath. Implementation use SDK `DefaultAWSCredentialsProviderChain` and `DefaultAwsRegionProviderChain` to get IAM credential and region.\
see [DefaultAWSCredentialsProviderChain](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/DefaultAWSCredentialsProviderChain.html) and [DefaultAwsRegionProviderChain](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/DefaultAWSCredentialsProviderChain.html) to check how those information can be retrieved (environment variable / system properties, files, ...)

Example: `jdbc:mariadb://host/db?credentialType=AWS-IAM&useSsl&serverSslCert=/somepath/rds-combined-ca-bundle.pem`

with `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_REGION` environment variable set.

#### **Environment**

User and Password are retrieved from environment variables. default environment variables are `MARIADB_USER` and `MARIADB_PWD`, but can be changed by setting additional option `userKey` and `pwdKey`

Example : using connection string `jdbc:mariadb://host/db?credentialType=ENV` user and password will be retrieved from environment variable `MARIADB_USER` and `MARIADB_PWD`.

#### **Property**

User and Password are retrieved from java properties. default property name are mariadb.user and mariadb.pwd, but property names can be changed by setting additional option `userKey` and `pwdKey`

Example : using connection string `jdbc:mariadb://host/db?credentialType=PROPERTY&userKey=mariadbUser&pwdKey=mariadbPwd` user and password will be retrieved from java properties `mariadbUser` and `mariadbPwd`

### Authentication service

[Client authentication plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) are now defined as services. This permits to easily add new client authentication plugins.

List of authentication plugins in java connector :

* mysql\_clear\_password
* auth\_gssapi\_client
* client\_ed25519
* mysql\_native\_password
* mysql\_old\_password
* dialog (PAM)
* sha256\_password
* caching\_sha2\_password

New authentication plugins can be created implementing interface `org.mariadb.jdbc.authentication`.`AuthenticationPlugin`, and listing new plugin in a `META-INF/services/org.mariadb.jdbc.authentication.AuthenticationPlugin` file.

### SSL factory service

Custom SSL implementation can be used implementing A connection to a server initially creates a socket. When set, SSL socket is layered over this existing socket. Implementing `org.mariadb.jdbc.tls.TlsSocketPlugin` permit to provide custom SSL implementation for example create a new [HostnameVerifier](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/net/ssl/HostnameVerifier.html) implementation.

Custom implementation need to implement `org.mariadb.jdbc.tls.TlsSocketPlugin` and register service `META-INF/services/org.mariadb.jdbc.tls.TlsSocketPlugin`

Custom implementation are activated using option `tlsSocketType`

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

Exemple of generated logs :

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

{% @marketo/form formId="4316" %}
