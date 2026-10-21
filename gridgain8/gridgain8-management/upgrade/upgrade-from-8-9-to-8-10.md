---
description: >-
  What to change or check when upgrading a GridGain 8.9.x cluster or application to 8.10: Java 17, removed modules, new defaults, license and permission changes, and tested upgrade and rollback steps.
---

# Upgrading from GridGain 8.9 to 8.10

GridGain 8.10 raises the Java baseline to Java 17, removes several modules and integrations, moves the Spring, Hibernate, Lucene, Cassandra, and Jetty dependencies to current versions, and changes a small number of defaults. This guide lists everything that you must change, or must be aware of, when you move a cluster or an application from GridGain 8.9.x to GridGain 8.10.

If you are migrating from Apache Ignite 2.x, see [Migrating from Apache Ignite 2](../migration-guides/apache-ignite-2x/README.md) instead.

<!-- TODO RE/SE: the procedure in "Upgrade Procedure" was run on a real 3-node persistent cluster twice (8.9.38 -> 8.10.127-SNAPSHOT master build): once on JDK 21, once with 8.9.38 on Java 11 and 8.10 on Java 17. Both worked. Prerequisite found by testing: the 8.9 cluster needs rollingUpdatesEnabled=true on ALL nodes, which needs one full cluster restart if it is not set. The official support statement for 8.9 -> 8.10 is not recorded. Confirm it before publishing. Also tested: Java 8 (with ignite-lucene-8) and Java 17 on 8.9.38, upgraded to 8.10 on Java 17; 1M and 2M rows with client load; revert before and after finish. Not tested: a multi-host cluster, other client types under load. -->

## Upgrade Checklist

Go through the table before you upgrade. Each row links to the section with the details.

| Area | Check | Section |
| --- | --- | --- |
| Java | Every server node, client application, and application that embeds GridGain runs on Java 17 or later. | [Platform Requirements](#platform-requirements) |
| Modules | Your `libs` folder, your `pom.xml` or Gradle files, and your Spring XML do not use a removed module. If you start remote nodes with `startNodes()`, you contacted GridGain Support about the removed `ignite-ssh` module. | [Removed Modules and Integrations](#removed-modules-and-integrations) |
| Spring and Hibernate | Applications that embed GridGain through Spring use Spring 7. Hibernate second-level cache users use Hibernate 7.4. | [Spring 7 Only](#spring-7-only), [Hibernate 7 Only](#hibernate-7-only) |
| REST | A custom `jetty.xml` is rewritten for Jetty 12. Scan queries with a filter class are allow-listed. | [Jetty 12 Is the Only REST Implementation](#jetty-12-is-the-only-rest-implementation), [REST Scan Queries With a Filter Class](#rest-scan-queries-with-a-filter-class) |
| Lucene | If you run `ignite-lucene-8`, you moved to `ignite-lucene-9` before the upgrade. If you plan to use Lucene 10, you switch every node to it after the upgrade. | [Lucene](#lucene) |
| Packaging | Modules that you copy from `libs/optional` or `integration` are still where you expect them. | [Distribution and Packaging Changes](#distribution-and-packaging-changes) |
| Thin client | Operations that run longer than 60 seconds are still expected to work. | [Java Thin Client Timeouts Have Default Values](#java-thin-client-timeouts-have-default-values) |
| Upgrade readiness | Every 8.9 node has `rollingUpdatesEnabled=true`, GridGain snapshots are configured, a full snapshot exists, and caches that must stay available have at least one backup. | [Upgrade Procedure](#upgrade-procedure) |
| Snapshots | SFTP snapshot destinations have a known hosts file. | [SFTP Snapshot Transport Verifies the Host Key by Default](#sftp-snapshot-transport-verifies-the-host-key-by-default) |
| SQL `COPY` | Roles that run server-side `COPY` have the new permissions, and `COPY` against files or object stores is enabled. | [Server-Side SQL COPY](#server-side-sql-copy) |
| License | The license enables every feature your configuration uses. | [Per-Feature License Checks](#per-feature-license-checks) |

## Upgrade Procedure

You can upgrade a cluster from 8.9.x to 8.10 without downtime by using [Rolling Upgrades](rolling-upgrades.md), a GridGain Enterprise and Ultimate feature. If you do not use Rolling Upgrades, you can upgrade offline: see [Upgrade Without Rolling Upgrades](#upgrade-without-rolling-upgrades).

Before you start, complete the [checklist](#upgrade-checklist) and install Java 17 or later on every server host. You can keep running the 8.9 nodes on their current Java version. The upgrade was tested from Java 8, 11, 17, and 21 on 8.9 to Java 17 (and 21) on 8.10. Each node switches to Java 17 when you restart it from the 8.10 distribution, so set `JAVA_HOME` for the 8.10 scripts before you start the node.

Unpack the 8.10 distribution next to the 8.9 one. Do not copy the `libs` folder of 8.9 into it. Compare the content of the two `libs` and `libs/optional` folders and copy only the modules that you use and that still exist in 8.10 (see [Removed Modules and Integrations](#removed-modules-and-integrations) and [Distribution and Packaging Changes](#distribution-and-packaging-changes)). A module that you enabled in 8.9 by moving it into `libs`, for example `control-center-agent`, `ignite-opencensus`, or `ignite-spring-6`, is not enabled in 8.10 until you do the same there, if the module still exists.

The procedure has three parts: configure Rolling Upgrades and snapshots on the 8.9 cluster and take a snapshot (steps 1 to 3), upgrade the nodes one at a time (steps 4 to 7), and check the result (step 8).

If your 8.9 cluster runs on Java 8 with the `ignite-lucene-8` module and uses full-text indexes, no extra step is needed in the procedure. Full-text queries returned the same results before, during, and after the upgrade in the test. Do not copy `ignite-lucene-8` to the 8.10 distribution, because the module is removed (see [Lucene](#lucene)).

1. Add Rolling Upgrades and GridGain snapshots to the configuration of the 8.9 cluster. Every 8.9 node must have the following in its `GridGainConfiguration` *before* the upgrade. Replace the license path and the snapshot folder with your own, and skip the properties that you already have:

   ```xml
   <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
       <property name="licenseUrl" value="file:///path/to/gridgain-license.xml"/>
       <property name="rollingUpdatesEnabled" value="true"/>
       <property name="snapshotConfiguration">
           <bean class="org.gridgain.grid.configuration.SnapshotConfiguration">
               <property name="snapshotsPath" value="/data/snapshots/node1"/>
           </bean>
       </property>
   </bean>
   ```

   `GridGainConfiguration` is an element of `IgniteConfiguration.pluginConfigurations`. Store the snapshots outside of the work directory, so that you can keep them when you remove the data. On one host, all nodes can use the same `snapshotsPath`, because each snapshot gets a subfolder for every node. In the test, 3 nodes on one host worked both with a shared folder and with one folder per node. Nodes on different hosts were not tested.

   If `rollingUpdatesEnabled` is not set, `control.sh --rolling-upgrade start` fails with the message `Rolling Upgrade mode cannot be enabled. Consider changing 'GridGainConfiguration.rollingUpdatesEnabled' configuration property.` If `snapshotConfiguration` is not set, `snapshot-utility.sh` fails with `GridGain snapshots are not configured` (error 4400).

2. Restart the cluster so that the new configuration takes effect. You cannot add `rollingUpdatesEnabled` one node at a time. A node with `rollingUpdatesEnabled=true` is not allowed to join a cluster whose nodes do not have it, even if all nodes run the same version, and fails to start with `Rolling updates are not properly configured`. If the property is not set yet, stop the whole cluster, add both properties to the configuration of every node, and start the cluster again. This is a planned downtime. With native persistence, the data and the baseline are kept. If you have to stop the whole cluster anyway, you can upgrade offline in the same window, see [Upgrade Without Rolling Upgrades](#upgrade-without-rolling-upgrades).

3. When the cluster is running with the new configuration, take a full snapshot on 8.9 with `snapshot-utility.sh snapshot -type=full`. See the note after the procedure for what the snapshot is good for.
4. If you use native persistence, make sure the new version uses the same data. Each node must keep its consistent ID and the same `storagePath`, `walPath`, and `walArchivePath`. If you do not set these properties, the default location is the `work` folder, and the `work` folder of a new distribution is empty. Point the new node at the old one by setting the `IGNITE_WORK_DIR` environment variable or the paths in the configuration.
5. Start the rolling upgrade:

   ```shell
   control.sh --rolling-upgrade start --yes
   ```

   Without the `--yes` option, the command asks for confirmation. When you run it from a script, always pass `--yes`.

   Setting `rollingUpdatesEnabled` is not enough on its own. The status stays `disabled` until you run this command.

   All `control.sh --rolling-upgrade` commands exit with code 0 also when they fail (for example when `start` or `finish` is refused), so check the message and not the exit code. Use the `control.sh` of the 8.10 distribution for the `--rolling-upgrade` commands from the first upgraded node on. In the test, the `control.sh` of 8.9 also worked in the mixed cluster.
6. For each node, one at a time. The order does not matter: in the test, the coordinator was upgraded first in one run and a node that was not the coordinator in another, and both worked.
   1. Stop the node and wait until its process has exited. In the test, nodes were stopped with SIGTERM (`kill <pid>`).
   2. Start the node from the 8.10 distribution with the same configuration, work directory, and consistent ID.
   3. Wait until the node has joined and rebalancing has finished. Look in the log of the new node for the `Finish exchange future` message and then for either `Completed (final) rebalancing` (data moved to the node) or `Skipping rebalancing (nothing scheduled)` (no data changed while the node was down, which is typical when the node was stopped for seconds). Do not stop the next node before you see one of them.
   4. Run `control.sh --rolling-upgrade status` and check that the node is listed under the updated nodes. The status lists the first 8 characters of the node ID, not the consistent ID, and a restarted node gets a new ID. Take the new ID from the node log: the line `Local node [ID=...]` in the startup banner, or `locNode=...` in the `Topology snapshot` line. For example, a node that was `62bb02f6` before the restart can be `ece6ab0b` after it.

   The new node writes a warning to its log that the build versions differ, but that they are compatible. This is expected.

   {% hint style="warning" %}
   `control.sh` connects to the first node on port 11211 by default. During a rolling upgrade, that node can be the one you stopped, and the command fails with `Connection to cluster failed`. Use the `--host` and `--port` options to connect to a node that is running. The port is the one of the REST connector (11211 and above), not the thin client port.
   {% endhint %}
7. When the status shows `none` under the nodes that are not updated, finish the rolling upgrade:

   ```shell
   control.sh --rolling-upgrade finish --yes
   ```

   If you run `finish` while an 8.9 node is still in the cluster, it is refused with `Rolling Upgrade mode cannot be disabled` and lists the nodes of each version. The exit code is 0 in this case too.

   After a successful `finish`, the initial version in the status output is `8.10`, and new 8.10 features become available.
8. Check the cluster: run `control.sh --baseline`, and run a query from a client to check that the data is intact. If you have caches without backups, look for `Detected lost partitions` in the node logs and reset them as described in [What Your Applications See During the Upgrade](#what-your-applications-see-during-the-upgrade). You can reset them once, after the last node is back.

If authentication is enabled, pass the credentials to every command: `control.sh --user <user> --password <password> ...` and `snapshot-utility.sh ... -user=<user> -password=<password>`. In the test, a configuration with native authentication, SSL for discovery, communication, and the thin client and JDBC port, a user created with SQL, and explicit `storagePath`, `walPath`, and `walArchivePath` settings started on 8.10 unchanged, so no configuration edits were needed for the upgrade itself.

While the upgrade is in progress, the cluster stays available. An 8.10 node that tries to join a cluster where Rolling Upgrades are not started is rejected with the message `The node has been rejected due to disabled Rolling Upgrade`.

{% hint style="info" %}
The full snapshot that you take in step 3 is your way back after `finish`. A snapshot that 8.9.38 created can be listed, checked, and restored with the 8.10 `snapshot-utility.sh` after the upgrade. In the test, `restore` on 8.10 brought the data back to the state of the snapshot. The same holds for incremental snapshots (`snapshot-utility.sh snapshot -type=inc`): a full snapshot and an incremental snapshot taken on 8.9 were listed by the 8.10 utility, and `restore -id=<incremental snapshot id>` on 8.10 returned the data to the state of the incremental snapshot (2,000 of 2,500 rows). A new incremental snapshot taken on 8.10 on top of the 8.9 full snapshot was created and listed.
{% endhint %}

{% hint style="warning" %}
Do not leave the cluster with mixed versions for long. See [Rolling Upgrades](rolling-upgrades.md) for the performance considerations.
{% endhint %}

<!-- TODO RE/SE: (1) is there a cluster-level way to see that rebalancing has finished (a control.sh command or a metric)? Step 6.3 relies on the node log only. (2) May nodes on different hosts share one snapshotsPath? On one host a shared folder worked (one subfolder per node in each snapshot); several hosts were not tested. -->
<!-- CHECK: not tested for snapshots: a snapshot restored into a different cluster or topology, point-in-time recovery, remote (SFTP) snapshot locations; the new incremental created on 8.10 was not restored. -->

### What Your Applications See During the Upgrade

In the test, a client under load ran during the whole upgrade: 4 JDBC threads (reads, updates, and inserts) and one Java thin client thread, built with the 8.9 libraries and not upgraded, against 1,000,000 rows and caches with one backup. About 5 million operations ran in about 7 minutes. The application saw 8 errors, all `Failed to handle JDBC request because node is stopping`, in the first seconds after a node was stopped, on JDBC connections that were open on that node. Every acknowledged insert was present after the upgrade, and no read returned a wrong value. The Java thin client reconnected and retried by itself and reported no error. A run with 2,000,000 rows (about 1.6 GB per node on disk) behaved the same way.

Keep the following in mind:

* An application must reconnect and repeat the failed operation. A JDBC connection that was open on a stopped node fails, and you must open a new one. Give the driver or the client more than one address (for example `jdbc:ignite:thin://host1:10800,host2:10800,host3:10800`), so that a new connection does not go to the node that is down.
* A cache with no backups (`backups=0`, the default) is not available for the partitions that live on the stopped node. In the test, operations on such a cache failed with `CacheInvalidStateException`, and the errors did not stop when the node returned. The message depends on the API: cache operations report `Failed to execute the cache operation (all partition owners have left the grid, partition data has been lost)`, and SQL queries report `Failed to execute query because cache partition has been lost [cacheName=SQL_PUBLIC_NB, part=0]`. This is not specific to the upgrade, it happens at every node restart, also between 8.9 nodes. The log of the nodes shows which cache is affected: `WARNING ... Detected lost partitions [grp=SQL_PUBLIC_NB, parts=[...]]`. Configure at least one backup for the caches that must stay available, or plan a maintenance window for the others. With native persistence the data is not lost: after the node is back, run `control.sh --cache reset_lost_partitions <cache name>` (or `--all`) and the cache works again. The cache of an SQL table is named `SQL_<SCHEMA>_<TABLE>`, for example `SQL_PUBLIC_NB` for the table `NB` in the `PUBLIC` schema, unless you set `CACHE_NAME` when you created the table. In the test, all 3,000 rows of such a table were there after the reset.
* The log of a node can contain `SEVERE ... Failed to send message to remote node ... Failed to send message (node left topology)` while another node is stopped under load. The message appears between 8.9 nodes as well and is not caused by the new version.
* Time per node on the test machine (3 nodes on one laptop): stop 1 to 24 seconds, the node joins within 5 to 50 seconds, and rebalancing finishes about a minute later. Only the data that changed while the node was down is moved. Expect more on real hardware and data sizes.

<!-- CHECK: the comma-separated JDBC host list was run once after the upgrade, with the first address unreachable, and the query succeeded; it was not run under load during the upgrade (the load test used the port range form). Not tested: .NET and C++ clients, a client built with the 8.10 libraries during the mixed phase under load, SQL queries that run longer than the stop of a node, transactions in flight, continuous queries, compute jobs, a cluster of several hosts. -->

### Roll Back an Upgrade

Whether you can go back depends on the moment.

**Before `finish`.** You can move the nodes that you already upgraded back to 8.9. For each of them, stop the node and start it again from the 8.9 distribution with the same configuration, work directory, consistent ID, and Java version. In the test, two of three nodes were on 8.10 and data was written through them. In a second test, a table, a column, and an index were also created through the 8.10 nodes, and one node was kept down for 30 seconds under load. When it started on 8.9, it rebalanced about 394,000 entries (84 MB) from the 8.10 nodes, and the new table and column were visible. After both nodes were back on 8.9 and `finish` was run, every acknowledged write (1.15 million inserts) was present, with 16 short `node is stopping` errors for the four node stops in the test. Both nodes started on 8.9 with the same data, joined with the warning about different build versions, and the cluster kept working. The row count of the main table did not change. The status still shows the target version 8.10 and lists all nodes as not updated. Run `control.sh --rolling-upgrade finish --yes` to leave the rolling upgrade mode. The initial version stays 8.9.38.

**After `finish`.** An 8.9 node cannot join the cluster any more. It fails to start with `The node has been rejected due to disabled Rolling Upgrade`, because the cluster is now 8.10 and the rolling upgrade is not active. The way back is to restore the snapshot that you took before the upgrade:

1. Stop all nodes.
2. Remove the data of the nodes (the `db` folder in the work directory, or your `storagePath`, `walPath`, and `walArchivePath`). Keep the snapshot folder.
3. Start the nodes from the 8.9 distribution and activate the cluster.
4. Restore the snapshot with the 8.9 `snapshot-utility.sh restore -id=<snapshot id>`.

In the test, the restore on an empty 8.9 cluster finished in 21 seconds with `Restored: true`, and the data was in the state of the snapshot (200,000 rows, same checksum). Everything written after the snapshot is lost. Restore into a cluster with the same topology as the one that took the snapshot. A snapshot of 3 nodes restored into a cluster of 2 nodes is refused with `snapshot is broken ... Not enough partitions in current topology to complete restore operation` (error 5510), and nothing is restored.

{% hint style="warning" %}
Do not start 8.9 nodes on data that 8.10 nodes have written and treat it as a rollback. In the test, 8.9 nodes started on such data after `finish` and the cluster worked: 200,000 new rows in a new table with an index, columns added and dropped, and a short write load were all there, and `idle_verify` found no conflicts. It is still not a supported way back, and data written by 8.10 can use formats that 8.9 does not read.
{% endhint %}

<!-- TODO RE/SE: confirm that starting 8.9 on data written by 8.10 is not supported, and whether there is a supported downgrade path other than a snapshot. The test only shows that it started and read the data after light updates. Not tested: PITR, revert with several GB to rebalance, revert with transactions in flight. -->

### Upgrade Without Rolling Upgrades

If you can stop the cluster, you do not need `rollingUpdatesEnabled` and you do not need `control.sh --rolling-upgrade`:

1. Take a full snapshot (see the note after the [procedure](#upgrade-procedure)) and stop all nodes.
2. Install the 8.10 distribution and Java 17 or later. Do not copy the old `libs` folder, and review the [removed modules](#removed-modules-and-integrations).
3. Start all nodes from the 8.10 distribution with the same configuration, work directory, and consistent IDs.

In the test, a 3-node cluster with native persistence and no `rollingUpdatesEnabled` in the configuration (and one with the property) was stopped on 8.9.38 and started on 8.10. The cluster became active with the old baseline, all data and a table created shortly before the stop were there, and `idle_verify` found no conflicts. No other action was needed.

Another way is to start an empty 8.10 cluster with the same number of nodes and restore the 8.9 snapshot into it with the 8.10 `snapshot-utility.sh restore -id=<snapshot id>`. In the test, this restored an 8.9.38 snapshot of 3 nodes (300,000 rows, 3 tables) on a fresh 8.10 cluster in 26 seconds, with the data equal to the state of the snapshot. Use it when you want to move to new hosts or keep the old cluster untouched.

<!-- CHECK: not tested: stop-all upgrade with a large data set, an offline upgrade from Java 8. -->

## Platform Requirements

### Java 17 or Later

GridGain 8.10 requires Java 17 or later and supports Java 17, 21, and 25. GridGain 8.9.x supported Java 8, 11, 17, and (starting with 8.9.10) 21. On Java 8, full text search and vector search were not available, and Lucene 9 required replacing `libs/ignite-lucene-9` with `libs/optional/ignite-lucene-8` (see [Lucene](#lucene)). Every artifact is compiled to Java 17 bytecode, so the requirement applies to servers, thick clients, applications that embed a node, the Java thin client, and the JDBC thin driver.

* `ignite.sh`, `ignite.bat`, `control.sh`, and `control.bat` refuse to start on a JVM older than 17.
* The .NET client in thick mode starts a JVM and fails if `JAVA_HOME` points at an older JDK. The .NET thin client, the C++ client, and the ODBC driver do not use a JVM.
* An application that embeds the Control Center agent also needs Java 17.

Upgrade the JVM on every node and every application before you upgrade GridGain.

<!-- CHECK: the per-component enforcement list is from the 8.10.0-b1 release notes. Verified in source: compiler target 17 in parent/pom.xml, and build.sh refuses a JDK older than 17. The scripts' version check was not re-read. -->

## Removed Modules and Integrations

The following modules are removed in GridGain 8.10. If your application or configuration uses one of them, take the action in the last column, or stay on GridGain 8.9.x.

| Removed | What to use instead | Deprecated in 8.9.x |
| --- | --- | --- |
| `ignite-hibernate-4.2`, `ignite-hibernate-5.1`, `ignite-hibernate-5.3`, `ignite-hibernate-core` | `ignite-hibernate-7.4`. See [Hibernate 7 Only](#hibernate-7-only). | 8.9.35 |
| `ignite-spring-6` | `ignite-spring` on Spring 7. See [Spring 7 Only](#spring-7-only). | Not deprecated |
| `ignite-lucene-8` | `ignite-lucene-9`, or the Lucene 10 line in `libs/optional`. See [Lucene](#lucene). | Not deprecated |
| `ignite-aop` and the Gridify API in `ignite-core` | The [compute API](../../gridgain8-development/distributed-computing/distributed-computing.md). | 8.9.37 |
| `ignite-cloud` (`TcpDiscoveryCloudIpFinder`) | Another [IP finder](../clustering/discovery-in-the-cloud.md). | 8.9.37 |
| `ignite-ssh` | Contact GridGain Support if you use `IgniteCluster.startNodes()`. See [SSH Module Removed](#ssh-module-removed). | Not deprecated |
| `ignite-aws` (S3 checkpoint SPI, S3, ELB, and ALB IP finders, S3 IP finder encryption) | The Apache Ignite `ignite-aws-ext` extension. See [AWS Module Removed](#aws-module-removed). | 8.9.39 |
| `ignite-mesos` | None. Mesos deployments stay on 8.9.x. | 8.9.39 |
| `ignite-web` (Web Session Clustering: `WebSessionFilter`, `ServletStartup`, `ServletContextListenerStartup`) | None. Applications that cluster HTTP sessions through GridGain stay on 8.9.x. | Not deprecated |
| `ignite-ml`, `ignite-ml-spark-model-parser`, `ignite-ml-xgboost-model-parser`, `ignite-ml-mleap-model-parser` | The Apache Ignite `ignite-ml-ext` extension or the standalone GridGain ML download. See [Machine Learning Module Removed](#machine-learning-module-removed). | 8.9.38 |
| `gridgain-diagnostic`, `gridgain-tools`, `gridgain-yardstick` (Enterprise and Ultimate) | None. | Not deprecated |
| Local store support (`@CacheLocalStore`, `CacheFileLocalStore`) | Native persistence or a regular `CacheStore`. See [Local Store Support Removed](#local-store-support-removed). | `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` and `CacheFileLocalStore` in 8.9.39 |

The following modules are not removed in 8.10 and still ship in `libs/optional`: `ignite-cassandra-store`, `ignite-cassandra-serializers`, `ignite-kubernetes`, `ignite-zookeeper`, `ignite-gce`, `ignite-jta`, `ignite-yarn`, `ignite-compress`, and `ignite-direct-io`.

<!-- CHECK: the 8.9.x deprecation versions for Hibernate (8.9.35), Gridify (8.9.37) and ignite-cloud (8.9.37) come from the Confluence page. Verified in origin/8.9-master: GG-51560 (ignite-aws), GG-51574 (Mesos), GG-52246 (local store) are merged for 8.9.39. The 8.10.0-b2 release notes say Mesos was "Not deprecated in the 8.9.x"; that line needs to be corrected. -->
<!-- CHECK: gridgain-diagnostic/-tools/-yardstick removal verified (no such modules in ggprivate master). -->
<!-- CHECK: ignite-web is NOT removed in source yet. On origin/master e85742c4003, modules/web (artifactId ignite-web) is still in the root pom.xml and assembly/libs/README.txt:86 lists it. The removal ticket is GG-51845 (In Progress, master-next, no PR or branch yet). Its Definition of Done needs Support/Product sign-off that no customer uses it and a deprecation cycle before removal. The row stays because the removal is expected before this guide is published; confirm that it happened, and take the row out if it did not. Conflicting signals: GG-52208 (Open) is a customer request (EU Commission) for ignite-web on WebLogic 15, and it says the module was "marked for removal in 8.10 and deprecation in 8.9". In origin/8.9-master, WebSessionFilter and ServletStartup have no @Deprecated and the module README has no deprecation note, which matches the "Not deprecated" column. -->


### Hibernate 7 Only

The Hibernate second-level cache module targets Hibernate 7.4 and is named `ignite-hibernate-7.4`. Applications on Hibernate 4.2, 5.1, or 5.3 must move to Hibernate 7.4 or stay on GridGain 8.9.x.

### Spring 7 Only

GridGain 8.10 builds against Spring Framework 7.0.9 and Spring Data 4.1.0. The `ignite-spring` and `ignite-spring-data` modules are compiled to Java 17 bytecode and target Spring 7. Spring 5 and Spring 6 are no longer supported, and `ignite-spring-6` is removed.

An application that embeds GridGain through Spring must be on Spring 7. Otherwise, stay on GridGain 8.9.x, which keeps the Spring 5 and Spring 6 modules.

The Control Center agent also runs on Spring 7 (7.0.9) and Tyrus 2. An agent embedded in an application on Spring 5 or Spring 6 does not start. Upgrade the host application or keep using the 8.9.x agent.

#### Spring Data Module Renamed

The `ignite-spring-data_2.2` module is renamed to `ignite-spring-data`, and its package changes from `org.apache.ignite.springdata22` to `org.apache.ignite.springdata`.

1. Change the artifact ID in your build files from `ignite-spring-data_2.2` to `ignite-spring-data`.
2. Update the imports of `IgniteRepository`, `@EnableIgniteRepositories`, `@RepositoryConfig`, `@Query`, and the other classes of the module.

### Lucene

The `ignite-lucene-8` module is removed. If you still run it (the Java 8 workaround documented for GridGain 8.9.18 and later put it in `libs`), move to the Lucene 9 line before you upgrade.

The 8.10 package ships two Lucene lines. The Lucene 9 line (Lucene 9.10.0) is active by default, and the Lucene 10 line (Lucene 10.4.0) is in `libs/optional`, where it stays inactive until you move it. There is no separate Lucene 10 download. If you upgrade without changing anything, the node behaves as it did on 8.9: `ignite-lucene-9` is in `libs` and serves full-text and vector search.

| Folder in `libs/optional` | Requires | Editions |
| --- | --- | --- |
| `ignite-lucene-10` | JDK 21 or later | Community, Enterprise, Ultimate |
| `ignite-lucene-10-java22` | JDK 22 or later. Adds an opt-in scorer that reads vectors from off-heap memory. See the `README.txt` in the folder for the JVM options. | Community, Enterprise, Ultimate |
| `gridgain-vector-query-lucene-10` | The Lucene 10 line. Pairs with it only. | Enterprise, Ultimate |

The z/OS package does not ship the Lucene 10 line.

The Lucene 10 line replaces `ignite-lucene-9`, it does not add to it. The two use the same class names, so a node must run exactly one line, and every node in a cluster must run the same line. Two lines on one classpath fail to link at the first index the node touches. A cluster that mixes them returns different vector search recall depending on which node serves the query, because Lucene 10.4 scores a small segment exhaustively where Lucene 9.10 walks a graph.

To switch a node to Lucene 10:

1. Stop the node.
2. Remove the `libs/ignite-lucene-9` folder.
3. Move one of `ignite-lucene-10` (JDK 21 or later) or `ignite-lucene-10-java22` (JDK 22 or later) from `libs/optional` into `libs`.
4. If you use vector search on Enterprise or Ultimate, replace `libs/gridgain-vector-query` with `libs/optional/gridgain-vector-query-lucene-10`.
5. Start the node.

Finish the upgrade to 8.10 on the Lucene 9 line first, and switch lines afterward on every node. Switching during the rolling upgrade would put two lines in one cluster.

To go back to Lucene 9, reverse the steps. The Lucene index is held in memory and rebuilt from the cache data, so switching lines does not migrate or invalidate anything on disk.

<!-- CHECK: the Lucene 10 layout and the switching steps follow the open PRs for GG-51314 (gridgain/gridgain#4229, ggprivate/ggprivate#2525, ggprivate-tc#210), which are not merged. Verified from the diffs: ignite-lucene-10 and ignite-lucene-10-java22 go to libs/optional in the CE descriptors, gridgain-vector-query-lucene-10 in the EE and ULT descriptors only, zOS unchanged, and the switching text is the new modules/lucene-10/README.txt. Not run, and the 8.10.0-master-20261019 build does not have these folders. Re-check the editions, the folder names, and the step that replaces libs/gridgain-vector-query against an unpacked package after the merge. -->
<!-- TODO RE: the README tells the user to "restore libs/ignite-lucene-9" to go back, but step 2 deletes it, and nothing says where to get it from. The rollback paragraph above assumes the folder was moved to libs/optional instead. Confirm, or change step 2 here. Also confirm whether libs/gridgain-vector-query is in libs or libs/optional by default in 8.10. -->

### Gridify API Removed

The Gridify API is removed from `ignite-core`, together with the `ignite-aop` module. This covers the `org.apache.ignite.compute.gridify` package, including `@Gridify`, `@GridifySetToSet`, and `@GridifySetToValue`. Replace Gridify usage with the [compute API](../../gridgain8-development/distributed-computing/distributed-computing.md).

### SSH Module Removed

The `ignite-ssh` module is removed and no longer ships in `libs/optional`. The `org.gridgain:ignite-ssh` artifact is no longer published. `IgniteCluster.startNodes()` and `startNodesAsync()` remain in the API, but they need an SSH implementation on the node classpath. Without one, `startNodes()` throws an `IgniteCheckedException` with the message `Failed to create Ignite component (consider adding ignite-ssh module to classpath)`.

If you start remote nodes with `startNodes()`, contact GridGain Support before you upgrade.

<!-- DECISION (Dmitry Baranov via user, 2026-10-21): the guide does not name the Apache ignite-ssh-ext extension. Customers who need SSH contact GridGain, which provides an external extension. Do not add instructions to build ignite-ssh-ext (it is not published to Maven Central and has no release tag), and do not document the JAVA_HOME or setsid differences: they belong to the extension that GridGain supplies. Verified in source (origin/master e85742c4003): modules/ssh is absent, IgniteCluster.startNodes(...) and IgniteSshHelper remain in core, IgniteComponentType.SSH loads org.apache.ignite.internal.util.nodestart.IgniteSshHelperImpl by name, and the exception text comes from IgniteComponentType.componentException. No 8.9 deprecation notice (GG-50505 closed as Won't Do). -->

### AWS Module Removed

The `ignite-aws` module is removed. It contained the following classes, which are no longer bundled:

* `org.apache.ignite.spi.checkpoint.s3.S3CheckpointSpi`
* `org.apache.ignite.spi.discovery.tcp.ipfinder.s3.TcpDiscoveryS3IpFinder`
* `org.apache.ignite.spi.discovery.tcp.ipfinder.elb.TcpDiscoveryElbIpFinder`
* `org.apache.ignite.spi.discovery.tcp.ipfinder.elb.TcpDiscoveryAlbIpFinder`
* The `EncryptionService` classes that the S3 IP finder uses: `AsymmetricKeyEncryptionService`, `SymmetricKeyEncryptionService`, and `AwsKmsEncryptionService`.

A configuration that references any of them fails with `ClassNotFoundException` until the Apache Ignite `ignite-aws-ext` extension is on the classpath. These classes are marked `@Deprecated` in GridGain 8.9.39, and the javadoc carries the migration notes below.

The extension defines the same class names as `ignite-aws`, so do not use both. Remove `ignite-aws` first (the `libs/ignite-aws` folder of a standalone node, or the `ignite-aws` dependency of a Maven project), and only then add `ignite-aws-ext`. If both are on the classpath, two jars define the same classes and the classpath order decides which one is loaded.

The extension is not a drop-in replacement:

* **Maven coordinates.** `org.gridgain:ignite-aws` stops resolving, so a Maven or Gradle build fails. Use `org.apache.ignite:ignite-aws-ext` instead. The group ID is different, and the classes keep their `org.apache.ignite.*` packages, so imports do not change. You do not need an `<exclusion>`: the extension declares `org.apache.ignite:ignite-core` with `provided` scope, which is not transitive.
* **Region setter.** `AwsKmsEncryptionService` has only `setRegion(Region)` in the extension, and no `setRegion(String)`. A Spring XML file that passes a plain region string fails. Use a `RegionUtils.getRegion` factory bean instead.
* **Older dependencies.** The extension (1.0.0) pulls in older libraries at compile scope than `ignite-aws` does: AWS SDK 1.11.75, `jackson-databind` 2.12.4, `httpclient` 4.5.1, and `bcprov-ext-jdk15on` 1.69. Check them against your security requirements before you switch. This is not a security upgrade.
* **AWS Encryption SDK version.** The extension's KMS support works only with AWS Encryption SDK 1.x. It pins 1.3.2, which has no key commitment (CVE-2020-8897), and it fails with `NoSuchMethodError` on the 2.x SDK that `ignite-aws` ships. If your application uses the 2.x SDK, it cannot use the extension's KMS service.
* **S3 IP finder with `AwsKmsEncryptionService`.** The extension cannot decrypt the key-committed ciphertext that `ignite-aws` wrote with AWS Encryption SDK 2.4.0, and `ignite-aws` rejects the extension's ciphertext. Nodes on the two modules cannot read each other's entries, and the failure stops a node from joining. Switch every node, thick clients included, at once, and set a fresh `keyPrefix` on the IP finder. Entries that the old nodes left in the bucket are not cleaned up by the new ones. This cannot be done as a rolling upgrade. The symmetric and asymmetric key services do not use the SDK and are not affected.

<!-- CHECK: AWS text from GG-51561 and the merged PRs gridgain#4166 (removal, master) and #4187 (8.9 deprecation, with the README and javadoc notes). Verified in source: modules/aws is absent on origin/master e85742c4003 and present with @Deprecated on origin/8.9-master; the extension's AwsKmsEncryptionService has only setRegion(Region) and the extension pins aws-encryption-sdk-java 1.3.2 (apache/ignite-extensions modules/aws-ext); ignite-aws-ext 1.0.0 is on Maven Central; its pom declares ignite-core with provided scope. The dependency versions, the NoSuchMethodError on the 2.x SDK, CVE-2020-8897, and the two-way ciphertext incompatibility are from the @deprecated javadoc merged in #4187 (AwsKmsEncryptionService, TcpDiscoveryS3IpFinder); merged PRs are treated as the source of truth, and they are not run. Apache Ignite made the same move in 2.12.0. -->

### Machine Learning Module Removed

The `ignite-ml` module is removed together with `ignite-ml-spark-model-parser`, `ignite-ml-xgboost-model-parser`, and `ignite-ml-mleap-model-parser`. The module was deprecated in 8.9.38: every public type in `org.apache.ignite.ml.**` carries `@Deprecated`.

Switch to the Apache Ignite `ignite-ml-ext` extension (version 1.0.0, tested against GridGain 8.9 and 8.10) or to the standalone GridGain ML download.

<!-- CHECK: the tested-against statement is from a GG-51303 comment of 2026-09-24 (ignite-ml-ext-1.0.0, the only release). The user-facing wording of "supported" must be confirmed with Product. -->

### Local Store Support Removed

The local store is removed: `@CacheLocalStore`, `CacheFileLocalStore` (Enterprise), and the `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` system property no longer exist. Use native persistence or a regular `CacheStore`, and remove the system property from your start scripts.

### Jetty 12 Is the Only REST Implementation

The `ignite-rest-http` module now runs on Jetty 12 (12.0.40) and requires Java 17. The Jetty 9.4 module is removed, and so is the separate `ignite-rest-http-jetty-12` module that GridGain 8.9.x shipped as an option. The module keeps the `ignite-rest-http` artifact name, so dependency declarations do not change.

A configuration that does not set `ConnectorConfiguration.setJettyPath(...)` needs no changes. A custom Jetty XML file written for Jetty 9.4 does not load on Jetty 12, and the node fails to start with `Failed to start Jetty HTTP server` and `IllegalStateException: No matching constructor class org.eclipse.jetty.server.Server`. Migrate it as follows:

1. Rename the `threadpool` argument of the `Server` constructor to `threadPool`, or remove the name and pass the argument by position. A named argument that matches no constructor parameter makes the whole constructor unmatchable.
2. Remove the `<Set name="handler">` block that uses `HandlerCollection` or `HandlerList`. Both classes are removed in Jetty 12, and GridGain installs its own REST handler after your file is applied.

The `DOCTYPE` declaration needs no change.

For HTTPS and mutual TLS, use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` with `SslConnectionFactory` and `HttpConnectionFactory`. `SecureRequestCustomizer` checks the SNI host name by default. Set `sniHostCheck` to `false` on it if the certificate name does not match the bind address. The client certificate chain is available to the REST handler through the SSL session data, not through the Jetty 9 `X509_ATTRIBUTE`.

<!-- CHECK: the HTTPS and mutual-TLS notes are condensed from modules/rest-http/MIGRATION.md (master) and were not run. Decide whether to include the full HTTPS XML example from MIGRATION.md or link to the REST API page. Each of the two Jetty XML edits alone was not tried; the failure and the fix were verified with both edits together. -->

## Distribution and Packaging Changes

* **Integrations move out of the server packages.** The Oracle GoldenGate integrations and the Kafka Connect connector no longer ship in the server package and are not in an `integration` folder. Get them from the integrations download, Maven, or Confluent Hub. `gridgain-kafka-connect` is shipped only as its own artifact.
* **Maven-only modules.** `ignite-hibernate-7.4` and `ignite-spring-data` are published to Maven only and are no longer in `libs/optional`. If you copy these jars into `libs`, take them from Maven.
* **OpenCensus.** `ignite-opencensus` moves from `libs` to `libs/optional`. To keep OpenCensus tracing, move the `ignite-opencensus` folder back into `libs`.
* **Control Center agent.** `control-center-agent` moves from `libs` to `libs/optional`. A node started from the 8.10 distribution does not load the agent, and does not connect to Control Center, until you move the `control-center-agent` folder into `libs`.
* **Spring Data commons.** `ignite-spring-data-commons` is no longer in `libs/optional`. Like `ignite-spring-data` in the previous bullet, it is published to Maven only. Take the commons dependency from Maven if you copied it.
* **Bulk load.** `gridgain-bulkload` stays in `libs/optional` of the server packages. It is not moved to the integrations download. Its dependency set is smaller (about 93 MB instead of about 857 MB): the single AWS SDK bundle jar is replaced by the individual AWS clients that bulk load uses, so reading from S3 still works, and the Hadoop, Snowflake, and Iceberg dependency closures are reduced. The Snowflake JDBC driver (`snowflake-jdbc`) is no longer in `libs/optional/gridgain-bulkload`. Snowflake was never a supported source, and both paths to it are closed by default: `jdbc:snowflake:` is not in the schemes that `COPY ... FORMAT JDBC` accepts (see [Server-Side SQL COPY](#server-side-sql-copy)), and `SnowflakeCatalog` is not in `importExport.allowedIcebergClasses`, which is empty by default. The change affects you only if you added `jdbc:snowflake:` to `GRIDGAIN_BULKLOAD_JDBC_ALLOWED_URL_SCHEMES` or `SnowflakeCatalog` to `importExport.allowedIcebergClasses`. In that case, put a Snowflake JDBC driver next to the module yourself.
* **No evaluation license archives.** The Enterprise, Ultimate, and z/OS evaluation-license archives are no longer built.
* **Examples.** Examples are no longer part of the source repository. They are published in the public `gg8-examples` repository and are still bundled into the packages.
* **C++ client.** The C++ client requires C++14, and the autotools build is removed. Build the C++ client with CMake.

<!-- CHECK: the Snowflake text is from GG-51118 and GG-51108 (the default scheme list is JdbcProperties.DFLT_ALLOWED_SCHEMES = mariadb, mysql, postgresql, with a pinning test JdbcPropertiesTest.rejectsSnowflakeSchemeByDefault). Not run. Check that allowedIcebergClasses is the right name next to allowedCatalogUris in the COPY section, which does not list it. -->
<!-- CHECK: compared the 8.9.38 and 8.10.0-master-20261019 distributions: control-center-agent moved from libs to libs/optional (the agent log line was seen on 8.9 only; that the 8.10 node does not connect without it is from the folder layout, not run). -->
<!-- CHECK: ignite-spring-data-commons is in 8.9.38 libs/optional and absent from the 8.10 master build. The module still exists on master (modules/spring-data-commons), and assembly/dependencies-apache-ignite.xml excludes both org.gridgain:ignite-spring-data and org.gridgain:ignite-spring-data-commons from the distribution, so it is Maven-only. -->
<!-- CHECK: in the 8.10 master build, libs/optional has no ignite-aws, ignite-hibernate-7.4, or ignite-spring-data, has ignite-opencensus, and has no integration/ folder. GG-51112 (gridgain-bulkload to the integrations download) was closed on 2026-10-17 by Dmitry Baranov as "decided not to do this": bulkload stays in libs/optional, and the size was solved by GG-51107 (the awssdk bundle fat jar is dropped, the granular s3, sts, and glue clients stay) and GG-51108 (857 MB to about 93 MB). Narrowing the dependency set further is GG-52384. The integrations download itself was not part of the verified build. -->
<!-- TODO Unison/RE: link to the integrations download (GG-51118 is the Docs ticket for this upgrade guide section, owner Dmitry Baranov). The list of what leaves libs/optional and integration/ is settled: GG-51115 and GG-51116 (ignite-hibernate-7.4 and ignite-spring-data, Maven only) are Resolved, GG-51112 (bulkload) is not done, and the GoldenGate and Kafka Connect integrations are out of the server packages. -->

## Cassandra Store Uses the DataStax Driver 4

The Cassandra store moves from DataStax Java driver 3.2 to 4.17 (`com.datastax.oss.driver.*`) and from `cassandra-all` 3.11 to 5.0.8. Cassandra 2.1 or later is required, and Cassandra 3 clusters must be upgraded 3 → 4 → 5.

The `DataSource` configuration API changed:

* `setLocalDataCenter()` is required when you specify explicit contact points and no custom load balancing policy.
* Policies are configured by class: `setLoadBalancingPolicyClass()`, `setReconnectionPolicyClass()`, `setRetryPolicyClass()`, `setAddressTranslatorClass()`, and `setSpeculativeExecutionPolicyClass()` replace the former instance-based setters.
* `setPoolingOptions()`, `setSocketOptions()`, and `setNettyOptions()` are removed. Use `setConfigFile()` and a driver configuration file.
* `setSslOptions()` is replaced by `setSslEngineFactory()`.
* `user` and `password` are mutually exclusive with `credentials`. Set one or the other.

Update the `DataSource` bean definitions in your Spring XML configuration. Previously serialized `DataSource` instances (those held by dynamically created caches) cannot be read by 8.10. Drop and recreate those caches. Large transactions may reach the Cassandra `batch_size_fail_threshold` setting.

<!-- CHECK: verified in source: driver 4.17.0, cassandra-all 5.0.8, setLoadBalancingPolicyClass / setConfigFile / setSslEngineFactory / setLocalDataCenter present; setPoolingOptions / setSocketOptions / setNettyOptions absent (present on 8.9). Not verified: error messages, setCollectMetrix / setJmxReporting removal, credentials exclusivity, the serialized-DataSource failure, and the batch-size threshold. The text follows the 8.10.0-b1 release notes and the GG-49566 release note summary. -->

## Configuration and Default Value Changes

### SFTP Snapshot Transport Verifies the Host Key by Default

`SftpConfiguration.strictHostKeyChecking` now defaults to `true`. In 8.9.x it defaulted to `false`. Before the first snapshot transfer to an SFTP destination, add the server to the OpenSSH-format known hosts file, or set `strictHostKeyChecking` to `false` explicitly. Otherwise transfers fail. The file is the one that `knownHostsPath` points at. If `knownHostsPath` is not set, GridGain uses `~/.ssh/known_hosts` of the account that runs the node.

For more information, see [Configuring SFTP Location](../snapshots/network-backups.md#configuring-sftp-location).

<!-- CHECK: default values verified by reading them from the 8.9.38 and 8.10 master builds; a real SFTP transfer was not run. -->

### Java Thin Client Timeouts Have Default Values

The Java thin client now has a handshake timeout of 10 seconds and a request timeout of 60 seconds. In 8.9.x both were infinite. A request that takes longer than 60 seconds now fails with a timeout. To keep the previous behavior, call `ClientConfiguration.setHandshakeTimeout(0)` and `ClientConfiguration.setRequestTimeout(0)`. The .NET thin client defaults are unchanged: `HandshakeTimeout` and `RequestTimeout` both default to 5 seconds, as `SocketTimeout` did in 8.9.

`ClientConfiguration.setTimeout()` is deprecated. It sets both timeouts. `getTimeout()` returns the request timeout and logs a warning if the two timeouts differ.

### Thin Client DNS Resolution

The Java thin client resolves its configured addresses through `DnsClientAddressFinder` when no custom address finder is set. When a host name resolves to several IP addresses, the client uses all of them instead of one. This affects host names backed by several A records or round-robin DNS.


### Java Thin Client Transactions Start Lazily

A Java thin client transaction now starts lazily. `txStart()` no longer sends `TX_START`; the message is deferred until the first cache operation in the transaction, and it is routed to a node chosen from the cache and the affinity key of that operation. Applications are not expected to notice, but a transaction that performs no cache operation never reaches the server, and an error that used to surface at `txStart()` now surfaces at the first operation.

<!-- TODO Tiago Marques Godinho / Pavel Tupitsyn (GG-48504): the Confluence page says Java thin client transactions are "partition-aware by default" with an opt-out by disabling partition awareness. In source the node for TX_START is chosen by affinity only when ReliableChannel.partitionAwarenessEnabled (ClientConfiguration.affinityAwarenessEnabled, default false) is set and the affinity info is current (ReliableChannel.affinityService, :412); otherwise TX_START goes to the default channel (TcpClientTransactions.txStart0, :130-134). Is transaction routing meant to be opt-in through that flag? If it is meant to be on by default, the guide must warn about the connectivity that partition awareness needs. -->



### Vector Search Limits

Vector search now enforces limits and rejects queries above them:

* The number of dimensions of a vector index is limited by `GRIDGAIN_VECTOR_MAX_DIMENSIONS`, which defaults to 4096. A vector with 4097 or more dimensions is rejected when you put it into the cache (`Field [VEC_VEC] vector's dimensions must be <= [4096]`). The limit applies to indexes that are created after the property is set, so raise it before you create indexes on wider vectors. The memory and search time of an index grow with the number of dimensions, and above 8192 dimensions a vector no longer fits into the 32 KB read buffer of the index storage, so every read spans several buffers.
* A vector query may request at most `GRIDGAIN_VECTOR_MAX_K` neighbors (default 10000). A query with `k` below 1 or above the limit is rejected with a `CacheException`, for example `Vector query 'k' is above the maximum number of neighbors a query may ask for [k=10001, max=10000]`. The limit is read in the JVM that runs the query, so set the property on the application that runs queries as a thick client, and on the server nodes for thin-client queries.

Neither limit exists in 8.9.x. For more information, see [Vector Search](../../gridgain8-development/vector-search/README.md).

<!-- TODO RE/QA: has a vector index built on 8.9 been opened on 8.10 (rolling upgrade or restart)? Any index-format change? Not tested: 8.9.38 rejects the test license for vector search. Also not tested: the thin-client path of the k limit (confirm with Platforms). The "applies to indexes created after the property is set" wording follows the javadoc of GRIDGAIN_VECTOR_MAX_DIMENSIONS in IgniteSystemProperties; it was not run. -->

### Startup Messages for Stale Properties

An unknown property in the Spring XML configuration still fails node startup, as it did in 8.9.x, but the message is now short and names the bean and the property, for example `Configuration property IgniteConfiguration.noSuchProperty does not exist`.

GridGain 8.10 also logs a warning at node start for each Apache Ignite system property or environment variable that GridGain does not support. The list is fixed: the Calcite SQL engine (`IGNITE_CALCITE_*`), `IGNITE_SNAPSHOT_SEQUENTIAL_WRITE`, the performance statistics properties (`IGNITE_PERF_STAT_*`), `IGNITE_ALLOW_MIXED_CACHE_GROUPS`, `IGNITE_ENABLE_OBJECT_INPUT_FILTER_AUTOCONFIGURATION`, `IGNITE_USE_BINARY_ARRAYS`, and `IGNITE_SQL_FORCE_LAZY_RESULT_SET`. The warning names the property and the reason and links to the Apache Ignite migration guide. The node starts normally. Remove these properties from your startup scripts.

### JMX Object Metrics Are Strings

Metric values of the `ObjectMetric` type are exposed through JMX as strings. A JMX tool that reads these attributes gets a `String` instead of the typed object. For example, in the `ignite` metric registry, `localNodeId` was a `UUID`, `userAttributesFormatted` and `lifecycleBeansFormatted` were `List` values, and `longJVMPauseLastEvents` was a `Map` in 8.9.x. In 8.10 all four are `String` values, and the declared attribute type is `java.lang.String`.

{% hint style="info" %}
The metric MBeans exist only if you configure `JmxMetricExporterSpi` in `IgniteConfiguration.metricExporterSpi`. The default exporter does nothing.
{% endhint %}

### System Properties

| Property | Change |
| --- | --- |
| `IGNITE_REST_SCAN_QUERY_FILTER_CLASSES` | New. See [REST Scan Queries With a Filter Class](#rest-scan-queries-with-a-filter-class). |
| `GRIDGAIN_VECTOR_MAX_DIMENSIONS`, `GRIDGAIN_VECTOR_MAX_K` | New. See [Vector Search Limits](#vector-search-limits). |
| `GRIDGAIN_VECTOR_BINARY_QUANTIZATION`, `GRIDGAIN_VECTOR_INDEX_DELETES_PCT`, `GRIDGAIN_VECTOR_INDEX_MAX_SEGMENTS`, `GRIDGAIN_VECTOR_INDEX_RAM_BUFFER_MB`, `GRIDGAIN_VECTOR_NOCOPY_SCORER`, `GRIDGAIN_VECTOR_QUERY_CACHE_MIN_SEGMENT_DOCS`, `GRIDGAIN_VECTOR_QUERY_CACHE_MIN_SEGMENT_SIZE_RATIO`, `GRIDGAIN_VECTOR_QUERY_THREADS` | New. Vector index and query tuning. No action is needed. `GRIDGAIN_VECTOR_BINARY_QUANTIZATION` is `false` by default. See [Vector Search](../../gridgain8-development/vector-search/README.md). |
| `IGNITE_CUSTOM_METRICS_MAX_NAME_LENGTH` | New. Limits the length of custom metric registry and metric names. The default is 256. |
| `IGNITE_TCP_COMM_MSG_QUEUE_WARN_SIZE` | New. When set to a positive number, logs a warning when the outgoing message queue of the TCP communication SPI exceeds it. The default is 0, which prints no warning. |
| `IGNITE_BPLUS_TREE_DISABLE_METRICS` | New. Disables the metrics of the secondary index B+Trees. The default is `false`. |
| `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` | Removed with local store support. |

## Security, Permission, and Licensing Changes

### Server-Side SQL COPY

Server-side SQL `COPY` against a file or an object store is closed by default. In 8.9.x the statement read any file that the node process could read, and 8.10 rejects it with `Server-side file/object-store COPY is disabled on this node` until you configure it. To use it after the upgrade:

1. Set `fileAccessEnabled` to `true` on the `ImportExportConfiguration` block of the GridGain plugin configuration (default `false`).
2. Fill the allow-lists on that block: `importRoots` for local directories, `allowedS3Buckets` and `allowedS3Endpoints` for S3, and `allowedCatalogUris` for Iceberg catalogs. An empty list forbids the access.
3. Grant the new `COPY_FROM_FILE` and `COPY_TO_FILE` [permissions](../../security/authorization-permissions.md) to the roles that run server-side `COPY`. They are system permissions, for example `{system:['COPY_FROM_FILE']}` in the permission string. In 8.9.x the statement needed no permission beyond the cache permissions. In 8.10 a role without `COPY_FROM_FILE` fails with `Authorization failed [perm=COPY_FROM_FILE, name=null, ...]`.

`ImportExportConfiguration` is node-local, so configure it identically on every node. Point `importRoots` at dedicated directories, never at the node work directory: `COPY_TO_FILE` overwrites files in a root. Client-side `COPY` is not affected.

`COPY ... FORMAT JDBC` also validates the JDBC URL. Only the `jdbc:mariadb:`, `jdbc:mysql:`, and `jdbc:postgresql:` schemes are accepted by default (`GRIDGAIN_BULKLOAD_JDBC_ALLOWED_URL_SCHEMES`), and `${VAR}` placeholders are no longer expanded unless the variables are listed in `GRIDGAIN_BULKLOAD_JDBC_ENV_ALLOWLIST`.

<!-- CHECK: not run: COPY into a file (COPY_TO_FILE check; the grammar needs a subquery) and the JDBC URL scheme and ${VAR} behavior (source only). Rejection texts verified: "COPY location is outside the configured import roots (importExport.importRoots)" and "COPY S3 location is not in the configured allow-list (importExport.allowedS3Buckets)". -->

### REST Scan Queries With a Filter Class

The `EXECUTE_SCAN_QUERY` REST command instantiates a filter class only if the class is listed in the `IGNITE_REST_SCAN_QUERY_FILTER_CLASSES` system property. In 8.9.x the node instantiated any class that the request named. The list is empty by default, so a scan query that passes `className` is rejected until you allow the class. Set the property to a comma-separated list of fully qualified class names (exact match) on every node that has the REST connector enabled.

REST error responses no longer include the server stack trace. In 8.9.x the `error` field ended with `trace=` followed by the Java stack trace. In 8.10 it contains only the message, for example `Failed to handle request: [req=CACHE_GET, err=Failed to find cache for given cache name: nonexistent]`. Clients that parsed the trace must use the message instead.

### Thin Client Permission and Filter Checks

Thin client requests are checked more strictly:

* `SERVICE_INVOKE` is checked for thin client calls to Java services, including services that run on a node other than the one the client is connected to. A role without it fails with `Authorization failed [perm=SERVICE_INVOKE, name=<service name>]`. Grant `SERVICE_INVOKE` to the roles whose thin clients call services.
* Continuous query remote filters sent by thin clients go through the marshaller class filter (`IGNITE_MARSHALLER_WHITELIST` and `IGNITE_MARSHALLER_BLACKLIST`). A filter class that the lists do not allow starts failing.

<!-- CHECK: GG-51625 describes the unchecked path: ClientServiceInvokeRequest never called authorize() for ordinary Java services (not PlatformService) invoked through a thin client, and it matters only when a security plugin enforces SERVICE_INVOKE, not with setAuthenticationEnabled(true) alone. The fix ("check SERVICE_INVOKE for Java services on remote nodes", #4171) is on both master and 8.9-master, so a cluster on a later 8.9.x build that includes it behaves the same as 8.10. Not run: the 8.9.38 build rejected the call in the test, so confirm with Pavel Tupitsyn which 8.9.x build first has the fix before the first bullet claims what changes. -->
<!-- CHECK: GG-50453 (marshaller filter for continuous query remote filters) is on master with tests; behavior not run. It only matters when IGNITE_MARSHALLER_WHITELIST or IGNITE_MARSHALLER_BLACKLIST is set. Names of the two properties are from the Confluence page. -->

### Per-Feature License Checks

GridGain 8.10 checks the license for every feature that the node configuration uses. GridGain 8.9 checked only snapshots, compression, vector search, and z/OS, so a configuration that started on 8.9 can fail on 8.10 with the same license file. When the check fails depends on the feature:

* **At node start.** Authentication or authorization, data center replication, rolling upgrades, and snapshots (including point-in-time recovery) fail the node start, with a message such as `Security feature is not allowed by the licence.`
* **When a cache starts.** Rack awareness, cache encryption, and vector indexes are checked for each cache configuration. The cache fails to start with `Rack awareness is not allowed by the licence [cacheName=...]`, `Encryption is not allowed by the licence [cacheName=...]`, or `Vector search is not allowed by the licence [cacheName=...]`.

The license file lists its features as `<enabled-feature name="..."/>` entries and has a `<type>` element (`ENT` for Enterprise). Feature names are matched exactly, and most of them use underscores, not hyphens. A license with the `ultimate` feature passes every check. The table shows what else is accepted:

| Your configuration uses | The license must have | 8.9.x |
| --- | --- | --- |
| Authentication or authorization (`authenticator` or `authenticationEnabled`) | `security` | Not checked |
| Data center replication (a data center ID) | `data_center_replication` | Not checked |
| Rack awareness (an affinity backup filter) | `rack_awareness` | Not checked |
| Rolling upgrades (`rollingUpdatesEnabled=true`) | Type `ENT`, or `rolling_upgrades` | Not checked |
| Cache encryption | Type `ENT`, or `encryption` | Not checked |
| Vector search index | Type `ENT`, or `vector-search` | `vector-search` only |
| Local snapshots (a `snapshotConfiguration`) | `local_snapshots` | `ultimate` |
| Remote (SFTP) snapshots | `remote_snapshots` | `ultimate` |
| Point-in-time recovery | `point_in_time_recovery` | `ultimate` |
| Entry compression | `compression` | `compression` or `ultimate` |

In every row, a license with the `ultimate` feature is also accepted. Before you upgrade, compare the features of your license with your configuration, and contact GridGain support if a feature is missing. A license file that works on 8.9 is accepted by 8.10 as a file, and the checks above decide only which features it enables. The MariaDB license key format is also supported.

<!-- CHECK: the table is verified in source (ggprivate master GridPluginProvider vs origin/8.9-master). A failing start on 8.10 was not run (needs a license without the feature). The 8.10.0-b1 release notes say an Enterprise license does not satisfy data center replication, security, and rack awareness by type. -->


## Client and Driver Changes

* **.NET.** The packages target `netstandard2.0`, `net8.0`, and `net10.0`, and nullable reference annotations are added, so projects with nullable enabled may see new warnings. Transactions are async-local, so `async`/`await` works inside a transaction block; code that relies on per-thread transactions can restore the old behavior with the `IGNITE_TX_USE_THREAD_LOCAL` environment variable. Requests that are not partition-aware are balanced across connections round-robin.
* **C++.** See [Distribution and Packaging Changes](#distribution-and-packaging-changes).
<!-- TODO Pavel Tupitsyn (Platforms): a thin client built with the 8.10 libraries against 8.9 servers. Held out of the guide until confirmed. Draft bullet: "The thin client protocol version is the same in 8.9 and 8.10, and new capabilities are negotiated with feature flags. A thin client built with the 8.10 libraries can connect to an 8.9 server, but an operation that needs a feature the server does not have, for example creating an SQL cache from the client, service awareness, or the new vector query parameters, is rejected until the servers are upgraded." Source: ProtocolVersion.CURRENT_VER is V1_7_1 on both branches, and ProtocolBitmaskFeature differs. Not run. -->

<!-- CHECK: the thin client compatibility bullet follows ProtocolVersion.CURRENT_VER (V1_7_1 on both 8.9-master and master) and the ProtocolBitmaskFeature lists; it was not run against a mixed cluster. The .NET defaults are IgniteClientConfiguration.DefaultSocketTimeout = 5000 ms on both branches, and SocketTimeout is [Obsolete] on master. -->
<!-- CHECK: target frameworks verified. IGNITE_TX_USE_THREAD_LOCAL exists in ThreadOrAsyncLocal.cs; behavior not tested. -->

## Deprecations

The following still work and are deprecated:

* `TRANSACTIONAL_SNAPSHOT` atomicity mode. Use `TRANSACTIONAL` or `ATOMIC`. Also deprecated in 8.9.38.
* `DataStorageConfiguration.setSystemRegionInitialSize()` and `setSystemRegionMaxSize()`. Use `SystemDataRegionConfiguration`.
* `IgniteConfiguration.setDefaultQueryTimeout()` and `getDefaultQueryTimeout()`. Use `SqlConfiguration`.
* `ClientConfiguration.setTimeout()`. Use `setHandshakeTimeout()` and `setRequestTimeout()`.
* `ClientConfiguration.setPartitionAwarenessEnabled()`. Use `setAffinityAwarenessEnabled()`.
* .NET `IgniteClientConfiguration.SocketTimeout`. Use `HandshakeTimeout` and `RequestTimeout`.
* The rebalance settings of `ClientCacheConfiguration`.

## Changes That Need No Action

* **Baseline auto-adjust.** New separate scale-up and scale-down timeouts are available in the Java API, `control.sh` (`--baseline scale_up_auto_adjust` and `--baseline scale_down_auto_adjust`), the MXBean, and .NET. The single timeout still works: `control.sh --baseline auto_adjust enable timeout <ms>` sets both timeouts. The output of `control.sh --baseline` now shows a separate line for scale-up and scale-down. When scale-down auto-adjust is disabled, its line shows `softTimeout=9223372036854775807` (the largest `long` value). This is not a real timeout, and no scale-down happens.
* **`VisorDataTransferObject` header check.** The header check that `VisorDataTransferObject` performs when it reads a payload now compares the full magic number. The header is written the same way in 8.9 and 8.10, so no action is needed, and only a malformed or foreign payload is rejected where it could previously pass.
* **New SQL views and metrics.** Four SQL views are new in `SYS`: `CACHE_LOCKS`, `CACHE_EXPLICIT_LOCKS`, `PLUGINS`, and `SQL_PLANS_HISTORY`. A new metric registry, `communication.tcp.connectionPool`, is available. Nothing was removed from either list.
* **New `control.sh` commands.** `--snapshot create|restore|status|cancel` (Apache Ignite style, with `--incremental`), `--baseline scale_up_auto_adjust` and `scale_down_auto_adjust`, and the `--node-ids` and `--all-nodes` options of `--system-view`. The GridGain `snapshot-utility.sh` keeps working with 8.9 snapshots (full and incremental), and it is the tool to use for the upgrade and rollback steps in this guide. `control.sh --snapshot` is an Apache Ignite 2 compatible front end for GridGain snapshots, intended for scripts written for Apache Ignite 2. It needs the Ultimate edition with snapshots configured, and otherwise fails with `Snapshots are not enabled on this GridGain cluster, Ultimate edition is required.` GridGain 8.9 has no `control.sh --snapshot` command.
* **Data center replication handshake.** The handshake between data centers now negotiates the batch format version and optional protocol features. With a peer that does not negotiate, for example an 8.9 cluster, it uses the previous format.
* **New tools and packages.** `bin/schema-import.sh` and a `mcp` folder with the GridGain MCP server are included in the 8.10 distribution.

## New Features

GridGain 8.10 also adds the following features. You do not need them to upgrade, and they need no action. For details, see the 8.10 release notes and the documentation of each feature.

* **Vector search.** Similarity scores, filters and keys-only queries, per-index HNSW parameters, `int8` storage, binary quantization, a `PARTITIONED` vector index, and version 2 of the thin client vector protocol. See [Vector Search](../../gridgain8-development/vector-search/README.md) and [Vector Search Limits](#vector-search-limits).
* **Apache Ignite thin clients.** Apache Ignite thin clients can connect to a GridGain server.
* **Java thin client.** `DataStreamer`, asynchronous overloads of the cache operations, service awareness, and a method to create an SQL cache.
* **.NET.** More asynchronous API methods, to match the Java API.
* **Compatibility with Apache Ignite 2.** The Apache Ignite snapshot API, CDC WAL records, and `keepBinary` in the REST API.
* **Metrics.** A custom metrics API, a `snapshot` metric registry, and further metrics that Apache Ignite 2 has, so that JMX metrics match it more closely. Data center replication has new handshake and delay metrics. A role that registers custom metrics needs the new `CUSTOM_METRICS_MANAGE` system permission, for example `{system:['CUSTOM_METRICS_MANAGE']}` in the permission string.

<!-- CHECK: the list above comes from the 8.10.0-b1 release notes, the Confluence page, and the titles of GG-52363, GG-52364, GG-51735, GG-52322, GG-52323 and GG-49202. None of it was run, and the tickets have no description beyond a link to the source ticket. Check each line with its feature owner before publishing, and add a link to the feature page where one exists. -->
<!-- CHECK: odd values in the `control.sh --baseline` output ("will happen in '9223370244437924903' ms" for scale-down, and a scale-up countdown that ignores the new timeout) are a question for the developers; not described here. -->
<!-- CHECK: the following additions come from the 8.10.0-b1 release notes and the Confluence page and were not run: vector search additions (similarity scores, filter and keys-only, per-index HNSW parameters, int8 storage, binary quantisation, PARTITIONED vector index, thin-client vector protocol v2), custom metrics API, Apache Ignite thin clients connecting to GridGain servers, Java thin client DataStreamer and async overloads, .NET async parity, AI2 compatibility (snapshot API, CDC WAL records, REST keepBinary), data center replication handshake and delay metrics. -->
<!-- CHECK: the control.sh --snapshot text follows SnapshotCommand ("AI2 API compatible"), the VisorIgniteSnapshot*Task jobs and IgniteSnapshotTranslator in ggprivate, and GG-49474 / GG-49762. Not tested: whether a snapshot made with snapshot-utility.sh can be restored with control.sh --snapshot, or the other way round. -->
<!-- TODO Mikhail Pochatkin (GG-50908): upgrade order for two clusters connected by data center replication, and whether an 8.9 and an 8.10 cluster were run together end to end. In source the order should not matter: the batch format version is negotiated per connection, and an 8.10 sender re-encodes batches to the legacy format for an 8.9 receiver (DrProtocolVersion, DrReceiver, DrSenderRemoteDataCenterNode). Open: the sender store keeps every batch in the V2 format (DrSenderImpl, DrExternalBatchRequestV2, wire type 8), so can an 8.9 node read batches that are still in the store after a rollback of the sender cluster? The handshake text above follows the ticket (negotiation with a fallback for peers that do not negotiate, proven by wire-level tests); it is on master only and was not backported to 8.9. The DCR configuration, metric, and behavior changes for customers are also still missing. Views and registries that only appear when a feature is configured were not listed. -->
