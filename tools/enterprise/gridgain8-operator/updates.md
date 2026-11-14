---
description: >-
  Upgrade the operator with Helm, change GridGain version by scaling to zero,
  and apply configuration changes one node at a time.
---

# Updates

Two upgrades are separate. One replaces the operator. The other changes a running GridGain cluster. Upgrade the operator first when a release includes both.

Changing the GridGain **server version** while pods are running is not supported. The new node would join nodes still on the old build, and GridGain refuses that. Scale to zero first.

Admission does **not** reject changing `spec.image` while `replicas` is 2 or more. That still starts a one-node-at-a-time restart and produces a mixed-version cluster. Do not use it for a version change. Admission **does** reject a template change (including `spec.image`) in the same patch that scales a running cluster to `0`.

Configuration changes restart one node at a time.

## Upgrade the Operator

Use the same Helm release names and namespace as the original install.

```sh
helm repo update
helm upgrade gridgain8-operator-crds gridgain8-operator/gridgain8-operator-crds --version <new-version>
helm upgrade gridgain8-operator gridgain8-operator/gridgain8-operator \
  -n gridgain-k8s-operator-system \
  --reuse-values \
  --version <new-version>
```

Upgrade the CRD chart first. If the release notes say the CRDs are unchanged, you can skip that chart.

Wait until the controller is Ready:

```sh
kubectl -n gridgain-k8s-operator-system rollout status \
  deploy/gridgain-k8s-operator-controller-manager
```

GridGain pods stay in place when the new operator renders the same pod template. Check one cluster:

```sh
kubectl get gridgaincluster gridgaincluster -o jsonpath=\
'phase={.status.phase} upgrade={.status.upgrade.phase} api={.apiVersion}{"\n"}'
```

Expect `phase=Ready`, `upgrade=Complete`, and `api=gridgain.gridgain.com/v1`. Pod UIDs and restart counts stay the same.

A release that changes the pod template is a maintenance window: every cluster then takes the one-node-at-a-time restart described under [Change Configuration](#change-configuration). A cluster with one replica stays `Pending` until you set `spec.upgrade.allowSingleReplicaRoll: true`.

## Change the GridGain Server Version

In-memory data is discarded. Take any copy you need before the first step. The operator does not back up the cluster.

1. Set `spec.replicas` to `0` and wait until the pods are gone. Do not change the image in that update. Admission rejects a template change that also scales a running cluster to 0.

```sh
kubectl patch gridgaincluster gridgaincluster --type=merge \
  -p '{"spec":{"replicas":0}}'
kubectl get pods -l app.kubernetes.io/instance=gridgaincluster
```

2. After the pod list is empty, set the new image and the replica count you want in one update. The StatefulSet creates every pod on the new image, ordinal 0 then 1 then 2. There is no mixed-version rolling restart.

```sh
kubectl patch gridgaincluster gridgaincluster --type=merge -p '{
  "spec": {
    "replicas": 3,
    "image": {"repository": "gridgain/ultimate", "tag": "8.9.38"}
  }
}'
```

Changing the image while `replicas` stays `0` is allowed. A later scale-up starts on that image.

Setting the replica count back to `1` still needs `spec.upgrade.allowSingleReplicaRoll: true` unless it is already set. Scaling back to 2 or more does not.

3. Wait until the cluster is `Ready` and the new pods report the new build:

```sh
kubectl get gridgaincluster gridgaincluster -o jsonpath='{.status.phase}{"\n"}'
kubectl exec gridgaincluster-0 -c gridgaindb -- \
  curl -sS 'http://127.0.0.1:8080/ignite?cmd=version'
```

## Change Configuration

With `spec.upgrade.enabled` at its default (`true`), a change to mounted configuration restarts the StatefulSet from the highest pod number down to 0. One node is down at a time. The next node waits until the current one is Ready.

Caches declared in `spec.caches` are `PARTITIONED` with `backups=0`. A restart drops entries whose only copy was on the restarted node.

After `status.upgrade.phase` returns to `Complete`, read back a known key.

## When a Restart Stops Halfway

`status.upgrade.phase` of `Failed` means the one-node-at-a-time restart is stuck. The node that did not become Ready stays the one being updated. Pods that have not moved are still serving. A missing image tag produces this state. It is not a version upgrade.

The operator does not continue and does not roll back by itself.

1. Read the status:

```sh
kubectl get gridgaincluster gridgaincluster -o jsonpath=\
'phase={.status.upgrade.phase} stuck={.status.upgrade.stuckOrdinal} token={.status.upgrade.recoveryToken} message={.status.upgrade.message}{"\n"}'
```

2. Leave the pods in place. Deleting one does not clear `Failed`.
3. Write `spec.upgrade.recovery` with that token and one action:
   * `retry` deletes the stuck pod once and gives it one more readiness window.
   * `retryUntilReady` keeps deleting it on a backoff until it is Ready or you stop.
   * `rollback` restores the previous pod template, including the configuration that template mounts.

```sh
kubectl patch gridgaincluster gridgaincluster --type=merge -p '{
  "spec": {
    "upgrade": {
      "recovery": {"action": "rollback", "token": "TOKEN"}
    }
  }
}'
```

4. `rollback` does not change `spec`. The phase becomes `RolledBack` while the spec still describes the failed target. Set the spec back to the restored image and configuration, or to a new target.

The token belongs to this failure. Copy it again after each `Failed`.

## Not Reversible

* Entries lost from a `backups=0` cache during a restart.
* In-memory data discarded by scaling to 0.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
