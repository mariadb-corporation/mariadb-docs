---
description: >-
  Reference for every setting of a MaxScale service section, in alphabetical
  order: router, targets, credentials, logging, timeouts, and session history.
---

# MaxScale Service Settings

These settings go in a service section (`type=service`) of the MaxScale configuration file and are listed in alphabetical order. For what a service is, see [Service](README.md#service-1). The settings of each router are described on the router's page.

## `auth_all_servers`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Manages whether authentication data is loaded from one server or aggregated from all servers.

This parameter controls whether only a single server or all of the servers are used when loading the users from the backend servers.

By default MaxScale uses the first server labeled as `Master` as the source of the authentication data. When this option is enabled, the authentication data is loaded from all the servers and combined into one big data set.

**Note:** This parameter was deprecated in MaxScale 24.02.0 but it was then un-deprecated as there were still uses for it. Modules that required this to function correctly (e.g. schemarouter) now automatically enable it.

## `cluster`

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Monitor that defines servers for this service.

The servers the service uses are defined by the monitor specified as value of this configuration parameter.

```
cluster=TheMonitor
```

**NOTE:** The `cluster` parameter is mutually exclusive with the `servers` and`targets` parameters.

## `connection_keepalive`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`
* Auto tune: [Yes](global-settings.md#auto_tune)
* Description: Send pings to keep idle backend connections alive.

Keep idle connections alive by sending pings to backend servers. This feature was introduced in MaxScale 2.5.0 where it was changed from a readwritesplit-specific feature to a generic service feature. The default value for this parameter is 300 seconds. To disable this feature, set the value to 0.

The keepalive interval is specified as documented [here](README.md#durations). If no explicit unit is provided, the value is interpreted as seconds in MaxScale 2.5. In subsequent versions a value without a unit may be rejected. Note that since the granularity of the keepalive is seconds, a keepalive specified in milliseconds will be rejected, even if the duration is longer than a second.

The parameter value is the interval in seconds between each keepalive ping. A keepalive ping will be sent to a backend server if the connection has been idle for longer than the configured keepalive interval.

Starting with MaxScale 2.5.21 and 6.4.0, the keepalive pings are not sent if the client has been idle for longer than the configured value of `connection_keepalive`. Older versions of MaxScale sent the keepalive pings regardless of the client state.

This parameter only takes effect in top-level services. A top-level service is the service where the listener that the client connected to points (i.e. the value of `service` in the listener). If a service defines other services in its `targets` parameter, the `connection_keepalive` for those is not used.

If the value of `connection_keepalive` is changed at runtime, the change in the value takes effect immediately.

As the connection keepalive pings must be done only when there's no ongoing query, all requests and responses must be tracked by MaxScale. In the case of `readconnroute`, this will incur a small drop in performance. For routers that rely on result tracking (e.g. `readwritesplit` and `schemarouter`), the performance will be the same with or without `connection_keepalive`.

If you want to avoid the performance cost and you don't need the connection keepalive feature, you can disable it with `connection_keepalive=0s`.

## `disable_sescmd_history`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Disable session command history entirely.

This option disables the session command history. This way no history is stored and if a replica server fails, the router will not try to replace the failed replica. Disabling session command history will allow long-lived connections without causing a constant growth in the memory consumption.

This parameter should only be used when either the memory footprint must be as small as possible or when the pruning of the session command history is not acceptable.

This parameter was moved into the MaxScale core in MaxScale 6.0. The parameter can be configured for all routers that support the session command history. The `readwritesplit`, `schemarouter`, and `smartrouter` routers support it.

## `enable_root_user`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Controls whether the root user is allowed to connect through MaxScale to backend servers.

This parameter controls the ability of the root user to connect to MariaDB MaxScale and hence onwards to the backend servers via MariaDB MaxScale.

## `filters`

* Type: filter list
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a list of filters applied to client requests before routing to backend servers.

The filters option allow a set of filters to be defined for a service; requests from the client are passed through these filters before being sent to the router for dispatch to the backend server. The filters parameter takes one or more filter names, as defined within the filter definition section of the configuration file. Multiple filters are separated using the `|` character.

```
filters=counter | QLA
```

The requests pass through the filters from left to right in the order defined in the configuration parameter.

If a value in the `filters` list is not the name of any object in MaxScale but is the name of a filter [module](README.md#module) which does not have any configuration settings, it is interpreted as an _implicit filter_. These types of filters will be automatically created whenever they're used in a service. This makes it easy to enable functionality which does not require configuration that is implemented in filters.

* The created filter will have the same name as the filter module. For example, using `filters=hintfilter` will automatically create a filter named `hintfilter` using the `hintfilter` module and add it to the service.
* Only filters that have no configuration settings can be implicitly created.
* If the implicit filter fails to be created, an error is logged and no further automatic attempts are made to load that specific filter module even if it's referred to by other services.
* Implicitly created filters otherwise behave similarly to normal filters that are defined in the configuration file. If an implicitly created filter is destroyed, it will be created again the next time a service uses it.

## `force_connection_keepalive`

* Type: [boolean](README.md#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`
* Description: Send keepalive pings to any backends even when client is idle.

By default, connection keepalive pings are only sent if the client is either executing a query or has been idle for less than the duration configured in `connection_keepalive`. When this parameter is enabled, keepalive pings are unconditionally sent to any backends that have been idle for longer than `connection_keepalive` seconds. This option was added in MaxScale 6.4.9 and can be used to emulate the pre-2.5.21 behavior if long-lived application connections rely on the old unconditional keepalive pings.

_Note:_ if `force_connection_keepalive` is enabled and `connection_keepalive` in MaxScale is set to a lower value than the `wait_timeout` on the database, the client idle timeouts that `wait_timeout` control are no longer effective. This happens because MaxScale unconditionally sends the pings which make the client behave like it is not idle and thus the connections will never be killed due to `wait_timeout`.

## `idle_session_pool_time`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `-1s`
* Description: Time idle before pooling backend connections.

Normally, MaxScale only pools backend connections when a session is closed (controlled by server settings _persistpoolmax_ and _persistmaxtime_). Other sessions can use the pooled connections instead of creating new connections to backends. If connection sharing is enabled, MaxScale can pool backend connections also from running sessions, and re-attach a pooled connection when a session is doing a query. This effectively allows multiple sessions to share backend connections.

_idle\_session\_pool\_time_ defines the amount of time a session must be idle before its backend connections may be pooled. To enable connection sharing, set _idle\_session\_pool\_time_ to zero or greater. The value can be given in seconds or milliseconds.

This feature has a significant drawback: when a backend connection is reused, it needs to be restored to the correct state. This means reauthenticating and replaying session commands. This can add a significant delay before the connection is actually ready for a query. If the session command history size exceeds the value of _max\_sescmd\_history_, connection sharing is disabled for the session.

This feature should only be used when limiting the backend connection count is a priority, even at the cost of query delay and throughput. This feature only works when the following server settings are also set in MaxScale configuration:

1. [max\_routing\_connections](../../../../reference/maxscale-servers.md#max_routing_connections)
2. [persistpoolmax](../../../../reference/maxscale-servers.md#persistpoolmax)
3. [persistmaxtime](../../../../reference/maxscale-servers.md#persistmaxtime)

Since reusing a backend connection is an expensive operation, MaxScale only pools connections when another session requires them. _idle\_session\_pool\_time_ thus effectively limits the frequency at which a connection can be moved from one session to another. Setting `idle_session_pool_time=0ms` causes MaxScale to move connections as soon as possible.

```
idle_session_pool_time=900ms
```

See below for more information on configuring connection sharing.

**Details, limitations and suggestions for connection sharing**

As noted above, when a connection is pooled and reused its state is lost. Although session variables and prepared statements are restored by replaying session commands, some state information cannot be transferred.

The most common such state is a transaction. When a transaction is on, connection sharing is disabled for that session until the transaction completes. Other similar situations may not be properly detected, and it's the responsibility of the user to avoid introducing such state to the session when using connection sharing. This means that the following should not be used:

* Statements such as `LOCK TABLES` and `GET LOCK` or any other statement that introduces state into the connection.
* Temporary tables and some problematic user or session variables such as `LAST_INSERT_ID()`. For `LAST_INSERT_ID()`, the value returned by the connector must be used instead of the variable.
* Stored procedures that cause session level side-effects.

Several settings affect connection sharing and its effectiveness. Reusing a connection is an expensive operation so its frequency should be minimized. The important configuration settings in addition to _idle\_session\_pool\_time_ are MaxScale server settings [persistpoolmax](../../../../reference/maxscale-servers.md#persistpoolmax), [persistmaxtime](../../../../reference/maxscale-servers.md#persistmaxtime) and [max\_routing\_connections](../../../../reference/maxscale-servers.md#max_routing_connections). The service settings [max\_sescmd\_history](#max_sescmd_history), [prune\_sescmd\_history](#prune_sescmd_history) and [multiplex\_timeout](#multiplex_timeout) also have an effect. These settings should be tuned according to the use case.

_persistpoolmax_ limits how many connections can be kept in a pool for a given server. If the pool is full, no more connections are detached from sessions even if they are idle and required. The pool size should be large enough to contain any connections being transferred between sessions, but not be greater than _max\_routing\_connections_. Using the value of _max\_routing\_connections_ is a reasonable starting point.

_persistmaxtime_ limits the time a connection may stay in the pool. This should be high enough so that pooled connections are not unnecessarily closed. Cleaning up clearly unneeded connections from the pool may be useful when _max\_routing\_connections_ is restrictively tuned. Because each MaxScale routing thread has its own connection pool, one thread can monopolize access to a server. For example, if the pool of thread 1 has 100 connections to _ServerA_ with `max_routing_connections=100`, other threads can no longer connect to the server. In such a situation, reducing _persistmaxtime_ of _ServerA_ may help as it would cause unneeded connections in the pool to be closed faster. Such connection slots then become available to other routing threads. Reducing the number of [routing threads](global-settings.md#threads) may also help, as it reduces pool fragmentation. This may reduce overall throughput, though. When using connection sharing, backend connections are only in the pool momentarily. Consequently, _persistmaxtime_ can be set quite low, e.g. 10s.

If a client session exceeds _max\_sescmd\_history_ (default 50), pooling is disabled for that session. If many sessions do this and _max\_routing\_connections_ is set, other sessions will stall as they cannot find a backend connection. This can be avoided with _prune\_sescmd\_history_. However, pruning means that old session commands will not be replayed when a pooled connection is reused. If the pruned commands are important (e.g. statement preparations), the session may fail later on.

If the number of clients actively running queries is greater than _max\_routing\_connections_, query throughput will suffer as clients will need to take turns. In this situation, it's imperative to minimize the number of backend connections a single session uses. The settings to achieve this depend on the router. For ReadWriteSplit the following should be used:

```
max_slave_connections=1
lazy_connect=1
transaction_replay=true
```

The above settings mean that MaxScale can process roughly (_number of replica servers_ X _max\_routing\_connections_) read queries simultaneously. Write queries will still need to take turns as there is only one primary server.

The following configuration snippet shows example server and service configurations for connection sharing with ReadWriteSplit.

```
[server1]
type=server
max_routing_connections=1000 #this should be based on MariaDB Server capacity
persistpoolmax=1000 #same as above
persistmaxtime=10
#other server settings...

[myservice]
type=service
max_slave_connections=1
transaction_replay=true
idle_session_pool_time=500ms
lazy_connect=1
#other service settings...
```

## `localhost_match_wildcard_host`

Deprecated and ignored.

## `log_auth_warnings`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Log authentication failures and warnings.

Enable or disable the logging of authentication failures and warnings. If enabled, messages about failed authentication attempts will be logged with details about who tried to connect to MariaDB MaxScale and from where.

## `log_debug`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Enable service-level debug logging.

When enabled, this allows a service to log debug messages even if the global log level configuration disables them.

Debug messages are only enabled for debug builds. Enabling `log_debug` in a release build does nothing.

## `log_info`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Enable service-level info logging.

When enabled, this allows a service to log info messages even if the global log level configuration disables them.

## `log_notice`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Enable service-level notice logging.

When enabled, this allows a service to log notice messages even if the global log level configuration disables them.

## `log_warning`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Enable service-level warning logging.

When enabled, this allows a service to log warning messages even if the global log level configuration disables them.

Note that disabling the service level logging does not override the global logging configuration: with `log_warning=false` in the service and `log_warning=true` globally, warnings will still be logged for all services.

## `max_connections`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0 in MaxScale, 15 in MaxScale Trial.
* Minimum: 0 in MaxScale, 1 in MaxScale Trial.
* Maximum: Unlimited in MaxScale, 15 in MaxScale Trial.
* Description: Maximum number of simultaneous connections allowed to this service.

The maximum number of simultaneous connections MaxScale should permit to this service. Any attempt to make more connections after the limit is reached will result in a "Too many connections" error being returned.

A value of 0 means no limit, which is the default for MaxScale. MaxScale Trial is limited to a maximum of 15 connections per service.

**Warning**: In MaxScale 2.5, it is possible that the number of concurrent connections temporarily exceeds the value of `max_connections`. This has been fixed in MaxScale 6.

Example:

```
[Test-Service]
max_connections=100
```

## `max_sescmd_history`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `50`
* Description: Maximum session commands to store for replay.

`max_sescmd_history` sets a limit on how many distinct session commands are stored in the session command history. When the history limit is exceeded, the history is either pruned to the last `max_sescmd_history` command (when `prune_sescmd_history` is enabled) or the history is disabled and server reconnections are no longer possible.

The required history size can be estimated by counting the total number of session state modifying commands (e.g `SET NAMES`) that are used by a client. Note that connectors usually add some commands that aren't visible to the application developer which means a safety margin should be added. A good rule of thumb is to count the expected number of statements and double that number. The default value of 50 is a value that'll work for most applications that do not rely heavily on user variables.

Starting with MaxScale versions 21.06.18, 22.08.15, 23.02.12, 23.08.8, 24.02.4 and 24.08.1, binary protocol prepared statements do not count towards the `max_sescmd_history` limit. In practice this means that all binary protocol prepared statements opened by the client are also kept open by MaxScale and are restored whenever a reconnection to a server happens. The limits imposed by `max_sescmd_history` apply to other text protocol commands e.g. `SET NAMES`. Note that text protocol prepared statements count as text protocol commands and are thus potentially pruned when history pruning happens. If an application uses a lot of `PREPARE stmt FROM <sql>` commands, it is recommended that the value of `max_sescmd_history` is increased accordingly.

In older versions of MaxScale, binary protocol prepared statements were limited by `max_sescmd_history` and were also pruned by `prune_sescmd_history` but this caused problems when the binary protocol prepared statement were pruned while they were still open from the client's point of view. In older versions, the recommended value of `max_sescmd_history` is the number of state modifying commands plus the maximum number of open prepared statements that any application may use.

This parameter was moved into the MaxScale core in MaxScale 6.0. The parameter can be configured for all routers that support the session command history. The `readwritesplit`, `schemarouter`, and `smartrouter` routers support it.

In addition to limiting the number of commands to store, it also acts as a hard limit on the number of packets that may be queued up on a backend before it is closed. Packets are queued while the TCP socket is being opened and when prepared statements are being prepared. In certain rare cases, a slow server may fall behind and not catch up to the rest of the cluster and a backlog of packets forms. In these cases, if more than `max_sescmd_history` packets are queued, the connection to the server is closed.

## `multiplex_timeout`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`
* Description: Maximum wait time for backend connection.

When connection sharing (as described above) is on, clients may have to wait for their turn to use a backend connection. If too much time passes without a connection becoming available, MaxScale returns an error to the client, usually also ending the session. _multiplex\_timeout_ sets this timeout. Increase it if queries are failing with "Timed out when waiting for a connection". Decrease it if failing early is preferable to stalling.

```
multiplex_timeout=33s
```

## `net_write_timeout`

* Type: [durations](README.md#durations)
* Mandatory No
* Dynamic: Yes
* Default: `0s`
* Description: Disconnects connection if data buffered longer than this duration.

This parameter controls how long a network write can stay buffered. This feature is disabled by default.

When `net_write_timeout` is configured and data is buffered on a network connection, if the time since the last successful network write exceeds the configured limit, the connection will be disconnected.

In MaxScale 24.08 and older releases, this only affected the client connections. Backend connections were never disconnected even if they had writes buffered for very long times.

## `password`

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the password the service uses to retrieve user accounts from backends.

This settings defines the _password_ the service uses to fetch user account information from backends. The _password_ may be either a plain text password or an [encrypted password](README.md#encrypting-passwords). The _user_ is specified using [user](#user).

```
user=maxscale
password=Mhu87p2D
```

See [MySQL protocol authentication documentation](../../../../maxscale-security/authentication-modules.md) for more information (such as required grants) and troubleshooting tips regarding user account management and client authentication.

From 23.08.0 onwards, MaxScale will remember the previous password when the password is changed. If the fetching of the user account information fails using the new password, it will be attempted using the previous one. The purpose of this change is to make it a smoother operation to change the password of the service user. The steps are as follows:

1. `$ maxctrl alter service MyService password=TheNewPassword`
2. `MariaDB [(none)]> set password for TheServiceUser = password('TheNewPassword');`

Since the old password is remembered and used if the new password does not work, it is no longer necessary to perform those steps simultaneously.

## `prune_sescmd_history`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Prune old session commands when limit exceeded the configured value.

This option enables pruning of the session command history when it exceeds the value configured in `max_sescmd_history`. When this option is enabled, only a set number of statements are stored in the history. This limits the per-session memory use while still allowing safe reconnections.

This parameter is intended to be used with pooled connections that remain in use for a very long time. Most connection pool implementations do not reset the session state and instead re-initialize it with new values. This causes the session command history to grow at roughly a constant rate for the lifetime of the pooled connection.

Starting with MaxScale 23.08, the session command history is also simplified before being stored. The simplification is done by removing repeated occurrences of the same command and only executing the latest one of them. The order in which the commands are executed still remains the same but inter-dependencies between commands are not preserved.

For example, the following set of commands demonstrates how the history simplification works and how inter-dependencies can be lost.

```
SET @my_planet='Earth';                            -- This command will be removed by history simplification
SET @my_home='My home is: ' || @my_planet;         -- Command #1 in the history
SET @my_planet='Earth';                            -- Command #2 in the history
```

In the example, the value of `@my_home` has a dependency on the value of `@my_planet` which is lost when the same statement is executed again and the history simplification removes the earlier one.

This same problem can occur even in older versions of MaxScale that used a sliding window of the history when the window moves past the statement that later statement depended on. If inter-dependent session commands are being used, the history pruning should be disabled.

Each client-side session that uses a pooled connection only executes a finite amount of session commands. By retaining a shorter history that encompasses all session commands the individual clients execute, the session state of a pooled connection can be accurately recreated on another server.

When the session command history pruning is enabled, there is a theoretical possibility that upon server reconnection the session states of the connections are inconsistent. This can only happen if the length of the stored history is shorter than the list of relevant statements that affect the session state. In practice the default value of 50 session commands is a fairly reasonable value and the risk of inconsistent session state is relatively low.

In case the default history length is too short for safe pruning, set the value of `max_sescmd_history` to the total number of commands that affect the session state plus a safety margin of 10. The safety margin reserves some extra space for new commands that might be executed due to changes in the client side application.

Starting with MaxScale 24.02.1, the execution of simple session commands done with binary protocol prepared statements are also stored in the history. A simple session command in the binary protocol is one that:

* Takes no parameters
* Modifies the session state
* Is executed while the original prepared statement is still in the history

The same limitations that apply to the text protocol session commands apply to the binary protocol session commands.

This parameter was moved into the MaxScale core in MaxScale 6.0. The parameter can be configured for all routers that support the session command history. The `readwritesplit`, `schemarouter`, and `smartrouter` routers support it.

## `retain_last_statements`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`
* Description: Defines the number of statements MaxScale stores per session.

How many statements MaxScale should store for each session of this service. This overrides the value of the global setting with the same name. If `retain_last_statements` has been specified in the global section of the MaxScale configuration file, then if it has _not_ been explicitly specified for the service, the global value holds, otherwise the service specific value rules. That is, it is possible to enable the setting globally and turn it off for a specific service, or just enable it for specific services.

The value of this parameter can be changed at runtime using `maxctrl` and the new value will take effect for sessions created thereafter.

```
maxctrl alter service MyService retain_last_statements 5
```

## `role`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Role to activate after connecting to a server.

[Role](../../../../../server/security/user-account-management/roles/roles_overview.md) the service should activate right after connecting to a server. If empty, no role is set. This setting may be useful if the same username is used for both monitors and services. As monitors and services require different privileges, these privileges can be granted to the monitor and the service roles separately instead of granting them all to the same user.

For services, this setting only affects user account fetching from MariaDB Servers. It does not affect router specific connections such as replication by the [Binlogrouter](../../../../reference/maxscale-routers/maxscale-binlogrouter.md) or replication management by the [Diff router](../../../../reference/maxscale-routers/maxscale-diff.md).

## `router`

* Type: router
* Mandatory: Yes
* Dynamic: No
* Description: Defines the router module that a service uses to direct client connections to backend servers.

The router parameter of a service defines the name of the router module that will be used to implement the routing algorithm between the client of MariaDB MaxScale and the backend databases. Additionally routers may also be passed a comma separated list of options that are used to control the behavior of the routing algorithm. The two parameters that control the routing choice are router and router\_options. The router options are specific to a particular router and are used to modify the behavior of the router. The read connection router can be passed options of `master`, `slave` or `synced`, an example of configuring a service to use this router and limiting the choice of servers to those in `slave` state would be as follows.

```
router=readconnroute
router_options=slave
```

To change the router to connect on to servers in the `master` state as well as slave servers, the router options can be modified to include the `master` state.

```
router=readconnroute
router_options=master,slave
```

A more complete description of router options and what is available for a given router is included with the documentation of the router itself.

## `servers`

* Type: server list
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the backend servers associated with the service.

The servers parameter in a service definition provides a comma separated list of the backend servers that comprise the service. The server names are those used in the name section of a block with a type parameter of server (see below).

```
servers=server1,server2,server3
```

**NOTE:** The `servers` parameter is mutually exclusive with the `cluster` and `targets` parameters.

## `session_track_trx_state`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Improves accuracy by enabling backend-based transaction state tracking.

_Note:_ This parameter has been deprecated in MaxScale 23.08 as the feature is now used automatically if needed. In addition, the session tracking no longer needs to be enabled in MariaDB for the transaction state tracking to work correctly.

Enable transaction state tracking by offloading it to the backend servers. Getting the transaction state from the server will be more accurate for stored procedures or multi-statement SQL that modifies the transaction state non-atomically.

In general, it is better to avoid using this type of SQL as tracking the transaction state via the server responses is not compatible with features such as `transaction_replay` in readwritesplit. `session_track_trx_state` should only be enabled if the default transaction tracking done by MaxScale does not produce the desired outcome.

 The following must be configured in the MariaDB server in order for this feature to work. Not configuring the MariaDB server with it can result in the transaction state being wrong in MaxScale which can result in data inconsistency.

```
session_track_state_change = ON
session_track_transaction_info = CHARACTERISTICS
```

## `strip_db_esc`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Remove escape characters from database names when loading users grants from a backend server.

**Note:** This parameter has been deprecated in MaxScale 23.08. The stripping of escape characters is in all known cases the correct thing to do.

This setting controls whether escape characters (`\`) are removed from database names when loading user grants from a backend server. When enabled, a grant such as ``grant select on `test\_`.* to 'user'@'%';`` is read as ``grant select on `test_`.* to 'user'@'%';``

This setting has no effect on database-level grants fetched from a MariaDB Server. The database names of a MariaDB Server are compared using the LIKE operator to properly handle wildcards and escaped wildcards. This setting may affect database names in table and column level grants, although these typically do not contain backlashes.

Some visual database management tools automatically escape some characters and this might cause conflicts when MaxScale tries to authenticate users.

## `targets`

* Type: target list
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Nested services or servers for multi-level routing.

The `targets` parameter is a comma separated list of server and/or service names that comprise the routing targets of the service. This parameter was added in MaxScale 2.5.0.

```
targets=My-Service,server2
```

This parameter allows nested service configurations to be defined without having to configure listeners for all services. For example, one use-case is to use multiple readwritesplit services behind a schemarouter service to have both the sharding of schemarouter with the high-availability of readwritesplit.

**NOTE:** The `targets` parameter is mutually exclusive with the `cluster` and `servers` parameters.

## `user`

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Username for retrieving user account information from backends.

This setting defines the _user_ the service uses to fetch user account information from backends. A _password_ is specified using [password](#password).

```
user=maxscale
password=Mhu87p2D
```

See [MySQL protocol authentication documentation](../../../../maxscale-security/authentication-modules.md) for more information (such as required grants) and troubleshooting tips regarding user account management and client authentication.

## `user_accounts_file`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Specifies the path to a JSON file containing additional user accounts for client authentication.

Defines path to a file with additional user accounts for incoming clients. Default value is empty, which disables the feature.

```
user_accounts_file=/home/root/users.json
```

In addition to querying the backends, MaxScale can read users from a file. This feature is useful when backends have limitations on the type of users that can be created, or if MaxScale needs to allow users to log in even when backends are down (e.g. binlog router). The users read from the file are only present on MaxScale, so logging into backends can still fail. The format of the file is protocol-specific. The following only applies to MariaDB-protocol, which is also the only protocol supporting this feature.

The file contains json text. Three objects are read from it: _user_, _db_ and _roles\_mapping_, none of which are mandatory. These objects must be arrays which contain user information similar to the _mysql.user_, _mysql.db_ and _mysql.roles\_mapping_ tables on the server. Each array element must define at least the string fields _user_ and _host_, which define the user account to add or modify.

The elements in the _user_-array may contain the following additional fields. If a field is not defined, it is assumed either empty (string) or false (boolean).

* password: String. Password hash, similar to the equivalent column on server.
* plugin: String. Authentication plugin used by client, similar to server.
* authentication\_string: String. Additional authentication info, similar to server.
* default\_role: String. Default role of user, similar to server.
* super\_priv: Boolean. True if user has SUPER grant.
* global\_db\_priv: Boolean. True if user can access any database on login.
* proxy\_priv: Boolean. True if user has a PROXY grant.
* is\_role: Boolean. True if user is a role.

The elements in the _db_-array must contain the following additional field:

* db: String. Database which the user can access. Can contain % and \_ wildcards.

The elements in the _roles\_mapping_-array must contain the following additional field:

* role: String. Role the user can access.

When users are read from both servers and the file, the server takes priority. That is, if user `'joe'@'%'` is defined on both, the file-version is discarded. The file can still affect the database grants and roles of `'joe'@'%'`, as the _db_ and _roles\_mapping_-arrays are read separately and added to existing grant and role lists.

An example users file is below.

```
{
    "user": [
        {
            "user": "test1",
            "host": "%",
            "global_db_priv": true
        },
        {
            "user": "test2",
            "host": "127.0.0.1",
            "password": "*032169CDF0B90AF8C00992D43D354E29A2EACB42",
            "plugin": "mysql_native_password",
            "default_role": "role2"
        },
        {
            "user": "",
            "host": "%",
            "plugin": "pam",
            "proxy_priv": true
        }
    ],
    "db": [
        {
            "user": "test2",
            "host": "127.0.0.1",
            "db": "test"
        }
    ],
    "roles_mapping": [
        {
            "user": "test2",
            "host": "127.0.0.1",
            "role": "role2"
        }
    ]
}
```

## `user_accounts_file_usage`

* Type: [enum](README.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `add_when_load_ok`, `file_only_always`
* Default: `add_when_load_ok`
* Description: Specifies when the user accounts file is read instead of or alongside server data.

Defines when _user\_accounts\_file_ is read. The value is an enum, either "add\_when\_load\_ok" (default) or "file\_only\_always".

"add\_when\_load\_ok" means that the file is only read when users are successfully read from a server. The file contents are then added to the server-based data. If reading from server fails (e.g. servers are down), the file is ignored.

"file\_only\_always" means that users are not read from the servers at all and the file contents is all that matters. The state of the servers is ignored. This mode can be useful with the binlog router, as it allows clients to log in and fetch binary logs from MaxScale even when backend servers are down.

```
user_accounts_file_usage=file_only_always
```

## `version_string`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: None
* Description: Custom version string sent in MySQL handshake.

This parameter sets a custom version string that is sent in the MySQL Handshake from MariaDB MaxScale to clients.

Example:

```
version_string=10.11.2-MariaDB-RWsplit
```

If not set, MaxScale will attempt to use a version string from the backend databases by selecting the version string of the database with the lowest version number. If the selected version is from the MariaDB 10 series, a `5.5.5-` prefix will be added to it similarly to how the MariaDB 10 series versions added it.

If MaxScale has not been able to connect to a single database and the versions are unknown, the default value of `5.5.5-10.4.32 <MaxScale version>-maxscale` is used where `<MaxScale version>` is the version of MaxScale.

## `wait_timeout`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s` (>= MaxScale 24.02.5, 25.01.2), `0s` (<= MaxScale 24.02.4, 25.01.1)
* Auto tune: [Yes](global-settings.md#auto_tune)
* Description: Specifies the idle timeout for client sessions before termination.

The wait\_timeout parameter is used to disconnect sessions to MariaDB MaxScale that have been idle for too long. The session timeout is set to 28800 seconds by default. A value of zero is interpreted as no timeout.

This parameter used to be called `connection_timeout` and this name is still accepted as an alias for `wait_timeout`. The old name has been deprecated in MaxScale 23.08.

The default value of `wait_timeout` changed from `0s` to `28800s` in MaxScale versions 24.02.5 and 25.01.2 to match the default value of MariaDB ([MXS-5530](https://jira.mariadb.org/browse/MXS-5530)).

Note that since the granularity of the timeout is seconds, a timeout specified in milliseconds will be rejected, even if the duration is longer than a second.

This parameter only takes effect in top-level services. A top-level service is the service where the listener that the client connected to points (i.e. the value of `service` in the listener). If a service defines other services in its `targets` parameter, the `wait_timeout` for those is not used.

The value of `wait_timeout` in MaxScale should be lower than the lowest `wait_timeout` value on the backend servers. This way idle clients are disconnected by MaxScale before the backend servers have to close them. Any client-side idle timeouts (e.g. maximum lifetime for connection pools) should be lower than `wait_timeout` in both MaxScale and MariaDB. This way the client application will end up closing the connection itself which most of the time results in better and more helpful error messages.

**Warning:** If a connection is idle for longer than the configured connection timeout, it will be forcefully disconnected and a warning will be logged in the MaxScale log file.

Example:

```
[Test-Service]
wait_timeout=300s
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
