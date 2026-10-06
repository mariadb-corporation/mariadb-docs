---
hidden: true
description: >-
  Reference for the GridGain JDBC Thin Driver: connection strings, supported
  parameters, SSL, partition awareness, data streaming, and error codes.
---

# JDBC Driver

GridGain is shipped with JDBC drivers that allow processing of distributed data using standard SQL statements like `SELECT`, `INSERT`, `UPDATE` or `DELETE` directly from the JDBC side.

Presently, there are two drivers supported by GridGain: the lightweight and easy to use JDBC Thin Driver described in this document and [JDBC Client Driver](jdbc-client-driver.md) that interacts with the cluster by means of a [client node](https://www.gridgain.com/docs/gridgain8/latest/getting-started/concepts#clustering-servers-and-clients).

## JDBC Thin Driver

The JDBC Thin driver is a default, lightweight driver provided by GridGain. To start using the driver, just add `ignite-core-8.10.jar` to your application's classpath.

The driver connects to one of the cluster nodes and forwards all the queries to it for final execution. The node handles the query distribution and the result's aggregations. Then the result is sent back to the client application.

The JDBC connection string may be formatted with one of two patterns: `URL query` or `semicolon`:

{% code title="Connection String Syntax" %}
```text
// URL query pattern
jdbc:ignite:thin://<hostAndPortRange0>[,<hostAndPortRange1>]...[,<hostAndPortRangeN>][/schema][?<params>]

hostAndPortRange := host[:port_from[..port_to]]

params := param1=value1[&param2=value2]...[&paramN=valueN]

// Semicolon pattern
jdbc:ignite:thin://<hostAndPortRange0>[,<hostAndPortRange1>]...[,<hostAndPortRangeN>][;schema=<schema_name>][;param1=value1]...[;paramN=valueN]
```
{% endcode %}

- `host` is required and defines the host of the cluster node to connect to.
- `port_from` is the beginning of the port range to use to open the connection. 10800 is used by default if this parameter is omitted.
- `port_to` is optional. It is set to the `port_from` value by default if this parameter is omitted.
- `schema` is the schema name to access. PUBLIC is used by default. This name should correspond to the SQL ANSI-99 standard. Non-quoted identifiers are not case sensitive. Quoted identifiers are case sensitive. When semicolon format is used, the schema may be defined as a parameter with name schema.
- `<params>` are optional.

The name of the driver's class is `org.apache.ignite.IgniteJdbcThinDriver`. For instance, this is how you can open a JDBC connection to the cluster node listening on localhost:

```java
// Register JDBC driver.
Class.forName("org.apache.ignite.IgniteJdbcThinDriver");

// Open the JDBC connection.
Connection conn = DriverManager.getConnection("jdbc:ignite:thin://127.0.0.1");

```

{% hint style="info" %}
**Put the JDBC URL in quotes when connecting from bash**

Make sure to put the connection URL in double quotes (" ") when connecting from a bash environment, for example: `"jdbc:ignite:thin://[address]:[port];user=[username];password=[password]"`
{% endhint %}

### Parameters

The following table lists all the parameters that are supported by the JDBC connection string:

| Parameter | Description | Default Value |
| --- | --- | --- |
| `user` | Username for the SQL Connection. This parameter is required if authentication is enabled on the server. See the [Authentication](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication) and [CREATE user](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/ddl#create-user) documentation for more details. | ignite |
| `password` | Password for SQL Connection. Required if authentication is enabled on the server. See the [Authentication](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication) and [CREATE user](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/ddl#create-user) documentation for more details. | `ignite` |
| `distributedJoins` | Whether to execute distributed joins in [non-colocated mode](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/SQL/distributed-joins#non-colocated-joins). | false |
| `enforceJoinOrder` | Whether to enforce join order of tables in the query. If set to `true`, the query optimizer will not reorder tables in the join. | `false` |
| `collocated` | Set this parameter to `true` if your SQL statement includes a GROUP BY clause that groups the results by either primary or affinity key. Whenever GridGain executes a distributed query, it sends subqueries to individual cluster members. If you know in advance that the elements of your query selection are colocated together on the same node and you group by a primary or affinity key, then GridGain makes significant performance and network optimizations by grouping data locally on each node participating in the query. | `false` |
| `replicatedOnly` | Whether the query contains only replicated tables. This is a hint for potentially more effective execution. | `false` |
| `autoCloseServerCursor` | Whether to close server-side cursors automatically when the last piece of a result set is retrieved. When this property is enabled, calling `ResultSet.close()` does not require a network call, which could improve performance. However, if the server-side cursor is already closed, you may get an exception when trying to call `ResultSet.getMetadata()`. This is why it defaults to `false`. | `false` |
| `partitionAwareness` | Enables [Partition Awareness](#partition-awareness) mode. In this mode, the driver tries to determine the nodes where the data that is being queried is located and send the query to these nodes. | `false` |
| `partitionAwarenessSQLCacheSize` | The number of distinct SQL queries that the driver keeps locally for optimization. When a query is executed for the first time, the driver receives the partition distribution for the table that is being queried and saves it for future use locally. When you query this table next time, the driver uses the partition distribution to determine where the data being queried is located to send the query to the right nodes. This local storage with SQL queries invalidates when the cluster topology changes. The optimal value for this parameter should equal the number of distinct SQL queries you are going to perform. | 1000 |
| `partitionAwarenessPartitionDistributionsCacheSize` | The number of distinct objects that represent partition distribution that the driver keeps locally for optimization. See the description of the previous parameter for details. This local storage with partition distribution objects invalidates when the cluster topology changes. The optimal value for this parameter should equal the number of distinct tables ([cache groups](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/configuring-caches/cache-groups)) you are going to use in your queries. | 1000 |
| `socketSendBuffer` | Socket send buffer size. When set to 0, the OS default is used. | 0 |
| `socketReceiveBuffer` | Socket receive buffer size. When set to 0, the OS default is used. | 0 |
| `tcpNoDelay` | Whether to use `TCP_NODELAY` option. | `true` |
| `lazy` | Lazy query execution.<br><br>With `lazy=false`, GridGain fetches the entire query result set to memory and sends it upstream. For small and medium result sets, this provides optimal performance and minimizes duration of internal database locks, thus increasing concurrency.<br><br>With `lazy=true` (by default), query result sets are processed in a streaming manner, and are sent upstream page-by-page, thus minimizing memory consumption at the cost of moderate performance reduction. This is the preferred option for large result sets because, if a result set does not fit in the available memory, the processing leads to excessive GC pauses and [Out of Memory (OOM) errors](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/memleaks002.html).<br><br>• `SELECT * FROM Table` or `SELECT col1, col2 FROM Table` - the data is fetched page-by-page, which precludes OOM.<br>• `SELECT * FROM Table WHERE col>10` or `SELECT col1, col2 FROM Table WHERE col>10` (any predicate as long as it's not a nested subquery) - the data is fetched page-by-page, which precludes OOM.<br><br>If the system does not have an index that corresponds to the query, `lazy=true` might not prevent OOM errors in the following cases:<br>• `SELECT col1 FROM Table GROUP BY col1` - grouping without aggregation; `lazy=true` doesn't help if the aggregating node runs out of memory.<br>• `SELECT col1, AVG(col2) FROM Table GROUP BY col1` - same as the previous case.<br>• `SELECT DISTINCT(col1)` or `SELECT COUNT(DISTINCT(col1))` or `SELECT DISTINCT(col1) ... LIMIT` - the entire result set must be fetched. However, the data is retrieved page-by-page. Therefore, if the aggregating node is the same as the node containing the data, these two nodes share the available memory, so `lazy=true` will reduce memory utilization, thus reducing the probability of OOM errors.<br>• `SELECT ... JOIN` - same outcome as in the previous case.<br>• `SELECT .. OFFSET/LIMIT ORDER BY` - aggregates the entire result set on a node and passes on a chunk (page). Same result as in the previous case.<br>• Subqueries - the result depends on what a specific subquery is interpreted into. It is safe to assume that `lazy=true` brings no benefit (even if the system has an index that corresponds to the query). | `true` |
| `skipReducerOnUpdate` | Enables server side updates. When GridGain executes a DML operation, it fetches all the affected intermediate rows and sends them to the query initiator (also known as reducer) for analysis. Then it prepares batches of updated values to be sent to remote nodes. This approach might impact performance and it can saturate the network if a DML operation has to move many entries over it. Use this flag to tell GridGain to perform all intermediate row analysis and updates "in-place" on corresponding remote data nodes. Defaults to `false`, meaning that the intermediate results are fetched to the query initiator first. | `false` |
| `queryMaxMemory` | Maximum amount of memory available to each query executed through the current connection. This parameter overrides the [memory quota for queries](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/memory-configuration/memory-quotas#memory-quota-for-a-single-query). | none |
| `queryTimeout` | Sets the number of seconds the driver will wait for a Statement object to execute. Zero means there is no limits. | `0` |
| `connectionTimeout` | Sets the number of milliseconds JDBC client will waits for server to response. Zero means there is no limits. | '0' |
| `useLowerCaseForBinaryTypes` | If set to true, names of binary types are set to lower case before hashing their value. See [Binary Configuration](#binary-configuration) for more information. | `null` |
| `useSimpleNamesForBinaryTypes` | If set to true, names of binary types will be simplified. See [Binary Configuration](#binary-configuration) for more information. | `null` |
| `binaryConfigurationFactory` | Class name of a custom `Factory<BinaryConfiguration>` that supplies the `BinaryConfiguration` used by the JDBC client. See [Binary Configuration](#binary-configuration) for more information. | `null` |

For the list of security parameters, refer to the [Using SSL](#using-ssl) section.

### Binary Configuration

By default, the JDBC Thin Driver builds its own `BinaryConfiguration` with default ID and name mappers. If your cluster is configured with a non-default `BinaryConfiguration`, you need to align binary configuration on the driver side.

You can use the following parameters to configure your connection:

- `useLowerCaseForBinaryTypes` and `useSimpleNamesForBinaryTypes` — toggles the basic mappers. Use these when the server uses adjusted `BinaryBasicIdMapper` and/or `BinaryBasicNameMapper`. When unset, the JDBC client falls back to the mapper defaults (`BinaryBasicIdMapper.DFLT_LOWER_CASE` and `BinaryBasicNameMapper.DFLT_SIMPLE_NAME`).
- `binaryConfigurationFactory` — fully-qualified class name of a `javax.cache.configuration.Factory<BinaryConfiguration>` whose `create()` method returns the `BinaryConfiguration` to use. The factory class must be available on the JDBC driver's classpath.

### Connection String Examples

- `jdbc:ignite:thin://myHost` - connect to myHost on the port 10800 with all defaults.
- `jdbc:ignite:thin://myHost:11900` - connect to myHost on custom port 11900 with all defaults.
- `jdbc:ignite:thin://myHost:11900;user=ignite;password=ignite` - connect to myHost on custom port 11900 with user credentials for authentication.
- `jdbc:ignite:thin://myHost:11900;distributedJoins=true&autoCloseServerCursor=true` - connect to myHost on custom port 11900 with enabled distributed joins and autoCloseServerCursor optimization.
- `jdbc:ignite:thin://myHost:11900/myschema;` - connect to myHost on custom port 11900 and access to MYSCHEMA.
- `jdbc:ignite:thin://myHost:11900/"MySchema";lazy=false` - connect to myHost on custom port 11900 with disabled lazy query execution and access to MySchema (schema name is case sensitive).
- `jdbc:ignite:thin://myHost:11900?useLowerCaseForBinaryTypes=true&useSimpleNamesForBinaryTypes=true` - connect with the JDBC client's binary configuration aligned to a server that has `BinaryBasicIdMapper(isLowerCase=true)` and `BinaryBasicIdMapper(isSimpleName=true)` configuration properties.

### Multiple Endpoints

You can enable automatic failover if a current connection is broken by setting multiple connection endpoints in the connection string. The JDBC Driver randomly picks an address from the list to connect to. If the connection fails, the JDBC Driver selects another address from the list until the connection is restored. The Driver stops reconnecting and throws an exception if all the endpoints are unreachable.

The example below shows how to pass three addresses via the connection string:

```java

// Register JDBC Driver.
Class.forName("org.apache.ignite.IgniteJdbcThinDriver");

// Open the JDBC connection passing several connection endpoints.
Connection conn = DriverManager
        .getConnection("jdbc:ignite:thin://192.168.0.50:101,192.188.5.40:101,192.168.10.230:101");
```

### Partition Awareness

Partition awareness is a feature that makes the JDBC driver "aware" of the partition distribution in the cluster. It allows the driver to pick the nodes that own the data that is being queried and send the query directly to those nodes (if the addresses of the nodes are provided in the driver's configuration). Partition awareness can increase average performance of queries that use the affinity key.

Without partition awareness, the JDBC driver connects to a single node, and all queries are executed through that node. If the data is hosted on a different node, the query has to be rerouted within the cluster, which adds an additional network hop. Partition awareness eliminates that hop by sending the query to the right node.

To make use of the partition awareness feature, provide the addresses of all the server nodes in the connection properties. The driver will route requests to the nodes that store the data requested by the query.

{% hint style="danger" %}
Note that presently you need to provide the addresses of all server nodes in the connection properties because the driver does not load them automatically after a connection is opened. It also means that if a new server node joins the cluster, you are advised to reconnect the driver and add the node's address to the connection properties. Otherwise, the driver will not be able to send direct requests to this node.
{% endhint %}

To enable partition awareness, add the `partitionAwareness=true` parameter to the connection string and provide the endpoints of multiple server nodes:

```java
Class.forName("org.apache.ignite.IgniteJdbcThinDriver");

Connection conn = DriverManager
        .getConnection("jdbc:ignite:thin://192.168.0.50,192.188.5.40,192.168.10.230?partitionAwareness=true");
```

{% hint style="info" %}
Partition Awareness can be used only with the default affinity function.
{% endhint %}

Also see the description of the two related parameters: `partitionAwarenessSQLCacheSize` and `partitionAwarenessPartitionDistributionsCacheSize`.

### Cluster Configuration

In order to accept and process requests from JDBC Thin Driver, a cluster node binds to a local network interface on port 10800 and listens to incoming requests.

Use an instance of `ClientConnectorConfiguration` to change the connection parameters:

{% tabs %}
{% tab title="XML" %}
```xml
<bean id="ignite.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
  <property name="clientConnectorConfiguration">
    <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration" />
  </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration()
    .setClientConnectorConfiguration(new ClientConnectorConfiguration());
```
{% endtab %}

{% tab title="C#/.NET" %}
Not supported.
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

The following parameters are supported:

| Parameter | Description | Default Value |
| --- | --- | --- |
| `host` | Host name or IP address to bind to. When set to `null`, binding is made to `localhost`. | `null` |
| `port` | TCP port to bind to. If the specified port is already in use, GridGain tries to find another available port using the `portRange` property. | `10800` |
| `portRange` | Defines the number of ports to try to bind to. E.g. if the port is set to `10800` and `portRange` is `100`, then the server tries to bind consecutively to any port in the `[10800, 10900]` range until it finds a free port. | `100` |
| `maxOpenCursorsPerConnection` | Maximum number of cursors that can be opened simultaneously for a single connection. | `128` |
| `threadPoolSize` | Number of request-handling threads in the thread pool. | `MAX(8, CPU cores)` |
| `socketSendBufferSize` | Size of the TCP socket send buffer. When set to 0, the system default value is used. | `0` |
| `socketReceiveBufferSize` | Size of the TCP socket receive buffer. When set to 0, the system default value is used. | `0` |
| `tcpNoDelay` | Whether to use `TCP_NODELAY` option. | `true` |
| `idleTimeout` | Idle timeout for client connections. Clients are disconnected automatically from the server after remaining idle for the configured timeout. When this parameter is set to zero or a negative value, the idle timeout is disabled. | `0` |
| `isJdbcEnabled` | Whether access through JDBC is enabled. | `true` |
| `isThinClientEnabled` | Whether access through thin client is enabled. | `true` |
| `sslEnabled` | If SSL is enabled, only SSL client connections are allowed. The node allows only one mode of connection: `SSL` or `plain`. A node cannot receive both types of client connections. But this option can be different for different nodes in the cluster. | `false` |
| `useIgniteSslContextFactory` | Whether to use SSL context factory from the node's configuration (see `IgniteConfiguration.sslContextFactory`). | `true` |
| `sslClientAuth` | Whether client authentication is required. | `false` |
| `sslContextFactory` | The class name that implements `Factory<SSLContext>` to provide node-side SSL. See [this](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/ssl-tls) for more information. | `null` |

{% hint style="danger" %}
**JDBC Thin Driver is not thread safe**

The JDBC objects `Connections`, `Statements`, and `ResultSet` are not thread safe. Do not use statements and results sets from a single JDBC Connection in multiple threads.

JDBC Thin Driver guards against concurrency. If concurrent access is detected, an exception (`SQLException`) is produced with the following message:

```
"Concurrent access to JDBC connection is not allowed
[ownThread=<guard_owner_thread_name>, curThread=<current_thread_name>]",
SQLSTATE="08006"
```
{% endhint %}

### Using SSL

You can configure the JDBC Thin Driver to use SSL to secure communication with the cluster. SSL must be configured both on the cluster side and in the JDBC Driver. Refer to the [SSL for Thin Clients and JDBC/ODBC](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/ssl-tls#ssl-for-clients) section for the information about cluster configuration.

To enable SSL in the JDBC Driver, pass the `sslMode=require` parameter in the connection string and provide the key store and trust store parameters:

```java
Class.forName("org.apache.ignite.IgniteJdbcThinDriver");

String keyStore = "keystore/node.p12";
String keyStorePassword = "123456";

String trustStore = "keystore/trust.p12";
String trustStorePassword = "123456";

try (Connection conn = DriverManager.getConnection("jdbc:ignite:thin://127.0.0.1?sslMode=require"
        + "&sslClientCertificateKeyStoreUrl=" + keyStore + "&sslClientCertificateKeyStorePassword="
        + keyStorePassword + "&sslTrustCertificateKeyStoreUrl=" + trustStore
        + "&sslTrustCertificateKeyStorePassword=" + trustStorePassword)) {

    ResultSet rs = conn.createStatement().executeQuery("select 10");
    rs.next();
    System.out.println(rs.getInt(1));
} catch (Exception e) {
    e.printStackTrace();
}

```

The following table lists all parameters that affect SSL/TLS connection:

| Parameter | Description | Default Value |
| --- | --- | --- |
| `sslMode` | Enables SSL connection. Available modes:<br>• `require`: SSL protocol is enabled on the client. Only SSL connection is available.<br>• `disable`: SSL protocol is disabled on the client. Only plain connection is supported. | `disable` |
| `sslProtocol` | Protocol name for secure transport. Protocol implementations supplied by JSSE: `SSLv3 (SSL)`, `TLSv1 (TLS)`, `TLSv1.1`, `TLSv1.2` | `TLS` |
| `sslKeyAlgorithm` | The Key manager algorithm to be used to create a key manager. Note that in most cases the default value is sufficient. Algorithms implementations supplied by JSSE: `PKIX (X509 or SunPKIX)`, `SunX509`. | `None` |
| `sslClientCertificateKeyStoreUrl` | URL of the client key store file. This is a mandatory parameter since SSL context cannot be initialized without a key manager. If `sslMode` is `require` and the key store URL isn't specified in the GridGain properties, the value of the JSSE property `javax.net.ssl.keyStore` will be used. | The value of the `javax.net.ssl.keyStore` system property. |
| `sslClientCertificateKeyStorePassword` | Client key store password.<br><br>If `sslMode` is `require` and the key store password isn't specified in the GridGain properties, the JSSE property `javax.net.ssl.keyStorePassword` will be used. | The value of the `javax.net.ssl.keyStorePassword` system property. |
| `sslClientCertificateKeyStoreType` | Client key store type used in context initialization.<br><br>If `sslMode` is `require` and the key store type isn't specified in the GridGain properties, the JSSE property `javax.net.ssl.keyStoreType` will be used. | The value of the `javax.net.ssl.keyStoreType` system property. If the system property is not defined, the default value is `JKS`. |
| `sslTrustCertificateKeyStoreUrl` | URL of the trust store file. This is an optional parameter; however, one of these properties must be set: `sslTrustCertificateKeyStoreUrl` or `sslTrustAll`<br><br>If `sslMode` is `require` and the trust store URL isn't specified in the GridGain properties, the JSSE property `javax.net.ssl.trustStore` will be used. | The value of the `javax.net.ssl.trustStore` system property. |
| `sslTrustCertificateKeyStorePassword` | Trust store password.<br><br>If `sslMode` is `require` and the trust store password isn't specified in the GridGain properties, the JSSE property `javax.net.ssl.trustStorePassword` will be used. | The value of the `javax.net.ssl.trustStorePassword` system property |
| `sslTrustCertificateKeyStoreType` | Trust store type.<br><br>If `sslMode` is `require` and the trust store type isn't specified in the GridGain properties, the JSSE property `javax.net.ssl.trustStoreType` will be used. | The value of the `javax.net.ssl.trustStoreType` system property. If the system property is not defined the default value is `JKS` |
| `sslTrustAll` | Disables server's certificate validation. Set to `true` to trust any server certificate (revoked, expired, or self-signed SSL certificates).<br><br>**Caution:** Do not enable this option in production on a network you do not entirely trust. Especially anything using the public internet. | `false` |
| `sslFactory` | Class name of the custom implementation of the `Factory<SSLSocketFactory>`.<br><br>If `sslMode` is `require` and a factory is specified, the custom factory is used instead of the JSSE socket factory. In this case, other SSL properties are ignored. | `null` |

The default implementation is based on JSSE, and works through two Java keystore files:

- `sslClientCertificateKeyStoreUrl` - the client certificate keystore holds the keys and certificate for the client.
- `sslTrustCertificateKeyStoreUrl` - the trusted certificate keystore contains the certificate information to validate the server's certificate.

The trusted store is an optional parameter, however one of the following parameters: `sslTrustCertificateKeyStoreUrl` or `sslTrustAll` must be configured.

{% hint style="danger" %}
**Using the "sslTrustAll" option**

Do not enable this option in production on a network you do not entirely trust, especially anything using the public internet.
{% endhint %}

If you want to use your own implementation or method to configure the `SSLSocketFactory`, you can use JDBC Driver's `sslFactory` parameter. It is a string that must contain the name of the class that implements the interface `Factory<SSLSocketFactory>`. The class must be available for JDBC Driver's class loader.

### Handling Disconnects

Auto-recovery logic applies only to idempotent requests (like `SELECT`).

If the connection cannot be re-established, the current statement is forced to close, and an SQLException with SQL state `08006` is raised. Once that happens, you can retry the operation at your own risk.

The connection is not re-established if MVCC is used. In this case, the connection is forced to close.

This is what a disconnection looks like in the Java code:

```java
...
catch(SQLException ex) {
  if (!conn.isClosed() && "08006".equals(ex.getSQLState()))
}
```

The following example showcases a method for repeating an operation.

{% hint style="info" %}
In case of disconnection, there is a risk of duplicating a request to change data.
{% endhint %}

```java
try (Connection conn = DriverManager.getConnection(URL)) {
        executeWithRetries(conn, 3, () -> {
            try (Statement stmt = conn.createStatement()) {
                return stmt.executeUpdate("INSERT INTO TEST VALUES (1, 1)");
            }
        });
    }

<T> T executeWithRetries(Connection conn, int retryCount, Callable<T> sqlCall) throws SQLException {
    for (; ; ) {
        try {
            return sqlCall.call();
        }
        catch (SQLException e) {
            if (--retryCount == 0) {
                // The number of retries exceeded.
                throw e;
            }
            if (!"08006".equals(e.getSQLState())) {
                // Other kind of error has occurred.
                throw e;
            }
            if (conn.isClosed()) {
                // Must re-establish connection manually.
                throw e;
            }
        }
        catch (Exception e) {
            throw (RuntimeException)e;
        }
    }
}
```

## Ignite DataSource

The DataSource object is used as a deployed object that can be located by logical name via the JNDI naming service. JDBC Driver's `org.apache.ignite.IgniteJdbcThinDataSource` implements a JDBC DataSource interface allowing you to utilize the DataSource interface instead.

In addition to generic DataSource properties, `IgniteJdbcThinDataSource` supports all the Ignite-specific properties that can be passed into a JDBC connection string. For instance, the `distributedJoins` property can be (re)set via the `IgniteJdbcThinDataSource#setDistributedJoins()` method.

Refer to the [JavaDocs](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/IgniteJdbcThinDataSource.html) for more details.

## Examples

To start processing the data located in the cluster, you need to create a JDBC Connection object via one of the methods below:

```java
// Open the JDBC connection via DriverManager.
Connection conn = DriverManager.getConnection("jdbc:ignite:thin://192.168.0.50");
```

or

```java
// Or open connection via DataSource.
IgniteJdbcThinDataSource ids = new IgniteJdbcThinDataSource();
ids.setUrl("jdbc:ignite:thin://127.0.0.1");
ids.setDistributedJoins(true);

Connection conn = ids.getConnection();
```

Then you can execute SQL SELECT queries as follows:

```java
// Query people with specific age using prepared statement.
PreparedStatement stmt = conn.prepareStatement("select name, age from Person where age = ?");

stmt.setInt(1, 30);

ResultSet rs = stmt.executeQuery();

while (rs.next()) {
    String name = rs.getString("name");
    int age = rs.getInt("age");
    // ...
}
```

You can also modify the data via DML statements.

### INSERT

```java
// Insert a Person with a Long key.
PreparedStatement stmt = conn
        .prepareStatement("INSERT INTO Person(_key, name, age) VALUES(CAST(? as BIGINT), ?, ?)");

stmt.setInt(1, 1);
stmt.setString(2, "John Smith");
stmt.setInt(3, 25);

stmt.execute();
```

### MERGE

```java
// Merge a Person with a Long key.
PreparedStatement stmt = conn
        .prepareStatement("MERGE INTO Person(_key, name, age) VALUES(CAST(? as BIGINT), ?, ?)");

stmt.setInt(1, 1);
stmt.setString(2, "John Smith");
stmt.setInt(3, 25);

stmt.executeUpdate();

```

### UPDATE

```java
// Update a Person.
conn.createStatement().
  executeUpdate("UPDATE Person SET age = age + 1 WHERE age = 25");
```

### DELETE

```java
conn.createStatement().execute("DELETE FROM Person WHERE age = 25");
```

## Streaming

JDBC Driver allows streaming data in bulk using the `SET` command. See the `SET` command [documentation](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/operational-commands#set-streaming) for more information.

## Error Codes

The JDBC drivers pass error codes in the `java.sql.SQLException` class, used to facilitate exception handling on the application side. To get an error code, use the `java.sql.SQLException.getSQLState()` method. It returns a string containing the ANSI SQLSTATE error code defined:

```java
PreparedStatement ps;

try {
    ps = conn.prepareStatement("INSERT INTO Person(id, name, age) values (1, 'John', 'unparseableString')");
} catch (SQLException e) {
    switch (e.getSQLState()) {
    case "0700B":
        System.out.println("Conversion failure");
        break;

    case "42000":
        System.out.println("Parsing error");
        break;

    default:
        System.out.println("Unprocessed error: " + e.getSQLState());
        break;
    }
}
```

The table below lists all the [ANSI SQLSTATE](https://en.wikipedia.org/wiki/SQLSTATE) error codes currently supported by GridGain. Note that the list may be extended in the future.

| Code | Description |
| --- | --- |
| 0700B | Conversion failure (for example, a string expression cannot be parsed as a number or a date). |
| 0700E | Invalid transaction isolation level. |
| 08001 | The driver failed to open a connection to the cluster. |
| 08003 | The connection is in the closed state. Happened unexpectedly. |
| 08004 | The connection was rejected by the cluster. |
| 08006 | I/O error during communication. |
| 22004 | Null value not allowed. |
| 22023 | Unsupported parameter type. |
| 23000 | Data integrity constraint violation. |
| 24000 | Invalid result set state. |
| 0A000 | Requested operation is not supported. |
| 40001 | Concurrent update conflict. See [Concurrent Updates](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/transactions/mvcc#concurrent-updates). |
| 42000 | Query parsing exception. |
| 50000 | Internal error.<br>The code is not defined by ANSI and refers to an Ignite specific error. Refer to the `java.sql.SQLException` error message for more information. |
