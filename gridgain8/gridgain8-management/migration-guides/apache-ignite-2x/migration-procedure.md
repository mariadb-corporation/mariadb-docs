---
description: >-
  Step-by-step procedure for migrating a cluster, its data, clients, and tooling
  from Apache Ignite 2.18 to GridGain 8.10, with cutover, verification, and rollback.
---

# Migrating from Apache Ignite 2 to GridGain 8

This guide provides step-by-step instructions for migrating from Apache Ignite 2.18 to the [GridGain 8.10 Ultimate release]({release-notes}/8.10/release-notes_8.10). The procedure covers the cluster and its data, client applications and operational tooling.

Before you start, read [What to Know Before Migrating](before-you-migrate.md). It covers the compatibility model, the features you need to migrate, and the artifact, configuration, and SQL changes this guide refers to.

Work through the phases below in order:

1. [Prerequisites](#prerequisites) — a short gate before any work starts: the license, the downtime window, and the distributions are in place; persistent clusters also need backup storage.
2. [Check compatibility](#check-compatibility) — discovery: you find which differences between Ignite and GridGain affect your deployment. The result is your migration work list.
3. [Prepare configuration and code](#prepare-configuration-and-code) — the bulk of the migration, on staging, with production untouched: artifacts, configuration, feature replacements, clients, and SQL, over several rounds, by operators and application teams in parallel. Done when the [preparation criteria](#when-is-preparation-complete) pass.
4. [Perform the cutover](#perform-the-cutover) — the production event: the cluster stops, restarts on GridGain with its data carried over (persistent) or reloaded (in-memory), and the rebuilt clients reconnect. The only downtime, and for persistent clusters the only irreversible part. Done when the cutover criteria pass.
5. [Verify and stabilize](#verify-and-stabilize) — confirmation under real load: data, functionality, performance, and monitoring all check out before you call the migration complete.

{% hint style="warning" %}
Do not begin the cutover until the preparation criteria are met.
{% endhint %}

If a step in the cutover fails and you cannot fix it quickly, fall back to [Rollback](#rollback).

## Persistent and In-Memory Clusters

The procedure covers clusters that use [Native Persistence](../../../architecture/storage/native-persistence.md) and clusters that keep data only in memory. The phases are the same for both. The difference is what happens to the data at the cutover:

- *Persistent cluster.* GridGain starts directly on Ignite's persistence files. Follow the steps marked _persistent only_: leave the data in a clean state and back it up first, because once GridGain writes to it, the migration is one-way.
- *In-memory cluster.* GridGain starts empty. Skip the steps marked _persistent only_ and reload the data at [step 9]().
- *Mixed cluster.* Follow the persistent path, including every step marked _persistent only_, and additionally reload the in-memory caches at [step 9]().

## Which Phases Apply to You

Everything migrates together in one cutover, because Ignite and GridGain server nodes and clients cannot mix. Which phases you work through depends on your role:

- *You administer the cluster* — you install, configure, and run the server nodes. All five phases are required.
- *You develop a client application* that connects to a cluster someone else administers. Your main work is in [Check Compatibility](#check-compatibility) and [Prepare Configuration and Code](#prepare-configuration-and-code): rebuild the application against GridGain artifacts and re-test it. You are also needed during the [cutover](#perform-the-cutover), where you stop the application, reconnect the rebuilt version, and take part in the smoke test, and in [Verify and Stabilize](#verify-and-stabilize), where you run the application workload. The rebuilt application must not connect to the production cluster before the cutover, so coordinate the switch with the cluster administrators.
- *You maintain operational tooling* — monitoring, scripts, automation. Your main work is in [Check Compatibility](#check-compatibility) and [Prepare Configuration and Code](#prepare-configuration-and-code): adapt the tooling to the CLI, logging, and metrics changes. In [Verify and Stabilize](#verify-and-stabilize), you reconnect monitoring and confirm that dashboards and alerts show data.

## Prerequisites

You arranged these during planning (see [Before You Begin](before-you-migrate.md#before-you-begin)); confirm all of them before you start:

- You understand the [migration constraints](before-you-migrate.md#migration-constraints), most importantly that for a persistent cluster this is a one-way upgrade with no in-place rollback once GridGain writes to the data directory.
- A valid GridGain 8 Ultimate [license](../../licensing.md) is installed.
- The downtime window for the full cluster cutover is scheduled.
- _Persistent only:_ storage for a complete backup of the persistence directory is reserved.
- The GridGain distribution is in place, and your current Apache Ignite distribution is archived for rollback.

## Check Compatibility

Most migration work is conditional: each area below may or may not apply to your deployment. Review every area and record each item that applies:

1. *Review the features to replace.* CDC, snapshots, Metrics API, Read Repair, and the other features that work differently or are absent in GridGain. Each entry in [Features to Replace](features-to-replace.md) starts with whether it applies to you.
2. *Review the configuration changes.* Changed defaults, removed properties, stricter validation, and the binary field-sort setting. See [Configuration and Validation Changes](configuration.md).
3. *Review the client changes.* All clients are rebuilt; record the per-language changes for Java, .NET, C++, Python, JDBC, ODBC, and REST. See [Clients](apis-and-clients.md#clients).
4. *Review the SQL changes.* The engine change to H2 and the SQL memory quotas. See [SQL Changes](apis-and-clients.md#sql-changes).
5. *Review the deployment and artifact changes.* Distribution, build coordinates, Docker, modules and extensions. See [Artifacts and Deployment](artifacts-and-modules.md).
6. *Review the monitoring and CLI changes.* Logs, metrics, system views, events, and the scripts and automation that call `control.sh` and `ignite.sh`. See [Monitoring and CLI Changes](operations.md).

{% hint style="info" %}
You are done with this phase when you have gone through every area above and written down the items that apply to you. That list is your migration work list: every item on it must be addressed and tested in the next phase, before you cut over.
{% endhint %}

## Prepare Configuration and Code

Do all of this on a separate staging GridGain cluster while your Apache Ignite cluster stays in production. None of it requires downtime, and nothing here touches the production cluster. Stand up the staging cluster, load it with representative data, then apply each change below and test it there, fixing failures and re-testing until everything passes. The cutover later applies the configuration you settle on here to production.

### Preparation Tasks

1. *Update artifacts.* Apply the build-coordinate and packaging changes for your languages and deployment method. See [Artifacts and modules](artifacts-and-modules.md).
2. *Migrate server configuration.* Set the changed defaults explicitly, remove Ignite-only properties, and resolve the stricter validation rules. See [Server configuration differences](configuration.md).
3. *Replace big features.* For each big feature on your task list, implement and test the GridGain equivalent now. These are the highest-effort changes. See [Features to Replace](features-to-replace.md).
4. *Update clients and SQL.* Recompile clients against GridGain artifacts, remove Calcite configuration, and re-test every query on the H2 engine. Decide your SQL memory-quota policy (keep the GridGain default, tune it, or set `sqlGlobalMemoryQuota=0`) and test the choice with production-scale queries. See [SQL changes](apis-and-clients.md#sql-changes).
5. *Update operational scripts.* Adjust automation that calls `control.sh` and `ignite.sh` for removed or renamed commands and the changed restart mechanism. See [CLI changes](operations.md).
6. *Check the binary field-sort setting.* _Persistent only._ See [Binary object field ordering](configuration.md). If the source uses the default, skip the related cutover step.

Begin with *Update artifacts* (step 1). Once the GridGain libraries are in place, work through feature replacement, configuration changes, and SQL validation (steps 2–5), revisiting them as staging tests uncover issues.

### Common Pitfalls

- *Feature replacements take the most time.* Data Center Replication, enterprise snapshots, and enterprise security usually require their own implementation and validation work. Start them early and test each one in staging.
- *Choose the binary field-sort value early* (persistent clusters). `IGNITE_BINARY_SORT_OBJECT_FIELDS` affects the on-disk and on-wire layout, so fix it before loading staging data, use it consistently, and carry the same value into the cutover (step 6).
- *Validate with realistic workloads.* Production-scale datasets and query patterns expose H2 optimizer and type-coercion differences and SQL memory-quota issues that small staging datasets hide.
- *Do not connect updated clients to production.* GridGain clients are incompatible with an Apache Ignite cluster, so keep rebuilt clients on staging until you reconnect them during the cutover (step 10).

### When Is Preparation Complete?

{% hint style="warning" %}
Preparation is complete only when all of these are true on staging:

- The cluster starts cleanly with your migrated configuration.
- Your rebuilt clients connect and pass functional tests.
- Every feature replacement on your work list works under a realistic workload.

Do not begin the cutover until all three hold.
{% endhint %}

You will go through several rounds to get there. It is normal at this stage for configuration to be rejected, for queries to fail or run slowly, and for some replacements to be unfinished. Fix each problem in your configuration or client code and test again on staging. Fixing it now is much cheaper than fixing it during the cutover, when the cluster is down.

If you cannot finish a replacement, use a temporary workaround or drop the feature. Test that decision on staging too. Once GridGain writes to persisted data, you cannot roll back.

A clean run on staging shows that your changes work. It does not show that staging behaves like production. If staging has less data, fewer kinds of queries, or different client versions, a passing test can still hide problems. Make staging match production before you trust the results.

## Perform the Cutover

Start only once [preparation is complete](#when-is-preparation-complete). Do the following with the cluster down, strictly in the order shown. Do not reorder or skip steps, except the steps marked _persistent only_ or _in-memory only_ that do not apply to your cluster.

The cutover has three parts:

- [steps 1–4]() take the cluster down cleanly and secure your way back;
- [steps 5–7]() switch it to GridGain;
- [steps 8–11]() bring the service back: verify the cluster, reload the data if nothing was carried over, reconnect clients, and smoke-test. On a persistent cluster, the point of no return is [step 7](): once GridGain writes to the data, the migration is irreversible.

### 1. Stop Running Applications

Drain and stop all application clients and CDC processes.

### 2. Deactivate the Cluster (Persistent Only)

Deactivating forces a final checkpoint.

```shell
$IGNITE_HOME/bin/control.sh --set-state INACTIVE   # confirm with 'y'
$IGNITE_HOME/bin/control.sh --state                # expect: Cluster state: INACTIVE
```

### 3. Shut Down All Nodes

Stop the nodes gracefully, in any order, and wait for each process to exit. The order does not matter because the cluster is already deactivated (persistent) or its data is not being kept (in-memory). On a persistent cluster, the graceful stop lets the final checkpoint complete cleanly.

### 4. Back Up the Persistence Directory (Persistent Only)

Copy the whole work directory, including `db/`, `db/binary_meta/`, `db/marshaller/`, and the WAL. Also archive the Ignite binary distribution and its configuration so you can rebuild the pre-migration cluster if needed.

```shell
tar czf ignite-pds-backup-PRECUTOVER.tgz $IGNITE_HOME/work/db
```

{% hint style="danger" %}
Once GridGain starts and writes, this backup is the only way back to Apache Ignite. Before continuing, verify it exists, check that its size is what you expect, and copy it off the node.
{% endhint %}

### 5. Configure GridGain 8

Apply your prepared GridGain configuration.

_Persistent only:_ the GridGain node must use the *same `consistentId`* and the *same persistence directory* as the Ignite node it replaces. Point GridGain's `workDirectory` at the existing work directory, or copy `db/` into GridGain's work directory.

{% hint style="info" %}
Because each GridGain node reuses the same `consistentId` and persistence directory as the Ignite node it replaces, the baseline topology (part of the persisted cluster metadata) is carried over with the data. You do not reset or re-create it during the migration.
{% endhint %}

### 6. Match the Field-Sort Setting (Persistent Only)

If the source explicitly set `IGNITE_BINARY_SORT_OBJECT_FIELDS`, pass the same value as `-DIGNITE_BINARY_SORT_OBJECT_FIELDS=<source-value>` on every GridGain node and client. Otherwise, leave it unset. See [Binary object field ordering](configuration.md).

### 7. Start GridGain

Start every server node with your migrated configuration:

```shell
$GRIDGAIN_HOME/bin/ignite.sh <your-migrated-config>.xml
```

On an in-memory cluster, the nodes start with fresh storage and the cluster is active as soon as they join. Continue to step 8.

On a persistent cluster, start one node first, confirm the recovery lines below in its log, and then start the rest. The cluster reports `INACTIVE` until every baseline node has joined; if it stays that way, see [Problem: The cluster stays INACTIVE after the start](#problem-the-cluster-stays-inactive-after-the-start).

The log must show GridGain restoring your data — this confirms it opened the migrated persistence rather than creating fresh storage. Output is trimmed here; cache names, counts, and IDs differ on your cluster:

```text
Binary memory state restored at node startup [restoredPtr=...]
Started cache in recovery mode [name=OrderCache, ...]
Started cache in recovery mode [name=CustomerCache, ...]
Started cache in recovery mode [name=ProductCache, ...]
Finished restoring partition state for local groups [groupsProcessed=4, ...]
```

After all nodes have joined, each node finishes with:

```text
Topology snapshot [ver=1, servers=1, clients=0, state=ACTIVE, ...]
Ignite node started OK (id=8f3a...e21)
```

If the recovery lines are missing or your caches are absent, stop: see [Problem: GridGain starts, but the data is gone](#problem-gridgain-starts-but-the-data-is-gone).

GridGain upgrades partition-metadata page versions on first write. From this point on, the migration of a persistent cluster is irreversible.

### 8. Activate and Verify

```shell
$GRIDGAIN_HOME/bin/control.sh --set-state ACTIVE
$GRIDGAIN_HOME/bin/control.sh --state         # expect: Cluster is active
$GRIDGAIN_HOME/bin/control.sh --cache list .  # expect your caches
```

`--state` and `--cache list` confirm the cluster is up with your caches. On an in-memory cluster, activation is automatic and `--set-state ACTIVE` is a harmless confirmation; the caches are empty until the next step, so check the state and the cache list and skip the row-count checks below. Output is trimmed here; note that GridGain's `--state` output format differs from Apache Ignite's `Cluster state: ACTIVE`, so update any scripts that parse it:

```text
Cluster is active

[cacheName=CustomerCache, ..., mode=PARTITIONED, atomicity=TRANSACTIONAL, ..., cacheSize=500]
[cacheName=OrderCache, ..., mode=PARTITIONED, atomicity=TRANSACTIONAL, ..., cacheSize=1000]
[cacheName=ProductCache, ..., mode=PARTITIONED, atomicity=ATOMIC, ..., cacheSize=100]
```

The `cacheSize` values give you a first row-count check before you query anything.

_Persistent only:_ spot-check row counts with `sqlline` and confirm they match the pre-cutover values:

```sql
0: jdbc:ignite:thin://127.0.0.1/> SELECT COUNT(*) FROM Customer;
+----------+
| COUNT(*) |
+----------+
| 500      |
+----------+
```

{% hint style="info" %}
These checks need nothing special, including `SELECT *`. Only selecting the hidden `_VAL` or `_KEY` system column can fail on a missing application class; if you need that, add `keepBinary=true` to the JDBC URL (see [Problem: sqlline fails to deserialize values](#problem-sqlline-fails-to-deserialize-values)).
{% endhint %}

### 9. Reload the Data (In-Memory Only)

This step applies to in-memory clusters and to the in-memory data regions of a mixed cluster; the persistent data is already in place from step 7.

Repopulate the caches the way you repopulate Ignite after any restart:

- Preload the caches from the database that backs them, the same way you warm them up on Ignite.
- Re-run your data-loading jobs.
- Or let the caches fill once clients reconnect (step 10): read-through caches load entries on first access.

If you copied data out before the cutover because it had no external source to reload from, load it back now. When loading completes, spot-check row counts against the source.

### 10. Reconnect Updated Clients

Bring up the clients you rebuilt against GridGain artifacts and connect them to the GridGain cluster.

### 11. Run an End-to-End Smoke Test

Run a minimal write, read, and query path through the real application stack.

{% hint style="warning" %}
The cutover has succeeded when all of these hold:

- The cluster reports `ACTIVE` and `--cache list` shows your caches (step 8).
- The data is in place: spot-checked row counts match the pre-cutover values (persistent, step 8), or the reload completed and matches its source (in-memory, step 9).
- The end-to-end smoke test passes (step 11).

If any of these fail and cannot be fixed quickly, restore the cluster using the procedure in [Rollback](#rollback). Do not leave the cluster partially migrated.
{% endhint %}

## Verify and Stabilize

With the cluster live on GridGain, confirm it is healthy before you consider the migration complete:

1. *Check data integrity.* Compare full row counts per cache against the pre-cutover values (persistent) or the reload source (in-memory), then run `control.sh --cache idle_verify`. A healthy run reports no conflicts:

   ```text
   idle_verify check has finished, no conflicts have been found.
   ```
2. *Run the real workload.* Run your regression suite or production workload end to end and confirm it passes.
3. *Watch performance over the first days.* Look for SQL memory-quota failures on large queries, since GridGain enables SQL memory quotas by default. If a query that worked in Ignite now fails, tune `sqlGlobalMemoryQuota` or set it to `0`. See [SQL changes](apis-and-clients.md#sql-changes).
4. *Reconnect monitoring.* Update log parsing for the new file-name pattern and quiet-mode default, and move any removed metrics, system-view, or event usages to JMX or the `SYS` schema. Confirm your dashboards and alerts show data again.
5. *Re-establish backups.* Recreate your backup regime with GridGain snapshots, because Ignite snapshots are not compatible. Take a first snapshot and confirm it completes.

{% hint style="warning" %}
The migration is complete when data integrity, application functionality, performance, and monitoring all check out under the production workload. On a persistent cluster, keep the pre-cutover backup and the archived Ignite distribution until then. They are your only path back.
{% endhint %}

## Troubleshooting

These are the problems that come up most often during this migration. If you hit something not covered here, contact your GridGain Account Executive or [GridGain Support](https://support.gridgain.com/).

### Problem: GridGain starts, but the data is gone

The node comes up on an empty baseline with none of your caches.

**Cause:** The GridGain node is not using the same identity or directory as the Ignite node it replaces, so it created fresh storage instead of opening the migrated data.

**Fix:** Stop the node. Confirm it uses the *same `consistentId`*, and that `workDirectory` points at the migrated `db/` (step 5). Restart.

### Problem: The cluster stays INACTIVE after the start

Nodes are up, but the `Topology snapshot` log line or `control.sh --state` reports `INACTIVE`.

**Cause:** A persistent cluster activates only after every node of the carried-over baseline has joined. The `Topology snapshot` line can also show `INACTIVE` when it is logged an instant before auto-activation completes; on its own, this is not a failure.

**Fix:** Start the remaining baseline nodes, then look for `Cluster state was changed from INACTIVE to ACTIVE` in the log or confirm with `control.sh --state`. If all nodes are up and your caches are listed but the cluster has not activated, activate it manually (step 8). If the cluster is `INACTIVE` with none of your caches, see [Problem: GridGain starts, but the data is gone](#problem-gridgain-starts-but-the-data-is-gone).

### Problem: GridGain refuses to start on the persistence

Startup fails while reading the existing data.

**Cause:** The data was not left in a clean state: the cluster was not deactivated and shut down gracefully, CDC was still enabled at the last write, or the binary field-sort setting differs from the source.

**Fix:** These are preconditions, not post-fixes. Restore the pre-cutover backup, bring the Ignite cluster back, deactivate it cleanly with CDC stopped, and redo the cutover. Match `IGNITE_BINARY_SORT_OBJECT_FIELDS` to the source value (step 6).

### Problem: Do I have to activate manually?

The cluster is already `ACTIVE` before you run `--set-state ACTIVE`.

**Cause:** GridGain can auto-activate from the persisted baseline on first start, and a cluster without persistence is always active once it forms, so the explicit activation in step 8 is sometimes a no-op.

**Fix:** This is expected. Running `--set-state ACTIVE` against an already-active cluster is harmless; keep it as a confirmation step.

### Problem: Enterprise features will not start

Nodes start, but Ultimate features fail, or startup aborts on a license error.

**Cause:** Missing or expired GridGain Ultimate license.

**Fix:** Install a valid license (see [Prerequisites](#prerequisites)).

### Problem: sqlline fails to deserialize values

Counts and column queries (including `SELECT *`) work, but selecting the `_VAL` or `_KEY` system column fails with a serialization error caused by `ClassNotFoundException` on your key or value class.

**Cause:** `keepBinary` defaults to `false`, so selecting `_KEY` or `_VAL` deserializes the whole object into its Java class, and application classes are not on the `sqlline` classpath. Primitive keys and values are unaffected, as are declared columns, which are extracted on the server.

**Fix:** Verify data through the declared columns. To select the object itself, add `keepBinary=true` to the JDBC URL; it is returned in binary form, rendered as an opaque numeric value rather than field values. If you instead fix it by adding your classes to the classpath, note that `sqlline` takes JVM options from `SQL_JVM_OPTS`, not `JVM_OPTS`.

### Problem: sqlline output looks truncated or columns are missing

A wide query, such as `SELECT *`, displays fewer columns than the table has, cuts values mid-string, or shows blank column headers.

**Cause:** `sqlline` truncates its table output at the display width (80 characters by default) without marking the truncation. It is a display issue, not a data problem, and is unrelated to `keepBinary`.

**Fix:** Re-run with `--maxWidth=<n>`, or use `--outputformat=csv`, which does not truncate. Judge data integrity by row counts and `idle_verify`, never by how output renders.

### Problem: Queries that worked in Ignite now fail

Queries error out or behave differently after the cutover.

**Cause:** GridGain enables SQL memory quotas by default, and dropping Calcite moves you onto the H2 engine, which optimizes and coerces types differently.

**Fix:** Tune `sqlGlobalMemoryQuota` (or set it to `0`), and re-test queries on H2 in staging before the cutover. See [SQL changes](apis-and-clients.md#sql-changes).

## Rollback

On an in-memory cluster, rollback is simply a restart on the old version: stop GridGain, start the archived Apache Ignite distribution with the original configuration, reconnect the original clients, and reload the data as after any restart.

On a persistent cluster, rollback is possible only by restoring the backup you took during the cutover onto the archived Ignite binaries. There is no in-place path once GridGain has written:

1. Stop the GridGain cluster.
2. Restore the pre-cutover backup to a clean work directory.
3. Start the archived Apache Ignite distribution against the restored data.
4. Activate, verify, and reconnect the original Ignite clients.

Keep the backup and the archived Ignite binaries until the migration has been validated in production.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
