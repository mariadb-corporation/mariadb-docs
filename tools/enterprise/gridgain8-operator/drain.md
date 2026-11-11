---
description: >-
  How the operator drains a GridGain 8 node before deletion, drain abort
  reasons, and preStop behavior.
---

# Drain and Graceful Shutdown

Requires GridGain **8.9.37** or newer. Operator-generated `default-config.xml` sets `ShutdownPolicy.GRACEFUL`.

A pod restart discards that node's in-memory data. The operator waits for the node to finish supplying partitions **before** Kubernetes sets `DeletionTimestamp`, so `terminationGracePeriodSeconds` only covers the short tail (readiness, settle window, WAL flush).

Default `spec.terminationGracePeriodSeconds` when unset is `600`.

## Sequence

For a voluntary death of ordinal *k* (configuration restart, retry delete, or replica decrease):

1. `POST /ignite?cmd=drain&action=start` on the pod REST port `8080`. Readiness becomes 503; kubelet drops the pod from Service endpoints. Cluster protocol continues.
2. Poll `GET /ignite?cmd=supply-status` until `supplying=false`, bounded by `spec.drain.supplyWaitTimeoutSeconds` (default 3600).
3. Delete the pod. Kubelet runs preStop, then SIGTERM.

The operator never sends `shutdown=true` before delete. That would start internal shutdown while the pod is still Running.

There is no opt-out of drain/preStop. `spec.upgrade.enabled: false` only drops the operator supply gate; supply wait then sits in preStop.

## Abort Reasons

| `status.upgrade.drainReason` | Cause |
| --- | --- |
| `UniqueDataHeld` | The node is the only owner of a partition. `force=true` is not sent. |
| `SupplyTimeout` | Still supplying past `supplyWaitTimeoutSeconds`. |
| `Unauthorized` | Passcode rejected, or no server user / Secret to read. |
| `UnsupportedImage` | The image does not implement `cmd=drain` / `cmd=supply-status` (including 8.9.36). |
| `RESTUnreachable` | No HTTP answer from port `8080` within 60s. |

On abort the operator:

1. Sends `POST cmd=drain&action=stop` unless `spec.drain.undrainOnAbort: false`.
2. Records `drainReason`, sets `DrainBlocked=True`, and emits Warning `DrainAborted`.
3. For a configuration walk: phase `Failed` and a recovery token. For scale-down: replica count is held.

`undrainOnAbort: false` parks the node NotReady and freezes the PodDisruptionBudget until you intervene. Default is `true`.

## Scale-Down

Replica decrease is one ordinal at a time: drain, wait for supply, patch `replicas`, wait until that pod has terminated. Scale-down is held while `Failed` or `RolledBack`.

## NetworkPolicy

If you enable `spec.networkPolicy`, allow the operator namespace to reach pod REST port `8080`. A blocked path fails closed with `RESTUnreachable`.

## Auth

When the Auth gate is on and `spec.auth.enabled` is true, drain start/stop and `supply-status?shutdown=true` require the server-user passcode. Missing credentials abort with `Unauthorized`.

## Observability

| Signal | Where |
| ------ | ----- |
| Which pod | `status.upgrade.drainPod` |
| Why it stopped | `status.upgrade.drainReason` and `DrainBlocked` |
| Event trail | `SupplyWait`, `DrainStopped`, `DrainAborted`, `UpgradeNodeDeleted` |

See [Status and Events](status.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
