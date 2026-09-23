---
description: >-
  Reference for GridGain 9 per-node configuration parameters, including network,
  storage, compute, RAFT, REST, and system settings and how to apply them.
---

# Node Configuration Parameters

Node configuration is individual for each node and is not shared across the whole cluster.

In GridGain 9, you can create and maintain configuration in either HOCON or JSON. The configuration file has a single root "node," called `ignite`. All configuration sections are children, grandchildren, etc., of that node.

## Setting Initial Node Configuration

GridGain node configuration is separated between two sections.

- When node starts, it reads the contents of the `{GRIDGAIN_HOME}/etc/vars.env` file to set baseline node properties. Based on the contents of this file, node name is set, folders to store data are designated and JVM is configured. This configuration can only be changed by modifying the `vars.env` file and restarting the node.
- Once node is started, it reads the contents of the `{GRIDGAIN_HOME}/etc/gridgain-config.conf` file to set node properties. This configuration can be modified via CLI tool as described below.

## Checking Node Configuration

To get node configuration, use the CLI tool.

- Start the CLI tool and connect to the node.
- Run the `node config show` command.

The CLI tool will print the full node configuration. If you only need a part of the configuration, you can narrow down the search by providing the properties you need as the command argument, for example:

```bash
node config show ignite.clientConnector
```

## Changing Node Configuration

Node configuration is changed from the CLI tool. You can update it both in the interactive (REPL) and non-interactive mode by passing a configuration file with the `--file` parameter.

{% hint style="info" %}
Values set directly via the CLI take precedence over values set in the configuration file.
{% endhint %}

### Update via REPL:

- Start the CLI tool and connect to the node. This becomes the "default" node for subsequent CL commands.
- To update the default node's configuration, run the `node config update` command and provide the update as the command argument, for example:

  ```bash
  node config update ignite.clientConnector.connectTimeoutMillis=10000
  ```
- To update the configuration of a node other than the default one, run the `node config update` command with the target node explicitly specified. For example, for node named `node1`:

  ```bash
  node config update -n node1 ignite.userAttributes.clientConnector="10900"
  ```
- To update one or more parameters, pass the configuration file to the `node config update` command:

  ```bash
  node config update --file ../gridgain-config.conf
  ```
- You also can update the configuration combining both approaches:

  ```bash
  node config update --file ../gridgain-config.conf ignite.system.idleSafeTimeSyncIntervalMillis=600
  ```
- Restart the node to apply the configuration changes.

### Update via Non-Interactive Mode

You also can update the configuration [without](../cli-tool.md#non-interactive-cli-mode) starting the CLI.

- Pass the configuration file with the `--file` parameter:

  ```bash
  bin/gridgain9 node config update --file ../gridgain-config.conf
  ```
- Restart the node to apply the configuration changes.

You can also modify cluster configuration via [non-interactive](../cli-tool.md#non-interactive-cli-mode) CLI mode without starting the CLI tool first.

## Exporting Node Configuration

If you need to export node configuration to a HOCON-formatted file, use the following command:

```bash
bin/gridgain9 node config show > node-config.conf
```

## Configuration Parameters

### Client Connector Configuration

```json
{
  "ignite": {
    "clientConnector": {
      "connectTimeoutMillis": 10000,
      "idleTimeoutMillis": 0,
      "listenAddresses": [],
      "metricsEnabled": true,
      "port": 10800,
      "sendServerExceptionStackTraceToClient": false,
      "ssl": {
        "ciphers": "",
        "clientAuth": "none",
        "enabled": false,
        "keyStore": {
          "password": "********",
          "path": "",
          "type": "PKCS12"
        },
        "trustStore": {
          "password": "********",
          "path": "",
          "type": "PKCS12"
        }
      }
    }
  }
}
```

See the [Clients](../../developers-guide/clients/overview.md) section for more information on configuring the client connector.

### Compute Configuration

```json
{
  "ignite" : {
    "compute" : {
      "queueMaxSize" : 2147483647,
      "statesLifetimeMillis" : 60000,
      "threadPoolSize" : 10,
      "wasm" : {
        "moduleMaxMemory" : "64m",
        "enableCompiler" : true,
        "moduleCache" : {
          "enabled" : true,
          "maxSize" : 10,
          "expireAfterAccessSeconds" : 5,
          "expireAfterWriteSeconds" : 6
         }
      },
      "dotnet" : {
        "serverGc" : true,
        "executorPath" : "",
        "gcHeapHardLimit" : "",
        "gcHeapHardLimitPercent" : 0
      }
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|queueMaxSize|2147483647|Maximum number of compute tasks in queue.|Yes|Yes|1 - Integer.MAX_VALUE|
|statesLifetimeMillis|60000|The lifetime of job states after the job finishes, in milliseconds.|Yes|Yes|0 - inf|
|threadPoolSize|10|The number of threads available to compute jobs.|Yes|Yes|1 - Integer.MAX_VALUE|
|wasm.moduleMaxMemory|64m|The maximum amount of memory that can be allocated to a single WebAssembly module. Always rounded to the nearest multiple of 65536 bytes.|Yes|Yes|1 - Integer.MAX_VALUE|
|wasm.enableCompiler|true|Defines if the WebAssembly module [compiles code](https://chicory.dev/docs/usage/runtime-compiler) or uses an interpretator.|Yes|Yes|true, false|
|wasm.moduleMaxMemory|8|Maximum linear memory per module instance. Use data-size suffixes (e.g., 8m).|Yes|Yes|1 - Integer.MAX_VALUE|
|wasm.moduleCache.enabled|true|Turns on module instance caching to avoid repeated load and initialize cycles.|Yes|Yes|true, false|
|wasm.moduleCache.maxSize|10|Upper bound on cached instances.|Yes|Yes|1 - Integer.MAX_VALUE|
|wasm.moduleCache.expireAfterAccessSeconds.|5|Evicts an entry if it has not been accessed for the configured number of seconds.|Yes|Yes|0 - inf|
|wasm.moduleCache.expireAfterWriteSeconds|6|Evicts an entry a fixed number of seconds after creation/update.|Yes|Yes|0 - inf|
|dotnet.serverGc|true|Enables .NET Server GC mode for the .NET compute executor (sidecar) process. Sets the `DOTNET_gcServer` environment variable.|Yes|Yes|true, false|
|dotnet.executorPath|(empty)|Path to the directory that contains the .NET compute executor binaries. An empty string resolves the location automatically relative to the GridGain installation; set it explicitly when automatic resolution fails, for example in a fat JAR or other non-standard deployment.|Yes|Yes|Filesystem path or empty|
|dotnet.gcHeapHardLimit|(empty)|Absolute hard memory limit for the .NET sidecar process, as a number followed by a `k`, `m`, or `g` suffix. An empty string means no limit. Sets `DOTNET_GCHeapHardLimit`.|Yes|Yes|Data-size string or empty|
|dotnet.gcHeapHardLimitPercent|0|Relative hard memory limit for the .NET sidecar process, as a percentage of total physical memory. `0` means no limit.|Yes|Yes|0 - 100|
|`dotnet.env.<NAME>`|(empty)|Additional environment variables passed to the .NET sidecar process, specified as named entries (for example, `dotnet.env.MY_VAR` = `value`).|Yes|Yes|Any string|

### Code Deployment Configuration

```json
{
  "ignite" : {
    "deployment" : {
      "location" : "deployment",
      "tempLocation" : "deployment/tmp"
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|location|deployment|Relative path to folder in the working directory. All deployment units content will be stored there.|Yes|No|A valid path|
|tempLocation|None|Relative path to the folder used for storing temporary files needed for code deployment. Must be writable and have sufficient space.|Yes|Yes|A valid path.|

### Failure Handler Configuration

```json
{
  "ignite" : {
    "failureHandler": {
      "dumpThreadsOnFailure" : true,
      "dumpThreadsThrottlingTimeoutMillis" : 10000,
      "handler" : {
        "ignoredFailureTypes" : [
          "systemWorkerBlocked", "systemCriticalOperationTimeout"
        ],
        "type" : "stop"
      },
      "oomBufferSizeBytes" : 16384
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|dumpThreadsOnFailure|true|The number of items that can be expired at once.|Yes|No|true, false|
|dumpThreadsThrottlingTimeoutMillis|10000|Throttling timeout for thread dump generation during failure handling, in milliseconds.|Yes|No|1 - inf|
|handler.ignoredFailureTypes|[systemWorkerBlocked, systemCriticalOperationTimeout]|Types of failures that will be ignored. Possible values:<br>- `systemWorkerTermination` - system worker thread was unexpectedly terminated;<br>- `systemWorkerBlocked` - system worker thread has not updated its heartbeat for longer than the configured threshold;<br>- `criticalError` - an unrecoverable error that renders the system inoperable;<br>- `systemCriticalOperationTimeout` - system-critical operation has exceeded its allowed execution time.|Yes|No|systemWorkerTermination, systemWorkerBlocked, criticalError, systemCriticalOperationTimeout|
|handler.type|stop|Failure handler configuration type. Possible values:<br>- `noop` - handler will write the error to log and perform no other operations;<br>- `stop` - handler will stop the node if an error occurs;<br>- `stopOrHalt` - If `tryStop` is set to `false` (default), the handler will immediately stop the process. If `tryStop` is set to `true`, the handler will attempt to gracefully stop the node if an error occurs, and if the node is not stopped after `timeoutMillis`, it will kill the process.|Yes|No|noop, stop, stopOrHalt|
|tryStop|false|If `true` and the `stopOrHalt` is set, failure handler will attempt to stop the node before killing the node process. Can only be specified for `stopOrHalt` failure handler.|Yes|No|true, false|
|timeoutMillis|0|The time in milliseconds for which the `stopOrHalt` failure handler will wait for the node to stop. Can only be specified for `stopOrHalt` failure handler.|Yes|No|1 - inf|
|oomBufferSizeBytes|16384|Amount of memory reserved in the heap at node start, in bytes.|Yes|No|1 - inf|

### Import and Export Configuration

Controls server-side file and object-store access for the SQL `COPY` command.

```json
{
  "ignite": {
    "importExport": {
      "fileAccessEnabled": false,
      "importRoots": [],
      "allowedS3Buckets": [],
      "allowedS3Endpoints": [],
      "allowedIcebergClasses": [],
      "allowedCatalogUris": [],
      "maxGlobDepth": 16,
      "maxGlobFiles": 10000
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|fileAccessEnabled|false|Whether `COPY` may read from and write to filesystem paths and object-store URIs on this node. When `false`, a `COPY` statement that names a path or URI is rejected. A `COPY` between tables is unaffected.|Yes|No|`true`, `false`|
|importRoots|[]|Absolute directories that `COPY` may read from and write to. A location must resolve inside one of these directories. An empty list allows no local file access.|Yes|No|Absolute paths|
|allowedS3Buckets|[]|S3 buckets that `COPY` may read from and write to. Each entry is a bucket name or a `bucket/key-prefix`. An empty list forbids S3 access.|Yes|No|Bucket names or bucket/key prefixes|
|allowedS3Endpoints|[]|S3 endpoint overrides that `COPY` may use. Entries match by host, ignoring case, or by full URI. An allow-listed host is reachable on any port. An empty list forbids endpoint overrides.|Yes|No|Hosts or URIs|
|allowedIcebergClasses|[]|Class names that `COPY` may load reflectively for Iceberg, covering the `catalog-impl`, `io-impl`, and `client.factory` roles. An empty list forbids Iceberg access.|Yes|No|Fully qualified class names|
|allowedCatalogUris|[]|Iceberg catalog URIs for REST, JDBC, and Nessie catalogs. Entries match by host, ignoring case, or by full URI. An empty list forbids hosted catalog URIs.|Yes|No|Hosts or URIs|
|maxGlobDepth|16|Maximum directory depth the Parquet glob walk descends.|Yes|No|1 - Integer.MAX_VALUE|
|maxGlobFiles|10000|Maximum number of files the Parquet glob walk matches.|Yes|No|1 - Integer.MAX_VALUE|

### Network Configuration

This section describes how GridGain 9 nodes communicate within a cluster and expose endpoints for client and management connections.

#### Default Ports

GridGain 9 uses several network ports for inter-node communication, client access, and monitoring.

The following ports are used by GridGain 9 by default.

- `3344`: Cluster communication port
- `10300`: [HTTP REST](../rest-api/overview.md) endpoint
- `10400`: [HTTPS REST](../../security/ssl-tls.md) endpoint (**when HTTPS is enabled**)
- `10800`: Client connector ([JDBC](../../developers-guide/clients/jdbc-driver.md), [ODBC](../../developers-guide/sql/odbc/odbc-driver.md), [clients](../../developers-guide/clients/overview.md), [CLI](../cli-tool.md))
- `49000`: [Data Replication](../../gridgain9-management/migration-from-gridgain-8/dcr-from-gridgain-8.md) (DR) connector inbound port

{% hint style="info" %}
To enable the [JMX remote](https://docs.oracle.com/en/java/javase/17/management/monitoring-and-management-using-jmx-technology.html#GUID-2C1922AD-4BA0-4397-A3FE-7823F42A94A3__READY-TO-USEMONITORINGANDMANAGEMENT-0CCB777F) agent which creates a remote JMX connector to listen through the specified port, use `com.sun.management.jmxremote.port` to [set](README.md#configuration-files) the port explicitly.
{% endhint %}

#### Suspicion-Based Failure Node Detection

GridGain 9 uses `suspicionTimeout` to determine how long a suspected node is allowed to confirm liveness before it is treated as failed. The value is calculated using the following formula:

```bash
suspicionTimeout = suspicionMultiplier × ceil(log2(clusterSize + 1)) × failurePingIntervalMillis
```

#### Node Address

A node listens on the addresses in `listenAddresses` and publishes one address to the other nodes. The other nodes use the published address to connect to it. The published address is chosen as follows:

- If `advertisedAddress` is set, it is published.
- Otherwise, if `listenAddresses` is set, the listen address is published (only one listen address is supported).
- Otherwise, the node publishes the address that its host name resolves to, only if it is not mapped to a loopback or a link-local address.
- If none of the above is applicable, the node chooses one of the addresses of its network interfaces, sorted numerically, IPv4 first.

Use `advertisedAddress` and `advertisedPort` when the node is behind NAT or in a container, or when the automatic choice picks the wrong network interface.

#### Node Finder Configuration

In GridGain 9, you can choose between two node discovery types. With `STATIC` type, you manually specify the node addresses, while `MULTICAST` type automatically detects nodes on your network, making setup simpler.

- Example configuration with a `STATIC` node finder:

  ```json
  {
    "ignite": {
      "network": {
        "advertisedAddress": "",
        "advertisedPort": 0,
        "fileTransfer": {
          "chunkSizeBytes": 1048576,
          "maxConcurrentRequests": 4,
          "responseTimeoutMillis": 10000,
          "threadPoolSize": 8
        },
        "inbound": {
          "soBacklog": 128,
          "soKeepAlive": true,
          "soLinger": 0,
          "soReuseAddr": true,
          "tcpNoDelay": true
        },
        "listenAddresses": [],
        "membership": {
          "failurePingIntervalMillis": 2000,
          "membershipSyncIntervalMillis": 30000,
          "scaleCube": {
            "failurePingRequestMembers": 3,
            "gossipIntervalMillis": 200,
            "gossipRepeatMult": 3,
            "membershipSuspicionMultiplier": 5,
            "metadataTimeoutMillis": 3000
          }
        },
        "nodeFinder": {
          "type": "STATIC",
          "netClusterNodes": [
            "localhost:3344"
          ],
          "nameResolutionAttempts": 10
        },
        "outbound": {
          "soKeepAlive": true,
          "soLinger": 0,
          "tcpNoDelay": true
        },
        "port": 3344,
        "shutdownQuietPeriodMillis": 0,
        "shutdownTimeoutMillis": 15000,
        "ssl": {
          "ciphers": "",
          "clientAuth": "none",
          "enabled": false,
          "keyStore": {
            "password": "********",
            "path": "",
            "type": "PKCS12"
          },
          "trustStore": {
            "password": "********",
            "path": "",
            "type": "PKCS12"
          }
        }
      }
    }
  }
  ```
- To switch to a `MULTICAST` node finder, update the `nodeFinder` section in your configuration file to the following:

  ```json
  {
    "ignite" : {
      "network": {
        "nodeFinder": {
          "type": "MULTICAST",
          "group": "239.192.0.0",
          "port": 47401,
          "resultWaitTimeMillis": 1000,
          "ttl": -1
        }
      }
    }
  }
  ```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|advertisedAddress||Address (IP or hostname) that other nodes use to connect to this node. If empty, the address is chosen automatically. See [Node Address](#node-address).|Yes|Yes|A valid address|
|advertisedPort|0|Port that other nodes use to connect to this node. If 0, `port` is used. Applies only together with `advertisedAddress`.|Yes|Yes|0 - 65535|
|fileTransfer||File transfer configuration.||||
|fileTransfer.chunkSizeBytes|1048576|Chunk size in bytes.|Yes|Yes|1 - Integer.MAX_VALUE|
|fileTransfer.maxConcurrentRequests|4|Maximum number of concurrent requests.|Yes|Yes|1 - Integer.MAX_VALUE|
|fileTransfer.responseTimeoutMillis|10000|Node response timeout during file transfer.|Yes|Yes|0 - inf|
|fileTransfer.threadPoolSize|8|File sender thread pool size.|Yes|Yes|1 - Integer.MAX_VALUE|
|inbound||Server socket configuration. See [TCP documentation](https://man7.org/linux/man-pages/man7/tcp.7.html) and [socket documentation](https://man7.org/linux/man-pages/man7/socket.7.html) for more information.||||
|inbound.soBacklog|128|The size of the backlog.|Yes|Yes|0 - Integer.MAX_VALUE|
|inbound.soKeepAlive|true|Defines if the keep-alive packets are allowed.|Yes|Yes|true, false|
|inbound.soLinger|0|Defines how long the closed socket should linger.|Yes|Yes|0 - 65535|
|inbound.soReuseAddr|true|Defines if the address can be reused.|Yes|Yes|true, false|
|inbound.tcpNoDelay|true|Defines if the TCP no delay option is used.|Yes|Yes|true, false|
|listenAddresses||List of addresses (IPs or hostnames) to listen on. If empty, listens on all interfaces. Currently, only a single address is supported. This limitation will be lifted in a future update.|Yes|Yes|A list of valid addresses separated by comma|
|membership||Node membership configuration.||||
|membership.failurePingIntervalMillis|2000|Failure detector ping interval.|Yes|Yes|0 - inf|
|membership.membershipSyncIntervalMillis|30000|Periodic membership data synchronization interval.|Yes|Yes|0 - inf|
|membership.scaleCube||ScaleCube-specific configuration.||||
|scaleCube.failurePingRequestMembers|3|Number of members that are randomly selected by a cluster node for an indirect ping request.|Yes|Yes|1 - inf|
|scaleCube.gossipIntervalMillis|200|[Gossip](https://en.wikipedia.org/wiki/Gossip_protocol) spreading interval.|Yes|Yes|1 - inf|
|scaleCube.gossipRepeatMult|3|Gossip repeat multiplier.|Yes|Yes|1 - inf|
|scaleCube.membershipSuspicionMultiplier|5|The multiplier that is used to calculate the timeout after which the node is considered dead.|Yes|Yes|1 - inf|
|scaleCube.metadataTimeoutMillis|3000|The timeout on metadata update operation, in milliseconds.|Yes|Yes|1 - inf|
|nodeFinder||Configuration for how the node finds other nodes in the cluster.||||
|nodeFinder.type|STATIC|Node finder type. Use `STATIC` to manually configure node addresses. Use `MULTICAST` to automatically detect nodes on your network. When using this type, you must also specify a multicast group address.|Yes|Yes|STATIC|
|nodeFinder.netClusterNodes||Addresses of all nodes in the cluster in the host:port format. Applicable when `STATIC` node finder type is used.|Yes|Yes|Addresses in a valid format|
|nodeFinder.nameResolutionAttempts|10|Number of attempts to resolve a hostname to an IP address before giving up. Applicable when `STATIC` node finder type is used. 1 means no retries will be performed apart from the initial attempt.|Yes|Yes|1 - inf|
|nodeFinder.group|239.192.0.0|The multicast group address for node discovery.|Yes|Yes|Multicast address in a valid format|
|nodeFinder.port|47401|The port used for multicast.|Yes|Yes|0 - 65535|
|nodeFinder.resultWaitTimeMillis|1000|The time in milliseconds a node waits for responses after a discovery request.|Yes|Yes|1 - inf|
|nodeFinder.ttl|-1|Sets the maximum number of network hops for multicast packets. By default is set to -1 and uses the default system TTL.|Yes|Yes|-1 - 255|
|outbound||Outbound request configuration.||||
|outbound.soKeepAlive|true|Defines if the keep-alive packets are allowed.|Yes|Yes|true, false|
|outbound.soLinger|0|Defines how long the closed socket should linger.|Yes|Yes|0 - 65535|
|outbound.tcpNoDelay|true|Defines if the TCP no delay option is used.|Yes|Yes|true, false|
|port|3344|TCP port used by cluster nodes to communicate with each other.|Yes|Yes|A valid port number|
|shutdownQuietPeriodMillis|0|The period during node shutdown when GridGain ensures that no tasks are submitted for the before the node shuts itself down. If a task is submitted during this period, it is guaranteed to be accepted.|Yes|No|0 - inf|
|shutdownTimeoutMillis|15000|The maximum amount of time until the node is shut down regardless of if new network messages were submitted during `shutdownQuietPeriodMillis`.|Yes|No|0 - inf|
|ssl.ciphers|""|List of ciphers to enable, comma-separated. Empty for automatic cipher selection.|Yes|Yes|TLS_AES_256_GCM_SHA384, etc. (standard cipher ids)|
|ssl.clientAuth||Whether the SSL client authentication is enabled and whether it is mandatory.|Yes|Yes|non, optional, require|
|ssl.enabled|false|Defines if SSL is enabled for the node.|Yes|Yes|true, false|
|ssl.keyStore||SSL keystore configuration.||||
|keyStore.password|********|Keystore password.|Yes|Yes|A valid password|
|keyStore.path||Path to the keystore.|Yes|Yes|A valid path|
|keyStore.type|PKCS12|Keystore type.|Yes|Yes|PKCS12, JKS|
|ssl.trustStore||SSL trustsore configuration.||||
|trustStore.password|********|Truststore password.|Yes|Yes|A valid password|
|trustStore.path||Path to the truststore.|Yes|Yes|A valid path|
|trustStore.type|PKCS12|Truststore type.|Yes|Yes|PKCS12, JKS|

### Node Attributes

```json
{
  "ignite" : {
    "userAttributes" : {
      "region" : "US",
      "storage" : "SSD"
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|userAttributes||A collection of node attributes used for dynamically distributing data only to those nodes that have the specified attribute values.|Yes|Yes|A JSON-formatted object|
|nodeAttributes||Deprecated in 9.1.27. Use `userAttributes` instead.|Yes|Yes|A JSON-formatted object|

{% hint style="info" %}
The `ignite.nodeAttributes.nodeAttributes` section is deprecated and should not be used.
{% endhint %}

### Point-in-Time Recovery

```json
{
  "ignite" : {
    "pitr" : {
      "threadPoolSize" : 20
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|threadPoolSize|20|The number of threads dedicated to [point-in-time recovery](../../gridgain9-management/snapshots/point-in-time-recovery.md) during data restoration.|Yes|Yes|0 - inf|

### RAFT Configuration

```json
{
  "ignite" : {
    "raft" : {
        "disruptor": {
            "logManagerStripes" : 4,
            "queueSize" : 16384,
            "stripes" : 10
        },
        "fsync" : false,
        "installSnapshotTimeoutMillis" : 2147483647,
        "logStorage" : {
            "hardPartitionsDataDriveUsageLimitBytes" : 9223372036854775807,
            "hardPartitionsLogDriveUsageLimitBytes" : 9223372036854775807,
            "softPartitionsLogSizeLimitBytes" : 21474836470,
            "softPartitionsLogSpilloutSizeLimitBytes" : 21474836470
        },
        "logYieldStrategy" : false,
        "maxInflightOverflowRate" : 1.3,
        "outgoingSnapshotsThreadPoolSize" : 8,
        "responseTimeoutMillis" : 3000,
        "retryDelayMillis" : 200,
        "retryTimeoutMillis" : 10000,
        "volatileRaft" : {
            "logStorageBudget" : {
                "name" : "unlimited"
            }
        }
    }
  }
}
```

#### Hard Disk Usage Limits

The `hardPartitionsDataDriveUsageLimitBytes` and `hardPartitionsLogDriveUsageLimitBytes` properties cap the overall usage of the drives that host persistent partition data and the partitions' RAFT log, respectively. Files written by other processes on those drives also count toward the limits. Keep the following behaviors in mind when setting these values:

- **Only client writes are blocked.** When a limit is exceeded, the node rejects writes from clients, but internal system writes continue so that the cluster remains operational.
- **Reserve headroom for free space reclaim.** The mechanisms that reclaim free disk space (for example, log storage compaction) themselves consume storage while running. Set the limit far enough below total drive capacity that reclaim has room to operate once the limit is hit; otherwise the node may be unable to free space.
- **Enforcement is not instantaneous.** Each node checks its own disk usage once per second, so a few client writes can slip through after the limit is reached but before the next check. Pick a value slightly below your target so these extra writes do not eat into your reclaim headroom.
- **Writes are blocked per partition.** A client write to a partition is rejected when either the partition's RAFT leader has hit its limit, or a majority of the partition's replicas have hit their limits: in either case the write cannot be committed. A single over-limit node holding only minority replicas does not, on its own, block writes to that partition.

#### Soft Disk Usage Limits

Each node enforces two soft limits, one for each kind of partition RAFT log that lives on disk:

- `softPartitionsLogSizeLimitBytes` — combined size of RAFT log files for *persistent partitions* on the node, which write their RAFT log directly to disk.
- `softPartitionsLogSpilloutSizeLimitBytes` — combined size of RAFT log spillout files for *volatile partitions* on the node, which keep their RAFT log in memory and only spill entries to disk when the configured [log storage budget](../../architecture/storage/engines/in-memory-storage.md#log-storage-budget) is exhausted.

Both differ from the hard limits in several important ways:

- **Limits track different values.** Soft limits track only the combined size of the RAFT log files or log spillout files on the node, while hard limits track overall usage of the host drive, including files unrelated to GridGain.
- **Writes are never blocked.** When a soft limit is exceeded, client writes continue normally. The limit only triggers reactive log compaction, never admission control.
- **Scope is per-node, with separate accounting for persistent and volatile partitions.** One accounting is maintained for all persistent partitions' RAFT log on the node, and a separate one for all volatile partitions' spillout. The limit is not tracked per partition.
- **Soft and hard limits are independent.** The soft limit does not coordinate with the hard limit. If reactive compaction cannot keep up with the write rate, the hard limit will eventually trip and start rejecting client writes. Set the soft limits comfortably below the hard limits so that reclaim has time to operate before admission control engages.

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|disruptor.logManagerStripes|4|The number of disruptors for RAFT log manager.|Yes|Yes|1 - Integer.MAX_VALUE|
|disruptor.queueSize|16384|The maximum size of a queue for disruptors.|Yes|Yes|1 - Integer.MAX_VALUE|
|disruptor.stripes|10|The number of disruptor that handle the RAFT server.|Yes|Yes|1 - Integer.MAX_VALUE|
|fsync|false|Specifies whether `fsync` is used to safely write Raft log entries to disk on table partition groups before confirming replication. If set to `false`, user data may be lost in the event of an OS crash. However, a GridGain application crash will not cause data loss.|Yes|Yes|true, false|
|installSnapshotTimeoutMillis|2147483647|The maximum period allowed for transferring a RAFT snapshot to a recipient and installing it.|Yes|Yes|1 - inf|
|logStorage.hardPartitionsDataDriveUsageLimitBytes|9223372036854775807|Hard limit, in bytes, on the disk space used on the drive that hosts persistent partition data. Once exceeded, the node rejects client writes. Default is `Long.MAX_VALUE` (effectively unlimited).|Yes|No|1 - Long.MAX_VALUE|
|logStorage.hardPartitionsLogDriveUsageLimitBytes|9223372036854775807|Hard limit, in bytes, on the disk space used on the drive that hosts the partitions RAFT log. Once exceeded, the node rejects client writes. Default is `Long.MAX_VALUE` (effectively unlimited).|Yes|No|1 - Long.MAX_VALUE|
|logStorage.softPartitionsLogSizeLimitBytes|21474836470|Soft limit, in bytes, on the total size of all persistent partitions' RAFT log storage files. Once exceeded, log storage compaction is triggered to reclaim disk space.|Yes|No|1 - Long.MAX_VALUE|
|logStorage.softPartitionsLogSpilloutSizeLimitBytes|21474836470|Soft limit, in bytes, on the total size of all volatile partitions' RAFT log spillout files. Once exceeded, log storage compaction is triggered to reclaim disk space.|Yes|No|1 - Long.MAX_VALUE|
|logYieldStrategy|false|If true, the non-blocking strategy is used in the Disruptor of log manager.|Yes|Yes|true, false|
|maxInflightOverflowRate|1.3|Maximum percent of inflights overflow rate. Used for partitions throttling. Default value 1.3 allows 30% overflow.|Yes|Yes|1.0 - 2.0|
|outgoingSnapshotsThreadPoolSize|Number of available CPU cores|The number of threads in the executor that serves outgoing [RAFT snapshot](../../architecture/storage/data-partitioning.md#log-replication-and-snapshots) requests across all concurrent outgoing snapshot sessions on the node. Increasing it improves rebalance throughput when many partitions are snapshotted simultaneously, at the cost of more concurrent storage reads.|Yes|Yes|1 - Integer.MAX_VALUE|
|responseTimeoutMillis|3000|Period for which the RAFT client will try to receive a response from a remote peer.|Yes|No|0 - inf|
|retryDelayMillis|200|Delay between re-sends of a failed request by the RAFT client.|Yes|No|0 - inf|
|retryTimeoutMillis|10000|Period for which the RAFT client will try to receive a successful response from a remote peer.|Yes|No|0 - inf|
|volatileRaft.logStorageBudget.name|unlimited|The name of the log storage budget used by the node.|Yes|No, but the new values are only applied to new partitions|unlimited, entry-count|

### REST Configuration

```json
{
  "ignite" : {
    "rest" : {
      "dualProtocol" : false,
      "httpToHttpsRedirection" : false,
      "port" : 10300,
      "sql" : {
        "cursorIdleTimeoutMillis" : 300000,
        "defaultPageSize" : 1000,
        "maxOpenCursors" : 100,
        "maxPageSize" : 10000
      },
      "ssl" : {
        "ciphers" : "",
        "clientAuth" : "none",
        "enabled" : false,
        "keyStore" : {
          "password" : "********",
          "path" : "",
          "type" : "PKCS12"
        },
        "port" : 10400,
        "trustStore" : {
          "password" : "********",
          "path" : "",
          "type" : "PKCS12"
        }
      }
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|dualProtocol|false|Defines if both HTTP and HTTPS protocols are used by the endpoint.|Yes|Yes|true, false|
|httpToHttpsRedirection|false|Defines if requests to HTTP endpoint will be redirected to HTTPS.|Yes|Yes|true, false|
|port|10300|The port of the node's REST endpoint.|Yes|Yes|A valid port|
|sql.cursorIdleTimeoutMillis|300000|How long a paged [SQL result](../rest-api/overview.md#running-sql) may go untouched, in milliseconds, before the node releases its cursor. Keep this below `ignite.transaction.readOnlyTimeoutMillis` so that a client sees the cursor released rather than its transaction expiring.|Yes|Yes|1000 - Long.MAX_VALUE|
|sql.defaultPageSize|1000|Number of rows in a page when a SQL request over REST does not ask for a specific page size. Must not exceed `sql.maxPageSize`.|Yes|No|1 - Integer.MAX_VALUE|
|sql.maxOpenCursors|100|How many paged SQL results one node may hold at once. A request that needs another cursor while the node is at this limit fails with `429`.|Yes|Yes|1 - Integer.MAX_VALUE|
|sql.maxPageSize|10000|Largest page a SQL request over REST may ask for. A request for a larger page fails with `400`.|Yes|No|1 - Integer.MAX_VALUE|
|ssl.ciphers||Explicitly set node SSL cipher.|Yes|Yes|See [acceptable values](https://www.java.com/en/configure_crypto.html)|
|ssl.clientAuth||Client authorization used by the node, if any.|Yes|Yes|non, optional, require|
|ssl.enabled|false|Defines if SSL is enabled for the node.|Yes|Yes|true, false|
|ssl.keyStore||SSL keystore configuration.||||
|keyStore.password|********|Keystore password.|Yes|Yes|A valid password|
|keyStore.path||Path to the keystore.|Yes|Yes|A valid path|
|keyStore.type|PKCS12|Keystore type.|Yes|Yes|PKCS12, JKS|
|ssl.port|10400|Port used for SSL connections.|Yes|Yes|A valid port|
|ssl.trustStore||SSL trustsore configuration.||||
|trustStore.password|********|Truststore password.|Yes|Yes|A valid password|
|trustStore.path||Path to the truststore.|Yes|Yes|A valid path|
|trustStore.type|PKCS12|Truststore type.|Yes|Yes|PKCS12, JKS|

### Snapshots Configuration

```json
{
  "ignite": {
    "snapshot": {
      "diskBuffersCapacityBytes" : 67108864,
      "encryptionBuffersCapacityBytes" : 67108864,
      "snapshotChunkSizeBytes": 65536,
      "snapshotDiskBufferSizeBytes": 65536,
      "threadPoolSize": 20
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|diskBuffersCapacityBytes|67108864|The amount of off-heap space allocated to snapshotting process, in bytes.|Yes|Yes|1 - Integer.MAX_VALUE (Must be a multiple of 16.)|
|encryptionBuffersCapacityBytes|67108864|The amount of off-heap space allocated to snapshot compression process, in bytes.|Yes|Yes|1 - Integer.MAX_VALUE (Must be a multiple of 16.)|
|snapshotChunkSizeBytes|65536|The size of the chunk in bytes which will be used to process the snapshot content. Note, that when reading the snapshot, this property will not be used, since the size of the chunk with which it was written is saved in the snapshot metadata.|Yes|Yes|1 - Integer.MAX_VALUE (Must be a multiple of 16.)|
|snapshotDiskBufferSizeBytes|65536|The size of the buffer in bytes which will be used to write the snapshot content to disk. Use instead of `snapshotFlushBufferSize`|Yes|Yes|1 - Integer.MAX_VALUE (Must be a multiple of 16.)|
|threadPoolSize|20|Number of threads used by GridGain for IO operations when creating or restoring snapshots.|Yes|Yes|1 - Integer.MAX_VALUE|
|snapshotFlushBufferSize|65536|**Deprecated** Use `snapshotDiskBufferSizeBytes` instead. This property is obsolete and should not be used as it will not be supported in the future releases.|Yes|Yes|1 - Integer.MAX_VALUE (Must be a multiple of 16.)|

### SQL Configuration

```json
{
  "ignite" : {
    "sql" : {
      "execution" : {
        "threadCount" : 4
      },
      "nodeMemoryQuota" : "60%",
      "offloadingDataDir" : "sql_offloading",
      "offloadingDataLimit" : "0g",
      "planner" : {
        "threadCount" : 4
      }
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|execution.threadCount|4|Number of threads for query execution.|Yes|Yes|1 - Integer.MAX_VALUE|
|nodeMemoryQuota|60%|Node-wide limit for memory to be used for SQL queries. A number with a dimension identifier:<br>- % - percentage of the node's heap memory<br>- k - Kb<br>- m - Mb<br>- g - Gb<br>`0` with any of the dimension identifiers turns the memory tracking off.|Yes|No|0 -100%<br>0 - 9223372036854775807k/m/g|
|offloadingDataDir|sql_offloading|Absolute or relative path to the directory SQL data will be offloaded to.|Yes|Yes|1 - Integer.MAX_VALUE|
|offloadingDataLimit|0g|Node-wide limit for the amount of data that can be offloaded to disk. A number with a dimension identifier:<br>- % - percentage of the node's heap memory<br>- k - Kb<br>- m - Mb<br>- g - Gb<br>`0` with any of the dimension identifiers removes the data limit for data offloaded to disk. Exceeding this limit will cause the `SQL query ran out of memory: Offloading data limit was exceeded.` error.|Yes|Yes|1 - Integer.MAX_VALUE|
|planner.threadCount|4|Number of threads for query planning.|Yes|Yes|1 - Integer.MAX_VALUE|

### Storage Configuration

GridGain Persistence is designed to provide a quick and responsive persistent storage. When using the persistent storage, GridGain stores all the data on disk, and loads as much data as it can into RAM for processing. When persistence is enabled, GrigGain stores each partition in a separate file on disk. In addition to data partitions, GridGain stores indexes and metadata.

Each GridGain storage engine can have several storage _profiles_.

```json
{
  "ignite": {
    "storage": {
      "engines": {
        "aimem": {
          "pageSizeBytes": 16384
        },
        "aipersist": {
          "checkpoint": {
            "checkpointDelayMillis": 200,
            "checkpointThreads": 4,
            "compactionThreads": 4,
            "intervalDeviationPercent": 40,
            "intervalMillis": 180000,
            "logReadLockThresholdTimeoutMillis": 0,
            "readLockTimeoutMillis": 10000,
            "useAsyncFileIoFactory": true
          },
          "pageSizeBytes": 16384
        },
        "columnar": {
          "compressingConfiguration" : {
            "enableLz4Compression": true
          },
          "memtableConfiguration" : {
            "dataRegionSize": 2147483648,
            "memtableMaxSize": 67108864
          },
          "mergeTreeConfiguration": {
            "mergeTreeFanout": 4,
            "mergeTreeFirstLevelSize": 262144
          },
          "threadPoolConfiguration": {
            "threadPoolThreadCount": 16
          }
        },
        "rocksdb": {
          "flushDelayMillis": 100
        },
        "profiles": [
          {
            "engine": "aipersist",
            "name": "default",
            "replacementMode": "CLOCK",
            "sizeBytes": -1
          },
          {
            "engine": "aimem",
            "name": "default_aimem",
            "emptyPagesPoolSize": 100,
            "eviction": {
              "batchSize": 200,
              "interval": 60000,
              "lwmThreshold": 1000,
              "lwmUpdateInterval": 60000,
              "mode": "DISABLED",
              "threshold": "90%"
            },
            "initSizeBytes": -1,
            "maxSizeBytes": -1
          },
          {
            "engine": "rocksdb",
            "name": "default_rocksdb",
            "sizeBytes": -1,
            "writeBufferSizeBytes": 67108864
          },
          {
            "engine" : "columnar",
            "name" : "default_columnar"
          }
        ]
      }
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|engines.aimem||Aimem configuration.||||
|aimem.pageSizeBytes|16384|The size of pages in the storage, in bytes.|Yes|Yes|1024-16384|
|engines.aipersist||Aipersist configuration.||||
|aipersist.checkpoint.checkpointDelayMillis|200|Delay before staring a checkpoint after receiving the command.|Yes|No|0 - inf|
|aipersist.checkpoint.checkpointThreads|4|Number of CPU threads dedicated to checkpointing.|Yes|Yes|1 - inf|
|aipersist.checkpoint.compactionThreads|4|Number of CPU threads dedicated to data compaction.|Yes|Yes|1 - inf|
|aipersist.checkpoint.intervalMillis|180000|Interval between checkpoints in milliseconds.|Yes|No|0 - inf|
|aipersist.checkpoint.intervalDeviationPercent|40|Jitter that will be added or subtracted from time period till next scheduled checkpoint (percentage).|Yes|No|0-100|
|aipersist.checkpoint.logReadLockThresholdTimeoutMillis|0|Threshold for logging long read locks, in milliseconds.|Yes|Yes|0 - inf|
|aipersist.checkpoint.readLockTimeoutMillis|10000|Timeout for checkpoint read lock acquisition, in milliseconds.|Yes|Yes|0 - inf|
|aipersist.checkpoint.useAsyncFileIoFactory|true|Define if GridGain uses asynchronous file I/O operations provider.|Yes|Yes|true, false|
|aipersist.pageSizeBytes|16384|The size of pages in the storage, in bytes.|No|N/A|1024-16384|
|engines.columnar||Columnar storage engine configuration.||||
|columnar.compressingConfiguration.enableLz4Compression|true|Defines if Lz4 compression will be used on columnar storage.|Yes|Yes|true, false|
|columnar.memtableConfiguration.dataRegionSize|2147483648|Maximum size of all memory table buffers combined.|Yes|Yes||
|columnar.memtableConfiguration.memtableMaxSize|67108864|Maximum size of a single memory table.|Yes|Yes||
|columnar.mergeTreeConfiguration.mergeTreeFanout|4|The number of times by which the tree grows with each level.|Yes|Yes||
|columnar.mergeTreeConfiguration.mergeTreeFirstLevelSize|262144|The size of entries of the first level of merge tree.|Yes|Yes||
|columnar.threadPoolConfiguration.threadPoolThreadCount|10|Columnar thread-pool size.|Yes|Yes||
|engines.rocksdb||Rocksdb configuration.||||
|rocksdb.flushDelayMillis|100|Delay before executing a flush triggered by RAFT.|Yes|Refreshed on engine registration|0 - inf|
|profiles||The list of available storage profiles.||||
|engine||The storage engine.|No|N/A|aimem, aipersist, rocksdb|
|name||User-defined profile name.|No|N/A|A valid name|
|profiles.aipersist.replacementMode|CLOCK|Sets the page replacement algorithm. `RANDOM_LRU` and `SEGMENTED_LRU` are deprecated. Use `CLOCK`.|Yes|Yes|CLOCK, RANDOM_LRU (deprecated), SEGMENTED_LRU (deprecated)|
|profiles.aipersist.sizeBytes|-1|Memory (RAM) region size in bytes. When set to -1 will be computed automatically equal to 20% of the available memory.|Yes|Yes|Min 256Mb, max defined by the addressable memory limit of the OS, or -1.|
|profiles.aimem.initSizeBytes|-1|Initial memory region size in bytes, when the used memory size exceeds this value, new chunks of memory will be allocated. When set to -1 `aimem.maxSizeBytes` value will be used instead.|Yes|Yes|Min 256Mb, max defined by the addressable memory limit of the OS, or -1.|
|profiles.aimem.maxSizeBytes|-1|Maximum memory region size in bytes. When set to -1 will be computed automatically equal to 20% of the available memory.|Yes|Yes|Min 256Mb, max defined by the addressable memory limit of the OS, or -1.|
|profiles.aimem.eviction.mode|DISABLED|Eviction mode.|Yes|No|- DISABLED - Eviction is disabled.<br>- HISTORY_ONLY - Only historical versions of rows are evicted.<br>- RANDOM - Historical versions of rows are evicted first, followed by the eviction of the most recent row versions, which are chosen randomly.|
|profiles.aimem.eviction.threshold|90%|Threshold for eviction initiation. A number with a dimension identifier:<br>- % - percentage of aimem.maxSize<br>- k - Kb<br>- m - Mb<br>- g - Gb<br>For instance, "90%" means that the page memory starts eviction only after 90% of the data region is occupied.|Yes|No|- 0-100%<br>- 0-9223372036854775807k/m/g|
|profiles.aimem.eviction.lwmUpdateInterval|60000|Frequency of the low watermark update in milliseconds.|Yes|No|1 - inf|
|profiles.aimem.eviction.interval|60000|Interval between the data eviction iterations.|Yes|No|1 - inf|
|profiles.aimem.eviction.lwmThreshold|1000|If the low watermark is less than evictionLwmThreshold from the current timestamp, the row eviction is triggered.|Yes|No|0 - inf|
|profiles.aimem.eviction.batchSize|60000|Eviction batch size in rows.|Yes|No|1 - inf|
|profiles.rocksdb.writeBufferSizeBytes|67108864|Size of rocksdb write buffer in bytes.|Yes|Yes|Min 1, max defined by the addressable memory limit of the OS.|
|profiles.rocksdb.sizeBytes|-1|Size of the rocksdb offheap cache in bytes. When set to -1, will be computed automatically equal to 20% of the available memory.|Yes|Yes|Min 1, max defined by the addressable memory limit of the OS, or -1.|

### System Configuration

This section describes internal properties, which are used by a number of GridGain components.

Although you can edit these properties in the same way you edit all others - using the `node config update` CLI command - we suggest that you discuss the proposed changes with the GridGain support team. The properties can apply to a specific node - see below - or to the [cluster as a whole](cluster-configuration-parameters.md#system-configuration).

{% hint style="info" %}
Note that the property names are in `camelCase`.
{% endhint %}

```json
{
  "ignite" : {
    "system" : {
      "cmgPath" : "",
      "criticalWorkers" : {
        "livenessCheckIntervalMillis" : 2000,
        "maxAllowedLagMillis" : 5000,
        "nettyThreadsHeartbeatIntervalMillis" : 1000
      },
      "metastoragePath" : "",
      "partitionsBasePath" : "",
      "partitionsLogPath" : "",
      "properties":{}
    }
  }
}
```

|Property|Description|Default|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|system.cmgPath|The path the cluster management group information is stored to. Only applicable if the node is part of CMG. By default, data is stored in `{GRIDGAIN_HOME}/work/cmg`. It is recommended to only change this path on an empty node.||Yes|Yes|Valid absolute path.|
|system.criticalWorkers.livenessCheckIntervalMillis|Interval between liveness checks (ms) performed by the critical worker infrastructure.|2000|Yes|Yes|1 - inf (not greater than half of `maxAllowedLagMillis`)|
|system.criticalWorkers.maxAllowedLagMillis|Maximum allowed delay from the last heartbeat to the current time (ms). If exceeded, the critical worker is considered to be blocked.|5000|Yes|No|1 - inf (should be at least twice `livenessCheckIntervalMillis`)|
|system.criticalWorkers.nettyThreadsHeartbeatIntervalMillis|Interval between heartbeats used to update the Netty threads' heartbeat timestamps (ms).|1000|Yes|Yes|1 - inf|
|system.metastoragePath|The path the cluster meta information is stored to. Only applicable if the node is part of the metastorage group. By default, data is stored in `{GRIDGAIN_HOME}/work/metastorage`. It is recommended to only change this path on an empty node.||Yes|Yes|Valid absolute path.|
|system.partitionsBasePath|The path data partitions are saved to on the node. By default, partitions are stored in `{GRIDGAIN_HOME}/work/partitions`. It is recommended to only change this path on an empty node.||Yes|Yes|Valid absolute path.|
|system.partitionsLogPath|The path RAFT log the partitions are stored at. By default, this log is stored in `{system.partitionsBasePath}/log`. It is recommended to only change this path on an empty node.||Yes|Yes|Valid absolute path.|
|system.properties|System properties used by the GridGain components.||Yes|Yes|A map of properties.|
|system.cmgPath|The path the cluster management group information is stored to. Only applicable if the node is part of CMG. By default, data is stored in `{GRIDGAIN_HOME}/work/cmg`. It is recommended to only change this path on an empty node.||Yes|Yes|Valid absolute path.|
|system.metastoragePath|The path the cluster meta information is stored to. Only applicable if the node is part of the metastorage group. By default, data is stored in `{GRIDGAIN_HOME}/work/metastorage`. It is recommended to only change this path on an empty node.||Yes|Yes|Valid absolute path.|
|system.partitionsBasePath|The path data partitions are saved to on the node. By default, partitions are stored in `{GRIDGAIN_HOME}/work/partitions`. It is recommended to only change this path on an empty node.||Yes|Yes|Valid absolute path.|
|system.partitionsLogPath|The path RAFT log the partitions are stored at. By default, this log is stored in `{system.partitionsBasePath}/log`. It is recommended to only change this path on an empty node.||Yes|Yes|Valid absolute path.|
|system.properties|System properties used by the Ignite components.||Yes|Yes|An named list of properties.|

### Table Configuration

```json
{
  "ignite" : {
    "table": {
      "eviction" : {
        "checkInterval" : 60000
      },
      "expiration" : {
        "batchSize" : 1000,
        "checkInterval" : 30000,
        "parallelismLevel" : 1
      }
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|eviction.checkInterval|60000|How often the data is checked for eviction threshold, in milliseconds.|Yes|Yes|1 - inf|
|expiration.batchSize|1000|The number of items that can be expired at once.|Yes|Yes|1 - inf|
|expiration.checkInterval|30000|How often the data is checked for expiration, in milliseconds.|Yes|Yes|1 - inf|
|expiration.parallelismLevel|1|The number of threads used for data expiry.|Yes|Yes|1 - Integer.MAX_VALUE|
