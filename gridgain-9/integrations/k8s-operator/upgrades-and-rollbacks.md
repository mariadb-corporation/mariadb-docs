---
description: >-
  Perform rolling upgrades and automatic or manual rollbacks of GridGain 9
  clusters with the Kubernetes Operator, and inspect the related status fields.
---

# Upgrades and Rollbacks

{% hint style="warning" %}
Upgrading GridGain through kubernetes operator is an experimental feature.
{% endhint %}

The operator can perform rolling upgrades when the image version or cluster configuration changes. It monitors pod health during the upgrade and can automatically roll back if the failure rate exceeds a configurable threshold.

## Upgrade Configuration

The `upgradeConfig` field controls how the operator executes rolling upgrades:

```yaml
spec:
  upgradeConfig:
    nodeTimeoutSeconds: 600
    clusterTimeoutSeconds: 1800
    failureThresholdPercent: 20
    rollbackTimeoutSeconds: 1800
    maxUnavailable: 1
    maxSurge: 0
```

| Parameter | Default | Description |
| --- | --- | --- |
| nodeTimeoutSeconds | 600 | Maximum time in seconds to wait for a single node to become ready after being restarted. Minimum value is 60. |
| clusterTimeoutSeconds | 1800 | Maximum time in seconds for the entire cluster upgrade to complete. If the upgrade is not finished within this window, the operator triggers a rollback. Minimum value is 300. |
| failureThresholdPercent | 20 | Percentage of pods that can be unhealthy before the operator triggers an automatic rollback. Valid range is 1 to 100. |
| rollbackTimeoutSeconds | 1800 | Maximum time in seconds for a rollback operation to complete. Minimum value is 300. |
| maxUnavailable | 1 | Maximum number of pods that can be unavailable during the upgrade. |
| maxSurge | 0 | Maximum number of extra pods created during the upgrade. For StatefulSets, this is typically 0 or 1. |

## Image Upgrades

{% hint style="warning" %}
Rolling upgrade feature requires an Enterprise or Ultimate license.
{% endhint %}

To upgrade the GridGain version, change the `image.tag` field and apply the updated manifest:

```yaml
spec:
  image:
    tag: "9.1.21"
  upgradeConfig:
    nodeTimeoutSeconds: 600
    clusterTimeoutSeconds: 1800
    failureThresholdPercent: 20
    maxUnavailable: 1
```

The operator detects the image change and begins a rolling update. It restarts pods one at a time (controlled by `maxUnavailable`), waits for each pod to become ready within `nodeTimeoutSeconds`, and verifies overall cluster health before proceeding to the next pod.

Monitor the upgrade progress:

```bash
kubectl get gg9 my-cluster -w
kubectl describe gg9 my-cluster
```

The cluster's `Phase` transitions through `Upgrading` and back to `Running` when the upgrade completes successfully.

## Configuration-Driven Upgrades

Changes to the following fields are treated as configuration changes and trigger a rolling upgrade when `upgradeConfig` is defined:

- `spec.image` — image version changes
- `spec.gridgainConfig` — node configuration changes
- `spec.clusterConfig` — cluster configuration changes
- `spec.license` — license changes
- `spec.extraEnvVars` — environment variable changes, including JVM arguments

The operator computes a hash of the configuration and compares it against the `lastStableConfigHash` stored in the resource status. When the hash changes, the operator adds a config-hash annotation to the pod template, which forces the StatefulSet controller to recreate each pod with the new configuration.

You can change multiple fields at once. All changes are applied in a single rolling upgrade rather than triggering separate upgrades for each field.

## Validation Rules During Upgrades

The CRD includes validation rules that prevent modifications to `image`, `clusterConfig`, `gridgainConfig`, `license`, and `extraEnvVars` while the cluster is in the `Upgrading` or `RollingBack` phase. This prevents conflicting changes from being introduced while an upgrade is in progress. Attempts to modify these fields during an active upgrade will be rejected by the Kubernetes API server.

## Automatic Rollback

The operator automatically rolls back to the last known stable state when any of the following conditions occur:

- The percentage of unhealthy pods exceeds `failureThresholdPercent`.
- The total upgrade time exceeds `clusterTimeoutSeconds`.
- The cluster fails to reach an active state after the upgrade.

During a rollback, the cluster Phase changes to `RollingBack`. The operator reverts to the image and configuration hash stored in `status.lastStableImage` and `status.lastStableConfigHash`.

To prevent infinite rollback loops, the operator limits rollback attempts to a maximum of three, tracked in `status.rollbackCount`. The counter resets when the user changes to a different image than the one that caused the failure (tracked in `status.lastFailedImage`). If all three rollback attempts fail, the cluster enters a `Failed` phase and requires manual intervention.

## Manual Rollback

To manually trigger a rollback at any time, set `spec.rollback` to `true`:

```bash
kubectl patch gg9 my-cluster --type=merge -p '{"spec":{"rollback":true}}'
```

The operator reverts the cluster to the last stable configuration. Once the rollback completes, the operator clears the `rollback` flag automatically.

Monitor the rollback:

```bash
kubectl get gg9 my-cluster -w
kubectl get gg9 my-cluster -o jsonpath='{.status.rollbackCount}'
```

## Upgrade Status Fields

The operator tracks upgrade state in several status fields:

| Field | Description |
| --- | --- |
| phase | Current cluster phase. Values include `Running`, `Upgrading`, `RollingBack`, and `Failed`. |
| upgradeLocked | `true` while an upgrade or rollback is in progress. |
| upgradeStartTime | Timestamp when the current upgrade started. |
| upgradeStepStartTime | Timestamp when the current upgrade or rollback step started, used to enforce delays between topology changes. |
| upgradeTargetImage | The image locked in when the current upgrade started. The operator ignores spec changes to `image` during an active upgrade and uses this value instead. |
| upgradeTargetConfigHash | The configuration hash locked in when the current upgrade started. |
| lastStableImage | The image of the last successful deployment, used as the rollback target. |
| lastStableConfigHash | The configuration hash of the last successful deployment. |
| lastFailedImage | The image that caused the most recent rollback, used to reset the rollback counter when the user switches to a different image. |
| lastUpgradeSuccessful | Whether the most recent upgrade completed successfully. |
| rollbackCount | Number of consecutive rollback attempts for the current target, capped at 3. |
