---
description: >-
  Complete field reference for the GridGain9Cluster custom resource definition,
  covering all spec and status fields organized by functional area.
---

# CRD Reference

{% hint style="warning" %}
Kubernetes operator is an experimental feature. The configuration may change in a subsequent release.
{% endhint %}

This page provides a complete reference of all fields in the `GridGain9Cluster` custom resource definition, organized by functional area.

## Spec Fields

The `spec` field defines the desired state of the cluster. The only required field is `replicas`.

### Core

```yaml
spec:
  replicas: 3
  gridgainWorkDir: /persistence
  terminationGracePeriodSeconds: 600
  revisionHistoryLimit: 10
  podManagementPolicy: Parallel
  serviceAccountName: gridgain-sa
  rollback: false
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| replicas | int32 | 3 | Number of GridGain cluster nodes. Minimum value is 1. |
| gridgainWorkDir | string | /persistence | Working directory for the GridGain process inside the container. |
| terminationGracePeriodSeconds | int64 | 600 | Seconds to wait for graceful pod shutdown before forcibly killing the process. |
| revisionHistoryLimit | int32 | 10 | Number of old StatefulSet revisions to retain for rollback. |
| podManagementPolicy | string | Parallel | Controls how pods are created during initial scale up. Accepts `Parallel` or `OrderedReady`. |
| serviceAccountName | string |  | Name of an existing ServiceAccount to use for the pods. |
| rollback | boolean |  | Set to `true` to trigger a manual rollback to the last stable configuration. |

### Image

```yaml
spec:
  image:
    registry: docker.io
    repository: gridgain/gridgain9
    tag: "9.1.20"
    pullPolicy: IfNotPresent
  imagePullSecrets:
    - name: my-registry-secret
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| image.registry | string | docker.io | Docker registry. |
| image.repository | string | gridgain/gridgain9 | Image repository. |
| image.tag | string |  | Image tag. When omitted, the operator uses its built-in default. |
| image.pullPolicy | string | IfNotPresent | Image pull policy. Accepts `Always`, `Never`, or `IfNotPresent`. |
| imagePullSecrets | []LocalObjectReference |  | List of Secrets for authenticating with private registries. |

### Resources

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

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| resources.requests.cpu | Quantity |  | Minimum CPU allocation for the GridGain container. |
| resources.requests.memory | Quantity |  | Minimum memory allocation for the GridGain container. |
| resources.limits.cpu | Quantity |  | Maximum CPU allocation for the GridGain container. |
| resources.limits.memory | Quantity |  | Maximum memory allocation for the GridGain container. |

### Persistence

```yaml
spec:
  persistence:
    enabled: true
    size: 100Gi
    storageClassName: fast-ssd
    # existingClaim: my-existing-pvc
    accessModes:
      - ReadWriteOnce
    volumePermissions:
      enabled: true
    additionalVolumes:
      raft:
        enabled: true
        mountPath: /raft
        size: 50Gi
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| persistence.enabled | boolean | true | Enables persistent storage via PersistentVolumeClaims. |
| persistence.size | Quantity | 8Gi | Size of the PVC. |
| persistence.storageClassName | string |  | Storage class name. Uses the cluster default when omitted. |
| persistence.existingClaim | string |  | Name of an existing PVC to use instead of creating a new one. |
| persistence.accessModes | []string |  | PVC access modes (e.g. `ReadWriteOnce`). |
| persistence.volumePermissions.enabled | boolean | true | Runs an init container to fix volume ownership. |
| persistence.volumePermissions.image | object |  | Image for the volume permissions init container. Supports `registry`, `repository`, `tag`, and `pullPolicy`. |
| persistence.volumePermissions.resources | ResourceRequirements |  | Resource requests and limits for the volume permissions init container. |
| persistence.additionalVolumes.\<name>.enabled | boolean |  | Enables the named additional volume. |
| persistence.additionalVolumes.\<name>.mountPath | string |  | Mount path for the additional volume. |
| persistence.additionalVolumes.\<name>.size | Quantity |  | Size of the additional volume PVC. |
| persistence.additionalVolumes.\<name>.storageClassName | string |  | Storage class for the additional volume. |
| persistence.additionalVolumes.\<name>.accessModes | []string |  | Access modes for the additional volume. |

### Storage Profile

```yaml
spec:
  storage:
    profile:
      memoryPercentage: 60
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| storage.profile.memoryPercentage | int32 | 60 | Percentage of the container memory limit allocated to the storage engine. Valid range is 1 to 100. |

### License

```yaml
spec:
  license:
    # Option 1: From a Secret
    secretName: gridgain-license
    secretKey: license.conf
    # Option 2: Inline content
    # content: |
    #   {"edition":"ULTIMATE",...}
    mountPath: /opt/gridgain/etc/license.conf
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| license.content | string |  | Inline license content. The operator creates a Secret from this value. |
| license.secretName | string |  | Name of an existing Secret containing the license. |
| license.secretKey | string |  | Key within the Secret that holds the license data. |
| license.mountPath | string | /opt/gridgain/etc/license.conf | Path where the license file is mounted in the container. |

### Cluster Configuration

```yaml
spec:
  clusterConfig:
    # Option 1: Inline content
    content: |
      {"security":{"authentication":{"enabled":true}}}
    # Option 2: From a Secret
    # secretName: my-cluster-config
    # secretKey: cluster.json
    mountPath: /etc/gridgain9db/cluster.conf
    authentication:
      enabled: true
      type: basic
      users:
        - username: admin
          password: changeme
    ssl:
      enabled: true
      clientAuth: require
      keyStore:
        secretName: ssl-certs
        secretKey: keystore.p12
        password: keystorepass
        type: PKCS12
      trustStore:
        secretName: ssl-certs
        secretKey: truststore.p12
        password: truststorepass
        type: PKCS12
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| clusterConfig.content | string |  | Inline cluster configuration as a JSON document. |
| clusterConfig.secretName | string |  | Name of an existing Secret containing the cluster configuration. |
| clusterConfig.secretKey | string |  | Key within the Secret. |
| clusterConfig.mountPath | string | /etc/gridgain9db/cluster.conf | Path where the cluster configuration file is mounted. |
| clusterConfig.authentication.enabled | boolean |  | Enables authentication. |
| clusterConfig.authentication.type | string | basic | Authentication type. Accepts `basic` or `ldap`. |
| clusterConfig.authentication.users | []UserSpec |  | List of users for basic authentication. Each user requires `username` and `password`. Optional fields: `displayName` (display name) and `roles` (list of role strings). |
| clusterConfig.ssl.enabled | boolean |  | Enables SSL/TLS. |
| clusterConfig.ssl.clientAuth | string | none | Client authentication mode. Accepts `none`, `require`, or `optional`. |
| clusterConfig.ssl.ciphers | string |  | Comma-separated list of allowed SSL ciphers. |
| clusterConfig.ssl.keyStore.secretName | string |  | Secret containing the keystore file. |
| clusterConfig.ssl.keyStore.secretKey | string |  | Key within the Secret for the keystore file. |
| clusterConfig.ssl.keyStore.password | string |  | Keystore password. |
| clusterConfig.ssl.keyStore.type | string | PKCS12 | Keystore type. Accepts `PKCS12` or `JKS`. |
| clusterConfig.ssl.trustStore.secretName | string |  | Secret containing the truststore file. |
| clusterConfig.ssl.trustStore.secretKey | string |  | Key within the Secret for the truststore file. |
| clusterConfig.ssl.trustStore.password | string |  | Truststore password. |
| clusterConfig.ssl.trustStore.type | string | PKCS12 | Truststore type. Accepts `PKCS12` or `JKS`. |

### Node Configuration

```yaml
spec:
  gridgainConfig:
    # Option 1: Inline content
    content: |
      ignite {
        network {
          port=27100
        }
        rest {
          port=10300
        }
        clientConnector {
          port=10800
        }
      }
    # Option 2: From a ConfigMap
    # configMapName: my-gridgain-config
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| gridgainConfig.content | string |  | Inline GridGain node configuration in HOCON format. |
| gridgainConfig.configMapName | string |  | Name of an existing ConfigMap containing the node configuration. |

### JMX

```yaml
spec:
  jmx:
    enabled: true
    port: 9404
    config: |
      lowercaseOutputName: true
      rules:
        - pattern: '^java.lang<type=Memory><HeapMemoryUsage>used'
          name: jvm_memory_heap_used
          type: GAUGE
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| jmx.enabled | boolean |  | Enables JMX metrics exporter. |
| jmx.port | int32 | 9404 | Port for the JMX exporter. Valid range is 1 to 65535. |
| jmx.config | string |  | JMX exporter configuration in YAML format. |

### Services

```yaml
spec:
  services:
    - name: rest-external
      type: LoadBalancer
      externalTrafficPolicy: Local
      sessionAffinity: None
      ports:
        - name: rest
          port: 10300
          targetPort: 10300
      annotations:
        service.beta.kubernetes.io/aws-load-balancer-type: nlb
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| services[].name | string |  | Required. Service name suffix. The full service name is `<cluster-name>-<name>`. |
| services[].type | string | ClusterIP | Service type. Accepts `ClusterIP`, `NodePort`, `LoadBalancer`, or `Headless`. |
| services[].ports[].name | string |  | Required. Port name. |
| services[].ports[].port | int32 |  | Required. Service port. Valid range is 1 to 65535. |
| services[].ports[].targetPort | int32 |  | Target port on the pod. Defaults to the same value as `port`. |
| services[].ports[].nodePort | int32 |  | Node port for NodePort services. Valid range is 30000 to 32767. |
| services[].ports[].protocol | string | TCP | Port protocol. Accepts `TCP`, `UDP`, or `SCTP`. |
| services[].externalTrafficPolicy | string |  | External traffic policy. Accepts `Cluster` or `Local`. |
| services[].sessionAffinity | string | None | Session affinity. Accepts `None` or `ClientIP`. |
| services[].loadBalancerIP | string |  | Static IP for LoadBalancer services. |
| services[].loadBalancerSourceRanges | []string |  | CIDR ranges allowed to access LoadBalancer services. |
| services[].publishNotReadyAddresses | boolean |  | Publishes addresses of pods that are not yet ready. |
| services[].annotations | map[string]string |  | Additional annotations for the service (e.g. cloud provider configuration). |

### Health Probes

The `probes` field supports `liveness`, `readiness`, and `startup` probes. Each probe accepts the standard Kubernetes probe fields. GridGain exposes liveness and readiness endpoints on port 10300 at `/health/liveness` and `/health/readiness` respectively.

```yaml
spec:
  probes:
    liveness:
      httpGet:
        path: /health/liveness
        port: 10300
      initialDelaySeconds: 30
      periodSeconds: 30
      timeoutSeconds: 10
      failureThreshold: 3
    readiness:
      httpGet:
        path: /health/readiness
        port: 10300
      initialDelaySeconds: 30
      periodSeconds: 10
    startup:
      httpGet:
        path: /health/readiness
        port: 10300
      initialDelaySeconds: 0
      periodSeconds: 10
      failureThreshold: 30
```

| Field | Type | Description |
| --- | --- | --- |
| probes.\<type>.httpGet.path | string | HTTP path to probe. |
| probes.\<type>.httpGet.port | int/string | Port to probe. |
| probes.\<type>.initialDelaySeconds | int32 | Seconds before the first probe after container start. |
| probes.\<type>.periodSeconds | int32 | Interval between probes. |
| probes.\<type>.timeoutSeconds | int32 | Seconds before the probe times out. |
| probes.\<type>.failureThreshold | int32 | Consecutive failures before the probe is considered failed. |
| probes.\<type>.successThreshold | int32 | Consecutive successes before the probe is considered successful. |

### Pod Disruption Budget

```yaml
spec:
  podDisruptionBudget:
    enabled: true
    minAvailable: 2
    # maxUnavailable: 1
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| podDisruptionBudget.enabled | boolean |  | Enables the PodDisruptionBudget. |
| podDisruptionBudget.minAvailable | int32 |  | Minimum number of pods that must remain available during voluntary disruptions. |
| podDisruptionBudget.maxUnavailable | int32 |  | Maximum number of pods that can be unavailable during voluntary disruptions. |

### Upgrade Configuration

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

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| upgradeConfig.nodeTimeoutSeconds | int32 | 600 | Timeout for a single node upgrade. Minimum 60. |
| upgradeConfig.clusterTimeoutSeconds | int32 | 1800 | Timeout for the entire cluster upgrade. Minimum 300. |
| upgradeConfig.failureThresholdPercent | int32 | 20 | Percentage of failed pods that triggers automatic rollback. Range 1-100. |
| upgradeConfig.rollbackTimeoutSeconds | int32 | 1800 | Timeout for a rollback operation. Minimum 300. |
| upgradeConfig.maxUnavailable | int32 | 1 | Maximum pods unavailable during upgrade. |
| upgradeConfig.maxSurge | int32 | 0 | Maximum extra pods during upgrade. Range 0-1. |

### Scheduling

```yaml
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchLabels:
              app.kubernetes.io/name: gridgain9
          topologyKey: kubernetes.io/hostname
  tolerations:
    - key: workload
      operator: Equal
      value: database
      effect: NoSchedule
  nodeSelector:
    node-type: database
  topologySpreadConstraints:
    - maxSkew: 1
      topologyKey: topology.kubernetes.io/zone
      whenUnsatisfiable: ScheduleAnyway
      labelSelector:
        matchLabels:
          app.kubernetes.io/name: gridgain9
  priorityClassName: high-priority
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| affinity | Affinity |  | Pod affinity and anti-affinity rules. Accepts the standard Kubernetes `Affinity` object. |
| tolerations | []Toleration |  | Pod tolerations for node taints. |
| nodeSelector | map[string]string |  | Node label selector for pod scheduling. |
| topologySpreadConstraints | []TopologySpreadConstraint |  | Constraints for spreading pods across topology domains. |
| priorityClassName | string |  | Priority class for the pods. |

### StatefulSet

```yaml
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 0
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| updateStrategy.type | string | RollingUpdate | StatefulSet update strategy. Accepts `RollingUpdate` or `OnDelete`. |
| updateStrategy.rollingUpdate.partition | int32 | 0 | Ordinal at which to partition the update. Pods with an ordinal greater than or equal to the partition are updated. |

### Security Contexts

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1001
    fsGroup: 1001
    seccompProfile:
      type: RuntimeDefault
  containerSecurityContext:
    allowPrivilegeEscalation: false
    readOnlyRootFilesystem: false
    runAsNonRoot: true
    runAsUser: 1001
    capabilities:
      drop:
        - ALL
```

| Field | Type | Description |
| --- | --- | --- |
| securityContext | PodSecurityContext | Pod-level security context. Supports `runAsNonRoot`, `runAsUser`, `fsGroup`, `seccompProfile`, and all standard fields. |
| containerSecurityContext | SecurityContext | Container-level security context. Supports `allowPrivilegeEscalation`, `readOnlyRootFilesystem`, `runAsUser`, `capabilities`, and all standard fields. |

### Metadata

```yaml
spec:
  podLabels:
    app-component: database
    monitoring: enabled
  podAnnotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "10300"
```

| Field | Type | Description |
| --- | --- | --- |
| podLabels | map[string]string | Custom labels added to every pod in the StatefulSet. |
| podAnnotations | map[string]string | Custom annotations added to every pod in the StatefulSet. |

### Containers and Volumes

```yaml
spec:
  initContainers:
    - name: init-permissions
      image: busybox:1.36
      command: ["sh", "-c", "chown -R 1001:1001 /persistence"]
      volumeMounts:
        - name: persistence
          mountPath: /persistence
      securityContext:
        runAsUser: 0
  sidecars:
    - name: log-exporter
      image: fluent/fluent-bit:2.0
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
  extraVolumes:
    - name: custom-config
      configMap:
        name: my-custom-config
  extraVolumeMounts:
    - name: custom-config
      mountPath: /etc/custom
  extraEnvVars:
    - name: GRIDGAIN9_EXTRA_JVM_ARGS
      value: "-Xms8g -Xmx8g -XX:+UseG1GC"
```

| Field | Type | Description |
| --- | --- | --- |
| initContainers | []Container | Additional init containers added to the pod template. Accepts standard Kubernetes container definitions. |
| sidecars | []Container | Sidecar containers that run alongside the GridGain container. Accepts standard Kubernetes container definitions. |
| extraVolumes | []Volume | Additional volumes added to the pod template. |
| extraVolumeMounts | []VolumeMount | Additional volume mounts added to the GridGain container. |
| extraEnvVars | []EnvVar | Environment variables injected into the GridGain container. |

## Status Fields

The `status` sub-resource reflects the observed state of the cluster. These fields are read-only and managed by the operator. To inspect the full status of a cluster:

```bash
kubectl get gg9 my-cluster -o jsonpath='{.status}' | jq .
```

To check individual fields:

```bash
kubectl get gg9 my-cluster -o jsonpath='{.status.phase}'
kubectl get gg9 my-cluster -o jsonpath='{.status.readyReplicas}'
kubectl get gg9 my-cluster -o jsonpath='{.status.lastStableImage}'
```

| Field | Type | Description |
| --- | --- | --- |
| phase | string | Current cluster phase: `Running`, `Upgrading`, `RollingBack`, `Failed`, or other transient states. |
| replicas | int32 | Total number of pods created by the StatefulSet. |
| readyReplicas | int32 | Number of pods in the Ready state. |
| currentReplicas | int32 | Number of pods created for the current generation. |
| updatedReplicas | int32 | Number of pods at the current version. |
| initialized | boolean | Whether the cluster has been initialized with a license. |
| clusterState | string | The GridGain cluster state as reported by the cluster itself. |
| observedGeneration | int64 | The `metadata.generation` most recently observed by the controller. |
| conditions | []Condition | Standard Kubernetes conditions with `type`, `status`, `reason`, `message`, `lastTransitionTime`, and `observedGeneration`. |
| upgradeLocked | boolean | `true` while an upgrade or rollback is in progress. |
| upgradeStartTime | date-time | Timestamp when the current upgrade started. |
| upgradeStepStartTime | date-time | Timestamp when the current upgrade or rollback step started. |
| upgradeTargetImage | string | Image locked in for the current upgrade. |
| upgradeTargetConfigHash | string | Configuration hash locked in for the current upgrade. |
| lastStableImage | string | Image of the last successful deployment, used as the rollback target. |
| lastStableConfigHash | string | Configuration hash of the last successful deployment. |
| lastFailedImage | string | Image that caused the most recent rollback. |
| lastUpgradeSuccessful | boolean | Whether the most recent upgrade completed successfully. |
| rollbackCount | int32 | Number of consecutive rollback attempts for the current target. |
