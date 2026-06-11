---
description: >-
  Failover and load balancing in MariaDB Connector/J 2.x support sequential,
  loadbalance, replication, and aurora modes across multi-master, master-slave,
  and Amazon Aurora clusters.
---

# Failover and High availability with MariaDB Connector/J for 2.x driver

_This guide will cover:_

* The load balancing and high availability concepts in MariaDB Connector/J for versions before 3.0
* The different options.

{% hint style="info" %}
This concerns only the version _before_ 3.0. See [documentation for 3+ version](failover-and-high-availability-with-mariadb-connector-j.md)
{% endhint %}

Failover and high availability were introduced in 1.2.0.

## Load balancing and failover distinction

Failover occurs when a connection to a primary database server fails, and the connector opens up a connection to another database server.

For example, server A has the current connection. After a failure (server crash, network down …), the connection will switch to another server (B).

Load balancing allows load (read and write) to be distributed over multiple servers.

## Replication cluster type

In MariaDB (and MySQL) replication, there are 2 different replication roles:

* Master role: Database server that permits read and write operations
* Slave role: Database server that permits only read operations

This document describes the configuration and implementation for 3 types of clusters:

* Multi-Master replication cluster. All hosts have a master replication role. (example: Galera)
* Master/slaves cluster: one host has the master replication role with multiple hosts in the slave replication role.
* Hybrid cluster: multiple hosts in the master replication role with multiple hosts in the slave replication role.

## Load balancing implementation

### Random picking

When initializing a connection or after a failed connection, the connector will attempt to connect to a host with a certain role (slave/master).\
The connection is selected randomly among the valid hosts. Thereafter, all statements will run on that database server until the connection is closed (or fails).

The load-balancing will include a pooling mechanism.\
Example: when creating a pool of 60 connections, each one will use a random host. With 3 master hosts, the pool will have about 20 connections to each host.

### Master/slave distributed load

For a cluster composed of masters and slaves on connection initialization, there will be 2 underlying connections: one with a master host, another with a slave host. Only one connection is used at a time.\
For a cluster composed of master hosts only, each connection has only one underlying connection.\
The load will be distributed due to the random distribution of connections..

### Master/slave connection selection

It’s the application that has to decide to use a master or slave connection (the master connection is set by default).\
Switching the type of connection is done by using the JDBC [connection.setReadOnly(boolean readOnly)](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#setReadOnly\(boolean\)) method. Setting read-only to true will use the slave connection; false, the master connection.

Example in standard Java:

```java
connection = DriverManager.getConnection("jdbc:mysql:replication://master1,slave1/test");
stmt = connection.createStatement();
stmt.execute("SELECT 1"); // will execute query on the underlying master1 connection
connection.setReadOnly(true);
stmt.execute("SELECT 1"); // will execute query on the underlying slave1 connection
```

Some frameworks render this kind of operation easier, for example Spring [@transactionnal](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/transaction/annotation/Transactional.html#readOnly--) readOnly parameter (since Spring 3.0.1).\
In this example, setting readOnly to false will call the connection.setReadOnly(false) and therefore use the master connection.

```java
@Autowired
private EntityManager em;

@Transactional(readOnly = false, propagation = Propagation.REQUIRED)
public void createContacts() {
  Contact contact1 = new Contact();
  contact1.setGender("M");
  contact1.setName("JIM");
  em.persist(contact1);
}
```

Generated Spring Data repository objects use the same logic: the find\* method will use the slave connection, and other use master connection without having to explicitly set that for each method.

On a cluster with master hosts only, the use of connection.setReadOnly(true) does not change the connection, but if the database version is 10.0.0 or higher, the session is set to readOnly if option assureReadOnly is set to true, which means that any write query will throw an exception.

## Failover behaviour

### Basic failover

When no failover/high availability parameter is set, the failover support is basic. Before executing a query, if the connection with the host is discarded, the connection will be reinitialized if parameter “autoReconnect” is set to true.

### Standard failover

When a failover/high availability parameter is set. Check the [configuration](failover-and-high-availability-with-mariadb-connector-j-for-2x-driver.md#configuration) section for an overview of how to set the parameters.

The failure can be multiple fail causes. When a failure occurs, many things will be done:

* The failed host address will be put on a blacklist (shared by JVM). This host will not be used for the amount of time defined by the “loadBalanceBlacklistTimeout” parameter (default to 50 seconds). The only time a blacklisted address can be used is if all hosts of the same type (master/slave) are blacklisted.
* The connector will check the connection (with the MySQL [ping protocol](https://dev.mysql.com/doc/internals/en/com-ping.html)). If the connection is back, is not read-only, and is in a transaction, the transaction will be rolled back (there is no way to know if the last query has been received by the server and executed).
* If the failure relates to a slave connection
  * If the master connection is still active, the master connection will be used immediately.\
    The query that was read-only will be relaunched, and the connector will not throw any exception.\
    A "failover" thread will be launched to attempt to reconnect a slave host.\
    (If the query was a prepared query, this query will be re-prepared before execution.)
  * If the master connection is not active, the driver will attempt to create a new master or slave connection with a [connection loop](failover-and-high-availability-with-mariadb-connector-j-for-2x-driver.md#connection-loop).\
    If any connection is found, the query will be relaunched; if not, an SQLException with sqlState like “08XXX” will be thrown.
* If the failure relates to a master connection, the driver will attempt to create a new master connection with a [connection loop](failover-and-high-availability-with-mariadb-connector-j-for-2x-driver.md#connection-loop), so the connection object will be immediately reusable.\\
  * On failure, an SQLException with be thrown with SQLState "08XXX". If using a pool, this connection will be discarded.
  * on success,
    * if possible query will be relaunched without throwing error (if was using a slave connection, or was a SELECT query not in a transaction for example).
    * if not possible, an SQLException with be thrown with SQLState "25S03".
* When throwing an SQLException with SQLState "08XXX", the connection will be marked as closed.
* A “failover” thread will be launched to attempt to reconnect failing connection if connection is not closed.

It’s up to the application to take measures to handle SQLException. See details in the [application concerns](failover-and-high-availability-with-mariadb-connector-j-for-2x-driver.md#application-concerns).

1. Connection loop\
   When initializing a connection or after a failure, the driver will launch a connection loop. The only case when this connection loop will not be executed is when a failure occurred on a slave with an active master.\
   This connection loop will try to connect to a valid host until finding a new connection or until the number of connections exceeds the parameter “retriesAllDown” value (default to 120).

This loop will attempt to connect sequentially to hosts in the following order:

For a master connection :

* random connect to master host not blacklisted
* random connect to master blacklisted

For a slave connection :

* random connect to slave host not blacklisted
* random connect to master host not blacklisted (if no active master connection)
* random connect to the slave blacklisted
* random connect to master host blacklisted (if no active master connection)\
  The sequence stops as soon as all the underlying needed connections are found. Every time an attempt fails, the host will be blacklisted.\
  If after an entire loop a master connection is missing, the connection will be marked as closed.

## Additional threads

### Failover reconnection threads

A thread pool is created in case of a master/slave cluster, the size is defined according to the number of connection.\
After a failure on a slave connection, readonly operations are temporary executed on the master connection. Some “failover threads” will try to reconnect the failed underlying connections.\
When a new slave connection is retrieved, this one will be immediately used if connection was still in read-only mode.

### Connection validation thread

An additional thread is created when setting the option "validConnectionTimeout". This thread will very that connections are all active. This is normally done by pool that call [Connection.isValid()](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#isValid\(int\)).

## Application concerns

When a failover happen a SQLException with sqlState like "08XXX" or "25S03" may be thrown.

Here are the different connection error codes:

<table><thead><tr><th width="155">Code</th><th>Condition</th></tr></thead><tbody><tr><td>08000</td><td>connection exception</td></tr><tr><td>08001</td><td>SQL client unable to establish an SQL connection</td></tr><tr><td>08002</td><td>connection name in use</td></tr><tr><td>08003</td><td>connection does not exist</td></tr><tr><td>08004</td><td>SQL server rejected SQL connection</td></tr><tr><td>08006</td><td>connection failure</td></tr><tr><td>08007</td><td>transaction resolution unknown</td></tr><tr><td>25S03</td><td>invalid transaction state-transaction is rolled back</td></tr></tbody></table>

A connection pool will detect connection error in SQLException (SQLState begin with "08"), and this connection will be discarded from pool.

When a failover occurs, the connector cannot know if the last request has been received by the database server and executed. Applications may have failover design to handle these particular cases:

* If the application was in autoCommit mode (not recommended), the last query may have been executed and committed. The application will have no possibility to know that but the application will be functional.
* If not in autoCommit mode, the query has been launched in a transaction that will not be committed. Depending of what caused the exception, the host may have the connection open on his side during a certain amount of time. Take care of [transaction isolation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set-transaction) level that may lock too much rows.

## Configuration

(See [About MariaDB java connector](about-mariadb-connector-j.md) for all connection parameters)\
JDBC connection string format is :

```java
jdbc:(mysql|mariadb):[replication:|sequential:|loadbalance:|aurora:]//<hostDescription>[,<hostDescription>...]/[database][?<key1>=<value1>[&<key2>=<value2>]...]
```

The standard option "connectTimeout" defines the socket connection timeout. By default, this option is set to 0 (no timeout).

Since there are many servers, setting this option to a small amount of time make sense.\
During the [connection loop phase](failover-and-high-availability-with-mariadb-connector-j-for-2x-driver.md#connection-loop), the driver will try to connect to the server sequentially until the creation of an active connection.

Set this option to a small value (such as 2000ms - to be set according to your environment) which will permit rejecting a faulty server quickly.

### Failover and Load Balancing Modes

Each parameter corresponds to a specific use case:

<table><thead><tr><th width="144">Mode</th><th>Description</th></tr></thead><tbody><tr><td>sequential</td><td>This mode supports connection failover in a multi-master environment, such as MariaDB Galera Cluster. This mode does not support load-balancing reads on slaves. The connector will try to connect to hosts in the order in which they were declared in the connection URL, so the first available host is used for all queries.For example, let's say that the connection URL is the following: jdbc:mariadb:sequential:host1,host2,host3/testdbWhen the connector tries to connect, it will always try host1 first. If that host is not available, then it will try host2. etc. When a host fails, the connector will try to reconnect to hosts in the same order.This mode has been available since <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/java/1.3/1.3.0">MariaDB Connector/J 1.3.0</a></td></tr><tr><td>loadbalance</td><td>This mode permits load-balancing connection in a multi-master environment, such as MariaDB Galera Cluster. This mode does not support load-balancing reads on slaves. The connector performs load-balancing for all queries by randomly picking a host from the connection URL for each connection, so queries will be load-balanced as a result of the connections getting randomly distributed across all hosts.This mode has been available since <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/java/1.2/1.2.0">MariaDB Connector/J 1.2.0</a></td></tr><tr><td>replication</td><td>This mode supports connection failover in a master-slave environment, such as a MariaDB Replication cluster. The mode supports environments with one or more masters. This mode does support load-balancing reads on slaves if the connection is set to read-only before executing the read. The connector performs load-balancing by randomly picking a slave from the connection URL to execute read queries for a connection.This mode has been available since <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/java/1.2/1.2.0">MariaDB Connector/J 1.2.0</a></td></tr><tr><td>aurora</td><td>This mode supports connection failover in an Amazon Aurora cluster. This mode does support load-balancing reads on slave instances if the connection is set to read-only before executing the read. The connector performs load-balancing by randomly picking a slave instance to execute read queries for a connection.This mode has been available since <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/java/1.2/1.2.0">MariaDB Connector/J 1.2.0</a></td></tr></tbody></table>

### Failover and Load Balancing Parameters

<table><thead><tr><th width="206">Parameter</th><th>Description</th></tr></thead><tbody><tr><td>autoReconnect</td><td>When this parameter is enabled, when a failover and Load Balancing Mode are not in use, the connector will simply try to reconnect to its host after a failure. This is referred to as basic failover. When this parameter is enabled, when a Failover and Load Balancing Mode is in use, the connector will blacklist the failed host and try to connect to a different host of the same type. This is referred to as Standard Failover. Default is false. since 1.1.7</td></tr><tr><td>retriesAllDown</td><td>When the connector is performing a failover and all hosts are down, this parameter defines the maximum number of connection attempts the connector will make before throwing an exception.Default: 120 seconds.since 1.2.0</td></tr><tr><td>failoverLoopRetries</td><td>When the connector is searching silently for a valid host, this parameter defines the maximum number of connection attempts the connector will make before throwing an exception.This parameter differs from the "retriesAllDown" parameter because this silent search is used in situations where the connector can temporarily workaround the problem, such as by using the master connection to execute reads when the slave connection fails.Default: 120.since 1.2.0</td></tr><tr><td>validConnectionTimeout</td><td>When multiple hosts are configured, the connector verifies that the connections haven't been lost after this much time in seconds has elapsed.When this parameter is set to 0, no verification will be done. Default:120 secondssince 1.2.0</td></tr><tr><td>loadBalanceBlacklistTimeout</td><td>When a connection fails, this host will be blacklisted for the amount of time defined by this parameter.When connecting to a host, the driver will try to connect to a host in the list of non-blacklisted hosts and, only if none are found, attempt blacklisted ones.This blacklist is shared inside the classloader.Default: 50 seconds.since 1.2.0</td></tr><tr><td>assureReadOnly</td><td>When this parameter enabled when a Failover and Load Balancing Mode is in use, and a read-only connection is made to a host, assure that this connection is in read-only mode by setting the session to read-only.Default to false.Since 1.3.0</td></tr><tr><td>allowMasterDownConnection</td><td>When the replication Failover and Load Balancing Mode is in use, allow the creation of connections when the master is down. If no masters are available, then the default connection will be a slave, and Connection.isReadOnly() will return true. Default: false. Since 2.2.0</td></tr></tbody></table>

## Specifics for Amazon Aurora

Amazon Aurora is a Master/Slaves cluster composed of one master instance with a maximum of 15 slave instances. Amazon Aurora includes automatic promotion of a slave instance in case of the master instance failing. The MariaDB connector/J implementation for Aurora is specific to handle this automatic failover.

To permit development/integration on a single-node cluster, only one host can be defined.\
In this case, the driver behaves as for the configuration **failover**.

### Aurora failover implementation

Aurora failover management steps :

* Instance A is in write replication mode, instance B and C are in read replication mode.
* Instance A fails.
* Aurora detects A failure, and promote instance B in write mode. Instance C will change his master to use B.
* Cluster end-point will change to instance B end-point.
* Instance A will recover and be in read replication mode.

### Aurora configuration

#### Aurora endpoints and discovery

Every Aurora instance has a specific endpoint, i.e., an URL that identifies the host. Those endpoints look like `xxx.yyy.zzz.rds.amazonaws.com`.

There is another endpoint named "cluster endpoint" (format `xxx.cluster-yyy.zzz.rds.amazonaws.com`), which is assigned to the current master instance and will change when a new master is promoted.

In versions before 1.5.1, cluster endpoint use was discouraged, since when a failover occurs, this cluster endpoint can point for a limited time to a host that isn't the current master any more. The old recommendation was to list all specific end-points.\
This kind of url string will still work, but now, recommended url string has to use only cluster endpoint.

Driver will automatically discover master and slaves of this cluster from current cluster end-point during connection time. This permits adding new replicas to the cluster instance which will be discovered without changing driver configuration.

This discovery appends at connection time, so if you are using pool framework, check if this framework as a property that controls the maximum lifetime of a connection in the pool, and set a value to avoid infinite lifetime. When this lifetime is reached, pool will discard the current connection, and create a new one (if needed). New connections will use the new replicas. (If connections are never discarded, new replicas will begin to be used only when a failover occur)

#### JDBC connection string

The implementation is activated by specifying the “aurora” failover parameter.\
Recommended connection string is using cluster end-point:

```java
jdbc:(mysql|mariadb):aurora://[clusterInstanceEndPoint[:port]]/[database][?<key1>=<value1>[&<key2>=<value2>]...]
```

Before driver version 1.5.1, the connection string has to list all end-points:

```java
jdbc:(mysql|mariadb):aurora://[instanceEndPoint[:port]][,instanceEndPoint[:port]...]/[database][?<key1>=<value1>[&<key2>=<value2>]...]
```

If setting many endpoints, the replication role of each instance must not be defined for Aurora, because the role of each instance changes over time. The driver will check the instance role after connection initialization.

Example of connection string

```java
jdbc:mysql:aurora://cluster.cluster-xxxx.us-east-1.rds.amazonaws.com/db
```

Another difference is the option "socketTimeout" that defaults to 10 seconds, meaning that - if not changed - queries exceeding 10 seconds will throw exceptions.

### Aurora connection loop

When searching for the master instance and connecting to a slave instance, the connection order will be:

* Every Aurora instance knows the hostname of the current master. If the host has been described using their instance endpoint, that will permit knowing the master instance and connecting directly to it.
* If this isn’t the current master (because using IP, or possibly after a failover between step 2 and 3), the loop will connect randomly the other not blacklisted instance (minus the current slave instance).
* Connect randomly to a blacklisted instance.

When searching for a slave instance, the loop connection order will be:

* random not blacklisted instances (excluding the current host if connected).
* random blacklisted instances .\
  The loop will retry until the connections are found or the value of the “retriesAllDown” parameter is exceeded.

### Aurora master verification

Without any query during the time defined by the validConnectionTimeout parameter (defaults to 120s), and if not set to 0, a verification will be done that the replication role of the underlying connections hasn't changed.

### Aurora connection validation thread

Aurora is a specific [connection validation thread](failover-and-high-availability-with-mariadb-connector-j-for-2x-driver.md#connection-validation-thread) implementation. Since the role of each instance can change over time, this will validate that connections are active AND roles have not changed.

{% @marketo/form formId="4316" %}
