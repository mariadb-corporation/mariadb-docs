# Step 6: Test MariaDB MaxScale

## Overview

This page details step 6 of the 6-step procedure "[Deploy Galera Cluster Topology](./)".

This step tests MariaDB MaxScale.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Check Global Configuration

Use [maxctrl show maxscale](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#show-maxscale) command to view the global MaxScale configuration.

This action is performed on the MaxScale node:

```bash
$ maxctrl show maxscale
```

```
┌──────────────┬───────────────────────────────────────────────────────┐
│ Version      │ 25.01.2                                               │
├──────────────┼───────────────────────────────────────────────────────┤
│ Commit       │ 3761fa7a52046bc58faad8b5a139116f9e33364c              │
├──────────────┼───────────────────────────────────────────────────────┤
│ Started At   │ Thu, 05 Aug 2021 20:21:20 GMT                         │
├──────────────┼───────────────────────────────────────────────────────┤
│ Activated At │ Thu, 05 Aug 2021 20:21:20 GMT                         │
├──────────────┼───────────────────────────────────────────────────────┤
│ Uptime       │ 868                                                   │
├──────────────┼───────────────────────────────────────────────────────┤
│ Config Sync  │ null                                                  │
├──────────────┼───────────────────────────────────────────────────────┤
│ Parameters   │ {                                                     │
│              │     "admin_auth": true,                               │
│              │     "admin_enabled": true,                            │
│              │     "admin_gui": true,                                │
│              │     "admin_host": "0.0.0.0",                          │
│              │     "admin_log_auth_failures": true,                  │
│              │     "admin_pam_readonly_service": null,               │
│              │     "admin_pam_readwrite_service": null,              │
│              │     "admin_port": 8989,                               │
│              │     "admin_secure_gui": false,                        │
│              │     "admin_ssl_ca_cert": null,                        │
│              │     "admin_ssl_cert": null,                           │
│              │     "admin_ssl_key": null,                            │
│              │     "admin_ssl_version": "MAX",                       │
│              │     "auth_connect_timeout": "10000ms",                │
│              │     "auth_read_timeout": "10000ms",                   │
│              │     "auth_write_timeout": "10000ms",                  │
│              │     "cachedir": "/var/cache/maxscale",                │
│              │     "config_sync_cluster": null,                      │
│              │     "config_sync_interval": "5000ms",                 │
│              │     "config_sync_password": "*****",                  │
│              │     "config_sync_timeout": "10000ms",                 │
│              │     "config_sync_user": null,                         │
│              │     "connector_plugindir": "/usr/lib64/mysql/plugin", │
│              │     "datadir": "/var/lib/maxscale",                   │
│              │     "debug": null,                                    │
│              │     "dump_last_statements": "never",                  │
│              │     "execdir": "/usr/bin",                            │
│              │     "language": "/var/lib/maxscale",                  │
│              │     "libdir": "/usr/lib64/maxscale",                  │
│              │     "load_persisted_configs": true,                   │
│              │     "local_address": null,                            │
│              │     "log_debug": false,                               │
│              │     "log_info": false,                                │
│              │     "log_notice": true,                               │
│              │     "log_throttling": {                               │
│              │         "count": 10,                                  │
│              │         "suppress": 10000,                            │
│              │         "window": 1000                                │
│              │     },                                                │
│              │     "log_warn_super_user": false,                     │
│              │     "log_warning": true,                              │
│              │     "logdir": "/var/log/maxscale",                    │
│              │     "max_auth_errors_until_block": 10,                │
│              │     "maxlog": true,                                   │
│              │     "module_configdir": "/etc/maxscale.modules.d",    │
│              │     "ms_timestamp": false,                            │
│              │     "passive": false,                                 │
│              │     "persistdir": "/var/lib/maxscale/maxscale.cnf.d", │
│              │     "piddir": "/var/run/maxscale",                    │
│              │     "query_classifier": "qc_sqlite",                  │
│              │     "query_classifier_args": null,                    │
│              │     "query_classifier_cache_size": 289073971,         │
│              │     "query_retries": 1,                               │
│              │     "query_retry_timeout": "5000ms",                  │
│              │     "rebalance_period": "0ms",                        │
│              │     "rebalance_threshold": 20,                        │
│              │     "rebalance_window": 10,                           │
│              │     "retain_last_statements": 0,                      │
│              │     "session_trace": 0,                               │
│              │     "skip_permission_checks": false,                  │
│              │     "sql_mode": "default",                            │
│              │     "syslog": true,                                   │
│              │     "threads": 1,                                     │
│              │     "users_refresh_interval": "0ms",                  │
│              │     "users_refresh_time": "30000ms",                  │
│              │     "writeq_high_water": 16777216,                    │
│              │     "writeq_low_water": 8192                          │
│              │ }                                                     │
└──────────────┴───────────────────────────────────────────────────────┘
```

Output should align to the global MaxScale configuration in the new configuration file you created.

## Check Server Configuration

Use the [maxctrl list servers](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-servers) and [maxctrl show server](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#show-server) commands to view the configured server objects.

This action is performed on the MaxScale node:

1. Obtain the full list of servers objects:

```bash
$ maxctrl list servers
```

```
┌────────┬─────────────┬──────┬─────────────┬─────────────────────────┬──────┐
│ Server │ Address     │ Port │ Connections │ State                   │ GTID │
├────────┼─────────────┼──────┼─────────────┼─────────────────────────┼──────┤
│ node1  │ 192.0.2.101 │ 3306 │ 0           │ Slave, Synced, Running  │      │
├────────┼─────────────┼──────┼─────────────┼─────────────────────────┼──────┤
│ node2  │ 192.0.2.102 │ 3306 │ 0           │ Slave, Synced, Running  │      │
├────────┼─────────────┼──────┼─────────────┼─────────────────────────┼──────┤
│ node3  │ 192.0.2.103 │ 3306 │ 0           │ Master, Synced, Running │      │
└────────┴─────────────┴──────┴─────────────┴─────────────────────────┴──────┘
```

2. For each server object, view the configuration:

```bash
$ maxctrl show server node3
```

```
┌─────────────────────┬───────────────────────────────────────────┐
│ Server              │ node3                                     │
├─────────────────────┼───────────────────────────────────────────┤
│ Address             │ 192.0.2.103                               │
├─────────────────────┼───────────────────────────────────────────┤
│ Port                │ 3306                                      │
├─────────────────────┼───────────────────────────────────────────┤
│ State               │ Master, Synced, Running                   │
├─────────────────────┼───────────────────────────────────────────┤
│ Version             │ 11.4.5-3-MariaDB-enterprise-log           │
├─────────────────────┼───────────────────────────────────────────┤
│ Last Event          │ master_up                                 │
├─────────────────────┼───────────────────────────────────────────┤
│ Triggered At        │ Thu, 05 Aug 2021 20:22:26 GMT             │
├─────────────────────┼───────────────────────────────────────────┤
│ Services            │ connection_router_service                 │
│                     │ query_router_service                      │
├─────────────────────┼───────────────────────────────────────────┤
│ Monitors            │ cluster_monitor                           │
├─────────────────────┼───────────────────────────────────────────┤
│ Master ID           │ -1                                        │
├─────────────────────┼───────────────────────────────────────────┤
│ Node ID             │ 1                                         │
├─────────────────────┼───────────────────────────────────────────┤
│ Slave Server IDs    │                                           │
├─────────────────────┼───────────────────────────────────────────┤
│ Current Connections │ 1                                         │
├─────────────────────┼───────────────────────────────────────────┤
│ Total Connections   │ 1                                         │
├─────────────────────┼───────────────────────────────────────────┤
│ Max Connections     │ 1                                         │
├─────────────────────┼───────────────────────────────────────────┤
│ Statistics          │ {                                         │
│                     │     "active_operations": 0,               │
│                     │     "adaptive_avg_select_time": "0ns",    │
│                     │     "connection_pool_empty": 0,           │
│                     │     "connections": 1,                     │
│                     │     "max_connections": 1,                 │
│                     │     "max_pool_size": 0,                   │
│                     │     "persistent_connections": 0,          │
│                     │     "reused_connections": 0,              │
│                     │     "routed_packets": 0,                  │
│                     │     "total_connections": 1                │
│                     │ }                                         │
├─────────────────────┼───────────────────────────────────────────┤
│ Parameters          │ {                                         │
│                     │     "address": "192.0.2.103",               │
│                     │     "disk_space_threshold": null,         │
│                     │     "extra_port": 0,                      │
│                     │     "monitorpw": null,                    │
│                     │     "monitoruser": null,                  │
│                     │     "persistmaxtime": "0ms",              │
│                     │     "persistpoolmax": 0,                  │
│                     │     "port": 3306,                         │
│                     │     "priority": 0,                        │
│                     │     "proxy_protocol": false,              │
│                     │     "rank": "primary",                    │
│                     │     "socket": null,                       │
│                     │     "ssl": false,                         │
│                     │     "ssl_ca_cert": null,                  │
│                     │     "ssl_cert": null,                     │
│                     │     "ssl_cert_verify_depth": 9,           │
│                     │     "ssl_cipher": null,                   │
│                     │     "ssl_key": null,                      │
│                     │     "ssl_verify_peer_certificate": false, │
│                     │     "ssl_verify_peer_host": false,        │
│                     │     "ssl_version": "MAX"                  │
│                     │ }                                         │
└─────────────────────┴───────────────────────────────────────────┘
```

Output should align to the Server Object configuration you performed.

## Check Monitor Configuration

Use the [maxctrl list monitors](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-monitors) and [maxctrl show monitor](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#show-monitor) commands to view the configured monitors.

This action is performed on the MaxScale node:

1. Obtain the full list of monitors:

```bash
$ maxctrl list monitors
```

```
┌─────────────────┬─────────┬─────────────────────┐
│ Monitor         │ State   │ Servers             │
├─────────────────┼─────────┼─────────────────────┤
│ cluster_monitor │ Running │ node1, node2, node3 │
└─────────────────┴─────────┴─────────────────────┘
```

2. For each monitor, view the monitor configuration:

```bash
$ maxctrl show monitor cluster_monitor
```

```
┌─────────────────────┬──────────────────────────────────────────────────────┐
│ Monitor             │ cluster_monitor                                      │
├─────────────────────┼──────────────────────────────────────────────────────┤
│ Module              │ galeramon                                            │
├─────────────────────┼──────────────────────────────────────────────────────┤
│ State               │ Running                                              │
├─────────────────────┼──────────────────────────────────────────────────────┤
│ Servers             │ node1                                                │
│                     │ node2                                                │
│                     │ node3                                                │
├─────────────────────┼──────────────────────────────────────────────────────┤
│ Parameters          │ {                                                    │
│                     │     ..                                               │
│                     │ }                                                    │
├─────────────────────┼──────────────────────────────────────────────────────┤
│ Monitor Diagnostics │ {                                                    │
│                     │     ..                                               │
│                     │ }                                                    │
└─────────────────────┴──────────────────────────────────────────────────────┘
```

Output should align to the Galera Monitor (galeramon) configuration you performed.

## Check Service Configuration

Use the [maxctrl list services](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-services) and [maxctrl show service](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#show-services) commands to view the configured routing services.

This action is performed on the MaxScale node:

1. Obtain the full list of routing services:

```bash
$ maxctrl list services
```

```
┌───────────────────────────┬────────────────┬─────────────┬───────────────────┬─────────────────────┐
│ Service                   │ Router         │ Connections │ Total Connections │ Servers             │
├───────────────────────────┼────────────────┼─────────────┼───────────────────┼─────────────────────┤
│ connection_router_service │ readconnroute  │ 0           │ 0                 │ node1, node2, node3 │
├───────────────────────────┼────────────────┼─────────────┼───────────────────┼─────────────────────┤
│ query_router_service      │ readwritesplit │ 1           │ 1                 │ node1, node2, node3 │
└───────────────────────────┴────────────────┴─────────────┴───────────────────┴─────────────────────┘
```

2. For each service, view the service configuration:

```bash
$ maxctrl show service query_router_service
```

```
┌─────────────────────┬─────────────────────────────────────────────────────────────┐
│ Service             │ query_router_service                                        │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Router              │ readwritesplit                                              │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ State               │ Started                                                     │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Started At          │ Thu Aug  5 20:23:38 2021                                    │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Current Connections │ 1                                                           │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Total Connections   │ 1                                                           │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Max Connections     │ 1                                                           │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Cluster             │                                                             │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Servers             │ node1                                                       │
│                     │ node2                                                       │
│                     │ node3                                                       │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Services            │                                                             │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Filters             │                                                             │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Parameters          │ {                                                           │
│                     │     "auth_all_servers": false,                              │
│                     │     "causal_reads": "false",                                │
│                     │     "causal_reads_timeout": "10000ms",                      │
│                     │     "connection_keepalive": "300000ms",                     │
│                     │     "connection_timeout": "0ms",                            │
│                     │     "delayed_retry": false,                                 │
│                     │     "delayed_retry_timeout": "10000ms",                     │
│                     │     "disable_sescmd_history": false,                        │
│                     │     "enable_root_user": false,                              │
│                     │     "idle_session_pool_time": "-1000ms",                    │
│                     │     "lazy_connect": false,                                  │
│                     │     "localhost_match_wildcard_host": true,                  │
│                     │     "log_auth_warnings": true,                              │
│                     │     "master_accept_reads": false,                           │
│                     │     "master_failure_mode": "fail_instantly",                │
│                     │     "master_reconnection": false,                           │
│                     │     "max_connections": 0,                                   │
│                     │     "max_sescmd_history": 50,                               │
│                     │     "max_slave_connections": 255,                           │
│                     │     "max_slave_replication_lag": "0ms",                     │
│                     │     "net_write_timeout": "0ms",                             │
│                     │     "optimistic_trx": false,                                │
│                     │     "password": "*****",                                    │
│                     │     "prune_sescmd_history": true,                           │
│                     │     "rank": "primary",                                      │
│                     │     "retain_last_statements": -1,                           │
│                     │     "retry_failed_reads": true,                             │
│                     │     "reuse_prepared_statements": false,                     │
│                     │     "router": "readwritesplit",                             │
│                     │     "session_trace": false,                                 │
│                     │     "session_track_trx_state": false,                       │
│                     │     "slave_connections": 255,                               │
│                     │     "slave_selection_criteria": "LEAST_CURRENT_OPERATIONS", │
│                     │     "strict_multi_stmt": false,                             │
│                     │     "strict_sp_calls": false,                               │
│                     │     "strip_db_esc": true,                                   │
│                     │     "transaction_replay": false,                            │
│                     │     "transaction_replay_attempts": 5,                       │
│                     │     "transaction_replay_max_size": 1073741824,              │
│                     │     "transaction_replay_retry_on_deadlock": false,          │
│                     │     "type": "service",                                      │
│                     │     "use_sql_variables_in": "all",                          │
│                     │     "user": "mxs",                                          │
│                     │     "version_string": null                                  │
│                     │ }                                                           │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Router Diagnostics  │ {                                                           │
│                     │     "avg_sescmd_history_length": 0,                         │
│                     │     "max_sescmd_history_length": 0,                         │
│                     │     "queries": 1,                                           │
│                     │     "replayed_transactions": 0,                             │
│                     │     "ro_transactions": 0,                                   │
│                     │     "route_all": 0,                                         │
│                     │     "route_master": 0,                                      │
│                     │     "route_slave": 1,                                       │
│                     │     "rw_transactions": 0,                                   │
│                     │     "server_query_statistics": [                            │
│                     │         {                                                   │
│                     │             "avg_selects_per_session": 0,                   │
│                     │             "avg_sess_duration": "0ns",                     │
│                     │             "id": "node2",                                  │
│                     │             "read": 1,                                      │
│                     │             "total": 1,                                     │
│                     │             "write": 0                                      │
│                     │         }                                                   │
│                     │     ]                                                       │
│                     │ }                                                           │
└─────────────────────┴─────────────────────────────────────────────────────────────┘
```

Output should align to the Read Connection Router (readconnroute) or Read/Write Split Router (readwritesplit) configuration you performed.

## Test Application User

Applications should use a dedicated user account. The user account must be created on the primary server.

When users connect to MaxScale, MaxScale authenticates the user connection before routing it to an Enterprise Server node. Enterprise Server authenticates the connection as originating from the IP address of the MaxScale node.

The application users must have one user account with the host IP address of the application server and a second user account with the host IP address of the MaxScale node.

The requirement of a duplicate user account can be avoided by enabling the `proxy_protocol` parameter for MaxScale and the proxy\_protocol\_networks for Enterprise Server.

### Create a User to Connect from MaxScale

This action is performed on any Enterprise Cluster node:

1. Connect to the node:

```bash
$ sudo mariadb
```

2. Create the database user account for your MaxScale node:

```sql
CREATE USER 'app_user'@'192.0.2.104' IDENTIFIED BY 'app_user_passwd';
```

Replace 192.0.2.104 with the relevant IP address specification for your MaxScale node.

Passwords should meet your organization's password policies.

3. Grant the privileges required by your application to the database user account for your MaxScale node:

```sql
GRANT ALL ON test.* TO 'app_user'@'192.0.2.104';
```

The privileges shown are designed to allow the tests in the subsequent sections to work. The user account for your production application may require different privileges.

### Create a User to Connect from the Application Server

This action is performed on any Enterprise Cluster node:

1. Create the database user account for your application server:

```sql
CREATE USER 'app_user'@'192.0.2.11' IDENTIFIED BY 'app_user_passwd';
```

Replace 192.0.2.11 with the relevant IP address specification for your application server.

Passwords should meet your organization's password policies.

2. Grant the privileges required by your application to the database user account for your application server:

```sql
GRANT ALL ON test.* TO 'app_user'@'192.0.2.11';
```

The privileges shown are designed to allow the tests in the subsequent sections to work. The user account for your production application may require different privileges.

### Test Connection with Application User

To test the connection, use the MariaDB Client from your application server to connect to an Enterprise Cluster node through MaxScale.

This action is performed on the application server:

```bash
$ mariadb --host 192.0.2.104 --port 3307
      --user app_user --password
```

## Test Connection with Read Connection Router

If you configured the Read Connection Router, confirm that MaxScale routes connections to the replica servers.

1. On the MaxScale node, use the [maxctrl list listeners](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-listeners) command to view the available listeners and ports:

```bash
$ maxctrl list listeners
```

```
┌────────────────────────────┬──────┬──────┬─────────┬───────────────────────────┐
│ Name                       │ Port │ Host │ State   │ Service                   │
├────────────────────────────┼──────┼──────┼─────────┼───────────────────────────┤
│ connection_router_listener │ 3308 │ ::   │ Running │ connection_router_service │
├────────────────────────────┼──────┼──────┼─────────┼───────────────────────────┤
│ query_router_listener      │ 3307 │ ::   │ Running │ query_router_service      │
└────────────────────────────┴──────┴──────┴─────────┴───────────────────────────┘
```

2. Open multiple terminals connected to your application server, in each use MariaDB Client to connect to the listener port for the Read Connection Router (in the example 3308):

```bash
$ mariadb --host 192.0.2.104 --port 3308 \
      --user app_user --password
```

Use the application user credentials you created for the `--user` and `--password` options.

3. In each terminal, query the hostname system variable to identify to which you're connected:

```sql
SELECT @@global.hostname;

+-------------------+
| @@global.hostname |
+-------------------+
|             node2 |
+-------------------+
```

Different terminals should return different values since MaxScale routes the connections to different nodes.

Since the router was configured the slave router option, the Read Connection Router only routes connections to replica servers.

## Test Write Queries with the Read/Write Split Router

If you configured the Read/Write Split Router, confirm that readwritesplit correctly routes write queries.

This action is performed with multiple client connections to the MaxScale node.

1. On the MaxScale node, use the [maxctrl list servers](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-servers) command to identify the Enterprise Cluster node currently operating as the primary server:

```bash
$ maxctrl list servers
```

```
┌────────┬─────────────┬──────┬─────────────┬─────────────────────────┬──────┐
│ Server │ Address     │ Port │ Connections │ State                   │ GTID │
├────────┼─────────────┼──────┼─────────────┼─────────────────────────┼──────┤
│ node1  │ 192.0.2.101 │ 3306 │ 0           │ Slave, Synced, Running  │      │
├────────┼─────────────┼──────┼─────────────┼─────────────────────────┼──────┤
│ node2  │ 192.0.2.102 │ 3306 │ 0           │ Slave, Synced, Running  │      │
├────────┼─────────────┼──────┼─────────────┼─────────────────────────┼──────┤
│ node3  │ 192.0.2.103 │ 3306 │ 0           │ Master, Synced, Running │      │
└────────┴─────────────┴──────┴─────────────┴─────────────────────────┴──────┘
```

The server listed as Master is currently operating as the primary server.

2. On the MaxScale node, use the [maxctrl list listeners](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-listeners) command to identify the correct listener port:

```bash
$ maxctrl list listeners galerarouter
```

```
┌────────────────────────────┬──────┬───────┬─────────┬───────────────────────────┐
│ Name                       │ Port │ Host  │ State   │ Service                   │
├────────────────────────────┼──────┼───────┼─────────┼───────────────────────────┤
│ connection_router_listener │ 3308 │       │ Running │ connection_router_service │
│ query_router_listener      │ 3307 │       │ Running │ query_router_service      │
└────────────────────────────┴──────┴───────┴─────────┴───────────────────────────┘
```

In the example, the listener port for the Read/Write Split router is 3307.

3. Use the MariaDB Client to establish multiple connections to the listener configured for the Read/Write Split routing service, `query_router_listener`, on the MaxScale node:

```bash
$ mariadb --host=192.0.2.104 --port=3307 \
      --user=app_user --password=app_user_passwd
```

The database user account for your application server should be specified by the `--user` option.

4. Using any client connection, create a test table:

```sql
CREATE TABLE test.load_balancing_test (
   id INT PRIMARY KEY AUTO_INCREMENT,
   hostname VARCHAR(256)
);
```

5. Using each client connection, insert the values of the hostname system variable into the table using the INSERT statement to identify the node that executes the statement:

```sql
INSERT INTO test.load_balancing_test (hostname)
VALUES (@@global.hostname);
```

6. Using any client connection, query the table using the SELECT statement:

```sql
SELECT * FROM test.load_balancing_test;
```

```
+----+----------+
| id | hostname |
+----+----------+
|  1 | node3    |
|  4 | node3    |
|  7 | node3    |
+----+----------+
```

The output shows the hostname from the Enterprise Cluster node operating as the primary server. (Enterprise Cluster offsets auto-increment values by node to avoid write conflicts.)

Confirm that MaxScale is routing write queries to the Enterprise Cluster node operating as the primary server by checking that the test table only contains the hostname of the correct Enterprise Cluster node.

## Test Read Queries with the Read/Write Split Router

If you configured the Read/Write Split Router, confirm that readwritesplit properly routes read queries to multiple replica servers.

This action is performed with multiple clients connected to the MaxScale node.

1. On the MaxScale node, use [maxctrl list servers](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-servers) to identify the Enterprise Cluster nodes that are currently operating as replica servers:

```bash
$ maxctrl list servers
```

```
┌────────┬─────────────┬──────┬─────────────┬─────────────────────────┬──────┐
│ Server │ Address     │ Port │ Connections │ State                   │ GTID │
├────────┼─────────────┼──────┼─────────────┼─────────────────────────┼──────┤
│ node1  │ 192.0.2.101 │ 3306 │ 0           │ Slave, Synced, Running  │      │
├────────┼─────────────┼──────┼─────────────┼─────────────────────────┼──────┤
│ node2  │ 192.0.2.102 │ 3306 │ 0           │ Slave, Synced, Running  │      │
├────────┼─────────────┼──────┼─────────────┼─────────────────────────┼──────┤
│ node3  │ 192.0.2.103 │ 3306 │ 0           │ Master, Synced, Running │      │
└────────┴─────────────┴──────┴─────────────┴─────────────────────────┴──────┘
```

The servers listed as Slave are currently operating as replica servers.

2. On the MaxScale node, use the [maxctrl list listeners](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-listeners) command to identify the correct listener port:

```bash
$ maxctrl list listeners
```

```
┌────────────────────────────┬──────┬───────┬─────────┬───────────────────────────┐
│ Name                       │ Port │ Host  │ State   │ Service                   │
├────────────────────────────┼──────┼───────┼─────────┼───────────────────────────┤
│ connection_router_listener │ 3308 │       │ Running │ connection_router_service │
│ query_router_listener      │ 3307 │       │ Running │ query_router_service      │
└────────────────────────────┴──────┴───────┴─────────┴───────────────────────────┘
```

In the example, the listener port for the Read/Write Split router is 3307.

3. Use the MariaDB Client to establish multiple connections to `query_router_listener` which is the listener configured for the Read/Write Split routing service on the MaxScale node:

```bash
$ mariadb --host=192.0.2.104 --port=3307 \
   --user=app_user --password=app_user_passwd
```

The database user account for your application server should be specified by the --user option.

4. Using each client connection, query the hostname system variable to identify the node that executes the statement:

```sql
SELECT @@global.hostname;

+-------------------+
| @@global.hostname |
+-------------------+
|             node2 |
+-------------------+
```

The output shows the hostname value from one of the Enterprise Cluster nodes operating as replica servers.

Confirm that MaxScale is routing read queries to multiple Enterprise Cluster nodes operating as replica servers by checking that different client connections return different hostname values.

For more information on different routing criteria, `slave_selection_criteria`

## Next Step

Navigation in the procedure "Deploy Galera Cluster Topology":

This page was step 6 of 6.

This procedure is complete.

{% include "../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
