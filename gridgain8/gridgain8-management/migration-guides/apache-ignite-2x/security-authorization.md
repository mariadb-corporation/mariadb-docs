---
description: >-
  How to migrate authorization from a secured Apache Ignite 2.x cluster to
  GridGain 8: retired permissions, coarser admin grants, and user management.
---

# Security Authorization Changes

This page explains how to migrate authorization when moving a secured Apache Ignite 2.x cluster to GridGain 8. It covers the authorization differences that affect users, roles, and administrative operations. This guide is verified against Apache Ignite 2.18; on earlier 2.x releases some of these permissions may not exist yet.

To move a custom `GridSecurityProcessor` or Ignite built-in authentication to GridGain enterprise security, see the _Custom security plugins_ entry in [Features to Replace](features-to-replace.md). For the full list of permission names and how to configure them, see [Authorization and Permissions](../../../security/authorization-permissions.md).

## Overview

Most authorization permissions remain unchanged. Before you start GridGain 8, check your configuration for the nine Apache Ignite 2.x permission names that GridGain 8 no longer recognizes, and replace or remove them using the [table below](#permissions-that-changed).

Three differences require attention. They stem from fine-grained authorization permissions that Apache Ignite 2.18 defines but GridGain 8 does not:

* Nine fine-grained permissions are not part of GridGain 8's permission set. Replace or remove them. See [Permissions that changed](#permissions-that-changed).
* Some admin operations are now authorized by the single `ADMIN_OPS` permission instead of separate ones. See [Coarser admin permissions](#coarser-admin-permissions).
* User management no longer uses a grantable permission; it follows a fixed rule. See [User management](#user-management).

{% hint style="warning" %}
GridGain 8 accepts only its own predefined permission names. If your configuration names any retired Apache Ignite permission (or any unknown name), GridGain rejects the security configuration, and the node fails to start. *Replace or remove all nine permissions below before you start the cluster.*
{% endhint %}

## Permissions that changed

| Permission in your Ignite 2.x policy | What it controlled | What to do on GridGain 8 |
|---|---|---|
| `ADMIN_CLUSTER_STATE` | Activate / deactivate / change cluster state | Grant `ADMIN_OPS` |
| `ADMIN_CLUSTER_NODE_START` / `ADMIN_CLUSTER_NODE_STOP` | Start / stop / restart nodes | Grant `ADMIN_OPS` |
| `ADMIN_SNAPSHOT` | Create / restore / cancel snapshots | Grant `ADMIN_OPS` |
| `ADMIN_ROLLING_UPGRADE` | Enable rolling upgrade and change its mode | Grant `ADMIN_OPS` |
| `ADMIN_KILL` | Cancel running compute tasks, services, transactions, queries (the `--kill` family) | Grant `KILL_QUERY` for SQL query cancellation. Other cancellation types have no single replacement (see [Coarser admin permissions](#coarser-admin-permissions)) |
| `ADMIN_USER_ACCESS` | Create / alter / drop users | Remove it. User management is not a permission (see [User management](#user-management)) |
| `SQL_VIEW_CREATE` / `SQL_VIEW_DROP` | Create / drop user-defined SQL views | Remove them. GridGain 8 has no user-defined SQL views |

All other permission names keep the same behavior, including cache, task, service, event, and the remaining administrative permissions. For the complete list, see [Authorization and Permissions](../../../security/authorization-permissions.md).

## Coarser admin permissions

Apache Ignite 2 split cluster administration into fine-grained permissions so you could, for example, allow a role to change cluster state but not stop nodes. GridGain 8 does not have that split. Cluster-state changes, baseline changes, node start/stop, snapshot operations, and rolling-upgrade control all require `ADMIN_OPS`.

A role that needs any one of these actions effectively gets all of them. If your Ignite policy assigned these operations to different roles, GridGain 8 cannot preserve that separation, because they all require `ADMIN_OPS`. Review whether the broader `ADMIN_OPS` grant is acceptable under your least-privilege requirements before you migrate those roles.

Cancellation operations are a related case. Apache Ignite grouped them under the `ADMIN_KILL` permission. GridGain 8 replaces only SQL query cancellation, with `KILL_QUERY`. Other cancellation operations (compute tasks, services, transactions, continuous and scan queries) are authorized as part of the underlying operation rather than by a dedicated kill permission. Review each cancellation workflow individually instead of assuming a single replacement permission.

## User management

In Apache Ignite 2, creating, altering, and dropping users is controlled by the `ADMIN_USER_ACCESS` permission. GridGain 8 uses a fixed rule instead. With built-in authentication:

* Only the default user (`ignite`) may create, alter, or drop other users.
* Any other user may change only their own password.
* The default user cannot be deleted.

This rule is not configurable and is not tied to any grant.

*What to do:* remove `ADMIN_USER_ACCESS` from your policy. If your Ignite setup let a non-default administrative role manage users, that arrangement does not carry over. Perform user administration using the default `ignite` user. To delegate user administration to other roles, use GridGain enterprise security with an external identity provider rather than built-in authentication.

## User-defined SQL views

GridGain 8 uses the H2 SQL engine and does not support user-defined SQL views. Remove `SQL_VIEW_CREATE` and `SQL_VIEW_DROP` from your policy.

## If you maintain a custom security implementation

Most deployments configure security through files and never touch code. If you are the exception and built a custom security provider in Java that references the removed permission names directly, that code will not compile against GridGain 8, because GridGain's `SecurityPermission` enum does not define the corresponding constants. Replace those references according to [Permissions that changed](#permissions-that-changed): use `ADMIN_OPS`, use `KILL_QUERY`, or remove the permission entirely. Only the permissions listed in [Authorization and Permissions](../../../security/authorization-permissions.md) are valid.

## Migration checklist

1. Locate permission grants in your security configuration (role definitions, permission sets) that name any of the nine changed permissions.
2. Replace or remove them per [Permissions that changed](#permissions-that-changed): cluster, node, snapshot, and rolling-upgrade admin → `ADMIN_OPS`; SQL kill → `KILL_QUERY`; user management and SQL views → remove.
3. Move user administration to the default `ignite` user and drop `ADMIN_USER_ACCESS`.
4. Review any role that now requires the broader `ADMIN_OPS`, and confirm that is acceptable under least privilege.
5. Start a secured node. If GridGain reports an unknown permission, remove or remap the offending Ignite 2.x permission before retrying.
6. Test each migrated role end to end: cluster activate/deactivate, baseline change, node stop, SQL `KILL QUERY`, and user create/drop.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
