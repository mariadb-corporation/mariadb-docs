# Pool Datasource Implementation

## Pool Datasource Implementation

MariaDB Connector/J provides 2 different Datasource pool implementations:

* `MariaDbDataSource`: The basic implementation. It creates a new connection each time the `getConnection()` method is called.
* `MariaDbPoolDataSource`: A connection pool implementation. It maintains a pool of connections, and when a new connection is requested, one is borrowed from the pool.

When using MariaDbPoolDataSource, different options permit specifying the pool behaviour:

| pool               | poolName                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | maxPoolSize | minPoolSize | poolValidMinDelay | maxIdleTime | staticGlobal | useResetConnection | registerJmxPool |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------- | ----------------- | ----------- | ------------ | ------------------ | --------------- |
| pool               | Use pool. This option is useful only if not using a DataSource object, but only a connection object. Default: false. since 2.2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |             |             |                   |             |              |                    |                 |
| poolName           | Pool name that permits identifying threads.default: auto-generated as MariaDb-pool-since 2.2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |             |             |                   |             |              |                    |                 |
| maxPoolSize        | The maximum number of physical connections that the pool should contain. Default: 8. since 2.2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |             |             |                   |             |              |                    |                 |
| minPoolSize        | When connections are removed due to not being used for longer than "maxIdleTime", connections are closed and removed from the pool. "minPoolSize" indicates the number of physical connections the pool should keep available at all times. Should be less or equal to maxPoolSize.Default: maxPoolSize value. Since 2.2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |             |             |                   |             |              |                    |                 |
| poolValidMinDelay  | When asking a connection to pool, the pool will validate the connection state. "poolValidMinDelay" permits disabling this validation if the connection has been borrowed recently avoiding useless verifications in case of frequent reuse of connections. 0 means validation is done each time the connection is asked.Default: 1000 (in milliseconds). Since 2.2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |             |             |                   |             |              |                    |                 |
| maxIdleTime        | The maximum amount of time in seconds that a connection can stay in the pool when not used. This value must always be below @wait\_timeout value - 45s Default: 600 in seconds (=10 minutes), minimum value is 60 seconds. Since 2.2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |             |                   |             |              |                    |                 |
| staticGlobal       | Indicates the values of the global variables [max\_allowed\_packet](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_allowed_packet), [wait\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#wait_timeout), [autocommit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#autocommit), [auto\_increment\_increment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables), [time\_zone](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#time_zone), [system\_time\_zone](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#system_time_zone) and [tx\_isolation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#tx_isolation)) won't be changed, permitting the pool to create new connections faster.Default: false. Since 2.2.0 |             |             |                   |             |              |                    |                 |
| useResetConnection | When a connection is closed() (given back to pool), the pool resets the connection state. Setting this option, the prepare command will be deleted, session variables changed will be reset, and user variables will be destroyed when the server permits it (>= [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes), >= MySQL 5.7.3), permitting saving memory on the server if the application make extensive use of variables. Must not be used with the useServerPrepStmts optionDefault: false. Since 2.2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |             |             |                   |             |              |                    |                 |
| registerJmxPool    | Register JMX monitoring pools.Default: true. Since 2.2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |             |             |                   |             |              |                    |                 |

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

Each time a connection is asked, if the pool contains a connection that is not used, the pool will validate the connection, exchanging an empty MySQL packet with the server to ensure the connection state, then give the connection. The pool reuses connection intensively, so this validation is done only if a connection has not been used for a period (specified by the "poolValidMinDelay" option with the default value of 1000ms).

If no connection is available, the request for a connection will be put in a queue until connection timeout.\
When a connection is available (new creation or released to the pool), it will be use to satisfy queued requests in FIFO order.

A dedicated thread will handle new connection creation (one by one) to avoid a connection burst.\
This thread will create connections until "maxPoolSize" if needed with a minimum connection of "minPoolSize".

99.99% of the time, a connection is created, a few queries are executed, then the connection is released.\
Creating connections one after another permits handling sudden peaks of connection, avoiding creating lot of connections immediately and dropping them after idle timeout:

### Connection Close

On connection.close(), a connection is not really closed, but given back to the pool. The pool will then reset the connection state. The reset goal is that the next connection received from the pool has the same state as a new freshly created connection.

Reset operations:

* Rollback remaining active transactions
* Reuse the initial configured database if changed
* Default connection read-only state to false (master in a masters/slaves configuration) if changed
* Re-initialize socket timeout if changed
* autocommit reset to default
* Transaction Isolation if changed

If the server version is >= [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes) (5.7.3 for MySQL server), then the "useResetConnection" option can be used. This option will delete all user variables, and reset session variables to their initial state.

### Idle Timeout Thread

An additional thread will periodically close idle connections not used for a time corresponding to option "maxIdleTime".\
The pool will ensure recreating the connection to satisfy the "minPoolSize" option value.

This avoids keeping unused connections in the pool, overloading the server uselessly.\
If the "staticGlobal" option is set, the driver will ensure that the "maxIdleTime" option is less than the server [wait\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#wait_timeout) setting.

### Connection Performance Boost

When creating a connection, driver need to execute between 2 to 4 additional queries after socket initialization / ssl initialization depending on options.

If your application never change the following global variables don't change (rarely changed) :

* [max\_allowed\_packet](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_allowed_packet)
* [wait\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#wait_timeout)
* [autocommit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#autocommit)
* [auto\_increment\_increment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
* [time\_zone](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#time_zone)
* [system\_time\_zone](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#system_time_zone)
* [tx\_isolation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#tx_isolation)

Then you can use the option "staticGlobal". Those value will be kept in memory, avoiding any additional queries when establishing a new connection (connection creation can be 30% faster, depending on network)

Additional enhancement then : Statement.cancel, Connection.abort() methods using pool are super fast, because of reusing a connection from pool.

If any change occur, JMX method resetStaticGlobal permit to reset values from memory.

### JMX

if not disabled by option "registerJmxPool", JMX give some information on pool state. MBeans name are like "org.mariadb.jdbc.pool:type=\*".

Some statistics of current pool :

* long getActiveConnections(); -> indicate current used connection
* long getTotalConnections(); -> indicate current number of connections in pool
* long getIdleConnections(); -> indicate the number of connection currently not used
* long getConnectionRequests(); -> indicate threads number that wait for a connection.

Example accessing JMX through java :

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
