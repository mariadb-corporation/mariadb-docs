---
description: >-
  MariaDB Connector/J provides MariaDbDataSource and MariaDbPoolDataSource
  implementations with configurable pool size, idle timeout, validation
  delay, and JMX monitoring support.
---

# Pool Datasource Implementation

## Pool Datasource Implementation

MariaDB Connector/J provides 2 different Datasource pool implementations:

* `MariaDbDataSource`: The basic implementation. It creates a new connection each time the `getConnection()` method is called.
* `MariaDbPoolDataSource`: A connection pool implementation. It maintains a pool of connections, and when a new connection is requested, one is borrowed from the pool.

When using MariaDbPoolDataSource, different options permit specifying the pool behaviour:

<table><thead><tr><th width="90">pool</th><th>poolName</th><th width="133">maxPoolSize</th><th width="127">minPoolSize</th><th width="126">poolValidMinDelay</th><th>maxIdleTime</th><th>staticGlobal</th><th>useResetConnection</th><th>registerJmxPool</th></tr></thead><tbody><tr><td>pool</td><td>Use pool. This option is useful only if not using a DataSource object, but only a connection object. Default: false. since 2.2.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>poolName</td><td>Pool name that permits identifying threads.default: auto-generated as MariaDb-pool-since 2.2.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>maxPoolSize</td><td>The maximum number of physical connections that the pool should contain. Default: 8. since 2.2.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>minPoolSize</td><td>When connections are removed due to not being used for longer than "maxIdleTime", connections are closed and removed from the pool. "minPoolSize" indicates the number of physical connections the pool should keep available at all times. Should be less or equal to maxPoolSize.Default: maxPoolSize value. Since 2.2.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>poolValidMinDelay</td><td>When asking a connection to pool, the pool will validate the connection state. "poolValidMinDelay" permits disabling this validation if the connection has been borrowed recently avoiding useless verifications in case of frequent reuse of connections. 0 means validation is done each time the connection is asked.Default: 1000 (in milliseconds). Since 2.2.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>maxIdleTime</td><td>The maximum amount of time in seconds that a connection can stay in the pool when not used. This value must always be below @wait_timeout value - 45s Default: 600 in seconds (=10 minutes), minimum value is 60 seconds. Since 2.2.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>staticGlobal</td><td>Indicates the values of the global variables <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_allowed_packet">max_allowed_packet</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#wait_timeout">wait_timeout</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#autocommit">autocommit</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables">auto_increment_increment</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#time_zone">time_zone</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#system_time_zone">system_time_zone</a> and <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tx_isolation">tx_isolation</a>) won't be changed, permitting the pool to create new connections faster.Default: false. Since 2.2.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>useResetConnection</td><td>When a connection is closed() (given back to pool), the pool resets the connection state. Setting this option, the prepare command will be deleted, session variables changed will be reset, and user variables will be destroyed when the server permits it (>= <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes">MariaDB 10.2.4</a>, >= MySQL 5.7.3), permitting saving memory on the server if the application make extensive use of variables. Must not be used with the useServerPrepStmts optionDefault: false. Since 2.2.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>registerJmxPool</td><td>Register JMX monitoring pools.Default: true. Since 2.2.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

Example of use:

```java
MariaDbPoolDataSource pool = new MariaDbPoolDataSource("jdbc:mariadb://server/db?user=myUser&maxPoolSize=10");

    try (Connection connection = pool.getConnection()) {
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery("SELECT CONNECTION_ID()");
            rs.next();
            System.out.println(rs.getLong(1)); //4489
        }
    }

    try (Connection connection = pool.getConnection()) {
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery("SELECT CONNECTION_ID()");
            rs.next();
            System.out.println(rs.getLong(1)); //4489 (reused same connection)
        }
    }

    pool.close();
```

Pooling can be configured at connection level using the "pool" option: (The main difference is that there is no accessible object to close the pool if needed.)

```java
//option "pool" must be set to indicate that pool has to be used
    String connectionString = "jdbc:mariadb://server/db?user=myUser&maxPoolSize=10&pool";
    
    try (Connection connection = DriverManager.getConnection(connectionString)) {
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery("SELECT CONNECTION_ID()");
            rs.next();
            System.out.println(rs.getLong(1)); //4506 
        }
    }

    try (Connection connection = DriverManager.getConnection(connectionString)) {
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery("SELECT CONNECTION_ID()");
            rs.next();
            System.out.println(rs.getLong(1)); //4506 (reused same connection)
        }
    }
```

### Pool Connection Handling

Whenever a connection is requested, the pool checks for an available unused connection. If one is found, it validates the connection by sending an empty MySQL packet to the server to confirm its state before returning it. Since the pool reuses connections frequently, this validation is only performed if the connection has been idle for longer than the period defined by the `poolValidMinDelay` option (default: 1000 ms).

If no connection is currently available, the request will be placed in a queue and wait until the connection timeout is reached.\
When a connection becomes available—either newly created or released back into the pool—it is assigned to queued requests in FIFO order.

A dedicated thread manages the creation of new connections one at a time, preventing sudden bursts. The thread will create additional connections as needed, up to the configured amount,`maxPoolSize` while ensuring at least two `minPoolSize` connections remain available.

In the vast majority of cases (99.99%), a connection is created, used for a few queries, and then released. Creating connections sequentially allows the system to handle sudden spikes in demand without opening a large number of connections at once, which would otherwise be closed after the idle timeout.

### Connection Close

When `connection.close()` called, the connection is not terminated. Instead, it is returned to the connection pool. Before making the connection available for reuse, the pool resets its state so that the next borrower receives it in the same condition as a newly created connection.

Reset operations:

* Rolling back any active transactions.
* Restoring the initially configured default database (if it was changed).
* Setting the connection’s read-only state back to `false` master mode (in a master/slave setup) if it was modified.
* Reapplying the original socket timeout value (if it was changed).
* Resetting `autocommit` to its default value.
* Restoring the original transaction isolation level (if changed).

If the server version is >= [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes) (5.7.3 for MySQL server), then the "useResetConnection" option can be used. This option will delete all user variables and reset session variables to their initial state.

### Idle Timeout Thread

An additional thread will periodically close idle connections not used for a time corresponding to option "maxIdleTime". The pool will ensure recreating the connection to satisfy the "minPoolSize" option value.

It avoids keeping unused connections in the pool, overloading the server uselessly. If the "staticGlobal" option is set, the driver will ensure that the "maxIdleTime" option is less than the server [wait\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#wait_timeout) setting.

### Connection Performance Boost

When creating a connection, the driver needs to execute between 2 and 4 additional queries after socket initialization/SSL initialization, depending on options.

If your application never changes, the following global variables don't change (rarely changed):

* [max\_allowed\_packet](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_allowed_packet)
* [wait\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#wait_timeout)
* [autocommit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#autocommit)
* [auto\_increment\_increment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
* [time\_zone](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#time_zone)
* [system\_time\_zone](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#system_time_zone)
* [tx\_isolation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tx_isolation)

Then you can use the option "staticGlobal". Those value will be kept in memory, avoiding any additional queries when establishing a new connection (connection creation can be 30% faster, depending on the network)

Additional enhancement then: The `Statement.cancel` and `Connection.abort()` methods using the pool are super fast because of reusing a connection from the pool.

If any change occurs, the JMX method `resetStaticGlobal` permits resetting values from memory.

### JMX

If not disabled by the option "registerJmxPool", JMX gives some information on the pool state. MBeans names are like "org.mariadb.jdbc.pool:type=\*".

Some statistics of the current pool:

* long `getActiveConnections(`); -> indicate current used connection
* long `getTotalConnections(`); -> indicate current number of connections in pool
* long `getIdleConnections()`; "->" indicates the number of connections currently not used
* long `getConnectionRequests()`; -> indicates the number of threads that wait for a connection.

Example of accessing JMX through Java:

```java
try (MariaDbPoolDataSource pool = new MariaDbPoolDataSource(connUri + "jdbc:mariadb://localhost/testj?user=root&maxPoolSize=5&minPoolSize=3&poolName=PoolTestJmx")) {

    try (Connection connection = pool.getConnection()) {

        MBeanServer server = ManagementFactory.getPlatformMBeanServer();
        ObjectName filter = new ObjectName("org.mariadb.jdbc.pool:type=PoolTest*");
        Set<ObjectName> objectNames = server.queryNames(filter, null);
        ObjectName name = objectNames.iterator().next();

        System.out.println(server.getAttribute(name, "ActiveConnections"));  //1
        System.out.println(server.getAttribute(name, "TotalConnections"));   //3
        System.out.println(server.getAttribute(name, "IdleConnections"));    //2
        System.out.println(server.getAttribute(name, "ConnectionRequests")); //0
    }
}
```

{% @marketo/form formId="4316" %}
