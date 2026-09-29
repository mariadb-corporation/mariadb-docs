---
description: >-
  GridGain 8.8.14 speeds up node start, adds continuous queries to the C++ thin client
  and thin client support to Spring Data, and includes numerous fixes.
hidden: true
---

# GridGain 8.8.14 Release Notes

## New Features

### Sped up Node Start

GridGain now periodically creates checkpoint history snapshots. This significantly speeds up node startup time by removing the need to read checkpoint to prepare node history for PME.

### Added Continuous Queries to C++ Thin Client

C++ thin clients now also support [continuous queries](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/key-value-api/continuous-queries). Here is an example of how you can implement them in your code:

{% code title="C++" %}
```cpp
#include <ignite/thin/ignite_client.h>

using namespace ignite::thin::cache;
using namespace ignite::thin::cache::event;

/**
 * Test listener class. Stores events it has been notified about in concurrent
 * queue so they can be checked later.
 */
template<typename K, typename V>
class MyListener : public CacheEntryEventListener<K, V>
{
	/**
	 * Event callback.
	 *
	 * @param events Events.
	 * @param num Events number.
	 */
	virtual void OnEvent(const CacheEntryEvent<K, V>* events, uint32_t num)
	{
		for (uint32_t i = 0; i < num; ++i)
		{
			const CacheEntryEvent<K, V>& event = events[i];

			std::cout << "New cache event" << std::endl;
			std::cout << "Event type: " << event.GetEventType() << std::endl;
			std::cout << "Key: " << event.GetKey() << std::endl;
			std::cout << "Value: " << (event.HasValue() ? event.GetValue() : "None") << std::endl;
			std::cout << "Old value: " << (event.HasOldValue() ? event.GetOldValue() : "None") << std::endl;
		}
	}

	/**
	 * Disconnected callback.
	 *
	 * Called if channel was disconnected. This also means that continuous query was closed and no more
	 * events will be provided for this listener.
	 */
	virtual void OnDisconnected()
	{
	    std::cout <<
			"Connection to the node lost. Continuous query is closed. "
			"You will not get any new notifications unless you register a new continuous query."
			<< std::endl;
	}
}


void Example(ignite::thin::IgniteClient& client)
{
	CacheClient<int32_t, std::string> cache = client.GetOrCreateCache<int32_t, std::string>("MyCache");

    auto listener = make_shared< Listener<int32_t, std::string> >();

    query::continuous::ContinuousQueryClient<int32_t, TestEntry> qry(MakeReferenceFromSmartPointer(listener));

    query::continuous::ContinuousQueryHandleClient handle = cache.QueryContinuous(qry);

	cache.Put(1, "Lorem ipsum");
	cache.Put(2, "Hello world");
	cache.Put(1, "Lorem ipsum dolor sit amet");
	cache.Remove(1);
}
```
{% endcode %}

### Added Support for Thin Clients in Spring Data Client

Spring Data Client now can be worked with from thin clients. Here is the example:

{% code title="Java" %}
```java
// Used igniteClient bean for accessing to ignite.
@RepositoryConfig(cacheName = "PersonCache", igniteInstance = "igniteClient")
public interface IgniteClientConfigRepository extends IgniteRepository<Object, Serializable> {
    // No-op.
}
```
{% endcode %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34570 | Platforms & Thin Clients | .NET: Fixed platform cache not restoring data from persistent storage after node restart. |
| GG-34550 | Cluster SQL Engine | Fixed a possible NullPointerException if a column type was null in the JmxSystemViewExporterSpi. |
| GG-34539 | Cluster Compute Grid | Added an ability to run compute tasks without @ComputeTaskSessionFullSupport annotation when using PriorityQueueCollisionSpi. |
| GG-34537 | Cluster Storage Engine | Fixed an issue when a cache destroy operation during an active transaction could cause NullPointerException. |
| GG-34463 | Cluster Communication | Suppressed a non-informative ClosedChannelException which was logged in some cases. |
| GG-34400 | Binary Objects | Fixed an AssertionError when getting unassigned field in BinaryObjectBuilder. |
| GG-34391 | Binary Objects | Fixed unexpected object deserialization on concurrent operations when binary projection was used. |
| GG-34377 | Platforms & Thin Clients | Java thin: reduced memory usage by avoiding extra buffer copy. |
| GG-34372 | Cluster SQL Engine | Prevented confusing warning from being logged. |
| GG-34370 | Cluster SQL Engine | Added query ID to logs for long running SQL queries. |
| GG-34300 | Cluster Metrics & Monitoring | Fixed a possible NullPointerException in cache metrics on node startup. |
| GG-34295 | Platforms & Thin Clients | .NET: Fixed dynamically generated types deserialization support. |
| GG-34294 | Cluster Storage Engine | Fixed a bug with the defragmentation failing on DECIMAL and VARCHAR indexes. |
| GG-34258 | Cluster Compute Grid | Added the ability to change the priority of a compute task if PriorityQueueCollisionSpi is configured. |
| GG-34257 | Platforms & Thin Clients | Fixed potential out of memory exception in thin client protocol handler that could be caused by erroneous data. |
| GG-34225 | Distributed Data Structures | Fixed potential data corruption during rapid delete and update operations. |
| GG-34222 | Cluster Storage Engine | IGNITE_WAIT_FOR_BACKUPS_ON_SHUTDOWN system property was deprecated. Use ShutdownPolicy instead. |
| GG-34218 | Control Center Agent | Increased security in management script command outputs. |
| GG-34200 | Cluster SQL Engine | Fixed an issue with comparing indexed fields with values that have different types. |
| GG-34196 | Platforms & Thin Clients | CPP Thin: Continuous Queries implemented. |
| GG-34186 | Cluster Compute Grid | Added a subscription to changes in compute task statuses. |
| GG-33884 | Cluster Deployment | Fixed a bug with cluster crashing if a class with higher bytecode version was received from the client. |
| GG-33743 | Platforms & Thin Clients | Fixed a possible freeze when thin clients were used with TLS1.3. |
| GG-33717 | Cluster Metrics & Monitoring | Added system views for data structures. |
| GG-33698 | Cluster Storage Engine | Fixed a rare case when rebalance did not happen during a client joining the cluster. |
| GG-33675 | Cluster Storage Engine | Fixed an issue that caused speed-based writes throttling to fail in protecting Checkpoint Buffer from exhaustion. |
| GG-33208 | Cluster Storage Engine | Introduced checkpoint history snapshots to speed up node startup process. |
| GG-33203 | Cluster SQL Engine | Fixed inline-size calculation for PK of varchar(N) column. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34556 | Cluster Security | Updated jackson-databind and log4j2 version to fix a vulnerability. |
| GG-34371 | GridGain Integrations | Added support for Spring Data in thin clients. |
| GG-34339 | Cluster SQL Engine | Added an ability to specify inline size of PK and affinity key indexes from CREATE TABLE and QueryEntity commands. |
| GG-33727 | Control Center Agent | Added APIs (Java, control.sh, and JMX) to change cluster ID and cluster secret. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34335 | Cluster Snapshot Utility | Fixed a rare freeze (caused by node stop) during custom snapshot operation. |
| GG-33981 | Cluster Data Snapshots and Recovery | Fixed a rare freeze during custom snapshot operation. |
| GG-33737 | Cluster Data Snapshots and Recovery | Added a log message about the impossibility of creating a snapshot on a schedule. |
| GG-33532 | Cluster Data Snapshots and Recovery | Snapshot creation now stops early if there are caches with lost partitions and partition loss policy is not IGNORE. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34562 | Control Center Agent | Added sending of compute task priority to Control Center. |
| GG-34558 | Control Center Agent | Fixed CVE-2021-44832. |
| GG-34241 | Control Center Agent | Fixed node versions on Cluster page in GridGain Portal. |
| GG-33996 | Control Center Agent | Added support for SFTP for code deployment. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

- 8.7.2-p15
- 8.7.3
- 8.7.4
- 8.7.5
- 8.7.5-p1
- 8.7.6
- 8.7.6-p1
- 8.7.7
- 8.7.8
- 8.7.9
- 8.7.10
- 8.7.11
- 8.7.12
- 8.7.13
- 8.7.14
- 8.7.15
- 8.7.16
- 8.7.17
- 8.7.18
- 8.7.19
- 8.7.19-p1
- 8.7.20
- 8.7.21
- 8.7.22
- 8.7.23
- 8.7.24
- 8.7.25
- 8.7.26
- 8.7.26-p1
- 8.7.27
- 8.7.27-p1
- 8.7.28
- 8.7.29
- 8.7.29-p1
- 8.7.30
- 8.7.31
- 8.7.32
- 8.7.33
- 8.7.33-p2
- 8.7.34
- 8.7.35
- 8.7.36
- 8.7.37
- 8.7.38
- 8.7.39
- 8.7.40
- 8.7.41
- 8.7.42
- 8.8.1
- 8.8.2
- 8.8.3
- 8.8.4
- 8.8.5
- 8.8.6
- 8.8.7
- 8.8.8
- 8.8.9
- 8.8.10
- 8.8.11
- 8.8.12
- 8.8.13

### Known Limitations

#### Jetty Configuration Incompatibility in GridGain 8.7.21 and Later

If you are upgrading from version 8.7.20 or earlier, consider an incompatibility issue related to Jetty configuration introduced in GridGain 8.7.21.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration that enables SSL for REST
- Your Jetty configuration uses the `org.eclipse.jetty.util.ssl.SslContextFactory` class
- The keystore specified in the Jetty configuration contains both the CA certificate and the private certificate

In this case, after starting a new version, an exception is thrown with an error message similar to the following:

```text
java.lang.IllegalStateException: KeyStores with multiple certificates are not supported on the base class
org.eclipse.jetty.util.ssl.SslContextFactory. (Use org.eclipse.jetty.util.ssl.SslContextFactory$Server
or org.eclipse.jetty.util.ssl.SslContextFactory$Client instead)
```

To workaround this issue, alter the Jetty configuration to use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` or `org.eclipse.jetty.util.ssl.SslContextFactory$Client`. See the configuration example at the [Client Certificate Authentication](https://www.gridgain.com/docs/latest/administrators-guide/security/authentication#client-certificate-authentication) page.

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and Later

In GridGain 8.7.26, the default value of the property `IgniteConfiguration.rebalanceThreadPoolSize` changed from `1` to `min(4, number of CPU / 4)`. It may cause a compatibility issue under the following conditions:

- When a Rolling Upgrade is performed
- The upgrade is performed from 8.5.7 version (or earlier) to 8.5.x or from 8.7.3 (or earlier) to 8.7.x
- The server nodes have at least 8 CPU cores
- The nodes configuration does not have the property `IgniteConfiguration.rebalanceThreadPoolSize`, so the default value is used

In this case, an exception is thrown with an error message similar to the following:

```text
сlass org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
Different values of such parameter may lead to rebalance process instability and hanging.  [rmtNodeId=5fc58fb7-209d-489a-8034-0127a81abed6, locRebalanceThreadPoolSize = 4, rmtRebalanceThreadPoolSize = 1]
```

To workaround this issue, change the configuration of the server nodes to `rebalanceThreadPoolSize=1` so that it matches the previous default configuration. For example:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="rebalanceThreadPoolSize" value="1"/>

    <!-- The rest of the configuration goes here -->
</bean>
```

#### Jetty Doesn't Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect. Starting this version, errors in the configuration will lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

You will need to fix the custom Jetty configuration before upgrading.

#### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

Starting from 8.7.31 version, GridGain no longer attempts to automatically enable the remote JMX. Default settings are known to cause issues if customized (for example, secure the connection). Also, in most cases, remote JMX is not required since many tools use local JMX connections (not using TCP).

Your setup may be affected if:

- You start GridGain nodes via `ignite.sh` script
- You connect to GridGain nodes' JMX interface remotely over TCP using the default configuration

To continue using remote JMX, you need to manually specify the required JMX settings. Please see the example below. Note that you don't need remote JMX if you use a local connection, such as connecting JConsole to a GridGain process on the same host.

```bash
export JVM_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=33333 \
    -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"

bin/ignite.sh
```

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
