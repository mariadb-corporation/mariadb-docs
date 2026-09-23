---
description: >-
  Connect to a GridGain 9 cluster with the JDBC driver, configure connection
  parameters, run transactions, control follower reads, and use partition
  awareness.
---

# JDBC Driver

GridGain is shipped with JDBC driver that allows processing of distributed data using standard SQL statements like `SELECT`, `INSERT`, `UPDATE`, or `DELETE` directly from the JDBC side. The name of the driver's class is `org.apache.ignite.jdbc.IgniteJdbcDriver`.

{% hint style="info" %}
The JDBC driver was completely reworked in GridGain 9.1.16 and now supports multiple endpoints and [partition awareness](overview.md#partition-awareness).

The new driver is not compatible with GridGain 9.1.15 or earlier. To connect to those versions, use the previous version of the driver that was shipped with the appropriate version of GridGain.

The server part remains compatible with previous versions of the driver, so driver for GridGain 9.1.15 and earlier can connect to the 9.1.16+ cluster.
{% endhint %}

See also:

* [Unsupported Mandatory JDBC Features](#unsupported-mandatory-jdbc-features)
* [Unsupported Optional JDBC Features](#unsupported-optional-jdbc-features)
* [JDBC Features with Limited Support](#jdbc-features-with-limited-support)

## Prerequisites

{% include "../../../.gitbook/includes/prereqs-java.md" %}

## Setting Up

JDBC driver uses the client connector to work with the cluster. For more information on configuring client connector, see [Client Connector Configuration](overview.md#client-connector-configuration).

The JDBC connector needs to be included from Maven:

```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>ignite-jdbc</artifactId>
    <version>9.1</version>
</dependency>
```

Here is how you can open a JDBC connection to the cluster node listening on IP address `127.0.0.1`:

```java
Connection conn = DriverManager.getConnection("jdbc:ignite:thin://127.0.0.1:10800");
```

The driver connects to one of the cluster nodes and forwards all the queries to it for final execution. The node handles the query distribution and the result's aggregations. Then the result is sent back to the client application.

The JDBC connection string can have an optional list of name-value pairs as parameters after the '?' delimiter. Name and value are separated by the '=' symbol and multiple properties are separated either by an '&' or a ';'.
Separate sign can't be mixed and should be either semicolon or ampersand sign.

```java
jdbc:ignite:thin://host[:port][,host[:port][/schema][[?parameter1=value1][&parameter2=value2],...]]
jdbc:ignite:thin://host[:port][,host[:port][/schema][[?parameter1=value1][;parameter2=value2],...]]
```

* `host` is required and defines the host of the cluster node to connect to.
* `port` is the port to use to open the connection. 10800 is used by default if this parameter is omitted.
* `schema` is the schema name to access. PUBLIC is used by default. This name should correspond to the SQL ANSI-99 standard. Non-quoted identifiers are not case sensitive. Quoted identifiers are case sensitive. When semicolon format is used, the schema may be defined as a parameter with name schema.
* `parameters` are optional parameters. The following parameters are available:
    * `connectionTimeZone` - Client connection time-zone ID. This property can be used by the client to change the time zone of the session on the server. Affects the interpretation of dates in queries that do not specify the time zone explicitly. If not set, system default on client timezone will be used.
    * `partitionAwarenessMetadataCacheSize` - Size of cache to store partition awareness metadata of queries, in number of entries. Default value: `1024`.
    * `allowDdlInTx` - When `true`, DDL statements are allowed to run on a connection with auto-commit disabled. The DDL executes outside the explicit transaction and is not affected by `commit` or `rollback`. Enable this option for compatibility with external tools (for example, DBeaver). Default value: `false`.
    * `queryTimeoutSeconds` - Number of seconds the driver will wait for a `Statement` object to execute. 0 means there is no limit. Default value: `0`.
    * `connectionTimeoutMillis` - Number of milliseconds JDBC client will wait for server to respond. 0 means there is no limit. Default value: `0`.
    * `transactionTimeoutMillis` - Timeout, in milliseconds, applied to transactions started on this connection. `0` means the cluster-wide default is used (see [Transaction Timeouts](../../administrators-guide/transactions.md#transaction-timeouts)). Default value: `0`.
    * `allowFollowerReads` - Determines whether read-only SQL statements on this connection can read data from non-primary replicas. If not set, the cluster-wide [`sql.allowFollowerReads`](../../administrators-guide/config/cluster-config.md#sql-configuration) setting applies. Possible values: `true`, `false`. Default value: not set.
    * `username` - username for basic authentication to the cluster.
    * `password` - user password for basic authentication to the cluster.
    * `sslEnabled` - Determines if SSL is enabled. Possible values: `true`, `false`. Default value: `false`
        * `trustStorePath` - Path to trust store on client side.
        * `trustStorePassword` - Trust store password.
        * `keyStorePath` - Path to key store on client side.
        * `keyStorePassword` - Key store password.
        * `clientAuth` - SSL client authentication. Possible values: `NONE`, `OPTIONAL`, `REQUIRE`.
        * `ciphers` - comma-separated SSL ciphers list.

### Parameter Precedence

If the same parameters are passed by using different means, the JDBC driver prioritizes them in the following way:

1. API arguments passed in the `Connection` objects;
2. Last instance of the parameter in the connection string;
3. Properties object passed during connection.

## Performing Transactions

By default, a JDBC connection is in auto-commit mode, and in this mode all its SQL statements will be executed and committed as individual transactions.
To be able to manage the transaction, you must switch connection to non-autocommit mode.
In non-autocommit mode, you can perform `commit` and `rollback` transactions. For more information about transactions, see [Performing Transactions](../transactions.md).

Here is how you can commit a transaction:

```java
// Open the JDBC connection.
Connection conn = DriverManager.getConnection("jdbc:ignite:thin://127.0.0.1:10800");

// Disable auto-commit mode.
conn.setAutoCommit(false);

// Commit a transaction
conn.commit();
```

You can also configure GridGain to automatically commit transactions by using the `setAutoCommit()` method.

Here is how you can rollback a transaction:

```java
conn.rollback();
```

### Setting the Transaction Timeout

By default, transactions opened through the JDBC driver use the cluster-wide transaction timeout (see [Transaction Timeouts](../../administrators-guide/transactions.md#transaction-timeouts)). To override it for a single connection, set the `transactionTimeoutMillis` connection parameter:

```java
Connection conn = DriverManager.getConnection(
        "jdbc:ignite:thin://127.0.0.1:10800?transactionTimeoutMillis=5000");
```

You can also set the timeout programmatically by unwrapping the connection as `IgniteJdbcConnection`. The new value applies to transactions started after the call. Transactions already in progress are not affected.

```java
conn.unwrap(IgniteJdbcConnection.class)
        .setTransactionTimeout(5000L);
```

In non-autocommit mode, the timeout is applied to each explicit transaction. In auto-commit mode, where each statement runs in its own implicit transaction, the driver enforces the timeout by limiting the statement's execution time to the smaller of `transactionTimeoutMillis` and `queryTimeoutSeconds` (a value of `0` for either means no limit).

### Retrying Failed Transactions

Some transaction failures are transient. For example, a transaction may be killed, or a primary replica may become temporarily unavailable. When `commit` or a statement fails for a retriable reason, the JDBC driver throws a `java.sql.SQLRecoverableException` instead of a plain `java.sql.SQLException`. Because `SQLRecoverableException` is a subclass of `SQLException`, code that already catches `SQLException` continues to work unchanged.

`SQLRecoverableException` signals that the operation may succeed if you retry the entire transaction. Connection pools and frameworks that recognize this standard JDBC exception can retry the operation automatically.

```java
try (Connection conn = DriverManager.getConnection("jdbc:ignite:thin://127.0.0.1:10800")) {
    conn.setAutoCommit(false);

    // Execute statements.

    conn.commit();
} catch (SQLRecoverableException e) {
    // Transient failure: retry the entire transaction from the start.
} catch (SQLException e) {
    // Non-retriable failure: handle or propagate the error.
}
```

## Configuring Memory Quota Block Size

The JDBC driver supports configuring memory quota block size for each SQL statement. Setting a larger block size can improve performance for memory-intensive queries.

The value determines the block size in bytes and must not be negative. If set to `null`, GridGain uses system default.

To set a memory quota, unwrap the `Statement` object:

```java
try (Connection conn = DriverManager.getConnection("jdbc:ignite:thin://127.0.0.1:10800");
        Statement stmt = conn.createStatement()) {

    stmt.unwrap(IgniteJdbcStatement.class)
            .setMemoryQuotaBlockSize(1024L);

    try (ResultSet rs = stmt.executeQuery("SELECT * FROM big_table")) {
        // Process results
    }
}
```

## Controlling Follower Reads

By default, GridGain executes read-only SQL statements against primary replicas only. Allowing follower reads spreads read load across all replicas and lets a query read from a local replica, which avoids a network hop. In exchange, the query may take longer while a follower replica catches up.

Follower reads apply only to statements that run in a read-only transaction. A statement that runs in a read-write transaction always reads from primary replicas.

To allow or disallow follower reads for a whole connection, use the `allowFollowerReads` connection parameter:

```java
Connection conn = DriverManager.getConnection(
        "jdbc:ignite:thin://127.0.0.1:10800?allowFollowerReads=true");
```

To control individual statements, unwrap the `Statement` object:

```java
try (Connection conn = DriverManager.getConnection("jdbc:ignite:thin://127.0.0.1:10800");
        Statement stmt = conn.createStatement()) {

    stmt.unwrap(IgniteJdbcStatement.class)
            .setAllowFollowerReads(false);

    try (ResultSet rs = stmt.executeQuery("SELECT * FROM big_table")) {
        // Process results
    }
}
```

## Partition Awareness

Partition awareness is supported by the JDBC driver.

See [Partition Awareness Overview](overview.md#partition-awareness) for more details.

## Unsupported Mandatory JDBC Features

The following mandatory JDBC features are currently not supported (sorted alphabetically):

* java.sql.Connection#clearWarnings
* java.sql.Connection#getWarnings
* java.sql.Connection#prepareCall
* java.sql.PreparedStatement#getParameterMetaData
* java.sql.PreparedStatement#setAsciiStream
* java.sql.PreparedStatement#setBinaryStream
* java.sql.PreparedStatement#setCharacterStream
* java.sql.ResultSet#clearWarnings
* java.sql.ResultSet#getAsciiStream
* java.sql.ResultSet#getBinaryStream
* java.sql.ResultSet#getCharacterStream
* java.sql.ResultSet#getWarnings
* java.sql.ResultSet#setFetchDirection
* java.sql.Statement#clearWarnings
* java.sql.Statement#getWarnings
* java.sql.Statement#setEscapeProcessing
* java.sql.Statement#setFetchDirection
* java.sql.Statement#setMaxFieldSize

## Unsupported Optional JDBC Features

The following optional JDBC features are currently not supported (sorted alphabetically):

* java.sql.Connection#createArrayOf
* java.sql.Connection#createBlob
* java.sql.Connection#createClob
* java.sql.Connection#createNClob
* java.sql.Connection#createSQLXML
* java.sql.Connection#createStruct
* java.sql.Connection#getTypeMap
* java.sql.Connection#releaseSavepoint
* java.sql.Connection#setSavepoint
* java.sql.Connection#setTypeMap
* java.sql.Driver#getParentLogger
* java.sql.PreparedStatement#getMetaData
* java.sql.PreparedStatement#setArray
* java.sql.PreparedStatement#setBlob
* java.sql.PreparedStatement#setClob
* java.sql.PreparedStatement#setNCharacterStream
* java.sql.PreparedStatement#setNClob
* java.sql.PreparedStatement#setRef
* java.sql.PreparedStatement#setRowId
* java.sql.PreparedStatement#setSQLXML
* java.sql.PreparedStatement#setUnicodeStream
* java.sql.PreparedStatement#setURL
* java.sql.ResultSet#cancelRowUpdates
* java.sql.ResultSet#deleteRow
* java.sql.ResultSet#getArray
* java.sql.ResultSet#getBlob
* java.sql.ResultSet#getClob
* java.sql.ResultSet#getNCharacterStream
* java.sql.ResultSet#getNClob
* java.sql.ResultSet#getRef
* java.sql.ResultSet#getRowId
* java.sql.ResultSet#getSQLXML
* java.sql.ResultSet#getUnicodeStream
* java.sql.ResultSet#insertRow
* java.sql.ResultSet#moveToInsertRow
* java.sql.ResultSet#refreshRow
* java.sql.ResultSet#updateArray
* java.sql.ResultSet#updateAsciiStream
* java.sql.ResultSet#updateBigDecimal
* java.sql.ResultSet#updateBinaryStream
* java.sql.ResultSet#updateBlob
* java.sql.ResultSet#updateBoolean
* java.sql.ResultSet#updateByte
* java.sql.ResultSet#updateBytes
* java.sql.ResultSet#updateCharacterStream
* java.sql.ResultSet#updateClob
* java.sql.ResultSet#updateDate
* java.sql.ResultSet#updateDouble
* java.sql.ResultSet#updateFloat
* java.sql.ResultSet#updateInt
* java.sql.ResultSet#updateLong
* java.sql.ResultSet#updateNCharacterStream
* java.sql.ResultSet#updateNClob
* java.sql.ResultSet#updateNString
* java.sql.ResultSet#updateNull
* java.sql.ResultSet#updateObject
* java.sql.ResultSet#updateRef
* java.sql.ResultSet#updateRow
* java.sql.ResultSet#updateRowId
* java.sql.ResultSet#updateShort
* java.sql.ResultSet#updateSQLXML
* java.sql.ResultSet#updateString
* java.sql.ResultSet#updateTime
* java.sql.ResultSet#updateTimestamp
* java.sql.Statement#getGeneratedKeys
* java.sql.Statement#setCursorName
* java.sql.Statement#setPoolable

## JDBC Features with Limited Support

The following JDBC features are supported only in specific cases:

| Feature | Supported Cases |
| --- | --- |
| java.sql.Connection#prepareStatement | autoGeneratedKeys=Statement.NO_GENERATED_KEYS, resultSetType=ResultSet.TYPE_FORWARD_ONLY, resultSetConcurrency=ResultSet.CONCUR_READ_ONLY, null or empty columnIndexes, and null or empty columnNames. |
| java.sql.Connection#rollback | Without savepoint. |
| java.sql.Statement#execute | autoGeneratedKeys=Statement.NO_GENERATED_KEYS, null or empty columnIndexes, and null or empty columnNames. |
| java.sql.Statement#executeUpdate | autoGeneratedKeys=Statement.NO_GENERATED_KEYS, null or empty columnIndexes, and null or empty columnNames. |
| java.sql.Statement#getMoreResults | current=Statement.CLOSE_CURRENT_RESULT. |
</content>
