---
hidden: true
description: >-
  Reference for the GridGain JDBC Client Driver, which connects to the cluster
  through a client node, including supported parameters and streaming mode.
---

# JDBC Client Driver

JDBC Client Driver interacts with the cluster by means of a [client node](https://www.gridgain.com/docs/gridgain8/latest/getting-started/concepts#clustering-servers-and-clients).

## JDBC Client Driver

The JDBC Client Driver connects to the cluster by using a [client node](https://www.gridgain.com/docs/gridgain8/latest/getting-started/concepts#clustering-servers-and-clients) connection. You must provide a complete Spring XML configuration as part of the JDBC connection string, and copy all the JAR files mentioned below to the classpath of your application or SQL tool:

- All the JARs under `{GRIDGAIN_HOME}\libs` directory.
- All the JARs under `{GRIDGAIN_HOME}\ignite-indexing` and `{GRIDGAIN_HOME}\ignite-spring` directories.

The driver itself is more robust, and might not support the latest SQL features of Ignite. However, because it uses the client node connection underneath, it can execute and distribute queries, and aggregate their results directly from the application side.

The JDBC connection URL has the following pattern:

```shell
jdbc:ignite:cfg://[<params>@]<config_url>
```

Where:

- `<config_url>` is required and must represent a valid URL that points to the configuration file for the client node. This node will be started within the Ignite JDBC Client Driver when it (the JDBC driver) tries to establish a connection with the cluster.
- `<params>` is optional and has the following format:

```text
param1=value1:param2=value2:...:paramN=valueN
```

The name of the driver's class is `org.apache.ignite.IgniteJdbcDriver`. For example, here's how to open a JDBC connection to the Ignite cluster:

```java
// Registering the JDBC driver.
Class.forName("org.apache.ignite.IgniteJdbcDriver");

// Opening JDBC connection (cache name is not specified, which means that we use default cache).
Connection conn = DriverManager.getConnection("jdbc:ignite:cfg://config/ignite-jdbc.xml");
        
```

{% hint style="info" %}
**Securing Connection**

For information on how to secure the JDBC client driver connection, you can refer to the [Security documentation](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/ssl-tls).
{% endhint %}

### Supported Parameters

| Parameter | Description | Default Value |
| --- | --- | --- |
| `cache` | Cache name. Note that the cache name is case sensitive. | None. |
| `nodeId` | ID of node where query will be executed. Useful for querying through local caches. | None. |
| `local` | Query will be executed only on a local node. Use this parameter with the `nodeId` parameter in order to limit data set by specified node. | `false` |
| `collocated` | Flag that is used for optimization purposes. Whenever GridGain executes a distributed query, it sends subqueries to individual cluster members. If you know in advance that the elements of your query selection are colocated together on the same node, Ignite can make significant performance and network optimizations. | `false` |
| `distributedJoins` | Allows use of distributed joins for non-colocated data. | `false` |
| `streaming` | Turns on bulk data load mode via INSERT statements for this connection. Refer to the [Streaming Mode](#streaming-mode) section for more details. | `false` |
| `streamingAllowOverwrite` | Tells GridGain to overwrite values for existing keys on duplication instead of skipping them. Refer to the [Streaming Mode](#streaming-mode) section for more details. | `false` |
| `streamingFlushFrequency` | Timeout, in milliseconds, that data streamer should use to flush data. By default, the data is flushed on connection close. Refer to the [Streaming Mode](#streaming-mode) section for more details. | `0` |
| `streamingPerNodeBufferSize` | Data streamer's per node buffer size. Refer to the [Streaming Mode](#streaming-mode) section for more details. | `1024` |
| `streamingPerNodeParallelOperations` | Data streamer's per node parallel operations number. Refer to the [Streaming Mode](#streaming-mode) section for more details. | `16` |
| `transactionsAllowed` | Presently ACID Transactions are supported, but only at the key-value API level. At the SQL level, GridGain supports atomic, but not transactional consistency.<br><br>This means that the JDBC driver might throw a `Transactions are not supported` exception if you try to use this functionality.<br><br>However, in cases when you need transactional syntax to work (even without transactional semantics), e.g. some BI tools might force the transactional behavior, set this parameter to `true` to prevent exceptions from being thrown. | `false` |
| `multipleStatementsAllowed` | JDBC driver will be able to process multiple SQL statements at a time, returning multiple `ResultSet` objects. If the parameter is disabled, the query with multiple statements fails. | `false` |
| `lazy` | Lazy query execution.<br><br>With `lazy=false`, GridGain fetches the entire query result set to memory and sends it upstream. For small and medium result sets, this provides optimal performance and minimizes duration of internal database locks, thus increasing concurrency.<br><br>With `lazy=true` (by default), query result sets are processed in a streaming manner, and are sent upstream page-by-page, thus minimizing memory consumption at the cost of moderate performance reduction. This is the preferred option for large result sets because, if a result set does not fit in the available memory, the processing leads to excessive GC pauses and [Out of Memory (OOM) errors](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/memleaks002.html).<br><br>• `SELECT * FROM Table` or `SELECT col1, col2 FROM Table` - the data is fetched page-by-page, which precludes OOM.<br>• `SELECT * FROM Table WHERE col>10` or `SELECT col1, col2 FROM Table WHERE col>10` (any predicate as long as it's not a nested subquery) - the data is fetched page-by-page, which precludes OOM.<br><br>If the system does not have an index that corresponds to the query, `lazy=true` might not prevent OOM errors in the following cases:<br>• `SELECT col1 FROM Table GROUP BY col1` - grouping without aggregation; `lazy=true` doesn't help if the aggregating node runs out of memory.<br>• `SELECT col1, AVG(col2) FROM Table GROUP BY col1` - same as the previous case.<br>• `SELECT DISTINCT(col1)` or `SELECT COUNT(DISTINCT(col1))` or `SELECT DISTINCT(col1) ... LIMIT` - the entire result set must be fetched. However, the data is retrieved page-by-page. Therefore, if the aggregating node is the same as the node containing the data, these two nodes share the available memory, so `lazy=true` will reduce memory utilization, thus reducing the probability of OOM errors.<br>• `SELECT ... JOIN` - same outcome as in the previous case.<br>• `SELECT .. OFFSET/LIMIT ORDER BY` - aggregates the entire result set on a node and passes on a chunk (page). Same result as in the previous case.<br>• Subqueries - the result depends on what a specific subquery is interpreted into. It is safe to assume that `lazy=true` brings no benefit (even if the system has an index that corresponds to the query). | `true` |
| `skipReducerOnUpdate` | Enables server side update feature.<br><br>When GridGain executes a DML operation, it first fetches all of the affected intermediate rows for analysis to the query initiator (also known as reducer), and then prepares batches of updated values to be sent to remote nodes.<br><br>This approach might impact performance and saturate the network if a DML operation has to move many entries over it.<br><br>Use this flag as a hint for GridGain to perform all intermediate rows analysis and updates "in-place" on the corresponding remote data nodes.<br><br>Defaults to `false`, meaning that intermediate results will be fetched to the query initiator first. | `false` |
| `queryMaxMemory` | Maximum amount of memory available to each query executed through the current connection. This parameter overrides the [memory quota for queries](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/memory-configuration/memory-quotas#memory-quota-for-a-single-query). | none |

{% hint style="info" %}
**Cross-Cache Queries**

The cache to which the driver is connected is treated as the default schema. To query across multiple caches, you can use Cross-Cache queries.
{% endhint %}

### Streaming Mode

It's feasible to add data into a cluster in streaming mode (bulk mode) using the JDBC driver. In this mode, the driver instantiates `IgniteDataStreamer` internally and feeds data to it. To activate this mode, add the `streaming` parameter set to `true` to a JDBC connection string:

```java
// Register JDBC driver.
Class.forName("org.apache.ignite.IgniteJdbcDriver");

// Opening connection in the streaming mode.
Connection conn = DriverManager.getConnection("jdbc:ignite:cfg://streaming=true@file:///etc/config/ignite-jdbc.xml");
```

Streaming mode is supported only for INSERT operations. This is useful in cases when you want to achieve fast data preloading into a cache. The JDBC driver defines multiple connection parameters that affect the behavior of the streaming mode. These parameters are listed in the parameters table above.

{% hint style="danger" %}
**Cache Name**

Make sure you specify a target cache for streaming as an argument to the `cache=` parameter in the JDBC connection string. If a cache is not specified or does not match the table used in streaming DML statements, updates will be ignored.
{% endhint %}

The parameters cover almost all of the settings of a general `IgniteDataStreamer` and allow you to tune the streamer according to your needs. Please refer to the [Data Streaming](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/data-streaming) section for more information on how to configure the streamer.

{% hint style="info" %}
**Time Based Flushing**

By default, the data is flushed when either a connection is closed or `streamingPerNodeBufferSize` is met. If you need to flush the data more frequently, adjust the `streamingFlushFrequency` parameter.
{% endhint %}

```java
// Register JDBC driver.
   Class.forName("org.apache.ignite.IgniteJdbcDriver");

   // Opening a connection in the streaming mode and time based flushing set.
   Connection conn = DriverManager.getConnection("jdbc:ignite:cfg://streaming=true:streamingFlushFrequency=1000@file:///etc/config/ignite-jdbc.xml");

   PreparedStatement stmt = conn.prepareStatement(
     "INSERT INTO Person(_key, name, age) VALUES(CAST(? as BIGINT), ?, ?)");

   // Adding the data.
   for (int i = 1; i < 100000; i++) {
         // Inserting a Person object with a Long key.
         stmt.setInt(1, i);
         stmt.setString(2, "John Smith");
         stmt.setInt(3, 25);

         stmt.execute();
   }

   conn.close();

   // Beyond this point, all data is guaranteed to be flushed into the cache.

```

## Example

To start processing the data located in the cluster, you need to create a JDBC `Connection` object using one of the methods below:

```java
// Register JDBC driver.
Class.forName("org.apache.ignite.IgniteJdbcDriver");

// Open JDBC connection (cache name is not specified, which means that we use default cache).
Connection conn = DriverManager.getConnection("jdbc:ignite:cfg://file:///etc/config/ignite-jdbc.xml");
```

Right after that you can execute your SQL `SELECT` queries:

```java
// Query names of all people.
ResultSet rs = conn.createStatement().executeQuery("select name from Person");

while (rs.next()) {
    String name = rs.getString(1);
}

```

```java
// Query people with specific age using prepared statement.
PreparedStatement stmt = conn.prepareStatement("select name, age from Person where age = ?");

stmt.setInt(1, 30);

ResultSet rs = stmt.executeQuery();

while (rs.next()) {
    String name = rs.getString("name");
    int age = rs.getInt("age");
}
```

You can use DML statements to modify the data.

### INSERT

```java
// Insert a Person with a Long key.
PreparedStatement stmt = conn.prepareStatement("INSERT INTO Person(_key, name, age) VALUES(CAST(? as BIGINT), ?, ?)");

stmt.setInt(1, 1);
stmt.setString(2, "John Smith");
stmt.setInt(3, 25);

stmt.execute();
```

### MERGE

```java
// Merge a Person with a Long key.
PreparedStatement stmt = conn.prepareStatement("MERGE INTO Person(_key, name, age) VALUES(CAST(? as BIGINT), ?, ?)");

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
