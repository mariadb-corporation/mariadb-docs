# Common Monitor Parameters

This document settings supported by all monitors. These should be defined in the monitor section of the configuration file.

### Settings

#### `module`

* Type: string
* Mandatory: Yes
* Dynamic: No

The monitor module this monitor should use. Typically `mariadbmon` or`galeramon`.

#### `user`

* Type: string
* Mandatory: Yes
* Dynamic: Yes

Username used by the monitor to connect to the backend servers. If a server defines
the `monitoruser` parameter, that value will be used instead.

#### `password`

* Type: string
* Mandatory: Yes
* Dynamic: Yes

Password for the user defined with the `user` parameter. If a server defines
the `monitorpw` parameter, that value will be used instead.

**Note:** In older versions of MaxScale this parameter was called `passwd`. The
use of `passwd` was deprecated in MaxScale 2.3.0.

#### `servers`

* Type: string
* Mandatory: Yes
* Dynamic: Yes

A comma-separated list of servers the monitor should monitor.

```
servers=MyServer1,MyServer2
```

#### `monitor_interval`

* Type: [duration](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `2s`

Defines how often the monitor updates the status of the servers. Choose a lower
value if servers should be queried more often. The smallest possible value is
100 milliseconds. If querying the servers takes longer than `monitor_interval`,
the effective update rate is reduced.

```
monitor_interval=2s
```

The interval is specified as documented [here](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as milliseconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected.

#### `backend_connect_timeout`

* Type: [duration](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

This parameter controls the timeout for connecting to a monitored server.
The interval is specified as documented [here](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second. The minimum value is 1 second.

```
backend_connect_timeout=3s
```

#### `backend_write_timeout`

* Type: [duration](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

This parameter controls the timeout for writing to a monitored server.
The timeout is specified as documented [here](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second. The minimum value is 1 seconds.

```
backend_write_timeout=3s
```

#### `backend_read_timeout`

* Type: [duration](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

This parameter controls the timeout for reading from a monitored server.
The timeout is specified as documented [here](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second. The minimum value is 1 second.

```
backend_read_timeout=3s
```

#### `backend_connect_attempts`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`

This parameter defines the maximum times a backend connection is attempted every
monitoring loop. Every attempt may take up to `backend_connect_timeout` seconds
to perform. If none of the attempts are successful, the backend is considered to
be unreachable and down.

```
backend_connect_attempts=1
```

#### `disk_space_threshold`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

This parameter duplicates the `disk_space_threshold`[server parameter](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md).
If the parameter has _not_ been specified for a server, then the one specified
for the monitor is applied.

**NOTE**: Since MariaDB 10.4.7, MariaDB 10.3.17 and MariaDB 10.2.26, the
information will be available _only_ if the monitor user has the `FILE`
privilege.

That is, if the disk configuration is the same on all servers monitored by
the monitor, it is sufficient (and more convenient) to specify the disk
space threshold in the monitor section, but if the disk configuration is
different on all or some servers, then the disk space threshold can be
specified individually for each server.

For example, suppose `server1`, `server2` and `server3` are identical
in all respects. In that case we can specify `disk_space_threshold`
in the monitor.

```ini
[server1]
type=server
...

[server2]
type=server
...

[server3]
type=server
...

[monitor]
type=monitor
servers=server1,server2,server3
disk_space_threshold=/data:80
...
```

However, if the servers are heterogeneous with the disk used for the
data directory mounted on different paths, then the disk space threshold
must be specified separately for each server.

```ini
[server1]
type=server
disk_space_threshold=/data:80
...

[server2]
type=server
disk_space_threshold=/Data:80
...

[server3]
type=server
disk_space_threshold=/DBData:80
...

[monitor]
type=monitor
servers=server1,server2,server3
...
```

If _most_ of the servers have the data directory disk mounted on
the same path, then the disk space threshold can be specified on
the monitor and separately on the server with a different setup.

```
[server1]
type=server
disk_space_threshold=/DbData:80
...

[server2]
type=server
...

[server3]
type=server
...

[monitor]
type=monitor
servers=server1,server2,server3
disk_space_threshold=/data:80
...
```

Above, `server1` has the disk used for the data directory mounted
at `/DbData` while both `server2` and `server3` have it mounted on`/data` and thus the setting in the monitor covers them both.

#### `disk_space_check_interval`

* Type: [duration](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

With this parameter it can be specified the minimum amount of time
between disk space checks. The interval is specified as documented [here](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as milliseconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected.
The default value is 0, which means that by default the disk space
will not be checked.

Note that as the checking is made as part of the regular monitor interval
cycle, the disk space check interval is affected by the value of`monitor_interval`. In particular, even if the value of`disk_space_check_interval` is smaller than that of `monitor_interval`,
the checking will still take place at `monitor_interval` intervals.

#### `script`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

This command will be executed on a server state change. The parameter should
be an absolute path to a command or the command should be in the executable
path. The user running MaxScale should have execution rights to the file itself
and the directory it resides in. The script may have placeholders which
MaxScale will substitute with useful information when launching the script.

The placeholders and their substitution results are:

* `$INITIATOR` -> IP and port of the server which initiated the event
* `$EVENT` -> event description, e.g. "server\_up"
* `$LIST` -> list of IPs and ports of all servers
* `$NODELIST` -> list of IPs and ports of all running servers
* `$SLAVELIST` -> list of IPs and ports of all replica servers
* `$MASTERLIST` -> list of IPs and ports of all primary servers
* `$SYNCEDLIST` -> list of IPs and ports of all synced Galera nodes
* `$PARENT` -> IP and port of the parent of the server which initiated the event.
  For primary-replica setups, this will be the primary if the initiating server is a
  replica.
* `$CHILDREN` -> list of IPs and ports of the child nodes of the server who
  initiated the event. For primary-replica setups, this will be a list of replica
  servers if the initiating server is a primary.

The expanded variable value can be an empty string if no servers match the
variable's requirements. For example, if no primaries are available `$MASTERLIST`
will expand into an empty string. The list-type substitutions will only contain
servers monitored by the current monitor.

```
script=/home/user/myscript.sh initiator=$INITIATOR event=$EVENT live_nodes=$NODELIST
```

The above script could be executed as:

```
/home/user/myscript.sh initiator=[192.168.0.10]:3306 event=master_down live_nodes=[192.168.0.201]:3306,[192.168.0.121]:3306
```

See section [Script example](common-monitor-parameters.md#script-example) below for an example script.

Any output by the executed script will be logged into the MaxScale log. Each
outputted line will be logged as a separate log message.

The log level on which the messages are logged depends on the format of the
messages. If the first word in the output line is one of `alert:`, `error:`,`warning:`, `notice:`, `info:` or `debug:`, the message will be logged on the
corresponding level. If the message is not prefixed with one of the keywords,
the message will be logged on the notice level. Whitespace before, after or
between the keyword and the colon is ignored and the matching is
case-insensitive.

Currently, the script must not execute any of the following MaxCtrl
calls as they cause a deadlock:

* `alter monitor` to the monitor executing the script
* `stop monitor` to the monitor executing the script
* `call command` to a MariaDB-Monitor that is executing the script

#### `script_timeout`

* Type: [duration](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

The timeout for the executed script. The interval is specified as documented [here](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second.

If the script execution exceeds the configured timeout, it is stopped by sending
a SIGTERM signal to it. If the process does not stop, a SIGKILL signal will be
sent to it once the execution time is greater than twice the configured timeout.

#### `events`

* Type: enum
* Mandatory: No
* Dynamic: Yes
* Values: `master_down`, `master_up`, `slave_down`, `slave_up`, `server_down`, `server_up`, `lost_master`, `lost_slave`, `new_master`, `new_slave`
* Default: All events

A list of event names which cause the script to be executed. If this option is
not defined, all events cause the script to be executed. The list must contain a
comma separated list of event names.

```
events=master_down,slave_down
```

The following table contains all the possible event types and their
descriptions.

| Event Name   | Description                                  |
| ------------ | -------------------------------------------- |
| master\_down | A Primary server has gone down               |
| master\_up   | A Primary server has come up                 |
| slave\_down  | A Replica server has gone down               |
| slave\_up    | A Replica server has come up                 |
| server\_down | A server with no assigned role has gone down |
| server\_up   | A server with no assigned role has come up   |
| lost\_master | A server lost Primary status                 |
| lost\_slave  | A server lost Replica status                 |
| new\_master  | A new Primary was detected                   |
| new\_slave   | A new Replica was detected                   |

#### `journal_max_age`

* Type: [duration](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s`

The maximum journal file age. The interval is specified as documented [here](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the max age is seconds, a max age specified in milliseconds will be rejected,
even if the duration is longer than a second.

When the monitor starts, it reads any stored journal files. If the journal file
is older than the value of _journal\_max\_age_, it will be removed and the monitor
starts with no prior knowledge of the servers.

### Monitor Crash Safety

Starting with MaxScale 2.2.0, the monitor modules keep an on-disk journal of the
latest server states. This change makes the monitors crash-safe when options
that introduce states are used. It also allows the monitors to retain stateful
information when MaxScale is restarted.

For MySQL monitor, options that introduce states into the monitoring process are
the `detect_stale_master` and `detect_stale_slave` options, both of which are
enabled by default. Galeramon has the `disable_master_failback` parameter which
introduces a state.

The default location for the server state journal is in`/var/lib/maxscale/<monitor name>/monitor.dat` where `<monitor name>` is the
name of the monitor section in the configuration file. If MaxScale crashes or is
shut down in an uncontrolled fashion, the journal will be read when MaxScale is
started. To skip the recovery process, manually delete the journal file before
starting MaxScale.

### Script example

Below is an example monitor configuration which launches a script with all
supported substitutions. The example script reads the results and prints it to
file and sends it as email.

```
[MyMonitor]
type=monitor
module=mariadbmon
servers=C1N1,C1N2,C1N3
user=maxscale
password=password
monitor_interval=10s
script=/path/to/maxscale_monitor_alert_script.sh --initiator=$INITIATOR --parent=$PARENT --children=$CHILDREN --event=$EVENT --node_list=$NODELIST --list=$LIST --master_list=$MASTERLIST --slave_list=$SLAVELIST --synced_list=$SYNCEDLIST
```

File "maxscale\_monitor\_alert\_script.sh":

|    |                     |
| -- | ------------------- |
| 1  |                     |
| 2  |                     |
| 3  |                     |
| 4  |                     |
| 5  |                     |
| 6  |                     |
| 7  |                     |
| 8  |                     |
| 9  |                     |
| 10 |                     |
| 11 |                     |
| 12 |                     |
| 13 |                     |
| 14 |                     |
| 15 |                     |
| 16 |                     |
| 17 |                     |
| 18 |                     |
| 19 |                     |
| 20 |                     |
| 21 |                     |
| 22 |                     |
| 23 |                     |
| 24 |                     |
| 25 |                     |
| 26 |                     |
| 27 |                     |
| 28 |                     |
| 29 |                     |
| 30 |                     |
| 31 |                     |
| 32 |                     |
| 33 |                     |
| 34 |                     |
| 35 |                     |
| 36 |                     |
| 37 |                     |
| 38 |                     |
| 39 |                     |
| 40 |                     |
| 41 |                     |
| 42 |                     |
| 43 |                     |
| 44 |                     |
| 45 |                     |
| 46 |                     |
| 47 |                     |
| 48 |                     |
| 49 |                     |
| 50 |                     |
| 51 |                     |
| 52 |                     |
| 53 |                     |
| 54 |                     |
| 55 |                     |
| 56 |                     |
| 57 | #!/usr/bin/env bash |

initiator=""
parent=""
children=""
event=""
node\_list=""
list=""
master\_list=""
slave\_list=""
synced\_list=""

process\_arguments()
{
while \[ "$1" != "" ]; do
if \[\[ "$1" =\~ ^--initiator=.\* ]]; then
initiator=${1#'--initiator='}
elif \[\[ "$1" =\~ ^--parent.\* ]]; then
parent=${1#'--parent='}
elif \[\[ "$1" =\~ ^--children.\* ]]; then
children=${1#'--children='}
elif \[\[ "$1" =\~ ^--event.\* ]]; then
event=${1#'--event='}
elif \[\[ "$1" =\~ ^--node\_list.\* ]]; then
node\_list=${1#'--node\_list='}
elif \[\[ "$1" =\~ ^--list.\* ]]; then
list=${1#'--list='}
elif \[\[ "$1" =\~ ^--master\_list.\* ]]; then
master\_list=${1#'--master\_list='}
elif \[\[ "$1" =\~ ^--slave\_list.\* ]]; then
slave\_list=${1#'--slave\_list='}
elif \[\[ "$1" =\~ ^--synced\_list.\* ]]; then
synced\_list=${1#'--synced\_list='}
fi
shift
done
}

process\_arguments $@
read -r -d '' MESSAGE << EOM
A server has changed state. The following information was provided:

Initiator: $initiator
Parent: $parent
Children: $children
Event: $event
Node list: $node\_list
List: $list
Primary list: $master\_list
Replica list: $slave\_list
Synced list: $synced\_list
EOM

## print message to file

echo "$MESSAGE" > /path/to/script\_output.txt

## email the message

echo "$MESSAGE" | mail -s "MaxScale received $event event for initiator $initiator." mariadb\_admin@domain.com |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
