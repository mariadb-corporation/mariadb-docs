---
description: >-
  Deploy a first GridGainCluster after installing the operator, including
  license, apply, and checks that confirm the cluster is Ready.
---

# Quickstart

This page deploys one GridGain 8 node after the operator is installed.

## Prerequisites

* The operator is installed and Ready. See [Helm](installation/helm.md).
* A GridGain license file.
* GridGain 8 **8.9.37** or newer. This example uses `8.9.38`.

## Create the License Secret

```sh
kubectl create secret generic gridgaincluster-license \
  --from-file=gridgain-license.xml=/path/to/your/gridgain-license.xml
```

The operator does not ship a license.

## Apply a Cluster

```yaml
apiVersion: gridgain.gridgain.com/v1
kind: GridGainCluster
metadata:
  name: gridgaincluster
spec:
  replicas: 1
  upgrade:
    allowSingleReplicaRoll: true
  image:
    repository: gridgain/ultimate
    tag: "8.9.38"
    pullPolicy: IfNotPresent
  resources:
    requests:
      cpu: "500m"
      memory: "1Gi"
    limits:
      cpu: "500m"
      memory: "1Gi"
  license:
    mountPath: /opt/gridgain/license
    fromSecret:
      name: gridgaincluster-license
    secretKey: gridgain-license.xml
  terminationGracePeriodSeconds: 90
```

```sh
kubectl apply -f gridgaincluster.yaml
```

The same manifest is `gridgaincluster.yaml` in the [examples catalog](examples-catalog.md). On OpenShift, apply `gridgaincluster-openshift.yaml` from that catalog instead. See [Helm](installation/helm.md#openshift).

## Verify

The cluster is working when all of these succeed:

```sh
kubectl get gridgaincluster gridgaincluster
```

Expect `PHASE` `Ready` and `READY` `1`.

```sh
kubectl get pods -l app.kubernetes.io/instance=gridgaincluster
```

Expect the pod `Running` and `Ready`.

```sh
kubectl get gridgaincluster gridgaincluster -o jsonpath='{.status.phase} {.status.upgrade.phase} {.apiVersion}{"\n"}'
```

Expect `Ready Complete gridgain.gridgain.com/v1`.

```sh
kubectl exec gridgaincluster-0 -c gridgaindb -- \
  curl -sS 'http://127.0.0.1:8080/ignite?cmd=version'
```

Expect a JSON body with a GridGain 8 version, not a connection error.

If `PHASE` stays `Pending` or `Failed`, see [Troubleshooting](troubleshooting.md).

## Next Steps

* [Configuration](configuration.md)
* [Examples Catalog](examples-catalog.md)
* [API Reference](api-reference.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
