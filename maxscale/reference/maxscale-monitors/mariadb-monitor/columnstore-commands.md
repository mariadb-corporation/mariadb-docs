---
description: >-
  MariaDB Monitor commands for managing a ColumnStore cluster: get status,
  add or remove nodes, start and stop the cluster, and set read-only mode.
---

# MaxScale MariaDB Monitor ColumnStore Commands

MariaDB Monitor can manage a ColumnStore cluster through the ColumnStore Admin API. This page describes these commands.

Since MaxScale version 22.08, MariaDB Monitor can run ColumnStore administrative
commands against a ColumnStore cluster. The commands interact with the
ColumnStore REST-API present in recent ColumnStore versions and have been tested
with MariaDB-Server 10.6 running the ColumnStore plugin version 6.2. None of the
commands affect monitor configuration or replication topology. MariaDB Monitor
simply relays the commands to the backend cluster.

MariaDB Monitor can fetch cluster status, add and remove nodes, start and stop
the cluster, and set cluster read-only or readwrite. MaxScale only communicates
with the first server in the `servers`-list.

Most of the commands are asynchronous, i.e. they do not wait for the operation
to complete on the ColumnStore backend before returning to the command prompt.
MariaDB Monitor itself, however, runs the command in the background and does not
perform normal monitoring until the operation completes or fails. After an
operation has started the user should use _fetch-cmd-result_ to check its
status. The examples below show how to run the commands using MaxCtrl. If a
command takes a timeout-parameter, the timeout can be given in seconds (s),
minutes (m) or hours (h).

ColumnStore command settings are listed [here](README.md#settings). At least`cs_admin_api_key` must be set.

## Get status

Fetch cluster status. Returns the result as is. Status fetching has an automatic
timeout of ten seconds.

```
maxctrl call command mariadbmon cs-get-status <monitor-name>
maxctrl call command mariadbmon async-cs-get-status <monitor-name>
```

Examples:

```
maxctrl call command mariadbmon cs-get-status MyMonitor
{
    "mcs1": {
        "cluster_mode": "readwrite",
        "dbrm_mode": "master",
<snip>

maxctrl call command mariadbmon async-cs-get-status MyMonitor
OK
maxctrl call command mariadbmon fetch-cmd-result MyMonitor
{
    "mcs1": {
        "cluster_mode": "readwrite",
        "dbrm_mode": "master",
<snip>
```

## Add or remove node

Add or remove a node to/from the ColumnStore cluster.

```
maxctrl call command mariadbmon async-cs-add-node <monitor-name> <node-host> <timeout>
maxctrl call command mariadbmon async-cs-remove-node <monitor-name> <node-host> <timeout>
```

`<node-host>` is the hostname or IP of the node being added or removed.

Examples:

```
maxctrl call command mariadbmon async-cs-add-node MyMonitor mcs3 1m
OK
maxctrl call command mariadbmon fetch-cmd-result MyMonitor
{
    "node_id": "mcs3",
    "timestamp": "2022-05-05 08:07:51.518268"
}
maxctrl call command mariadbmon async-cs-remove-node MyMonitor mcs3 1m
OK
maxctrl call command mariadbmon fetch-cmd-result MyMonitor
{
    "node_id": "mcs3",
    "timestamp": "2022-05-05 10:46:46.506947"
}
```

## Start and stop cluster

```
maxctrl call command mariadbmon async-cs-start-cluster <monitor-name> <timeout>
maxctrl call command mariadbmon async-cs-stop-cluster <monitor-name> <timeout>
```

Examples:

```
maxctrl call command mariadbmon async-cs-start-cluster MyMonitor 1m
OK
maxctrl call command mariadbmon fetch-cmd-result MyMonitor
{
    "timestamp": "2022-05-05 09:41:57.140732"
}
maxctrl call command mariadbmon async-cs-stop-cluster MyMonitor 1m
OK
maxctrl call command mariadbmon fetch-cmd-result MyMonitor
{
    "mcs1": {
        "timestamp": "2022-05-05 09:45:33.779837"
    },
<snip>
```

## Set read-only or readwrite

```
maxctrl call command mariadbmon async-cs-set-readonly <monitor-name> <timeout>
maxctrl call command mariadbmon async-cs-set-readwrite <monitor-name> <timeout>
```

Examples:

```
maxctrl call command mariadbmon async-cs-set-readonly MyMonitor 30s
OK
maxctrl call command mariadbmon fetch-cmd-result MyMonitor
{
    "cluster-mode": "readonly",
    "timestamp": "2022-05-05 09:49:18.365444"
}
maxctrl call command mariadbmon async-cs-set-readwrite MyMonitor 30s
OK
maxctrl call command mariadbmon fetch-cmd-result MyMonitor
{
    "cluster-mode": "readwrite",
    "timestamp": "2022-05-05 09:50:30.718972"
}
```

## Settings for ColumnStore commands

The following settings control this feature:

* [`cs_admin_port`](mariadb-monitor-settings.md#cs_admin_port)
* [`cs_admin_api_key`](mariadb-monitor-settings.md#cs_admin_api_key)
* [`cs_admin_base_path`](mariadb-monitor-settings.md#cs_admin_base_path)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
