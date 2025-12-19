# MaxScale Servers

A server section defines a backend database server that MariaDB MaxScale uses. A server is identified by its section name in the configuration file.

Servers are essential components of a service. A server can be a member of one or more services but can only be monitored by one monitor.

## Configuration

A minimal server configuration requires a type and usually an address and port.

```ini
[server1]
type=server
address=127.0.0.1
port=3306
```

## Settings

### `address`

* Type: string
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: Yes
* Default: `""`

The IP-address or hostname of the machine running the database server. MaxScale uses this address to connect to the server.

Either _address_ or _socket_ must be defined, but not both. If the address is given as a hostname, MaxScale will perform name lookup on the hostname when starting and update the result every minute and when the address changes.

### `port`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `3306`

The port the backend server listens on for incoming connections. MaxScale uses this port to connect to the server.

### `socket`

* Type: string
* Mandatory: Yes, if `address` is not provided.
* Dynamic: Yes
* Default: `""`

The absolute path to a UNIX domain socket the MariaDB server is listening on.

### `private_address`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Alternative IP-address or hostname for the server. This is currently only used by MariaDB Monitor to detect and set up replication. See [MariaDB Monitor documentation](maxscale-monitors/mariadb-monitor.md) for more information.

### `monitoruser`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

This setting together with [monitorpasswd](maxscale-servers.md#monitorpw) define server-specific credentials for monitoring the server. Monitors typically use the credentials in their own configuration sections to connect to all servers. If server-specific settings are given, the monitor uses those instead.

```
monitoruser=mymonitoruser
monitorpw=mymonitorpasswd
```

### `monitorpw`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

This setting together with [monitoruser](maxscale-servers.md#monitoruser) define server-specific credentials for monitoring the server. Monitors typically use the credentials in their own configuration sections to connect to all servers. If server-specific settings are given, the monitor uses those instead.

```
monitoruser=mymonitoruser
monitorpw=mymonitorpasswd
```

`monitorpw` may be either a plain text password or an encrypted password. See the section [encrypting passwords](maxscale-servers.md#encrypting-passwords) for more information.

### `extra_port`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

An alternative port used for administrative connections to the server. If this setting is defined, MaxScale uses it for monitoring the server and to fetch user accounts. Client sessions will still use the normal port.

Defining _extra\_port_ allows MaxScale to connect even when _max\_connections_ on the backend server has been reached. Extra-port connections have their own connection limit, which is one by default. This needs to be increased to allow both monitor and user account manager to connect.

If the connection to the extra-port fails due to connection number limit or if the port is not open on the server, normal port is used.

For more information, see [extra\_port](../../server/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#extra_port) and [extra\_max\_connections](../../server/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#extra_max_connections)

### `persistpoolmax`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

Sets the size of the server connection pool. Disabled by default. When enabled, MaxScale places unused connections to the server to a pool and reuses them later. Connections typically become unused when a session closes. If the size of the pool reaches _persistpoolmax_, unused connections are closed instead.

Every routing thread has its own pool. As of version 6.3.0, MaxScale will round up _persistpoolmax_ so that every thread has an equal size pool.

When a MariaDB-protocol connection is taken from the pool to be used in a new session, the state of the connection is dependent on the router. ReadWriteSplit restores the connection to match the session state. Other routers do not.

### `persistmaxtime`

* Type: [duration](maxscale-servers.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

The `persistmaxtime` parameter defaults to zero but can be set to a duration as documented [here](maxscale-servers.md#durations). If no explicit unit is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent versions a value without a unit may be rejected. Note that since the granularity of the parameter is seconds, a value specified in milliseconds will be rejected, even if the duration is longer than a second.

A DCB placed in the persistent pool for a server will only be reused if the elapsed time since it joined the pool is less than the given value. Otherwise, the DCB will be discarded and the connection closed.

### `max_routing_connections`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0 in MaxScale, 15 in MaxScale Trial.
* Minimum: 0 in MaxScale, 1 in MaxScale Trial.
* Maximum: Unlimited in MaxScale, 15 in MaxScale Trial.

Maximum number of routing connections to this server. Connections held in a pool also count towards this maximum. Does not limit monitor connections or user account fetching. A value of 0 means no limit, which is the default for MaxScale. MaxScle Trial is limited to a maximum of 15 connections per server.

Since every client session can generate a connection to a server, the server may run out of memory when the number of clients is high enough. This setting limits server memory use caused by MaxScale. The effect depends on if the service setting [idle\_session\_pool\_time](maxscale-servers.md#idle_session_pool_time), i.e. connection sharing, is enabled or not.

If connection sharing is not on, _max\_routing\_connections_ simply sets a limit. Any sessions attempting to exceed this limit will fail to connect to the backend. The client can still connect to MaxScale, but queries will fail.

If connection sharing is on, sessions exceeding the limit will be put on hold until a connection is available. Such sessions will appear unresponsive, as queries will hang, possibly for a long time. The timeout is controlled by [multiplex\_timeout](maxscale-servers.md#multiplex_timeout).

```
max_routing_connections=1234
```

### `proxy_protocol`

* Type: [boolean](maxscale-servers.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

If `proxy_protocol` is enabled, MaxScale will send a [PROXY protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) header when connecting client sessions to the server. The header contains the original client IP address and port, as seen by MaxScale. The server will then read the header and perform authentication as if the connection originated from this address instead of MaxScale's IP address. With this feature, the user accounts on the backend server can be simplified to only contain the actual client hosts and not the MaxScale host.

**NOTE**: If you use a cloud load balancer like AWS ELB that supports the proxy protocol in front of a MaxScale, you need to configure [proxy\_protocol\_networks](maxscale-servers.md#proxy_protocol_networks) in MaxScale. This also needs to be done whenever one MaxScale may connect to another Maxscale and the connecting MaxScale has `proxy_protocol` enabled.

PROXY protocol will be supported by MariaDB 10.3, which this feature has been tested with. To use it, enable the PROXY protocol in MaxScale for every compatible server and configure the MariaDB servers themselves to accept the protocol headers from MaxScale's IP address. On the server side, the protocol should be enabled only for trusted IPs, as it allows the sender to spoof the connection origin. If a proxy header is sent to a server not expecting it, the connection will fail. Usually PROXY protocol should be enabled for every server in a cluster, as they typically have similar grants.

Other SQL-servers may support PROXY protocol as well, but the implementation may be highly restricting. Strict adherence to the protocol requires that the backend server does not allow mixing of un-proxied and proxied connections from a given IP. MaxScale requires normal connections to backends for monitoring and authentication data queries, which would be blocked. To bypass this restriction, the server monitor needs to be disabled and the service listener needs to be configured to disregard authentication errors (`skip_authentication=true`). Server states also need to be set manually in MaxCtrl. These steps are _not_ required for MariaDB 10.3, since its implementation is more flexible and allows both PROXY-headered and headerless connections from a proxy-enabled IP.

### `disk_space_threshold`

* Type: Custom
* Mandatory: No
* Dynamic: Yes
* Default: None

This parameter specifies how full a disk may be, before MaxScale should start logging warnings or take other actions (e.g. perform a switchover). This functionality will only work with MariaDB server versions 10.1.32, 10.2.14 and 10.3.6 onwards, if the `DISKS` _information schema plugin_ has been installed.

**NOTE**: Since MariaDB 10.4.7, MariaDB 10.3.17 and MariaDB 10.2.26, the information will be available _only_ if the monitor user has the `FILE` privilege.

A limit is specified as a path followed by a colon and a percentage specifying how full the corresponding disk may be, before action is taken. E.g. an entry like

```
/data:80
```

specifies that the disk that has been mounted on `/data` may be used until 80% of the total space has been consumed. Multiple entries can be specified by separating them by a comma. If the path is specified using `*`, then the limit applies to all disks. However, the value of `*` is only applied if there is not an exact match.

Note that if a particular disk has been mounted on several paths, only one path need to be specified. If several are specified, then the one with the smallest percentage will be applied.

Examples:

```
disk_space_threshold=*:80
disk_space_threshold=/data:80
disk_space_threshold=/data1:80,/data2:60,*:90
```

The last line means that the disk mounted at `/data1` may be used up to 80%, the disk mounted at `/data2` may be used up to 60% and all other disks mounted at any paths may be used up until 90% of maximum capacity, before MaxScale starts to warn to take action.

Note that the path to be used, is one of the paths returned by:

```sql
> use information_schema;
> select * from disks;
+-----------+----------------------+-----------+----------+-----------+
| Disk      | Path                 | Total     | Used     | Available |
+-----------+----------------------+-----------+----------+-----------+
| /dev/sda3 | /                    |  47929956 | 34332348 |  11139820 |
| /dev/sdb1 | /data                | 961301832 |    83764 | 912363644 |
...
```

There is no default value, but this parameter must be explicitly specified if the disk space situation should be monitored.

### `rank`

* Type: [enum](maxscale-servers.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `primary`, `secondary`
* Default: `primary`

This parameter controls the order in which servers are used. Valid values for this parameter are `primary` and `secondary`. The default value is `primary`.

This behavior depends on the router implementation but the general rule of thumb is that primary servers will be used before secondary servers. Note that this **does not affect** how monitors select servers.

Readconnroute will always use primary servers before secondary servers as long as they match the configured server type.

Readwritesplit will pick servers that have the same rank as the current primary. Read the [readwritesplit documentation on server ranks](maxscale-routers/maxscale-readwritesplit.md#server-ranks) for a detailed description of the behavior.

The following example server configuration demonstrates how `rank` can be used to exclude `DR-site` servers from routing.

```ini
[main-site-primary]
type=server
address=192.168.0.11
rank=primary

[main-site-replica]
type=server
address=192.168.0.12
rank=primary

[DR-site-primary]
type=server
address=192.168.0.21
rank=secondary

[DR-site-replica]
type=server
address=192.168.0.22
rank=secondary
```

The `main-site-primary` and `main-site-replica` servers will be used as long as they are available. When they are no longer available, the `DR-site-primary` and `DR-site-replica` will be used.

### `priority`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0

Server priority. Currently only used by galeramon to choose the order in which nodes are selected as the current primary server. Refer to the [Server Priorities](maxscale-monitors/galera-monitor.md#interaction-with-server-priorities) section of the galeramon documentation for more information on how to use it.

Starting with MaxScale 2.5.21, this parameter also accepts negative values. In older versions, the parameter only accepted non-negative values.

### `initial_status`

* Type: enum
* Mandatory: No
* Dynamic: Yes
* Values: `down`, `up`, `read`, `write`
* Default: `down`

The initial state of a server. This is the status in which the server is set into whenever it starts up or is reconfigured. This is only taken into account if the server is not being monitored by a monitor.

The main use-case of this setting is to enable static roles for servers that have no monitor. This can be useful for some special configurations where monitoring is either not an option or the behavior of the monitors is not suitable.

### `replication_custom_options`

* Type: string
* Default: None
* Dynamic: Yes

Server-specific custom string added to "CHANGE MASTER TO"-commands sent by MariaDB Monitor. Overrides `replication_custom_options` setting set in the monitor. This setting affects the server where the command is ran at, not the source of the replication. That is, if monitor sends a "CHANGE MASTER TO"- command to server A telling it to replicate from server B, the setting value from MaxScale configuration for server A would be used.

See [MariaDB Monitor documentation](maxscale-monitors/mariadb-monitor.md#replication_custom_options) for more information.

### `use_service_credentials`

* Type: [boolean](maxscale-servers.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

Whether to use the service credentials to log into MariaDB and then switch to the client account. This feature is only used when the backend database is MariaDB version 12 or newer and if the service user has the `SET USER` grant.

When enabled, the backend authentication will use the credentials defined in the service to log into the database and then execute a `SET SESSION AUTHORIZATION` query to change the user to the correct user account. This makes it possible to use any authentication plugin during the client-to-MaxScale authentication without requiring that a user mapping file is used. This also removes the need to use `proxy_protocol` in the servers as the exact client hostname can be specified directly in the `SET SESSION AUTHORIZATION` SQL.

To disable this and log in directly using the client credentials, add `use_service_credentials=false` to the server section. If disabled or if the service user does not have the `SET USER` grant, the PARSEC authentication plugin cannot be used and the Ed25519 authentication plugin must be configured to use the `caching_sha256_password` authentication by adding `authenticator_options=ed_mode=sha256` to the listeners.

### `labels`

* Type: string list
* Mandatory: No
* Dynamic: Yes
* Default: None

Comma-separated list of labels that are assigned for this server. These are user-defined labels that by default aren't interpreted by MaxScale. Some router modules may use them to customize the routing or to provide other mechanisms that otherwise depend on user-defined parameters.
