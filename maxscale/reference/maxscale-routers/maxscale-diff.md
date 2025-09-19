---
description: Diff is a router for comparing servers.
---

# MaxScale Diff

## Diff - router for comparing servers

### Overview

The `diff`-router, hereafter referred to as _Diff_, compares the
behaviour of one MariaDB server version to that of another.

Diff will send the workload both to the server currently being used -
called _main_ - and to another server - called _other_ - whose
behaviour needs to be assessed.

The responses from _main_ are returned to the client, without
waiting for the responses from _other_. While running, Diff collects
latency histogram data that later can be used for evaluating the
behaviour of _main_ and _other_.

Although Diff is a normal MaxScale router that can be configured
manually, typically it is created using commands provided by the
router itself. As its only purpose is to compare the behaviour of
different servers, it is only meaningful to start it provided certain
conditions are fulfilled and those conditions are easily ensured using
the router itself.

#### Histogram

Diff collects latency information separately for each _canonical_
\&#xNAN;_statement_, which simply means a statement where all literals have been
replaced with question marks. For instance, the canonical statement of`SELECT f FROM t WHERE f = 10` and `SELECT f FROM t WHERE f = 20` is
in both cases `SELECT f FROM t WHERE f = ?`. The latency information
of both of those statements will be collected under the same canonical
statement.

Before starting to register histogram data, Diff will collect [samples](maxscale-diff.md#samples) from _main_ that will be used for defining the
edges and the number of bins of the histogram.

#### Discrepancies

The responses from _main_ and _other_ are considered to be different

* if the checksum of the response from _main_ and \*other differ, or
* if the response time of \_other\* is outside the boundaries of the
  histogram edges calculated from the samples from _main_.

A difference in the response time of individual queries is not a
meaningful criteria, as there for varying reasons (e.g. network
traffic) can be a significant amount of variance in the results. It
would only always cause a large number of false positives.

#### EXPLAIN

When a discrepancy is detected, an EXPLAIN statement will be executed
if the query was a DELETE, SELECT, INSERT or UPDATE. The EXPLAIN will
be executed using the same connection that was used for executing the
original statement. In the normal case, the EXPLAIN will be executed
immediately after the original statement, but if the client is
streaming requests, an other statement may have been exceuted in
between.

EXPLAINs are not always executed, but the frequency is controlled by [explain\_entries](maxscale-diff.md#explain_entries) and [explain\_period](maxscale-diff.md#explain_period). The EXPLAIN results are included in
the [output](maxscale-diff.md#reporting) of Diff.

#### QPS

While running, Diff will also collect QPS information over a sliding
window whose size is defined by [qps\_period](maxscale-diff.md#qps_period).

#### Reporting

Diff produces two kinds of output:

* Output that is generated when Diff terminates or upon [request](maxscale-diff.md#summary). That output can be visualized as explained [here](maxscale-diff.md#visualizing).
* [Optionally](maxscale-diff.md#report) Diff can continuously report queries whose
  responses from _main_ and other _differ_ as described [here](maxscale-diff.md#discrepancies).

When Diff starts it will create a directory `diff` in MaxScale's
data directory (typically `/var/lib/maxscale`). Under that it
will create a directory whose name is the same as that of the
service specified in [service](maxscale-diff.md#service). The output files are created
in that directory.

### Setup

The behaviour and usage of Diff is most easily explained
using an example.

Consider the following simple configuration that only includes
the very essential.

```
[MyServer1]
type=server
address=192.168.1.2
port=3306

[MyService]
type=service
router=readwritesplit
servers=MyServer1
...
```

There is a service `MyService` that uses a single server `MyServer1`,
which, for this example, is assumed to run MariaDB 10.5.

Suppose that the server should be upgraded to 11.2 and we want
to find out whether there would be some issues with that.

#### Prerequisites

In order to use Diff for comparing the behaviour of MariaDB 10.5
and MariaDB 11.2, the following steps must be taken.

* Install MariaDB 11.2 on a host that performance wise is
  similar to the host on which MariaDB 10.5 is running.
* Configure the MariaDB 11.2 server to replicate from the
  MariaDB 10.5 server.
* Create a server entry for the MariaDB 11.2 server in
  the MaxScale configuration.

The created entry could be something like:

```
[MariaDB_112]
type=server
address=192.168.1.3
port=3306
protocol=mariadbbackend
```

Note that this server must **not** be added to the service that
uses the original server. That is, in this example, `MariaDB_112`
must not be added to the service `MyService`.

The new server can be added to the monitor used for monitoring
the servers of the service, but that is not necessary. However,
unless it is added, `maxctrl list servers` will show the server
as being down.

With these steps Diff is ready to be used.

#### Running Diff

Diff is controlled using a number of module commands.

**Create**

Syntax: `create new-service existing-service used-server new-server`

Where:

* `new-service`: The name of the service using the Diff router, to be
  created.
* `existing-service`: The name of an existing service in whose context
  the new server is to be evaluated.
* `used-server`: A server used by `existing-service`
* `new-server`: The server that should be compared to `used-server`.

```
maxctrl call command diff create DiffMyService MyService MyServer1 MariaDB_112
{
    "status": "Diff service 'DiffMyService' created. Server 'MariaDB_112' ready to be evaluated."
}
```

With this command, preparations for comparing the server `MariaDB_112`
against the server `MyServer1` of the service `MyService` will be made.
At this point it will be checked in what kind of replication relationship`MariaDB_112` is with respect to `MyServer1`. If the steps in [prerequisites](maxscale-diff.md#prerequisites) were followed, it will be detected that`MariaDB_112` replicates from `MyServer1`.

If everything seems to be in order, the service `DiffMyService` will be
created. Settings such as _user_ and _password_ that are needed by the
service `DiffMyService` will be copied from `MyService`.

Using maxctrl we can check that the service indeed has been created.

```
maxctrl list services
┌───────────────┬────────────────┬─────────────┬───────────────────┬────────────────────────┐
│ Service       │ Router         │ Connections │ Total Connections │ Targets                │
├───────────────┼────────────────┼─────────────┼───────────────────┼────────────────────────┤
│ MyService     │ readwritesplit │ 0           │ 0                 │ MyServer1              │
├───────────────┼────────────────┼─────────────┼───────────────────┼────────────────────────┤
│ DiffMyService │ diff           │ 0           │ 0                 │ MyServer1, MariaDB_112 │
└───────────────┴────────────────┴─────────────┴───────────────────┴────────────────────────┘
```

Now the comparison can be started.

**Start**

Syntax: `start diff-service`

Where:

* `diff-service: The name of the service created in the`create\` step.

```
maxctrl call command diff start DiffMyService
{
    "sessions": {
        "suspended": 0,
        "total": 0
    },
    "state": "synchronizing",
    "sync_state": "suspending_sessions"
}
```

When Diff is started, it performs the following steps:

1. All sessions of `MyService` are suspended.
2. In the `MyService` service, the server target `MyServer1`
   is replaced with `DiffMyService`.
3. The replication from `MyServer1` to `MariaDB_112` is stopped.
4. The sessions are restarted, which will cause existing connections
   to `MyServer1` to be closed and new ones to be created, via Diff,
   to both `MyServer1` and `MariaDB_112`.
5. The sessions are resumed, which means that the client traffic
   will continue.

In the first step, all sessions that are idle will immediately
be suspended, which simply means that nothing is read from
the client socket. Sessions that are waiting for a response
from the server and sessions that have an active transaction
continue to run. Immediately when a session becomes idle,
it is suspended.

Once all sessions have been suspended, the service is rewired.
In the case of `MyService` above, it means that the target`MyServer1` is replaced with `DiffMyService`. That is, requests
that earlier were sent to `MyServer1`, will, once the sessions
are resumed, be sent to `DiffMyService`, which sends them forward
to both `MyServer1` and `MariaDB_112`.

Restarting the sessions means that the direct connections to`MyServer1` will be closed and equivalent ones created via the
service `DiffMyService`, which will also create connections
to `MariaDB_112`.

When the sessions are resumed, client requests will again be
processed, but they will now be routed via `DiffMyService`.

With maxctrl we can check that MyServer has been rewired.

```
maxctrl list services
┌───────────────┬────────────────┬─────────────┬───────────────────┬────────────────────────┐
│ Service       │ Router         │ Connections │ Total Connections │ Targets                │
├───────────────┼────────────────┼─────────────┼───────────────────┼────────────────────────┤
│ MyService     │ readwritesplit │ 0           │ 0                 │ DiffMyService          │
├───────────────┼────────────────┼─────────────┼───────────────────┼────────────────────────┤
│ DiffMyService │ diff           │ 0           │ 0                 │ MyServer1, MariaDB_112 │
└───────────────┴────────────────┴─────────────┴───────────────────┴────────────────────────┘
```

The target of `MyService` is `DiffMyService` instead of `MyServer1`
that it used to be.

The output object returned by `create` tells the current state.

```
{
    "sessions": {
        "suspended": 0,
        "total": 0
    },
    "state": "synchronizing",
    "sync_state": "suspending_sessions"
}
```

The `sessions` object shows how many sessions there are in total
and how many that currently are suspended. Since there were no
existing sessions in this example, they are both 0.

The `state` shows what Diff is currently doing. `synchronizing`
means that it is in the process of changing `MyService` to use`DiffMyService`. `sync_state` shows that it is currently in the
process of suspending sessions.

**Status**

Syntax: `status diff-service`

Where:

* `diff-service: The name of the service created in the`create\` step.

When Diff has been started, its current status can be checked with the
command `status`. The output is the same as what was returned when
Diff was started.

```
maxctrl call command diff status DiffMyService
{
    "sessions": {
        "suspended": 0,
        "total": 0
    },
    "state": "comparing",
    "sync_state": "not_applicable"
}
```

The state is now `comparing`, which means that everything is ready
and clients can connect in normal fashion.

**Summary**

Syntax: `summary diff-service`

Where:

* `diff-service: The name of the service created in the`create\` step.

While Diff is running, it is possible at any point to request
a summary.

```
maxctrl call command diff summary DiffMyService
OK
```

The summary consists of two files, one for the _main_ server and
one for the _other_ server. The files are written to a subdirectory
with the same name as the Diff service, which is created in the
subdirectory `diff` in the data directory of MaxScale.

Assuming the data directory is the default `/var/lib/maxscale`,
the directory would in this example be`/var/lib/maxscale/diff/DiffMyService`.

The names of the files will be the server name, concatenated with a
timestamp. In this example, the names of the files could be:

```
MyServer1_2024-05-07_140323.json
MariaDB_112_2024-05-07_140323.json
```

The visualization of the results is done using the [maxvisualize](maxscale-diff.md#visualizing) program.

**Stop**

Syntax: `stop diff-service`

Where:

* `diff-service: The name of the service created in the`create\` step.

The comparison can stopped with the command `stop`.

```
maxctrl call command diff stop DiffMyService
{
    "sessions": {
        "suspended": 0,
        "total": 0
    },
    "state": "stopping",
    "sync_state": "suspending_sessions"
}
```

Stopping Diff reverses the effect of starting it:

1. All sessions are suspended.
2. In the service, 'DiffMyService' is replaced with 'MyServer1'.
3. The sessions are restarted.
4. The sessions are resumed.

As the sessions have to be suspended, it may take a while
before the operation has completed. The status can be checked with
the 'status' command.

**Destroy**

Syntax: `destroy diff-service`

Where:

* `diff-service: The name of the service created in the`create\` step.

As the final step, the command `destroy` can be called to
destroy the service.

```
maxctrl call command diff destroy DiffMyService
OK
```

### Visualizing

The visualization of the data is done with the `maxvisualize` program,
which is part of the _Capture_ functionality. The visualization will
open up a browser window to show the visualization.

If no browser opens up, the visualization URL is also printed into
the command line which by default should be.

In the case of the example above, the directory where the output files
are created would be `/var/lib/maxscale/diff/MyService`. And the files
to be used when visualizing would be called something like`MyServer1_2024-05-07_140323.json` and`MariaDB_112_2024-05-07_140323.json`. The timestamp will be different
every time [summary](maxscale-diff.md#summary) is executed.

```
maxvisualize MyServer1_2024-05-07_140323.json MariaDB_112_2024-05-07_140323.json
```

The order is significant; the first argument is the baseline and the
second argument the results compared to the baseline.

### Continuous Reporting

If the value of [report](maxscale-diff.md#report) is something else but `never`, Diff
will continously log results to a file whose name is the concatenation
for the main and other server followed by a timestamp. In the example
above, the name would be something like`MyServer1_MariaDB_112_2024-02-15_152838.json`.

Each line (here expanded for readability) in the file will look like:

```
{
  "id": 1,
  "session": 1,
  "command": "COM_QUERY",
  "query": "select @@version_comment limit 1",
  "results": [
    {
      "target": "MyServer1",
      "checksum": "0f491b37",
      "rows": 1,
      "warnings": 0,
      "duration": 257805,
      "type": "resultset",
      "explain": { ... }
    },
    {
      "target": "MariaDB_112",
      "checksum": "0f491b37",
      "rows": 1,
      "warnings": 0,
      "duration": 170043,
      "type": "resultset",
      "explain": { ... }
    }
  ]
}
```

The meaning of the fields are as follows:

* id: Running number, increases for each query, but will not be in
  strict increasing order if a statement needed to be EXPLAINed and
  the following did not.
* session: The session id.
* command: The protocol packet type.
* query: The SQL of the query.
* results: Array of results.
* target: The server the result relates to.
* checksum: The checksum of the result.
* rows: How many rows were returned.
* warnings: The number of warnings.
* duration: The execution duration in nanonseconds.
* type: What type of result `resultset`, `ok` or `error`.
* explain: The result of `EXPLAIN FORMAT=JSON statement`.

Instead of an `explain` object, there may be an `explained_by` array,
containing the ids of similar statements (i.e. their canonical
statement is the same) that were EXPLAINed.

### Mode

Diff can run in a read-only or read-write mode and the mode is
deduced from the replication relationship between _main_ an&#x64;_&#x6F;ther_.

If _other_ replicates from _main_, it is assumed that _main_ is
the primary. In this case Diff will, when started, stop the
replication from _main_ to _other_. When the comparison ends
Diff will, depending on the value of [reset\_replication](maxscale-diff.md#reset_replication)
either reset the replication from _main_ to _other_ or leave
the situation as it is.

If _other_ and _main_ replicates from a third seriver, it is
assumed _main_ is a replica. In this case, Diff will, when
started, leave the replication as it is and do nothing when
the comparison ends.

If the replication relationship between _main_ and _other_
is anything else, Diff will refuse to start.

### Settings

#### `main`

* Type: server
* Mandatory: Yes
* Dynamic: No

The main target from which results are returned to the client. Must be
a server and must be one of the servers listed in [targets](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md).

If the connection to the main target cannot be created or is lost
mid-session, the client connection will be closed.

#### `service`

* Type: service
* Mandatory: Yes
* Dynamic: No

Specifies the service Diff will modify.

#### `explain`

* Type: [enum](maxscale-diff.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `other`, \`both'
* Default: `both`

Specifies whether a request should be EXPLAINed on only _other_,
both _other_ and _main_ or neither.

#### `explain_entries`

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 2

Specifies how many times at most a particular canonical statement
is EXPLAINed during the period specified by [explain\_period](maxscale-diff.md#explain_period).

#### `explain_period`

* Type: [duration](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 15m

Specifies the length of the period during which at most [explain\_entries](maxscale-diff.md#explain_entries) number of EXPLAINs are executed
for a statement.

#### `max_request_lag`

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 10

Specifies the maximum number of requests _other_ may be lagging
behind _main_ before the execution of SELECTs against _other_
are skipped to bring it back in line with _main_.

#### `on_error`

* Type: [enum](maxscale-diff.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `close`, `ignore`
* Default: `ignore`

Specifies whether an error from _other_, will cause the session to
be closed. By default it will not.

#### `percentile`

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 100
* Default: 99

Specifies the percentile of sampels that will be considered when
calculating the width and number of bins of the histogram.

#### `qps_window`

* Type: [duration](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 15m

Specifies the size of the sliding window during which QPS is calculated
and stored. When a [summary](maxscale-diff.md#summary) is requested, the QPS information
will also be saved.

#### `report`

* Type: [enum](maxscale-diff.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_discrepancy`, `never`
* Default: `on_discrepancy`

Specifies when the results of executing a statement on _other_ and _main_
should be logged; _always_, when there is a significant difference o&#x72;_&#x6E;ever_.

#### `reset_replication`

* Type: [boolean](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

If Diff has started in read-write mode and the value of`reset_replication` is `true`, when the comparison ends
it will execute the following on _other_:

```
RESET SLAVE
START SLAVE
```

If Diff has started in read-only mode, the value of `reset_replication`
will be ignored.

Note that since Diff writes updates directly to both _main_ an&#x64;_&#x6F;ther_ there is no guarantee that it will be possible to simply
start the replication. Especially not if `gtid_strict_mode`
is on.

#### `retain_faster_statements`

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

Specifies the number of faster statements that are retained in memory.
The statements will be saved in the summary when the comparison ends,
or when Diff is explicitly instructed to do so.

#### `retain_slower_statements`

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

#### `samples`

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 100
* Default: 1000

Specifies the number of samples that will be collected in order to
define the edges and number of bins of the histograms.

### Limitations

Diff is not capable of adapting to any changes made in
the cluster configuration. For instance, if Diff starts up in
read-only mode and _main_ is subsequently made _primary_, Diff
will not sever the replication from _main_ to _other_. The result
will be that _other_ receives the same writes twice; once via the
replication from the server it is replicating from and once when
Diff executes the same writes.

Diff is not compatible with [configuration synchronization](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md).
If _configuration synchronization_ is enabled, an attempt to create a
Diff router will fail.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
