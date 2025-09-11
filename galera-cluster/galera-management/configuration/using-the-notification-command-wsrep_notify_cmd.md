# Using the Notification Command (wsrep\_notify\_cmd)

MariaDB Galera Cluster provides a powerful automation feature through the `wsrep_notify_cmd` [system variable](../../reference/galera-cluster-system-variables.md#wsrep_notify_cmd). When this variable is configured, the MariaDB server will automatically execute a specified command or script in response to changes in the cluster's membership or the local node's state.

This is extremely useful for integrating the cluster with external systems:

| System                                                                                                                                                | Description                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [Load Balancers](../../high-availability/load-balancing/load-balancing-in-mariadb-galera-cluster.md#id-2.-recommended-load-balancer-mariadb-maxscale) | Automatically add or remove nodes from the load balancer's pool as they join or leave the cluster. |
| [Monitoring and Alerting](../../high-availability/monitoring-mariadb-galera-cluster.md)                                                               | Send custom alerts to a monitoring system when a node's status changes.                            |
| Service Discovery                                                                                                                                     | Update a service discovery tool with the current list of active cluster members.                   |

## Configuration

To use this feature, you set the `wsrep_notify_cmd` variable in your MariaDB configuration file (`my.cnf`) to the full path of the script you want to execute:

```toml
[mariadb]
...
wsrep_notify_cmd = /path/to/your/script.sh
```

The MariaDB server user must have the permissions for the specified script.

## Passed Parameters

When a cluster event occurs, the server executes the configured script and passes several arguments to it, providing context about the event. The script can then use these arguments to take appropriate action.

The script is called with the following parameters:

| Position | Parameter    | Description                                                                                                                                                                                              |
| -------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$1`     | Status       | The new status of the node (e.g., `Synced`, `Donor`).                                                                                                                                                    |
| `$2`     | View ID      | A unique identifier for the current cluster membership view.                                                                                                                                             |
| `$3`     | Members List | A comma-separated list of the names of all members in the current view.                                                                                                                                  |
| `$4`     | Is Primary   | A boolean indicating if the current component is the [Primary Component](../../high-availability/understanding-quorum-monitoring-and-recovery.md#advanced-quorum-control) (`1` for true, `0` for false). |

#### Status Values (`$1`)

The first argument indicates the [new state of the local node](../../high-availability/monitoring-mariadb-galera-cluster.md#understanding-galera-node-states). The most common values are:

* `Joining`: The node is starting to join the cluster.
* `Joined`: The node has finished a state transfer and is catching up.
* `Synced`: The node is a fully operational member of the cluster.
* `Donor`: The node is currently providing a State Snapshot Transfer (SST).
* `Desynced`: The node has been manually desynchronized (`wsrep_desync=ON`).

#### View ID (`$2`)

The View ID is a unique identifier composed of the view sequence number and the UUID of the node that initiated the view change. It changes every time a node joins or leaves the cluster.

#### Members List Format (`$3`)

The third argument is a comma-separated list of the `wsrep_node_name` of every [member in the current cluster component](../../high-availability/understanding-quorum-monitoring-and-recovery.md).

```
galera1,galera2,galera3
```

Your script can parse this list to get a complete, real-time picture of the cluster's membership.

## Example Script

Here is a simple example of a bash script that logs all cluster state changes to a file.

`notify_script.sh`:

```bash
#!/bin/bash

# Define the log file
LOG_FILE="/var/log/galera_events.log"

# Arguments passed by Galera
STATUS="$1"
VIEW_ID="$2"
MEMBERS="$3"
IS_PRIMARY="$4"

# Get the current timestamp
TIMESTAMP=$(date +"%Y-%m-%d %T")

# Log the event
echo "${TIMESTAMP}: Node status changed to ${STATUS}. View ID: ${VIEW_ID}. Members: [${MEMBERS}]. Is Primary: ${IS_PRIMARY}" >> "${LOG_FILE}"

exit 0
```

This script would provide a simple, human-readable log of all membership and node state changes, which can be invaluable for troubleshooting.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
