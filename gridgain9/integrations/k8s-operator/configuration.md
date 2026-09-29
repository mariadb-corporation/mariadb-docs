---
description: >-
  Configure cluster-level and node-level settings, environment variables, JVM
  tuning, resources, and high availability for GridGain 9 clusters managed by
  the Kubernetes Operator.
---

# Cluster and Node Configuration

{% hint style="warning" %}
Kubernetes operator is an experimental feature. The configuration may change in a subsequent release.
{% endhint %}

The `GridGain9Cluster` resource exposes two separate configuration layers: cluster-level and node-level configuration. The cluster configuration (`clusterConfig`) supports two sources — inline in the manifest or from a Kubernetes Secret. The node configuration (`gridgainConfig`) supports two sources — inline in the manifest or from a ConfigMap.

## Cluster Configuration (clusterConfig)

The `clusterConfig` field holds settings that apply to the cluster as a whole. The content is a JSON document that the operator mounts into pods at `/etc/gridgain9db/cluster.conf` by default. You can override this path with `clusterConfig.mountPath`. For a full list of available cluster configuration parameters, see [Cluster Configuration Parameters](../../reference/configuration/cluster-configuration-parameters.md).

To provide the configuration inline:

```yaml
spec:
  clusterConfig:
    content: |
      {
        "security": {
          "authentication": {
            "enabled": true,
            "providers": [
              {
                "name": "basic",
                "type": "basic",
                "users": [
                  {"username": "admin", "password": "changeme", "roles": ["system"]}
                ]
              }
            ]
          }
        }
      }
```

Alternatively, reference an existing Secret:

```yaml
spec:
  clusterConfig:
    secretName: my-cluster-config
    secretKey: cluster.json
```

When using inline `content`, the operator creates a Secret from it automatically. The CRD also exposes structured `authentication` and `ssl` sub-fields under `clusterConfig` for cases where you want the operator to assemble the configuration rather than writing the JSON yourself. See the [Security](security.md) page for details.

## Node Configuration (gridgainConfig)

The `gridgainConfig` field controls per-node settings. The content uses the HOCON format that GridGain 9 expects for its node configuration files. For a full list of available node configuration parameters, see [Node Configuration Parameters](../../reference/configuration/node-configuration-parameters.md).

To provide the configuration inline:

```yaml
spec:
  gridgainConfig:
    content: |
      ignite {
        clientConnector {
          port=10800
        }
        network {
          nodeFinder {
            netClusterNodes=[
              "my-cluster-headless:27100"
            ]
            type=STATIC
          }
          port=27100
        }
        rest {
          port=10300
        }
        sql {
          nodeMemoryQuota="60%"
        }
      }
```

To use an existing ConfigMap instead:

```yaml
spec:
  gridgainConfig:
    configMapName: my-gridgain-config
```

The node finder address follows the pattern `<cluster-name>-headless:<network-port>`, where the headless service is created automatically by the operator for the StatefulSet.

## Environment Variables and JVM Tuning

The `extraEnvVars` field accepts a list of Kubernetes `EnvVar` objects that are injected into the GridGain container. The most common use case is passing JVM arguments through the `GRIDGAIN9_EXTRA_JVM_ARGS` variable:

```yaml
spec:
  extraEnvVars:
    - name: GRIDGAIN9_EXTRA_JVM_ARGS
      value: >-
        -Xms8g -Xmx8g
        -XX:+UseG1GC
        -XX:MaxGCPauseMillis=200
        -XX:G1HeapRegionSize=32M
```

You can also set the `GRIDGAIN9_LOG_LEVEL` variable to control logging verbosity:

```yaml
spec:
  extraEnvVars:
    - name: GRIDGAIN9_LOG_LEVEL
      value: DEBUG
```

{% hint style="info" %}
Changes to `extraEnvVars` are treated as configuration changes. If an `upgradeConfig` is defined, modifying environment variables triggers a rolling upgrade of the cluster. The CRD enforces a validation rule that prevents changes to `extraEnvVars` while the cluster is in the `Upgrading` or `RollingBack` phase.
{% endhint %}

## Resource Management

You can define CPU and memory requests and limits for the GridGain container using the standard Kubernetes `resources` field:

```yaml
spec:
  resources:
    requests:
      cpu: 2000m
      memory: 8Gi
    limits:
      cpu: 4000m
      memory: 16Gi
```

## Init Containers and Sidecars

The operator supports adding custom init containers and sidecar containers to every pod in the StatefulSet.

Init containers run before the GridGain container starts. A common use case is fixing volume permissions when the storage provider creates volumes owned by root:

```yaml
spec:
  initContainers:
    - name: volume-permissions
      image: busybox:1.36
      command:
        - sh
        - -c
        - |
          chown -R 1001:1001 /persistence
          chmod -R 755 /persistence
      volumeMounts:
        - name: persistence
          mountPath: /persistence
      securityContext:
        runAsUser: 0
```

Sidecar containers run alongside the GridGain container for the lifetime of the pod. A typical example is a log collector:

```yaml
spec:
  sidecars:
    - name: log-collector
      image: fluent/fluent-bit:2.0
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
```

## Extra Volumes and Volume Mounts

To mount additional volumes into the GridGain container — for example, SSL certificates or custom configuration files — use the `extraVolumes` and `extraVolumeMounts` fields:

```yaml
spec:
  extraVolumes:
    - name: ssl-certs
      secret:
        secretName: gridgain-ssl-certs
  extraVolumeMounts:
    - name: ssl-certs
      mountPath: /opt/gridgain/ssl
      readOnly: true
```

These fields accept standard Kubernetes volume and volume mount definitions. The operator adds them to the StatefulSet pod template alongside the built-in volumes.

## High Availability Recommendations

For production deployments, consider the following configuration to improve availability and resilience.

### Pod Anti-Affinity

Spreading GridGain pods across distinct nodes prevents a single node failure from taking down multiple cluster members. Use `preferredDuringSchedulingIgnoredDuringExecution` for a soft preference that works even when the cluster has fewer Kubernetes nodes than GridGain replicas, or `requiredDuringSchedulingIgnoredDuringExecution` for a hard constraint:

```yaml
spec:
  affinity:
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 100
          podAffinityTerm:
            labelSelector:
              matchLabels:
                app.kubernetes.io/name: gridgain9
                app.kubernetes.io/instance: my-cluster
            topologyKey: kubernetes.io/hostname
```

### Pod Disruption Budget

A PodDisruptionBudget ensures that voluntary disruptions (node drains, rolling updates) do not reduce the cluster below a safe minimum. For a three-node cluster, `minAvailable: 2` is a reasonable choice:

```yaml
spec:
  podDisruptionBudget:
    enabled: true
    minAvailable: 2
```

### Topology Spread

To distribute pods across availability zones in addition to individual nodes, use `topologySpreadConstraints`:

```yaml
spec:
  topologySpreadConstraints:
    - maxSkew: 1
      topologyKey: topology.kubernetes.io/zone
      whenUnsatisfiable: ScheduleAnyway
      labelSelector:
        matchLabels:
          app.kubernetes.io/name: gridgain9
          app.kubernetes.io/instance: my-cluster
```

This tells the scheduler to balance pods as evenly as possible across zones while still allowing scheduling when perfect balance is not achievable.
