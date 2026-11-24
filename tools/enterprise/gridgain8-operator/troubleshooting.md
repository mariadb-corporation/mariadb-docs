---
description: >-
  Failures the operator surfaces in status, events, and logs, and what to
  collect for Enterprise Support.
---

# Troubleshooting

This operator is available only with MariaDB Enterprise Platform Ultimate. Report problems through MariaDB Enterprise Support (`support@mariadb.com`). Attach the objects listed at the end of this page.

## Cluster Never Becomes Ready

```sh
kubectl get gridgaincluster
kubectl describe gridgaincluster gridgaincluster
kubectl get events --field-selector involvedObject.name=gridgaincluster
kubectl logs -n gridgain-k8s-operator-system deploy/gridgain-k8s-operator-controller-manager
```

| Symptom | Likely cause |
| ------- | ------------ |
| Image pull errors | Missing `imagePullSecrets` or global pull secret for `docker.mariadb.com`. |
| `PHASE` `Pending` with one replica | Set `spec.upgrade.allowSingleReplicaRoll: true`. |
| Webhook timeouts on apply | Controller not Ready, or single-namespace mode (webhook is off; OpenAPI/CEL only). |
| `FeatureGateDisabled` | Spec fills an Alpha field while the matching `--feature-gates` value is false. |
| License events | Secret missing, wrong key, or invalid XML. See [License](license.md). |
| `ForeignObjectNameTaken` | A Service, ConfigMap, or Secret name the operator needs already exists and is not owned. |

## Drain and Scale-Down

| `drainReason` | What to do |
| ------------- | ---------- |
| `UniqueDataHeld` | Add a replica or move unique partitions. The operator will not force. |
| `SupplyTimeout` | Raise `spec.drain.supplyWaitTimeoutSeconds`, or inspect why supply never finishes. |
| `Unauthorized` | Fix the server-user Secret, then acknowledge `spec.upgrade.recovery`. |
| `UnsupportedImage` | Use GridGain 8.9.37 or newer. |
| `RESTUnreachable` | Check NetworkPolicy, the pod, and port `8080`. |

See [Drain and Graceful Shutdown](drain.md) and [Status and Events](status.md).

## Configuration Walk Stuck (`upgrade.phase=Failed`)

Do not delete the stuck pod to "unstick" it. Copy `status.upgrade.recoveryToken` into `spec.upgrade.recovery`. See [Updates](updates.md#when-a-restart-stops-halfway).

## GridGain Version Change

Changing `spec.image` while pods are still running is not a supported version upgrade. GridGain will not join a node on a different server build. Scale `replicas` to `0`, wait until the pods are gone, then set the new image. See [Updates](updates.md#change-the-gridgain-server-version).

Admission does not reject an image change on a running cluster with two or more replicas. That starts a one-node-at-a-time restart (the configuration path). Do not use it to change GridGain version.

Admission does reject:

* A pod-template change (including `spec.image`) in the **same** patch that scales a running cluster to `0`. Scale first, wait, then change the image.
* A template change when `spec.replicas` is `1`, unless `spec.upgrade.allowSingleReplicaRoll` is `true`.

## OpenShift Permission Errors

Set `spec.podSecurityContext` without `runAsUser` or `fsGroup` so `restricted-v2` assigns IDs from the namespace range. Apply `gridgaincluster-openshift.yaml` from the [examples catalog](examples-catalog.md). See [Helm](installation/helm.md#openshift). The operator default UID `1000` / `fsGroup` `2000` fails `restricted-v2`.

## PreStop

`FailedPreStopHook` on the pod is a signal. Termination still proceeds.

| Exit | Meaning |
| ---- | ------- |
| 0 | Shutdown gate passed |
| 2 | Passcode rejected |
| 3 | Drain REST not implemented by the image |
| 4 | Localhost REST did not answer |
| 5 | Gate still closed when the supply budget ran out (`kubectl delete pod`, eviction, or grace period too small) |

## What to Attach to a Ticket

* `kubectl get gridgaincluster gridgaincluster -o yaml`
* `kubectl describe gridgaincluster gridgaincluster`
* Operator logs from the controller Deployment
* `kubectl get pods,svc,events -o wide` in the cluster namespace
* Operator and GridGain image tags **and digests**
* Kubernetes or OpenShift version (`oc get clusterversion` on OpenShift)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
