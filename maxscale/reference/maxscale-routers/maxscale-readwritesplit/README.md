---
description: >-
  Optimize query performance with read-write splitting. This router directs
  write queries to the primary server and load balances read queries across
  available replica nodes.
---

# MaxScale Readwritesplit

## Overview

This document provides a short overview of the **readwritesplit** router module and its intended use case scenarios. The router settings are described in [MaxScale Readwritesplit Settings](readwritesplit-settings.md). A list of current limitations of the module is included and use examples are provided.

The **readwritesplit** router is designed to increase the read-only processing capability of a cluster while maintaining consistency. This is achieved by splitting the query load into read and write queries. Read queries, which do not modify data, are spread across multiple nodes while all write queries will be sent to a single node.

The router is designed to be used with a traditional Primary-Replica replication cluster. It automatically detects changes in the primary server and will use the current primary server of the cluster. With a Galera cluster, one can achieve a resilient setup and easy primary failover by using one of the Galera nodes as a Write-Primary node, where all write queries are routed, and spreading the read load over all the nodes.

## Interaction with servers in `Maintenance` and `Draining` state

When a server that readwritesplit uses is put into maintenance mode, any ongoing requests are allowed to finish before the connection is closed. If the server that is put into maintenance mode is a primary, open transaction are allowed to complete before the connection is closed. Note that this means neither idle session nor long-running transactions will be closed by readwritesplit. To forcefully close the connections, use the following command:

```
maxctrl set server <server> maintenance --force
```

If a server is put into the `Draining` state while a connection is open, the connection will be used normally. Whenever a new connection needs to be created, whether that be due to a network error or when a new session being opened, only servers that are neither `Draining` nor `Drained` will be used.

## Configuration

Readwritesplit router-specific settings are specified in the configuration file of MariaDB MaxScale in its specific section. The section can be freely named but the name is used later as a reference in a listener section.

For more details about the standard service parameters, refer to the [Configuration Guide](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md).

All router parameters can be configured at runtime. Use`maxctrl alter service` to modify them. The changed configuration will only be taken into use by new sessions.

## Settings

Every readwritesplit setting, with its type, default, and behavior, is described in [MaxScale Readwritesplit Settings](readwritesplit-settings.md).

## Router Diagnostics

The `router_diagnostics` output for a readwritesplit service contains the following fields.

* `queries`: Number of queries executed through this service.
* `route_master`: Number of writes routed to primary.
* `route_slave`: Number of reads routed to replicas.
* `route_all`: Number of session commands routed to all servers.
* `rw_transactions`: Number of explicit read-write transactions.
* `ro_transactions`: Number of explicit read-only transactions.
* `replayed_transactions`: Number of replayed transactions.
* `server_query_statistics`: Statistics for each configured and used server consisting of the following fields.
* `id`: Name of the server
* `total`: Total number of queries.
* `read`: Total number of reads.
* `write`: Total number of writes.
* `avg_sess_duration`: Average duration of a client session to this server.
* `avg_sess_active_pct`: Average percentage of time client sessions were active. 0% means connections were opened but never used.
* `avg_selects_per_session`: Average number of selects per session.

## Server Ranks

The general rule with server ranks is that primary servers will be used before secondary servers. Readwritesplit is an exception to this rule. The following rules govern how readwritesplit behaves with servers that have different ranks.

* Sessions will use the current primary server as long as possible. This means that sessions with a secondary primary will not use the main primary as long as the secondary primary is available.
* All replica connections will use the same rank as the primary connection. Any stale connections with a different rank than the primary will be discarded.
* If no primary connection is available and `master_reconnection` is enabled, a connection to the best primary is created. If the new primary has a different priority than existing connections have, the connections with a different rank will be discarded.
* If open connections exist, these will be used for routing. This means that if the primary is lost but the session still has replica servers with the same rank, they will remain in use.
* If no open connections exist, the servers with the best rank will used.

## Routing hints

The readwritesplit router supports routing hints. For a detailed guide on hint syntax and functionality, please read [this](../../maxscale-filters/maxscale-hintfilter.md) document.

The `route to master` hint can be used to treat a read as if it was a write. This is useful when a read done outside of a transaction depends on a previously committed transaction that may not have replicated to the other servers in the cluster. Alternative automated ways of solving this are [`causal_reads`](readwritesplit-settings.md#causal_reads) and [`sync_transaction`](readwritesplit-settings.md#sync_transaction).

All routing hints are ignored if they are done inside of a transaction. This is done to guarantee the consistency of a transaction and to make sure that a transaction through readwritesplit behaves identically to a transaction done directly against MariaDB.

The `route to slave` hint is always ignored by readwritesplit as it is either redundant or would cause writes to be sent to the wrong server.

The `route to last` and `route to server <name>` hints only work on reads. If they are used on a write and the target server cannot be used for writes, it is treated as a retryable error if query retrying of writes is enable

## Module Commands

The readwritesplit router implements the following module commands.

### `reset-gtid`

The command resets the global GTID state in the router. It can be used with `causal_reads=global` to reset the state. This can be useful when the cluster is reverted to an earlier state and the GTIDs recorded in MaxScale are no longer valid.

The first and only argument to the command is the router name. For example, to reset the GTID state of a readwritesplit named `My-RW-Router`, the following MaxCtrl command should be used:

```
maxctrl call command readwritesplit reset-gtid My-RW-Router
```

## Examples

Examples of the readwritesplit router in use can be found in the [Tutorials](../../../mariadb-maxscale-tutorials/README.md) folder.

## Readwritesplit routing decisions

Here is a small explanation which shows what kinds of queries are routed to which type of server.

### Routing to Primary

Routing to primary is important for data consistency and because majority of writes are written to binlog and thus become replicated to replicas.

The following operations are routed to primary:

* DML statements (`INSERT`, `UPDATE`, `DELETE` etc.)
* DDL statements (`DROP`, `CREATE`, `ALTER` etc.)
* All statements within an open read-write transaction
* Stored procedure calls
* User-defined function calls
* Queries that use temporary tables created within the same session
* Queries that use sequences (`NEXT VALUE FOR seq`, `NEXTVAL(seq)` or `seq.nextval`)
* Statements that use any of the following functions:
  * `LAST_INSERT_ID()`
  * `GET_LOCK()`
  * `RELEASE_LOCK()`
  * `IS_USED_LOCK()`
  * `IS_FREE_LOCK()`
* Statements that use any of the following variables:
  * `@@last_insert_id`
  * `@@identity`
* Reads done with `causal_reads` enabled that timed out on the replica
* Replication primary commands (e.g. `SHOW MASTER STATUS`)

In addition to these, if the **readwritesplit** service is configured with the `max_replication_lag` parameter, and if all replicas suffer from too much replication lag, then statements will be routed to the primary.

#### Transaction Isolation Level Tracking

If either `session_track_transaction_info=CHARACTERISTICS` or `session_track_system_variables=tx_isolation` is configured for the MariaDB server, readwritesplit will track the transaction isolation level and lock the session to the primary when the isolation level is set to serializable. This retains the correctness of the isolation level which can otherwise cause problems.

Starting with MaxScale 23.08, once the transaction isolation level is set to something other than `SERIALIZABLE`, the session is no longer locked to the primary and returns to its normal state. Older versions of MaxScale remain locked to the primary even if the session goes out of the `SERIALIZABLE` isolation level.

### Routing to Replicas

The ability to route some statements to replicas is important because it also decreases the load targeted to _primary_. Moreover, it is possible to have multiple replicas to share the load in contrast to single primary.

The following types of queries can be routed to replicas:

* Read-only statements (i.e. `SELECT` and `SHOW`) outside of transactions with autocommit enabled that only use read-only built-in functions
* All statements within an explicit read-only transaction (`START TRANSACTION READ ONLY`)

### Routing to every session backend

A third class of statements includes those which modify session data, such as session system variables, user-defined variables, the default database, etc. We call them session commands, and they must be replicated as they affect the future results of read and write operations. They must be executed on all servers that could execute statements on behalf of this client.

Session commands include for example:

* Commands that modify the session state (`SET`, `USE`, `CHANGE USER`)
* Text protocol `PREPARE` statements
* Binary protocol prepared statements
* Other miscellaneous commands (`COM_QUIT`, `COM_PING` etc.)

**NOTE**: if variable assignment is embedded in a write statement it is routed to _primary_ only. For example, `INSERT INTO t1 values(@myvar:=5, 7)` would be routed to _primary_ only.

The router stores all of the executed session commands so that in case of a connection failure, a replacement connection can be opened and the session command history can be replayed on that new connections. The number of stored session commands depends on the router configuration. For more information, refer to the documentation of [`max_sescmd_history`](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#max_sescmd_history).

### Routing to previous target

In the following cases, a query is routed to the same server where the previous query was executed. If no previous target is found, the query is routed to the current primary.

* If a query uses the `FOUND_ROWS()` function, it will be routed to the server where the last query was executed. This is done with the assumption that a query with `SQL_CALC_FOUND_ROWS` was previously executed.
* `COM_STMT_FETCH_ROWS` will always be routed to the same server where the `COM_STMT_EXECUTE` was routed.

## Limitations

### Maximum Number of Targets

Starting with MaxScale 25.10, readwritesplit has a hard limit of 256 targets. If more than 256 targets are used in a service, only the first 256 are used.

### Routing of Read Queries to the Primary Server

Read queries are routed to the primary server in the following situations:

* Query is executed inside an open read-write transaction
* Statement includes a stored procedure or an UDF call
* If there are multiple statements inside one query e.g.`INSERT INTO ... ; SELECT LAST_INSERT_ID();`

### Prepared Statement Limitations

If a prepared statement targets a temporary table on the primary, the replica servers will fail to execute it. This will cause all replica connections to be closed (MXS-1816).

### Transaction Replay Limitations

When transaction replay is enabled, readwritesplit calculates a checksum of the server responses for each transaction. This is used to determine whether a replayed transaction was identical to the original transaction. Starting with MaxScale 23.08, a 128-bit xxHash checksum is stored for each statement that is in the transaction. Older versions of MaxScale used a single 160-bit SHA1 checksum for the whole transaction.

If the results from the replacement server are not identical when the transaction is replayed, the client connection is closed. This means that any transaction with a server specific result (e.g. `NOW()`, `@@server_id`) cannot be replayed successfully but it will still be attempted.

If a transaction reads data before updating it, the rows should be locked by using `SELECT ... FOR UPDATE`. This will prevent overlapping transactions when multiple transactions are being replayed that modify the same set of rows.

If the connection to the server where the transaction is being executed is lost when the final `COMMIT` is being executed, it is impossible to know whether the transaction was successfully committed. This means that there is a possibility for duplicate transaction execution which can result in data duplication in certain cases.

In MaxScale 23.08, the `transaction_replay_safe_commit` variable controls whether a replay is attempted or not whenever a `COMMIT` is interrupted. By default the transaction will not be replayed. Older versions of MaxScale always replayed the transaction.

Data duplication can happen with `transaction_replay_safe_commit=false` if the
transaction consists of the following statement types:

* INSERT of rows into a table that does not have an auto-increment primary key
* A "blind update" of one or more rows e.g. `UPDATE t SET c = c + 1 WHERE id = 123`
* A "blind delete" e.g. `DELETE FROM t LIMIT 100`

This is not an exhaustive list and any operations that do not check the row contents before performing the operation on them might face this problem.

In all cases the problem of duplicate transaction execution can be avoided by including a `SELECT ... FOR UPDATE` in the statement. This will guarantee that in the case that the transaction fails when it is being committed, the row is only modified if it matches the expected contents.

Similarly, a connection loss during `COMMIT` can also result in transaction replay failure. This happens due to the same reason as duplicate transaction execution but the retried transaction will not be committed. This can be considered a success case as the transaction replay detected that the results of the two transactions are different. In these cases readwritesplit will abort the transaction and close the client connection.

Statements that result in an implicit commit do not reset the transaction when `transaction_replay` is enabled. This means that if the transaction is replayed, the transaction will be committed twice due to the implicit commit being present. The exception to this are the transaction management statements such as`BEGIN` and `START TRANSACTION`: they are detected and will cause the transaction to be correctly reset.

In older versions of MaxScale, if a connection to a server is lost while a statement is being executed and the result was partially delivered to the client, readwritesplit would immediately close the session without attempting to replay the failing statement. Starting with MaxScale 23.08, this limitation no longer applies if the statement was done inside of a transaction and`transaction_replay` is enabled ([MXS-4549](https://jira.mariadb.org/browse/MXS-4549)).

If the connection to the server where a transaction is being executed is lost while a `ROLLBACK` is being executed, readwritesplit will still attempt to replay the transaction in the hopes that the real response can be delivered to the client. However, this does mean that it is possible that a rolled back transaction which gets replayed ends up with a conflict and is reported as a replay failure when in reality a rolled back transaction could be safely ignored.

#### Limitations in Session State Modifications

Any changes to the session state (e.g. autocommit state, SQL mode) done inside a transaction will remain in effect even if the connection to the server where the transaction is being executed fails. When readwritesplit creates a new connection to a server to replay the transaction, it will first restore the session state by executing all session commands that were executed. This means that if the session state is changed mid-transaction in a way that affects the results, transaction replay will fail.

The following partial transaction demonstrates the problem by using [`SQL_MODE`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) inside a transaction.

```
SET SQL_MODE='';            -- A session command
BEGIN;
SELECT "hello world";       -- Returns the string "hello world"
SET SQL_MODE='ANSI_QUOTES'; -- A session command
SELECT 'hello world';       -- Returns the string "hello world"
```

If this transaction has to be replayed the actual SQL that gets executed is the following.

```
SET SQL_MODE='';            -- Replayed session command
SET SQL_MODE='ANSI_QUOTES'; -- Replayed session command
BEGIN;
SELECT "hello world";       -- Returns an error
SELECT 'hello world';       -- Returns the string "hello world"
```

First the session state is restored by executing all commands that changed the state after which the actual transaction is replayed. Due to the fact that the `SQL_MODE` was changed mid-transaction, one of the queries will now return an error instead of the result we expected leading to a transaction replay failure.

#### Limitations in Service-to-Service Routing

In a service-to-service configuration (i.e. a service using another service in its `targets` list ), if the topmost service starts a transaction, all lower-level readwritesplit services will also behave as if a transaction is open. If a connection to a backend database fails during this, it can result in unnecessary transaction replays which in turn can end up with checksum conflicts. The recommended approach is to not use any commands inside a transaction that would be routed to more than one node.

#### Limitations in multi-statement handling

When a multi-statement query is executed through the readwritesplit router, it will always be routed to the primary. See [`strict_multi_stmt`](readwritesplit-settings.md#strict_multi_stmt) for more details.

If the multi-statement query creates a temporary table, it will not be detected and reads to this table can be routed to replica servers. To prevent this, always execute the temporary table creation as an individual statement.

#### Limitations in client session handling

Whenever a session command is executed, the type of the result that was returned by the primary server is compared to the result of all the other servers. If the command succeeded on the primary, it is expected to also succeed on all other servers and conversely, if it fails it's expected to fail on all other servers as well.

If a command produces a different result than was expected, the connection to that server is permanently discarded and no further connection attempts are made to it within the same session.

The most common case where a session command will produce a different result on a replica is when a database is created on the primary and a `USE <db>` command is executed right after it but the creation of the database hasn't had time to replicate to the replicas before the `USE <db>` command arrives.

If a `SELECT` query modifies a user variable when the `use_sql_variables_in` parameter is set to `all`, it will be routed to all backends to keep the session state consistent. For applications where this is a common pattern, the performance overhead of this can be avoided at the cost of the user variables being inconsistent by using `use_sql_variables_in=master`. This will route all queries that use user variables to the primary.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
