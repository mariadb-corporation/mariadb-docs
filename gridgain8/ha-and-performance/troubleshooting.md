---
description: >-
  Common tips and techniques for debugging and troubleshooting GridGain and Ignite
  deployments, including persistence, thin clients, GC issues, and node recovery.
---

# Troubleshooting and Debugging

This article covers some common tips and tricks for debugging and troubleshooting GridGain and Ignite deployments.

## Debugging Tools: Consistency Check Command

The `./control.sh|bat` utility includes a set of [consistency check commands](../reference/cli-tool/README.md#consistency-checks) that help with verifying internal data consistency invariants.

## Persistence Files Disappear on Restart

On some systems, the default location for Ignite persistence files might be under a `temp` folder. This can lead to situations when persistence files are removed by an operating system whenever a node process is restarted. To avoid this:

- Ensure that `WARN` logging level is enabled for GridGain. You will see a warning if the persistence files are written to the temporary directory.
- Change the location of all persistence files using the `DataStorageConfiguration` APIs, such as `setStoragePath(...)`, `setWalPath(...)`, and `setWalArchivePath(...)`

## Too Many Thin Clients Connect to Cluster

In some environments, the cluster may encounter a memory issue with an especially large number of clients. For example, if GridGain accepts a lot of client connections and then has to run a memory-intensive operation, the node may run out of memory. To avoid this:

- Track the `client.connector.ActiveSessionsCount` [metric](../reference/monitoring/generic-metrics.md#ignite-thin-client-connector) to make sure you are not getting more connections than necessary.
- Use [Java Metrics](../reference/monitoring/jmx-metrics.md) to keep track of memory usage on the node.
- Increase the amount of direct memory by setting the `MaxDirectMemorySize` JVM parameter. Specific memory requirement heavily depends on the amount of clients and the load performed by them.

If the metrics show that you are running low on memory, use the `maxConnectionCnt` thin client [configuration parameter]({connectors}/thin-clients/java-thin-client) to limit the number of .

## Cluster Does not Start After Field Type Changes

When developing your application, you may need to change the type of a custom
object’s field. For instance, let’s say you have object `A` with field `A.range` of
 `int` type and then you decide to change the type of `A.range` to `long` right in
 the source code. When you do this, the cluster or the application will fail to
 restart because GridGain doesn't support field/column type changes.

You can use the _experimental_ `meta` command to remove metadata that normally stores type affinity from the cluster. If you are not sure what to remove specifically, use the `list` subcommand to list all metadata types. You can specify the type to remove by ID or by name, and also specify the output folder to store a backup in. After you do so, GridGain will treat the column as a new type and continue to operate normally.

{% tabs %}
{% tab title="Unix" %}
```bash
control.sh --meta remove [--typeId <typeId>] [--typeName <typeName>] [--out <fileName>]
```
{% endtab %}

{% tab title="Windows" %}
```bash
control.bat --meta remove [--typeId <typeId>] [--typeName <typeName>] [--out <fileName>]
```
{% endtab %}
{% endtabs %}

The `meta` command is not intended for normal cluster operation and the user is responsible for fulfilling conditions for proper execution:

- Data of the removed type must not be stored in caches;
- No other operations should be performed with the type. For example, you should not delete metadata while creating a new object.

You can also, _in development_, go into the
file system and remove the following directories: `marshaller/`, `db/`, and `wal/`
located in the GridGain working directory (`db` and `wal` might be located in other
places if you have redefined their location). This achieves a similar result to performing a `meta` command, but is less targeted.

_In production_, we still recommend adding a
new field with a different name to your object model and removing the old one. This operation is fully
supported. At the same time, the `ALTER TABLE` command can be used to add new
columns or remove existing ones at run time.

## Saving WAL Data to Disk on Corruption

The normal way to deal with data corruption is to use [maintenance mode](maintenance-mode.md) to resolve the corruption issue and return to normal operation. Sometimes it may lead to data  being lost, for example when the index file is restored to a state not accounting for WAL. You can enable the  `IGNITE_DUMP_PERSISTENCE_FILES_ON_DATA_CORRUPTION` system property to save all stored data to the `{GRIDGAIN_HOME}/db/dump` folder when corruption is detected.

{% hint style="warning" %}
This property will create a copy of all wal files written since the last [checkpoint](../architecture/storage/native-persistence.md#checkpointing) plus related partition files. Make sure you have sufficient space on the drive to create a data dump before enabling the property.
{% endhint %}

## Debugging GC Issues

The section contains information that may be helpful when you need to debug and
troubleshoot issues related to Java heap usage or GC pauses.

### Heap Dumps

You can configure JVM to dump the heap automatically when the `OutOfMemoryException` exception occurs.
This helps if the root cause of this exception is not clear as the dump provides a deeper look at the heap state at the moment of failure:

{% code title="Shell" %}
```bash
-XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath=/path/to/heapdump
-XX:+ExitOnOutOfMemoryError
```
{% endcode %}

### Detailed GC Logs

In order to capture detailed information about GC related activities, make sure you have the settings below configured
in the JVM settings of your cluster nodes:

{% tabs %}
{% tab title="Java 11" %}
```bash
-XX:+ScavengeBeforeFullGC
-XX:+PrintFlagsFinal
-XX:+UnlockDiagnosticVMOptions
-Xlog:gc*,safepoint:/path/to/gc/logs/gc.log:time,uptime,level,tags:filecount=10,filesize=10M
```
{% endtab %}

{% tab title="Java 8" %}
```bash
-XX:+PrintGCDetails
-XX:+PrintGCTimeStamps
-XX:+PrintGCDateStamps
-XX:+UseGCLogFileRotation
-XX:NumberOfGCLogFiles=10
-XX:GCLogFileSize=100M
-Xloggc:/path/to/gc/logs/gc.log
```
{% endtab %}
{% endtabs %}

Replace `/path/to/gc/logs/` with an actual path on your file system.

In addition, for G1 collector set the property below. It provides many additional details that are
purposefully not included in the `-XX:+PrintGCDetails` setting:

{% code title="Shell" %}
```bash
-XX:+PrintAdaptiveSizePolicy
```
{% endcode %}

### Performance Analysis With Flight Recorder

In cases when you need to debug performance or memory issues you can use Java Flight Recorder to continuously
collect low level runtime statistics, enabling after-the-fact incident analysis. To enable Java Flight Recorder use the
following settings:

{% code title="Shell" %}
```bash
-XX:+FlightRecorder
-XX:+UnlockDiagnosticVMOptions
-XX:+DebugNonSafepoints
```
{% endcode %}

To start recording the state on a particular GridGain node use the following command:

{% code title="Shell" %}
```bash
jcmd <PID> JFR.start name=<recording_name> duration=60s filename=/var/recording/recording.jfr settings=profile
```
{% endcode %}

For Flight Recorder related details refer to Oracle's official documentation.

### JVM Pauses

Occasionally you may see an warning message about the JVM being paused for too long. It can happen during bulk loading, for example.

Adjusting the `IGNITE_JVM_PAUSE_DETECTOR_THRESHOLD` timeout setting may give the process time to finish without generating the warning. You can set the threshold via an environment variable, or pass it as a JVM argument (`-DIGNITE_JVM_PAUSE_DETECTOR_THRESHOLD=5000`) or as a parameter to ignite.sh (`-J-DIGNITE_JVM_PAUSE_DETECTOR_THRESHOLD=5000`).

The value is in milliseconds.

### Client Node Fails to Start Before Server Node

When running environments where clusters need to be brought up often, the expected behavior is to start the server node first and then have client nodes connect to it. If done in reverse, it may cause issues as the server is still starting when the client tries to get data from it. You can manually provide a readiness check by creating an AtomicLong data structure on server node after it starts, and checking for it from the client nodes:

Here is an example of server-side code:

```java
...
//loading is complete, create atomic sequence and set its value to 1
ignite.atomicLong("myAtomic", 1, true);
...
```

And the code below allows delays the client initialization until the value is retrieved:

```java
while (true) {
// try get "myAtomic" and check its value
IgniteAtomicLong atomicLong = ignite.atomicLong("myAtomic", 0, false);
if (atomicLong != null && atomicLong.get() == 1) {

        // initialization is complete
        break;
    }

    // not ready
    Thread.sleep(1000);
}
```

### Uneven Data Distribution

The default GridGain [affinity function](../architecture/data-modeling/data-partitioning.md#affinity-function) does not guarantee even data distribution. As a result, sometimes large clusters may encounter uneven data distribution across the nodes. For example, when a node leaves a 20-node cluster, some nodes may receive 10% of total cluster data, while others will not receive any additional data. This may cause performance issues with nodes that suddenly handle more data than expected.

In most cases, this can be remedied by increasing the number of partitions in your cluster. GridGain aims to reduce overhead caused by rebalancing data, so having smaller partitions means that data can be spread more evenly even in these scenarios.

If you are already in a situation of unfavorable data distribution, you can also force GridGain to redistribute data off the node by changing its consistent ID. This will trigger the rebalance process, usually resulting in a more fair distribution.

{% hint style="info" %}
While it is possible to manually modify affinity function to provide more fair results, it is generally not recommended. Minor errors in custom affinity code may cause major issues with cluster stability.
{% endhint %}

## Error When Executing COPY FROM Command

The `COPY FROM` command uses Apache Parquet, which in turn uses Snappy for data compression. Snappy depends on native libraries that are typically extracted and executed from the `/tmp` directory. If the `/tmp` directory is mounted with the `noexec` option, the `COPY FROM` command will fail. Here is how the error may look like:

{% tabs %}
{% tab title="Client" %}
```
Error: /tmp/snappy-1.1.10-b9ba72cc-cb56-4726-b38f-47bc7a207cd1-libsnappyjava.so: /tmp/snappy-1.1.10-b9ba72cc-cb56-4726-b38f-47bc7a207cd1-libsnappyjava.so: failed to map segment from shared object (state=50000,code=1)
```
{% endtab %}

{% tab title="Server" %}
```
java.lang.UnsatisfiedLinkError: /tmp/snappy-1.1.10-b9ba72cc-cb56-4726-b38f-47bc7a207cd1-libsnappyjava.so: /tmp/snappy-1.1.10-b9ba72cc-cb56-4726-b38f-47bc7a207cd1-libsnappyjava.so: failed to map segment from shared object
	at java.base/jdk.internal.loader.NativeLibraries.load(Native Method)
	at java.base/jdk.internal.loader.NativeLibraries$NativeLibraryImpl.open(NativeLibraries.java:388)
	at java.base/jdk.internal.loader.NativeLibraries.loadLibrary(NativeLibraries.java:232)
	at java.base/jdk.internal.loader.NativeLibraries.loadLibrary(NativeLibraries.java:174)
	at java.base/java.lang.ClassLoader.loadLibrary(ClassLoader.java:2394)
```
{% endtab %}
{% endtabs %}

To resolve this issue, first verify the mount options for your `/tmp` directory. Then:

- If possible, remount `/tmp` without the `noexec` option.
- Alternatively, redirect native library extraction by setting the `org.xerial.snappy.tempdir` system property. For example: `-Dorg.xerial.snappy.tempdir=/mystorage/tmp`.

## Restoring Node With Generated Consistent ID

When a node goes down without a manually specified consistent ID and the node needs a restart with cleaned-up persistence folders, you cannot reintroduce it to the cluster without additional actions - the node will be introduced as a new node and require all operations for introducing a new node to the cluster.

{% hint style="info" %}
To avoid this issue, always specify the consistent ID for your nodes.
{% endhint %}

As a workaround, you can reintroduce the new node with the consistent ID of the original node by specifying it manually in the node configuration. You must provide the consistent ID as a `UUID` object, not as a string value. Copy-pasting the UUID as a `consistentId` will not work.

The example below shows the correct way to configure a consistent ID for reintroduction:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="consistentId">
        <bean class="java.util.UUID" factory-method="fromString">
            <!-- Replace with your node's autogenerated consistent ID -->
            <constructor-arg value="6eaafa05-1419-4462-8ed8-dfc85c790d9e"/>
        </bean>
    </property>
</bean>
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
