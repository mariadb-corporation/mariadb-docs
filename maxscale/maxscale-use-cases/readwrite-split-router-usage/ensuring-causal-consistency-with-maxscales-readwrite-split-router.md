# Ensuring Causal Consistency with MaxScale's Read/Write Split Router

The [Read/Write Split Router (readwritesplit)](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit.md) load balances read-only queries between one or more replica servers. If the replica servers are using asynchronous [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), then the data on the replica servers can sometimes lag behind the primary server. When this occurs, read-only queries that are executed on the replica servers can return stale results if they are not executed in a causally consistent manner. Causal consistency is the act of ensuring that interdependent operations maintain consistency by performing them in the same order on all servers.

To prevent this, the Read/Write Split Router can be configured to enable "causal reads", which ensures causal consistency for read-only queries. When causal reads is enabled, the Read/Write Split Router ensures that load balanced read-only queries are only executed on the replica server after all write statements previously executed on the primary server are fully replicated and applied on that specific replica server.

## Multiple MaxScale Nodes

Starting with MaxScale 22.08, the Read/Write Split Router's causal reads functionality can be used with multiple MaxScale nodes.

Example of a Causal Read
Let's say that a client does the following:

1. The client executes an [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert) statement:

```
INSERT INTO hq_sales.invoices
   (customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, '2020-05-10 12:35:10', 1087.23, 'CREDIT_CARD');
```

The router will route this statement to the primary server.

2. The client executes a [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select) statement that reads the inserted row:

```
SELECT * FROM hq_sales.invoices
   WHERE customer_id = 1
   AND invoice_date = '2020-05-10 12:35:10';
```

The router will route this statement to a replica server.

In the above example, the replica server may not replicate and apply the [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert) statement immediately. If the [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select) statement is executed before this happens, then the results of the query will not be causally consistent.

However, if causal reads is enabled, then the Read/Write Split Router will only execute the [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select) statement after the [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert) statement has been fully replicated and applied on the replica server.

## Enabling Causal Reads

Causal reads requires configuration changes on both the back-end MariaDB Servers and on the MaxScale instance.

### Enabling Causal Reads on MariaDB Server

Perform the following procedure on all MariaDB Servers used by MaxScale:

1. Choose a configuration file in which to configure your system variables and options.
   It is not recommended to make custom changes to one of the bundled configuration files. Instead, it is recommended to create a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. If you want your custom configuration file to override the bundled configuration files, then it is a good idea to prefix the custom configuration file's name with a string that will be sorted last, such as z-.

* On RHEL, CentOS, Rocky Linux, and SLES, a good custom configuration file would be: `/etc/my.cnf.d/z-custom-my.cnf`
* On Debian and Ubuntu, a good custom configuration file would be: `/etc/mysql/mariadb.conf.d/z-custom-my.cnf`

2. Set the [session\_track\_system\_variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#session_track_system_variables) system variable to last\_gtid, so that the server will track session-level changes to the value of the [last\_gtid](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#last_gtid) system variable.

It needs to be set in the configuration file in a group that will be read by [mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client), such as \[mariadb] or \[server].

For example:

```
[mariadb]
...
session_track_system_variables=last_gtid
```

3. Restart the server.

```
$ sudo systemctl restart mariadb
```

## Enabling Causal Reads on MaxScale 2.5

1. Set the causal\_reads and `causal_reads_timeout` parameters for the Read/Write Split Router in `maxscale.cnf`.
   The `causal_reads` parameter can be set to the following values:

| Value  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| none   | • Causal reads are disabled. • This is the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| local  | • Writes are locally visible. • Writes are guaranteed to be visible only to the connection that does it. Unrelated modifications done by other connections are not visible. • This mode improves read scalability at the cost of latency and reduces the overall load placed on the primary server without breaking causality guarantees.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| global | • Writes are globally visible. • If one connection writes a value, all connections to the same service will see it. • In general this mode is slower than the local mode due to the extra synchronization it has to do. This guarantees global happens-before ordering of reads when all transactions are inside a single GTID domain. • This mode gives similar benefits as the local mode in that it improves read scalability at the cost of latency.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| fast   | • This mode is similar to the local mode where it will only affect the connection that does the write. • Whereas the local mode waits for a replica server to catch up, this mode will only use servers that are known to have replicated the write. • This means that if no replica server has replicated the write, the primary server where the write was done will be used. • The value of causal\_reads\_timeout is ignored in this mode. • Currently the replication state is only updated by the [MariaDB Monitor (mariadbmon)](../../maxscale-archive/archive/mariadb-maxscale-21-06/mariadb-maxscale-2106-maxscale-21-06-monitors/maxscale-mariadb-monitor-usage/maxscale-mariadb-monitor-usage-mariadb-monitor/understanding-maxscales-mariadb-monitor.md) whenever the servers are monitored. This means that a smaller monitor\_interval provides faster replication state updates and possibly better overall usage of servers. • This mode is the inverse of the local mode in the sense that it improves read latency at the cost of read scalability while still retaining the causality guarantees for reads. |

For example:

```
[split-router]
type                     = service
router                   = readwritesplit
...
causal_reads             = local
causal_reads_timeout     = 15
The unit for the causal_reads_timeout parameter is seconds, and the default value is 10.
```

2. Restart the MaxScale instance.

```
$ sudo systemctl restart maxscale
```

## Enabling Causal Reads on MaxScale 2.4 and Before

1. Set the `causal_reads and causal_reads_timeout` parameters for the Read/Write Split Router in maxscale.cnf.

For example:

```
[split-router]
type                     = service
router                   = readwritesplit
...
causal_reads             = ON
causal_reads_timeout     = 15
The unit for the causal_reads_timeout parameter is seconds, and the default value is 10.
```

2. Restart the MaxScale instance.

```
$ sudo systemctl restart maxscale
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
