---
description: >-
  Route queries by workload type. SmartRouter directs
  transactional queries to MariaDB and analytical queries to an analytical
  backend such as ColumnStore or Exasol, for hybrid (HTAP) processing.
---

# MaxScale SmartRouter

## Overview

SmartRouter is the query router of the SmartQuery framework. Based on the type of the query, each query is routed to the server or cluster that can best handle it.

For workloads where both transactional and analytical queries are needed, SmartRouter unites the Transactional (OLTP) and Analytical (OLAP) workloads into a single entry point in MaxScale. This allows a MaxScale client to freely mix transactional and analytical queries using the same connection. This is known as Hybrid Transactional and Analytical Processing, HTAP.

The transactional cluster is typically a primary-replica MariaDB deployment fronted by [ReadWriteSplit](maxscale-readwritesplit.md). The analytical cluster can be MariaDB ColumnStore or an Exasol analytics engine — the configuration examples below use ColumnStore, but SmartRouter treats each configured target the same way and routes each query to whichever one answers it fastest.

{% hint style="info" %}
To use Exasol as the analytical cluster, configure it through the [Exasolrouter](maxscale-exasolrouter.md), which is available from MaxScale 25.10.1.
{% endhint %}

## Settings

SmartRouter is configured as a service that either routes to other MaxScale routers or plain servers. Although one can configure SmartRouter to use a plain server directly, we refer to the configured "servers" as clusters.

For details about the standard service parameters, refer to the [Configuration Guide](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md).

### `master`

* Type: target
* Mandatory: Yes
* Dynamic: No

One of the clusters must be designated as the **`master`**. All writes go to the primary cluster, which for all practical purposes should be a primary-replica ReadWriteSplit. This document does not go into details about setting up primary-replica clusters, but suffice to say, that when setting up the ColumnStore servers they should be configured to be replicas of a MariaDB server running an InnoDB engine. The ReadWriteSplit [documentation](maxscale-readwritesplit.md) has more on primary-replica setup.

#### Example

Suppose we have a Transactional service like

```
[RWS-Row]
type=service
router=readwritesplit
servers = row_server_1, row_server_2, ...
```

for which we have defined the listener

```
[RWS-Row-Listener]
type=listener
service=RWS-Row
socket=/tmp/rws-row.sock
```

That is, that service can be accessed using the socket `/tmp/rws-row.sock`.

The Analytical service could look like this

```
[RWS-Column]
type = service
router = readwritesplit
servers = column_server_1, column_server_2, ...

[RWS-Column-Listener]
type = listener
service = RWS-Column
socket = /tmp/rws-col.sock
```

Then we can define the SmartQuery service as follows

```
[SmartQuery]
type = service
router = smartrouter
targets = RWS-Row, RWS-Column
master = RWS-Row

[SmartQuery-Listener]
type = listener
service = SmartQuery
port = <port>
```

Note that the SmartQuery listener listens on a port, while the Row and Column service listeners listen on Unix domain sockets. The reason is that there is a significant performance benefit when SmartRouter accesses the services over a Unix domain socket compared to accessing them over a TCP/IP socket.

A complete configuration example can be found at the end of this document.

### `causal_reads`

* Type: [enum](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `local`
* Default: `none`

Specifies whether a read must see the writes that the same session has made
earlier. SmartRouter may route a read to a cluster other than the master, and
that cluster may be behind the master. Without causal reads, the read then
does not see the write.

* `none` (default)
  * Read causality is disabled.
* `local`
  * A read that SmartRouter would route to a cluster other than the master is
    held until that cluster has applied the latest write of the session. Writes
    made by other sessions are not waited for.

The values are the same as the corresponding values of
[readwritesplit](maxscale-readwritesplit.md#causal_reads). The other values of
that parameter are not supported by SmartRouter.

A change of the value affects only the sessions that are created after the
change. For details, see [Causal reads](#causal-reads).

{% tabs %}
{% tab title="< 26.10" %}
This feature is only available in MaxScale 26.10.0 and later.
{% endtab %}
{% endtabs %}

### `causal_reads_timeout`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

How long a read waits for a cluster to catch up with the latest write of the
session, before [causal\_reads\_on\_timeout](#causal_reads_on_timeout) is
applied. The granularity is seconds, so a timeout given in milliseconds is
rejected.

{% tabs %}
{% tab title="< 26.10" %}
This feature is only available in MaxScale 26.10.0 and later.
{% endtab %}
{% endtabs %}

### `causal_reads_on_timeout`

* Type: [enum](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `stale`, `error`
* Default: `master`

What to do with a read when the cluster has not caught up within
`causal_reads_timeout`.

* `master`
  * The read is routed to the master, which has the write. This can be much
    more expensive than running the read on the cluster that SmartRouter
    selected. A query that is best handled by an analytical cluster may take
    minutes or hours on the master, and also burden it.
* `stale`
  * The read is routed to the selected cluster anyway. The result may not
    include the latest write of the session.
* `error`
  * The read is not run anywhere and the client receives an error (1105, with
    the message "Causal read timed out"). The session remains usable. This is
    intended for cases where an up-to-date result is essential but running the
    read on the master would take too long.

{% tabs %}
{% tab title="< 26.10" %}
This feature is only available in MaxScale 26.10.0 and later.
{% endtab %}
{% endtabs %}

## Cluster selection - how queries are routed

SmartRouter keeps track of the performance, or the execution time, of queries to the clusters. Measurements are stored with the canonical of a query as the key. The canonical of a query is the sql with all user-defined constants replaced with question marks. When SmartRouter sees a read-query whose canonical has not been seen before, it will send the query to all clusters. The first response from a cluster will designate that cluster as the best one for that canonical. Also, when the first response is received, the other queries are cancelled. The response is sent to the client once all clusters have responded to the query or the cancel.

There is obviously overhead when a new canonical is seen. This means that queries after a MaxScale start will be slightly slower than normal. The execution time of a query depends on the database engine, and on the contents of the tables being queried. As a result, MaxScale will periodically re-measure queries.

The performance behavior of queries under dynamic conditions, and their effect on different storage engines is being studied at MariaDB. As we learn more, we will be able to better categorize queries and move that knowledge into SmartRouter.

## Causal reads

A client that writes and then reads expects to see what it wrote. As
SmartRouter may send the read to a cluster that is updated asynchronously, for
example by replication, that cluster may not yet have the write. With
`causal_reads=local` SmartRouter makes sure that it has.

{% tabs %}
{% tab title="< 26.10" %}
This feature is only available in MaxScale 26.10.0 and later.
{% endtab %}
{% endtabs %}

SmartRouter learns the GTID of each write that a session makes from the
master, using the same session tracking of `last_gtid` as readwritesplit. The
requirements for the master servers are the same as for the `causal_reads`
parameter of [readwritesplit](maxscale-readwritesplit.md#causal_reads).

Before a read is sent to a cluster other than the master, the GTID of the
latest write of the session is compared with the GTID position of the
cluster. If the cluster is behind, the read is held in MaxScale and the
position is checked repeatedly. The read is sent when the cluster has caught
up, or, when `causal_reads_timeout` has passed, handled according to
`causal_reads_on_timeout`. Anything else that the client sends meanwhile
waits, and is routed in order afterwards.

A read that SmartRouter has not seen before is run on all clusters, to find
out which is the fastest. If any cluster other than the master is behind, such
a read is held until all of them have caught up, so that the first answer
cannot come from a cluster that lacks the write. If the timeout is reached
with `causal_reads_on_timeout=master` or `error`, the read is not run on all
clusters and is not measured. With `stale` it is measured as usual.

Writes, and everything else that is routed to the master, which includes all
statements of a transaction, are never held.

The GTID position of a cluster comes from MaxScale's monitoring. For a
server, it is the position that its monitor reports, which is how often it is
updated. A smaller `monitor_interval` therefore makes a held read be released
sooner after the cluster has caught up. The position of a service is that of
its least up to date running server.

**Example**

```
[SmartQuery]
type = service
router = smartrouter
targets = RWS-Row, RWS-Column
master = RWS-Row
causal_reads = local
causal_reads_timeout = 5s
causal_reads_on_timeout = error
```

### Limitations of causal reads

* Only `none` and `local` are supported.
* The value of `causal_reads` is fixed when a session is created. A change
  affects only new sessions.
* If the master does not report a GTID for a write, for example because the
  binary log is disabled, there is nothing to wait for and reads are not held.
* MaxScale must be able to learn the GTID position of a cluster. The MariaDB
  Monitor and the Galera Monitor report it for servers. If a cluster never
  reports a position, every read to it is held for the entire
  `causal_reads_timeout`, so `causal_reads` should not be enabled for it.
* A held read adds latency of up to `causal_reads_timeout`. This also applies
  to the first execution of a query that SmartRouter has not seen before.

## Limitations

* `LOAD DATA LOCAL INFILE` is not supported.
* The performance data is not persisted. The measurements will be performed anew after each startup.

## Complete configuration example

```
[maxscale]

[row_server_1]
type = server
address = <ip>
port = <port>

[row_server_2]
type = server
address = <ip>
port = <port>

[Row-Monitor]
type = monitor
module = mariadbmon
servers = row_server_1, row_server_2
user = <user>
password = <password>
monitor_interval = 2000ms

[column_server_1]
type = server
address = <ip>
port = <port>

[Column-Monitor]
type = monitor
module = csmon
servers = column_server_1
user = <user>
password = <password>
monitor_interval = 2000ms

# Row Read write split
[RWS-Row]
type = service
router = readwritesplit
servers = row_server_1, row_server_2
user = <user>
password = <password>

[RWS-Row-Listener]
type = listener
service = RWS-Row
socket = /tmp/rws-row.sock

# ColumnStore Read write split
[RWS-Column]
type = service
router = readwritesplit
servers = column_server_1
user = <user>
password = <password>

[RWS-Column-Listener]
type = listener
service = RWS-Column
socket = /tmp/rws-col.sock

# Smart Query router
[SmartQuery]
type = service
router = smartrouter
targets = RWS-Row, RWS-Column
master = RWS-Row
user = <user>
password = <password>

[SmartQuery-Listener]
type = listener
service = SmartQuery
port = <port>
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
