---
description: >-
  GridGain 8.7.28 adds .NET thin client transactions, a Java thin client async API, and SFTP snapshot storage, plus many fixes across integrations, thin clients, and data replication.
hidden: true
---

# GridGain 8.7.28 Release Notes

## New Features

### .NET Thin Client Transactions
GridGain.NET Thin Client can now perform multiple cache operations atomically with the Transaction API.

{% code title="Explicit GridGain transaction" %}
```csharp
var cfg = new IgniteClientConfiguration { ... };
IIgniteClient client = Ignition.StartClient(config);
ICacheClient<int, int> cache = client.GetOrCreateCache<int, int>("foo");

using (var tx = client.GetTransactions().TxStart(
    TransactionConcurrency.Optimistic,
    TransactionIsolation.Serializable))
{
    if (cache.TryGet(1, out var val))
        cache[1] = val + 10;
    else
        cache[1] = 20;

    tx.Commit();
}
```
{% endcode %}

{% code title="Ambient TransactionScope" %}
```csharp
var cfg = new IgniteClientConfiguration { ... };
IIgniteClient client = Ignition.StartClient(config);
ICacheClient<int, int> cache = client.GetOrCreateCache<int, int>("foo");

using (var tx = new TransactionScope(
    TransactionScopeOption.Required,
    new TransactionOptions {IsolationLevel = IsolationLevel.Serializable}))
{
    if (cache.TryGet(1, out var val))
        cache[1] = val + 10;
    else
        cache[1] = 20;

    tx.Complete();
}
```
{% endcode %}

See [documentation](https://www.gridgain.com/docs/latest/developers-guide/key-value-api/transactions) for more details on GridGain transactions.

### Java Thin Client Async API
GridGain Thin Client now provides async counterparts for most of the APIs.
Async methods return `IgniteClientFuture<T>` interface, which extends `Future<T>` and `CompletionStage<T>`.

{% code title="Chain multiple asynchronous operations with `CompletionStage`" %}
```java
IgniteClient client = Ignition.startClient(...);

client.<Integer, String>createCacheAsync("some-cache")
        .thenCompose(cache -> cache.getAsync(1))
        .thenAccept(cacheVal -> System.out.println("Cache value: " + cacheVal));
```
{% endcode %}

{% code title="Blocking wait" %}
```java
IgniteClient client = Ignition.startClient(...);

IgniteClientFuture<Collection<String>> future = client.cacheNamesAsync();
Collection<String> cacheNames = future.get();
```
{% endcode %}

### Use SFTP to store snapshots
Snapshots API has been expanded to support SFTP as remote centralized storage for snapshot drives. This is helpful when mounting the remote storage as a network drive is not possible.

Supported operations: `copy`, `move`, `check`, `list`, `restore`, `recoveryTo`.

{% code title="Enabling access to SFTP server with SSL keys via XML configuration" %}
```xml
<property name="pluginConfigurations">
  <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
    <property name="snapshotConfiguration">
      <bean class="org.gridgain.grid.configuration.SnapshotConfiguration">
          <property name="sftpConfiguration">
              <!-- Enabling SFTP storage with SSL keys access. -->
              <bean class="org.gridgain.grid.persistentstore.snapshot.file.SftpConfiguration">
                  <!-- JKS path. -->
                  <property name="keyPath" value="path" />

                  <!-- JKS passphrase(optional). -->
                  <property name="passphrase" value="password" />
              </bean>
          </property>
      </bean>
    </property>
  </bean>
</property>
```
{% endcode %}

{% code title="Enabling access to SFTP server with SSL keys via java configuration" %}
```java
new IgniteConfiguration()
    .setPluginConfigurations(
        new GridGainConfiguration()
            .setSnapshotConfiguration(
                new SnapshotConfiguration()
                    .setSftpConfiguration(
                        new SftpConfiguration()
                            .setKeyPath("storage/key.jks")
                            .setPassphrase("secret"))));
```
{% endcode %}

{% code title="Unified java API for snapshot operations" %}
```java
SnapshotPath sftpDestWithKey = SnapshotPath.sftp()
    .uri(new URI("sftp://login@address:port/relativePath"))
    .keyAlias("keyAlias")// Alias to get sftp key from JKS
    .build();
SnapshotPath sftpDestWithLoginPassword = SnapshotPath.sftp()
    .uri(new URI("sftp://login:password@address:port/relativePath"))
    .build();
SnapshotPath fsDest = SnapshotPath.file()
    .path(new File(path))
    .build();

Ignite ignite;
GridGain gridgain = ignite.plugin(GridGain.PLUGIN_NAME);
GridSnapshot snapshotFacade = gridgain.snapshot();

// Copy example
snapshotFacade.copy(
    new CopySnapshotParams()
        .snapshotId(snapshotId)
        .destinationPath(sftpDestWithKey)
        .chainMode(SnapshotChainMode.SINGLE)
        .singleFileCopy(true)
    ).get();

// Move example
snapshotFacade.move(
    new MoveSnapshotParams()
        .snapshotId(snapshotId)
        .destinationPath(sftpDestWithKey)
        .chainMode(SnapshotChainMode.SINGLE)
        .singleFileCopy(true)
    ).get();

// Check example
snapshotFacade.check(
    new CheckSnapshotParams()
        .snapshotId(arg.getSnapshotId())
        .optionalSearchPaths(Arrays.asList(sftpDestWithKey, sftpDestWithLoginPassword, fsDest))
        .forceRestore(arg.isForce())
        .cacheNames(arg.getCacheNames())
        .skipCrc(arg.isSkipCrc())
        .message(arg.getMessage())
    ).get();

// Check example
snapshotFacade.check(
    new CheckSnapshotParams()
        .snapshotId(arg.getSnapshotId())
        .optionalSearchPaths(Arrays.asList(sftpDestWithKey, sftpDestWithLoginPassword, fsDest))
        .forceRestore(arg.isForce())
        .cacheNames(arg.getCacheNames())
        .skipCrc(arg.isSkipCrc())
        .message(arg.getMessage())
    ).get();

// List example
snapshotFacade.list(
    new ListSnapshotParams()
        .optionalSearchPaths(Arrays.asList(sftpDestWithKey, sftpDestWithLoginPassword, fsDest))
    ).get();

// Restore example
snapshotFacade.restore(
    new RestoreSnapshotParams()
        .snapshotId(snapshotId)
        .optionalSearchPaths(Arrays.asList(sftpDestWithKey, sftpDestWithLoginPassword, fsDest))
    ).get();

// Enterprise Edition
GridSnapshotEx pitrSnapshotFacade = (GridSnapshotEx)snapshotFacade;
// Recovery to example
pitrSnapshotFacade.recoveryTo(
    new RecoveryParams()
        .time(p.time)
        .message("recovery done")
        .optionalSearchPaths(Arrays.asList(sftpDestWithKey, sftpDestWithLoginPassword, fsDest))
    ).get();
```
{% endcode %}

{% code title="Snapshot-util API" %}
```shell
# Key alias may be provided in additional parameter.
# In this case all sftp destinations will try to use this key alias.
snapshot-utility.sh move -id=123456 -dest=sftp://login@address:port/relativePath -key_alias=keyAlias
snapshot-utility.sh copy -id=123456 -dest=sftp://login:password@address:port/relativePath
snapshot-utility.sh list -src=sftp://login@address:port/relativePath -key_alias=keyAlias
snapshot-utility.sh restore -src=sftp://login@address:port/relativePath -key_alias=keyAlias
```
{% endcode %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30933 | GridGain Integrations | Upgraded Spring Core 4.3.25 to 4.3.29, Spring Core 5.0.17 to 5.0.19, Spring Data 1.13.14 to 1.13.23 |
| GG-30929 | GridGain Integrations | netty is upgraded from 4.1.42 in ignite-cassandra and 4.1.51 in ignite-zookeeper to 4.1.52 |
| GG-30927 | Cluster Storage Engine | Fixed memory leak introduced in 8.7.25 manifesting itself when caches with unique names are created and then destroyed |
| GG-30917 | Cluster Continuous Queries | Fixed an issue where Continuous Query deployment, after client node reconnection with the new node id, could lead to remote nodes failure when peer class loading is enabled, and remote nodes don't have a remote filter in the classpath. |
| GG-30878 | Platforms & Thin Clients | Java Thin Client: Added asynchronous methods to Cache API, Compute API and `IgniteClient` interface |
| GG-30868 | Platforms & Thin Clients | Added Transaction API to .NET thin client |
| GG-30851 | Platforms & Thin Clients | Improved server performance for a case when there are a lot of thin client connections |
| GG-30818 | Cluster Control Script | New command '--property' is added to manage distributed properties by command line interface |
| GG-30816 | Control Center Agent | Fixed a bug in the Control Center Agent when it does not try to reconnect to the Control Center if there is no answer on heartbeat. |
| GG-30754 | Platforms & Thin Clients | Fixed "Unsupported protocol version" exception when getting cache configuration from Java thin client. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30817 | Cluster Data Replication | Introduced a property `DrReceiverConfiguration.lazyBinaryMetadataRegistration`: if set to false (default), all binary types from the sender cluster will be registered on the receiver; if set to true, only the types of the values actually replicated will be registered; the latter is useful when some of the caches don't take part in the replication. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30841 | Cluster Snapshot Utility | Improved error output of the `snapshot` command. |
| GG-30814 | Cluster Data Snapshots and Recovery | Added ability to use remote SFTP server to store snapshots. Java API for snapshots was updated. |

## Installation and Upgrade Information
See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`,
`8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`,
`8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`,
`8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`,
`8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`

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
