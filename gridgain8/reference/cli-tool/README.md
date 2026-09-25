---
description: >-
  Reference for the GridGain control.sh|bat command line tool used to monitor and
  control clusters — full command list, syntax, and connection parameters.
---

# Control Script

GridGain provides a command line script — `control.sh|bat` — that you can use to monitor and control your clusters.
The script is located under the `/bin/` folder of the installation directory.

You can define the `control.sh|bat` log directory via an environment variable:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
$ CONTROL_JVM_OPTS=-Djava.util.logging.config.file=<PATH_TO_CONFIG> ./control.sh
```
{% endtab %}

{% tab title="Windows" %}
```shell
$ CONTROL_JVM_OPTS=-Djava.util.logging.config.file=<PATH_TO_CONFIG> ./control.bat
```
{% endtab %}
{% endtabs %}

## Commands

The control script supports the following commands (in alphabetical order):

- [baseline add](#baseline-add)
- [baseline autoadjust disable](#baseline-autoadjust-disable)
- [baseline autoadjust enable](#baseline-autoadjust-enable)
- [baseline scale_down_auto_adjust](#baseline-scale_down_auto_adjust)
- [baseline scale_up_auto_adjust](#baseline-scale_up_auto_adjust)
- [baseline remove](#baseline-remove)
- [baseline set](#baseline-set)
- [baseline version](#baseline-version)
- [baseline](#baseline)
- [cache check_index_inline_sizes](#cache-check_index_inline_sizes)
- [cache clear](#cache-clear)
- [cache contention](#cache-contention)
- [cache destroy](#cache-destroy)
- [cache distribution](#cache-distribution)
- [cache idle_verify](#cache-idle_verify)
- [cache indexes_list](#cache-indexes_list)
- [cache indexes_force_rebuild](#cache-indexes_force_rebuild)
- [cache list](#cache-list)
- [cache partition_reconciliation_cancel](#cache-partition_reconciliation_cancel)
- [cache partition_reconciliation](#cache-partition_reconciliation)
- [cache reset_lost_partitions](#cache-reset_lost_partitions)
- [cache validate_indexes](#cache-validate_indexes)
- [change-id](#change-id)
- [change-tag](#change-tag)
- [checkpoint](#checkpoint)
- [checkpointing force](#checkpointing-force)
- [defragmentation cancel](#defragmentation-cancel)
- [defragmentation schedule](#defragmentation-schedule)
- [defragmentation status](#defragmentation-status)
- [diagnostic](#diagnostic)
- [dr cache](#dr-cache)
- [dr check-partition-counters](#dr-check-partition-counters)
- [dr cleanup-partition-tree](#dr-cleanup-partition-tree)
- [dr full-state-transfer cancel](#dr-full-state-transfer-cancel)
- [dr full-state-transfer list](#dr-full-state-transfer-list)
- [dr full-state-transfer start](#dr-full-state-transfer-start)
- [dr node](#dr-node)
- [dr pause](#dr-pause)
- [dr rebuild-partition-tree](#dr-rebuild-partition-tree)
- [dr repair-partition-counters](#dr-repair-partition-counters)
- [dr reset-partition-tree](#dr-reset-partition-tree)
- [dr resume](#dr-resume)
- [dr state](#dr-state)
- [dr topology](#dr-topology)
- [encryption change_cache_key](#encryption-change_cache_key)
- [encryption cache_key_ids](#encryption-cache_key_ids)
- [encryption change_master_key](#encryption-change_master_key)
- [encryption get_master_key_name](#encryption-get_master_key_name)
- [encryption reencryption_rate_limit](#encryption-reencryption_rate_limit)
- [encryption reencryption_status](#encryption-reencryption_status)
- [encryption resume_reencryption](#encryption-resume_reencryption)
- [encryption suspend_reencryption](#encryption-suspend_reencryption)
- [kill sql](#kill-sql)
- [kill client](#kill-client)
- [kill continuous](#kill-continuous)
- [kill scan](#kill-scan)
- [meta details](#meta-details)
- [meta list](#meta-list)
- [meta remove](#meta-remove)
- [meta update](#meta-update)
- [metric](#metric)
- [persistence backup](#persistence-backup)
- [persistence clean](#persistence-clean)
- [persistence](#persistence)
- [property get](#property-get)
- [property list](#property-list)
- [property set](#property-set)
- [rolling-upgrade finish](#rolling-upgrade-finish)
- [rolling-upgrade force](#rolling-upgrade-force)
- [rolling-upgrade start](#rolling-upgrade-start)
- [rolling-upgrade status](#rolling-upgrade-status)
- [set-state](#set-state)
- [shutdown-policy](#shutdown-policy)
- [snapshot cancel](#snapshot-cancel)
- [snapshot create](#snapshot-create)
- [snapshot restore](#snapshot-restore)
- [snapshot status](#snapshot-status)
- [state](#state)
- [tracing-configuration](#tracing-configuration)
- [tracing-configuration get](#tracing-configuration-get)
- [tracing-configuration get_all](#tracing-configuration-get_all)
- [tracing-configuration reset](#tracing-configuration-reset)
- [tracing-configuration reset_all](#tracing-configuration-reset_all)
- [tracing-configuration set](#tracing-configuration-set)
- [tx --info](#tx-info)
- [tx --kill](#tx-kill)
- [warm-up](#warm-up)

## Script Syntax

The control script has the following syntax:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh <connection parameters> <command> <arguments>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat <connection parameters> <command> <arguments>
```
{% endtab %}
{% endtabs %}

- `<connection parameters>` – parameters the script uses to connect to a cluster node. These parameters are required for the commands that are executed on the cluster nodes. If no connection parameters are provided, the control script tries to connect to a node running on localhost (`localhost:11211`).
- `<command>` – one of the commands listed above.
- `<arguments>` – command-specific arguments.

{% hint style="info" %}
The `control.sh|bat` script commands use a legacy protocol that requires direct connections to all nodes in the cluster, not just the one you are running the command on. When you run the command on a coordinator node, it succeeds because that node has direct visibility to all other nodes. However, if you run the command from a node that is not the coordinator, it can fail if that node cannot reach all the others on the required port.
{% endhint %}

To resolve this issue, you can try the following:

- Ensure that port 11211 is open between all nodes on your server subnet.
- In some cases, if the wrong network interface is used, or a node has more than one network interface, you may need to explicitly specify the correct hostname or IP address by using the `--host` option and pass your hostname as an argument:

```shell
./control.sh --host your_hostname
```

## Connection Parameters

|Parameter|Description|Default Value|
|---|---|---|
|--host HOST_OR_IP|The host name or IP address of the node.|`localhost`|
|--port PORT|The port to connect to. The port must be opened on the host specified in the `--host` property.|`11211`|
|--user USER|The user name.||
|--password PASSWORD|The user password.||
|--ping-interval PING_INTERVAL|The ping interval.|5000|
|--ping-timeout PING_TIMEOUT|The ping response timeout.|30000|
|--ssl-protocol PROTOCOL1, PROTOCOL2...|A list of SSL protocols to try when connecting to the cluster. [Supported protocols](https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html#SunJSSE_Protocols).|`TLS`|
|--ssl-cipher-suites CIPHER1,CIPHER2...|A list of SSL ciphers. [Supported ciphers](https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html#SupportedCipherSuites).||
|--ssl-key-algorithm ALG|The SSL key algorithm.|`SunX509`|
|--keystore-type KEYSTORE_TYPE|The keystore type.|`JKS`|
|--keystore KEYSTORE_PATH|The path to the keystore. Specify a keystore to enable SSL for the control script.||
|--keystore-password KEYSTORE_PWD|The password to the keystore.||
|--truststore-type TRUSTSTORE_TYPE|The type of the truststore.|`JKS`|
|--truststore TRUSTSTORE_PATH|The path to the truststore.||
|--truststore-password TRUSTSTORE_PWD|The trustore password.||

## Activation, Deactivation, and Topology Management

You can use the control script to activate or deactivate your cluster, and manage the [Baseline Topology](../../architecture/baseline-topology.md).

{% include "../../.gitbook/includes/gg8-note-on-deactivation.md" %}

### set-state

Use this command to set a cluster's state:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --set-state <state> [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --set-state <state> [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|Values|
|---|---|---|
|state|The state to put the cluster in.|- `ACTIVE` - sets the baseline topology of the cluster to the set of nodes available at the moment of activation. Activation is required only if you use [native persistence](../../architecture/storage/native-persistence.md).<br>- `INACTIVE` - deactivates the cluster.<br>- `ACTIVE_READ_ONLY` - sets cluster to read only mode: it will be active but cache updates will be denied.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.||

### state

To get the state of a cluster (activated or not), use the following syntax:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --state
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --state
```
{% endtab %}
{% endtabs %}

### baseline

To get a list of nodes registered in the [baseline topology](../../architecture/baseline-topology.md), run the following command:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline
```
{% endtab %}
{% endtabs %}

The output contains the current topology version, the list of consistent IDs of the nodes included in the baseline topology, and the list of nodes that joined the cluster but were not added to the baseline topology.

```shell
Command [BASELINE] started
Arguments: --baseline
--------------------------------------------------------------------------------
Cluster state: active
Current topology version: 3

Current topology version: 3 (Coordinator: ConsistentId=dd3d3959-4fd6-4dc2-8199-bee213b34ff1, Order=1)

Baseline nodes:
    ConsistentId=7d79a1b5-cbbd-4ab5-9665-e8af0454f178, State=ONLINE, Order=2
    ConsistentId=dd3d3959-4fd6-4dc2-8199-bee213b34ff1, State=ONLINE, Order=1
--------------------------------------------------------------------------------
Number of baseline nodes: 2

Other nodes:
    ConsistentId=30e16660-49f8-4225-9122-c1b684723e97, Order=3
Number of other nodes: 1
Command [BASELINE] finished with code: 0
Control utility has completed execution at: 2019-12-24T16:53:08.392865
Execution time: 333 ms
```

### baseline add

To add a node (or multiple nodes) to the [baseline topology](../../architecture/baseline-topology.md), run the following command.

{% hint style="info" %}
Addition of a node starts the [rebalancing process](../../architecture/rebalancing/data-rebalancing.md).
{% endhint %}

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline add <consistentId1,consistentId2,...> [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline add <consistentId1,consistentId2,...> [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|Id1,Id2,...|A comma-separated list of consistent IDs of the nodes to add.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### baseline remove

To remove a node from the [baseline topology](../../architecture/baseline-topology.md), use the following command.

{% hint style="info" %}
Only offline nodes can be removed from the baseline topology. Shut down the node first and then use the `remove` command.
This operation starts the [rebalancing process](../../architecture/rebalancing/data-rebalancing.md), which will re-distribute the data across the nodes that remain in the baseline topology.
{% endhint %}

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline remove <consistentId1,consistentId2,...> [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline remove <consistentId1,consistentId2,...> [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|Id1,Id2,...|A comma-separated list of consistent IDs of the nodes to remove.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### baseline set

You can set [baseline topology](../../architecture/baseline-topology.md) by providing a list of nodes (consistent IDs).

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline set <consistentId1,consistentId2,...> [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline set <consistentId1,consistentId2,...> [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|Id1,Id2,...|A comma-separated list of consistent IDs of the nodes for setting baseline topology.|
|--yes|Optional; if used, it fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### baseline version

To restore a specific version of the [baseline topology](../../architecture/baseline-topology.md), use the following command:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline version <topologyVersion> [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline version <topologyVersion> [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|topologyVersion|The version of the baseline topology to restore.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### baseline autoadjust enable

{% hint style="warning" %}
The `auto_adjust` command is deprecated and will be removed in a future release. Use [baseline scale_up_auto_adjust](#baseline-scale_up_auto_adjust) and [baseline scale_down_auto_adjust](#baseline-scale_down_auto_adjust) to control autoadjust instead.
{% endhint %}

[Baseline topology autoadjustment](../../architecture/baseline-topology.md#baseline-topology-autoadjustment) is an automatic update of baseline topology after the topology has been stable for a specific amount of time.

For in-memory clusters, autoadjustment is enabled by default with the timeout set to 0. It means that baseline topology changes immediately after server nodes join or leave the cluster.

For clusters with persistence, the automatic baseline adjustment is disabled by default.

To enable autoadjust, use the following command:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline auto_adjust enable timeout <value>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline auto_adjust enable timeout <value>
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|Default Value|
|---|---|---|
|timeout|The autoadjust timeout, in milliseconds. The baseline is set to the current topology when a given number of milliseconds has passed after the last JOIN/LEFT/FAIL event. Every new JOIN/LEFT/FAIL event restarts the timeout countdown.|`0`|

### baseline autoadjust disable

{% hint style="warning" %}
The `auto_adjust` command is deprecated and will be removed in a future release. Disabling it turns off both scale-up and scale-down autoadjustment. Use [baseline scale_up_auto_adjust](#baseline-scale_up_auto_adjust) and [baseline scale_down_auto_adjust](#baseline-scale_down_auto_adjust) to control autoadjust instead.
{% endhint %}

[Baseline topology autoadjustment](../../architecture/baseline-topology.md#baseline-topology-autoadjustment) is an automatic update of baseline topology after the topology has been stable for a specific amount of time.

For clusters with persistence, the automatic baseline adjustment is disabled by default.

For in-memory clusters, autoadjustment is enabled by default with the timeout set to 0. It means that baseline topology changes immediately after server nodes join or leave the cluster.

To disable baseline autoadjustment, use the following command:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline auto_adjust disable
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline auto_adjust disable
```
{% endtab %}
{% endtabs %}

### baseline scale_up_auto_adjust

You can configure [baseline autoadjustment](../../architecture/baseline-topology.md#baseline-topology-autoadjustment) separately for scale-up events — when server nodes join the cluster and are added to the baseline topology. This lets you use a different timeout for adding nodes than for removing them.

For in-memory clusters, scale-up autoadjustment is enabled by default with the timeout set to 0. For clusters with persistence, it is disabled by default; when enabled, the default timeout is 5 minutes.

To enable scale-up autoadjustment, use the following command:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline scale_up_auto_adjust enable timeout <value>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline scale_up_auto_adjust enable timeout <value>
```
{% endtab %}
{% endtabs %}

To disable scale-up autoadjustment, use the following command:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline scale_up_auto_adjust disable
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline scale_up_auto_adjust disable
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|Default Value|
|---|---|---|
|timeout|The scale-up autoadjust timeout, in milliseconds. The baseline is set to the current topology when the given number of milliseconds has passed since the last node-join event. Every new join event restarts the timeout countdown.|`0`|

### baseline scale_down_auto_adjust

You can configure [baseline autoadjustment](../../architecture/baseline-topology.md#baseline-topology-autoadjustment) separately for scale-down events — when server nodes leave the cluster and are removed from the baseline topology.

For in-memory clusters, scale-down autoadjustment is enabled by default with the timeout set to 0. For clusters with persistence, it is disabled by default. Note that on persistent clusters the default scale-down timeout is effectively infinite: even after you enable scale-down autoadjustment, departed nodes are not removed from the baseline automatically until you set a finite timeout. This prevents unintended data loss from removing persistent nodes.

To enable scale-down autoadjustment, use the following command:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline scale_down_auto_adjust enable timeout <value>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline scale_down_auto_adjust enable timeout <value>
```
{% endtab %}
{% endtabs %}

To disable scale-down autoadjustment, use the following command:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --baseline scale_down_auto_adjust disable
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --baseline scale_down_auto_adjust disable
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|Default Value|
|---|---|---|
|timeout|The scale-down autoadjust timeout, in milliseconds. The baseline is set to the current topology when the given number of milliseconds has passed since the last node-leave or node-fail event. Every new leave/fail event restarts the timeout countdown.|`0`|

## Transaction Management

The control script allows you to get information about the transactions that are executed in the cluster, as well as to cancel specific transactions.

### tx --info

The following command returns a list of transactions that meet the filter conditions (or all transactions if no filter is defined):

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --tx --info <transaction filter>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --tx --info <transaction filter>
```
{% endtab %}
{% endtabs %}

The transaction filter parameters are as follows.

|Parameter|Description|
|---|---|
|--xid XID|The transaction ID.|
|--min-duration SECONDS|The minimum number of seconds a transaction has been executing.|
|--min-size SIZE|The minimum transaction size.|
|--label LABEL|The user label for transactions (you can use a regular expression).|
|--servers\|--clients|Limits the scope of the operation to either the server or client nodes.|
|--nodes nodeId1,nodeId2...|The list of consistent IDs of the nodes to get transactions from.|
|--limit NUMBER|Limits the number of transactions to the given value.|
|--order DURATION\|SIZE\|START_TIME|The parameter to sort the output by.|

### tx --kill

To cancel transactions, use the following command:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --tx <transaction filter> --kill
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --tx <transaction filter> --kill
```
{% endtab %}
{% endtabs %}

The transaction filter parameters are as follows.

|Parameter|Description|
|---|---|
|--xid XID|The transaction ID.|
|--min-duration SECONDS|The minimum number of seconds a transaction has been executing.|
|--min-size SIZE|The minimum transaction size.|
|--label LABEL|The user label for transactions (you can use a regular expression).|
|--servers\|--clients|Limits the scope of the operation to either the server or client nodes.|
|--nodes nodeId1,nodeId2...|The list of consistent IDs of the nodes to get transactions from.|
|--limit NUMBER|Limits the number of transactions to the given value.|
|--order DURATION\|SIZE\|START_TIME|The parameter to sort the output by.|

The command affects the following transactions:

- ACTIVE
- PREPARING
- PREPARED

For example, to cancel the transactions that have been running for more than 100 seconds, execute the following command:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --tx --min-duration 100 --kill
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --tx --min-duration 100 --kill
```
{% endtab %}
{% endtabs %}

### cache contention

Use this command to detects situations where multiple transactions are in contention to create a lock for the same key. The command is useful if you have long-running or hanging transactions.

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache contention <arguments>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache contention <arguments>
```
{% endtab %}
{% endtabs %}

The command arguments are as follows:

|Argument|Description|
|---|---|
|min queue size|The minimum number of transactions to wait for a specific key for the contention to be detected.|
|node id|Optional; the Id of the node to query for contentions|
|max lines|Optional; the number of lines to be printed in the output.|

Example:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
# Reports all keys that are a point of contention for at least 5 transactions on all cluster nodes.
control.sh --cache contention 5

# Reports all keys that are a point of contention for at least 5 transactions on a specific server node.
control.sh --cache contention 5 f2ea-5f56-11e8-9c2d-fa7a
```
{% endtab %}

{% tab title="Windows" %}
```shell
# Reports all keys that are a point of contention for at least 5 transactions on all cluster nodes.
control.bat --cache contention 5

# Reports all keys that are a point of contention for at least 5 transactions on a specific server node.
control.bat --cache contention 5 f2ea-5f56-11e8-9c2d-fa7a
```
{% endtab %}
{% endtabs %}

If contended keys are detected, the command dumps extensive information including the keys, transactions, and nodes where the contention took place.

Example:

```
[node=TcpDiscoveryNode [id=d9620450-eefa-4ab6-a821-644098f00001, addrs=[127.0.0.1], sockAddrs=[/127.0.0.1:47501], discPort=47501, order=2, intOrder=2, lastExchangeTime=1527169443913, loc=false, ver=2.5.0#20180518-sha1:02c9b2de, isClient=false]]

// No contention on node d9620450-eefa-4ab6-a821-644098f00001.

[node=TcpDiscoveryNode [id=03379796-df31-4dbd-80e5-09cef5000000, addrs=[127.0.0.1], sockAddrs=[/127.0.0.1:47500], discPort=47500, order=1, intOrder=1, lastExchangeTime=1527169443913, loc=false, ver=2.5.0#20180518-sha1:02c9b2de, isClient=false]]
    TxEntry [cacheId=1544803905, key=KeyCacheObjectImpl [part=0, val=0, hasValBytes=false], queue=10, op=CREATE, val=UserCacheObjectImpl [val=0, hasValBytes=false], tx=GridNearTxLocal[xid=e9754629361-00000000-0843-9f61-0000-000000000001, xidVersion=GridCacheVersion [topVer=138649441, order=1527169439646, nodeOrder=1], concurrency=PESSIMISTIC, isolation=REPEATABLE_READ, state=ACTIVE, invalidate=false, rollbackOnly=false, nodeId=03379796-df31-4dbd-80e5-09cef5000000, timeout=0, duration=1247], other=[]]
    TxEntry [cacheId=1544803905, key=KeyCacheObjectImpl [part=0, val=0, hasValBytes=false], queue=10, op=READ, val=null, tx=GridNearTxLocal[xid=8a754629361-00000000-0843-9f61-0000-000000000001, xidVersion=GridCacheVersion [topVer=138649441, order=1527169439656, nodeOrder=1], concurrency=PESSIMISTIC, isolation=REPEATABLE_READ, state=ACTIVE, invalidate=false, rollbackOnly=false, nodeId=03379796-df31-4dbd-80e5-09cef5000000, timeout=0, duration=1175], other=[]]
    TxEntry [cacheId=1544803905, key=KeyCacheObjectImpl [part=0, val=0, hasValBytes=false], queue=10, op=READ, val=null, tx=GridNearTxLocal[xid=6a754629361-00000000-0843-9f61-0000-000000000001, xidVersion=GridCacheVersion [topVer=138649441, order=1527169439654, nodeOrder=1], concurrency=PESSIMISTIC, isolation=REPEATABLE_READ, state=ACTIVE, invalidate=false, rollbackOnly=false, nodeId=03379796-df31-4dbd-80e5-09cef5000000, timeout=0, duration=1175], other=[]]
    TxEntry [cacheId=1544803905, key=KeyCacheObjectImpl [part=0, val=0, hasValBytes=false], queue=10, op=READ, val=null, tx=GridNearTxLocal[xid=7a754629361-00000000-0843-9f61-0000-000000000001, xidVersion=GridCacheVersion [topVer=138649441, order=1527169439655, nodeOrder=1], concurrency=PESSIMISTIC, isolation=REPEATABLE_READ, state=ACTIVE, invalidate=false, rollbackOnly=false, nodeId=03379796-df31-4dbd-80e5-09cef5000000, timeout=0, duration=1175], other=[]]
    TxEntry [cacheId=1544803905, key=KeyCacheObjectImpl [part=0, val=0, hasValBytes=false], queue=10, op=READ, val=null, tx=GridNearTxLocal[xid=4a754629361-00000000-0843-9f61-0000-000000000001, xidVersion=GridCacheVersion [topVer=138649441, order=1527169439652, nodeOrder=1], concurrency=PESSIMISTIC, isolation=REPEATABLE_READ, state=ACTIVE, invalidate=false, rollbackOnly=false, nodeId=03379796-df31-4dbd-80e5-09cef5000000, timeout=0, duration=1175], other=[]]

// Node 03379796-df31-4dbd-80e5-09cef5000000 is place for contention on key KeyCacheObjectImpl [part=0, val=0, hasValBytes=false].
```

## Cache Management

### cache list

This command is used for cache monitoring. It retrieves a list of deployed caches, their affinity/distribution parameters, and their distribution within cache groups. There is also a command option for viewing existing atomic sequences.

Use the following command syntax:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache list <arguments>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache list <arguments>
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|.|With this argument, the command lists all caches.|
|account-.*|With this argument, the command lists caches whose names start with "account-".|
|. --groups|With this argument, the command displays info about cache group distribution for all caches.|
|account-.* --groups|With this argument, the command displays info about cache group distribution for the caches whose names start with "account-".|
|. --seq|With this argument, the command displays info about all atomic sequences.|
|account-.* --groups|With this argument, the command displays info about the atomic sequences whose names start with "counter-".|

### cache reset_lost_partitions

This command resets lost partitions in the specified caches.
Refer to [Partition Loss Policy](../../architecture/rebalancing/partition-loss-policy.md) for details.

Use the following command syntax:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache reset_lost_partitions <cacheName1,cacheName2,...> | --all
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache reset_lost_partitions <cacheName1,cacheName2,...> | --all
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|cacheName1,cacheName2,...|A comma-separated list of the caches to be affected by the command.|
|--all|Makes the command check all caches for lost partition, print a list of caches with lost partitions (if any are found), and reset lost partitions in all the caches it has found.|

### cache idle_verify

This command verifies counters and hash sums of primary and backup partitions for the specified caches or scache groups on an idle cluster and prints out the differences, if any.

Use the following command syntax:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache idle_verify [--dump] [--skip-zeros] [--check-crc] [--exclude-caches <cacheName1,...,cacheNameN>] [--cache-filter ALL|USER|SYSTEM|PERSISTENT|NOT_PERSISTENT] [cacheName1,...,cacheNameN]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache idle_verify [--dump] [--skip-zeros] [--check-crc] [--exclude-caches <cacheName1,...,cacheNameN>] [--cache-filter ALL|USER|SYSTEM|PERSISTENT|NOT_PERSISTENT] [cacheName1,...,cacheNameN]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--dump|Writes the command response to a local file on each node (in addition to returning response in the terminal window).|
|--skip-zeros|Skips zero-sized partitions.|
|--check-crc|Checks the CRC-sum of pages stored on disk before verifying partition data consistency between primary and backup nodes.|
|--exclude-caches|Excludes caches provided as a comma-separated list.|
|--cache-filter|Limits the caches affected by the command to only USER caches, only user PERSISTENT caches, only user NOT_PERSISTENT caches, only SYSTEM caches, or ALL of the above.|
|cacheName1,...,cacheNameN|A comma-separated list of the caches to be affected by the command.|

### cache partition_reconciliation

Partition reconciliation is a process of consistency checking, with the goal to verify the internal data consistency invariants and fix the inconsistent entries. The main difference between `idle_verify` and `partition_reconciliation` is that the latter one can work under the load.

If the topology is changed while the script is running, or if the task execution fails, the command is automatically cancelled.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache partition_reconciliation <cache1,cache2,cache3...> [--repair {option}] [--fast-check] [--parallelism <number>] [--batch-size <number>] [--include-sensitive] [--recheck-attempts <number>] [--recheck-delay <seconds>] [--sensitive-mode {default|hash|plain}]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache partition_reconciliation <cache1,cache2,cache3...> [--repair {option}] [--fast-check] [--parallelism <number>] [--batch-size <number>] [--include-sensitive] [--recheck-attempts <number>] [--recheck-delay <seconds>] [--sensitive-mode {default|hash|plain}]
```
{% endtab %}
{% endtabs %}

The command has the following optional arguments.

|Argument|Description|Default Value|
|---|---|---|
|cache1,cache2,...|A comma-separated list of the caches to be affected by the command. If caches are not specified, the command is executed on all caches.||
|--repair {option}|If specified, fixes all inconsistent data. You can choose the repair algorithm for the keys where the valid key is not obvious.<br><br>**Warning:** Do not use the `repair` argument if you have no intention of auto-fixing the partition reconciliation keys or values.<br><br>The following values can be used:<br>- `print_only` - fixes only those conflicts where the key is present on all nodes. Conflicts with missing keys are printed in the report.<br>- `latest` - picks the latest value. If any partition value is NULL, selects the latest value from the existing NOT NULL partitions. This may result in restoring a removed key.<br>- `primary` - picks a value from the primary partition. Beware: this option may result in key removal.<br>- `latest_trust_missing_primary` - picks the latest value from the primary partition, including NULL values. If the key was removed in the primary partition, it will also be removed in backup partitions. Beware: this option may result in key removal.<br>- `latest_skip_missing_primary` - picks the latest value, skipping reconciliation for any keys that are missing in the primary partition. Beware: this option may leave some data inconsistent.<br>- `mahority` - picks the most common value, or one of the most common values randomly (if there is no consensus). If the missing value is a majority, the key is removed.<br>- `remove` - removes a key if a conflict cannot be resolved without a user algorithm.|`PRINT_ONLY`|
|--fast-check|Checks and repairs only those partitions that did not pass validation during the last partition map exchange. If not specified, all partitions are checked and repaired.||
|--parallelism|The maximum number of threads that can be involved in the reconciliation activities. If not specified, the number of the node's cores is used.||
|--batch-size|The number of keys to retrieve within one job.|1000|
|--include-sensitive|Includes sensitive information in the printout: keys and values.|`false`|
|--recheck-attempts|The number mount of recheck attempts for the potentially inconsistent keys. The recommended value is between 1 and 5.|2|
|--recheck-delay|Recheck delay in seconds.|5|
|--sensitive-mode|The output mode of sensitive information. Possible values:<br>- `default` - same security level as defined for the cluster.<br>- `hash` - hashed representation of objects.<br>- `plain` - plain representation of objects.|`default`|

### cache partition_reconciliation_cancel

Use this command to safely stop the partition reconciliation process. All changes done before the cancellation are preserved.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache  partition_reconciliation_cancel
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache  partition_reconciliation_cancel
```
{% endtab %}
{% endtabs %}

### cache destroy

Use this command to destroy caches.

The syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
 control.sh --cache destroy --caches <cache1,...,cacheN>|--destroy-all-caches
```
{% endtab %}

{% tab title="Windows" %}
```shell
 control.bat --cache destroy --caches <cache1,...,cacheN>|--destroy-all-caches
```
{% endtab %}
{% endtabs %}

The command uses one of the following two arguments:

|Argument|Description|
|---|---|
|--caches|A comma-separated list of names of the caches to be destroyed.|
|--destroy-all-caches|Destroys all user-created caches.|

### cache clear

Use this command to clear caches.

The syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
 control.sh --cache clear --caches <cache1,...,cacheN>
```
{% endtab %}

{% tab title="Windows" %}
```shell
 control.bat --cache clear --caches <cache1,...,cacheN>
```
{% endtab %}
{% endtabs %}

The command uses the following argument:

|Argument|Description|
|---|---|
|--caches|A comma-separated list of names of the caches to be cleared.|

## cache indexes_list

Gets the list of indexes. You can specify filters to narrow down the list.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache indexes_list [--node-id node_id] [--group-name group_name] [--cache-name cache_name] [--index-name index_name]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache indexes_list [--node-id node_id] [--group-name group_name] [--cache-name cache_name] [--index-name index_name]
```
{% endtab %}
{% endtabs %}

|Argument|Description|
|---|---|
|--node-id|The node the command will be executed on. If not specified, the node is chosen automatically.|
|--cache-name|If specified, the command output will be filtered to only include the caches matching the regular expression.|
|--group-name|If specified, the command output will be filtered to only include the cache groups matching the regular expression.|
|--index-name|If specified, the command output will be filtered to only include the indexes matching the regular expression.|

## cache indexes_rebuild_status

Lists all caches the indexes for which are currently being rebuilt.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache indexes_rebuild_status [--node-id node_id]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache indexes_rebuild_status [--node-id node_id]
```
{% endtab %}
{% endtabs %}

|Argument|Description|
|---|---|
|--node-id|The node the command will be executed on. If not specified, the node is chosen automatically.|

## cache indexes_force_rebuild

You can use the `control.sh|bat` script to manage the process of rebuilding indexes for specified caches or cache groups.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
 control.sh --cache indexes_force_rebuild --node-id <nodeId1,...,nodeIdN> --cache-names <cacheName[index1,...indexN],...,cacheName3[index1] --group-names <groupName1,...groupNameN>
```
{% endtab %}

{% tab title="Windows" %}
```shell
 control.bat --cache indexes_force_rebuild --node-id <nodeId1,...,nodeIdN> --cache-names <cacheName[index1,...indexN],...,cacheName3[index1] --group-names <groupName1,...groupNameN>
```
{% endtab %}
{% endtabs %}

The command arguments are as follows:

|Argument|Description|
|---|---|
|--node-id|A comma-separated list of nodes to rebuild indexes on. If not specified, rebuild is scheduled on all nodes.|
|--cache-names|A comma-separated list of cache names, optionally with indexes. If indexes are not specified, all indexes of the cache will be scheduled for the rebuild operation. Can be used in addition to cache group names.|
|--group-names|A comma-separated list of cache group names. Can be used in addition to cache names.|

## Tracing Configuration Management

The `control.sh|bat` script includes a set of commands that enable you to manage tracing configurations.

{% hint style="info" %}
The commands described in this section are experimental. They require the `IGNITE_ENABLE_EXPERIMENTAL_COMMAND` environment variable to be set to `true`.
{% endhint %}

### tracing-configuration

Use this command to print tracing configuration for all scopes and labels.

The syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
 control.sh --tracing-configuration
```
{% endtab %}

{% tab title="Windows" %}
```shell
 control.bat --tracing-configuration
```
{% endtab %}
{% endtabs %}

### tracing-configuration get_all

Use this command to print tracing configuration for all labels and, optionally, the specified `--scope`.

The syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
 control.sh --tracing-configuration get_all [--scope <scope>]
```
{% endtab %}

{% tab title="Windows" %}
```shell
 control.bat --tracing-configuration get_all [--scope <scope>]
```
{% endtab %}
{% endtabs %}

The command uses the following argument:

|Argument|Description|
|---|---|
|--scope|The scope to print the tracing configuration for: `DISCOVERY`, `EXCHANGE`, `COMMUNICATION`, `TX`, `CACHE_API_WRITE`, `CACHE_API_READ`, or `SQL`.|

### tracing-configuration get

Use this command to print tracing configuration for specified `--scope` and `--label`.

The syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
 control.sh --tracing-configuration get --scope <scope> [--label<label>]
```
{% endtab %}

{% tab title="Windows" %}
```shell
 control.bat --tracing-configuration get --scope <scope> [--label<label>]
```
{% endtab %}
{% endtabs %}

The command uses the following arguments:

|Argument|Description|
|---|---|
|--scope|The scope to print the tracing configuration for: `DISCOVERY`, `EXCHANGE`, `COMMUNICATION`, `TX`, `CACHE_API_WRITE`, `CACHE_API_READ`, or `SQL`.|
|--label|The label to print the tracing configuration for.|

### tracing-configuration reset_all

Use this command to reset tracing configurations to default values, then print the reset configurations, optionally for the specified `--scope`.

The syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
 control.sh --tracing-configuration reset_all [--scope <scope>]
```
{% endtab %}

{% tab title="Windows" %}
```shell
 control.bat --tracing-configuration reset_all [--scope <scope>]
```
{% endtab %}
{% endtabs %}

The command uses the following argument:

|Argument|Description|
|---|---|
|--scope|If specified, the command applies the configurations only to the specified scope, which can be `DISCOVERY`, `EXCHANGE`, `COMMUNICATION`, `TX`, `CACHE_API_WRITE`, `CACHE_API_READ`, or `SQL`.|

### tracing-configuration reset

Use this command to reset tracing configurations to default values, then print the reset configurations. If both `--scope` and `--label` are specified, removes the current configuration. If only `--scope` is specified, resets the current configuration to the default.

The syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
 control.sh --tracing-configuration reset --scope <scope> [--label <label>]
```
{% endtab %}

{% tab title="Windows" %}
```shell
 control.bat --tracing-configuration reset --scope <scope> [--label <label>]
```
{% endtab %}
{% endtabs %}

The command uses the following arguments:

|Argument|Description|
|---|---|
|--scope|The command applies to configurations only for the specified scope, which can be `DISCOVERY`, `EXCHANGE`, `COMMUNICATION`, `TX`, `CACHE_API_WRITE`, `CACHE_API_READ`, or `SQL`.|
|--label|If specified, the command applies to configurations for the specified label.|

### tracing-configuration set

Use this command to set a new tracing configuration, then print it.

The syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
 control.sh --tracing-configuration set --scope <scope> [--label <label>] [--sampling-rate <samplingRate>] [--included-scopes <scope, ...>]
```
{% endtab %}

{% tab title="Windows" %}
```shell
 control.bat --tracing-configuration set --scope <scope> [--label <label>] [--sampling-rate <samplingRate>] [--included-scopes <scope, ...>]
```
{% endtab %}
{% endtabs %}

The command uses the following arguments:

|Argument|Description|
|---|---|
|--scope|The command applies to configurations only for the specified scope, which can be `DISCOVERY`, `EXCHANGE`, `COMMUNICATION`, `TX`, `CACHE_API_WRITE`, `CACHE_API_READ`, or `SQL`.|
|--label|If specified, the command applies to configurations for the specified label.|
|--sampling-rate|A decimal value between 0 and 1, where 0 means "never" and 1 means "always." Reflects the probability of sampling a specific trace.|
|--included-scopes|A comma-separated list of scopes that defines the sub-traces to be included in a given trace. In other words, if a child's span scope equals the parent's scope, or if it belongs to the set of scopes included in the parent's span, then the specified child span is attached to the current trace. The scopes can be `DISCOVERY`, `EXCHANGE`, `COMMUNICATION`, `TX`, `CACHE_API_WRITE`, `CACHE_API_READ`, or `SQL`|

## Consistency Checks

The `control.sh|bat` script includes a set of commands that enable you to verify the internal data consistency.

These commands can be used for:

- Debugging and troubleshooting, especially during active development
- Checking for data inconsistencies when there is a suspicion that a query - such as an SQL query - returns an incomplete or wrong result set
- Regular cluster health monitoring

### cache idle_verify

This command compares the hash of the primary partition with that of the backup partitions and reports differences, if any. Said differences might result from node failure or incorrect shutdown during an update operation.

{% hint style="info" %}
If an inconsistency is detected, we recommend removing the problematic partitions.
{% endhint %}

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache idle_verify [<cache1,cache2,cache3...>]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache idle_verify [<cache1,cache2,cache3...>]
```
{% endtab %}
{% endtabs %}

The command has the following optional arguments.

|Argument|Description|
|---|---|
|cache1,cache2,...|A comma-separated list of the caches to be affected by the command.|

A list of diverging partitions is printed out, as follows:

```
idle_verify check has finished, found 2 conflict partitions.

Conflict partition: PartitionKey [grpId=1544803905, grpName=default, partId=5]
Partition instances: [PartitionHashRecord [isPrimary=true, partHash=97506054, updateCntr=3, size=3, consistentId=bltTest1], PartitionHashRecord [isPrimary=false, partHash=65957380, updateCntr=3, size=2, consistentId=bltTest0]]
Conflict partition: PartitionKey [grpId=1544803905, grpName=default, partId=6]
Partition instances: [PartitionHashRecord [isPrimary=true, partHash=97595430, updateCntr=3, size=3, consistentId=bltTest1], PartitionHashRecord [isPrimary=false, partHash=66016964, updateCntr=3, size=2, consistentId=bltTest0]]
```

{% hint style="warning" %}
Cluster must be idle during `idle_verify` checks. All updates should be stopped when `idle_verify` calculates hashes. Otherwise, this operation may show false error results. It's impossible to compare big datasets in a distributed system while these datasets are updated.
{% endhint %}

### cache check_index_inline_sizes

This command verifies that *index inline size* is the same on all cluster nodes. Every entry in the SQL index has a constant size, which is calculated during the index creation. Having different sizes on different nodes in a cluster may lead to performance issues.

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache check_index_inline_sizes
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache check_index_inline_sizes
```
{% endtab %}
{% endtabs %}

The command returns a response in the command line.

### cache validate_indexes

This command validates the indexes of the specified caches on the specified cluster nodes.

It verifies that:

- All key-value entries referenced from the primary index are reachable from the secondary SQL indexes.
- All the key-value entries referenced from the primary index are reachable as defined.
- All the key-value entries referenced from the secondary SQL indexes are reachable from the primary index.

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache validate_indexes <optional arguments>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache validate_indexes <optional arguments>
```
{% endtab %}
{% endtabs %}

The command can use one or both of the following optional arguments:

|Argument|Description|
|---|---|
|cache1,...,cacheN|A comma-separated list of names of the caches to be validated.|
|node ID; e.g., f2ea-5f56-11e8-9c2d-fa7a|ID of the cluster node on which the caches should be validated.|

If indexes refer to non-existing entries, or if some entries are not indexed, errors appear in the command output. Example:

```
PartitionKey [grpId=-528791027, grpName=persons-cache-vi, partId=0] ValidateIndexesPartitionResult [updateCntr=313, size=313, isPrimary=true, consistentId=bltTest0]
IndexValidationIssue [key=0, cacheName=persons-cache-vi, idxName=_key_PK], class org.apache.ignite.IgniteCheckedException: Key is present in CacheDataTree, but can't be found in SQL index.
IndexValidationIssue [key=0, cacheName=persons-cache-vi, idxName=PERSON_ORGID_ASC_IDX], class org.apache.ignite.IgniteCheckedException: Key is present in CacheDataTree, but can't be found in SQL index.
validate_indexes has finished with errors (listed above).
```

{% hint style="warning" %}
Cluster must be idle during `validate_indexes` checks. This command works correctly only if all updates had been stopped. Otherwise, there might be a race between the checker thread and the thread that updates the entry/index, which can result in false errors.
{% endhint %}

### cache distribution

This command prints information about partition distribution.

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --cache distribution nodeId|null [cacheName1,...,cacheNameN] [--user-attributes attrName1,...,attrNameN]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --cache distribution nodeId|null [cacheName1,...,cacheNameN] [--user-attributes attrName1,...,attrNameN]
```
{% endtab %}
{% endtabs %}

The command can use one or both of the following optional arguments:

|Argument|Description|
|---|---|
|node ID; e.g., f2ea-5f56-11e8-9c2d-fa7a|ID of the cluster node whose cache distribution must be queried. Alternatively, "null", which means "all nodes."|
|cacheName1,...,cacheNameN|A comma-separated list of names of the caches whose distribution must be queried. Providing no cache names means "all caches."|
|--user-attributes attrName1,...,attrNameN|A comma-separated list of the names of [node attributes](../monitoring/system-views.md#node_attributes) to be included in the command response. User attributes are [configurable](https://www.gridgain.com/sdk/latest/javadoc/org/apache/ignite/configuration/IgniteConfiguration.html#setUserAttributes-java.util.Map-).|

## Cluster Properties

You can use the control script to set cluster-wide properties.

{% hint style="info" %}
`--property list` may also return entries that are managed internally by the cluster (for example, the cluster ID and tag, the tracing configuration, or the rolling-upgrade status) and are not listed below. Do not set those entries directly, use the dedicated commands instead.
{% endhint %}

Available properties:

|Name|Default|Description|
|---|---|---|
|baselineAutoAdjustEnabled|`false` (for persistence), `true` (for in-memory)|If baseline auto adjust is enabled. When true, baseline topology is adjusted automatically.|
|baselineAutoAdjustTimeout|300000 (5 minutes, for persistence), 0 (for in-memory)|Time in milliseconds to wait before changing the cluster topology when a node is found or leaves the cluster.|
|checkpoint.deviation|null|Checkpoint frequency deviation value in percent. Used to add randomness to checkpoint scheduling to avoid all nodes performing checkpoints simultaneously.|
|checkpoint.frequency|null|Checkpoint frequency in milliseconds. If not `null`, overrides the local configuration of each node in the cluster.|
|collisionsDumpInterval|1000|When above zero, prints tx key collisions once per interval. Each transaction besides `OPTIMISTIC SERIALIZABLE` capture locks on all enlisted keys, for some reasons per key lock queue may rise. This property sets the interval during which statistics are collected.|
|computeJobWorkerInterruptTimeout|`IgniteConfiguration#getFailureDetectionTimeout`|Timeout in milliseconds for interrupting the internal worker for compute jobs after job cancellation. Specifies how long to wait before forcefully interrupting a cancelled job worker thread. By default, each node uses local configuration (30 seconds if not specified).|
|dr.sender.store_scan_policy|`FST_LAST`|DR sender scan policy used when regular replication batches and full state transfer (FST) batches share separate stores. Possible values:<br>- `FST_LAST` - regular DR batches have priority over FST batches (default).<br>- `FST_FIRST` - FST batches have priority over regular DR batches.<br>- `ROUND_ROBIN` - regular and FST batches are scanned with the same priority.<br>- `FAIR` - regular and FST batches are prioritized using a weighted function.|
|exchangelessPointInTimeRecoveryEnabled|`null`|If `true`, the cluster creates snapshots without triggering a partition map exchange. If `false`, snapshots are created using the legacy mode that requires an exchange. Default value is `null`, in which case each node falls back to its local configuration (`true` unless overridden). Requires point-in-time recovery to be enabled.|
|historical.rebalance.threshold|500|Threshold value to use historical (WAL-based) rebalance or full rebalance for local partition. If partition's fullSize exceeds this threshold, historical rebalance is preferred.|
|longOperationsDumpTimeout|60000|Long operations dump timeout in milliseconds. Transactions exceeding this timeout will be logged. 0 means no timeout. The `IGNITE_LONG_OPERATIONS_DUMP_TIMEOUT` system property overrides this property on the node.|
|longTransactionTimeDumpSamplesPerSecondLimit|5|The limit of samples of completed transactions that will be dumped in log per second, if `transactionTimeDumpSamplesCoefficient` is above 0.0. Must be integer value greater than 0. The `IGNITE_TRANSACTION_TIME_DUMP_SAMPLES_PER_SECOND_LIMIT` system property overrides this property on the node.|
|longTransactionTimeDumpThreshold|0|Threshold timeout for long transactions in milliseconds. 0 means no transactions are dumped. The `IGNITE_LONG_TRANSACTION_TIME_DUMP_THRESHOLD` system property overrides this property on the node.|
|pointInTimeRecoveryEnabled|`null`|Cluster-wide switch for the [point-in-time recovery](../../gridgain8-management/snapshots/point-in-time-recovery.md) (PITR) feature. If `true`, PITR is enabled at runtime; if `false`, it is disabled. Default value is `null`, in which case each node falls back to its `DataStorageConfiguration.pointInTimeRecoveryEnabled` setting from the local configuration.|
|shutdown.policy|null|Case-insensitive configuration for cluster shutdown policy. Possible values:<br>- `IMMEDIATE` - stops the node as soon as all components are ready;<br>- `GRACEFUL` - node will stop only if it does not store any unique partitions that do not have other copies in the cluster.<br><br>By default, local configuration on each node is used (`IMMEDIATE` if not specified).|
|snapshotSecurityLevel|`null`|Snapshot file-registry security level. Available only when the snapshot security feature is enabled in the Ultimate Edition. Possible values:<br>- `DISABLED` - the snapshot file registry is not created and is not validated if present (default behavior).<br>- `IGNORE_EXISTING` - new snapshots include a file registry; existing file registries are not verified.<br>- `IGNORE_MISSING` - new snapshots include a file registry; existing file registries are verified when present and tolerated when missing.<br>- `REQUIRE` - new snapshots include a file registry; presence and validity of file registries in all snapshots is required.<br><br>When `null`, the value from the local node configuration is used.|
|sql.defaultQueryTimeout|0|Default query timeout in milliseconds. 0 means no timeout.|
|sql.disabledFunctions|`FILE_READ`, `FILE_WRITE`, `CSVWRITE`, `CSVREAD`, `MEMORY_FREE`, `MEMORY_USED`, `LOCK_MODE`, `LINK_SCHEMA`, `SESSION_ID`, `CANCEL_SESSION`|A comma-separated list of disabled SQL functions. Functions in this set cannot be used in SQL queries.|
|sql.disableCreateLuceneIndexForStringValueType|`false`|Disable creation of Lucene index for String value type by default. If `true`, Lucene indexes are not automatically created for String columns.|
|sql.timeZone|System default|Cluster SQL time zone. When set, all date/time operations in SQL queries use this timezone.|
|statistics.usage.state|`null`|If the cluster collects usage statistics. Possible values are `ON`, `OFF`, or `NO_UPDATE`. Default value is `null`, interpreted as `ON`.|
|thinClientProperty.maxConnectionsPerNode|`null`|Maximum number of active thin client connections per node. Applies to thin clients, ODBC, and thin JDBC connections. Zero means no limit. Default value is `null`, interpreted as `0`.<br><br>The limit is set for each individual server. Example, if the limit is set to 1000 connections, this means each server can accept and handle up to 1000 connections.<br><br>When the limit is dynamically lowered, excess connections are not terminated, but no new ones are established until the total number of connections drops below the limit. Example: there are currently 1000 connections, and we lower the setting to 900. No connections will be terminated, but new ones will not be created until the total number of connections falls to 899 or lower.<br><br>The port itself does not close when the limit is reached. If the limit of available connections is exceeded, a new connection will be accepted but then closed right away before buffers and other server-side resources are allocated, to avoid unnecessary garbage collection.|
|thinClientProperty.showStackTrace|`null`|If `false`, only the top level exception message is included. If `true`, thin client response will include full stack trace when exception occurs. Default value is `null`, interpreted as `false`.|
|tombstones.limit|`null`|Tombstone limit per cache group. Controls the maximum number of tombstones allowed before cleanup operations are triggered. Default value is `null`, interpreted as the largest signed 64-bit integer value.|
|tombstones.suspended.cleanup|`null`|If `true`, tombstone cleanup is disabled. If `false`, tombstone cleanup is enabled. Default value is `null`, interpreted as `false`.|
|tombstones.ttl|`null`|Tombstone time to live in milliseconds. If not specified, is calculated automatically as 1.5 times the failure detection timeout, or 30 seconds, whichever is higher.|
|transactionTimeDumpSamplesCoefficient|`IGNITE_TRANSACTION_TIME_DUMP_SAMPLES_COEFFICIENT`|The coefficient for samples of completed transactions that will be dumped in log. Must be between 0.0 and 1.0. By default, is set to the value of `IGNITE_TRANSACTION_TIME_DUMP_SAMPLES_COEFFICIENT` system property on the node (0.0 unless otherwise specified), if specified overrides it.|
|txOwnerDumpRequestsAllowed|`IGNITE_TX_OWNER_DUMP_REQUESTS_ALLOWED`|If dump requests from local node to near node are allowed when a long running transaction is found. If allowed, compute request to near node will be made to get thread dump of transaction owner thread. By default, is set to the value of the `IGNITE_TX_OWNER_DUMP_REQUESTS_ALLOWED` on the node (`true` unless otherwise specified), if specified overrides it.|

### property list

Use this command to get the full list of the available cluster properties.

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --property list
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat  --property list
```
{% endtab %}
{% endtabs %}

### property set

Use this command to set property values.

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --property set --name <property name> --val <property value>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --property set --name <property name> --val <property value>
```
{% endtab %}
{% endtabs %}

For example, you to enable SQL statistics in a cluster:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --property set --name 'statistics.usage.state' --val 'ON'
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat  --property set --name 'statistics.usage.state' --val 'ON'
```
{% endtab %}
{% endtabs %}

### property get

Use this command to get a property value.

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --property get --name <name>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --property get --name <name>
```
{% endtab %}
{% endtabs %}

### checkpoint

When a user uploads a large volume of data to the cluster, to be sure the data is delivered successfully, you can trigger a manual checkpoint on the cluster.

Use the following command to trigger a checkpoint on a specific node or on all server nodes simultaneously, then wait until the checkpoint completes:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --checkpoint [--node-id <nodeId>] 
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --checkpoint [--node-id <nodeId>]
```
{% endtab %}
{% endtabs %}

The command has the following optional argument:

|Argument|Description|
|---|---|
|node-id|The ID of the node to start checkpoint on. If not specified, checkpoint is started on all nodes.|

In a large distributed database, triggering multiple checkpoints at the same time can create a spike in traffic and, consequently, negatively affect the cluster performance. To prevent this, you can set the `checkpoint.deviation` property to offset checkpoints' time, so that they happen within specified interval of `checkpoint.frequency`. For example, if your checkpoints trigger every 100 seconds, and you set  `checkpoint.deviation` at 10%, your triggers will happen every 95-105 seconds.

The example below offsets the checkpoints by 10% to reduce traffic issues:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --property set --name checkpoint.deviation --val 10
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.sh --property set --name checkpoint.deviation --val 10
```
{% endtab %}
{% endtabs %}

## Cluster Diagnostics

The `control.sh|bat` script provides diagnostics for your cluster.

### diagnostic

Use this command to get diagnostic information for your cluster (page locks or connectivity):

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --diagnostic pageLocks|connectivity dump|dump_log [--path <absolute path>] [--all]|[--nodes <nodeId1,...,nodeIdN>]

```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --diagnostic pageLocks|connectivity dump|dump_log [--path <absolute path>] [--all]|[--nodes <nodeId1,...,nodeIdN>]

```
{% endtab %}
{% endtabs %}

The command arguments are as follows:

|Argument|Description|
|---|---|
|pageLocks|Determines what pages are currently locked and outputs the page lock information to a file/log.|
|connectivity|Detects inter-node communication issues and outputs the corresponding information to log/file.|
|dump|Dumps the page lock information to a file.|
|dump_log|Dumps the page lock information to the log.|
|--path <path>|Optional. If used, provides an absolute path to the folder to write the output to. If not used, the data is saved in the work folder.|
|--all|Gets information on all nodes.|
|--nodes|A comma-separated list of IDs of the nodes to get information on.|

Example `pageLock` output:

```
Thread=[name=main, id=1], state=RUNNABLE
Locked pages = [2[0000000000000002](r=1|w=0)]
Locked pages log: name=main time=(1673270864117, 2023-01-09 15:27:44.117)
L=1 -> Read lock pageId=2, structureId=null [pageIdHex=0000000000000002, partId=0, pageIdx=2, flags=00000000]
```

Example `connectivity` output:

```
There is no connectivity between the following nodes:
SOURCE-NODE-ID                        SOURCE-CONSISTENT-ID     SOURCE-NODE-TYPE  DESTINATION-NODE-ID                   DESTINATION_CONSISTENT_ID  DESTINATION-NODE-TYPE  
ea0b75f5-8c31-4934-b076-edb911800001  gridCommandHandlerTest1  SERVER            3db4a4bb-f758-458c-8569-1ed3e3500003  gridCommandHandlerTest3    SERVER                 
99ac27d8-4e5e-43cd-9acc-1320e6500002  gridCommandHandlerTest2  SERVER            3db4a4bb-f758-458c-8569-1ed3e3500003  gridCommandHandlerTest3    SERVER
```

## Cluster Encryption

You can use the `control.sh|bat` script to manage cluster encryption parameters. For more information about encryption key, see the [Transparent Data Encryption](../../security/tde.md) page.

### encryption get_master_key_name

Use the this command to get the master key that is used in the cluster encryption:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --encryption get_master_key_name
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --encryption get_master_key_name
```
{% endtab %}
{% endtabs %}

### encryption change_master_key

Use the this command to set the master key that is used in the cluster encryption:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --encryption change_master_key <newMasterKeyName>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --encryption change_master_key <newMasterKeyName>
```
{% endtab %}
{% endtabs %}

### encryption change_cache_key

Use this command to change cache-level encryption keys:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --encryption change_cache_key <cacheGroupName>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --encryption change_cache_key <cacheGroupName>
```
{% endtab %}
{% endtabs %}

### encryption cache_key_ids

Use this command to list IDs of the cache group encryption keys:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --encryption cache_key_ids <cacheGroupName>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --encryption cache_key_ids <cacheGroupName>
```
{% endtab %}
{% endtabs %}

### encryption reencryption_status

Use this command to monitor cluster reencryption:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --encryption reencryption_status <cacheGroupName>

```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --encryption reencryption_status cacheGroupName

```
{% endtab %}
{% endtabs %}

### encryption suspend_reencryption

Use this command to pause reencryption of your cluster:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell

control.sh --encryption suspend_reencryption <cacheGroupName>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --encryption suspend_reencryption <cacheGroupName>
```
{% endtab %}
{% endtabs %}

### encryption resume_reencryption

When re-encryption is initiated on the cluster, you can monitor it with the `reencryption_status` subcommand.

Use this command to resume reencryption of your cluster that you had previously suspended (see [encryption suspend_reencryption](#encryption-suspend_reencryption)):

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --encryption resume_reencryption <cacheGroupName>
```
{% endtab %}

{% tab title="Windows" %}
```shell

control.bat --encryption resume_reencryption <cacheGroupName>
```
{% endtab %}
{% endtabs %}

### encryption reencryption_rate_limit

Encryption requires a large amount of system resources. One way to address this is to suspend reencryption to allow the system to handle the workload - see [encryption suspend_reencryption](#encryption-suspend_reencryption). Alternatively, you can use this command to limit the reencryption rate.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --encryption reencryption_rate_limit <limit in MB/sec>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --encryption reencryption_rate_limit <limit in MB/sec>
```
{% endtab %}
{% endtabs %}

## Kill Queries

### kill sql

This command stops the specific sql query.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --kill SQL <queryId>

```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --kill SQL <queryId>
```
{% endtab %}
{% endtabs %}

Use the SQL_QUERIES [system view](../monitoring/system-views.md#sql_queries) to get the IDs of currently running queries.

### kill client

This command drops the connection to the specific [client]({connectors}/thin-clients/getting-started-with-thin-clients).

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --kill CLIENT <connection_id> [--node-id node_id]

```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --kill CLIENT <connection_id> [--node-id node_id]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|connection_id|The identifier of the connection to drop or `ALL` to drop all connections.|
|--node-id|Optional; if used, drops the connection from a specific node.|

### kill continuous

This command stops the specific [continuous query](../../gridgain8-usage/continuous-queries.md).

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --kill CONTINUOUS <NodeId> <routineId>

```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --kill CONTINUOUS <NodeId> <routineId>
```
{% endtab %}
{% endtabs %}

Use the CONTINUOUS_QUERIES [system view](../monitoring/system-views.md#continuous_queries) to get the origin node ID and routine ID for your queries.

### kill scan

This command stops the specific [scan query](../../gridgain8-usage/key-value-api/using-scan-queries.md).

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --kill SCAN <origin_node_id> <cache_name> <query_id>

```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --kill SCAN <origin_node_id> <cache_name> <query_id>
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|origin_node_id|The ID of the node the query originates from.|
|cache_name|The name of the cache in the query.|
|query_id|The query identifier.|

### kill compute

This command stops the specific [compute task](../../gridgain8-usage/distributed-computing/distributed-computing.md).

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --kill COMPUTE  <session_id>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --kill COMPUTE  <session_id>
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|session_id|Session identifier.|

### kill service

This command stops the specific [service](../../gridgain8-usage/services/services.md).

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --kill SERVICE <name>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --kill SERVICE <name>
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|name|Service name.|

### kill transaction

This command stops the specific [transaction](../../gridgain8-usage/transactions.md).

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --kill TRANSACTION <id>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --kill TRANSACTION <id>
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|id|Transaction identifier.|

## Rolling Upgrades

You can manage rolling upgrades using the `control.sh|bat` script.

### rolling-upgrade start

Use this command to enable rolling upgrades:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --rolling-upgrade start [--yes]

```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --rolling-upgrade start [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### rolling-upgrade finish

Use this command to disable rolling upgrades:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell

control.sh --rolling-upgrade finish [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell

control.bat --rolling-upgrade finish [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### rolling-upgrade force

Use this command to force a rolling upgrade on your cluster.

{% hint style="warning" %}
Forcing may cause unexpected issues during a rolling upgrade.
{% endhint %}

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --rolling-upgrade force [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --rolling-upgrade force [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### rolling-upgrade status

Use this command to check the current status of the rolling upgrade on your cluster:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --rolling-upgrade status
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --rolling-upgrade status
```
{% endtab %}
{% endtabs %}

## Cluster IDs and Tags

You can set cluster ID and tag values using the `control.sh|bat` script.

### change-id

Use this command to change the cluster ID of in-memory clusters.

{% hint style="info" %}
This command does not apply to [persistent clusters](../../architecture/storage/native-persistence.md).
{% endhint %}

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --change-id <newIdValue> [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --change-id <newIdValue> [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|newIdValue|The new ID for the cluster.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### change-tag

Use this command to change the cluster tag of in-memory clusters.

{% hint style="info" %}
This command does not apply to [persistent clusters](../../architecture/storage/native-persistence.md).
{% endhint %}

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --change-tag <newTagValue> [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --change-tag <newTagValue> [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|newTagValue|The new tag for the cluster.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

## Data Center Replication

You can use the `control.sh|bat` script to track data center replication.

### dr state

Use this command to get the current state of data center replication:

With the `--verbose` option, you can get extended status information.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr state [--verbose]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr state [--verbose]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--verbose|Optional; if used, prints extended status information.|

### dr topology

Use this command to print the cluster topology with the Data Center Replication details:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr topology [--sender-hubs] [--receiver-hubs] [--data-nodes] [--other-nodes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr topology [--sender-hubs] [--receiver-hubs] [--data-nodes] [--other-nodes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--sender-hubs|Optional; if used, displays information about sender nodes.|
|--receiver-hubs|Optional; if used, displays information about receiver nodes.|
|--data-nodes|Optional; if used, displays information about data nodes in the cluster.|
|--other-nodes|Optional; if used, displays information about nodes that are not currently involved in the DR.|

### dr pause

Use this command to [pause data center replication](../../gridgain8-management/data-center-replication/managing-and-monitoring.md#pausing-and-resuming-replication) on all sender nodes, or on a specific sender node.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr pause <remoteDataCenterId> [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr pause <remoteDataCenterId> [--yes]

```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|remoteDataCenterId|The ID of the remote data center.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### dr resume

Use this command to [resume data center replication](../../gridgain8-management/data-center-replication/managing-and-monitoring.md#pausing-and-resuming-replication) on all sender nodes, or on a specific sender node.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr resume <remoteDataCenterId> [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr resume <remoteDataCenterId> [--yes]

```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|remoteDataCenterId|The ID of the remote data center.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### dr full-state-transfer start

Use this command to execute a full state transfer on all caches in a cluster if the caches in the master cluster already have data:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr full-state-transfer start [--snapshot <snapshotId>]  [--caches <cache1, ...>] [--sender-group <group1, ...>] [--data-centers <dcId, ...>] [--sync] [--yes] 
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr full-state-transfer start [--snapshot <snapshotId>]  [--caches <cache1, ...>] [--sender-group <group1, ...>] [--data-centers <dcId, ...>] [--sync] [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--snapshot|Optional; the ID of the snapshot to perform the state transfer on.|
|--caches|Optional; the list of caches to transfer.|
|--sender-group|Optional; the group of the sender caches. Possible values: <groupName>, ALL, DEFAULT, NONE.|
|--data-centers|Optional; IDs of the data centers involved in the transfer.|
|--sync|Optional; if used, executes the full state transfer in a synchronous way. Otherwise, the full state transfer is executed asynchronously.|
|--yes|Optional; if used, it fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### dr check-partition-counters

Use this command to check whether all partition counters are in order:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr check-partition-counters [--caches <cache1,...>] 
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr check-partition-counters [--caches cache1,cache2]
```
{% endtab %}
{% endtabs %}

The command argument is as follows.

|Argument|Description|
|---|---|
|--caches|Optional; the list of caches to check the partition counters for.|

### dr rebuild-partition-tree

Use this command to schedule/run the maintenance task for rebuilding DR trees:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr rebuild-partition-tree [--caches <cacheName1,...,cacheNameN>] [--groups <groupName1,...,groupNameN>] [--yes] 
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr rebuild-partition-tree [--caches <cacheName1,...,cacheNameN>] [--groups <groupName1,...,groupNameN>] [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--caches|A comma-separated list of caches to be affected by the command.|
|--groups|A comma-separated list of cache groups to be affected by the command.|
|--yes|If used, fast-forwards the command by automatically answering "yes" to all of the command’s prompts.|

### dr repair-partition-counters

Use this command to repair partition counters during data center replication:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr repair-partition-counters [--caches <cache1,...>] 
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr repair-partition-counters [--caches cache1,cache2]
```
{% endtab %}
{% endtabs %}

The command argument is as follows.

|Argument|Description|
|---|---|
|--caches|Optional; the list of caches to check the partition counters for.|

### dr cleanup-partition-tree

Use this command to schedule and run a maintenance task to clean up DR trees:

{% hint style="info" %}
The operation this command initiates can be performed only in the [maintenance mode](../../ha-and-performance/maintenance-mode.md).
{% endhint %}

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr cleanup-partition-tree [--caches <cacheName1,...,cacheNameN>] [--groups <groupName1,...,groupNameN>] [--nodes <consistentId0,consistentId1,...,consistentIdN>] [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr cleanup-partition-tree [--caches <cacheName1,...,cacheNameN>] [--groups <groupName1,...,groupNameN>] [--nodes <consistentId0,consistentId1,...,consistentIdN>] [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--caches|Optional; the list of caches to clean up.|
|--groups|Optional; the list of cache groups to clean up.|
|--nodes|Optional; the list of nodes the command is run on.|
|--yes|If used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### dr reset-partition-tree

Use this command to reset the DR partition log state and drop existing DR tree data at run time.

Unlike `dr cleanup-partition-tree`, this command does not require maintenance mode.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr reset-partition-tree [--caches <cacheName1,...,cacheNameN>] [--partitions <0,1,...,N>] [--nodes <consistentId0,consistentId1,...,consistentIdN>] [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr reset-partition-tree [--caches <cacheName1,...,cacheNameN>] [--partitions <0,1,...,N>] [--nodes <consistentId0,consistentId1,...,consistentIdN>] [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--caches|Optional; the list of caches to reset.|
|--partitions|Optional; the list of partition IDs to reset.|
|--nodes|Optional; the list of nodes the command is run on.|
|--yes|If used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### checkpointing force

Use this command to dump all data to persistent storage (for example, to make sure that all data is saved before deleting the source data):

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --checkpointing force
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --checkpointing force
```
{% endtab %}
{% endtabs %}

### dr full-state-transfer cancel

Use this command to cancel an active full state transfer at any time:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr full-state-transfer cancel <fullStateTransferUID> [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr full-state-transfer cancel <fullStateTransferUID> [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|fullStateTransferUID|The ID of the fill state transfer to cancel.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### dr full-state-transfer list

Use this command to get a list of all full state transfers currently in progress.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr full-state-transfer list
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr full-state-transfer list
```
{% endtab %}
{% endtabs %}

### dr node

Use this command to get information about a node's status during data center replication:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr node <nodeId> [--config] [--metrics] [--clear-store] [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr node <nodeId> [--config] [--metrics] [--clear-store] [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--config|Optional; displays node configuration.|
|--metrics|Optional; displays node metrics.|
|--clear-store|Optional; cleans store after the command execution.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

### dr cache

Use this command to get specific cache details related to data center replication:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --dr cache <regExp> [--config] [--metrics] [--cache-filter ALL|SENDING|RECEIVING|PAUSED|ERROR] [--sender-group <groupName>|ALL|DEFAULT|NONE] [--action stop|start|full-state-transfer] [--yes]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --dr cache <regExp> [--config] [--metrics] [--cache-filter ALL|SENDING|RECEIVING|PAUSED|ERROR] [--sender-group <groupName>|ALL|DEFAULT|NONE] [--action stop|start|full-state-transfer] [--yes]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--config|Optional; displays cache configuration.|
|--metrics|Optional; displays node metrics.|
|--cache-filter|Optional; the cache filter. Possible values: ALL, SENDING, RECEIVING, PAUSED, ERROR.|
|--sender-group|Optional: the group of the sender caches. Possible values: <groupName>, ALL, DEFAULT, NONE.|
|--action|Optional; the action to perform. Possible values: stop, start, full-state-transfer.|
|--yes|Optional; if used, fast-forwards the command by automatically answering "yes" to all of the command's prompts.|

## Shutdown Policies

### shutdown-policy

Use the `shutdown-policy` command to set the node shutdown policy to:

- GRACEFUL - to have nodes manage their ongoing tasks before they shut down
- IMMEDIATE - to have nodes shut down immediately

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --shutdown-policy [IMMEDIATE|GRACEFUL]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --shutdown-policy [IMMEDIATE|GRACEFUL]
```
{% endtab %}
{% endtabs %}

## Warmup Configuration

### warm-up

Use the `warm-up` command to disable cache warmup on the cluster:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --warm-up --stop
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --warm-up --stop
```
{% endtab %}
{% endtabs %}

## Persistence Configuration

You can use the `control.sh|bat` script to define the way the data files and caches are treated.

### persistence

This command works only for nodes in [maintenance](../../ha-and-performance/maintenance-mode.md) mode.

To get information about the potentially corrupted caches on a local node, use either:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --persistence
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.sh --persistence
```
{% endtab %}
{% endtabs %}

or `--persistence info` command, that prints the same information.

### persistence clean

Use this command to clean persistent caches.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --persistence clean [corrupted]|[all]|[caches <cache1,cache2,...,cacheN>]

```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --persistence clean [corrupted]|[all]|[caches <cache1,cache2,...,cacheN>]

```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|corrupted|Optional; cleans corrupted caches.|
|all|Optional; cleans all caches.|
|caches|Optional; cleans caches included in a comma-delimited list.|

### persistence backup

Use this command to back up caches:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --persistence backup [corrupted]|[all]|[caches <cache1,cache2,...,cacheN>]

```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --persistence backup [corrupted]|[all]|[caches <cache1,cache2,...,cacheN>]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|corrupted|Optional; backs up corrupted caches.|
|all|Optional; backs up all caches.|
|caches|Optional; backs up caches included in a comma-delimited list.|

## Snapshots

The `--snapshot` command is an Apache Ignite 2 compatibility layer over GridGain snapshots. Use it to run existing Apache Ignite 2 snapshot scripts against a GridGain cluster without rewriting them.

To manage GridGain snapshots directly, use the [`snapshot-utility.sh`](../../gridgain8-management/snapshots/snapshots-management-tool.md) tool instead, which exposes the full GridGain feature set.

The command requires the Ultimate Edition.

{% hint style="warning" %}
The command cannot read snapshot files written by Apache Ignite. It operates only on snapshots created by GridGain.
{% endhint %}

### snapshot create

Use this command to create a snapshot of all persistent cache groups in the cluster:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --snapshot create <snapshotName> [--incremental] [--dest <path>] [--sync]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --snapshot create <snapshotName> [--incremental] [--dest <path>] [--sync]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows:

|Argument|Description|
|---|---|
|snapshotName|The name of the snapshot to create. The name must be unique: GridGain does not reuse snapshot names, so delete the existing snapshot first if the name is taken.|
|--incremental|Optional. Creates an incremental snapshot that extends an existing full snapshot instead of creating a new full snapshot. GridGain extends only the latest full snapshot, so `snapshotName` must name that snapshot.|
|--dest|Optional. The directory to write the snapshot to. If not specified, the configured snapshot path is used.|
|--sync|Optional. Waits for the operation to complete before returning. If not specified, the command returns as soon as the operation starts.|

### snapshot cancel

Use this command to cancel a running snapshot operation:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --snapshot cancel (--id <operationId>|--name <snapshotName>)
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --snapshot cancel (--id <operationId>|--name <snapshotName>)
```
{% endtab %}
{% endtabs %}

Specify exactly one of `--id` or `--name`. The command fails if you pass both or neither.

The command arguments are as follows:

|Argument|Description|
|---|---|
|--id|The ID of the operation to cancel, as reported by [snapshot status](#snapshot-status).|
|--name|The name of the snapshot whose operation you want to cancel. If no operation with that name is running, the command does nothing.|

### snapshot restore

Use this command to restore cache groups from a snapshot:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --snapshot restore <snapshotName> [--increment <index>] [--groups <group1,...,groupN>] [--src <path>] [--sync]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --snapshot restore <snapshotName> [--increment <index>] [--groups <group1,...,groupN>] [--src <path>] [--sync]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows:

|Argument|Description|
|---|---|
|snapshotName|The name of the snapshot to restore.|
|--increment|Optional. Restores the full snapshot and its increments up to the given index. Must be a non-negative integer; `0` restores the full snapshot only.|
|--groups|Optional. A comma-delimited list of cache groups to restore. If not specified, all cache groups in the snapshot are restored. Names are matched against GridGain cache names.|
|--src|Optional. The directory to read the snapshot from. If not specified, the configured snapshot path is used.|
|--sync|Optional. Waits for the operation to complete before returning. If not specified, the command returns as soon as the operation starts.|

To cancel a running restore, use [snapshot cancel](#snapshot-cancel) with the snapshot name.

### snapshot status

Use this command to print the status of the snapshot operation currently running in the cluster:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --snapshot status
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --snapshot status
```
{% endtab %}
{% endtabs %}

The command takes no arguments. If an operation is running, it prints the operation type, the snapshot name, the operation request ID, and the start time:

```
Create snapshot operation is in progress.
Snapshot name: nightly
Operation request ID: 6bf1e0a1c91-42e6b1d5-9f0c-4a7e-8d3b-2c5a91ff0e14
Started at: Jul 31, 2026, 4:05:22 PM
```

Otherwise it prints `There is no create or restore snapshot operation in progress.`

{% hint style="info" %}
Unlike Apache Ignite 2, this command does not print a per-node progress table.
{% endhint %}

## Defragmentation

When persistence is enabled on the disk, you need to perform data defragmentation on that disk.

### defragmentation schedule

Use this command to schedule the disk defragmentation:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --defragmentation schedule --nodes <consistentId0,...,consistentIdN,> [--caches <cache1,cache2,...,cacheN>]

```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --defragmentation schedule --nodes <consistentId0,...,consistentIdN,> [--caches <cache1,cache2,...,cacheN>]

```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--nodes|A comma-separate list of nodes to undergo defragmentation.|
|--caches|Optional; a comma-separated list pf caches to undergo defragmentation.|

### defragmentation cancel

Use this command to cancel a scheduled or active defragmentation if it interferes with other operations:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh  --defragmentation cancel
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --defragmentation cancel
```
{% endtab %}
{% endtabs %}

### defragmentation status

Use this command to check the status the current defragmentation process.

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh  --defragmentation status
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --defragmentation status
```
{% endtab %}
{% endtabs %}

## Metric

Use the `metric` command to get the current value of a specific metric or all metrics in a metric registry.

### metric

Use the following command to print the value of a metric or, if a metric registry name is provided, the values of all metrics in that registry:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --metric [--node-id <node_id>] <name>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --metric [--node-id <node_id>] <name>
```
{% endtab %}
{% endtabs %}

The command arguments are as follows:

|Argument|Description|
|---|---|
|name|The name of the metric whose value should be printed. If the name of a metric registry is specified, the values of all its metrics are printed.|
|--node-id|Optional. The ID of the node to get the metric value from. If not specified, a random node is chosen.|

## Binary Type Management

### meta list

Use this command to list meta information:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --meta list
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --meta list
```
{% endtab %}
{% endtabs %}

The command prints one line per registered binary type, with the following fields:

- `typeId=<ID>`
- `typeName=<name>`
- `fields=<count>`
- `schemas=<count>`
- `isEnum=<bool>`
- `affinityKeyFieldName=<name>`

The example below shows the command output:

```shell
typeId=0xCC882ED7 (-863490345), typeName=org.apache.ignite.util.GridCommandExample, fields=2, schemas=1, isEnum=false, affinityKeyFieldName=affField
```

### meta details

Use this command to print information about the specified binary type:

- `typeId=<ID>`
- `typeName=<name>`
- `affinityKeyFieldName=<name>`
- `fields=<fields_count>`
- `schemas=<schemas_count>`
- `isEnum=<bool>`

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --meta details --typeId <ID>|--typeName <name>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --meta details --typeId <ID>|--typeName <name>
```
{% endtab %}
{% endtabs %}

One of the following command arguments must be used.

|Argument|Description|
|---|---|
|--typeId|The ID of the binary type.|
|--typeName|The name of the binary type.|

Following is an example of the command output:

```shell
typeId=0xCC882ED7 (-863490345)
typeName=org.apache.ignite.util.GridCommandExample
affinityKeyFieldName=affField
Fields:
  name=val, type=int, fieldId=0x1C721 (116513)
  name=affField, type=String, fieldId=0x23EA8CB9 (602574009)
Schemas:
  schemaId=0xE3B0A4D6 (-474962730), fields=[affField, val]
```

### meta remove

Use this command to remove metadata for the specified type form the cluster and save the removed metadata to a file.

{% hint style="info" %}
This command requires a confirmation. All client sessions (ODBC, JDBC, and thin clients) are closed to remove the binary metadata from the local cache.
{% endhint %}

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --meta remove --typeId <ID>| --typeName <name> [--out <file_name>]
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --meta remove --typeId <ID>| --typeName <name> [--out <file_name>]
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--typeId|The ID of the binary type.|
|--typeName|The name of the binary type.|
|--out|The name of the file to save the removed metadata to. If not specified, the default `<typeId>.bin` is used.|

### meta update

Use this command to updates cluster metadata from a specified file.

{% hint style="info" %}
This command requires a confirmation.
{% endhint %}

The command syntax is as follows:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
control.sh --meta update --in <file_name>
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --meta update --in <file_name>
```
{% endtab %}
{% endtabs %}

The command arguments are as follows.

|Argument|Description|
|---|---|
|--in|The name of the file to use as a source of the metadata.|

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
