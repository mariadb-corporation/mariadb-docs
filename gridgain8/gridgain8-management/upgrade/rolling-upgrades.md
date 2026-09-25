---
description: >-
  How to use GridGain Enterprise/Ultimate Rolling Upgrades to upgrade a cluster
  version without downtime, including the process, monitoring, guidelines, and the Java API.
---

# Rolling Upgrades

## Overview

_Rolling Upgrades_ is a feature of GridGain Enterprise and Ultimate Edition that allows nodes with different GridGain versions to coexist in a cluster while you roll out a new version. This prevents downtime when performing software
upgrades.

With Rolling Upgrades [enabled](#enable-rolling-upgrades), you can have a new node with a newer version of GridGain join the cluster. For example, if you have ten nodes running on ten physical servers, you can start a new node with a new version of GridGain on any of the servers. The data is rebalanced to accommodate this new member of the cluster. Once the data rebalancing is complete, you can shut down the old node. Then repeat the above process for all server nodes.

## Enable Rolling Upgrades

The Rolling Upgrades feature is disabled by default. To upgrade GridGain without stopping the entire cluster, you need to enable this feature.

{% hint style="info" %}
Enabling rolling upgrades may have a [performance impact](#performance-considerations) on your environment.
{% endhint %}

To enable Rolling Upgrades:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="pluginConfigurations">
        <list>
            <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
                <property name="rollingUpdatesEnabled" value="true"/> 
            </bean>
        </list>
    </property>

</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
GridGainConfiguration pluginCfg = new GridGainConfiguration();
pluginCfg.setRollingUpdatesEnabled(true);

IgniteConfiguration cfg = new IgniteConfiguration();
cfg.setPluginConfigurations(pluginCfg);

Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new GridGainPluginConfiguration()
{
    RollingUpdatesEnabled = true
};
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

This page contains:

* [The Rolling Upgrade Process](#the-rolling-upgrade-process)
* [Performance Considerations](#performance-considerations)
* [Rolling Upgrade Monitoring in Control Center](#rolling-upgrade-monitoring-in-control-center)
* [Guidelines and Incompatible Versions](#guidelines-and-incompatible-versions)
* Example: Using Rolling Upgrades for Migration.

## The Rolling Upgrade Process

{% hint style="info" %}
The functionality described below is available in GridGain starting from version 8.8.1.
{% endhint %}

### Start a Rolling Upgrade

To start a Rolling Upgrade:

{% tabs %}
{% tab title="Unix" %}
```shell
control.sh --rolling-upgrade start --yes
```
{% endtab %}
{% tab title="Windows" %}
```shell
control.bat --rolling-upgrade start --yes
```
{% endtab %}
{% endtabs %}

The Rolling Upgrades feature enable you to connect nodes with only one GridGain version different from (more recent than) the current one.

To suppress this constraint, you can activate the Rolling Updates using the "force" option: 

{% tabs %}
{% tab title="Unix" %}
```shell
control.sh --rolling-upgrade force
```
{% endtab %}
{% tab title="Windows" %}
```shell
control.bat --rolling-upgrade force
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Using the "force" option is not recommended. Trying to join a node with an old version with this option may cause severe errors if a new node already uses a new communication protocol.
{% endhint %}

### Perform the Rolling Upgrade

Once you have [activated a rolling upgrade](), you can upgrade a multi-node cluster to a new GridGain version without stopping the whole cluster:

1. Download the new GridGain version.
2. If you are using persistence: Configure `storagePath`, `walPath` and `walArchivePath` properties. If these properties are explicitly configured in the current version of GridGain you are using, then provide the same value of these properties to the new GridGain version's configuration. If these properties are not set, provide the default location used by these properties.
3. Stop one running node.
4. Restart the node with the new version. At this point, the cluster will start to rebalance.
5. Wait while the rebalancing is going on. You can monitor the logs for something like this:

   ```text
Rebalancing scheduled [order=[Cache1, Cache2, Cache3], top=AffinityTopologyVersion [topVer=59, minorTopVer=1], force=false, evt=DISCOVERY_CUSTOM_EVT, node=79794392-5518-4609-ac13]
...
...
...
Completed (final) rebalancing [fromNode=node=79794392-5518-4609-ac13, cacheOrGroup=Cache2, topology=AffinityTopologyVersion [topVer=59, minorTopVer=1], time=370550 ms]
   ```

   After this, there is a partition map exchange for the new minor topology
   change, which is caused by Late Affinity Assignment. So, instead of checking
   the rebalancing for all the caches, you can look for a message about the
   exchange:

   ```text
Finish exchange future [startVer=AffinityTopologyVersion [topVer=42, minorTopVer=1], resVer=AffinityTopologyVersion [topVer=42, minorTopVer=1], err=null]
   ```

   Alternatively, if rebalancing is not needed, it is skipped:

   ```text
Skipping rebalancing (no affinity changes) [top=AffinityTopologyVersion [topVer=42, minorTopVer=1], rebTopVer=AffinityTopologyVersion [topVer=42, minorTopVer=0], evt=DISCOVERY_CUSTOM_EVT, evtNode=38640608-5518-4609-ac13-0b35eea1d6cb, client=false]
   ```
6. After rebalancing is complete, repeat steps 1-6 for all nodes.

{% hint style="info" %}
Due to performance reasons, it is not advisable to run multiple versions of GridGain in the cluster for a long period of time.
{% endhint %}

### Check the Rolling Upgrade Status

To check the Rolling Upgrade status:

{% tabs %}
{% tab title="Unix" %}
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

### Stop the Rolling Upgrade

The features available from a newer GridGain version are not activated until you manually stop the Rolling Upgrades process. To stop the Rolling Upgrade:

{% tabs %}
{% tab title="Unix" %}
```shell
control.sh --rolling-upgrade finish
```
{% endtab %}
{% tab title="Windows" %}
```shell
control.bat --rolling-upgrade finish
```
{% endtab %}
{% endtabs %}

## Performance Considerations

When Rolling Upgrades are enabled, every network message is appended with rolling upgrade data. In most situations, the overhead is small compared to the overall throughput and has almost no performance impact. This includes workloads dealing with medium- or large-sized entries (1 KB and larger), as well as compute-intensive applications.

The impact can get more noticeable if the system handles a comparatively larger number of smaller entries and messages. Using batching techniques (for example, [data streamer](../../gridgain8-usage/data-streaming.md) or [putAll method](https://www.gridgain.com/sdk/latest/javadoc/org/apache/ignite/IgniteCache.html#putAll-java.util.Map-)) allows you to combine entries in larger requests and reduce the overhead ratio.

## Rolling Upgrade Monitoring in Control Center

GridGain [Control Center]({tools}/control-center) allows you to monitor the process of Rolling Upgrades as you move to a newer version of GridGain.

The [Rebalance widget]({tools}/control-center/gg8/dashboard/configuring-widgets#rebalance-widget) in Control Center displays the cluster nodes and their versions. As you perform node-by-node migration to a newer version, watch the status of the rebalancing progress and proceed to the next node when it is finished.

## Guidelines and Incompatible Versions

{% hint style="warning" %}
Before upgrading to a new version, refer to the release notes for that version for information about the possibility of performing a rolling upgrade. The release notes contain information about incompatibilities and additional steps required to perform a rolling upgrade.
{% endhint %}

Before you start to upgrade to a newer version of GridGain, please note the following:

* Upgrades are supported for minor and maintenance versions of the same major series only. The feature is not supported for upgrades between major versions due to the changes that might not be backward-compatible. For instance, it is possible to upgrade from 8.5.6 to 8.7.5 without downtime, but rolling upgrades will not work from version 7.9.1 to 8.7.5. For major version upgrades, contact GridGain for a possible zero-downtime solution.

* There is always a way to upgrade to the latest GridGain version from any version of the same major series without downtime. In most cases, it is a direct one-step upgrade. For instance, you can upgrade from 8.5.6 to 8.7.5 with rolling upgrades, avoiding production outages.

* Suppose there are any breaking changes between minor or maintenance versions of the same series.
In that case, the upgrade involves a transitioning version: moving from version "A" to version "B" via "C" without production outages. For instance, if you need to upgrade from 8.1.3 to 8.8.1, then 8.5.3 has to be used as a transitioning version: 8.1.3 -> 8.5.3 -> 8.8.1.

## Rolling Upgrade Example

This example demonstrates how to use the Rolling Upgrade functionality to upgrade a cluster from GridGain version 8.8.0 to 8.8.1:

1. Check the current status of the Rolling Upgrade:

   {% tabs %}
   {% tab title="Unix" %}
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

   Currently, the initial version corresponds to the current version of the cluster, and the Rolling Upgrades are disabled.
   If you run a new version, the joining node throws an exception, as shown below:

   ```text
The local node's build version differs from the remote node's [locBuildVer=8.7.23#20200728-sha1:4e015639, rmtBuildVer=8.8.0#20200714-sha1:35c405b6].
The node has been rejected due to the disabled Rolling Upgrade.
Please consider enabling it via control.sh utility with the following command: `--rolling-upgrade start` or using GridGain.rollingUpgrade().start() method.
   ```
2. Start a Rolling Upgrade:

   {% tabs %}
   {% tab title="Unix" %}
   ```shell
control.sh --rolling-upgrade start --yes
   ```
   {% endtab %}
   {% tab title="Windows" %}
   ```shell
control.bat --rolling-upgrade start --yes
   ```
   {% endtab %}
   {% endtabs %}
3. Check the Rolling Upgrade status:

   {% tabs %}
   {% tab title="Unix" %}
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
4. When a new node connects to a new cluster, its version is saved in the target version, which you can verify by checking the status again:

   ```text
Rolling upgrade is enabled
Initial version: 8.8.0#20200714-sha1:35c405b6
Target version: 8.8.1#20200728-sha1:4e015639
List of alive nodes in the cluster that are not updated yet: 54a088fb
List of alive nodes in the cluster that are updated: 01110503
   ```

   {% hint style="info" %}
   You cannot change versions until the update process is complete. If you try to stop the Rolling Upgrade in an inconsistent state, you will get an error, as shown in the example below:
   {% endhint %}

   ```text
Rolling upgrade operation failed. Rolling Upgrade mode cannot be disabled.
Rolling upgrade cannot be disabled because there is more than one node with a
different product version.

8.8.0#20200714-sha1:35c405b6=Nodes: [0:0:0:0:0:0:0:1%lo],
8.8.1#20200728-sha1:4e015639=Nodes: [0:0:0:0:0:0:0:1%lo]
   ```
5. Once the last old node is released, you can stop the upgrade process:

   {% tabs %}
   {% tab title="Unix" %}
   ```shell
control.sh --rolling-upgrade finish
   ```
   {% endtab %}
   {% tab title="Windows" %}
   ```shell
control.bat --rolling-upgrade finish
   ```
   {% endtab %}
   {% endtabs %}

### Reverting Rolling Upgrades

You can revert a Rolling Upgrade while its process is still in progress. Even if the target version is identified, it is yet possible to shut down all nodes with the target version (8.8.1) and disable Rolling Upgrade. In this case, the initial version remains unchanged (8.8.0).

{% hint style="info" %}
If you use the [persistence](../../architecture/storage/native-persistence.md) functionality, the rolling upgrade status is persisted as well. You may shut down the whole cluster during the rolling upgrade and resume the process after the restart.
After the upgrade is finished, the initial version is changed to the upgrade target version, as illustrated in the example below:
{% endhint %}

```text
The cluster must not contain node older than the initial [initVer=8.7.23#20200728-sha1:4e015639, nodeVer=8.8.0#20200714-sha1:35c405b6]
```

### Using Java API to Manage a Rolling Upgrade

Since [control.sh](../../reference/cli-tool/README.md) is based on the Java API, you can use Java to manage rolling upgrades programmatically. For that purpose, use the following methods:

| Method Name | Description |
|---|---|
| `start` | Activates rolling upgrade mode or throws an exception if it is not possible. |
| `finish` | Disables rolling upgrade mode or throws an exception if it is not possible. |
| `force` | Switches rolling upgrade to the "force" mode. |
| `getStatus` | Returns the state of the rolling upgrade process. |

A full description is provided in the `GridGainRollingUpgrade` class.

The following examples illustrate how to use the Java API to manage rolling upgrades:

```java
/**
* Enables rolling upgrade mode.
*/
public void start();

/**
* Disables rolling upgrade mode.
*/
public void finish();

/**
* Enables forced mode of rolling upgrade. This means that the strict version checking of the node should not be
* used and therefore this mode allows to coexist more than two versions of Ignite nodes in the cluster.
*/
public void force();

/**
* Returns cluster-wide status of Rolling Upgrade process.
*
* @return status of Rolling Upgrade process.
*/
public GridRollingUpgradeStatus getStatus();
```

The following example illustrates how to use this function in java code:

```java
try (Ignite ig = Ignition.start("your_configuration.xml")) {
GridGain gg = ig.plugin(GridGain.PLUGIN_NAME);
GridGainRollingUpgrade ru = gg.rollingUpgrade();

 GridRollingUpgradeStatus status = ru.getStatus();

 ru.start();
 ru.finish();
 ru.force();
}
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
