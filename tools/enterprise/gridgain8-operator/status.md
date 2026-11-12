---
description: >-
  GridGainCluster status phases, upgrade phases, conditions, and events to
  inspect when a cluster is not Ready.
---

# Status and Events

```sh
kubectl get gridgaincluster
kubectl describe gridgaincluster gridgaincluster
```

## Cluster Phase

`status.phase` is a high-level summary.

| Phase | Meaning |
| ----- | ------- |
| `Pending` | Not running yet. A one-replica cluster waits here until `spec.upgrade.allowSingleReplicaRoll` is true. |
| `Provisioning` | Pods are being created. |
| `Ready` | Desired replicas are Ready. |
| `Degraded` | Some replicas are not Ready. |
| `Failed` | The operator stopped progressing. Read `status.upgrade` for a stuck configuration restart. |
| `Terminating` | The custom resource is deleting. |

Also watch `status.replicas`, `status.readyReplicas`, and `status.observedGeneration`.

## Conditions

| Type | Role |
| ---- | ---- |
| `Available` | True when Ready replicas equal `spec.replicas`. |
| `Progressing` | True while a rollout is incomplete. |
| `UpgradeComplete` | Tracks operator-managed configuration restarts. |
| `DrainBlocked` | True when the drain gate aborted, or after five minutes of waiting on supply. Reasons match `status.upgrade.drainReason` when aborted, or `SupplyInProgress` while waiting. `NotBlocked` when idle. |

`FeatureGateDisabled`, `UnsafeCustomConfig`, and `ForeignObjectNameTaken` appear as condition reasons and Warning events when those checks fail.

## Upgrade Status

`status.upgrade` reports a configuration restart, not a GridGain version upgrade.

| Field | Meaning |
| ----- | ------- |
| `phase` | `Idle`, `Pending`, `Rolling`, `Retrying`, `Failed`, `Complete`, `RolledBack` |
| `stuckOrdinal` | Pod ordinal that did not become Ready |
| `recoveryToken` | Copy into `spec.upgrade.recovery.token` |
| `message` | Progress or failure text |
| `drainPod` | Pod currently drained and not yet deleted |
| `drainReason` | Why the drain gate aborted |

See [Updates](updates.md#when-a-restart-stops-halfway) for recovery actions.

## Events

Useful Warning events include `DrainAborted`, `ScaleDownBlocked`, `FeatureGateDisabled`, and `FailedPreStopHook` on the pod. `SupplyWait` is re-emitted at 1, 2, 5, 10, 20, 30, and 45 minutes, then hourly.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
