---
description: >-
  Reference for GridGain 9 cluster-wide configuration parameters, including how
  to set, check, change, and export cluster configuration from the CLI.
---

# Cluster Configuration Parameters

GridGain 9 cluster configuration is shared across the whole cluster. Regardless of which node you apply the configuration on, it will be propagated to all nodes in the cluster.

In GridGain 9, you can create and maintain configuration in either HOCON or JSON. The configuration file has a single root "node," called `ignite`. All configuration sections are children, grandchildren, etc., of that node.

## Setting Initial Cluster Configuration

When starting a cluster, it uses default parameters unless otherwise specified. You can provide custom configuration parameters in the `--config` parameter, or a path to the configuration file in the `--config-files` parameter. You also need to pass a valid license using the `--license` key.

```bash
cluster init --name=sampleCluster --license=/valid-license.conf --config-files=/cluster-config.conf
```

## Checking Cluster Configuration

To get cluster configuration, use the [CLI tool](../cli-tool.md).

- Start the CLI tool and connect to any node in the cluster.
- Run the `cluster config show` command.

The CLI tool will print the full cluster configuration. If you only need a part of the configuration, you can narrow down the search by providing the properties you need as the command argument, for example:

```bash
cluster config show ignite.transaction
```

## Changing Cluster Configuration

Cluster configuration is changed from the CLI tool. You can update it both in the interactive (REPL) and non-interactive mode by passing a configuration file with the `--file` parameter.

{% hint style="info" %}
Values set directly via the CLI take precedence over values set in the configuration file.
{% endhint %}

### Update via REPL:

Start the CLI tool and connect to any node in the cluster.

- Run the `cluster config update` command and provide the updated configuration as the command argument, for example:

  ```bash
  cluster config update ignite.system.idleSafeTimeSyncIntervalMillis=600
  ```
- To update one or more parameters, pass the configuration file to the `cluster config update` command:

  ```bash
  cluster config update --file ../gridgain-config.conf
  ```
- You also can update the configuration combining both approaches:

  ```bash
  cluster config update --file ../gridgain-config.conf ignite.system.idleSafeTimeSyncIntervalMillis=600
  ```
- To delete a configuration section that uses a list, such as [exporters](#metrics-configuration), pass `null` as the argument.

  ```bash
  ignite.metrics.exporters.name=null
  ```

The updated configuration will automatically be applied across the cluster.

### Update via Non-Interactive Mode

You can also modify cluster configuration via [non-interactive](../cli-tool.md#non-interactive-cli-mode) CLI mode without starting the CLI tool first.

- Pass the configuration file with the `--file` parameter:

  ```bash
  bin/gridgain9 cluster config update --file ../gridgain-config.conf
  ```

The updated configuration will automatically be applied across the cluster.

## Exporting Cluster Configuration

If you need to export cluster configuration to file, use the following command:

```bash
bin/gridgain9 cluster config show > cluster-config.conf
```

## Configuration Parameters

### Encryption Configuration

```json
{
  "ignite" : {
    "encryption" : {
      "activeProvider" : "",
      "enabled" : false,
      "providers" : { }
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|activeProvider|""|The name of the currently active encryption provider.|Yes|No|A name from the provider map|
|enabled|false|Whether the encryption is enabled.|Yes|No|true, false|
|providers||A named list (map) of the available encryption providers.|Yes|No|A valid provider map|

### Event Log Configuration

```json
{
  "ignite" : {
    "eventlog" : {
      "channels" : { },
      "sinks" : { }
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|channels||A named list of event log channels.|Yes|No|Valid channels|
|sinks||A named list of event log sinks.|Yes|No|Valid sinks|

### Garbage Collection Configuration

```json
{
  "ignite" : {
    "gc" : {
      "batchSize" : 5,
      "lowWatermark" : {
        "dataAvailabilityTimeMillis" : 600000,
        "updateIntervalMillis" : 300000
      },
      "threads" : 16
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|batchSize|5|The number of entries to be removed by the garbage collection batch for each partition|Yes|No|0 - inf|
|lowWatermark.dataAvailabilityTimeMillis|600000|The duration the outdated versions are available for, in milliseconds.|Yes|No|1000 - inf|
|lowWatermark.updateIntervalMillis|300000|The interval of the low watermark updates.|Yes|No|0 - inf|
|threads|Runtime.getRuntime().availableProcessors()|The number of threads used by the garbage collector.|Yes|Yes|1 - inf|

### License Configuration

```json
{
  "ignite" : {
    "license" : {
        "content" : "********",
        "signature" : "********"
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|content|""|License content; a JSON string.|Yes|No|A JSON string with valid constraints|
|signature|""|Signature for the license content.|Yes|No|A valid HEX string|

{% hint style="info" %}
If a cluster license expires, the nodes will stop and fail to restart with a `License is expired` validation error. To recover the cluster, set the `GG_LICENSE_OVERRIDE` environment variable on every node to the path of a valid license file, then start the nodes. Each node applies the override license and persists it to the cluster configuration. Unset the variable after a successful start.
{% endhint %}

### Metrics Configuration

```json
{
  "ignite" : {
    "metrics" : {
      "exporters" : [ ]
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|exporters||The list of [metric](../../gridgain9-management/monitoring/configuring-metrics.md) exporters currently used.|Yes|No|Valid exporters|

### Replication Configuration

```json
{
  "ignite" : {
    "replication" : {
      "batchSizeBytes" : 8192,
      "idleSafeTimePropagationDurationMillis" : 1000,
      "leaseAgreementAcceptanceTimeLimitMillis" : 120000,
      "leaseExpirationIntervalMillis" : 5000,
      "longOperationTimeoutMillis" : 10000,
      "maxConcurrentWaitingUserOperations" : 1000,
      "partitionOperationHeapUsagePercent" : 20,
      "replicaOperationRetryIntervalMillis" : 10,
      "rpcTimeoutMillis" : 60000
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|batchSizeBytes|8192|Batch size (in bytes) to be written into physical storage. Used to limit the size of an atomic Write.|Yes|No|1 - Integer.MAX_VALUE|
|idleSafeTimePropagationDurationMillis|1000|Interval between Partition Safe Time updates.|No|N/A|1 - inf|
|leaseAgreementAcceptanceTimeLimitMillis|120000|The maximum duration of an election for a new partition leaseholder, in milliseconds.|Yes|N/A|5000 - inf|
|leaseExpirationIntervalMillis|5000|The duration of a single lease.|Yes|N/A|2000 - 120000|
|longOperationTimeoutMillis|10000|Default timeout, in milliseconds, for user operations that wait for a system replication group (the Cluster Management Group or Meta Storage) to become available. If the group cannot reach a quorum within this time, the operation fails with [`IGN-REP-10`](../error-codes/README.md#replicator-exceptions) instead of waiting indefinitely. Set to 0 to fail the request immediately after confirming that no node is available in the group, or set higher to wait for group availability for longer.|Yes|No|0 - inf|
|maxConcurrentWaitingUserOperations|1000|Maximum number of user operations that can wait simultaneously for a system replication group (the Cluster Management Group or Meta Storage) to become available. When this limit is reached, additional user operations fail immediately with [`IGN-REP-9`](../error-codes/README.md#replicator-exceptions) instead of queuing, which prevents memory exhaustion during a prolonged outage.|Yes|No|1 - Integer.MAX_VALUE|
|partitionOperationHeapUsagePercent|20|Maximum share of JVM max heap the node may reserve for pending partition operations. Requests that would push usage past this share are rejected with [`IGN-REP-12`](../error-codes/README.md#replicator-exceptions); operations already in progress continue uninterrupted. Set to `0` to disable the limit.|Yes|Yes|0 - 100|
|replicaOperationRetryIntervalMillis|10|The retry interval for replica operations.|Yes|N/A|1 - inf|
|rpcTimeoutMillis|60000|Replication request processing timeout.|Yes|No|0 - inf|

### Schema Sync Configuration

```json
{
  "ignite" : {
    "schemaSync" : {
      "delayDurationMillis" : 500,
      "maxClockSkewMillis" : 500
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|delayDurationMillis|500|The delay after which a schema update becomes active. Should exceed the typical time to deliver a schema update to all cluster nodes, otherwise delays in handling operations are possible. Should not be less than `metaStorage.idleSyncTimeIntervalMillis`. The optimal value is `metaStorage.idleSyncTimeIntervalMillis` * 2.|No|N/A|1 - inf|
|maxClockSkewMillis|500|Maximum physical clock skew (ms) tolerated by the cluster. If the difference between physical clocks of two nodes in the cluster exceeds this value, the cluster might demonstrate abnormal behavior.|No|N/A|0 - inf|

### Security Configuration

```json
{
  "ignite": {
    "security": {
      "authentication": {
        "providers": {
          "default": {
            "type": "basic",
            "users": {
              "ignite": {
                "displayName": "ignite",
                "password": "********",
                "passwordEncoding": "PLAIN",
                "roles": [
                  "system"
                ]
              }
            }
          }
        }
      },
      "authorization": {
        "roles": {
          "system": {
            "displayName": "system",
            "privileges": { }
          }
        }
      },
      "enabled": false,
      "jwt": {
        "keyTtl": 1209600000,
        "ttl": 28800000
      }
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|Authentication parameters||||||
|providers.name|default|The name of the authentication provider.|Yes|No|A valid string|
|providers.type|basic|The authentication provider type.|Yes|No|basic, ldap|
|providers.users||The list of users registered with the specific provider.||||
|providers.users.displayName|ignite|Case sensitive user name.|No|N/A|A valid username|
|providers.users.password|********|User password.|Yes|No|A valid password|
|providers.users.passwordEncoding|PLAIN|User password's encoding.|Yes|No|PLAIN, BCRYPT|
|providers.users.roles|system|The list of roles assigned to the user.|Yes|No|A valid role|
|providers.users.username|ignite|Case-insensitive user name.|Yes|No|A valid user name|
|LDAP authentication parameters (`ldap` provider type only)||||||
|providers.url||The URL of the LDAP server.|Yes|No|A valid `ldap://` or `ldaps://` URL|
|providers.userSearch.dn||The DN of the container to search for users.|Yes|No|A valid DN|
|providers.userSearch.scope|SUB_TREE|The scope of the user search.|Yes|No|SUB_TREE, ONE_LEVEL, BASE|
|providers.userSearch.filter|`(uid={0})`|A filter used when searching for the user. `{0}` is replaced by the username.|Yes|No|A valid LDAP filter|
|providers.userSearch.groupAttribute||An attribute of the user entry checked for group membership. If not empty, `groupSearch` is ignored.|Yes|No|A valid attribute name|
|providers.groupSearch.dn||The DN of the container to search for groups.|Yes|No|A valid DN|
|providers.groupSearch.scope|SUB_TREE|The scope of the group search.|Yes|No|SUB_TREE, ONE_LEVEL, BASE|
|providers.groupSearch.filter|`(\|(member={0})(memberOf={0})(memberUid={0}))`|A filter used when searching for the user's groups. `{0}` is replaced by the value of the attribute defined in `userAttribute`.|Yes|No|A valid LDAP filter|
|providers.groupSearch.userAttribute||The user attribute provided as the parameter to the group search filter. If empty, the user DN is used.|Yes|No|A valid attribute name|
|providers.roleMapping.groupName||The name of the LDAP group mapped to GridGain roles.|Yes|No|A valid group name|
|providers.roleMapping.roles||The list of GridGain roles assigned to users in the LDAP group.|Yes|No|A list of valid roles|
|Authorization parameters||||||
|roles.displayName|system|Case-sensitive role name.|Yes|No|A valid role name|
|roles.name|system|Case-insensitive role name.|Yes|No|A valid role name|
|roles.privileges||A list of [privileges](../../security/user-permissions-and-roles.md) available to users with the role.||||
|roles.privileges.action|""|The action the privilege relates to.|Yes|No|A valid action|
|roles.privileges.name|""|A privilege name on privilege list .|No|N/A|A valid name|
|roles.privileges.on|""|The name of the object the privilege applies to.|Yes|No|A valid object name or empty|
|Security parameters||||||
|enabled|false|Whether authentication is enabled.|Yes|No|true, false|
|JWT parameters||||||
|jwt.keyTtl|1209600000|TTL for JWT security tokens.|Yes|No|A valid LONG value|
|jwt.ttl|28800000|The frequency of private key updates used to issue JWT tokens.|Yes|No|A valid LONG value|

For more information on configuring authentication, including an LDAP provider example, see [User Authentication](../../security/authentication.md).

### Snapshots Configuration

```json
{
  "ignite": {
    "snapshot": {
      "snapshotTombstonesTtlMinutes": 1440,
      "paths": [
        {
          "default": false,
          "name": "local-default-relative-example",
          "type": "LOCAL",
          "uri": "file:/snapshots"
        },
        {
          "default": false,
          "name": "remote-absolute-example",
          "type": "REMOTE",
          "uri": "file:///absolute/path/to/snapshots"
        }
      ]
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|snapshotTombstonesTtlMinutes|1440|The period of time during which it is possible to create an incremental snapshot after creating another snapshot. Deleted data will still still occupy some storage space for this time.|Yes|No|Non-negative `long` value|
|paths.default|false|If set to `true`, this path is used as the default when no `--source` or `--destination` option is specified in the snapshot command. Only one path can be marked as default. If no default is set, the system falls back to the LOCAL path `file:/snapshots` when no `--source` or `--destination` is provided.|Yes|No|boolean|
|paths.name||The name of the snapshot path.|Yes|No|A valid string|
|paths.type|LOCAL|The snapshot path's type. LOCAL paths are not shared between nodes; REMOTE ones are shared. The REMOTE paths use a single-copy algorithm, which saves only one copy of meta and partition files|Yes|No|LOCAL, REMOTE|
|paths.uri||The base URI where snapshots will be stored. Use either `scheme:///absolute-path` for absolute paths or `scheme:/relative-path` for relative paths. Currently, only the `file` scheme is supported. If an absolute path is provided, it is treated as a REMOTE path and used "as is". For LOCAL paths, a subfolder named after the node is appended: `/absolute-path/node-name`. Relative paths are resolved from the node's working directory: `{GRIDGAIN_HOME}/work/relative-path`.|Yes|No|A valid URI|

### SQL Configuration

```json
{
  "ignite" : {
    "sql" : {
      "allowFollowerReads" : false,
      "createTable" : {
        "minStaleRowsCount" : 500,
        "staleRowsFraction" : 0.2
      },
      "memoryQuotaBlockSize" : "512k",
      "offloadingEnabled" : false,
      "planner" : {
        "estimatedNumberOfQueries" : 1024,
        "maxPlanningTimeMillis" : 15000,
        "planCacheExpiresAfterSeconds" : 1800
      },
      "statementMemoryQuota" : "100%",
      "statistics" : {
            "autoRefresh" : {
                "staleRowsCheckIntervalSeconds" : 60
            }
        }
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|allowFollowerReads|false|Determines whether read-only SQL queries can read data from non-primary replicas. When `false`, these queries always read from primary replicas. Can be overridden for an individual statement or JDBC connection.|Yes|no|true, false|
|createTable.minStaleRowsCount|500|Number of updates since the last query plan update required to automatically recreate query execution plan. Is overridden by `WITH min stale rows` [parameter](../sql/ddl.md#create-table).|Yes|no|0 - Long.MAX_VALUE|
|createTable.staleRowsFraction|0.2|Fraction of the table that must change for query execution plan to be recreated automatically. Is overridden by `WITH stale rows fraction` [parameter](../sql/ddl.md#create-table)|Yes|no|0 - 1|
|memoryQuotaBlockSize|512k|The size of individual memory blocks.|Yes|Yes|0 - inf|
|offloadingEnabled|false|Determines if SQL memory offloading|Yes|no|true, false|
|planner.estimatedNumberOfQueries|1024|The estimated number of unique queries that are planned to be executed in the cluster in a certain period of time. Used to optimize internal caches and processes. Optional.|Yes|Yes|0 - Integer.MAX_VALUE|
|planner.maxPlanningTimeMillis|15000|Query planning timeout in milliseconds. Plan optimization process stops when the timeout is reached. `0` means no timeout.|Yes|Yes|0 - Long.MAX_VALUE|
|planner.planCacheExpiresAfterSeconds|1800|The number of seconds after which a query plan in removed from the query plan cache if it is not used. `0` means query plans are never removed.|Yes|Yes|0 - Long.MAX_VALUE|
|statementMemoryQuota|100%|The amount of memory that can be used by a single SQL statement. A number with a dimension identifier:<br>- % - percentage of the node's heap memory<br>- k - Kb<br>- m - Mb<br>- g - Gb<br>`0` with any of the dimension identifiers turns the memory tracking off.|Yes|No|0 - 100%<br>0 - 9223372036854775807k/m/g|
|statistics.autoRefresh.staleRowsCheckIntervalSeconds|60|Time period between checks for stale rows in seconds. Only applies if there is at least one statistics object with `autorefresh` set to `true`.|Yes|Yes|1 - Long.MAX_VALUE|

### System Configuration

This section describes internal properties used by various GridGain components.

You can edit these properties using the `cluster config update` CLI command, just like any other configuration option. However, we recommend discussing any changes with the GridGain [support team](https://www.gridgain.com/services/support) before applying them.

These properties may apply to the entire cluster (see below) or to a [specific node](node-configuration-parameters.md#system-configuration).

{% hint style="info" %}
Property names are written in `camelCase`.
{% endhint %}

```json
{
  "ignite" : {
    "system" : {
      "properties":{},
      "idleSafeTimeSyncIntervalMillis" : 250
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|system.properties||System properties used by the GridGain components.|Yes|Yes|A map of properties.|
|idleSafeTimeSyncIntervalMillis|250|Period (in milliseconds) used to determine how often to issue time sync commands when Metastorage is idle (no Writes are issued). Should not exceed `schemaSync.delayDurationMillis`. The optimal value is `schemaSync.delayDurationMillis` / 2.|Yes|No (becomes effective on Metastorage leader reelection)|1 - inf|

### Transactions Configuration

```json
{
  "ignite" : {
    "transaction" : {
      "observableTimestampDelayMillis" : -1,
      "readOnlyTimeoutMillis" : 600000,
      "readWriteTimeoutMillis" : 30000
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|observableTimestampDelayMillis|-1|Delay, in milliseconds, subtracted from the current time to compute the observable timestamp used as the read timestamp for read-only transactions (`observableTimestamp = now - observableTimestampDelayMillis`). A larger delay reduces latency by letting clients observe slightly older data, reducing the chance that a request to a lagging node has to wait for safe time to catch up; a smaller delay favors reading the newest data. The default value `-1` means "not set": the delay is selected automatically based on server configuration, providing a sensible tradeoff between data freshness and latency.|Yes|No|-1, or 0 - inf|
|readOnlyTimeoutMillis|600000|Timeout for read-only transactions. It defines how long the transaction holds acquired resources on participating nodes. If no timeout is specified, or it is set to `0`, a default value of 10 minutes is applied. The transaction is guaranteed to remain active until the timeout expires. Once the timeout is reached, the transaction is aborted but may persist briefly beyond the timeout while corresponding resources are cleaned up. Use instead of `readOnlyTimeout`.|Yes|No|1 - inf|
|readWriteTimeoutMillis|30000|Timeout for read-write transactions. It defines how long the transaction holds acquired resources on participating nodes. If no timeout is specified, or it is set to `0`, a default value of 30 seconds is applied. The transaction is guaranteed to remain active until the timeout expires. Once the timeout is reached, the transaction is aborted but may persist briefly beyond the timeout while corresponding resources are cleaned up. Use instead of `readWriteTimeout`.|Yes|No|1 - inf|
