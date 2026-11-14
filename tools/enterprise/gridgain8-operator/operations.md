---
description: >-
  Day-two operations for a GridGainCluster: scale, rotate secrets, and what the
  operator does not back up.
---

# Operations

## Scale

Change `spec.replicas`. Scale-up is a StatefulSet scale. Scale-down, while operator-managed upgrades are on, drains the highest ordinal, waits for supply, then patches `replicas`. The operator never writes your spec for you.

A scale-down is held while an upgrade is `Failed` or `RolledBack`. See [Drain and Graceful Shutdown](drain.md#scale-down).

Park a cluster with `spec.replicas: 0`. In-memory data is discarded.

## Rotate Secrets

* **License value** (same Secret name and key): hot-reload, no pod restart. See [License](license.md).
* **License Secret name or mount path**: pod template change; one node at a time. See [Updates](updates.md#change-configuration).
* **Auth password Secret value**: kubelet updates the projected file; the operator re-reads it on the next drain. Enabling auth or changing the username/Secret **name** rolls the cluster (Auth gate on).

## Backup

The operator does **not** orchestrate backup Jobs, persistence snapshots, or VolumeSnapshots. There is no Backup custom resource. Copy any data you need before you scale to zero or restart nodes with `backups=0` caches.

## Configuration Changes

Edit the `GridGainCluster` spec. Template changes restart one node at a time. Image **version** changes require scale to zero. See [Updates](updates.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
