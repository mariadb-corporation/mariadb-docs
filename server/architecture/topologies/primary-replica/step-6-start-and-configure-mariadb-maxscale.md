# Step 6: Start and Configure MariaDB MaxScale

## Overview

This page details step 6 of the 7-step procedure "[Deploy Primary/Replica Topology](./)".

This step starts and configures MariaDB MaxScale.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Replace the Default Configuration File

MariaDB MaxScale installations include a configuration file with some example objects. This configuration file should be replaced.

**On the MaxScale node**, replace the default `/etc/maxscale.cnf` with the following configuration:

```
[maxscale]
threads          = auto
admin_host       = 0.0.0.0
admin_secure_gui = false
```

For additional information, see "[Global Settings](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-archive/archive-of-2x.xx-versions/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide#global-settings)".

## Restart MaxScale

**On the MaxScale node**, restart the MaxScale service to ensure that MaxScale picks up the new configuration:

```bash
$ sudo systemctl restart maxscale
```

For additional information, see "[Starting and Stopping MariaDB](../../../server-management/starting-and-stopping-mariadb/)".

## Configure Server Objects

**On the MaxScale node**, use [maxctrl create](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#create-monitor) server to create a server object for each MariaDB Enterprise Server:

```bash
$ maxctrl create server node1 192.0.2.101

$ maxctrl create server node2 192.0.2.102

$ maxctrl create server node3 192.0.2.103
```

## Configure MariaDB Monitor

MaxScale uses monitors to retrieve additional information from the servers. This information is used by other services in filtering and routing connections based on the current state of the node. For MariaDB Replication, use the MariaDB Monitor (mariadbmon).

**On the MaxScale node**, use [maxctrl create monitor](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#create-monitor) to create a MariaDB Monitor:

```bash
$ maxctrl create monitor mdb_monitor mariadbmon \
     user=mxs \
     password='MAXSCALE_USER_PASSWORD' \
     replication_user=repl \
     replication_password='REPLICATION_USER_PASSWORD' \
     --servers node1 node2 node3
```

In this example:

* `mdb_monitor` is an arbitrary name that is used to identify the new monitor.
* mariadbmon is the name of the module that implements the MariaDB Monitor.
* `user=MAXSCALE_USER` sets the `user` parameter to the database user account that MaxScale uses to monitor the ES nodes.
* `password='MAXSCALE_USER_PASSWORD'` sets the `password` parameter to the password used by the database user account that MaxScale uses to monitor the ES nodes.
* `replication_user=REPLICATION_USER` sets the `replication_user` parameter to the database user account that MaxScale uses to setup replication.
* `replication_password='REPLICATION_USER_PASSWORD'` sets the `replication_password` parameter to the password used by the database user account that MaxScale uses to setup replication.
* `--servers` sets the `servers` parameter to the set of nodes that MaxScale should monitor. All non-option arguments after `--servers` are interpreted as server names.
* Other Module Parameters supported by `mariadbmon` in MaxScale can also be specified.

## Choose a MaxScale Router

Routers control how MaxScale balances the load between Enterprise Server nodes. Each router uses a different approach to routing queries. Consider the specific use case of your application and database load and select the router that best suits

<table><thead><tr><th width="168.4073486328125" valign="top">Router</th><th width="241.5926513671875" valign="top">Configuration Procedure</th><th>Description</th></tr></thead><tbody><tr><td valign="top"><a href="https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readconnroute">Read Connection (readconnroute)</a></td><td valign="top"><a href="step-6-start-and-configure-mariadb-maxscale.md#configure-read-connection-router">Configure Read Connection Router</a></td><td><p><strong>Connection-based load balancing</strong></p><ul><li>Routes connections to Enterprise ColumnStore nodes designated as replica servers for a read-only pool</li><li>Routes connections to an Enterprise ColumnStore node designated as the primary server for a read-write pool.</li></ul></td></tr><tr><td valign="top"><a href="https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit">Read/Write Split (readwritesplit)</a></td><td valign="top"><a href="step-6-start-and-configure-mariadb-maxscale.md#configure-read-write-split-router-for-queries">Configure Read/Write Split</a></td><td><p><strong>Query-based load balancing</strong></p><ul><li>Routes write queries to an Enterprise ColumnStore node designated as the primary server</li><li>Routes read queries to Enterprise ColumnStore node designated as replica servers</li><li>Automatically reconnects after node failures</li><li>Automatically replays transactions after node failures</li><li>Optionally enforces causal reads</li></ul></td></tr></tbody></table>

## Configure Read Connection Router

Use MaxScale Read Connection Router (readconnroute) to route connections to replica servers for a read-only pool.

On the MaxScale node, use `maxctrl create service` to create a router:

```bash
$ maxctrl create service connection_router_service readconnroute \
     user=mxs \
     password='MAXSCALE_USER_PASSWORD' \
     router_options=slave \
     --servers node1 node2 node3
```

In this example:

* `connection_router_service` is an arbitrary name that is used to identify the new service.
* `readconnroute` is the name of the module that implements the Read Connection Router.
* `user=MAXSCALE_USER` sets the `user` parameter to the database user account that MaxScale uses to connect to the ES nodes.
* `password=MAXSCALE_USER_PASSWORD` sets the password parameter to the password used by the database user account that MaxScale uses to connect to the ES nodes.
* `router_options=slave` sets the `router_options` parameter to `slave`, so that MaxScale only routes connections to the replica nodes.
* `--servers sets the servers` parameter to the set of nodes to which MaxScale should route connections. All non-option arguments after `--servers`are interpreted as server names.
* Other Module Parameters supported by `readconnroute` in MaxScale 25.01 can also be specified.

### Configure Listener for the Read Connection Router

These instructions reference TCP port 3308. You can use a different TCP port. The TCP port used must not be bound by any other listener.

On the MaxScale node, use the maxctrl create listener command to configure MaxScale to use a listener for the Read Connection Router (readconnroute):

```bash
$ maxctrl create listener connection_router_service connection_router_listener 3308 \
     protocol=MariaDBClient
```

In this example:

* `connection_router_service` is the name of the readconnroute service that was previously created.
* `connection_router_listener` is an arbitrary name that is used to identify the new listener.
* `3308` is the TCP port.
* `protocol=MariaDBClient` sets the protocol parameter.
* Other Module Parameters supported by listeners in MaxScale can also be specified.

## Configure Read/Write Split Router for Queries

MaxScale Read/Write Split Router (readwritesplit) performs query-based load balancing. The router routes write queries to the primary and read queries to the replicas.

On the MaxScale node, use the maxctrl create service command to configure MaxScale to use the Read/Write Split Router (readwritesplit):

```bash
$ maxctrl create service query_router_service readwritesplit  \
     user=mxs \
     password='MAXSCALE_USER_PASSWORD' \
     --servers node1 node2 node3
```

In this example:

* `query_router_service` is an arbitrary name that is used to identify the new service.
* `readwritesplit` is the name of the module that implements the Read/Write Split Router.
* `user=MAXSCALE_USER` sets the `user` parameter to the database user account that MaxScale uses to connect to the ES nodes.
* `password=MAXSCALE_USER_PASSWORD` sets the `password` parameter to the password used by the database user account that MaxScale uses to connect to the ES nodes.
* `--servers sets the servers` parameter to the set of nodes to which MaxScale should route queries. All non-option arguments after `--servers` are interpreted as server names.
* Other Module Parameters supported by `readwritesplit` in MaxScale can also be specified.

### Configure a Listener for the Read/Write Split Router

These instructions reference TCP port `3307`. You can use a different TCP port. The TCP port used must not be bound by any other listener.

On the MaxScale node, use the `maxctrl create listener` command to configure MaxScale to use a listener for the Read/Write Split Router (readwritesplit):

```bash
$ maxctrl create listener query_router_service query_router_listener 3307 \
     protocol=MariaDBClient
```

In this example:

* `query_router_service` is the name of the `readwritesplit` service that was previously created.
* `query_router_listener` is an arbitrary name that is used to identify the new listener.
* 3307 is the TCP port.
* `protocol=MariaDBClient` sets the `protocol` parameter.
* Other Module Parameters supported by listeners in MaxScale can also be specified.

## Start Services

To start the services and monitors, on the MaxScale node use maxctrl start services:

```bash
$ maxctrl start services
```

## Next Step

Navigation in the procedure "Deploy Primary/Replica Topology":

This page was step 6 of 7.

Next: Step 7: Test MariaDB MaxScale

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
