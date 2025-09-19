# MaxScale Hintfilter

## Hintfilter

* [Hint Syntax](maxscale-hintfilter.md#hint-syntax)
  * [Comments and comment types](maxscale-hintfilter.md#comments-and-comment-types)
  * [Hint body](maxscale-hintfilter.md#hint-body)
    * [Routing destination hints](maxscale-hintfilter.md#routing-destination-hints)
      * [Route to primary](maxscale-hintfilter.md#route-to-primary)
      * [Route to replica](maxscale-hintfilter.md#route-to-replica)
      * [Route to named server](maxscale-hintfilter.md#route-to-named-server)
      * [Route to last used server](maxscale-hintfilter.md#route-to-last-used-server)
      * [Name-value hints](maxscale-hintfilter.md#name-value-hints)
  * [Hint stack](maxscale-hintfilter.md#hint-stack)
* [Prepared Statements](maxscale-hintfilter.md#prepared-statements)
  * [Binary Protocol](maxscale-hintfilter.md#binary-protocol)
  * [Text Protocol](maxscale-hintfilter.md#text-protocol)
* [Examples](maxscale-hintfilter.md#examples)
  * [Routing SELECT queries to primary](maxscale-hintfilter.md#routing-select-queries-to-primary)

## Hint Syntax

**Note:** If a query has more than one comment only the first comment is
processed. Always place any MaxScale related comments first before any other
comments that might appear in the query.

### Comments and comment types

The client connection will need to have comments enabled. For example the`mariadb` and `mysql` command line clients have comments disabled by default and
they need to be enabled by passing the `--comments` or `-c` option to it. Most,
if not all, connectors keep all comments intact in executed queries.

```
# The --comments flag is needed for the command line client
mariadb --comments -u my-user -psecret -e "SELECT @@hostname -- maxscale route to server db1"
```

For comment types, use either `--` (notice the whitespace after the double
hyphen) or `#` after the semicolon or `/* ... */` before the semicolon.

Inline comment blocks, i.e. `/* .. */`, do not require a whitespace character
after the start tag or before the end tag but adding the whitespace is advised.

### Hint body

All hints must start with the `maxscale` tag.

```
-- maxscale <hint body>
```

The hints have two types, ones that define a server type and others that contain
name-value pairs.

#### Routing destination hints

These hints will instruct the router to route a query to a certain type of a
server.

```
-- maxscale route to [master | slave | server <server name>]
```

**Route to primary**

```
-- maxscale route to master
```

A `master` value in a routing hint will route the query to a primary server. This
can be used to direct read queries to a primary server for a up-to-date result
with no replication lag.

**Route to replica**

```
-- maxscale route to slave
```

A `slave` value will route the query to a replica server. Please note that the
hints will override any decisions taken by the routers which means that it is
possible to force writes to a replica server.

**Route to named server**

```
-- maxscale route to server <server name>
```

A `server` value will route the query to a named server. The value of`<server name>` needs to be the same as the server section name in
maxscale.cnf. If the server is not used by the service, the hint is ignored.

**Route to last used server**

```
-- maxscale route to last
```

A `last` value will route the query to the server that processed the last
query. This hint can be used to force certain queries to be grouped to the same
server.

**Name-value hints**

```
-- maxscale <param>=<value>
```

These control the behavior and affect the routing decisions made by the
router. Currently the only accepted parameter is the readwritesplit parameter`max_slave_replication_lag`. This will route the query to a server with a lower
replication lag than this parameter's value.

### Hint stack

Hints can be either single-use hints, which makes them affect only one query, or
named hints, which can be pushed on and off a stack of active hints.

Defining named hints:

```
-- maxscale <hint name> prepare <hint content>
```

Pushing a hint onto the stack:

```
-- maxscale <hint name> begin
```

Popping the topmost hint off the stack:

```
-- maxscale end
```

You can define and activate a hint in a single command using the following:

```
-- maxscale <hint name> begin <hint content>
```

You can also push anonymous hints onto the stack which are only used as long as
they are on the stack:

```
-- maxscale begin <hint content>
```

## Prepared Statements

The hintfilter supports routing hints in prepared statements for both the`PREPARE` and `EXECUTE` SQL commands as well as the binary protocol prepared
statements.

### Binary Protocol

With binary protocol prepared statements, a routing hint in the prepared
statement is applied to the execution of the statement but not the preparation
of it. The preparation of the statement is routed normally and is sent to all
servers.

For example, when the following prepared statement is prepared with the MariaDB
Connector-C function `mariadb_stmt_prepare` and then executed with`mariadb_stmt_execute` the result is always returned from the primary:

```
SELECT user FROM accounts WHERE id = ? -- maxscale route to master
```

Support for binary protocol prepared statements was added in MaxScale 6.0
([MXS-2838](https://jira.mariadb.org/browse/MXS-2838)).

The protocol commands that the routing hints are applied to are:

* COM\_STMT\_EXECUTE
* COM\_STMT\_BULK\_EXECUTE
* COM\_STMT\_SEND\_LONG\_DATA
* COM\_STMT\_FETCH
* COM\_STMT\_RESET

Support for direct execution of prepared statements was added in MaxScale
6.2.0. For example the MariaDB Connector-C uses direct execution when`mariadb_stmt_execute_direct` is used.

### Text Protocol

Text protocol prepared statements (i.e. the `PREPARE` and `EXECUTE` SQL
commands) behave differently. If a `PREPARE` command has a routing hint, it will
be routed according to the routing hint. Any subsequent `EXECUTE` command will
not be affected by the routing hint in the `PREPARE` statement. This means they
must have their own routing hints.

The following example is the recommended method of executing text protocol
prepared statements with hints:

```
PREPARE my_ps FROM 'SELECT user FROM accounts WHERE id = ?';
EXECUTE my_ps USING 123; -- maxscale route to master
```

The `PREPARE` is routed normally and will be routed to all servers. The`EXECUTE` will be routed to the primary as a result of it having the `route to master` hint.

## Examples

### Routing `SELECT` queries to primary

In this example, MariaDB MaxScale is configured with the readwritesplit router
and the hint filter.

```
[ReadWriteService]
type=service
router=readwritesplit
servers=server1,server2
user=maxuser
password=maxpwd
filters=Hint

[Hint]
type=filter
module=hintfilter
```

Behind MariaDB MaxScale is a primary server and a replica server. If there is
replication lag between the primary and the replica, read queries sent to the replica
might return old data. To guarantee up-to-date data, we can add a routing hint
to the query.

```
INSERT INTO table1 VALUES ("John","Doe",1);
SELECT * FROM table1; -- maxscale route to master
```

The first INSERT query will be routed to the primary. The following SELECT query
would normally be routed to the replica but with the added routing hint it will be
routed to the primary. This way we can do an INSERT and a SELECT right after it
and still get up-to-date data.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
