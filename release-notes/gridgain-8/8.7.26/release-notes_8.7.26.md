---
description: >-
  GridGain 8.7.26 introduces memory warm-up from native persistence, tracing of cache operations and transactions, C++ thin client transactions, and .NET service invocation from Java, plus many fixes.
hidden: true
---

# GridGain 8.7.26 Release Notes


## New Features

This release introduces several notable features and new capabilities.

### Memory Warm-up on Restarts from Native Persistence
Starting with this release you can warm up your RAM with the data from Native Persistence upon restarts. This feature
is useful for latency-sensitive use cases when you prefer having all data loaded into RAM before the node
starts processing application load.

{% code title="Enabling memory warm-up via XML configuration" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
	<property name="dataStorageConfiguration">
	    <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
		<property name="defaultWarmUpConfiguration">
		    <bean class="org.apache.ignite.configuration.NoOpWarmUpConfiguration"/>
		</property>
		<property name="defaultDataRegionConfiguration">
		    <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
		        <property name="warmUpConfiguration">
		            <bean class="org.apache.ignite.configuration.LoadAllWarmUpConfiguration"/>
		        </property>
		    </bean>
		</property>
	    </bean>
	</property>
</bean>
```
{% endcode %}

{% code title="Enabling memory warm-up via Java configuration" %}
```java
new IgniteConfiguration()
    .getDataStorageConfiguration()
    .setDefaultWarmUpConfiguration(new NoOpWarmUpConfiguration())

    .getDefaultDataRegionConfiguration()
    .setWarmUpConfiguration(new LoadAllWarmUpConfiguration());
```
{% endcode %}

### Tracing of Cache Operations and Specific Transactions
The release introduces new **experimental** tracing-related features.

- Tracing specific transactions - use the facade returned by the `withTracing()` function to specify which transactions
to add to the tracing scope.

{% code title="Enabling tracing of a specific transaction" %}
```java
try (Transaction tx = ignite.transactions().withLabel("user-label").withTracing().txStart(PESSIMISTIC, SERIALIZABLE)) {
    cache.putAll(entries);

    tx.commit();
}
```
{% endcode %}

- Tracing of caching APIs - trace the execution of updates, reads, and deletes performed via the caching APIs. Presently,
the feature is available for `ATOMIC` caches only.

{% code title="Enabling tracing of reads, updates and deletes" %}
```shell
control.sh --tracing-configuration set --scope CACHE_API_WRITE --sampling-rate 0.01 --included-scopes COMMUNICATION,EXCHANGE
control.sh --tracing-configuration set --scope CACHE_API_READ --sampling-rate 0.01 --included-scopes COMMUNICATION,EXCHANGE
```
{% endcode %}

### Transactions Support by C++ Thin Client
The C++ thin client now supports the transactional API. You can execute distributed transactions in various configuration
modes by selecting required isolation levels and concurrency modes.

{% code title="Using transactions with the C++ Thin Client" %}
```cpp
#include <ignite/thin/ignite_client.h>

using namespace ignite;

void Example(IgniteClient client) {
    cache::CacheClient<int, int> cache = client.GetOrCreateCache<int, int>("example");

    transactions::ClientTransactions transactions = client.ClientTransactions();

    cache.Put(1, 1);
    assert(1 == cache.Get(1));

    transactions::ClientTransaction tx = transactions.TxStart();

    cache.Put(1, 10);
    assert(10 == cache.Get(1));

    tx.Rollback();
    assert(1 == cache.Get(1));
}
```
{% endcode %}

### Ignite .NET Services Invocation from Java
GridGain.NET services can now be invoked from a Java application. New `PlatformServiceMethod` annotations provide
control over method name mapping.

{% code title="Creating a service in .NET" %}
```csharp
public class DotnetService : IService
{
    public int AddOne(int x) => x + 1;

    // IService implementation omitted
}

...

Ignite.GetServices().DeployClusterSingleton("dotnet-service", new DotnetService());
```
{% endcode %}

{% code title="Calling the .NET service from Java" %}
```java
public interface DotnetService
{
    @PlatformServiceMethod("AddOne") // Map to different naming convention
    int addOne(int x);
}

...

DotnetService svc = ignite.services().serviceProxy("dotnet-service", DotnetService.class, false);
int y = svc.addOne(5);
```
{% endcode %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30728 | SQL | Reverted some of the changes introduced in GG-30669 to resolve a performance degradation for specific SQL requests. |
| GG-30693 | SQL | Fixed a possible deadlock when multiple caches are being destroyed simultaneously. |
| GG-29288 | SQL | Fixed the H2 dependency clash that happened when other libraries such Spring were trying to include a different version of H2. |
| GG-30493 | Storage | Fixed a race condition between the node termination and partition clearing activities. |
| GG-23445 | Storage | Added the ability to pre-load data from Ignite persistence in memory after restarts. |
| GG-30689 | Transactions | Fixed the compatibility test suite after introducing the changes of GG-30669. |
| GG-30626 | Transactions | Fixed the compatibility test suite after introducing the changes of GG-30509. |
| GG-30616 | Transactions | Deprecated and stopped using the IGNITE_CACHE_KEY_VALIDATION_DISABLED system property. |
| GG-29064 | Transactions | The transaction recovery time has been optimized. |
| GG-30669 | Rebalancing | Fixed the issue that could cause a partition inconsistency during rebalancing.<br>The case could take place when entry relocation and entry deletion happen simultaneously. |
| GG-30579 | Rebalancing | Added additional details about the rebalancing progress with the details being printed to the log files. |
| GG-30509 | Rebalancing | Introduced several optimizations that accelerate the rebalancing process for certain scenarios. |
| GG-30650 | PME | Fixed an issue that could cause a cluster hung when the thin client was trying to connect with security enabled. |
| GG-30641 | Thin Clients & Platforms | Supported transactional APIs for thin clients. |
| GG-30560 | Thin Clients & Platforms | NET: Fixed the issue that could cause a query to return an incorrect result due to<br>an empty topology projection. A client node was not updating the local node info after reconnecting to the cluster. |
| GG-30391 | Thin Clients & Platforms | Added the ability to execute an Ignite .NET service from Java. |
| GG-30639 | Management & Monitoring | Fixed the issue when the Control Center Agent of an unsupported protocol version tried<br>to establish a connection with Control Center endlessly. |
| GG-30395 | Management & Monitoring | Added cache names and the number of keys metric to transaction tracing spans. |
| GG-30140 | Management & Monitoring | The Control Center Agent no longer attempts to collect metrics of disconnected clusters. |
| GG-28493 | Management & Monitoring | Added the ability to enable tracing of a specific transaction with the help of a transaction facade returned by the `withTracing()` method. |
| GG-26627 | Management & Monitoring | Added the API to check nodes' interconnection. Use the `control.sh --diagnostic connectivity` command to check the network connectivity. |
| GG-21042 | Management & Monitoring | Supported tracing of the updates and deletes executed via the cache APIs (experimental, available for atomic caches only). |
| GG-21041 | Management & Monitoring | Supported tracing of the read operations executed via the cache APIs (experimental, available for atomic caches only). |
| GG-30675 | Integrations | The AWS sdk version was updated for the `ignite-aws` to 1.11.851 to address the CVE-2020-24616 vulnerability. |
| GG-30597 | Integrations | Hibernate 5.3 is upgraded from 5.3.7 to 5.3.18 to address the CVE-2019-14900 vulnerability. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30129 | Snapshots & PITR | Supported the point-in-time recovery from an SFTP location. |

## Installation and Upgrade Information
See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information
about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`,
`8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`,
`8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`,
`8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`,
`8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`

### Known Limitations

#### Jetty configuration incompatibility in GridGain 8.7.21 and later

If you are upgrading from version 8.7.20 or earlier, you must take into account an incompatibility related to Jetty configuration, which was introduced in GridGain 8.7.21.

Your setup may be affected if:

- You're using the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration that enables SSL for REST
- Your Jetty configuration uses the `org.eclipse.jetty.util.ssl.SslContextFactory` class
- The keystore specified in the Jetty configuration contains both the CA certificate and the private certificate

In this case, after starting the new version, you'll see an error similar to:

```text
java.lang.IllegalStateException: KeyStores with multiple certificates are not supported on the base class
org.eclipse.jetty.util.ssl.SslContextFactory. (Use org.eclipse.jetty.util.ssl.SslContextFactory$Server
or org.eclipse.jetty.util.ssl.SslContextFactory$Client instead)
```

To workaround this issue, you need to alter the Jetty configuration to use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` or `org.eclipse.jetty.util.ssl.SslContextFactory$Client`.
For a configuration example, see [Client Certificate Authentication](https://www.gridgain.com/docs/latest/administrators-guide/security/authentication#client-certificate-authentication).

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and later

In GridGain 8.7.26, the default value of the property `IgniteConfiguration.rebalanceThreadPoolSize` has changed from `1` to `min(4, number of CPU / 4)`.
It may cause a compatibility issue under the following conditions:

- A Rolling Upgrade is being performed
- The upgrade is performed from a version 8.5.7 or earlier for 8.5.x, or 8.7.3 or earlier for 8.7.x
- The server nodes have at least 8 CPU cores
- The nodes configuration don't have the property `IgniteConfiguration.rebalanceThreadPoolSize` set (i.e. the default value is used)

In this case, you'll see an error similar to

```text
сlass org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
Different values of such parameter may lead to rebalance process instability and hanging.  [rmtNodeId=5fc58fb7-209d-489a-8034-0127a81abed6, locRebalanceThreadPoolSize = 4, rmtRebalanceThreadPoolSize = 1]
```

To workaround this issue, you need to change the configuration of the server nodes to set `rebalanceThreadPoolSize=1` so that it matches
the old default. Example:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="rebalanceThreadPoolSize" value="1"/>

    <!-- The rest of the configuration goes here -->
</bean>
```

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
