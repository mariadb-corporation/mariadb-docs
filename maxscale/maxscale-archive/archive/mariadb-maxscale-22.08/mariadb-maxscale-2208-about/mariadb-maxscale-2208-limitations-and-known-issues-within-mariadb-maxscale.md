# Limitations and Known Issues within MariaDB MaxScale

## Limitations and Known Issues within MariaDB MaxScale

## Limitations and Known Issues within MariaDB MaxScale

This document lists known issues and limitations in MariaDB MaxScale and its\
plugins. Since limitations are related to specific plugins, this document is\
divided into several sections.

* [Limitations and Known Issues within MariaDB MaxScale](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#limitations-and-known-issues-within-mariadb-maxscale)
  * [Configuration limitations](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#configuration-limitations)
    * [Multiple MaxScales on same server](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#multiple-maxscales-on-same-server)
  * [Security limitiations](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#security-limitiations)
    * [MariaDB 10.2](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#mariadb-102)
  * [MariaDB Default Values](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#mariadb-default-values)
  * [Query Classification](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#query-classification)
    * [Transaction Boundary Detection](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#transaction-boundary-detection)
    * [XA Transactions](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#xa-transactions)
  * [Prepared Statements](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#prepared-statements)
  * [Protocol limitations](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#protocol-limitations)
    * [Limitations with MySQL/MariaDB Protocol support (MariaDBClient)](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#limitations-with-mysqlmariadb-protocol-support-mariadbclient)
  * [Authenticator limitations](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#authenticator-limitations)
    * [Limitations in the MySQL authenticator (MariaDBAuth)](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#limitations-in-the-mysql-authenticator-mariadbauth)
  * [Filter limitations](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#filter-limitations)
    * [Tee filter limitations (tee)](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#tee-filter-limitations-tee)
  * [Monitor limitations](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#monitor-limitations)
    * [Limitations with Galera Cluster Monitoring (galeramon)](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#limitations-with-galera-cluster-monitoring-galeramon)
  * [Router limitations](mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md#router-limitations)

### Configuration limitations

In versions 2.1.2 and earlier, the configuration files are limited to 1024\
characters per line. This limitation was increased to 16384 characters in\
MaxScale 2.1.3. MaxScale 2.3.0 increased this limit to 16777216 characters.

In versions 2.2.12 and earlier, the section names in the configuration files\
were limited to 49 characters. This limitation was increased to 1023 characters\
in MaxScale 2.2.13.

#### Multiple MaxScales on same server

Starting with MaxScale 2.4.0, on systems with Linux kernels 3.9 or newer due to\
the addition of SO\_REUSEPORT support, it is possible for multiple MaxScale\
instances to listen on the same network port if the directories used by both\
instances are completely separate and there are no conflicts which can cause\
unexpected splitting of connections. This will only happen if users explicitly\
tell MaxScale to ignore the default directories and will not happen in normal\
use.

### Security limitiations

#### MariaDB 10.2

The parser of MaxScale correctly parses `WITH` statements, but fails to\
collect columns, functions and tables used in the `SELECT` defining the`WITH` clause.

Consequently, the database firewall will **not** block `WITH` statements\
where the `SELECT` of the `WITH` clause refers to forbidden columns.

### MariaDB Default Values

MaxScale assumes that certain configuration parameters in MariaDB are set to\
their default values. These include but are not limited to:

* `autocommit`: Autocommit is enabled for all new connections.
* `tx_read_only`: Transactions use `READ WRITE` permissions by default.

### Query Classification

#### Transaction Boundary Detection

If a module in MaxScale requires tracking of transaction boundaries but does not\
require query classification, a custom parser is used to detect them. Currently\
the only situation in which this parser is used is when a `readconnroute`\
service uses the `cache` filter.

The custom parser detects a subset of the full SQL syntax used to start\
transactions. This means that more complex statements will not be fully parsed\
and will cause the transaction state to not match the real state on the\
database. For example, `SET @my_var = (SELECT 1), autocommit = 0` is not parsed\
by the custom parser and causes the autocommit modification to not be noticed.

#### XA Transactions

MaxScale will treat statements executed after `XA START` and before `XA END` as\
if they were executed in a normal read-write transaction started with `START TRANSACTION`. This means that only XA transactions in the ACTIVE state will be\
routed as transactions and all statements after `XA END` are routed normally.

XA transactions and normal transactions are mutually exclusive in MariaDB. This\
means that a `START TRANSACTION` command will fail if the connection already has\
an open XA transaction. MaxScale currently only inspects the SQL and deduces the\
transaction state from that. If a transaction fails to start due to an open XA\
transaction, the state in MaxScale and in MariaDB can be different and MaxScale\
will keep routing statements as if they were inside of a transaction. However,\
as this is an unlikely scenario, usually no action needs to be taken.

### Prepared Statements

For its proper functioning, MaxScale needs in general to be aware of the\
transaction state and _autocommit_ mode. In order to be that, MaxScale\
parses statements going through it.

However, if a transaction is commited or rolled back, or the autocommit\
mode is changed using a prepared statement, MaxScale will miss that and its\
internal state will be incorrect, until the transaction state or autocommit\
mode is changed using an explicit statement.

For instance, after the following sequence of commands, MaxScale will still\
think _autocommit_ is on:

```
set autocommit=1
PREPARE hide_autocommit FROM "set autocommit=0"
EXECUTE hide_autocommit
```

To ensure that MaxScale functions properly, do not commit or rollback a\
transaction or change the autocommit mode using a prepared statement.

### Protocol limitations

#### Limitations with MySQL/MariaDB Protocol support (MariaDBClient)

* Compression is not included in the server handshake.
* If a `KILL [CONNECTION] <ID>` statement is executed, MaxScale will intercept\
  it. If the ID matches a MaxScale session ID, it will be closed by sending\
  modified `KILL` commands of the same type to all backend server to which the\
  session in question is connected to. This results in behavior that is similar\
  to how MariaDB does it. If the `KILL CONNECTION USER <user>` form is given,\
  all connections with a matching username will be closed instead.
* MariaDB MaxScale does not support `KILL QUERY ID <query_id>` type\
  statements. If a query by a query ID is to be killed, it needs to be done\
  directly on the backend databases.
* Any `KILL` commands executed using a prepared statement are ignored by\
  MaxScale. If any are executed, it is highly likely that the wrong connection\
  ends up being killed.
* If a `KILL` connection kills a session that is connected to a readwritesplit\
  service that has `transaction_replay` or `delayed_retry` enabled, it is\
  possible that the query is retried even if the connection is killed. To avoid\
  this, use `KILL QUERY` instead.
* A `KILL` on one service can cause a connection from another service to be\
  closed even if it uses a different protocol.
* The change user command (COM\_CHANGE\_USER) only works with standard\
  authentication.
* If a COM\_CHANGE\_USER succeeds on MaxScale yet fails on the server the session\
  ends up in an inconsistent state. This can happen if the password of the\
  target user is changed and MaxScale uses old user account data when processing\
  the change user. In such a situation, MaxScale and server will disagree on the\
  current user. This can affect e.g. reconnections.

### Authenticator limitations

#### Limitations in the MySQL authenticator (MariaDBAuth)

* MySQL old style passwords are not supported. MySQL versions 4.1 and newer use\
  a new authentication protocol which does not support pre-4.1 style passwords.
* When users have different passwords based on the host from which they connect\
  MariaDB MaxScale is unable to determine which password it should use to connect\
  to the backend database. This results in failed connections and unusable\
  usernames in MariaDB MaxScale.

### Filter limitations

#### Tee filter limitations (tee)

The Tee filter does not support binary protocol prepared statements. The\
execution of a prepared statements through a service that uses the tee filter is\
not guaranteed to succeed on the service where the filter branches to as it does\
on the original service.

This possibility exists due to the fact that the binary protocol prepared\
statements are identified by a server-generated ID. The ID sent to the client\
from the main service is not guaranteed to be the same that is sent by the\
branch service.

### Monitor limitations

A server can only be monitored by one monitor. Two or more monitors monitoring\
the same server is considered an error.

#### Limitations with Galera Cluster Monitoring (galeramon)

The default master selection is based only on MIN(wsrep\_local\_index). This\
can be influenced with the server priority mechanic described in the [Galera Monitor](../mariadb-maxscale-2208-monitors/mariadb-maxscale-2208-galera-monitor.md) manual.

### Router limitations

Refer to individual router documentation for a list of their limitations.

CC BY-SA / Gnu FDL
