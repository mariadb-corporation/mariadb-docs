---
description: >-
  GridGain authorization: the permission string format, the defaultAllow
  property, the full list of supported permissions, and how to scope them.
---

# Authorization and Permissions

{% hint style="warning" %}
The Authorization feature is available only with GridGain Enterprise or Ultimate Edition.
{% endhint %}

Authorization occurs after successful authentication of subjects (remote nodes or clients).
Once a subject is authenticated, it is assigned a set of preconfigured permissions.
Permissions are associated with the users in the [authenticator](authentication.md) configuration.

## Permission String Format

Permissions are configured as a single string in the following almost JSON-like format (spaces and newline characters are ignored).
The string contains the `defaultAllow` property and a list of objects that grant permissions for specific scopes.
In each object, you define a scope and specify a list of permissions for that scope.

```json
{
    defaultAllow: false,
    {
        cache: "mycache",
        permissions: [CACHE_READ, CACHE_PUT, CACHE_REMOVE]
    },
    {
        cache: "*",
        permissions: [CACHE_READ]
    },
    {
        task: "org.mytasks.*",
        permissions: [TASK_EXECUTE]
    },
    {
        service: "*",
        permissions: [SERVICE_INVOKE]
    },
    {
        system: [ADMIN_VIEW, CACHE_CREATE, JOIN_AS_SERVER]
    }
}
```

The example given above defines the following permissions:

* all permissions that are not listed explicitly are denied
* read, put and remove operations are allowed for the cache `mycache`
* read operations are allowed for any cache
* the tasks that are in the package `org.mytasks.*` can be executed
* any service can be invoked
* the user can create caches, join the cluster as a server node
* Control Center can view cluster statistics

### The defaultAllow Property

The `defaultAllow` property applies to all the operations that do not fall into the defined scopes.
If `defaultAllow` is set to `false`, the operations that do _not_ fall into any of the default scopes are _disallowed_.
If the property is set to `true`, the permissions that do _not_ fall into any of the default scopes are _granted_.

### Example 1

```json
{
    defaultAllow : true
}
```

The example above grants all possible permissions (including system permissions).

### Example 2

```json
{
    defaultAllow: true,
    {
        cache: "account*",
        permissions: [CACHE_READ]
    },
    {
        system: [JOIN_AS_SERVER]
    }
}
```

In the example above, the configuration defines two scopes: 1) caches whose name start with "account", and 2) the system scope.

* within scope 1, only CACHE_READ operations are granted, and other operations are disallowed,
* all operations on other caches are granted because `defaultAllow = true`,
* only the `JOIN_AS_SERVER` system permission is granted, other system permissions are denied.

As a result, the `CACHE_CREATE` permission is denied for the caches in scope 1, because it is listed neither in scope 1 nor among system permissions.
However, you can create caches outside of scope 1 (in fact, _any_ operation on caches outside of scope 1 is allowed).

### Example 3

```json
{
    defaultAllow: false,
    {
        cache: "account*",
        permissions: [CACHE_READ]
    },
    {
        system: [JOIN_AS_SERVER]
    }
}
```

Similarly to example 2, there are 2 scopes: 1) caches whose name start with "account", and 2) the system scope.

* within scope 1, only CACHE_READ operations are granted, and other operations are disallowed,
* all operations on other caches are prohibited because `defaultAllow = false`,
* only the `JOIN_AS_SERVER` system permission is granted, other system permissions are denied.

With this configuration, you cannot create caches.

## Supported Permissions

GridGain supports the following permissions:

**Cache permissions:**

- CACHE_READ - cache read operations
- CACHE_PUT -  cache put operations
- CACHE_REMOVE - cache remove operations
- CACHE_CREATE - creating new caches (including ones specified in the node configuration)
- CACHE_DESTROY - destroying existing caches

**Task permissions:**

- TASK_EXECUTE - task execution
- TASK_CANCEL - task cancellation

**Service permissions:**

- SERVICE_DEPLOY -  service deployment
- SERVICE_INVOKE - service invocation
- SERVICE_CANCEL - service cancellation

**System permissions:**

- JOIN_AS_SERVER - node joining the cluster as server
- EVENTS_ENABLE - enabling events in runtime
- EVENTS_DISABLE - disabling events in runtime
- ADMIN_OPS - operations executed from Control Center
- ADMIN_VIEW - viewing cluster statistics (metrics, graphs, cache sizes, etc.) in Control Center
- ADMIN_QUERY - executing SQL queries from Control Center
- ADMIN_CACHE - cache operations executed from Control Center (data loading, manual rebalancing, etc.)
- ADMIN_METADATA_OPS - administrative operations on cluster metadata (removing or updating binary type metadata)
- ADMIN_READ_DISTRIBUTED_PROPERTY - reading the values of distributed properties
- ADMIN_WRITE_DISTRIBUTED_PROPERTY - changing the values of distributed properties
- SET_QUERY_MEMORY_QUOTA - setting [memory quotas](../ha-and-performance/performance-tuning/sql-memory-management.md) for SQL queries
- GET_QUERY_VIEWS - viewing the `LOCAL_SQL_RUNNING_QUERIES` or `LOCAL_SQL_QUERY_HISTORY` system views
- KILL_QUERY - execute the `KILL QUERY` command
- CACHE_CREATE - creating new caches (including ones specified in the node configuration)
- CACHE_DESTROY - destroying existing caches
- REFRESH_STATISTICS - refreshing SQL statistics
- CHANGE_STATISTICS - running SQL analysis and dropping SQL statistics
- CHANGE_SNAPSHOT_SECURITY_LEVEL - changing the security level applied to snapshot operations

**Tracing permissions:**

- `TRACING_CONFIGURATION_UPDATE` - updating tracing configuration

Please note that `CACHE_CREATE` and `CACHE_DESTROY` can be configured both as cache permissions (will be applied only to the cache names that matche the pattern) and as system permissions (will be applied to all caches). In case of conflicting configuration on the system and on the cache level, the resulting behavior will be determined by `OR` rule: if `CACHE_CREATE` is granted on the system _or_ on the cache level, the action will be authorized.

## Specifying Scope of Permissions

Note that you can use wildcard patterns to indicate the scope of the permissions.
For example, the following string allows read operations for _all caches_:

```json
{
    cache:"*",
    permissions:[CACHE_READ]
}
```

This string allows read operations for the caches whose name starts with "person".

```json
{
    cache:"person*",
    permissions:[CACHE_READ]
}
```

The following table explains how the scope is defined:

|Permission | Scope Definition|
|---|---|
| Cache permissions | Cache name.|
| Task permissions | Task's full class name (including the package).|
| Service permissions | Service's full class name (including the package).|
| System permissions | Do not have a scope.|

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
