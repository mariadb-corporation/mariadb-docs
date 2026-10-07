---
description: >-
  GridGain 8.7.27 adds Service APIs for the Java and .NET thin clients and a Java thin client cluster API, along with SQL, communication, and snapshot fixes.
hidden: true
---

# GridGain 8.7.27 Release Notes


## New Features

### Java Thin Client Service API
Java thin clients can invoke GridGain Services that are deployed to the cluster from servers or thick clients.

{% code title="Deploying Ignite service from a server node" %}
```java
public class FooService implements Service {
    // Service interface omitted
    public int addOne(int x) {
        return x + 1;
    }
}

...

ignite.services().deployNodeSingleton("foo", new FooService());
```
{% endcode %}

{% code title="Invoking Ignite service from a thin client (no code is shared)" %}
```java
public interface FooService {
    int addOne(int x);
}

...

FooService svc = client.services().serviceProxy("foo", FooService.class);
svc.addOne(1);
```
{% endcode %}

### Java Thin Client Cluster API
Java thin client now has an API to inspect the Ignite cluster, control cluster state, enable or disable write-ahead 
logging, and restrict Compute or Service calls to custom cluster groups. 

{% code title="Inspecting the cluster" %}
```java
// Get client and server node count
ClientCluster cluster = client.cluster();

int clients = cluster.forClients().nodes().size();
int servers = cluster.forServers().nodes().size();

// List all nodes with start time and CPU count
Collection<ClusterNode> nodes = cluster.nodes();
for (ClusterNode node : nodes) {
    ClusterMetrics metrics = node.metrics();
    
    System.out.println(
            "Node " + node.id() +
            " started at " + metrics.getNodeStartTime() +
            ", CPUs: " + metrics.getTotalCpus());
}
```
{% endcode %}

{% code title="Changing the cluster state" %}
```java
// Activate the cluster
client.cluster().state(ClusterState.ACTIVE);

// Enable WAL for Person cache
client.cluster().enableWal("Person");
```
{% endcode %}

{% code title="Invoking Compute and Services on a specific set of nodes" %}
```java
// Get server nodes with user attribute "foo" set to "bar"
ClientClusterGroup clusterGroup = client.cluster()
    .forServers()
    .forAttribute("foo", "bar");

// Invoke "MyTask" compute task using only the nodes from the specified cluster group
client.compute(clusterGroup).execute("org.foo.bar.MyTask", null);

// Invoke "my-service" service method using only the nodes from the specified cluster group
client.services(clusterGroup).serviceProxy("my-service", MyService.class).fooBar();
```
{% endcode %}

### .NET Thin Client Service API
GridGain.NET thin clients can invoke services that are deployed to the cluster from servers or thick clients.
Services can be deployed from .NET or Java code.

{% code title="Deploying GridGain service from a server node" %}
```csharp
public class FooService : IService {
    // Service interface omitted
    public int AddOne(int x) => x + 1;
}

...

ignite.GetServices().DeployNodeSingleton("foo", new FooService());
```
{% endcode %}

{% code title="Invoking GridGain service from a thin client (no code is shared)" %}
```csharp
public interface IFooService {
    int AddOne(int x);
}

...

IFooService svc = client.GetServices().GetServiceProxy<IFooService>("foo");
svc.AddOne(1);
```
{% endcode %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30633 | SQL | Fixed the issue when Ignite JDBC drivers return metadata with invalid information about actual capabilities |
| GG-30166 | Communication | Added an ability to avoid opening of server TCP socket on client nodes. |
| GG-28196 | Atomic Cache | Client nodes no longer require CacheInterceptor classes to be present locally if they don't use the cache in question |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30484 | Snapshots & PITR | Fixed an issue when a Point-in-Time Recovery could not be completed due to a loss of an unrelated WAL segment |
| GG-29913 | RU | Fixed an issue causing errors on upgrading from 8.5 `<TBD>` |

## Installation and Upgrade Information
See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`,
`8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`,
`8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`,
`8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`,
`8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`

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
