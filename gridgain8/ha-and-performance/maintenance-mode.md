---
description: >-
  How GridGain nodes enter maintenance mode, the conditions that trigger it, and
  the operations available while a node is isolated from the cluster.
---

# Maintenance Mode

This article describes the maintenance mode, the conditions when nodes may enter it, and the available operations.

## What is Maintenance Mode

Maintenance mode is a special state of the node, in which node functionality is limited. Nodes in maintenance mode do not join the cluster, and will remain isolated until it is over.

Nodes may go into maintenance mode when they are restarted in certain scenarios that threaten data corruption, or if the required actions may affect cluster operation should the node remain in the cluster. Nodes only enter maintenance mode on restart.

When the node enters maintenance mode, it is isolated from the cluster and does not receive any data updates. Depending on the task, you may need to resolve issues with the node manually, or it may complete the task automatically.

Node will exit maintenance mode after all maintenance tasks are completed. Afterwards, it will re-enter the cluster on the next restart.

{% hint style="warning" %}
While the node is in maintenance mode, it is offline in cluster topology. If you plan to change the baseline topology, make sure to complete maintenance beforehand.
{% endhint %}

## Maintenance Process

When the node receives the command to enter maintenance mode, it creates the `maintenance_tasks.mntc` file in the node's work folder. If this file is present after a restart, the node enters the maintenance mode automatically and tries to perform required maintenance.

The list of tasks is kept in human-readable format. Here are the possible tasks:

| Task | Maintenance to perform | Performed automatically on startup |
|---|---|---|
| `clearFolderAction` | Outdated caches detected. Node needs to remove outdated information. | Yes |
| `corruptedCacheDataFilesTask` | Possible data corruption. Manual data cleanup is required. | Yes |
| `defragmentationMaintenanceTask` | Node defragmentation scheduled. | Yes |
| `indexRebuildMaintenanceTask` | Data index rebuild is scheduled. | Yes |
| `partitionLogTreeRebuildMaintenanceTask` | Partition tree rebuild is scheduled. | Yes |
| `cleanupPartitionLogTree` | Removal of all messages from the DR pending queue is scheduled. | Yes |

After the tasks are resolved, the `maintenance_tasks.mntc` file is deleted. The node continues to operate in maintenance mode until it is restarted manually. You can automate the restart in the following way:

- Configure your environment to restart the GridGain process if it is terminated.
- Enable the `IGNITE_MAINTENANCE_AUTO_SHUTDOWN_AFTER_RECOVERY` system property. With this property, the node will automatically shut down after all assigned maintenance tasks are complete.
- Once the node shuts down, the environment should restart the GridGain process. As all maintenance tasks are resolved, the node will enter normal mode and proceed to re-enter the topology.

## Causes for Maintenance Mode

### Possible Data Corruption

If the node with persistence enabled and WAL disabled crashes during the checkpointing process, the node will be unable to reliably determine if any data corruption happened. In this case, on restart after the crash it will identify possible data corruption and shut down. On the subsequent restart, the node will enter maintenance mode and wait for user input.

To solve this issue:

- Restart the node. It will enter maintenance mode.
- Use the control script to perform the `--persistence clean corrupted` command. This will remove all potentially corrupted data. You can also keep backups by using `control.sh --persistence backup corrupted` command.

  {% tabs %}
  {% tab title="Unix" %}
  ```bash
  control.sh --host {host} --port {port} --persistence backup corrupted

  control.sh --host {host} --port {port} --persistence clean corrupted
  ```
  {% endtab %}

  {% tab title="Windows" %}
  ```bash
  control.bat --host {host} --port {port} --persistence backup corrupted

  control.bat --host {host} --port {port} --persistence clean corrupted
  ```
  {% endtab %}
  {% endtabs %}

  {% hint style="info" %}
  You can get node host and port from node logs.
  {% endhint %}

- After the task is complete, restart the node. It will restart the checkpointing process.

The node will remain in maintenance mode until the potentially corrupted data is deleted. You can also delete the data manually and restart the node. In this case, it will get lost data from backups on other nodes in the cluster by starting the [rebalancing](../architecture/rebalancing/data-rebalancing.md) process.

After you delete the data either manually or by using the control script, the node will exit maintenance mode and re-enter the cluster after the next restart.

### Planned Maintenance

Some tasks require the node to be isolated to properly complete without affecting the cluster. After you use the command, the node will enter maintenance mode on the next restart and perform the required tasks. You will need to restart it once more for the node to re-enter the cluster.

The following commands start maintenance mode on next restart:

- `--defragmentation`
- `--dr rebuild-partition-tree`
- `--dr cleanup-partition-tree`

For more information about these commands, see [Control Script](../reference/cli-tool/README.md) information.

You will need to restart the node after the maintenance is done to return it to the cluster.

### Stale caches

If the node left a cluster for any reason (for example, to perform planned maintenance), and a cache was deleted on the cluster while the node is not available, this cache will be considered "stale", and must be removed. To keep data consistent, the node marks these "stale" caches for deletion and enters maintenance mode.

While in maintenance mode, the node automatically deletes the outdated caches. After maintenance is complete, restart the node for it to re-enter the cluster normally.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
