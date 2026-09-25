---
description: >-
  Basic and advanced performance-tuning practices for GridGain, including
  recommended high-performance settings, JVM options, ulimits, and OS tuning.
---

# Performance and Tuning

GridGain and Ignite as distributed storages and platforms require certain optimization techniques. Before you dive
into the more advanced techniques described in this and other articles, consider the following basic checklist:

- GridGain is designed and optimized for distributed computing scenarios. Deploy and benchmark a multi-node cluster
rather than a single-node one.
- GridGain can scale horizontally and vertically equally well.
Thus, consider allocating all the CPU and RAM resources available on a local machine to a GridGain node.
A single node per physical machine is a recommended configuration.
- In cases where GridGain is deployed in a virtual or cloud environment, it's ideal (but not strictly required) to
pin a GridGain node to a single host. This provides two benefits:
  - Avoids the "noisy neighbor" problem where GridGain VM would compete for the host resources with other applications. This might cause performance spikes on your GridGain cluster.
  - Ensures high-availability. If a host goes down and you have two or more GridGain server node VMs pinned to it, then it can lead to data loss.
- If resources allow, store the entire data set in RAM. Even though GridGain can keep and work with on-disk data, its architecture is memory-first. In other words, _the more data you cache in RAM the faster the performance_.
[Configure and tune](memory-and-jvm-tuning.md) memory appropriately.
- It might seem counter to the bullet point above but it's not enough just to put data in RAM and expect an
order of magnitude performance improvements. Be ready to adjust your data model and existing applications if any.
Use the [affinity colocation](../../architecture/data-modeling/affinity-colocation.md) concept during the data
modelling phase for proper data distribution. For instance, if your data is properly colocated, you can run SQL queries with JOINs at massive scale and expect significant performance benefits.
- If Native persistence is used, then follow these [persistence optimization techniques](persistence-tuning.md).
- If you are going to run SQL with GridGain, then get to know [SQL-related optimizations](sql-tuning.md).
- Adjust [data rebalancing settings](../../architecture/rebalancing/data-rebalancing.md) to ensure that rebalancing completes faster when your cluster topology changes.

## Recommended High Performance Settings

A number of default GridGain configuration properties are preset for better compatibility and ease of access.  However, when GridGain is configured and stable, you can change these properties to increase throughput.

{% hint style="info" %}
While tuning techniques, such as snapshot compression, WAL optimization, etc., will improve your GridGain or Apache Ignite performance or efficiency, you are not likely to see these improvements on small partitions (n x 100 MB). This is due to the overhead that remains the same and overshadows the operational speed/efficiency difference on small entities. We recommend that you test the performance and efficiency changes on larger partitions (n x 10 GB or larger).
{% endhint %}

### System Properties

GridGain has a number of internal properties that can be set to improve performance. A number of system properties can be used to make GridGain run better, or provide more information to handle errors. Below are some of these options:

- If you need additional debug information, disable the `IGNITE_QUIET` value. It enables verbose mode for logs.
- To get more information about mbeans in your project, disable the following property: `IGNITE_MBEAN_APPEND_CLASS_LOADER_ID`. Otherwise, GridGain may miss some mbeans.
- Enable the `IGNITE_BINARY_SORT_OBJECT_FIELDS` property to avoid legacy schema issues when building binary objects.

### TLS Version Configuration

By default, GridGain uses TLS 1.2 to secure connections. You can swap to TLS 1.3 instead by setting it in the properties: `-Djdk.tls.server.protocols=TLSv1.3`.

### Enabling One Way SSL

By default, all connections are secured by a two-way SSL. You can switch to one-way SSL to speed up connections by having the server not verify the client certificate by setting the `-DneedClientAuth=false` property.

### Limiting Number of Active Compute Tasks

Distributed computing can take a significant toll on network configuration. You can limit computing tasks throughput to make sure that all nodes in your cluster have a chance to `-DmaxActiveComputeTasksPerConnection=100`

### Recommended JVM Options

Below is the list of recommended JVM options for high performance GridGain installations:

```
-server -XX:+AggressiveOpts -XX:MaxPermSize=256m \
-DIGNITE_WAIT_FOR_BACKUPS_ON_SHUTDOWN=true \
-DIGNITE_CLUSTER_ID={{ ignite_cluster_id }} \
-DCODE_DEPLOYMENT={{ code_deployment_enabled }} \
-Djava.net.preferIPv4Stack=true -Dlog4j2.formatMsgNoLookups=true \
-Dcom.sun.management.jmxremote=true \
-Dcom.sun.management.jmxremote.port=9010 \
-Dcom.sun.management.jmxremote.local.only=false \
-Dcom.sun.management.jmxremote.authenticate=true \
-Dcom.sun.management.jmxremote.ssl=true \
-Djava.rmi.server.hostname={{ ansible_ec2_public_ipv4 }} \
-Djavax.net.ssl.keyStore={{ gridgain_ssl_path }}/server.p12 \
-Djavax.net.ssl.keyStorePassword={password} \
-DIGNITE_MBEAN_APPEND_CLASS_LOADER_ID=false
-DIGNITE_DISABLE_WAL_DURING_REBALANCING=true \
-DIGNITE_PDS_WAL_REBALANCE_THRESHOLD=1 \
-DIGNITE_WAL_MMAP=false \
-DIGNITE_BINARY_SORT_OBJECT_FIELDS=true \
-XX:StartFlightRecording=dumponexit=true,filename={{ gridgain_logs_path }}/gridgain.jfr,maxsize=1g,maxage=1h,settings=profile
-XX:+ScavengeBeforeFullGC \
-Xlog:gc:{{ gridgain_logs_path }}/gc.log \
-XX:+PrintGC -XX:+PrintGCDetails \
-XX:+PrintFlagsFinal \
-XX:+UnlockDiagnosticVMOptions \
-XX:LogFile={{ gridgain_logs_path }}/safepoint.log \
-XX:+PrintSafepointStatistics \
-XX:PrintSafepointStatisticsCount=1
```

### Additional Snapshot Options

Snapshot operations require a significant amount of resources and may cause slowdown is service. You can configure extra snapshot options to offset possible issues by reducing (or increasing) parallelism in [GridGain parameters](../../gridgain8-usage/understanding-configuration.md), or by introducing throttling:

- Set the level of parallelism for snapshot operations with the following option:
`gg_snapshot_operation_parallelism: "4"`.
- Configure snapshot throttling time in milliseconds with the following option:  `gg_snapshot_progress_throttling: "-1"`.

### Write Ahead Log Options

A number of WAL options can be added to make your WAL more reliable and compact. You can set them in [GridGain parameters](../../gridgain8-usage/understanding-configuration.md).

- Set wal mode to log only `gridgain_wal_mode: "LOG_ONLY"`.
- Increase the segment size `gridgain_wal_segment_size: "#{256 * 1024 * 1024}"`.
- Enable WAL compaction `gridgain_wal_compaction_enabled: "true"`.
- Set a WAL compaction level `gridgain_wal_compaction_level: "1"`.
- Set a archive size to. We recommend setting just under 30GB by using the `gridgain_wal_archive_size: "29000000000"` property.

### Ulimits

You can configure user limits for GridGain in the `/etc/security/limits.conf` file. In it, you set the limits for each user in the following format:

```
<domain> <type> <item> <value>
```

For GridGain, you can set both soft and hard limit `types` on the maximum number of open file descriptors (`nofile`) and maximum number of processes (`nproc`). The recommended values for environments of 50 caches or less are:

```
gridgain - nofile 65536
gridgain - nproc 65536
```

If the system-wide number of file descriptors is low, setting the `nofile` limit to a high value will not eliminate the "Too many open files" error. You can resolve this issue by modifying `/proc/sys/fs/file-max`.

If your environment is more complex, consider optimization of the ulimit file value. You can estimate the value that would work best in your environment using the following empiric formula:

files_ulimit =

[partitions_in_partitioned_caches * (backups + 1) * partitioned_caches](../../gridgain8-usage/configuring-caches/configuring-backups.md) / nodes +
[partitions_in_replicated_caches * replicated_caches](../../gridgain8-usage/configuring-caches/configuration-overview.md) +
[num_of_clients](../../gridgain8-get-started/concepts.md#clustering-servers-and-clients) +
[num_of_servers](../../gridgain8-get-started/concepts.md#clustering-servers-and-clients)

where:

- partitions_in_partitioned_caches - typically, 1024 (unless you have explicitly [changed it](https://www.gridgain.com/sdk/latest/javadoc/org/apache/ignite/cache/affinity/rendezvous/RendezvousAffinityFunction.html#setPartitions-int-))
- partitions_in_replicated_caches - typically, 512 (unless you have explicitly [changed it](https://www.gridgain.com/sdk/latest/javadoc/org/apache/ignite/cache/affinity/rendezvous/RendezvousAffinityFunction.html#setPartitions-int-))
- num_of_clients - a total of [thick and thin clients](../../gridgain8-get-started/concepts.md#thick-vs.-thin-clients)

{% hint style="info" %}
The `limits.conf` file is ignored if GridGain is run as a systemctl service. In this case, configure user limits in the `/etc/systemd/system/gridgain.service` file:

```
[Service]
LimitNOFILE=65536
LimitNPROC=65536
```
{% endhint %}

{% hint style="info" %}
Sometimes, even the values as high as `65536` aren't enough, especially if you have a lot of caches. Consider using cache groups.
{% endhint %}

### Linux Kernel Panic Delay

In case of kernel panic, GridGain needs some time to create data dumps. It is recommended to set the `kernel.panic` parameter to 3. You can set Linux kernel properties in the `/etc/sysctl.conf` file.

### Utilizing Linux Virtual Memory

Linux leaves space for an in-memory cache to handle I/O operations. You can manually configure them to provide more performance and better safety for larger operations. To configure the parameters below, set them in the `/etc/sysctl.conf` file and execute the `sudo sysctl –p` command, or run the `sysctl -w` command.

```
vm.dirty_background_ratio = 1
vm.dirty_ratio = 20
vm.dirty_expire_centisecs =	500
vm.dirty_writeback_centisecs = 100
vm.overcommit_memory = 2
vm.overcommit_ratio = 100
vm.swappiness = 0
```

Below is the expanded information on these parameters:

- The `vm.dirty_background_ratio` parameter sets how much of memory can be occupied by "dirty" pages after which they will be flushed to disk. Having too many dirty pages in memory can be detrimental to performance, so it is recommended to have a low percentage.
- The `vm.dirty_ratio` parameter sets the percent of memory occupied by dirty pages. If too many pages are dirty, they will be flushed to disk. Setting it low keeps the memory clean.
- The `vm.dirty_expire_centisecs` parameter sets how long dirty pages can be stored in memory. We recommend doing this every 5 seconds.
- The `vm.dirty_writeback_centisecs` parameter configures how often the system checks if any data needs to be flushed to the disk. It is recommended to keep checking it every 1 second.
- The `vm.overcommit_memory` parameter sets if applications can commit more data to memory than there is available space. Set to 2 to never overcommit.
- The `vm.overcommit_ratio` sets how much space is kept for overcommit, in percent. Set it to 100 to never commit more to memory than you have space available.
- The `vm.swappiness` parameter configures if swap will be used. We recommend disabling it to avoid it interfering with persistence.

### Read-Only For Clusters

Sometimes, you may need to keep your cluster from receiving any new data. For example, you may need this to lock a cluster in a certain date for the duration of maintenance, when a cluster restart is unadvisable, or to create a backup cluster in a read only state.

You can set your cluster to read only state from the control script by using the `--set-state ACTIVE_READ_ONLY` command.

You can also set the `clusterStateOnStart` cluster property to `ACTIVE_READ_ONLY` to have your cluster start in a read-only mode.

If a write attempt is performed on the cluster currently in read only state, it returns a `IgniteClusterReadOnlyException` exception.

### Fine-Tuning Message Queue

GridGain nodes constantly communicate with each other in the cluster. The messages sent to a different node in the cluster are stored in the special queue on the sender node until the acknowledgement is received, after which the messages are deleted and the memory is freed. To reduce network load, GridGain nodes confirm messages in batches instead on acknowledging individual messages. The acknowledgement is sent by the receiver node:

- Upon reaching `ackSendThresholdMillis` (1000 ms by default) limit since the last acknowledgement, or
- Upon reaching `ackSendThresholdBytes` (1 Mb by default) limit of unconfirmed messages that are stored on the sender node.

Additionally, the maximum queue size on the sender node is determined by the `messageQueueLimit` (4096 messages by default).

In most scenarios, this default configuration works well for the cluster. For fine-tuning your cluster performance, keep the following in mind:

- Upon reaching `messageQueueLimit` messages in the queue, the connection will be forcibly closed by the sender node, all messages in the queue will be discarded and the queue will be deleted. This may lead to loss of data if the receiver node did not receive some of the messages.
- The `ackSendThresholdMillis` and `ackSendThresholdBytes` limits do not lead to the connection being closed, these properties only control when acknowledgement is sent.
- Unstable cluster may cause additional complications in sending acknowledgements, potentially leading to queue being filled up despite thresholds being properly configured. Fine-tuning the environment works best when connection between nodes is stable.

As such, here are general recommendations depending on your environment:

- In most environments, default values are sufficient for normal performance.
- In environments with high volumes of small messages the queue may get filled up before either acknowledgement threshold is reached and the connection is reset. In these environments, you may want to increase the limit to allow more messages to be processed before the `ackSendThresholdMillis` is triggered, or reduce the same threshold to send acknowledgements more often.
- In environments with low to moderate volumes of large messages you may want to lower queue limit to reduce memory use. Make sure to fine-tune the `ackSendThresholdBytes` to send acknowledgements more often so that the queue does not fill up.
- In environments with both high volume of messages and large messages, you may want to reduce both thresholds to reduce the amount of memory required to store messages in the queue at the cost of more acknowledgements being sent. In these environments, increasing the queue limit may lead to it requiring a lot of memory to store messages, and it is better to keep the queue low by other means.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
