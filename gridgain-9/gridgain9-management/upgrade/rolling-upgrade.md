---
description: >-
  Move a GridGain 9 cluster between versions without downtime by rolling nodes
  one at a time, then committing the upgrade.
---

# Rolling Upgrade

{% hint style="info" %}
This feature is only available as part of GridGain 9 Enterprise and Ultimate editions.
{% endhint %}

A rolling upgrade moves the cluster from one product version to another while the data plane stays available. Nodes are restarted one at a time on the new binaries; the cluster runs in a mixed-version state for the duration of the upgrade and is promoted to the new version atomically when the operator commits.

{% hint style="info" %}
Take a [snapshot](../snapshots/data-snapshots.md) of your data before starting. If the update process fails, you will be able to restore your cluster state from snapshot.
{% endhint %}

## Limitations

### Cluster Configuration Changes Are Blocked

While an upgrade is in progress, the cluster rejects cluster-wide configuration changes. Local node-level configuration changes are still allowed. Cluster-wide configuration changes are accepted again after the upgrade is committed or cancelled.

### Schema Changes and DDL Are Blocked

While an upgrade is in progress, the cluster rejects all schema-modifying DDL: `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, index changes, distribution-zone changes, and similar statements. Read and DML operations (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) continue to work normally. DDL is accepted again after the upgrade is committed or cancelled.

### Rolling Upgrade and PITR Are Mutually Exclusive

A rolling upgrade and a point-in-time recovery (PITR) cannot run concurrently. Once a rolling upgrade has started, attempts to start PITR fail with an error naming the conflicting operation, and vice versa. The block is released when the upgrade is committed or cancelled.

### Mandatory Versions Cannot Be Skipped

A mandatory version carries changes that later versions rely on, so a rolling upgrade cannot skip it. A patch release of a mandatory version counts as that version.

If an upgrade from the version the rolling upgrade started from to the version of a joining node skips a mandatory version, the node cannot join the cluster. The error names the mandatory version. To continue, start the node on the version the upgrade started from, cancel the rolling upgrade, and upgrade the cluster to the mandatory version first.

This check does not apply to an offline upgrade, where all nodes are stopped.

{% hint style="info" %}
GridGain 9.2 has no mandatory versions.
{% endhint %}

## Rolling Upgrade Procedure

### Phase 1 — Start the Upgrade

#### Run `upgrade start`

```bash
upgrade start --version <V>
```

#### What Happens When You Start

1. The target version is validated. If it is not a valid GridGain version, the command fails immediately.
2. The cluster checks that no other cluster-wide operation (such as PITR) is in progress. If one is, the command fails with an error naming that operation.
3. The cluster records the target version and marks the upgrade as in progress. From this point, cluster-wide configuration changes are rejected.
4. The `upgrade.rolling` metrics are updated: `State` becomes `IN_PROGRESS`, `InitialVersion` records the cluster's version at the time of the start, and `TargetVersion` records the target.

The upgrade state is now durable: it survives any node restart, including the restart of any cluster-management node.

### Phase 2 — Roll the Nodes

Repeat the platform-specific procedure below for each node in the cluster, one at a time. After each node, confirm it has rejoined at the target version before moving to the next.

#### ZIP Archive

1. Stop the node.
2. If `work`, `etc`, and `log` are inside the install tree, move them outside before deleting the install tree. (If they are already outside the install tree, no action is needed.)
3. Replace the contents of the install directory with the unpacked new ZIP.
4. Copy `gridgain.properties` from the new install's `etc/` directory over the preserved file in your `etc/` directory, so that the version metadata matches the new binaries.
5. Start the node back up using the start script from the new install tree.
6. Run `upgrade state` and confirm the node appears in the `nextVersionNodes` list.

#### DEB / RPM Package

1. Stop the node.
2. Run the standard package-manager upgrade command for your distribution. The package upgrade preserves your existing `vars.env` and `gridgain-config.conf` files in a `backup/` subdirectory under the configuration directory and registers the service unit for the new binaries. The persistent `work` directory is left untouched.
3. Restart the GridGain service using `systemctl` (or the equivalent for your init system).
4. Run `upgrade state` and confirm the node appears in the `nextVersionNodes` list.

#### Docker

1. Stop the container for this node.
2. Update the image tag in your run command, Compose file, or Kubernetes manifest to the new version.
3. Start the container against the same persistent volume that holds `work`, `etc`, and `log`.
4. Run `upgrade state` and confirm the node appears in the `nextVersionNodes` list.

After all nodes are upgraded, proceed to phase 3.

### Phase 3 — Complete the Upgrade

#### Run `upgrade commit`

```bash
upgrade commit
```

#### What Happens on Commit

1. The cluster reads the current upgrade state and the list of active nodes.
2. The cluster validates that every active node is running the target version. If any node is still on the source version, the commit fails with an error listing the offending nodes by name and reported version.
3. The cluster validates that every node it knows about has rejoined fully. If a node has not rejoined, the commit fails with an error.
4. When upgrading from 9.1, the cluster [converts existing role names](#role-and-user-names-when-upgrading-from-9.1) to the case-sensitive form used in 9.2. If the conversion fails, the commit fails with an error, the cluster stays on the source version, and the upgrade remains in progress. After you fix the cause, run `upgrade commit` again.
5. The cluster's recorded version is set to the target version, the in-progress flag is cleared, and cluster-wide configuration changes are accepted again.
6. Cluster-wide features that depend on the new version are activated.
7. The `upgrade.rolling` metric `State` becomes `NOT_STARTED`.

#### Role and User Names When Upgrading from 9.1

GridGain 9.1 treats user and role names as case-insensitive and stores them in lower case. GridGain 9.2 treats them as case-sensitive and uses them exactly as written. When you commit an upgrade from 9.1, GridGain converts the stored names so that existing users keep their access:

- **Role names** are converted to upper case: the role `admin` becomes `ADMIN`. The roles assigned to users are updated to match. The built-in `system` role keeps its name, and an assignment of `system` spelled in any other case becomes `system`.
- **User names** are not changed. Every user created on 9.1 keeps the lower-case name it was stored under, even if it was created with `CREATE USER Alice` or `CREATE USER ALICE`.

Until you commit, the cluster keeps matching role names without regard to case. User names are different: a node matches them exactly as soon as it runs 9.2, so a login with a different spelling can fail on upgraded nodes while you are still rolling.

After the commit, check the following:

- **Log in with the stored name.** A user stored as `alice` must log in as `alice`. Logging in as `ALICE` or `Alice` worked on 9.1 and now fails with an invalid-credentials error. Update client connection settings, scripts, and applications that use a different spelling. To see the stored names, run `SHOW USERS`.
- **Quote user names in SQL.** SQL converts an unquoted name to upper case, so `DROP USER alice` looks for the user `ALICE`, which does not exist. Write `DROP USER "alice"`, `ALTER USER "alice" SET PASSWORD '...'`, and `GRANT ADMIN TO "alice"`. Role names do not need quotes, because the converted names are upper case.
- **Quote `system` in SQL.** An unquoted `system` is read as `SYSTEM`, which is an ordinary role and not the built-in super role. Write `"system"`.
- **Do not recreate old users with an unquoted name.** `CREATE USER alice` creates a new user `ALICE`, separate from the existing `alice`.
- **Expect `CURRENT_USER` to return the stored name.** For users created on 9.1 it is lower case. Row-level security policies that compare `CURRENT_USER` to data must use the same spelling.
- **Update LDAP role mappings.** The `roleMapping` values are not converted. A mapping that names a role in lower case, such as `admin`, no longer matches the role `ADMIN` and grants nothing. Change the values to match the new role names. LDAP group names are still matched without regard to case.
- **Review row-level security policies.** Policies are not converted, and policy roles are matched exactly. A policy that names a former lower-case role in quotes stops applying to the converted upper-case role. A policy created with an unquoted `TO SYSTEM` stores `SYSTEM` and no longer applies to holders of `system`. Recreate it with `TO "system"`. Depending on your other policies, users can see more or fewer rows than before, so check each policy.
- **Expect users to log in again.** Existing JWTs are not rewritten and expire normally. A token that carries `SYSTEM` loses the super role's privileges until the user logs in again. Existing sessions may also need to reconnect.

To switch a user to a different spelling, for example upper case, create a new user with the new name, grant it the same roles, and drop the old user. User names cannot be renamed.

The conversion state is stored in the [`roleNamesMigrationVersion`](../../reference/configuration/cluster-configuration-parameters.md) cluster configuration parameter. Do not change it manually.

After the commit, you cannot return to a 9.1 binary without a recovery plan, because the stored role names and the `roleNamesMigrationVersion` value have changed. To go back, [cancel the upgrade](#cancelling-an-in-progress-upgrade) before you commit. Cancel requires every node to be back on the source binaries first.

## Monitoring Update Progress

### The `upgrade state` Command

Returns four fields:

- `currentVersion` — the cluster's recorded version (the source version while the upgrade is in progress).
- `nextVersion` — the target version, or `null` when no upgrade is in progress.
- `nextVersionNodes` — names of nodes whose running version equals `nextVersion`.
- `currentVersionNodes` — names of nodes whose running version equals `currentVersion`.

### Metrics

The metric source `upgrade.rolling` exposes the following gauges:

- `State` — `NOT_STARTED` or `IN_PROGRESS`.
- `InitialVersion` — cluster version at the time the upgrade started; empty when no upgrade is in progress.
- `TargetVersion` — target version; empty when no upgrade is in progress.
- `UpgradedNodes` — comma-separated list of node names that have reached the target version.
- `NotUpgradedNodes` — comma-separated list of node names still on the source version.

## Recovery and Abort

### Cancelling an In-Progress Upgrade

#### Run `upgrade cancel`

```bash
upgrade cancel
```

#### Preconditions for Cancel

The cancel operation validates that every active node is on the source version. If any node is still on the target version (that is, it has been rolled forward to the new binaries), the cancel fails with an error listing the offending nodes. To cancel after binaries have been swapped on some nodes, the operator must first roll those nodes back to the source binaries.

When cancel succeeds, the cluster clears the in-progress flag while leaving the recorded version unchanged, accepts cluster-wide configuration changes again, and releases the block that prevents PITR from starting.

### Resuming After a Coordinator or Cluster-Management Node Restart

The upgrade state is durable across cluster restarts and cluster-management leader failover. You can safely restart your CLI session, and any cluster-management node reboot during a roll does not require restarting the upgrade. When a node rejoins after a restart, it picks up the in-progress upgrade state from the cluster and applies the cluster-wide configuration block locally.

### Handling Dead or Unresponsive Nodes

#### Reviving a Node at the Target Version

A node that was upgraded but is currently down does not appear as an active cluster member and is not counted toward upgrade progress. Bring it back up on the target binaries; it will rejoin and `upgrade state` will surface it under `nextVersionNodes`.

#### Evicting an Unrecoverable Node

A node that the cluster knows about but that has not rejoined fully blocks `upgrade commit`. Remove the node from the cluster following the standard topology-management procedure, then retry commit.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
