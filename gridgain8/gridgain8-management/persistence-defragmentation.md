---
description: >-
  How to reclaim disk space from GridGain persistent storage by scheduling and
  running defragmentation on cluster nodes with the control script.
---

# Persistence Defragmentation

## Overview

The persistent store enables users to store their data durably on disk, still benefiting from the in-memory nature of Apache Ignite. Data is stored in files created for every primary or backup partition assigned to that node and in an additional file for all user indexes.
Files in the filesystem are allocated lazily (only if some data is stored in a particular partition) and grow automatically when more data is added. The files cannot shrink even if all data is removed. The system only marks such files for further reuse. GridGain can only create or reuse pages for user data but never clear them from files.

Therefore the GridGain persistent data can only grow and never shrinks.
It doesn't cause any problems as once created page can be reused multiple times in most use cases. However, in certain cases, it is possible that the cache contains very little data but occupies large chunks of disk space because a significant volume of data was removed.

Defragmentation enables a user to shrink data files and claim back disk space.

{% hint style="info" %}
Defragmentation can only be used with the [historical rebalancing](../architecture/rebalancing/historical-rebalancing.md) enabled.
If the historical rebalancing is disabled, the server node always triggers full rebalance after the restart, which would throw away the defragmented partition.
A full set of data is transferred to the node from other nodes over a network. Depending on the dataset's size, transferring may require significant time and slow down the whole cluster as network capacity is essential to fulfill user requests.
{% endhint %}

## Performing Defragmentation

Defragmentation is a costly operation in terms of disk IO. To avoid slowing down user operations, do not execute it on a regular node joined to the cluster. To perform defragmentation, you need to request it first on a particular node or set of nodes and then restart them.

### Starting Defragmentation

To request defragmentation, execute the following command:

{% tabs %}
{% tab title="Unix" %}
```shell
control.sh --defragmentation schedule --nodes <consistentIds> [--caches <cacheNames>]
```
{% endtab %}
{% tab title="Windows" %}
```shell
control.bat --defragmentation schedule --nodes <consistentIds> [--caches <cacheNames>]
```
{% endtab %}
{% endtabs %}

After the manual restart, the node with the requested defragmentation enters a special mode called maintenance mode. The node in maintenance mode doesn't join the rest of the cluster but remains isolated until defragmentation is completed (or canceled by explicit user request). After that, the user has to restart the node one more time: it will exit maintenance mode and return to normal operations (joining the cluster and starting to serve regular workload).

{% hint style="info" %}
Nodes in maintenance mode don't participate in serving the regular workload. It is not recommended to execute defragmentation on several nodes simultaneously as it reduces the number of backups, thus increasing the risk of partition loss.
{% endhint %}

### Stopping Defragmentation

When a node executes defragmentation, it is possible to cancel it.
To stop defragmentation, run the following command available in the control utility:

{% tabs %}
{% tab title="Unix" %}
```shell
control.sh --host <hostName> --port <port> --defragmentation cancel
```
{% endtab %}
{% tab title="Windows" %}
```shell
control.bat --host <hostName> --port <port> --defragmentation cancel
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
To reduce disk space requirements during defragmentation, caches are defragmented one by one (if a defragmentation of more than one cache is requested). To calculate additional required space, find the cache that occupies the most disk space. The same amount of disk space is required for defragmentation at max.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
