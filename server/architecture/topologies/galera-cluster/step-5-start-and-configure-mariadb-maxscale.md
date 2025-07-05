# Step 5: Start and Configure MariaDB MaxScale

## Overview

This page details step 5 of the 6-step procedure "[Deploy Galera Cluster Topology](./)".

This step configures MariaDB MaxScale to route connections to MariaDB Enterprise Cluster.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Replace the Default Configuration File

MariaDB MaxScale installations include a configuration file with some example objects. This configuration file should be replaced.

On the MaxScale node, replace the default /etc/maxscale.cnf with the following configuration:

```
[maxscale]
threads          = auto
admin_host       = 0.0.0.0
admin_secure_gui = false
```

For additional information, see "Global Parameters".

## Restart MaxScale

On the MaxScale node, restart the MaxScale service to ensure that MaxScale picks up the new configuration:

```bash
$ sudo systemctl restart maxscale
```

For additional information, see "Start and Stop Services".

## Create MaxScale User Account

MariaDB MaxScale connects to Enterprise Cluster through the client port. MaxScale requires its own user account to monitor and orchestrate Enterprise Cluster nodes.

1. On any Enterprise Cluster node, use the CREATE USER statement to create a new user for MaxScale:

```sql
CREATE USER mxs@192.0.2.104 IDENTIFIED BY "passwd";
```

2. Use the GRANT statement to grant required privileges to the MaxScale user:

```sql
GRANT SHOW DATABASES ON *.* TO mxs@192.0.2.104;
GRANT SELECT ON mysql.columns_priv TO mxs@192.0.2.104;
GRANT SELECT ON mysql.db TO mxs@192.0.2.104;
GRANT SELECT ON mysql.procs_priv TO mxs@192.0.2.104;
GRANT SELECT ON mysql.proxies_priv TO mxs@192.0.2.104;
GRANT SELECT ON mysql.roles_mapping TO mxs@192.0.2.104;
GRANT SELECT ON mysql.tables_priv TO mxs@192.0.2.104;
GRANT SELECT ON mysql.user TO mxs@192.0.2.104;
```

Enterprise Cluster replicates the new user and privileges to the other Enterprise Cluster nodes.

## Configure Server Objects

MariaDB MaxScale uses server objects to define the connections it makes to MariaDB Enterprise Servers.

On the MaxScale node, use maxctrl [create server](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#create-server) to create a server object for each MariaDB Enterprise Server:

```bash
$ maxctrl create server node1 192.0.2.101

$ maxctrl create server node2 192.0.2.102

$ maxctrl create server node3 192.0.2.103
```

## Configure the Galera Monitor

MaxScale uses monitors to retrieve additional information from the servers. This information is used by other services in filtering and routing connections based on the current state of the node. For Enterprise Cluster, use the [Galera Monitor (galeramon)](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/mariadb-maxscale-2106-maxscale-21-06-monitors/maxscale-mariadb-monitor-usage/maxscale-mariadb-monitor-usage-galera-monitor/).

On the MaxScale node, use maxctrl [create monitor](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#create-monitor) to create a Galera Monitor for the cluster:

```bash
$ maxctrl create monitor cluster_monitor galeramon \
     user=mxs \
     password='MAXSCALE_USER_PASSWORD' \
     --servers node1 node2 node3
```

In this example:

* `cluster_monitor` is an arbitrary name that is used to identify the new monitor.
* `galeramon` is the name of the module that implements the Galera Monitor.
* `user=MAXSCALE_USER` sets the user parameter to the database user account that MaxScale uses to monitor the ES nodes.
* `password='MAXSCALE_USER_PASSWORD'` sets the password parameter to the password used by the database user account that MaxScale uses to monitor the ES nodes.
* `--servers sets the servers` parameter to the set of nodes that MaxScale should monitor. All non-option arguments after --servers are interpreted as server names.
* Other Module Parameters supported by galeramon in MaxScale 25.01 can also be specified.

## Choose a MaxScale Router

Routers control how MaxScale balances the load between Enterprise Cluster nodes. Each router uses a different approach to routing queries. Consider the specific use case of your application and database load and select the router that best suits your needs.

| Router                                                                                                                                                                         | Configuration Procedure          | Description                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Router                                                                                                                                                                         | Configuration Procedure          | Description                                                                                                                                                                                                                                                                                                                                          |
| [Read Connection (readconnroute)](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readconnroute)    | Configure Read Connection Router | • Connection-based load balancing • Routes connections to Enterprise ColumnStore nodes designated as replica servers for a read-only pool • Routes connections to an Enterprise ColumnStore node designated as the primary server for a read-write pool.                                                                                             |
| [Read/Write Split (readwritesplit)](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit) | Configure Read/Write Split       | • Query-based load balancing • Routes write queries to an Enterprise ColumnStore node designated as the primary server • Routes read queries to Enterprise ColumnStore node designated as replica servers • Automatically reconnects after node failures • Automatically replays transactions after node failures • Optionally enforces causal reads |

## Configure Read Connection Router

Use MaxScale Read Connection Router (readconnroute) to route connections to replica servers for a read-only pool.

On the MaxScale node, use maxctrl create service to create a router:

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
* `user=MAXSCALE_USER` sets the user parameter to the database user account that MaxScale uses to connect to the ES nodes.
* `password=MAXSCALE_USER_PASSWORD` sets the password parameter to the password used by the database user account that MaxScale uses to connect to the ES nodes.
* `router_options=slave` sets the router\_options parameter to slave, so that MaxScale only routes connections to the replica nodes.
* `--servers sets the servers` parameter to the set of nodes to which MaxScale should route connections. All non-option arguments after `--servers`are interpreted as server names.
* Other Module Parameters supported by readconnroute in MaxScale 25.01 can also be specified.

## Configure Listener for the Read Connection Router

These instructions reference TCP port 3308. You can use a different TCP port. The TCP port used must not be bound by any other listener.

On the MaxScale node, use the maxctrl create listener command to configure MaxScale to use a listener for the Read Connection Router (readconnroute):

```bash
$ maxctrl create listener connection_router_service connection_router_listener 3308 \
     protocol=MariaDBClient
```

In this example:

* `connection_router_service` is the name of the readconnroute service that was previously created.
* `connection_router_listener` is an arbitrary name that is used to identify the new listener.
* 3308 is the TCP port.
* `protocol=MariaDBClient` sets the protocol parameter.
* Other Module Parameters supported by listeners in MaxScale 25.01 can also be specified.

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
* `user=MAXSCALE_USER` sets the user parameter to the database user account that MaxScale uses to connect to the ES nodes.
* `password=MAXSCALE_USER_PASSWORD` sets the password parameter to the password used by the database user account that MaxScale uses to connect to the ES nodes.
* `--servers sets the servers` parameter to the set of nodes to which MaxScale should route queries. All non-option arguments after --servers are interpreted as server names.
* Other Module Parameters supported by readwritesplit in MaxScale 25.01 can also be specified.

## Configure a Listener for the Read/Write Split Router

These instructions reference TCP port 3307. You can use a different TCP port. The TCP port used must not be bound by any other listener.

On the MaxScale node, use the maxctrl create listener command to configure MaxScale to use a listener for the Read/Write Split Router (readwritesplit):

```bash
$ maxctrl create listener query_router_service query_router_listener 3307 \
     protocol=MariaDBClient
```

In this example:

* `query_router_service` is the name of the readwritesplit service that was previously created.
* `query_router_listener` is an arbitrary name that is used to identify the new listener.
* 3307 is the TCP port.
* `protocol=MariaDBClient` sets the protocol parameter.
* Other Module Parameters supported by listeners in MaxScale 25.01 can also be specified.

## Start Services

To start the services and monitors, on the MaxScale node use maxctrl start services:

```bash
$ maxctrl start services
```

## Next Step

Navigation in the procedure "Deploy Galera Cluster Topology":

This page was step 5 of 6.

Next: Step 6: Test MariaDB MaxScale

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
