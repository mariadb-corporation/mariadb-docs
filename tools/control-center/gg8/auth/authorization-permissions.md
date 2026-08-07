---
description: >-
  Cluster permissions required for Control Center actions on secured GridGain 8
  clusters — caches, queries, snapshots, compute, and more.
---

# Authorization and Permissions

You need an authorization to access the [secured GridGain clusters](https://www.gridgain.com/docs/latest/administrators-guide/security/authorization-permissions) via Control Center.

When you attempt to initiate a permission-protected action on a secured GridGain cluster, you are prompted to enter the cluster-specific user name and password.

![](../../../.gitbook/assets/cc-gg8-secured-cluster-auth.png)

Control Center supports the following permissions.

## Baseline Actions

All [baseline topology](../dashboard/my-cluster.md#viewing-cluster-health-details) actions require the ADMIN_OPS permission.

## Binary Type Actions

The [binary type](../caches/binary-types.md) actions that might affect the cluster state require the following permissions:

| Action | Permission |
|---|---|
| Update binary types | ADMIN_METADATA_OPS |
| Remove binary type | ADMIN_METADATA_OPS, TASK_EXECUTE |

## Cache Actions

The [cache](../caches/caches.md) actions that might affect the cluster state require the following permissions:

| Action | Permission |
|---|---|
| Reset lost partitions | ADMIN_OPS |
| Clear cache | CACHE_REMOVE |
| Destroy cache | CACHE_DESTROY |
| Rebalance caches | ADMIN_CACHE |
| Load cache | ADMIN_OPS, TASK_EXECUTE |
| Enable cache statistics | ADMIN_CACHE |
| Disable cache statistics | ADMIN_CACHE |

## Cache DR Actions

All [cache DR](../caches/caches.md) actions require the ADMIN_OPS permission.

## Cluster Actions

The cluster actions require the following permissions:

| Action | Permission |
|---|---|
| Activate cluster | ADMIN_OPS |
| Deactivate cluster | ADMIN_OPS |
| Change cluster tag | ADMIN_OPS |
| Export cluster logs | ADMIN_OPS, TASK_EXECUTE |

## License Actions

The [upload license](../../getting-started/adding-license.md) action requires the ADMIN_OPS permission.

## Code Deployment Actions

If you using Gridgain 8, all [code deployment](../deployment/code-deployment-gg8.md) actions require the ADMIN_OPS permission.

## Compute Actions

The [compute task](../compute/compute-grid.md) actions that might affect the cluster state require the following permissions:

| Action | Permission |
|---|---|
| Cancel compute task | TASK_CANCEL |
| Change priority of compute task | ADMIN_OPS |

## Node Actions

The [node](../dashboard/dashboard-overview.md) actions that might affect the cluster state require the following permissions:

| Action | Permission |
|---|---|
| Perform garbage collection | ADMIN_OPS |
| Create thread dump | ADMIN_OPS |

## Query Actions

The [query](../queries/querying.md) actions that might affect the cluster state require the following permissions:

| Action | Permission |
|---|---|
| Cancel query | KILL_QUERY |
| Kill query | KILL_QUERY |
| Execute SQL query | CACHE_READ, CACHE_CREATE, CACHE_PUT |
| Execute scan query | CACHE_READ |
| Show query history | GET_QUERY_VIEWS |
| Update configuration for running queries | ADMIN_OPS |

## Snapshot Actions

The [snapshot](../snapshots/snapshots.md) actions require the following permissions:

| Action | Permission |
|---|---|
| Create snapshot | ADMIN_OPS |
| Delete snapshot | ADMIN_CACHE |
| Copy snapshot | ADMIN_CACHE |
| Move snapshot | ADMIN_CACHE |
| Check snapshot | ADMIN_OPS |
| View snapshot list | ADMIN_VIEW |
| Restore snapshot | ADMIN_CACHE |
| Recover to snapshot | ADMIN_VIEW, ADMIN_CACHE |
| Cancel snapshot operation | ADMIN_OPS |

## Snapshot Schedule Actions

The [snapshot schedule](../snapshots/snapshot-schedules.md) actions require the following permissions:

| Action | Permission |
|---|---|
| View schedule list | ADMIN_VIEW |
| Create schedule | ADMIN_OPS |
| Delete schedule | ADMIN_OPS |
| Enable schedule | ADMIN_OPS |
| Disable schedule | ADMIN_OPS |

## Tracing Actions

The [change tracing configuration](../tracing/tracing.md) action requires the TRACING_CONFIGURATION_UPDATE permission.
