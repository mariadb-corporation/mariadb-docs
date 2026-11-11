# Storage

This operator gives you flexibility to define the storage that will back the `/var/lib/mysql` data directory mounted by `MariaDB`.

## Configuration

The simplest way to configure storage for your `MariaDB` is:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  storage:
    size: 1Gi
```

This will make use of the default `StorageClass` available in your cluster, but you can also provide a different one:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  storage:
    size: 1Gi
    storageClassName: gp3
```

Under the scenes, the operator is configuring the `StatefulSet`'s `volumeClaimTemplate` property, which you are also able to provide yourself:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  storage:
    size: 1Gi
    storageClassName: gp3
    volumeClaimTemplate:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
      storageClassName: gp3
```

## Volume resize

{% hint style="warning" %}
The `StorageClass` used for volume resizing must define `allowVolumeExpansion = true`.
{% endhint %}

It is possible to resize your storage after having provisioned a `MariaDB`. We need to distinguish between:

* PVCs already in use.
* `StatefulSet` storage size, which will be used when provisioning new replicas.

It is important to note that, for the first case, your `StorageClass` must support volume expansion by declaring the `allowVolumeExpansion = true`. In such case, it will be safe to expand the storage by increasing the `size`. The `resizeInUseVolumes` and `waitForVolumeResize` fields both default to `true`, so you don't need to set them:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  storage:
    size: 2Gi
    resizeInUseVolumes: true # default
    waitForVolumeResize: true # default
```

Depending on your storage provider, this operation might take a while. With `waitForVolumeResize = true` (the default), the operator waits until the PVCs have been resized before the `MariaDB` becomes ready again. While the resize is in progress, the `MariaDB` isn't ready, so operations such as [Galera cluster recovery](./topologies/galera.md#galera-cluster-recovery) and [primary switchover](./topologies/replication.md#primary-switchover) aren't performed, and no [physical backups](./backup-and-restore/physical_backup.md#scheduling) are scheduled. Set `waitForVolumeResize = false` if you don't want to wait for the PVCs.

Set `resizeInUseVolumes = false` to leave the existing PVCs as they are. The new `size` then only applies to the `StatefulSet`, and so to PVCs created for new replicas.

## Storage constraints

The operator's validating webhook enforces these rules:

* The storage `size` can only be increased. A smaller `size` is rejected with `Storage size cannot be decreased`.
* `storageClassName` can't be changed after the `MariaDB` has been created.
* Ephemeral storage only works for standalone `MariaDBs`, without replication or Galera. It can't be combined with `size` or `volumeClaimTemplate`, and it can't be turned on or off after the `MariaDB` has been created.

When the operator is installed in [single namespace](./installation/helm.md#single-namespace) mode, there's no validating webhook, so these rules aren't checked when you apply a change.

## PVC retention policy

By default, the PVCs of a `MariaDB` are kept when the `MariaDB` is deleted or scaled down, and you have to delete them yourself. Use `pvcRetentionPolicy` to change that, for example to delete the PVCs together with the `MariaDB`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  storage:
    size: 1Gi
    pvcRetentionPolicy:
      whenDeleted: Delete
      whenScaled: Retain
```

* `whenDeleted`: What happens to the PVCs when the `MariaDB` is deleted.
* `whenScaled`: What happens to the PVCs of the removed `Pods` when the `MariaDB` is scaled down.

Both accept `Retain` and `Delete`. The operator passes the policy to the `StatefulSet` as its [`persistentVolumeClaimRetentionPolicy`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#persistentvolumeclaim-retention). It's only applied on Kubernetes 1.32 or later; on older versions, the operator ignores the field.

## Ephemeral storage

Provisioning standalone `MariaDB` instances with ephemeral storage can be done by setting `ephemeral = true`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  storage:
    ephemeral: true
```

This may be useful for multiple use cases, like provisioning ephemeral `MariaDBs` for the integration tests of your CI.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}