---
description: >-
  Configure persistent storage, storage classes, existing PVCs, additional
  volumes, volume permissions, and storage profiles for GridGain 9 clusters on
  Kubernetes.
---

# Persistence and Storage

{% hint style="warning" %}
Kubernetes operator is an experimental feature. The configuration may change in a subsequent release.
{% endhint %}

GridGain 9 stores data on disk when using its native persistent storage engine. The operator manages PersistentVolumeClaims through the StatefulSet it creates, ensuring each pod gets a dedicated volume that survives pod restarts and rescheduling.

## Managing Persistence

Cluster persistence is enabled by default, with 8 Gi allocated. To explicitly disable persistence, set `persistence.enabled` to `false`:

```yaml
spec:
  persistence:
    enabled: false
```

Without persistence, pods use ephemeral storage. All data is lost when a pod is deleted or rescheduled.

## Storage Class and Size

Specify a storage class and volume size to control the type and capacity of the underlying storage:

```yaml
spec:
  persistence:
    enabled: true
    size: 100Gi
    storageClassName: fast-ssd
```

When `storageClassName` is omitted, Kubernetes uses the cluster's default storage class. The `size` field accepts any valid Kubernetes quantity (for example, `20Gi`, `100Gi`, `1Ti`).

## Using an Existing PVC

If you have a PersistentVolumeClaim that was provisioned outside of the operator — for example, pre-provisioned by an administrator or restored from a snapshot — reference it with `existingClaim`:

```yaml
spec:
  persistence:
    enabled: true
    existingClaim: my-existing-pvc
```

When an existing claim is specified, the operator does not create a new PVC. The claim must exist in the same namespace as the `GridGain9Cluster` resource.

## Additional Volumes

Beyond the main persistence volume, you can request additional persistent volumes for specific purposes. Common examples are separating cluster Raft logs (stored in `/raft`) or application logs (stored in `/logs`) from the primary data directory. Define them under `persistence.additionalVolumes` as a map of named volume specifications:

```yaml
spec:
  persistence:
    enabled: true
    size: 100Gi
    additionalVolumes:
      raft:
        enabled: true
        mountPath: /raft
        size: 50Gi
        storageClassName: standard-rwo
      logs:
        enabled: true
        mountPath: /logs
        size: 20Gi
        storageClassName: standard-rwo
```

Each entry in the map accepts `enabled`, `mountPath`, `size`, `storageClassName`, and `accessModes` fields. Disabled entries are ignored.

## Volume Permissions

Some storage providers create volumes owned by root, which prevents the GridGain process from writing to them when it runs as a non-root user. The operator can run an init container to fix ownership before the main container starts:

```yaml
spec:
  persistence:
    enabled: true
    size: 50Gi
    volumePermissions:
      enabled: true
```

When `volumePermissions` is specified, the `enabled` field defaults to `true`. You can also override the init container image and resource allocation:

```yaml
spec:
  persistence:
    volumePermissions:
      enabled: true
      image:
        registry: docker.io
        repository: bitnami/bitnami-shell
        tag: latest
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
```

## Storage Profile

The `storage.profile.memoryPercentage` field controls what fraction of the container's memory limit is allocated to the GridGain storage engine's off-heap memory region. The default is 60:

```yaml
spec:
  storage:
    profile:
      memoryPercentage: 60
```

The valid range is 1 to 100. Lower values leave more memory for the JVM heap and other processes in the container; higher values dedicate more memory to caching data pages. For development workloads with limited resources, reducing this to 40 can help avoid out-of-memory conditions. For large datasets, increasing it to 70 or above keeps more data in memory.
