# Physical backups

## What is a physical backup?

A physical backup is a snapshot of the entire data directory (`/var/lib/mysql`), including all data files. This type of backup captures the exact state of the database at a specific point in time, allowing for quick restoration in case of data loss or corruption.

Physical backups are the recommended method for backing up `MariaDB` databases, especially in production environments, as they are faster and more efficient than [logical backups](logical_backup.md).

## Backup strategies

Multiple strategies are available for performing physical backups, including:
- **mariadb-backup**: Taken using the enterprise version of [mariadb-backup](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup), specifically [MariaDB Enterprise backup](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup#nonblocking-backups), which is available in the `MariaDB` enterprise images. The operator supports scheduling `Jobs` to perform backups using this utility.
- **Kubernetes VolumeSnapshot**: Leverage [Kubernetes VolumeSnapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)  to create snapshots of the persistent volumes used by the `MariaDB` `Pods`. This method relies on a compatible CSI (Container Storage Interface) driver that supports volume snapshots. See the [VolumeSnapshots](#volumesnapshots) section for more details.

In order to use `VolumeSnapshots`, you will need to provide a `VolumeSnapshotClass` that is compatible with your storage provider. The operator will use this class to create snapshots of the persistent volumes:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  mariaDbRef:
    name: mariadb
  storage:
    volumeSnapshot:
      volumeSnapshotClassName: csi-hostpath-snapclass
```

For the rest of compatible [backup storage types](#storage-types), the `mariadb-backup` CLI will be used to perform the backup. For instance, to use `S3` as backup storage:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  mariaDbRef:
    name: mariadb
  storage:
    s3:
      bucket: physicalbackups
      endpoint: minio.minio.svc.cluster.local:9000
      accessKeyIdSecretKeyRef:
        name: minio
        key: access-key-id
      secretAccessKeySecretKeyRef:
        name: minio
        key: secret-access-key
      tls:
        enabled: true
        caSecretKeyRef:
          name: minio-ca
          key: ca.crt
```

## Storage types

Multiple storage types are supported for storing physical backups, including:
- **S3 compatible storage**: Store backups in a S3 compatible storage, such as [AWS S3](https://aws.amazon.com/s3/) or [Minio](https://github.com/minio/minio).
- **Azure Blob Storage**: Store backups in an [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs).
- **Persistent Volume Claims (PVC)**: Use any of the [StorageClasses](https://kubernetes.io/docs/concepts/storage/storage-classes/) available in your Kubernetes cluster to create a `PersistentVolumeClaim` (PVC) for storing backups.
- **Kubernetes Volumes**: Store backups in any of the [in-tree storage providers](https://kubernetes.io/docs/concepts/storage/volumes/#volume-types) supported by Kubernetes out of the box, such as NFS.
- **Kubernetes VolumeSnapshots**: Use [Kubernetes VolumeSnapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) to create snapshots of the persistent volumes used by the `MariaDB` `Pods`. This method relies on a compatible CSI (Container Storage Interface) driver that supports volume snapshots. See the [VolumeSnapshots](#volumesnapshots) section for more details.


## Scheduling

Physical backup schedule can be optionally configured using the `spec.schedule` field in the `PhysicalBackup` resource. When empty, a single backup job is scheduled:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  mariaDbRef:
    name: mariadb
    waitForIt: true
  schedule:
    cron: "*/1 * * * *"
    suspend: false
    immediate: true
    onDemand: "1"
    onPrimaryChange: true 
  # [...]
```

- `cron`: [Cron expression](https://en.wikipedia.org/wiki/Cron) to define the backup schedule.
- `suspend`: Setting it to `true`, it prevents new backups from being scheduled.
- `immediate`: Setting it `true`, it schedules a backup immediately after creating the `PhysicalBackup` resource.
- `onDemand`: Schedule identifier for triggering an on-demand backup. If the identifier is different from the one tracked under `status.lastScheduleOnDemand`, a new physical backup is triggered.
- `onPrimaryChange`: By setting it to `true`, it schedules a new backup after the  primary `Pod` in the referred `MariaDB` instance is changed. This is particularly useful for [point-in-time recovery](./pitr.md#full-base-backup).

It is very important to note that, by default, backups are only scheduled if the referred `MariaDB` resource is in ready state. Setting `mariaDbRef.waitForIt=false` skips this readiness check, so backups can be scheduled even if the `MariaDB` resource is not ready.

`waitForIt=false` only skips the readiness check. Whatever its value, the operator doesn't schedule a backup while the `MariaDB`:

- is suspended
- is restoring a backup or initializing
- is switching over its primary
- is being updated, or has an update pending
- is resizing its storage
- has a Galera cluster that isn't ready
- is replaying binary logs, or has a binary log replay pending

## Compression

When using physical backups based on `mariadb-backup`, you are able to choose the compression algorithm used to compress the backup files. The available options are:
- `bzip2`: Good compression ratio, but slower compression/decompression speed compared to gzip.
- `gzip`: Good compression/decompression speed, but worse compression ratio compared to bzip2.
- `none`: No compression.

To specify the compression algorithm, you can use the `compression` field in the `PhysicalBackup` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  mariaDbRef:
    name: mariadb
  compression: bzip2
  # [...]
```

`compression` is defaulted to `none` by the operator.

## Server-Side Encryption with Customer-Provided Keys (SSE-C) For S3

You can enable server-side encryption using your own encryption key (SSE-C) by providing a reference to a `Secret` containing a 32-byte (256-bit) key encoded in base64:

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: ssec-key
stringData:
  # 32-byte key encoded in base64 (use: openssl rand -base64 32)
  customer-key: YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoxMjM0NTY=
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  mariaDbRef:
    name: mariadb
  storage:
    s3:
      bucket: physicalbackups
      endpoint: minio.minio.svc.cluster.local:9000
      accessKeyIdSecretKeyRef:
        name: minio
        key: access-key-id
      secretAccessKeySecretKeyRef:
        name: minio
        key: secret-access-key
      tls:
        enabled: true
        caSecretKeyRef:
          name: minio-ca
          key: ca.crt
      ssec:
        customerKeySecretKeyRef:
          name: ssec-key
          key: customer-key
```

{% hint style="warning" %}
When using SSE-C, you are responsible for managing and securely storing the encryption key. If you lose the key, you will not be able to decrypt your backups. Ensure you have proper key management procedures in place.
{% endhint %}

{% hint style="info" %}
When restoring from SSE-C encrypted backups via `bootstrapFrom`, the same key must be provided in the S3 configuration.
{% endhint %}

## Retention policy

You can define a retention policy both for backups based on `mariadb-backup` and for `VolumeSnapshots`. The retention policy allows you to specify how long backups should be retained before they are automatically deleted. This can be defined via the `maxRetention` field in the `PhysicalBackup` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  # [...]
  mariaDbRef:
    name: mariadb
  maxRetention: 720h # 30 days
  # [...]
```

If you don't set `maxRetention`, it defaults to `720h` (30 days), so backups older than 30 days are deleted.

When using physical backups based on `mariadb-backup`, the operator will automatically delete backups files in the specified storage older than the retention period. The cleanup process will be performed after each successful backup.

When using `VolumeSnapshots`, the operator will automatically delete the `VolumeSnapshot` resources older than the retention period using the Kubernetes API. The cleanup process will be performed after a `VolumeSnapshot` is successfully created.


## Target policy

You can define a target policy both for backups based on `mariadb-backup` and for `VolumeSnapshots`. The target policy allows you to specify in which `Pod` the backup should be taken. This can be defined via the `target` field in the `PhysicalBackup` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  # [...]
  mariaDbRef:
    name: mariadb
  target: Replica
  # [...]
```

The following target policies are available:
- `Replica` (default): The backup will be taken in a ready replica. With replication, the replica must also be replicating without errors. If no such replica is available, the backup will not be scheduled.
- `PreferReplica`: The backup will be taken in a ready replica if available, otherwise it will be taken in the primary `Pod`.

The target policy only applies to `MariaDB` resources with replication or Galera. A single-instance `MariaDB` has no replicas, so its backups are always taken in its only `Pod`, whatever `target` is set to.

When using the `PreferReplica` target policy, you may be willing to schedule the backups even if the `MariaDB` resource is not ready. In this case, you can set `mariaDbRef.waitForIt=false` to allow scheduling the backup even if no replicas are available.

## Restoration

Physical backups can only be restored in brand new `MariaDB` instances without any existing data. This means that you cannot restore a physical backup into an existing `MariaDB` instance that already has data.

This also applies to storage left behind by a deleted `MariaDB`. If the storage PVCs of an earlier `MariaDB` with the same name still exist, the restoration doesn't start. The `MariaDB` reports an init error, and the operator emits a `MariaDBInitError` event and keeps retrying:

```bash
kubectl get events --field-selector involvedObject.name=mariadb-galera
LAST SEEN   TYPE      REASON             OBJECT                   MESSAGE
10s         Warning   MariaDBInitError   mariadb/mariadb-galera   Unable to init MariaDB: storage PVCs already exist
```

Delete the old storage PVCs, then the restoration proceeds. To have the PVCs deleted together with a `MariaDB`, see [PVC retention policy](../storage.md#pvc-retention-policy).

To perform a restoration, you can specify a `PhysicalBackup` as restoration source under the `spec.bootstrapFrom` field in the `MariaDB` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  # [...]
  bootstrapFrom:
    backupRef:
      name: physicalbackup
      kind: PhysicalBackup
  # [...]
```

This will take into account the backup strategy and storage type used in the `PhysicalBackup`, and it will perform the restoration accordingly.

As an alternative, you can also provide a reference to an S3 bucket that was previously used to store the physical backup files:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  bootstrapFrom:
    s3:
      bucket: physicalbackups
      prefix: mariadb
      endpoint: minio.minio.svc.cluster.local:9000
      accessKeyIdSecretKeyRef:
        name: minio
        key: access-key-id
      secretAccessKeySecretKeyRef:
        name: minio
        key: secret-access-key
      tls:
        enabled: true
        caSecretKeyRef:
          name: minio-ca
          key: ca.crt
    backupContentType: Physical
  storage:
    size: 1Gi
```

It is important to note that the `backupContentType` field must be set to `Physical` when restoring from a physical backup. This ensures that the operator uses the correct restoration method.

Similarly, you can restore from an Azure Blob Storage container that was previously used to store the physical backup files. The `azureBlob` fields are the same as in the [`PhysicalBackup` storage](#azure-blob-storage-credentials):

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  bootstrapFrom:
    azureBlob:
      containerName: physicalbackup
      serviceURL: https://examplestorageaccount.blob.core.windows.net
      prefix: mariadb
      storageAccountName: examplestorageaccount
      storageAccountKey:
        name: azurite-key
        key: storageAccountKey
      tls:
        enabled: true
        caSecretKeyRef:
          name: azurite-certs
          key: cert.pem
    backupContentType: Physical
  storage:
    size: 1Gi
```

To restore a `VolumeSnapshot`, you can provide a reference to a specific `VolumeSnapshot` resource in the `spec.bootstrapFrom` field:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  # [...]
  bootstrapFrom:
    volumeSnapshotRef:
      name: physicalbackup-20250611163352
  # [...]
```

## Target recovery time

By default, the operator will match the closest backup available to the current time. You can specify a different target recovery time by using the `targetRecoveryTime` field in the `PhysicalBackup` resource. This lets you define the exact point in time you want to restore to:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  # [...]
  bootstrapFrom:
    backupRef:
      name: physicalbackup
      kind: PhysicalBackup
    targetRecoveryTime: 2025-06-17T08:07:00Z
  # [...]
```
Only backups strictly before or at `targetRecoveryTime` will be matched.

`targetRecoveryTime` selects a backup from a restoration source, so `bootstrapFrom` must always name one. These rules apply to `bootstrapFrom`:

- It must have a source: `backupRef`, `volumeSnapshotRef`, `pointInTimeRecoveryRef`, `s3`, `azureBlob` or `volume`.
- `volumeSnapshotRef` can't be combined with `s3`, `volume` or `restoreJob`.
- `pointInTimeRecoveryRef` can't be combined with `backupRef` or `volumeSnapshotRef`.
- `backupContentType` is inferred from `backupRef.kind` (`Backup` means `Logical`, `PhysicalBackup` means `Physical`), and is `Physical` for `volumeSnapshotRef`. For any other source it defaults to `Logical`, so set `backupContentType: Physical` when you restore a physical backup from `s3` or `azureBlob`. A `backupContentType` that contradicts `backupRef.kind` or `volumeSnapshotRef` is rejected.

## Timeout

By default, both backups based on `mariadb-backup` and `VolumeSnapshots` will have a timeout of 1 hour. You can change this timeout by using the `timeout` field in the `PhysicalBackup` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  # [...]
  mariaDbRef:
    name: mariadb
  timeout: 2h
  # [...]
```

When timed out, the operator will delete the `Jobs` or `VolumeSnapshots` resources associated with the `PhysicalBackup` resource. The operator will create new `Jobs` or `VolumeSnapshots` to retry the backup operation if the `PhysicalBackup` resource is still scheduled.

## Log level

When taking backups based on `mariadb-backup`, you can specify the log level to be used by the `mariadb-enterprise-operator` container using the `logLevel` field in the `PhysicalBackup` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  # [...]
  mariaDbRef:
    name: mariadb
  logLevel: debug
  # [...]
```

## Extra options

When taking backups based on `mariadb-backup`, you can specify extra options to be passed to the `mariadb-backup` command using the `args` field in the `PhysicalBackup` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  # [...]
  mariaDbRef:
    name: mariadb
  args:
    - "--verbose"
  # [...]
```

Refer to the [mariadb-backup documentation](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options) for a list of available options.

## Azure Blob Storage Credentials

Credentials for accessing Azure Blob Storage can be provided via the `azureBlob` key in the storage field of the `PhysicalBackup` resource. The credentials are provided as a reference to a Kubernetes `Secret`:

```yaml
---
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  mariaDbRef:
    name: mariadb
  target: Replica
  compression: bzip2
  storage:
    azureBlob:
      containerName: physicalbackup
      serviceURL: https://physicalbackup.blob.core.windows.net # Format is: `https://%s.blob.core.windows.net/` where `%s` is the containerName
      prefix: mariadb
      storageAccountName: exampleStorageAccount
      storageAccountKey:
        name: azurite-key
        key: storageAccountKey
      # Optional.
      # tls:
      #   enabled: true
      #   caSecretKeyRef:
      #     name: azurite-certs
      #     key: cert.pem
```

Alternatively, you may choose to omit the `storageAccountKey` and `storageAccountName` if you are using [managed identity](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)

## S3 credentials

Credentials for accessing an S3 compatible storage can be provided via the `s3` key in the `storage` field of the `PhysicalBackup` resource. The credentials can be provided as a reference to a Kubernetes `Secret`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  mariaDbRef:
    name: mariadb
  storage:
    s3:
      bucket: physicalbackups
      endpoint: minio.minio.svc.cluster.local:9000
      accessKeyIdSecretKeyRef:
        name: minio
        key: access-key-id
      secretAccessKeySecretKeyRef:
        name: minio
        key: secret-access-key
      tls:
        enabled: true
        caSecretKeyRef:
          name: minio-ca
          key: ca.crt
```

Alternatively, if you are running in EKS, you can use dynamic credentials from an EKS Service Account using EKS Pod Identity or IRSA:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: mariadb-backup
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::<<account_id>>:role/my-role-irsa
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  mariaDbRef:
    name: mariadb
  serviceAccountName: mariadb-backup
  storage:
    s3:
      bucket: physicalbackups
      prefix: mariadb
      endpoint: s3.us-east-1.amazonaws.com
      region:  us-east-1
      tls:
        enabled: true
```

By leaving out the `accessKeyIdSecretKeyRef` and `secretAccessKeySecretKeyRef` credentials and pointing to the correct `serviceAccountName`, the backup `Job` will use the dynamic credentials from EKS.

## Staging area

{% hint style="info" %}
Backups based on `mariadb-backup` use a staging area when they're stored in S3 or in Azure Blob Storage. Only S3 backups let you configure it with `stagingStorage`: the operator rejects `stagingStorage` in a `PhysicalBackup` that doesn't use S3. Azure Blob Storage backups always stage to an `emptyDir` volume on the node where the backup `Job` runs, so make sure that the nodes have enough ephemeral storage for your largest backup.

When restoring, `bootstrapFrom.stagingStorage` works for both S3 and Azure Blob Storage.
{% endhint %}

When using S3 storage for backups, a staging area is used for keeping the external backups while they are being processed. By default, this staging area is an `emptyDir` volume, which means that the backups are temporarily stored in the node's local storage where the `PhysicalBackup` `Job` is scheduled. In production environments, large backups may lead to issues if the node doesn't have sufficient space, potentially causing the backup/restore process to fail.

Additionally, when restoring these backups, the operator will pull the backup files from S3, uncompress them if needded, and restore them to each of the `MariaDB` `Pods` in the cluster individually. To save network bandwidth and compute resources, a staging area is used to keep the uncompressed backup files after they have been restored to the first `MariaDB` `Pod`. This allows the operator to restore the same backup to the rest of `MariaDB` `Pods` seamlessly, without needing to pull and uncompress the backup again.

To configure the staging area, you can use the `stagingStorage` field in the `PhysicalBackup` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  mariaDbRef:
    name: mariadb
  storage:
    s3:
      bucket: physicalbackups
      prefix: mariadb
      endpoint: minio.minio.svc.cluster.local:9000
      region:  us-east-1
      accessKeyIdSecretKeyRef:
        name: minio
        key: access-key-id
      secretAccessKeySecretKeyRef:
        name: minio
        key: secret-access-key
      tls:
        enabled: true
        caSecretKeyRef:
          name: minio-ca
          key: ca.crt
  stagingStorage:
    persistentVolumeClaim:
      resources:
        requests:
          storage: 1Gi
      accessModes:
        - ReadWriteOnce
```

Similarly, you may also use a staging area when [bootstrapping from backup](#restoration), in the `MariaDB` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  mariaDbRef:
    name: mariadb
  bootstrapFrom:
    s3:
      bucket: physicalbackups
      prefix: mariadb
      endpoint: minio.minio.svc.cluster.local:9000
      accessKeyIdSecretKeyRef:
        name: minio
        key: access-key-id
      secretAccessKeySecretKeyRef:
        name: minio
        key: secret-access-key
      tls:
        enabled: true
        caSecretKeyRef:
          name: minio-ca
          key: ca.crt
    backupContentType: Physical
    stagingStorage:
      persistentVolumeClaim:
        resources:
          requests:
            storage: 1Gi
        accessModes:
          - ReadWriteOnce
  storage:
    size: 1Gi
```

In the examples above, a PVC with the default `StorageClass` will be provisioned to be used as staging area.

## `VolumeSnapshots`

{% hint style="warning" %}
 Before using this feature, ensure that you meet the following prerequisites :
 - [external-snapshotter](https://github.com/kubernetes-csi/external-snapshotter) and its CRs are installed in the cluster.
 - You have a compatible CSI driver that supports `VolumeSnapshots` installed in the cluster.
 - You have a `VolumeSnapshotClass` configured for your CSI driver.

{% endhint %}

The operator is capable of creating [`VolumeSnapshot` resources](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) of the PVCs used by the `MariaDB` `Pods`. This allows you to create point-in-time snapshots of your data in a Kubernetes-native way, leveraging the capabilities of your storage provider.

The scheduling, [retention policy](#retention-policy) (`maxRetention`), [timeout](#timeout) and [target policy](#target-policy) fields apply to `VolumeSnapshots` too. The fields that configure the backup `Job` don't, because no `Job` is created: compression, `stagingStorage`, extra `args`, `successfulJobsHistoryLimit` and `failedJobsHistoryLimit`. The main difference with the `mariadb-backup` based backups is that the operator will not create a `Job` to perform the backup, but instead it will create a `VolumeSnapshot` resource directly.

In order to create consistent, point-in-time snapshots of the `MariaDB` data, the operator will perform the following steps:
1. Execute a `BACKUP STAGE START` statement followed by `BACKUP STAGE BLOCK_COMMIT` in the target `Pod`, which is chosen by the [target policy](#target-policy).
2. Create a `VolumeSnapshot` resource of the data PVC mounted by the target `Pod`.
3. Wait until the `VolumeSnapshot` is provisioned by the storage system. When timing out, the operator will delete the `VolumeSnapshot` resource and retry the operation.
4. Issue a `BACKUP STAGE END` statement.

This backup process is described in the [MariaDB documentation](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/backup-optimization#taking-snapshots) and is designed to be [non-blocking](#non-blocking-physical-backups).

## Non-blocking physical backups

Both for `mariadb-backup` and `VolumeSnapshot` [backup strategies](#backup-strategies), the enterprise operator performs non-blocking physical backups by leveraging the [`BACKUP STAGE` feature.](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-and-backup-stage-commands). This implies that the backups are taken without long read locks, enabling consistent, production-grade backups with minimal impact on running workloads, ideal for high-availability and performance-sensitive environments.

## Important considerations and limitations

### Root credentials

When restoring a backup, the root credentials specified through the `spec.rootPasswordSecretKeyRef` field in the `MariaDB` resource must match the ones in the backup. These credentials are utilized by the liveness and readiness probes, and if they are invalid, the probes will fail, causing your `MariaDB` `Pods` to restart after the backup restoration.

### Restore `Job`

When using backups based on `mariadb-backup`, restoring and uncompressing large backups can consume significant compute resources and may cause restoration `Jobs` to become stuck due to insufficient resources. To prevent this, you can define the compute resources allocated to the `Job`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  # [...]
  bootstrapFrom:
    restoreJob:
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          memory: 1Gi
  # [...]
```

### `ReadWriteOncePod` access mode partially supported

When using backups based on `mariadb-backup`, the data PVC used by the `MariaDB` `Pod` cannot use the [`ReadWriteOncePod`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) access mode, as it needs to be mounted at the same time by both the `MariaDB` `Pod` and the `PhysicalBackup` `Job`. In this case, please use either the `ReadWriteOnce` or `ReadWriteMany` access modes instead.

Alternatively, if you want to keep using the `ReadWriteOncePod` access mode, you must use backups based on `VolumeSnapshots`, which do not require creating a `Job` to perform the backup and therefore avoid the volume sharing limitation.


### `PhysicalBackup` `Jobs` scheduling

`PhysicalBackup` `Jobs` must mount the data PVC used by the target `MariaDB` `Pod`, which is chosen by the [target policy](#target-policy). To avoid scheduling issues caused by the commonly used `ReadWriteOnce` access mode, the operator schedules backup `Jobs` on the same node as `MariaDB` by default.

If you prefer to disable this behavior and allow `Jobs` to run on any node, you can set `podAffinity=false`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  # [...]
  mariaDbRef:
    name: mariadb
  podAffinity: false
  # [...]
```

This configuration may be suitable when using the `ReadWriteMany` access mode, which allows multiple `Pods` across different nodes to mount the volume simultaneously.

## Troubleshooting

Custom columns are used to display the status of the `PhysicalBackup` resource:

```bash
kubectl get physicalbackups

NAME             COMPLETE   STATUS    MARIADB   LAST SCHEDULED   AGE
physicalbackup   True       Success   mariadb   17s              17s
```

To get a higher level of detail, you can also check the `status` field directly:

```bash
kubectl get physicalbackups physicalbackup -o json | jq -r '.status'

{
  "conditions": [
    {
      "lastTransitionTime": "2025-07-14T07:01:14Z",
      "message": "Success",
      "reason": "JobComplete",
      "status": "True",
      "type": "Complete"
    }
  ],
  "lastScheduleCheckTime": "2025-07-14T07:00:00Z",
  "lastScheduleTime": "2025-07-14T07:00:00Z",
  "nextScheduleTime": "2025-07-15T07:00:00Z"
}
```

You may also check the related events for the `PhysicalBackup` resource to see if there are any issues:

```bash
kubectl get events --field-selector involvedObject.name=physicalbackup

LAST SEEN   TYPE     REASON                  OBJECT                                 MESSAGE
116s        Normal   WaitForFirstConsumer    persistentvolumeclaim/physicalbackup   waiting for first consumer to be created before binding
116s        Normal   JobScheduled            physicalbackup/physicalbackup          Job physicalbackup-20250714140837 scheduled
116s        Normal   ExternalProvisioning    persistentvolumeclaim/physicalbackup   Waiting for a volume to be created either by the external provisioner 'rancher.io/local-path' or manually by the system administrator. If volume creation is delayed, please verify that the provisioner is running and correctly registered.
116s        Normal   Provisioning            persistentvolumeclaim/physicalbackup   External provisioner is provisioning volume for claim "default/physicalbackup"
113s        Normal   ProvisioningSucceeded   persistentvolumeclaim/physicalbackup   Successfully provisioned volume pvc-7b7c71f9-ea7e-4950-b612-2d41d7ab35b7
```

### Common errors

#### `mariadb-backup` log copy incomplete: consider increasing `innodb_log_file_size`

In some situations, when using the `mariadb-backup` strategy, you may encounter the following error in the backup `Job` logs:

```bash
mariadb [00] 2025-08-04 09:15:57 Was only able to copy log from 58087 to 59916, not 68968; try increasing
innodb_log_file_size
mariadb mariabackup: Stopping log copying thread.[00] 2025-08-04 09:15:57 Retrying read of log at LSN=59916
```

This can be addressed by increasing the `innodb_log_file_size` in the `MariaDB` configuration. You can do this by adding the following to your `MariaDB` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  # [...]
  myCnf: |
    [mariadb]
    innodb_log_file_size=200M
  # [...]
```

Refer to [MDEV-36159](https://jira.mariadb.org/browse/MDEV-36237) for further details on this issue.

#### `mariadb-backup` `Job` fails to start because the `Pod` cannot mount `MariaDB` PVC created with [openebs/lvm-localpv](https://github.com/openebs/lvm-localpv) `StorageClass` provider

Without explicitly enabled [shared option](https://github.com/openebs/lvm-localpv/blob/develop/design%2Flvm%2Fstorageclass-parameters%2Fshared.md) the `ReadWriteOnce` access mode is treated as `ReadWriteOncePod`.

Refer to [openebs/lvm-localpv#281](https://github.com/openebs/lvm-localpv/issues/281) for further details on this issue.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}