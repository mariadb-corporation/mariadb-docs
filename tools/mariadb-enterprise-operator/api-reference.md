---
description: >-
  Technical documentation of the Custom Resource Definitions (CRDs) and API
  fields used to configure the MariaDB Enterprise Kubernetes Operator.
---

# API Reference

## Packages

* [enterprise.mariadb.com/v1alpha1](api-reference.md#enterprisemariadbcomv1alpha1)

## enterprise.mariadb.com/v1alpha1

Package v1alpha1 contains API Schema definitions for the v1alpha1 API group

### Resource Types

* [Backup](api-reference.md#backup)
* [Connection](api-reference.md#connection)
* [Database](api-reference.md#database)
* [ExternalMariaDB](api-reference.md#externalmariadb)
* [Grant](api-reference.md#grant)
* [MariaDB](api-reference.md#mariadb)
* [MaxScale](api-reference.md#maxscale)
* [PhysicalBackup](api-reference.md#physicalbackup)
* [Restore](api-reference.md#restore)
* [SqlJob](api-reference.md#sqljob)
* [User](api-reference.md#user)

#### Affinity

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#affinity-v1-core.

_Appears in:_

* [AffinityConfig](api-reference.md#affinityconfig)

| Field                                                                   | Description | Default | Validation |
| ----------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `podAntiAffinity` [_PodAntiAffinity_](api-reference.md#podantiaffinity) |             |         |            |
| `nodeAffinity` [_NodeAffinity_](api-reference.md#nodeaffinity)          |             |         |            |

#### AffinityConfig

AffinityConfig defines policies to schedule Pods in Nodes.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [Exporter](api-reference.md#exporter)
* [Job](api-reference.md#job)
* [JobPodTemplate](api-reference.md#jobpodtemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScalePodTemplate](api-reference.md#maxscalepodtemplate)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PodTemplate](api-reference.md#podtemplate)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                                                   | Description                                                                                                                                                                                                                  | Default | Validation |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `podAntiAffinity` [_PodAntiAffinity_](api-reference.md#podantiaffinity) |                                                                                                                                                                                                                              |         |            |
| `nodeAffinity` [_NodeAffinity_](api-reference.md#nodeaffinity)          |                                                                                                                                                                                                                              |         |            |
| `antiAffinityEnabled` _boolean_                                         | <p>AntiAffinityEnabled configures PodAntiAffinity so each Pod is scheduled in a different Node, enabling HA.<br>Make sure you have at least as many Nodes available as the replicas to not end up with unscheduled Pods.</p> |         |            |

#### Agent

Agent is a sidecar agent that co-operates with mariadb-enterprise-operator.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)
* [Replication](api-reference.md#replication)
* [ReplicationSpec](api-reference.md#replicationspec)

| Field                                                                                                                         | Description                                                                                                                          | Default | Validation                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------------------------------------------- |
| `command` _string array_                                                                                                      | Command to be used in the Container.                                                                                                 |         |                                              |
| `args` _string array_                                                                                                         | Args to be used in the Container.                                                                                                    |         |                                              |
| `env` [_EnvVar_](api-reference.md#envvar) _array_                                                                             | Env represents the environment variables to be injected in a container.                                                              |         |                                              |
| `envFrom` [_EnvFromSource_](api-reference.md#envfromsource) _array_                                                           | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container.              |         |                                              |
| `volumeMounts` [_VolumeMount_](api-reference.md#volumemount) _array_                                                          | VolumeMounts to be used in the Container.                                                                                            |         |                                              |
| `livenessProbe` [_Probe_](api-reference.md#probe)                                                                             | LivenessProbe to be used in the Container.                                                                                           |         |                                              |
| `readinessProbe` [_Probe_](api-reference.md#probe)                                                                            | ReadinessProbe to be used in the Container.                                                                                          |         |                                              |
| `startupProbe` [_Probe_](api-reference.md#probe)                                                                              | StartupProbe to be used in the Container.                                                                                            |         |                                              |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                                   | Resources describes the compute resource requirements.                                                                               |         |                                              |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)                                                       | SecurityContext holds security configuration that will be applied to a container.                                                    |         |                                              |
| `image` _string_                                                                                                              | Image name to be used by the MariaDB instances. The supported format is `<image>:<tag>`.                                             |         |                                              |
| `imagePullPolicy` [_PullPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#pullpolicy-v1-core)     | ImagePullPolicy is the image pull policy. One of `Always`, `Never` or `IfNotPresent`. If not defined, it defaults to `IfNotPresent`. |         | <p>Enum: [Always Never IfNotPresent]<br></p> |
| `port` _integer_                                                                                                              | Port where the agent will be listening for API connections.                                                                          |         |                                              |
| `probePort` _integer_                                                                                                         | Port where the agent will be listening for probe connections.                                                                        |         |                                              |
| `kubernetesAuth` [_KubernetesAuth_](api-reference.md#kubernetesauth)                                                          | KubernetesAuth to be used by the agent container                                                                                     |         |                                              |
| `basicAuth` [_BasicAuth_](api-reference.md#basicauth)                                                                         | BasicAuth to be used by the agent container                                                                                          |         |                                              |
| `gracefulShutdownTimeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | GracefulShutdownTimeout is the time we give to the agent container in order to gracefully terminate in-flight requests.              |         |                                              |

#### AzureBlob







_Appears in:_
- [BootstrapFrom](#bootstrapfrom)
- [PhysicalBackupStorage](#physicalbackupstorage)
- [PointInTimeRecoveryStorage](#pointintimerecoverystorage)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `containerName` _string_ | ContainerName is the name of the storage container. |  | Required: \{\} <br /> |
| `serviceURL` _string_ | ServiceURL is the full URL for connecting to Azure, usually in the form: http(s)://<account>.blob.core.windows.net/. |  | Required: \{\} <br /> |
| `prefix` _string_ | Prefix indicates a folder/subfolder in the container. For example: mariadb/ or mariadb/backups. A trailing slash '/' is added if not provided. |  |  |
| `storageAccountName` _string_ | StorageAccountName is the name of the storage account. Pairs with StorageAccountKey for static credential authentication |  |  |
| `storageAccountKey` _[SecretKeySelector](#secretkeyselector)_ | StorageAccountKey is a reference to a Secret key containing the Azure Blob Storage Storage account Key. Pairs with StorageAccountKey for static credential authentication |  |  |
| `tls` _[TLSConfig](#tlsconfig)_ | TLS provides the configuration required to establish TLS connections with Azure Blob Storage. |  |  |


#### Backup

Backup is the Schema for the backups API. It is used to define backup jobs and its storage.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `Backup`                                                        |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_BackupSpec_](api-reference.md#backupspec)                                                                 |                                                                 |         |            |

#### BackupContentType

_Underlying type:_ _string_

BackupContentType defines the backup content type.

_Appears in:_

* [BootstrapFrom](api-reference.md#bootstrapfrom)

| Field      | Description                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------------- |
| `Logical`  | <p>BackupContentTypeLogical represents a logical backup created using mariadb-dump.<br></p>     |
| `Physical` | <p>BackupContentTypePhysical represents a physical backup created using mariadb-backup.<br></p> |

#### BackupSpec

BackupSpec defines the desired state of Backup

_Appears in:_

* [Backup](api-reference.md#backup)

| Field                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                         | Default   | Validation                                                  |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------- |
| `args` _string array_                                                                                                         | Args to be used in the Container.                                                                                                                                                                                                                                                                                                                                                   |           |                                                             |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                                   | Resources describes the compute resource requirements.                                                                                                                                                                                                                                                                                                                              |           |                                                             |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)                                                       | SecurityContext holds security configuration that will be applied to a container.                                                                                                                                                                                                                                                                                                   |           |                                                             |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                                                                                                                                                                                                                                                                                                                     |           |                                                             |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                                                                                                                                                                                          |           |                                                             |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                                                                                                                                                                                                  |           |                                                             |
| `serviceAccountName` _string_                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                                                                                                                                                                                                        |           |                                                             |
| `affinity` [_AffinityConfig_](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                     |           |                                                             |
| `nodeSelector` _object (keys:string, values:string)_                                                                          | NodeSelector to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                 |           |                                                             |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                  |           |                                                             |
| `priorityClassName` _string_                                                                                                  | PriorityClassName to be used in the Pod.                                                                                                                                                                                                                                                                                                                                            |           |                                                             |
| `successfulJobsHistoryLimit` _integer_                                                                                        | SuccessfulJobsHistoryLimit defines the maximum number of successful Jobs to be displayed.                                                                                                                                                                                                                                                                                           |           | <p>Minimum: 0<br></p>                                       |
| `failedJobsHistoryLimit` _integer_                                                                                            | FailedJobsHistoryLimit defines the maximum number of failed Jobs to be displayed.                                                                                                                                                                                                                                                                                                   |           | <p>Minimum: 0<br></p>                                       |
| `timeZone` _string_                                                                                                           | TimeZone defines the timezone associated with the cron expression.                                                                                                                                                                                                                                                                                                                  |           |                                                             |
| `mariaDbRef` [_MariaDBRef_](api-reference.md#mariadbref)                                                                      | MariaDBRef is a reference to a MariaDB object.                                                                                                                                                                                                                                                                                                                                      |           | <p>Required: {}<br></p>                                     |
| `compression` [_CompressAlgorithm_](api-reference.md#compressalgorithm)                                                       | Compression algorithm to be used in the Backup.                                                                                                                                                                                                                                                                                                                                     |           | <p>Enum: [none bzip2 gzip]<br></p>                          |
| `stagingStorage` [_BackupStagingStorage_](api-reference.md#backupstagingstorage)                                              | <p>StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.<br>It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Backup Job is scheduled.<br>The staging area gets cleaned up after each backup is completed, consider this for sizing it appropriately.</p> |           |                                                             |
| `storage` [_BackupStorage_](api-reference.md#backupstorage)                                                                   | Storage defines the final storage for backups.                                                                                                                                                                                                                                                                                                                                      |           | <p>Required: {}<br></p>                                     |
| `schedule` [_Schedule_](api-reference.md#schedule)                                                                            | Schedule defines when the Backup will be taken.                                                                                                                                                                                                                                                                                                                                     |           |                                                             |
| `maxRetention` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)            | <p>MaxRetention defines the retention policy for backups. Old backups will be cleaned up by the Backup Job.<br>It defaults to 30 days.</p>                                                                                                                                                                                                                                          |           |                                                             |
| `databases` _string array_                                                                                                    | Databases defines the logical databases to be backed up. If not provided, all databases are backed up.                                                                                                                                                                                                                                                                              |           |                                                             |
| `ignoreGlobalPriv` _boolean_                                                                                                  | <p>IgnoreGlobalPriv indicates to ignore the mysql.global_priv in backups.<br>If not provided, it will default to true when the referred MariaDB instance has Galera enabled and otherwise to false.</p>                                                                                                                                                                             |           |                                                             |
| `logLevel` _string_                                                                                                           | LogLevel to be used in the Backup Job. It defaults to 'info'.                                                                                                                                                                                                                                                                                                                       | info      | <p>Enum: [debug info warn error dpanic panic fatal]<br></p> |
| `backoffLimit` _integer_                                                                                                      | BackoffLimit defines the maximum number of attempts to successfully take a Backup.                                                                                                                                                                                                                                                                                                  |           |                                                             |
| `restartPolicy` [_RestartPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#restartpolicy-v1-core) | RestartPolicy to be added to the Backup Pod.                                                                                                                                                                                                                                                                                                                                        | OnFailure | <p>Enum: [Always OnFailure Never]<br></p>                   |
| `inheritMetadata` [_Metadata_](api-reference.md#metadata)                                                                     | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                                                                                                                                                                                         |           |                                                             |

#### BackupStagingStorage

BackupStagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [BootstrapFrom](api-reference.md#bootstrapfrom)
* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)
* [RestoreSource](api-reference.md#restoresource)
* [RestoreSpec](api-reference.md#restorespec)

| Field                                                                                             | Description                                              | Default | Validation |
| ------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------- | ---------- |
| `persistentVolumeClaim` [_PersistentVolumeClaimSpec_](api-reference.md#persistentvolumeclaimspec) | PersistentVolumeClaim is a Kubernetes PVC specification. |         |            |
| `volume` [_StorageVolumeSource_](api-reference.md#storagevolumesource)                            | Volume is a Kubernetes volume specification.             |         |            |

#### BackupStorage

BackupStorage defines the final storage for backups.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)

| Field                                                                                             | Description                                                               | Default | Validation |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------- | ---------- |
| `s3` [_S3_](api-reference.md#s3)                                                                  | S3 defines the configuration to store backups in a S3 compatible storage. |         |            |
| `persistentVolumeClaim` [_PersistentVolumeClaimSpec_](api-reference.md#persistentvolumeclaimspec) | PersistentVolumeClaim is a Kubernetes PVC specification.                  |         |            |
| `volume` [_StorageVolumeSource_](api-reference.md#storagevolumesource)                            | Volume is a Kubernetes volume specification.                              |         |            |

#### BasicAuth

BasicAuth refers to the basic authentication mechanism utilized for establishing a connection from the operator to the agent.

_Appears in:_

* [Agent](api-reference.md#agent)

| Field                                                                                    | Description                                              | Default | Validation |
| ---------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------- | ---------- |
| `enabled` _boolean_                                                                      | Enabled is a flag to enable BasicAuth                    |         |            |
| `username` _string_                                                                      | Username to be used for basic authentication             |         |            |
| `passwordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref) | PasswordSecretKeyRef to be used for basic authentication |         |            |

#### BootstrapFrom

BootstrapFrom defines a source to bootstrap MariaDB from.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                            | Description                                                                                                                                                                                                                                                                                                     | Default | Validation                          |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------- |
| `backupRef` [_TypedLocalObjectReference_](api-reference.md#typedlocalobjectreference)                            | <p>BackupRef is reference to a backup object. If the Kind is not specified, a logical Backup is assumed.<br>This field takes precedence over S3 and Volume sources.</p>                                                                                                                                         |         |                                     |
| `volumeSnapshotRef` [_LocalObjectReference_](api-reference.md#localobjectreference)                              | <p>VolumeSnapshotRef is a reference to a VolumeSnapshot object.<br>This field takes precedence over S3 and Volume sources.</p>                                                                                                                                                                                  |         |                                     |
| `backupContentType` [_BackupContentType_](api-reference.md#backupcontenttype)                                    | <p>BackupContentType is the backup content type available in the source to bootstrap from.<br>It is inferred based on the BackupRef and VolumeSnapshotRef fields. If inference is not possible, it defaults to Logical.<br>Set this field explicitly when using physical backups from S3 or Volume sources.</p> |         | <p>Enum: [Logical Physical]<br></p> |
| `s3` [_S3_](api-reference.md#s3)                                                                                 | <p>S3 defines the configuration to restore backups from a S3 compatible storage.<br>This field takes precedence over the Volume source.</p>                                                                                                                                                                     |         |                                     |
| `volume` [_StorageVolumeSource_](api-reference.md#storagevolumesource)                                           | Volume is a Kubernetes Volume object that contains a backup.                                                                                                                                                                                                                                                    |         |                                     |
| `targetRecoveryTime` [_Time_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#time-v1-meta) | <p>TargetRecoveryTime is a RFC3339 (1970-01-01T00:00:00Z) date and time that defines the point in time recovery objective.<br>It is used to determine the closest restoration source in time.</p>                                                                                                               |         |                                     |
| `stagingStorage` [_BackupStagingStorage_](api-reference.md#backupstagingstorage)                                 | <p>StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.<br>It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Job is scheduled.</p>                                                   |         |                                     |
| `restoreJob` [_Job_](api-reference.md#job)                                                                       | RestoreJob defines additional properties for the Job used to perform the restoration.                                                                                                                                                                                                                           |         |                                     |

#### CSIVolumeSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#csivolumesource-v1-core.

_Appears in:_

* [StorageVolumeSource](api-reference.md#storagevolumesource)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field                                                                                  | Description | Default | Validation |
| -------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `driver` _string_                                                                      |             |         |            |
| `readOnly` _boolean_                                                                   |             |         |            |
| `fsType` _string_                                                                      |             |         |            |
| `volumeAttributes` _object (keys:string, values:string)_                               |             |         |            |
| `nodePublishSecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference) |             |         |            |

#### CertConfig



CertConfig defines parameters to configure a certificate.



_Appears in:_
- [ExternalTLS](#externaltls)
- [MaxScaleTLS](#maxscaletls)
- [TLS](#tls)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `caLifetime` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)_ | CALifetime defines the CA certificate validity. |  |  |
| `certLifetime` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)_ | CertLifetime defines the certificate validity. |  |  |
| `privateKeyAlgorithm` _string_ | PrivateKeyAlgorithm is the algorithm to be used for the CA and leaf certificate private keys.<br />One of: ECDSA or RSA |  | Enum: [ECDSA RSA] <br /> |
| `privateKeySize` _integer_ | PrivateKeyAlgorithm is the key size to be used for the CA and leaf certificate private keys.<br />Supported values: ECDSA(256, 384, 521), RSA(2048, 3072, 4096) |  |  |


#### CleanupPolicy

_Underlying type:_ _string_

CleanupPolicy defines the behavior for cleaning up a resource.

_Appears in:_

* [DatabaseSpec](api-reference.md#databasespec)
* [GrantSpec](api-reference.md#grantspec)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [SQLTemplate](api-reference.md#sqltemplate)
* [UserSpec](api-reference.md#userspec)

| Field    | Description                                                                                                             |
| -------- | ----------------------------------------------------------------------------------------------------------------------- |
| `Skip`   | <p>CleanupPolicySkip indicates that the resource will NOT be deleted from the database after the CR is deleted.<br></p> |
| `Delete` | <p>CleanupPolicyDelete indicates that the resource will be deleted from the database after the CR is deleted.<br></p>   |

#### CompressAlgorithm

_Underlying type:_ _string_

CompressAlgorithm defines the compression algorithm for a Backup resource.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)

| Field   | Description                                                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------------------ |
| `none`  | <p>No compression<br></p>                                                                                          |
| `bzip2` | <p>Bzip2 compression. Good compression ratio, but slower compression/decompression speed compared to gzip.<br></p> |
| `gzip`  | <p>Gzip compression. Good compression/decompression speed, but worse compression ratio compared to bzip2.<br></p>  |

#### ConfigMapKeySelector

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#configmapkeyselector-v1-core.

_Appears in:_

* [EnvVarSource](api-reference.md#envvarsource)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field           | Description | Default | Validation |
| --------------- | ----------- | ------- | ---------- |
| `name` _string_ |             |         |            |
| `key` _string_  |             |         |            |

#### ConfigMapVolumeSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#configmapvolumesource-v1-core.

_Appears in:_

* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field                   | Description | Default | Validation |
| ----------------------- | ----------- | ------- | ---------- |
| `name` _string_         |             |         |            |
| `defaultMode` _integer_ |             |         |            |

#### Connection

Connection is the Schema for the connections API. It is used to configure connection strings for the applications connecting to MariaDB.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `Connection`                                                    |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_ConnectionSpec_](api-reference.md#connectionspec)                                                         |                                                                 |         |            |

#### ConnectionSpec

ConnectionSpec defines the desired state of Connection

_Appears in:_

* [Connection](api-reference.md#connection)

| Field                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Default | Validation              |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------- |
| `secretName` _string_                                                                    | SecretName to be used in the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |         |                         |
| `secretTemplate` [_SecretTemplate_](api-reference.md#secrettemplate)                     | SecretTemplate to be used in the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |         |                         |
| `healthCheck` [_HealthCheck_](api-reference.md#healthcheck)                              | HealthCheck to be used in the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |         |                         |
| `params` _object (keys:string, values:string)_                                           | Params to be used in the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |         |                         |
| `serviceName` _string_                                                                   | ServiceName to be used in the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |         |                         |
| `port` _integer_                                                                         | Port to connect to. If not provided, it defaults to the MariaDB port or to the first MaxScale listener.                                                                                                                                                                                                                                                                                                                                                                                                 |         |                         |
| `mariaDbRef` [_MariaDBRef_](api-reference.md#mariadbref)                                 | MariaDBRef is a reference to the MariaDB to connect to. Either MariaDBRef or MaxScaleRef must be provided.                                                                                                                                                                                                                                                                                                                                                                                              |         |                         |
| `maxScaleRef` [_ObjectReference_](api-reference.md#objectreference)                      | MaxScaleRef is a reference to the MaxScale to connect to. Either MariaDBRef or MaxScaleRef must be provided.                                                                                                                                                                                                                                                                                                                                                                                            |         |                         |
| `username` _string_                                                                      | Username to use for configuring the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |         | <p>Required: {}<br></p> |
| `passwordSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector)         | <p>PasswordSecretKeyRef is a reference to the password to use for configuring the Connection.<br>Either passwordSecretKeyRef or tlsClientCertSecretRef must be provided as client credentials.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.</p>                                                                                                                                                    |         |                         |
| `tlsClientCertSecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference) | <p>TLSClientCertSecretRef is a reference to a Kubernetes TLS Secret used as authentication when checking the connection health.<br>Either passwordSecretKeyRef or tlsClientCertSecretRef must be provided as client credentials.<br>If not provided, the client certificate provided by the referred MariaDB is used if TLS is enabled.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the client certificate.</p> |         |                         |
| `host` _string_                                                                          | Host to connect to. If not provided, it defaults to the MariaDB host or to the MaxScale host.                                                                                                                                                                                                                                                                                                                                                                                                           |         |                         |
| `database` _string_                                                                      | Database to use when configuring the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |         |                         |

#### ConnectionTemplate

ConnectionTemplate defines a template to customize Connection objects.

_Appears in:_

* [ConnectionSpec](api-reference.md#connectionspec)
* [ExternalMariaDBSpec](api-reference.md#externalmariadbspec)
* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                | Description                                                                                             | Default | Validation |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `secretName` _string_                                                | SecretName to be used in the Connection.                                                                |         |            |
| `secretTemplate` [_SecretTemplate_](api-reference.md#secrettemplate) | SecretTemplate to be used in the Connection.                                                            |         |            |
| `healthCheck` [_HealthCheck_](api-reference.md#healthcheck)          | HealthCheck to be used in the Connection.                                                               |         |            |
| `params` _object (keys:string, values:string)_                       | Params to be used in the Connection.                                                                    |         |            |
| `serviceName` _string_                                               | ServiceName to be used in the Connection.                                                               |         |            |
| `port` _integer_                                                     | Port to connect to. If not provided, it defaults to the MariaDB port or to the first MaxScale listener. |         |            |

#### Container

Container object definition.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)
* [PodTemplate](api-reference.md#podtemplate)

| Field                                                                                                                     | Description                                                                                                                          | Default | Validation                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------------------------------------------- |
| `name` _string_                                                                                                           | Name to be given to the container.                                                                                                   |         |                                              |
| `image` _string_                                                                                                          | Image name to be used by the container. The supported format is `<image>:<tag>`.                                                     |         | <p>Required: {}<br></p>                      |
| `imagePullPolicy` [_PullPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of `Always`, `Never` or `IfNotPresent`. If not defined, it defaults to `IfNotPresent`. |         | <p>Enum: [Always Never IfNotPresent]<br></p> |
| `command` _string array_                                                                                                  | Command to be used in the Container.                                                                                                 |         |                                              |
| `args` _string array_                                                                                                     | Args to be used in the Container.                                                                                                    |         |                                              |
| `env` [_EnvVar_](api-reference.md#envvar) _array_                                                                         | Env represents the environment variables to be injected in a container.                                                              |         |                                              |
| `volumeMounts` [_VolumeMount_](api-reference.md#volumemount) _array_                                                      | VolumeMounts to be used in the Container.                                                                                            |         |                                              |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                               | Resources describes the compute resource requirements.                                                                               |         |                                              |

#### ContainerTemplate

ContainerTemplate defines a template to configure Container objects.

_Appears in:_

* [Agent](api-reference.md#agent)
* [InitContainer](api-reference.md#initcontainer)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                       | Description                                                                                                             | Default | Validation |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `command` _string array_                                                    | Command to be used in the Container.                                                                                    |         |            |
| `args` _string array_                                                       | Args to be used in the Container.                                                                                       |         |            |
| `env` [_EnvVar_](api-reference.md#envvar) _array_                           | Env represents the environment variables to be injected in a container.                                                 |         |            |
| `envFrom` [_EnvFromSource_](api-reference.md#envfromsource) _array_         | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container. |         |            |
| `volumeMounts` [_VolumeMount_](api-reference.md#volumemount) _array_        | VolumeMounts to be used in the Container.                                                                               |         |            |
| `livenessProbe` [_Probe_](api-reference.md#probe)                           | LivenessProbe to be used in the Container.                                                                              |         |            |
| `readinessProbe` [_Probe_](api-reference.md#probe)                          | ReadinessProbe to be used in the Container.                                                                             |         |            |
| `startupProbe` [_Probe_](api-reference.md#probe)                            | StartupProbe to be used in the Container.                                                                               |         |            |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements) | Resources describes the compute resource requirements.                                                                  |         |            |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)     | SecurityContext holds security configuration that will be applied to a container.                                       |         |            |

#### CooperativeMonitoring

_Underlying type:_ _string_

CooperativeMonitoring enables coordination between multiple MaxScale instances running monitors. See: https://mariadb.com/docs/server/architecture/components/maxscale/monitors/mariadbmon/use-cooperative-locking-ha-maxscale-mariadb-monitor/

_Appears in:_

* [MaxScaleMonitor](api-reference.md#maxscalemonitor)

| Field                 | Description                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `majority_of_all`     | <p>CooperativeMonitoringMajorityOfAll requires a lock from the majority of the MariaDB servers, even the ones that are down.<br></p> |
| `majority_of_running` | <p>CooperativeMonitoringMajorityOfRunning requires a lock from the majority of the MariaDB servers.<br></p>                          |

#### CronJobTemplate

CronJobTemplate defines parameters for configuring CronJob objects.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                  | Description                                                                               | Default | Validation            |
| -------------------------------------- | ----------------------------------------------------------------------------------------- | ------- | --------------------- |
| `successfulJobsHistoryLimit` _integer_ | SuccessfulJobsHistoryLimit defines the maximum number of successful Jobs to be displayed. |         | <p>Minimum: 0<br></p> |
| `failedJobsHistoryLimit` _integer_     | FailedJobsHistoryLimit defines the maximum number of failed Jobs to be displayed.         |         | <p>Minimum: 0<br></p> |
| `timeZone` _string_                    | TimeZone defines the timezone associated with the cron expression.                        |         |                       |

#### Database

Database is the Schema for the databases API. It is used to define a logical database as if you were running a 'CREATE DATABASE' statement.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `Database`                                                      |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_DatabaseSpec_](api-reference.md#databasespec)                                                             |                                                                 |         |            |

#### DatabaseSpec

DatabaseSpec defines the desired state of Database

_Appears in:_

* [Database](api-reference.md#database)

| Field                                                                                                                 | Description                                                         | Default           | Validation                     |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------- | ------------------------------ |
| `requeueInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations.         |                   |                                |
| `retryInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)   | RetryInterval is the interval used to perform retries.              |                   |                                |
| `cleanupPolicy` [_CleanupPolicy_](api-reference.md#cleanuppolicy)                                                     | CleanupPolicy defines the behavior for cleaning up a SQL resource.  |                   | <p>Enum: [Skip Delete]<br></p> |
| `mariaDbRef` [_MariaDBRef_](api-reference.md#mariadbref)                                                              | MariaDBRef is a reference to a MariaDB object.                      |                   | <p>Required: {}<br></p>        |
| `characterSet` _string_                                                                                               | CharacterSet to use in the Database.                                | utf8              |                                |
| `collate` _string_                                                                                                    | Collate to use in the Database.                                     | utf8\_general\_ci |                                |
| `name` _string_                                                                                                       | Name overrides the default Database name provided by metadata.name. |                   | <p>MaxLength: 80<br></p>       |

#### EmptyDirVolumeSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#emptydirvolumesource-v1-core.

_Appears in:_

* [StorageVolumeSource](api-reference.md#storagevolumesource)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field                                                                                                                  | Description | Default | Validation |
| ---------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `medium` [_StorageMedium_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#storagemedium-v1-core) |             |         |            |
| `sizeLimit` [_Quantity_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#quantity-resource-api)   |             |         |            |

#### EnvFromSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#envfromsource-v1-core.

_Appears in:_

* [Agent](api-reference.md#agent)
* [ContainerTemplate](api-reference.md#containertemplate)
* [InitContainer](api-reference.md#initcontainer)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                          | Description | Default | Validation |
| ------------------------------------------------------------------------------ | ----------- | ------- | ---------- |
| `prefix` _string_                                                              |             |         |            |
| `configMapRef` [_LocalObjectReference_](api-reference.md#localobjectreference) |             |         |            |
| `secretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)    |             |         |            |

#### EnvVar

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#envvarsource-v1-core.

_Appears in:_

* [Agent](api-reference.md#agent)
* [Container](api-reference.md#container)
* [ContainerTemplate](api-reference.md#containertemplate)
* [InitContainer](api-reference.md#initcontainer)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                       | Description                                                | Default | Validation |
| ----------------------------------------------------------- | ---------------------------------------------------------- | ------- | ---------- |
| `name` _string_                                             | Name of the environment variable. Must be a C\_IDENTIFIER. |         |            |
| `value` _string_                                            |                                                            |         |            |
| `valueFrom` [_EnvVarSource_](api-reference.md#envvarsource) |                                                            |         |            |

#### EnvVarSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#envvarsource-v1-core.

_Appears in:_

* [EnvVar](api-reference.md#envvar)

| Field                                                                             | Description | Default | Validation |
| --------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `fieldRef` [_ObjectFieldSelector_](api-reference.md#objectfieldselector)          |             |         |            |
| `configMapKeyRef` [_ConfigMapKeySelector_](api-reference.md#configmapkeyselector) |             |         |            |
| `secretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector)          |             |         |            |

#### ExecAction

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#execaction-v1-core.

_Appears in:_

* [Probe](api-reference.md#probe)
* [ProbeHandler](api-reference.md#probehandler)

| Field                    | Description | Default | Validation |
| ------------------------ | ----------- | ------- | ---------- |
| `command` _string array_ |             |         |            |

#### Exporter

Exporter defines a metrics exporter container.

_Appears in:_

* [MariadbMetrics](api-reference.md#mariadbmetrics)
* [MaxScaleMetrics](api-reference.md#maxscalemetrics)

| Field                                                                                                                         | Description                                                                                                                          | Default | Validation                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------------------------------------------- |
| `image` _string_                                                                                                              | Image name to be used as metrics exporter. The supported format is `<image>:<tag>`.                                                  |         |                                              |
| `imagePullPolicy` [_PullPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#pullpolicy-v1-core)     | ImagePullPolicy is the image pull policy. One of `Always`, `Never` or `IfNotPresent`. If not defined, it defaults to `IfNotPresent`. |         | <p>Enum: [Always Never IfNotPresent]<br></p> |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                           |         |                                              |
| `args` _string array_                                                                                                         | Args to be used in the Container.                                                                                                    |         |                                              |
| `port` _integer_                                                                                                              | Port where the exporter will be listening for connections.                                                                           |         |                                              |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                                   | Resources describes the compute resource requirements.                                                                               |         |                                              |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                                                                      |         |                                              |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)                                                       | SecurityContext holds container-level security attributes.                                                                           |         |                                              |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings.                                                   |         |                                              |
| `affinity` [_AffinityConfig_](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                                                                      |         |                                              |
| `nodeSelector` _object (keys:string, values:string)_                                                                          | NodeSelector to be used in the Pod.                                                                                                  |         |                                              |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                                                                                                   |         |                                              |
| `priorityClassName` _string_                                                                                                  | PriorityClassName to be used in the Pod.                                                                                             |         |                                              |

#### ExternalMariaDB

ExternalMariaDB is the Schema for the external MariaDBs API. It is used to define external MariaDB server.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `ExternalMariaDB`                                               |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_ExternalMariaDBSpec_](api-reference.md#externalmariadbspec)                                               |                                                                 |         |            |

#### ExternalMariaDBSpec

ExternalMariaDBSpec defines the desired state of an External MariaDB

_Appears in:_

* [ExternalMariaDB](api-reference.md#externalmariadb)

| Field                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                          | Default | Validation                                   |
| ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------- |
| `image` _string_                                                                                                          | <p>Image name to be used to perform operations on the external MariaDB, for example, for taking backups.<br>The supported format is <code>&#x3C;image>:&#x3C;tag></code>. Only MariaDB official images are supported.<br>If not provided, the MariaDB image version be inferred by the operator in runtime. The default MariaDB image will be used in this case,</p> |         |                                              |
| `imagePullPolicy` [_PullPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of `Always`, `Never` or `IfNotPresent`. If not defined, it defaults to `IfNotPresent`.                                                                                                                                                                                                                                 |         | <p>Enum: [Always Never IfNotPresent]<br></p> |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                                                                                                                                                                           |         |                                              |
| `inheritMetadata` [_Metadata_](api-reference.md#metadata)                                                                 | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                                                                                                                                                                          |         |                                              |
| `host` _string_                                                                                                           | Hostname of the external MariaDB.                                                                                                                                                                                                                                                                                                                                    |         | <p>Required: {}<br></p>                      |
| `port` _integer_                                                                                                          | Port of the external MariaDB.                                                                                                                                                                                                                                                                                                                                        | 3306    |                                              |
| `username` _string_                                                                                                       | Username is the username to connect to the external MariaDB.                                                                                                                                                                                                                                                                                                         |         | <p>Required: {}<br></p>                      |
| `passwordSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector)                                          | PasswordSecretKeyRef is a reference to the password to connect to the external MariaDB.                                                                                                                                                                                                                                                                              |         |                                              |
| `tls` [_ExternalTLS_](api-reference.md#externaltls)                                                                       | TLS defines the PKI to be used with the external MariaDB.                                                                                                                                                                                                                                                                                                            |         |                                              |
| `connection` [_ConnectionTemplate_](api-reference.md#connectiontemplate)                                                  | Connection defines a template to configure a Connection for the external MariaDB.                                                                                                                                                                                                                                                                                    |         |                                              |

#### ExternalTLS

ExternalTLS defines the TLS configuration for external MariaDB instances.

_Appears in:_

* [ExternalMariaDBSpec](api-reference.md#externalmariadbspec)

| Field                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Default | Validation                                                     |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------- |
| `enabled` _boolean_                                                                   | <p>Enabled indicates whether TLS is enabled, determining if certificates should be issued and mounted to the MariaDB instance.<br>It is enabled by default.</p>                                                                                                                                                                                                                                                                                                                                                                                                                 |         |                                                                |
| `required` _boolean_                                                                  | <p>Required specifies whether TLS must be enforced for all connections.<br>User TLS requirements take precedence over this.<br>It disabled by default.</p>                                                                                                                                                                                                                                                                                                                                                                                                                      |         |                                                                |
| `versions` _string array_                                                             | <p>Versions specifies the supported TLS versions for this MariaDB instance.<br>By default, the MariaDB's default supported versions are used. See: https://mariadb.com/kb/en/ssltls-system-variables/#tls_version.</p>                                                                                                                                                                                                                                                                                                                                                          |         | <p>items:Enum: [TLSv1.0 TLSv1.1 TLSv1.2 TLSv1.3]<br></p>       |
| `serverCASecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)   | <p>ServerCASecretRef is a reference to a Secret containing the server certificate authority keypair. It is used to establish trust and issue server certificates.<br>One of:<br>- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.<br>- Secret containing only the 'ca.crt' in order to establish trust. In this case, either serverCertSecretRef or serverCertIssuerRef must be provided.<br>If not provided, a self-signed CA will be provisioned to issue the server certificate.</p>        |         |                                                                |
| `serverCertSecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference) | <p>ServerCertSecretRef is a reference to a TLS Secret containing the server certificate.<br>It is mutually exclusive with serverCertIssuerRef.</p>                                                                                                                                                                                                                                                                                                                                                                                                                              |         |                                                                |
| `serverCertIssuerRef` [_ObjectReference_](api-reference.md#objectreference)           | <p>ServerCertIssuerRef is a reference to a cert-manager issuer object used to issue the server certificate. cert-manager must be installed previously in the cluster.<br>It is mutually exclusive with serverCertSecretRef.<br>By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via serverCASecretRef.</p>                                                                                                                                                                            |         |                                                                |
| `serverCertConfig` [_TLSConfig_](api-reference.md#tlsconfig)                          | <p>ServerCertConfig allows configuring the server certificates, either issued by the operator or cert-manager.<br>If not set, the default settings will be used.</p>                                                                                                                                                                                                                                                                                                                                                                                                            |         |                                                                |
| `clientCASecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)   | <p>ClientCASecretRef is a reference to a Secret containing the client certificate authority keypair. It is used to establish trust and issue client certificates.<br>One of:<br>- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.<br>- Secret containing only the 'ca.crt' in order to establish trust. In this case, either clientCertSecretRef or clientCertIssuerRef fields must be provided.<br>If not provided, a self-signed CA will be provisioned to issue the client certificate.</p> |         |                                                                |
| `clientCertSecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference) | <p>ClientCertSecretRef is a reference to a TLS Secret containing the client certificate.<br>It is mutually exclusive with clientCertIssuerRef.</p>                                                                                                                                                                                                                                                                                                                                                                                                                              |         |                                                                |
| `clientCertIssuerRef` [_ObjectReference_](api-reference.md#objectreference)           | <p>ClientCertIssuerRef is a reference to a cert-manager issuer object used to issue the client certificate. cert-manager must be installed previously in the cluster.<br>It is mutually exclusive with clientCertSecretRef.<br>By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via clientCASecretRef.</p>                                                                                                                                                                            |         |                                                                |
| `clientCertConfig` [_TLSConfig_](api-reference.md#tlsconfig)                          | <p>ClientCertConfig allows configuring the client certificates, either issued by the operator or cert-manager.<br>If not set, the default settings will be used.</p>                                                                                                                                                                                                                                                                                                                                                                                                            |         |                                                                |
| `galeraSSTEnabled` _boolean_                                                          | <p>GaleraSSTEnabled determines whether Galera SST connections should use TLS.<br>It disabled by default.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |         |                                                                |
| `galeraServerSSLMode` _string_                                                        | <p>GaleraServerSSLMode defines the server SSL mode for a Galera Enterprise cluster.<br>This field is only supported and applicable for Galera Enterprise >= 10.6 instances.<br>Refer to the MariaDB Enterprise docs for more detail: https://mariadb.com/docs/galera-cluster/galera-security/mariadb-enterprise-cluster-security#wsrep-tls-modes</p>                                                                                                                                                                                                                            |         | <p>Enum: [PROVIDER SERVER SERVER_X509]<br></p>                 |
| `galeraClientSSLMode` _string_                                                        | <p>GaleraClientSSLMode defines the client SSL mode for a Galera Enterprise cluster.<br>This field is only supported and applicable for Galera Enterprise >= 10.6 instances.<br>Refer to the MariaDB Enterprise docs for more detail: https://mariadb.com/docs/galera-cluster/galera-security/mariadb-enterprise-cluster-security#sst-tls-modes</p>                                                                                                                                                                                                                              |         | <p>Enum: [DISABLED REQUIRED VERIFY_CA VERIFY_IDENTITY]<br></p> |
| `mutual` _boolean_                                                                    | <p>Mutual specifies whether TLS must be mutual between server and client for external connections.<br>When set to false, the client certificate will not be sent during the TLS handshake.<br>It is enabled by default.</p>                                                                                                                                                                                                                                                                                                                                                     |         |                                                                |

#### Galera

Galera allows you to enable multi-master HA via Galera in your MariaDB cluster.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                             | Description                                                                                                                                                                                                                   | Default | Validation                                     |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------- |
| `primary` [_PrimaryGalera_](api-reference.md#primarygalera)       | Primary is the Galera configuration for the primary node.                                                                                                                                                                     |         |                                                |
| `sst` [_SST_](api-reference.md#sst)                               | <p>SST is the Snapshot State Transfer used when new Pods join the cluster.<br>More info: https://galeracluster.com/library/documentation/sst.html.</p>                                                                        |         | <p>Enum: [rsync mariabackup mysqldump]<br></p> |
| `availableWhenDonor` _boolean_                                    | AvailableWhenDonor indicates whether a donor node should be responding to queries. It defaults to false.                                                                                                                      |         |                                                |
| `galeraLibPath` _string_                                          | <p>GaleraLibPath is a path inside the MariaDB image to the wsrep provider plugin. It is defaulted if not provided.<br>More info: https://galeracluster.com/library/documentation/mysql-wsrep-options.html#wsrep-provider.</p> |         |                                                |
| `replicaThreads` _integer_                                        | <p>ReplicaThreads is the number of replica threads used to apply Galera write sets in parallel.<br>More info: https://mariadb.com/kb/en/galera-cluster-system-variables/#wsrep_slave_threads.</p>                             |         |                                                |
| `providerOptions` _object (keys:string, values:string)_           | <p>ProviderOptions is map of Galera configuration parameters.<br>More info: https://mariadb.com/kb/en/galera-cluster-system-variables/#wsrep_provider_options.</p>                                                            |         |                                                |
| `agent` [_Agent_](api-reference.md#agent)                         | Agent is a sidecar agent that co-operates with mariadb-enterprise-operator.                                                                                                                                                   |         |                                                |
| `recovery` [_GaleraRecovery_](api-reference.md#galerarecovery)    | <p>GaleraRecovery is the recovery process performed by the operator whenever the Galera cluster is not healthy.<br>More info: https://galeracluster.com/library/documentation/crash-recovery.html.</p>                        |         |                                                |
| `initContainer` [_InitContainer_](api-reference.md#initcontainer) | InitContainer is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.                                                                                                             |         |                                                |
| `initJob` [_GaleraInitJob_](api-reference.md#galerainitjob)       | InitJob defines a Job that co-operates with mariadb-enterprise-operator by performing initialization tasks.                                                                                                                   |         |                                                |
| `config` [_GaleraConfig_](api-reference.md#galeraconfig)          | GaleraConfig defines storage options for the Galera configuration files.                                                                                                                                                      |         |                                                |
| `clusterName` _string_                                            | ClusterName is the name of the cluster to be used in the Galera config file.                                                                                                                                                  |         |                                                |
| `enabled` _boolean_                                               | Enabled is a flag to enable Galera.                                                                                                                                                                                           |         |                                                |

#### GaleraConfig

GaleraConfig defines storage options for the Galera configuration files.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field                                                                               | Description                                                                                                                                                                                                                                         | Default | Validation |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `reuseStorageVolume` _boolean_                                                      | <p>ReuseStorageVolume indicates that storage volume used by MariaDB should be reused to store the Galera configuration files.<br>It defaults to false, which implies that a dedicated volume for the Galera configuration files is provisioned.</p> |         |            |
| `volumeClaimTemplate` [_VolumeClaimTemplate_](api-reference.md#volumeclaimtemplate) | VolumeClaimTemplate is a template for the PVC that will contain the Galera configuration files shared between the InitContainer, Agent and MariaDB.                                                                                                 |         |            |

#### GaleraInitJob

GaleraInitJob defines a Job used to be used to initialize the Galera cluster.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field                                                                       | Description                                                     | Default | Validation |
| --------------------------------------------------------------------------- | --------------------------------------------------------------- | ------- | ---------- |
| `metadata` [_Metadata_](api-reference.md#metadata)                          | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements) | Resources describes the compute resource requirements.          |         |            |

#### GaleraRecovery

GaleraRecovery is the recovery process performed by the operator whenever the Galera cluster is not healthy. More info: https://galeracluster.com/library/documentation/crash-recovery.html.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `enabled` _boolean_                                                                                                            | Enabled is a flag to enable GaleraRecovery.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |         |            |
| `minClusterSize` [_IntOrString_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#intorstring-intstr-util) | <p>MinClusterSize is the minimum number of replicas to consider the cluster healthy. It can be either a number of replicas (1) or a percentage (50%).<br>If Galera consistently reports less replicas than this value for the given 'ClusterHealthyTimeout' interval, a cluster recovery is initiated.<br>It defaults to '1' replica, and it is highly recommendeded to keep this value at '1' in most cases.<br>If set to more than one replica, the cluster recovery process may restart the healthy replicas as well.</p> |         |            |
| `clusterMonitorInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)   | ClusterMonitorInterval represents the interval used to monitor the Galera cluster health.                                                                                                                                                                                                                                                                                                                                                                                                                                    |         |            |
| `clusterHealthyTimeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)    | <p>ClusterHealthyTimeout represents the duration at which a Galera cluster, that consistently failed health checks,<br>is considered unhealthy, and consequently the Galera recovery process will be initiated by the operator.</p>                                                                                                                                                                                                                                                                                          |         |            |
| `clusterBootstrapTimeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)  | <p>ClusterBootstrapTimeout is the time limit for bootstrapping a cluster.<br>Once this timeout is reached, the Galera recovery state is reset and a new cluster bootstrap will be attempted.</p>                                                                                                                                                                                                                                                                                                                             |         |            |
| `clusterUpscaleTimeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)    | ClusterUpscaleTimeout represents the maximum duration for upscaling the cluster's StatefulSet during the recovery process.                                                                                                                                                                                                                                                                                                                                                                                                   |         |            |
| `clusterDownscaleTimeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)  | ClusterDownscaleTimeout represents the maximum duration for downscaling the cluster's StatefulSet during the recovery process.                                                                                                                                                                                                                                                                                                                                                                                               |         |            |
| `podRecoveryTimeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)       | PodRecoveryTimeout is the time limit for recevorying the sequence of a Pod during the cluster recovery.                                                                                                                                                                                                                                                                                                                                                                                                                      |         |            |
| `podSyncTimeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)           | PodSyncTimeout is the time limit for a Pod to join the cluster after having performed a cluster bootstrap during the cluster recovery.                                                                                                                                                                                                                                                                                                                                                                                       |         |            |
| `forceClusterBootstrapInPod` _string_                                                                                          | <p>ForceClusterBootstrapInPod allows you to manually initiate the bootstrap process in a specific Pod.<br>IMPORTANT: Use this option only in exceptional circumstances. Not selecting the Pod with the highest sequence number may result in data loss.<br>IMPORTANT: Ensure you unset this field after completing the bootstrap to allow the operator to choose the appropriate Pod to bootstrap from in an event of cluster recovery.</p>                                                                                  |         |            |
| `job` [_GaleraRecoveryJob_](api-reference.md#galerarecoveryjob)                                                                | Job defines a Job that co-operates with mariadb-enterprise-operator by performing the Galera cluster recovery .                                                                                                                                                                                                                                                                                                                                                                                                              |         |            |

#### GaleraRecoveryJob

GaleraRecoveryJob defines a Job used to be used to recover the Galera cluster.

_Appears in:_

* [GaleraRecovery](api-reference.md#galerarecovery)

| Field                                                                       | Description                                                                                                           | Default | Validation |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `metadata` [_Metadata_](api-reference.md#metadata)                          | Refer to Kubernetes API documentation for fields of `metadata`.                                                       |         |            |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements) | Resources describes the compute resource requirements.                                                                |         |            |
| `podAffinity` _boolean_                                                     | PodAffinity indicates whether the recovery Jobs should run in the same Node as the MariaDB Pods. It defaults to true. |         |            |

#### GaleraSpec

GaleraSpec is the Galera desired state specification.

_Appears in:_

* [Galera](api-reference.md#galera)

| Field                                                             | Description                                                                                                                                                                                                                   | Default | Validation                                     |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------- |
| `primary` [_PrimaryGalera_](api-reference.md#primarygalera)       | Primary is the Galera configuration for the primary node.                                                                                                                                                                     |         |                                                |
| `sst` [_SST_](api-reference.md#sst)                               | <p>SST is the Snapshot State Transfer used when new Pods join the cluster.<br>More info: https://galeracluster.com/library/documentation/sst.html.</p>                                                                        |         | <p>Enum: [rsync mariabackup mysqldump]<br></p> |
| `availableWhenDonor` _boolean_                                    | AvailableWhenDonor indicates whether a donor node should be responding to queries. It defaults to false.                                                                                                                      |         |                                                |
| `galeraLibPath` _string_                                          | <p>GaleraLibPath is a path inside the MariaDB image to the wsrep provider plugin. It is defaulted if not provided.<br>More info: https://galeracluster.com/library/documentation/mysql-wsrep-options.html#wsrep-provider.</p> |         |                                                |
| `replicaThreads` _integer_                                        | <p>ReplicaThreads is the number of replica threads used to apply Galera write sets in parallel.<br>More info: https://mariadb.com/kb/en/galera-cluster-system-variables/#wsrep_slave_threads.</p>                             |         |                                                |
| `providerOptions` _object (keys:string, values:string)_           | <p>ProviderOptions is map of Galera configuration parameters.<br>More info: https://mariadb.com/kb/en/galera-cluster-system-variables/#wsrep_provider_options.</p>                                                            |         |                                                |
| `agent` [_Agent_](api-reference.md#agent)                         | Agent is a sidecar agent that co-operates with mariadb-enterprise-operator.                                                                                                                                                   |         |                                                |
| `recovery` [_GaleraRecovery_](api-reference.md#galerarecovery)    | <p>GaleraRecovery is the recovery process performed by the operator whenever the Galera cluster is not healthy.<br>More info: https://galeracluster.com/library/documentation/crash-recovery.html.</p>                        |         |                                                |
| `initContainer` [_InitContainer_](api-reference.md#initcontainer) | InitContainer is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.                                                                                                             |         |                                                |
| `initJob` [_GaleraInitJob_](api-reference.md#galerainitjob)       | InitJob defines a Job that co-operates with mariadb-enterprise-operator by performing initialization tasks.                                                                                                                   |         |                                                |
| `config` [_GaleraConfig_](api-reference.md#galeraconfig)          | GaleraConfig defines storage options for the Galera configuration files.                                                                                                                                                      |         |                                                |
| `clusterName` _string_                                            | ClusterName is the name of the cluster to be used in the Galera config file.                                                                                                                                                  |         |                                                |

#### GeneratedSecretKeyRef

GeneratedSecretKeyRef defines a reference to a Secret that can be automatically generated by mariadb-enterprise-operator if needed.

_Appears in:_

* [BasicAuth](api-reference.md#basicauth)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MariadbMetrics](api-reference.md#mariadbmetrics)
* [MaxScaleAuth](api-reference.md#maxscaleauth)
* [ReplicaReplication](api-reference.md#replicareplication)

| Field                | Description                                                                                        | Default | Validation |
| -------------------- | -------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `name` _string_      |                                                                                                    |         |            |
| `key` _string_       |                                                                                                    |         |            |
| `generate` _boolean_ | Generate indicates whether the Secret should be generated if the Secret referenced is not present. | false   |            |

#### Grant

Grant is the Schema for the grants API. It is used to define grants as if you were running a 'GRANT' statement.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `Grant`                                                         |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_GrantSpec_](api-reference.md#grantspec)                                                                   |                                                                 |         |            |

#### GrantSpec

GrantSpec defines the desired state of Grant

_Appears in:_

* [Grant](api-reference.md#grant)

| Field                                                                                                                 | Description                                                        | Default | Validation                             |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------- | -------------------------------------- |
| `requeueInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations.        |         |                                        |
| `retryInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)   | RetryInterval is the interval used to perform retries.             |         |                                        |
| `cleanupPolicy` [_CleanupPolicy_](api-reference.md#cleanuppolicy)                                                     | CleanupPolicy defines the behavior for cleaning up a SQL resource. |         | <p>Enum: [Skip Delete]<br></p>         |
| `mariaDbRef` [_MariaDBRef_](api-reference.md#mariadbref)                                                              | MariaDBRef is a reference to a MariaDB object.                     |         | <p>Required: {}<br></p>                |
| `privileges` _string array_                                                                                           | Privileges to use in the Grant.                                    |         | <p>MinItems: 1<br>Required: {}<br></p> |
| `database` _string_                                                                                                   | Database to use in the Grant.                                      | \*      |                                        |
| `table` _string_                                                                                                      | Table to use in the Grant.                                         | \*      |                                        |
| `username` _string_                                                                                                   | Username to use in the Grant.                                      |         | <p>Required: {}<br></p>                |
| `host` _string_                                                                                                       | Host to use in the Grant. It can be localhost, an IP or '%'.       |         |                                        |
| `grantOption` _boolean_                                                                                               | GrantOption to use in the Grant.                                   | false   |                                        |

#### Gtid

_Underlying type:_ _string_

Gtid indicates which Global Transaction ID (GTID) position mode should be used when connecting a replica to the master. See: https://mariadb.com/kb/en/gtid/#using-current\_pos-vs-slave\_pos.

_Appears in:_

* [ReplicaReplication](api-reference.md#replicareplication)

| Field        | Description                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `CurrentPos` | <p>GtidCurrentPos indicates the union of gtid_binlog_pos and gtid_slave_pos will be used when replicating from master.<br></p> |
| `SlavePos`   | <p>GtidSlavePos indicates that gtid_slave_pos will be used when replicating from master.<br></p>                               |

#### HTTPGetAction

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#httpgetaction-v1-core.

_Appears in:_

* [Probe](api-reference.md#probe)
* [ProbeHandler](api-reference.md#probehandler)

| Field                                                                                                                | Description | Default | Validation |
| -------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `path` _string_                                                                                                      |             |         |            |
| `port` [_IntOrString_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#intorstring-intstr-util) |             |         |            |
| `host` _string_                                                                                                      |             |         |            |
| `scheme` [_URIScheme_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#urischeme-v1-core)       |             |         |            |

#### HealthCheck

HealthCheck defines intervals for performing health checks.

_Appears in:_

* [ConnectionSpec](api-reference.md#connectionspec)
* [ConnectionTemplate](api-reference.md#connectiontemplate)

| Field                                                                                                               | Description                                                         | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------- | ---------- |
| `interval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)      | Interval used to perform health checks.                             |         |            |
| `retryInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | RetryInterval is the interval used to perform health check retries. |         |            |

#### HostPathVolumeSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#hostpathvolumesource-v1-core

_Appears in:_

* [StorageVolumeSource](api-reference.md#storagevolumesource)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field           | Description | Default | Validation |
| --------------- | ----------- | ------- | ---------- |
| `path` _string_ |             |         |            |
| `type` _string_ |             |         |            |

#### InitContainer

InitContainer is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)
* [Replication](api-reference.md#replication)
* [ReplicationSpec](api-reference.md#replicationspec)

| Field                                                                                                                     | Description                                                                                                                          | Default | Validation                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------------------------------------------- |
| `command` _string array_                                                                                                  | Command to be used in the Container.                                                                                                 |         |                                              |
| `args` _string array_                                                                                                     | Args to be used in the Container.                                                                                                    |         |                                              |
| `env` [_EnvVar_](api-reference.md#envvar) _array_                                                                         | Env represents the environment variables to be injected in a container.                                                              |         |                                              |
| `envFrom` [_EnvFromSource_](api-reference.md#envfromsource) _array_                                                       | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container.              |         |                                              |
| `volumeMounts` [_VolumeMount_](api-reference.md#volumemount) _array_                                                      | VolumeMounts to be used in the Container.                                                                                            |         |                                              |
| `livenessProbe` [_Probe_](api-reference.md#probe)                                                                         | LivenessProbe to be used in the Container.                                                                                           |         |                                              |
| `readinessProbe` [_Probe_](api-reference.md#probe)                                                                        | ReadinessProbe to be used in the Container.                                                                                          |         |                                              |
| `startupProbe` [_Probe_](api-reference.md#probe)                                                                          | StartupProbe to be used in the Container.                                                                                            |         |                                              |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                               | Resources describes the compute resource requirements.                                                                               |         |                                              |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)                                                   | SecurityContext holds security configuration that will be applied to a container.                                                    |         |                                              |
| `image` _string_                                                                                                          | Image name to be used by the MariaDB instances. The supported format is `<image>:<tag>`.                                             |         | <p>Required: {}<br></p>                      |
| `imagePullPolicy` [_PullPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of `Always`, `Never` or `IfNotPresent`. If not defined, it defaults to `IfNotPresent`. |         | <p>Enum: [Always Never IfNotPresent]<br></p> |

#### Job

Job defines a Job used to be used with MariaDB.

_Appears in:_

* [BootstrapFrom](api-reference.md#bootstrapfrom)
* [ReplicaBootstrapFrom](api-reference.md#replicabootstrapfrom)

| Field                                                                                                                         | Description                                                     | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------- | ---------- |
| `metadata` [_Metadata_](api-reference.md#metadata)                                                                            | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `affinity` [_AffinityConfig_](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                 |         |            |
| `nodeSelector` _object (keys:string, values:string)_                                                                          | NodeSelector to be used in the Pod.                             |         |            |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                              |         |            |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                                   | Resources describes the compute resource requirements.          |         |            |
| `args` _string array_                                                                                                         | Args to be used in the Container.                               |         |            |

#### JobContainerTemplate

JobContainerTemplate defines a template to configure Container objects that run in a Job.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                                                       | Description                                                                       | Default | Validation |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------- | ---------- |
| `args` _string array_                                                       | Args to be used in the Container.                                                 |         |            |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements) | Resources describes the compute resource requirements.                            |         |            |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)     | SecurityContext holds security configuration that will be applied to a container. |         |            |

#### JobPodTemplate

JobPodTemplate defines a template to configure Container objects that run in a Job.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                                                                                                         | Description                                                                        | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------- | ---------- |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                    |         |            |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.         |         |            |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings. |         |            |
| `serviceAccountName` _string_                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.       |         |            |
| `affinity` [_AffinityConfig_](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                    |         |            |
| `nodeSelector` _object (keys:string, values:string)_                                                                          | NodeSelector to be used in the Pod.                                                |         |            |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                                                 |         |            |
| `priorityClassName` _string_                                                                                                  | PriorityClassName to be used in the Pod.                                           |         |            |

#### KubernetesAuth

KubernetesAuth refers to the Kubernetes authentication mechanism utilized for establishing a connection from the operator to the agent. The agent validates the legitimacy of the service account token provided as an Authorization header by creating a TokenReview resource.

_Appears in:_

* [Agent](api-reference.md#agent)

| Field                            | Description                                                                                                                                                                                                                                           | Default | Validation |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `enabled` _boolean_              | Enabled is a flag to enable KubernetesAuth                                                                                                                                                                                                            |         |            |
| `authDelegatorRoleName` _string_ | <p>AuthDelegatorRoleName is the name of the ClusterRoleBinding that is associated with the "system:auth-delegator" ClusterRole.<br>It is necessary for creating TokenReview objects in order for the agent to validate the service account token.</p> |         |            |

#### LabelSelector

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#labelselector-v1-meta

_Appears in:_

* [PodAffinityTerm](api-reference.md#podaffinityterm)

| Field                                                                                              | Description | Default | Validation |
| -------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `matchLabels` _object (keys:string, values:string)_                                                |             |         |            |
| `matchExpressions` [_LabelSelectorRequirement_](api-reference.md#labelselectorrequirement) _array_ |             |         |            |

#### LabelSelectorRequirement

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#labelselectorrequirement-v1-meta

_Appears in:_

* [LabelSelector](api-reference.md#labelselector)

| Field                                                                                                                                    | Description | Default | Validation |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `key` _string_                                                                                                                           |             |         |            |
| `operator` [_LabelSelectorOperator_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#labelselectoroperator-v1-meta) |             |         |            |
| `values` _string array_                                                                                                                  |             |         |            |

#### LocalObjectReference

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#localobjectreference-v1-core.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [BootstrapFrom](api-reference.md#bootstrapfrom)
* [CSIVolumeSource](api-reference.md#csivolumesource)
* [ConfigMapKeySelector](api-reference.md#configmapkeyselector)
* [ConfigMapVolumeSource](api-reference.md#configmapvolumesource)
* [ConnectionSpec](api-reference.md#connectionspec)
* [EnvFromSource](api-reference.md#envfromsource)
* [Exporter](api-reference.md#exporter)
* [ExternalMariaDBSpec](api-reference.md#externalmariadbspec)
* [ExternalTLS](api-reference.md#externaltls)
* [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref)
* [JobPodTemplate](api-reference.md#jobpodtemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScalePodTemplate](api-reference.md#maxscalepodtemplate)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [MaxScaleTLS](api-reference.md#maxscaletls)
* [PhysicalBackupPodTemplate](api-reference.md#physicalbackuppodtemplate)
* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)
* [PodTemplate](api-reference.md#podtemplate)
* [ReplicaBootstrapFrom](api-reference.md#replicabootstrapfrom)
* [RestoreSource](api-reference.md#restoresource)
* [RestoreSpec](api-reference.md#restorespec)
* [SecretKeySelector](api-reference.md#secretkeyselector)
* [SqlJobSpec](api-reference.md#sqljobspec)
* [TLS](api-reference.md#tls)

| Field           | Description | Default | Validation |
| --------------- | ----------- | ------- | ---------- |
| `name` _string_ |             |         |            |

#### MariaDB

MariaDB is the Schema for the mariadbs API. It is used to define MariaDB clusters.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `MariaDB`                                                       |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_MariaDBSpec_](api-reference.md#mariadbspec)                                                               |                                                                 |         |            |

#### MariaDBMaxScaleSpec

MariaDBMaxScaleSpec defines a reduced version of MaxScale to be used with the current MariaDB.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                                                                  | Description                                                                                                                                                          | Default | Validation                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------- |
| `enabled` _boolean_                                                                                                                                    | Enabled is a flag to enable a MaxScale instance to be used with the current MariaDB.                                                                                 |         |                                              |
| `image` _string_                                                                                                                                       | <p>Image name to be used by the MaxScale instances. The supported format is <code>&#x3C;image>:&#x3C;tag></code>.<br>Only MariaDB official images are supported.</p> |         |                                              |
| `imagePullPolicy` [_PullPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#pullpolicy-v1-core)                              | ImagePullPolicy is the image pull policy. One of `Always`, `Never` or `IfNotPresent`. If not defined, it defaults to `IfNotPresent`.                                 |         | <p>Enum: [Always Never IfNotPresent]<br></p> |
| `services` [_MaxScaleService_](api-reference.md#maxscaleservice) _array_                                                                               | Services define how the traffic is forwarded to the MariaDB servers.                                                                                                 |         |                                              |
| `monitor` [_MaxScaleMonitor_](api-reference.md#maxscalemonitor)                                                                                        | Monitor monitors MariaDB server instances.                                                                                                                           |         |                                              |
| `admin` [_MaxScaleAdmin_](api-reference.md#maxscaleadmin)                                                                                              | Admin configures the admin REST API and GUI.                                                                                                                         |         |                                              |
| `config` [_MaxScaleConfig_](api-reference.md#maxscaleconfig)                                                                                           | Config defines the MaxScale configuration.                                                                                                                           |         |                                              |
| `auth` [_MaxScaleAuth_](api-reference.md#maxscaleauth)                                                                                                 | Auth defines the credentials required for MaxScale to connect to MariaDB.                                                                                            |         |                                              |
| `metrics` [_MaxScaleMetrics_](api-reference.md#maxscalemetrics)                                                                                        | Metrics configures metrics and how to scrape them.                                                                                                                   |         |                                              |
| `tls` [_MaxScaleTLS_](api-reference.md#maxscaletls)                                                                                                    | TLS defines the PKI to be used with MaxScale.                                                                                                                        |         |                                              |
| `connection` [_ConnectionTemplate_](api-reference.md#connectiontemplate)                                                                               | Connection provides a template to define the Connection for MaxScale.                                                                                                |         |                                              |
| `replicas` _integer_                                                                                                                                   | Replicas indicates the number of desired instances.                                                                                                                  |         |                                              |
| `podDisruptionBudget` [_PodDisruptionBudget_](api-reference.md#poddisruptionbudget)                                                                    | PodDisruptionBudget defines the budget for replica availability.                                                                                                     |         |                                              |
| `updateStrategy` [_StatefulSetUpdateStrategy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#statefulsetupdatestrategy-v1-apps) | UpdateStrategy defines the update strategy for the StatefulSet object.                                                                                               |         |                                              |
| `kubernetesService` [_ServiceTemplate_](api-reference.md#servicetemplate)                                                                              | KubernetesService defines a template for a Kubernetes Service object to connect to MaxScale.                                                                         |         |                                              |
| `guiKubernetesService` [_ServiceTemplate_](api-reference.md#servicetemplate)                                                                           | GuiKubernetesService define a template for a Kubernetes Service object to connect to MaxScale's GUI.                                                                 |         |                                              |
| `requeueInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)                                  | RequeueInterval is used to perform requeue reconciliations.                                                                                                          |         |                                              |

#### MariaDBRef

MariaDBRef is a reference to a MariaDB object.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [ConnectionSpec](api-reference.md#connectionspec)
* [DatabaseSpec](api-reference.md#databasespec)
* [GrantSpec](api-reference.md#grantspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)
* [UserSpec](api-reference.md#userspec)

| Field                 | Description                                                                                          | Default | Validation |
| --------------------- | ---------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `name` _string_       |                                                                                                      |         |            |
| `namespace` _string_  |                                                                                                      |         |            |
| `kind` _string_       | Kind of the referent.                                                                                |         |            |
| `waitForIt` _boolean_ | WaitForIt indicates whether the controller using this reference should wait for MariaDB to be ready. | true    |            |

#### MariaDBSpec

MariaDBSpec defines the desired state of MariaDB

_Appears in:_

* [MariaDB](api-reference.md#mariadb)

| Field                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Default | Validation                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------- |
| `command` _string array_                                                                                                      | Command to be used in the Container.                                                                                                                                                                                                                                                                                                                                                                                                                              |         |                                              |
| `args` _string array_                                                                                                         | Args to be used in the Container.                                                                                                                                                                                                                                                                                                                                                                                                                                 |         |                                              |
| `env` [_EnvVar_](api-reference.md#envvar) _array_                                                                             | Env represents the environment variables to be injected in a container.                                                                                                                                                                                                                                                                                                                                                                                           |         |                                              |
| `envFrom` [_EnvFromSource_](api-reference.md#envfromsource) _array_                                                           | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container.                                                                                                                                                                                                                                                                                                                                           |         |                                              |
| `volumeMounts` [_VolumeMount_](api-reference.md#volumemount) _array_                                                          | VolumeMounts to be used in the Container.                                                                                                                                                                                                                                                                                                                                                                                                                         |         |                                              |
| `livenessProbe` [_Probe_](api-reference.md#probe)                                                                             | LivenessProbe to be used in the Container.                                                                                                                                                                                                                                                                                                                                                                                                                        |         |                                              |
| `readinessProbe` [_Probe_](api-reference.md#probe)                                                                            | ReadinessProbe to be used in the Container.                                                                                                                                                                                                                                                                                                                                                                                                                       |         |                                              |
| `startupProbe` [_Probe_](api-reference.md#probe)                                                                              | StartupProbe to be used in the Container.                                                                                                                                                                                                                                                                                                                                                                                                                         |         |                                              |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                                   | Resources describes the compute resource requirements.                                                                                                                                                                                                                                                                                                                                                                                                            |         |                                              |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)                                                       | SecurityContext holds security configuration that will be applied to a container.                                                                                                                                                                                                                                                                                                                                                                                 |         |                                              |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                                                                                                                                                                                                                                                                                                                                                                                                   |         |                                              |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                                                                                                                                                                                                                                                                        |         |                                              |
| `initContainers` [_Container_](api-reference.md#container) _array_                                                            | InitContainers to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                                                                                             |         |                                              |
| `sidecarContainers` [_Container_](api-reference.md#container) _array_                                                         | SidecarContainers to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                                                                                          |         |                                              |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                                                                                                                                                                                                                                                                                |         |                                              |
| `serviceAccountName` _string_                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                                                                                                                                                                                                                                                                                      |         |                                              |
| `affinity` [_AffinityConfig_](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                                                                                                   |         |                                              |
| `nodeSelector` _object (keys:string, values:string)_                                                                          | NodeSelector to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                                                                                               |         |                                              |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                                                                                                |         |                                              |
| `volumes` [_Volume_](api-reference.md#volume) _array_                                                                         | Volumes to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                                                                                                    |         |                                              |
| `priorityClassName` _string_                                                                                                  | PriorityClassName to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                                                                                          |         |                                              |
| `topologySpreadConstraints` [_TopologySpreadConstraint_](api-reference.md#topologyspreadconstraint) _array_                   | TopologySpreadConstraints to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                                                                                  |         |                                              |
| `suspend` _boolean_                                                                                                           | <p>Suspend indicates whether the current resource should be suspended or not.<br>This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities.</p>                                                                                                                                                                                                               | false   |                                              |
| `image` _string_                                                                                                              | <p>Image name to be used by the MariaDB instances. The supported format is <code>&#x3C;image>:&#x3C;tag></code>.<br>Only MariaDB official images are supported.</p>                                                                                                                                                                                                                                                                                               |         |                                              |
| `imagePullPolicy` [_PullPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#pullpolicy-v1-core)     | ImagePullPolicy is the image pull policy. One of `Always`, `Never` or `IfNotPresent`. If not defined, it defaults to `IfNotPresent`.                                                                                                                                                                                                                                                                                                                              |         | <p>Enum: [Always Never IfNotPresent]<br></p> |
| `inheritMetadata` [_Metadata_](api-reference.md#metadata)                                                                     | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                                                                                                                                                                                                                                                                       |         |                                              |
| `rootPasswordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref)                                  | RootPasswordSecretKeyRef is a reference to a Secret key containing the root password.                                                                                                                                                                                                                                                                                                                                                                             |         |                                              |
| `rootEmptyPassword` _boolean_                                                                                                 | RootEmptyPassword indicates if the root password should be empty. Don't use this feature in production, it is only intended for development and test environments.                                                                                                                                                                                                                                                                                                |         |                                              |
| `database` _string_                                                                                                           | Database is the name of the initial Database.                                                                                                                                                                                                                                                                                                                                                                                                                     |         |                                              |
| `username` _string_                                                                                                           | <p>Username is the initial username to be created by the operator once MariaDB is ready.<br>The initial User will have ALL PRIVILEGES in the initial Database.</p>                                                                                                                                                                                                                                                                                                |         |                                              |
| `passwordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref)                                      | <p>PasswordSecretKeyRef is a reference to a Secret that contains the password to be used by the initial User.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.</p>                                                                                                                                                                                               |         |                                              |
| `passwordHashSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector)                                          | <p>PasswordHashSecretKeyRef is a reference to the password hash to be used by the initial User.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password hash.<br>It requires the 'strict-password-validation=false' option to be set. See: https://mariadb.com/docs/server/server-management/variables-and-modes/server-system-variables#strict_password_validation.</p> |         |                                              |
| `passwordPlugin` [_PasswordPlugin_](api-reference.md#passwordplugin)                                                          | <p>PasswordPlugin is a reference to the password plugin and arguments to be used by the initial User.<br>It requires the 'strict-password-validation=false' option to be set. See: https://mariadb.com/docs/server/server-management/variables-and-modes/server-system-variables#strict_password_validation.</p>                                                                                                                                                  |         |                                              |
| `cleanupPolicy` [_CleanupPolicy_](api-reference.md#cleanuppolicy)                                                             | CleanupPolicy defines the behavior for cleaning up the initial User, Database, and Grant created by the operator.                                                                                                                                                                                                                                                                                                                                                 |         | <p>Enum: [Skip Delete]<br></p>               |
| `myCnf` _string_                                                                                                              | <p>MyCnf allows to specify the my.cnf file mounted by Mariadb.<br>Updating this field will trigger an update to the Mariadb resource.</p>                                                                                                                                                                                                                                                                                                                         |         |                                              |
| `myCnfConfigMapKeyRef` [_ConfigMapKeySelector_](api-reference.md#configmapkeyselector)                                        | <p>MyCnfConfigMapKeyRef is a reference to the my.cnf config file provided via a ConfigMap.<br>If not provided, it will be defaulted with a reference to a ConfigMap containing the MyCnf field.<br>If the referred ConfigMap is labeled with "enterprise.mariadb.com/watch", an update to the Mariadb resource will be triggered when the ConfigMap is updated.</p>                                                                                               |         |                                              |
| `timeZone` _string_                                                                                                           | TimeZone sets the default timezone. If not provided, it defaults to SYSTEM and the timezone data is not loaded.                                                                                                                                                                                                                                                                                                                                                   |         |                                              |
| `bootstrapFrom` [_BootstrapFrom_](api-reference.md#bootstrapfrom)                                                             | BootstrapFrom defines a source to bootstrap from.                                                                                                                                                                                                                                                                                                                                                                                                                 |         |                                              |
| `storage` [_Storage_](api-reference.md#storage)                                                                               | Storage defines the storage options to be used for provisioning the PVCs mounted by MariaDB.                                                                                                                                                                                                                                                                                                                                                                      |         |                                              |
| `metrics` [_MariadbMetrics_](api-reference.md#mariadbmetrics)                                                                 | Metrics configures metrics and how to scrape them.                                                                                                                                                                                                                                                                                                                                                                                                                |         |                                              |
| `tls` [_TLS_](api-reference.md#tls)                                                                                           | TLS defines the PKI to be used with MariaDB.                                                                                                                                                                                                                                                                                                                                                                                                                      |         |                                              |
| `replication` [_Replication_](api-reference.md#replication)                                                                   | Replication configures high availability via replication. This feature is still in alpha, use Galera if you are looking for a more production-ready HA.                                                                                                                                                                                                                                                                                                           |         |                                              |
| `galera` [_Galera_](api-reference.md#galera)                                                                                  | Galera configures high availability via Galera.                                                                                                                                                                                                                                                                                                                                                                                                                   |         |                                              |
| `maxScaleRef` [_ObjectReference_](api-reference.md#objectreference)                                                           | <p>MaxScaleRef is a reference to a MaxScale resource to be used with the current MariaDB.<br>Providing this field implies delegating high availability tasks such as primary failover to MaxScale.</p>                                                                                                                                                                                                                                                            |         |                                              |
| `maxScale` [_MariaDBMaxScaleSpec_](api-reference.md#mariadbmaxscalespec)                                                      | <p>MaxScale is the MaxScale specification that defines the MaxScale resource to be used with the current MariaDB.<br>When enabling this field, MaxScaleRef is automatically set.</p>                                                                                                                                                                                                                                                                              |         |                                              |
| `replicas` _integer_                                                                                                          | Replicas indicates the number of desired instances.                                                                                                                                                                                                                                                                                                                                                                                                               | 1       |                                              |
| `replicasAllowEvenNumber` _boolean_                                                                                           | disables the validation check for an odd number of replicas.                                                                                                                                                                                                                                                                                                                                                                                                      | false   |                                              |
| `port` _integer_                                                                                                              | Port where the instances will be listening for connections.                                                                                                                                                                                                                                                                                                                                                                                                       | 3306    |                                              |
| `servicePorts` [_ServicePort_](api-reference.md#serviceport) _array_                                                          | ServicePorts is the list of additional named ports to be added to the Services created by the operator.                                                                                                                                                                                                                                                                                                                                                           |         |                                              |
| `podDisruptionBudget` [_PodDisruptionBudget_](api-reference.md#poddisruptionbudget)                                           | PodDisruptionBudget defines the budget for replica availability.                                                                                                                                                                                                                                                                                                                                                                                                  |         |                                              |
| `updateStrategy` [_UpdateStrategy_](api-reference.md#updatestrategy)                                                          | UpdateStrategy defines how a MariaDB resource is updated.                                                                                                                                                                                                                                                                                                                                                                                                         |         |                                              |
| `service` [_ServiceTemplate_](api-reference.md#servicetemplate)                                                               | <p>Service defines a template to configure the general Service object.<br>The network traffic of this Service will be routed to all Pods.</p>                                                                                                                                                                                                                                                                                                                     |         |                                              |
| `connection` [_ConnectionTemplate_](api-reference.md#connectiontemplate)                                                      | <p>Connection defines a template to configure the general Connection object.<br>This Connection provides the initial User access to the initial Database.<br>It will make use of the Service to route network traffic to all Pods.</p>                                                                                                                                                                                                                            |         |                                              |
| `primaryService` [_ServiceTemplate_](api-reference.md#servicetemplate)                                                        | <p>PrimaryService defines a template to configure the primary Service object.<br>The network traffic of this Service will be routed to the primary Pod.</p>                                                                                                                                                                                                                                                                                                       |         |                                              |
| `primaryConnection` [_ConnectionTemplate_](api-reference.md#connectiontemplate)                                               | <p>PrimaryConnection defines a template to configure the primary Connection object.<br>This Connection provides the initial User access to the initial Database.<br>It will make use of the PrimaryService to route network traffic to the primary Pod.</p>                                                                                                                                                                                                       |         |                                              |
| `secondaryService` [_ServiceTemplate_](api-reference.md#servicetemplate)                                                      | <p>SecondaryService defines a template to configure the secondary Service object.<br>The network traffic of this Service will be routed to the secondary Pods.</p>                                                                                                                                                                                                                                                                                                |         |                                              |
| `secondaryConnection` [_ConnectionTemplate_](api-reference.md#connectiontemplate)                                             | <p>SecondaryConnection defines a template to configure the secondary Connection object.<br>This Connection provides the initial User access to the initial Database.<br>It will make use of the SecondaryService to route network traffic to the secondary Pods.</p>                                                                                                                                                                                              |         |                                              |

#### MariadbMetrics

MariadbMetrics defines the metrics for a MariaDB.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                    | Description                                                                                                                                                                                                                                               | Default | Validation |
| ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `enabled` _boolean_                                                                      | Enabled is a flag to enable Metrics                                                                                                                                                                                                                       |         |            |
| `exporter` [_Exporter_](api-reference.md#exporter)                                       | Exporter defines the metrics exporter container.                                                                                                                                                                                                          |         |            |
| `serviceMonitor` [_ServiceMonitor_](api-reference.md#servicemonitor)                     | ServiceMonitor defines the ServiceMonior object.                                                                                                                                                                                                          |         |            |
| `username` _string_                                                                      | Username is the username of the monitoring user used by the exporter.                                                                                                                                                                                     |         |            |
| `passwordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref) | <p>PasswordSecretKeyRef is a reference to the password of the monitoring user used by the exporter.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.</p> |         |            |

#### MaxScale

MaxScale is the Schema for the maxscales API. It is used to define MaxScale clusters.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `MaxScale`                                                      |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_MaxScaleSpec_](api-reference.md#maxscalespec)                                                             |                                                                 |         |            |

#### MaxScaleAdmin

MaxScaleAdmin configures the admin REST API and GUI.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                  | Description                                                   | Default | Validation |
| ---------------------- | ------------------------------------------------------------- | ------- | ---------- |
| `port` _integer_       | Port where the admin REST API and GUI will be exposed.        |         |            |
| `guiEnabled` _boolean_ | GuiEnabled indicates whether the admin GUI should be enabled. |         |            |

#### MaxScaleAuth

MaxScaleAuth defines the credentials required for MaxScale to connect to MariaDB.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                           | Description                                                                                                                                                                                                                                                                                                          | Default | Validation |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `generate` _boolean_                                                                            | <p>Generate defies whether the operator should generate users and grants for MaxScale to work.<br>It only supports MariaDBs specified via spec.mariaDbRef.</p>                                                                                                                                                       |         |            |
| `adminUsername` _string_                                                                        | AdminUsername is an admin username to call the admin REST API. It is defaulted if not provided.                                                                                                                                                                                                                      |         |            |
| `adminPasswordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref)   | AdminPasswordSecretKeyRef is Secret key reference to the admin password to call the admin REST API. It is defaulted if not provided.                                                                                                                                                                                 |         |            |
| `deleteDefaultAdmin` _boolean_                                                                  | DeleteDefaultAdmin determines whether the default admin user should be deleted after the initial configuration. If not provided, it defaults to true.                                                                                                                                                                |         |            |
| `metricsUsername` _string_                                                                      | MetricsUsername is an metrics username to call the REST API. It is defaulted if metrics are enabled.                                                                                                                                                                                                                 |         |            |
| `metricsPasswordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref) | MetricsPasswordSecretKeyRef is Secret key reference to the metrics password to call the admib REST API. It is defaulted if metrics are enabled.                                                                                                                                                                      |         |            |
| `clientUsername` _string_                                                                       | ClientUsername is the user to connect to MaxScale. It is defaulted if not provided.                                                                                                                                                                                                                                  |         |            |
| `clientPasswordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref)  | <p>ClientPasswordSecretKeyRef is Secret key reference to the password to connect to MaxScale. It is defaulted if not provided.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.</p>                                 |         |            |
| `clientMaxConnections` _integer_                                                                | <p>ClientMaxConnections defines the maximum number of connections that the client can establish.<br>If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.<br>It defaults to 30 times the number of MaxScale replicas.</p>                                          |         |            |
| `serverUsername` _string_                                                                       | ServerUsername is the user used by MaxScale to connect to MariaDB server. It is defaulted if not provided.                                                                                                                                                                                                           |         |            |
| `serverPasswordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref)  | <p>ServerPasswordSecretKeyRef is Secret key reference to the password used by MaxScale to connect to MariaDB server. It is defaulted if not provided.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.</p>          |         |            |
| `serverMaxConnections` _integer_                                                                | <p>ServerMaxConnections defines the maximum number of connections that the server can establish.<br>If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.<br>It defaults to 30 times the number of MaxScale replicas.</p>                                          |         |            |
| `monitorUsername` _string_                                                                      | MonitorUsername is the user used by MaxScale monitor to connect to MariaDB server. It is defaulted if not provided.                                                                                                                                                                                                  |         |            |
| `monitorPasswordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref) | <p>MonitorPasswordSecretKeyRef is Secret key reference to the password used by MaxScale monitor to connect to MariaDB server. It is defaulted if not provided.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.</p> |         |            |
| `monitorMaxConnections` _integer_                                                               | <p>MonitorMaxConnections defines the maximum number of connections that the monitor can establish.<br>If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.<br>It defaults to 30 times the number of MaxScale replicas.</p>                                        |         |            |
| `syncUsername` _string_                                                                         | MonitoSyncUsernamerUsername is the user used by MaxScale config sync to connect to MariaDB server. It is defaulted when HA is enabled.                                                                                                                                                                               |         |            |
| `syncPasswordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref)    | <p>SyncPasswordSecretKeyRef is Secret key reference to the password used by MaxScale config to connect to MariaDB server. It is defaulted when HA is enabled.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.</p>  |         |            |
| `syncMaxConnections` _integer_                                                                  | <p>SyncMaxConnections defines the maximum number of connections that the sync can establish.<br>If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.<br>It defaults to 30 times the number of MaxScale replicas.</p>                                              |         |            |

#### MaxScaleConfig

MaxScaleConfig defines the MaxScale configuration.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                               | Description                                                                                                                                                                                                                                                                                  | Default | Validation |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `params` _object (keys:string, values:string)_                                      | <p>Params is a key value pair of parameters to be used in the MaxScale static configuration file.<br>Any parameter supported by MaxScale may be specified here. See reference:<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#global-settings.</p> |         |            |
| `volumeClaimTemplate` [_VolumeClaimTemplate_](api-reference.md#volumeclaimtemplate) | VolumeClaimTemplate provides a template to define the PVCs for storing MaxScale runtime configuration files. It is defaulted if not provided.                                                                                                                                                |         |            |
| `sync` [_MaxScaleConfigSync_](api-reference.md#maxscaleconfigsync)                  | Sync defines how to replicate configuration across MaxScale replicas. It is defaulted when HA is enabled.                                                                                                                                                                                    |         |            |

#### MaxScaleConfigSync

MaxScaleConfigSync defines how the config changes are replicated across replicas.

_Appears in:_

* [MaxScaleConfig](api-reference.md#maxscaleconfig)

| Field                                                                                                          | Description                                                                                                                                                                              | Default | Validation |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `database` _string_                                                                                            | Database is the MariaDB logical database where the 'maxscale\_config' table will be created in order to persist and synchronize config changes. If not provided, it defaults to 'mysql'. |         |            |
| `interval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | Interval defines the config synchronization interval. It is defaulted if not provided.                                                                                                   |         |            |
| `timeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)  | Interval defines the config synchronization timeout. It is defaulted if not provided.                                                                                                    |         |            |

#### MaxScaleListener

MaxScaleListener defines how the MaxScale server will listen for connections.

_Appears in:_

* [MaxScaleService](api-reference.md#maxscaleservice)

| Field                                          | Description                                                                                                                                                                                                                                         | Default | Validation              |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------- |
| `suspend` _boolean_                            | <p>Suspend indicates whether the current resource should be suspended or not.<br>This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities.</p> | false   |                         |
| `name` _string_                                | Name is the identifier of the listener. It is defaulted if not provided                                                                                                                                                                             |         |                         |
| `port` _integer_                               | Port is the network port where the MaxScale server will listen.                                                                                                                                                                                     |         | <p>Required: {}<br></p> |
| `protocol` _string_                            | Protocol is the MaxScale protocol to use when communicating with the client. If not provided, it defaults to MariaDBProtocol.                                                                                                                       |         |                         |
| `params` _object (keys:string, values:string)_ | <p>Params defines extra parameters to pass to the listener.<br>Any parameter supported by MaxScale may be specified here. See reference:<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#listener_1.</p>   |         |                         |

#### MaxScaleMetrics

MaxScaleMetrics defines the metrics for a Maxscale.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                | Description                                      | Default | Validation |
| -------------------------------------------------------------------- | ------------------------------------------------ | ------- | ---------- |
| `enabled` _boolean_                                                  | Enabled is a flag to enable Metrics              |         |            |
| `exporter` [_Exporter_](api-reference.md#exporter)                   | Exporter defines the metrics exporter container. |         |            |
| `serviceMonitor` [_ServiceMonitor_](api-reference.md#servicemonitor) | ServiceMonitor defines the ServiceMonior object. |         |            |

#### MaxScaleMonitor

MaxScaleMonitor monitors MariaDB server instances

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Default | Validation                                             |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------ |
| `suspend` _boolean_                                                                                            | <p>Suspend indicates whether the current resource should be suspended or not.<br>This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities.</p>                                                                                                                                                                                                                    | false   |                                                        |
| `name` _string_                                                                                                | Name is the identifier of the monitor. It is defaulted if not provided.                                                                                                                                                                                                                                                                                                                                                                                                |         |                                                        |
| `module` [_MonitorModule_](api-reference.md#monitormodule)                                                     | Module is the module to use to monitor MariaDB servers. It is mandatory when no MariaDB reference is provided.                                                                                                                                                                                                                                                                                                                                                         |         |                                                        |
| `interval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | Interval used to monitor MariaDB servers. It is defaulted if not provided.                                                                                                                                                                                                                                                                                                                                                                                             |         |                                                        |
| `cooperativeMonitoring` [_CooperativeMonitoring_](api-reference.md#cooperativemonitoring)                      | CooperativeMonitoring enables coordination between multiple MaxScale instances running monitors. It is defaulted when HA is enabled.                                                                                                                                                                                                                                                                                                                                   |         | <p>Enum: [majority_of_all majority_of_running]<br></p> |
| `params` _object (keys:string, values:string)_                                                                 | <p>Params defines extra parameters to pass to the monitor.<br>Any parameter supported by MaxScale may be specified here. See reference:<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-common-monitor-parameters/.<br>Monitor specific parameter are also supported:<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-galera-monitor/#galera-monitor-optional-parameters.<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-monitor/#configuration.</p> |         |                                                        |

#### MaxScalePodTemplate

MaxScalePodTemplate defines a template for MaxScale Pods.

_Appears in:_

* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                                                         | Description                                                                        | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------- | ---------- |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                    |         |            |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.         |         |            |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings. |         |            |
| `serviceAccountName` _string_                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.       |         |            |
| `affinity` [_AffinityConfig_](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                    |         |            |
| `nodeSelector` _object (keys:string, values:string)_                                                                          | NodeSelector to be used in the Pod.                                                |         |            |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                                                 |         |            |
| `priorityClassName` _string_                                                                                                  | PriorityClassName to be used in the Pod.                                           |         |            |
| `topologySpreadConstraints` [_TopologySpreadConstraint_](api-reference.md#topologyspreadconstraint) _array_                   | TopologySpreadConstraints to be used in the Pod.                                   |         |            |

#### MaxScaleServer

MaxScaleServer defines a MariaDB server to forward traffic to.

_Appears in:_

* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                          | Description                                                                                                                                                                                                                                   | Default | Validation              |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------- |
| `name` _string_                                | Name is the identifier of the MariaDB server.                                                                                                                                                                                                 |         | <p>Required: {}<br></p> |
| `address` _string_                             | Address is the network address of the MariaDB server.                                                                                                                                                                                         |         | <p>Required: {}<br></p> |
| `port` _integer_                               | Port is the network port of the MariaDB server. If not provided, it defaults to 3306.                                                                                                                                                         |         |                         |
| `protocol` _string_                            | Protocol is the MaxScale protocol to use when communicating with this MariaDB server. If not provided, it defaults to MariaDBBackend.                                                                                                         |         |                         |
| `maintenance` _boolean_                        | Maintenance indicates whether the server is in maintenance mode.                                                                                                                                                                              |         |                         |
| `params` _object (keys:string, values:string)_ | <p>Params defines extra parameters to pass to the server.<br>Any parameter supported by MaxScale may be specified here. See reference:<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#server_1.</p> |         |                         |

#### MaxScaleService

Services define how the traffic is forwarded to the MariaDB servers.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Default | Validation                                                      |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | --------------------------------------------------------------- |
| `suspend` _boolean_                                                | <p>Suspend indicates whether the current resource should be suspended or not.<br>This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities.</p>                                                                                                                                                                                                                 | false   |                                                                 |
| `name` _string_                                                    | Name is the identifier of the MaxScale service.                                                                                                                                                                                                                                                                                                                                                                                                                     |         | <p>Required: {}<br></p>                                         |
| `router` [_ServiceRouter_](api-reference.md#servicerouter)         | Router is the type of router to use.                                                                                                                                                                                                                                                                                                                                                                                                                                |         | <p>Enum: [readwritesplit readconnroute]<br>Required: {}<br></p> |
| `listener` [_MaxScaleListener_](api-reference.md#maxscalelistener) | MaxScaleListener defines how the MaxScale server will listen for connections.                                                                                                                                                                                                                                                                                                                                                                                       |         | <p>Required: {}<br></p>                                         |
| `params` _object (keys:string, values:string)_                     | <p>Params defines extra parameters to pass to the service.<br>Any parameter supported by MaxScale may be specified here. See reference:<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#service_1.<br>Router specific parameter are also supported:<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-readwritesplit/#configuration.<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-readconnroute/#configuration.</p> |         |                                                                 |

#### MaxScaleSpec

MaxScaleSpec defines the desired state of MaxScale.

_Appears in:_

* [MaxScale](api-reference.md#maxscale)

| Field                                                                                                                                                  | Description                                                                                                                                                                                                                                                          | Default | Validation                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------- |
| `command` _string array_                                                                                                                               | Command to be used in the Container.                                                                                                                                                                                                                                 |         |                                              |
| `args` _string array_                                                                                                                                  | Args to be used in the Container.                                                                                                                                                                                                                                    |         |                                              |
| `env` [_EnvVar_](api-reference.md#envvar) _array_                                                                                                      | Env represents the environment variables to be injected in a container.                                                                                                                                                                                              |         |                                              |
| `envFrom` [_EnvFromSource_](api-reference.md#envfromsource) _array_                                                                                    | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container.                                                                                                                                              |         |                                              |
| `volumeMounts` [_VolumeMount_](api-reference.md#volumemount) _array_                                                                                   | VolumeMounts to be used in the Container.                                                                                                                                                                                                                            |         |                                              |
| `livenessProbe` [_Probe_](api-reference.md#probe)                                                                                                      | LivenessProbe to be used in the Container.                                                                                                                                                                                                                           |         |                                              |
| `readinessProbe` [_Probe_](api-reference.md#probe)                                                                                                     | ReadinessProbe to be used in the Container.                                                                                                                                                                                                                          |         |                                              |
| `startupProbe` [_Probe_](api-reference.md#probe)                                                                                                       | StartupProbe to be used in the Container.                                                                                                                                                                                                                            |         |                                              |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                                                            | Resources describes the compute resource requirements.                                                                                                                                                                                                               |         |                                              |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)                                                                                | SecurityContext holds security configuration that will be applied to a container.                                                                                                                                                                                    |         |                                              |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                                                  | PodMetadata defines extra metadata for the Pod.                                                                                                                                                                                                                      |         |                                              |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                                             | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                                                                           |         |                                              |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                                                       | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                                                                                   |         |                                              |
| `serviceAccountName` _string_                                                                                                                          | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                                                                                         |         |                                              |
| `affinity` [_AffinityConfig_](api-reference.md#affinityconfig)                                                                                         | Affinity to be used in the Pod.                                                                                                                                                                                                                                      |         |                                              |
| `nodeSelector` _object (keys:string, values:string)_                                                                                                   | NodeSelector to be used in the Pod.                                                                                                                                                                                                                                  |         |                                              |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_                          | Tolerations to be used in the Pod.                                                                                                                                                                                                                                   |         |                                              |
| `priorityClassName` _string_                                                                                                                           | PriorityClassName to be used in the Pod.                                                                                                                                                                                                                             |         |                                              |
| `topologySpreadConstraints` [_TopologySpreadConstraint_](api-reference.md#topologyspreadconstraint) _array_                                            | TopologySpreadConstraints to be used in the Pod.                                                                                                                                                                                                                     |         |                                              |
| `suspend` _boolean_                                                                                                                                    | <p>Suspend indicates whether the current resource should be suspended or not.<br>This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities.</p>                  | false   |                                              |
| `mariaDbRef` [_MariaDBRef_](api-reference.md#mariadbref)                                                                                               | MariaDBRef is a reference to the MariaDB that MaxScale points to. It is used to initialize the servers field.                                                                                                                                                        |         |                                              |
| `primaryServer` _string_                                                                                                                               | <p>PrimaryServer specifies the desired primary server. Setting this field triggers a switchover operation in MaxScale to the desired server.<br>This option is only valid when using monitors that support switchover, currently limited to the MariaDB monitor.</p> |         |                                              |
| `servers` [_MaxScaleServer_](api-reference.md#maxscaleserver) _array_                                                                                  | Servers are the MariaDB servers to forward traffic to. It is required if 'spec.mariaDbRef' is not provided.                                                                                                                                                          |         |                                              |
| `image` _string_                                                                                                                                       | <p>Image name to be used by the MaxScale instances. The supported format is <code>&#x3C;image>:&#x3C;tag></code>.<br>Only MaxScale official images are supported.</p>                                                                                                |         |                                              |
| `imagePullPolicy` [_PullPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#pullpolicy-v1-core)                              | ImagePullPolicy is the image pull policy. One of `Always`, `Never` or `IfNotPresent`. If not defined, it defaults to `IfNotPresent`.                                                                                                                                 |         | <p>Enum: [Always Never IfNotPresent]<br></p> |
| `inheritMetadata` [_Metadata_](api-reference.md#metadata)                                                                                              | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                                                                          |         |                                              |
| `services` [_MaxScaleService_](api-reference.md#maxscaleservice) _array_                                                                               | Services define how the traffic is forwarded to the MariaDB servers. It is defaulted if not provided.                                                                                                                                                                |         |                                              |
| `monitor` [_MaxScaleMonitor_](api-reference.md#maxscalemonitor)                                                                                        | Monitor monitors MariaDB server instances. It is required if 'spec.mariaDbRef' is not provided.                                                                                                                                                                      |         |                                              |
| `admin` [_MaxScaleAdmin_](api-reference.md#maxscaleadmin)                                                                                              | Admin configures the admin REST API and GUI.                                                                                                                                                                                                                         |         |                                              |
| `config` [_MaxScaleConfig_](api-reference.md#maxscaleconfig)                                                                                           | Config defines the MaxScale configuration.                                                                                                                                                                                                                           |         |                                              |
| `auth` [_MaxScaleAuth_](api-reference.md#maxscaleauth)                                                                                                 | Auth defines the credentials required for MaxScale to connect to MariaDB.                                                                                                                                                                                            |         |                                              |
| `metrics` [_MaxScaleMetrics_](api-reference.md#maxscalemetrics)                                                                                        | Metrics configures metrics and how to scrape them.                                                                                                                                                                                                                   |         |                                              |
| `tls` [_MaxScaleTLS_](api-reference.md#maxscaletls)                                                                                                    | TLS defines the PKI to be used with MaxScale.                                                                                                                                                                                                                        |         |                                              |
| `connection` [_ConnectionTemplate_](api-reference.md#connectiontemplate)                                                                               | Connection provides a template to define the Connection for MaxScale.                                                                                                                                                                                                |         |                                              |
| `replicas` _integer_                                                                                                                                   | Replicas indicates the number of desired instances.                                                                                                                                                                                                                  | 1       |                                              |
| `podDisruptionBudget` [_PodDisruptionBudget_](api-reference.md#poddisruptionbudget)                                                                    | PodDisruptionBudget defines the budget for replica availability.                                                                                                                                                                                                     |         |                                              |
| `updateStrategy` [_StatefulSetUpdateStrategy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#statefulsetupdatestrategy-v1-apps) | UpdateStrategy defines the update strategy for the StatefulSet object.                                                                                                                                                                                               |         |                                              |
| `kubernetesService` [_ServiceTemplate_](api-reference.md#servicetemplate)                                                                              | KubernetesService defines a template for a Kubernetes Service object to connect to MaxScale.                                                                                                                                                                         |         |                                              |
| `guiKubernetesService` [_ServiceTemplate_](api-reference.md#servicetemplate)                                                                           | GuiKubernetesService defines a template for a Kubernetes Service object to connect to MaxScale's GUI.                                                                                                                                                                |         |                                              |
| `requeueInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)                                  | RequeueInterval is used to perform requeue reconciliations. If not defined, it defaults to 10s.                                                                                                                                                                      |         |                                              |

#### MaxScaleTLS

TLS defines the PKI to be used with MaxScale.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Default | Validation                                               |
| --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------- |
| `enabled` _boolean_                                                                     | <p>Enabled indicates whether TLS is enabled, determining if certificates should be issued and mounted to the MaxScale instance.<br>It is enabled by default when the referred MariaDB instance (via mariaDbRef) has TLS enabled and enforced.</p>                                                                                                                                                                                                                                                                                                                                                                       |         |                                                          |
| `adminVersions` _string array_                                                          | <p>Versions specifies the supported TLS versions in the MaxScale REST API.<br>By default, the MaxScale's default supported versions are used. See: https://mariadb.com/kb/en/mariadb-maxscale-25-mariadb-maxscale-configuration-guide/#admin_ssl_version</p>                                                                                                                                                                                                                                                                                                                                                            |         | <p>items:Enum: [TLSv10 TLSv11 TLSv12 TLSv13 MAX]<br></p> |
| `serverVersions` _string array_                                                         | <p>ServerVersions specifies the supported TLS versions in both the servers and listeners managed by this MaxScale instance.<br>By default, the MaxScale's default supported versions are used. See: https://mariadb.com/kb/en/mariadb-maxscale-25-mariadb-maxscale-configuration-guide/#ssl_version.</p>                                                                                                                                                                                                                                                                                                                |         | <p>items:Enum: [TLSv10 TLSv11 TLSv12 TLSv13 MAX]<br></p> |
| `adminCASecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)      | <p>AdminCASecretRef is a reference to a Secret containing the admin certificate authority keypair. It is used to establish trust and issue certificates for the MaxScale's administrative REST API and GUI.<br>One of:<br>- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.<br>- Secret containing only the 'ca.crt' in order to establish trust. In this case, either adminCertSecretRef or adminCertIssuerRef fields must be provided.<br>If not provided, a self-signed CA will be provisioned to issue the server certificate.</p> |         |                                                          |
| `adminCertSecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)    | AdminCertSecretRef is a reference to a TLS Secret used by the MaxScale's administrative REST API and GUI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |         |                                                          |
| `adminCertIssuerRef` [_ObjectReference_](api-reference.md#objectreference)              | <p>AdminCertIssuerRef is a reference to a cert-manager issuer object used to issue the MaxScale's administrative REST API and GUI certificate. cert-manager must be installed previously in the cluster.<br>It is mutually exclusive with adminCertSecretRef.<br>By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via adminCASecretRef.</p>                                                                                                                                                                                   |         |                                                          |
| `adminCertConfig` [_TLSConfig_](api-reference.md#tlsconfig)                             | <p>AdminCertConfig allows configuring the admin certificates, either issued by the operator or cert-manager.<br>If not set, the default settings will be used.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                      |         |                                                          |
| `listenerCASecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)   | <p>ListenerCASecretRef is a reference to a Secret containing the listener certificate authority keypair. It is used to establish trust and issue certificates for the MaxScale's listeners.<br>One of:<br>- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.<br>- Secret containing only the 'ca.crt' in order to establish trust. In this case, either listenerCertSecretRef or listenerCertIssuerRef fields must be provided.<br>If not provided, a self-signed CA will be provisioned to issue the listener certificate.</p>         |         |                                                          |
| `listenerCertSecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference) | ListenerCertSecretRef is a reference to a TLS Secret used by the MaxScale's listeners.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |         |                                                          |
| `listenerCertIssuerRef` [_ObjectReference_](api-reference.md#objectreference)           | <p>ListenerCertIssuerRef is a reference to a cert-manager issuer object used to issue the MaxScale's listeners certificate. cert-manager must be installed previously in the cluster.<br>It is mutually exclusive with listenerCertSecretRef.<br>By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via listenerCASecretRef.</p>                                                                                                                                                                                                |         |                                                          |
| `listenerCertConfig` [_TLSConfig_](api-reference.md#tlsconfig)                          | <p>ListenerCertConfig allows configuring the listener certificates, either issued by the operator or cert-manager.<br>If not set, the default settings will be used.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                |         |                                                          |
| `serverCASecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)     | <p>ServerCASecretRef is a reference to a Secret containing the MariaDB server CA certificates. It is used to establish trust with MariaDB servers.<br>The Secret should contain a 'ca.crt' key in order to establish trust.<br>If not provided, and the reference to a MariaDB resource is set (mariaDbRef), it will be defaulted to the referred MariaDB CA bundle.</p>                                                                                                                                                                                                                                                |         |                                                          |
| `serverCertSecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)   | <p>ServerCertSecretRef is a reference to a TLS Secret used by MaxScale to connect to the MariaDB servers.<br>If not provided, and the reference to a MariaDB resource is set (mariaDbRef), it will be defaulted to the referred MariaDB client certificate (clientCertSecretRef).</p>                                                                                                                                                                                                                                                                                                                                   |         |                                                          |
| `verifyPeerCertificate` _boolean_                                                       | <p>VerifyPeerCertificate specifies whether the peer certificate's signature should be validated against the CA.<br>It is disabled by default.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |         |                                                          |
| `verifyPeerHost` _boolean_                                                              | <p>VerifyPeerHost specifies whether the peer certificate's SANs should match the peer host.<br>It is disabled by default.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |         |                                                          |
| `replicationSSLEnabled` _boolean_                                                       | <p>ReplicationSSLEnabled specifies whether the replication SSL is enabled. If enabled, the SSL options will be added to the server configuration.<br>It is enabled by default when the referred MariaDB instance (via mariaDbRef) has replication enabled.<br>If the MariaDB servers are manually provided by the user via the 'servers' field, this must be set by the user as well.</p>                                                                                                                                                                                                                               |         |                                                          |

#### Metadata

Metadata defines the metadata to added to resources.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [Exporter](api-reference.md#exporter)
* [ExternalMariaDBSpec](api-reference.md#externalmariadbspec)
* [GaleraInitJob](api-reference.md#galerainitjob)
* [GaleraRecoveryJob](api-reference.md#galerarecoveryjob)
* [Job](api-reference.md#job)
* [JobPodTemplate](api-reference.md#jobpodtemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScalePodTemplate](api-reference.md#maxscalepodtemplate)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PhysicalBackupPodTemplate](api-reference.md#physicalbackuppodtemplate)
* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)
* [PhysicalBackupVolumeSnapshot](api-reference.md#physicalbackupvolumesnapshot)
* [PodTemplate](api-reference.md#podtemplate)
* [RestoreSpec](api-reference.md#restorespec)
* [SecretTemplate](api-reference.md#secrettemplate)
* [ServiceTemplate](api-reference.md#servicetemplate)
* [SqlJobSpec](api-reference.md#sqljobspec)
* [VolumeClaimTemplate](api-reference.md#volumeclaimtemplate)

| Field                                               | Description                                    | Default | Validation |
| --------------------------------------------------- | ---------------------------------------------- | ------- | ---------- |
| `labels` _object (keys:string, values:string)_      | Labels to be added to children resources.      |         |            |
| `annotations` _object (keys:string, values:string)_ | Annotations to be added to children resources. |         |            |

#### MonitorModule

_Underlying type:_ _string_

MonitorModule defines the type of monitor module

_Appears in:_

* [MaxScaleMonitor](api-reference.md#maxscalemonitor)

| Field        | Description                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| `mariadbmon` | <p>MonitorModuleMariadb is a monitor to be used with MariaDB servers.<br></p> |
| `galeramon`  | <p>MonitorModuleGalera is a monitor to be used with Galera servers.<br></p>   |

#### NFSVolumeSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#nfsvolumesource-v1-core.

_Appears in:_

* [StorageVolumeSource](api-reference.md#storagevolumesource)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field                | Description | Default | Validation |
| -------------------- | ----------- | ------- | ---------- |
| `server` _string_    |             |         |            |
| `path` _string_      |             |         |            |
| `readOnly` _boolean_ |             |         |            |

#### NodeAffinity

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#nodeaffinity-v1-core

_Appears in:_

* [Affinity](api-reference.md#affinity)
* [AffinityConfig](api-reference.md#affinityconfig)

| Field                                                                                                                           | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `requiredDuringSchedulingIgnoredDuringExecution` [_NodeSelector_](api-reference.md#nodeselector)                                |             |         |            |
| `preferredDuringSchedulingIgnoredDuringExecution` [_PreferredSchedulingTerm_](api-reference.md#preferredschedulingterm) _array_ |             |         |            |

#### NodeSelector

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#nodeselector-v1-core

_Appears in:_

* [NodeAffinity](api-reference.md#nodeaffinity)

| Field                                                                               | Description | Default | Validation |
| ----------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `nodeSelectorTerms` [_NodeSelectorTerm_](api-reference.md#nodeselectorterm) _array_ |             |         |            |

#### NodeSelectorRequirement

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#nodeselectorrequirement-v1-core

_Appears in:_

* [NodeSelectorTerm](api-reference.md#nodeselectorterm)

| Field                                                                                                                                  | Description | Default | Validation |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `key` _string_                                                                                                                         |             |         |            |
| `operator` [_NodeSelectorOperator_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#nodeselectoroperator-v1-core) |             |         |            |
| `values` _string array_                                                                                                                |             |         |            |

#### NodeSelectorTerm

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#nodeselectorterm-v1-core

_Appears in:_

* [NodeSelector](api-reference.md#nodeselector)
* [PreferredSchedulingTerm](api-reference.md#preferredschedulingterm)

| Field                                                                                            | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------ | ----------- | ------- | ---------- |
| `matchExpressions` [_NodeSelectorRequirement_](api-reference.md#nodeselectorrequirement) _array_ |             |         |            |
| `matchFields` [_NodeSelectorRequirement_](api-reference.md#nodeselectorrequirement) _array_      |             |         |            |

#### ObjectFieldSelector

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectfieldselector-v1-core.

_Appears in:_

* [EnvVarSource](api-reference.md#envvarsource)

| Field                 | Description | Default | Validation |
| --------------------- | ----------- | ------- | ---------- |
| `apiVersion` _string_ |             |         |            |
| `fieldPath` _string_  |             |         |            |

#### ObjectReference

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectreference-v1-core.

_Appears in:_

* [ConnectionSpec](api-reference.md#connectionspec)
* [MariaDBRef](api-reference.md#mariadbref)
* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                | Description | Default | Validation |
| -------------------- | ----------- | ------- | ---------- |
| `name` _string_      |             |         |            |
| `namespace` _string_ |             |         |            |

#### PasswordPlugin

PasswordPlugin defines the password plugin and its arguments.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)
* [UserSpec](api-reference.md#userspec)

| Field                                                                              | Description                                                                                                                                                                                                                                                                                     | Default | Validation |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `pluginNameSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector) | <p>PluginNameSecretKeyRef is a reference to the authentication plugin to be used by the User.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the authentication plugin.</p>                                |         |            |
| `pluginArgSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector)  | <p>PluginArgSecretKeyRef is a reference to the arguments to be provided to the authentication plugin for the User.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the authentication plugin arguments.</p> |         |            |

#### PersistentVolumeClaimRetentionPolicyType

_Underlying type:_ _string_

PersistentVolumeClaimRetentionPolicyType describes the lifecycle of persistent volume claims. Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#statefulsetpersistentvolumeclaimretentionpolicy-v1-apps.

_Appears in:_

* [StatefulSetPersistentVolumeClaimRetentionPolicy](api-reference.md#statefulsetpersistentvolumeclaimretentionpolicy)

| Field    | Description                                                                                                           |
| -------- | --------------------------------------------------------------------------------------------------------------------- |
| `Delete` | <p>PersistentVolumeClaimRetentionPolicyDelete deletes PVCs when their owning pods or StatefulSet are deleted.<br></p> |
| `Retain` | <p>PersistentVolumeClaimRetentionPolicyRetain retains PVCs when their owning pods or StatefulSet are deleted.<br></p> |

#### PersistentVolumeClaimSpec

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#persistentvolumeclaimspec-v1-core.

_Appears in:_

* [BackupStagingStorage](api-reference.md#backupstagingstorage)
* [BackupStorage](api-reference.md#backupstorage)
* [PhysicalBackupStorage](api-reference.md#physicalbackupstorage)
* [VolumeClaimTemplate](api-reference.md#volumeclaimtemplate)

| Field                                                                                                                                                         | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `accessModes` [_PersistentVolumeAccessMode_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#persistentvolumeaccessmode-v1-core) _array_ |             |         |            |
| `selector` [_LabelSelector_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#labelselector-v1-meta)                                      |             |         |            |
| `resources` [_VolumeResourceRequirements_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#volumeresourcerequirements-v1-core)           |             |         |            |
| `storageClassName` _string_                                                                                                                                   |             |         |            |

#### PersistentVolumeClaimVolumeSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#persistentvolumeclaimvolumesource-v1-core.

_Appears in:_

* [StorageVolumeSource](api-reference.md#storagevolumesource)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field                | Description | Default | Validation |
| -------------------- | ----------- | ------- | ---------- |
| `claimName` _string_ |             |         |            |
| `readOnly` _boolean_ |             |         |            |

#### PhysicalBackup

PhysicalBackup is the Schema for the physicalbackups API. It is used to define physical backup jobs and its storage.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `PhysicalBackup`                                                |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_PhysicalBackupSpec_](api-reference.md#physicalbackupspec)                                                 |                                                                 |         |            |

#### PhysicalBackupPodTemplate

PhysicalBackupPodTemplate defines a template to configure Container objects that run in a PhysicalBackup.

_Appears in:_

* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)

| Field                                                                                                                         | Description                                                                        | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------- | ---------- |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                    |         |            |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.         |         |            |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings. |         |            |
| `serviceAccountName` _string_                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.       |         |            |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                                                 |         |            |
| `priorityClassName` _string_                                                                                                  | PriorityClassName to be used in the Pod.                                           |         |            |

#### PhysicalBackupSchedule

PhysicalBackupSchedule defines when the PhysicalBackup will be taken.

_Appears in:_

* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)

| Field                 | Description                                                                                                 | Default | Validation |
| --------------------- | ----------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `cron` _string_       | Cron is a cron expression that defines the schedule.                                                        |         |            |
| `suspend` _boolean_   | Suspend defines whether the schedule is active or not.                                                      | false   |            |
| `immediate` _boolean_ | Immediate indicates whether the first backup should be taken immediately after creating the PhysicalBackup. |         |            |

#### PhysicalBackupSpec

PhysicalBackupSpec defines the desired state of PhysicalBackup.

_Appears in:_

* [PhysicalBackup](api-reference.md#physicalbackup)

| Field                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                 | Default   | Validation                                                  |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------- |
| `args` _string array_                                                                                                         | Args to be used in the Container.                                                                                                                                                                                                                                                                                                                                                           |           |                                                             |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                                   | Resources describes the compute resource requirements.                                                                                                                                                                                                                                                                                                                                      |           |                                                             |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)                                                       | SecurityContext holds security configuration that will be applied to a container.                                                                                                                                                                                                                                                                                                           |           |                                                             |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                                                                                                                                                                                                                                                                                                                             |           |                                                             |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                                                                                                                                                                                                  |           |                                                             |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                                                                                                                                                                                                          |           |                                                             |
| `serviceAccountName` _string_                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                                                                                                                                                                                                                |           |                                                             |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                          |           |                                                             |
| `priorityClassName` _string_                                                                                                  | PriorityClassName to be used in the Pod.                                                                                                                                                                                                                                                                                                                                                    |           |                                                             |
| `mariaDbRef` [_MariaDBRef_](api-reference.md#mariadbref)                                                                      | MariaDBRef is a reference to a MariaDB object.                                                                                                                                                                                                                                                                                                                                              |           | <p>Required: {}<br></p>                                     |
| `target` [_PhysicalBackupTarget_](api-reference.md#physicalbackuptarget)                                                      | Target defines in which Pod the physical backups will be taken. It defaults to "Replica", meaning that the physical backups will only be taken in ready replicas.                                                                                                                                                                                                                           |           | <p>Enum: [Replica PreferReplica]<br></p>                    |
| `compression` [_CompressAlgorithm_](api-reference.md#compressalgorithm)                                                       | Compression algorithm to be used in the Backup.                                                                                                                                                                                                                                                                                                                                             |           | <p>Enum: [none bzip2 gzip]<br></p>                          |
| `stagingStorage` [_BackupStagingStorage_](api-reference.md#backupstagingstorage)                                              | <p>StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.<br>It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the PhysicalBackup Job is scheduled.<br>The staging area gets cleaned up after each backup is completed, consider this for sizing it appropriately.</p> |           |                                                             |
| `storage` [_PhysicalBackupStorage_](api-reference.md#physicalbackupstorage)                                                   | Storage defines the final storage for backups.                                                                                                                                                                                                                                                                                                                                              |           | <p>Required: {}<br></p>                                     |
| `schedule` [_PhysicalBackupSchedule_](api-reference.md#physicalbackupschedule)                                                | Schedule defines when the PhysicalBackup will be taken.                                                                                                                                                                                                                                                                                                                                     |           |                                                             |
| `maxRetention` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)            | <p>MaxRetention defines the retention policy for backups. Old backups will be cleaned up by the Backup Job.<br>It defaults to 30 days.</p>                                                                                                                                                                                                                                                  |           |                                                             |
| `timeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)                 | <p>Timeout defines the maximum duration of a PhysicalBackup job or snapshot.<br>If this duration is exceeded, the job or snapshot is considered expired and is deleted by the operator.<br>A new job or snapshot will then be created according to the schedule.<br>It defaults to 1 hour.</p>                                                                                              |           |                                                             |
| `podAffinity` _boolean_                                                                                                       | <p>PodAffinity indicates whether the Jobs should run in the same Node as the MariaDB Pods to be able to attach the PVC.<br>It defaults to true.</p>                                                                                                                                                                                                                                         |           |                                                             |
| `backoffLimit` _integer_                                                                                                      | BackoffLimit defines the maximum number of attempts to successfully take a PhysicalBackup.                                                                                                                                                                                                                                                                                                  |           |                                                             |
| `restartPolicy` [_RestartPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#restartpolicy-v1-core) | RestartPolicy to be added to the PhysicalBackup Pod.                                                                                                                                                                                                                                                                                                                                        | OnFailure | <p>Enum: [Always OnFailure Never]<br></p>                   |
| `inheritMetadata` [_Metadata_](api-reference.md#metadata)                                                                     | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                                                                                                                                                                                                 |           |                                                             |
| `successfulJobsHistoryLimit` _integer_                                                                                        | SuccessfulJobsHistoryLimit defines the maximum number of successful Jobs to be displayed. It defaults to 5.                                                                                                                                                                                                                                                                                 |           | <p>Minimum: 0<br></p>                                       |
| `logLevel` _string_                                                                                                           | LogLevel to be used in the PhysicalBackup Job. It defaults to 'info'.                                                                                                                                                                                                                                                                                                                       | info      | <p>Enum: [debug info warn error dpanic panic fatal]<br></p> |

#### PhysicalBackupStorage

PhysicalBackupStorage defines the storage for physical backups.

_Appears in:_

* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)

| Field                                                                                             | Description                                                               | Default | Validation |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------- | ---------- |
| `s3` [_S3_](api-reference.md#s3)                                                                  | S3 defines the configuration to store backups in a S3 compatible storage. |         |            |
| `persistentVolumeClaim` [_PersistentVolumeClaimSpec_](api-reference.md#persistentvolumeclaimspec) | PersistentVolumeClaim is a Kubernetes PVC specification.                  |         |            |
| `volume` [_StorageVolumeSource_](api-reference.md#storagevolumesource)                            | Volume is a Kubernetes volume specification.                              |         |            |
| `volumeSnapshot` [_PhysicalBackupVolumeSnapshot_](api-reference.md#physicalbackupvolumesnapshot)  | VolumeSnapshot is a Kubernetes VolumeSnapshot specification.              |         |            |

#### PhysicalBackupTarget

_Underlying type:_ _string_

PhysicalBackupTarget defines in which Pod the physical backups will be taken.

_Appears in:_

* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)

| Field           | Description                                                                                                                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Replica`       | <p>PhysicalBackupTargetReplica indicates that the physical backup will be taken in a ready replica.<br></p>                                                                                                  |
| `PreferReplica` | <p>PhysicalBackupTargetReplica indicates that the physical backup will preferably be taken in a ready replica.<br>If no ready replicas are available, physical backups will be taken in the primary.<br></p> |

#### PhysicalBackupVolumeSnapshot

PhysicalBackupVolumeSnapshot defines parameters for the VolumeSnapshots used as physical backups.

_Appears in:_

* [PhysicalBackupStorage](api-reference.md#physicalbackupstorage)

| Field                                              | Description                                                                       | Default | Validation              |
| -------------------------------------------------- | --------------------------------------------------------------------------------- | ------- | ----------------------- |
| `metadata` [_Metadata_](api-reference.md#metadata) | Refer to Kubernetes API documentation for fields of `metadata`.                   |         |                         |
| `volumeSnapshotClassName` _string_                 | VolumeSnapshotClassName is the VolumeSnapshot class to be used to take snapshots. |         | <p>Required: {}<br></p> |

#### PodAffinityTerm

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#podaffinityterm-v1-core.

_Appears in:_

* [PodAntiAffinity](api-reference.md#podantiaffinity)
* [WeightedPodAffinityTerm](api-reference.md#weightedpodaffinityterm)

| Field                                                             | Description | Default | Validation |
| ----------------------------------------------------------------- | ----------- | ------- | ---------- |
| `labelSelector` [_LabelSelector_](api-reference.md#labelselector) |             |         |            |
| `topologyKey` _string_                                            |             |         |            |

#### PodAntiAffinity

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#podantiaffinity-v1-core.

_Appears in:_

* [Affinity](api-reference.md#affinity)
* [AffinityConfig](api-reference.md#affinityconfig)

| Field                                                                                                                           | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `requiredDuringSchedulingIgnoredDuringExecution` [_PodAffinityTerm_](api-reference.md#podaffinityterm) _array_                  |             |         |            |
| `preferredDuringSchedulingIgnoredDuringExecution` [_WeightedPodAffinityTerm_](api-reference.md#weightedpodaffinityterm) _array_ |             |         |            |

#### PodDisruptionBudget

PodDisruptionBudget is the Pod availability bundget for a MariaDB

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                                                          | Description                                                    | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | ------- | ---------- |
| `minAvailable` [_IntOrString_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#intorstring-intstr-util)   | MinAvailable defines the number of minimum available Pods.     |         |            |
| `maxUnavailable` [_IntOrString_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#intorstring-intstr-util) | MaxUnavailable defines the number of maximum unavailable Pods. |         |            |

#### PodSecurityContext

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#podsecuritycontext-v1-core

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [Exporter](api-reference.md#exporter)
* [JobPodTemplate](api-reference.md#jobpodtemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScalePodTemplate](api-reference.md#maxscalepodtemplate)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PhysicalBackupPodTemplate](api-reference.md#physicalbackuppodtemplate)
* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)
* [PodTemplate](api-reference.md#podtemplate)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                                                                                                                                 | Description | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `seLinuxOptions` [_SELinuxOptions_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#selinuxoptions-v1-core)                      |             |         |            |
| `runAsUser` _integer_                                                                                                                                 |             |         |            |
| `runAsGroup` _integer_                                                                                                                                |             |         |            |
| `runAsNonRoot` _boolean_                                                                                                                              |             |         |            |
| `supplementalGroups` _integer array_                                                                                                                  |             |         |            |
| `fsGroup` _integer_                                                                                                                                   |             |         |            |
| `fsGroupChangePolicy` [_PodFSGroupChangePolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#podfsgroupchangepolicy-v1-core) |             |         |            |
| `seccompProfile` [_SeccompProfile_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#seccompprofile-v1-core)                      |             |         |            |
| `appArmorProfile` [_AppArmorProfile_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#apparmorprofile-v1-core)                   |             |         |            |

#### PodTemplate

PodTemplate defines a template to configure Container objects.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                                         | Description                                                                        | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------- | ---------- |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                    |         |            |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.         |         |            |
| `initContainers` [_Container_](api-reference.md#container) _array_                                                            | InitContainers to be used in the Pod.                                              |         |            |
| `sidecarContainers` [_Container_](api-reference.md#container) _array_                                                         | SidecarContainers to be used in the Pod.                                           |         |            |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings. |         |            |
| `serviceAccountName` _string_                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.       |         |            |
| `affinity` [_AffinityConfig_](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                    |         |            |
| `nodeSelector` _object (keys:string, values:string)_                                                                          | NodeSelector to be used in the Pod.                                                |         |            |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                                                 |         |            |
| `volumes` [_Volume_](api-reference.md#volume) _array_                                                                         | Volumes to be used in the Pod.                                                     |         |            |
| `priorityClassName` _string_                                                                                                  | PriorityClassName to be used in the Pod.                                           |         |            |
| `topologySpreadConstraints` [_TopologySpreadConstraint_](api-reference.md#topologyspreadconstraint) _array_                   | TopologySpreadConstraints to be used in the Pod.                                   |         |            |

#### PointInTimeRecovery



PointInTimeRecovery is the Schema for the pointintimerecoveries API. It contains binlog archival and point-in-time restoration settings.





| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `enterprise.mariadb.com/v1alpha1` | | |
| `kind` _string_ | `PointInTimeRecovery` | | |
| `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `spec` _[PointInTimeRecoverySpec](#pointintimerecoveryspec)_ |  |  |  |


#### PointInTimeRecoverySpec



PointInTimeRecoverySpec defines the desired state of PointInTimeRecovery. It contains binlog archive and point-in-time restoration settings.



_Appears in:_
- [PointInTimeRecovery](#pointintimerecovery)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `physicalBackupRef` _[LocalObjectReference](#localobjectreference)_ | PhysicalBackupRef is a reference to a PhysicalBackup object that will be used as base backup. |  | Required: \{\} <br /> |
| `storage` _[PointInTimeRecoveryStorage](#pointintimerecoverystorage)_ | PointInTimeRecoveryStorage is the storage where the point in time recovery data will be stored |  | Required: \{\} <br /> |
| `compression` _[CompressAlgorithm](#compressalgorithm)_ | Compression algorithm to be used for compressing the binary logs.<br />This field is immutable, it cannot be updated after creation. |  | Enum: [none bzip2 gzip] <br /> |
| `archiveTimeout` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)_ | ArchiveTimeout defines the maximum duration for the binary log archival.<br />If this duration is exceeded, the sidecar agent will log an error and it will be retried in the next archive cycle.<br />It defaults to 1 hour. | 1h |  |
| `strictMode` _boolean_ | StrictMode controls the behavior when a point-in-time restoration cannot reach the exact target time:<br />When enabled: Returns an error and avoids replaying binary logs if target time is not reached.<br />When disabled (default): Replays available binary logs until the last recoverable time. It logs logs an error if target time is not reached. |  |  |
| `archiveInterval` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)_ | ArchiveInterval defines the time interval at which the binary logs will be archived.<br />It defaults to 10 minutes. | 10m |  |
| `maxParallel` _integer_ | MaxParallel defines the maximum number of parallel workers, both for archiving and restoring the binary logs.<br />It defaults to 1. | 1 | Minimum: 1 <br /> |
| `maxRetention` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)_ | MaxRetention defines the retention policy for binary logs. Binary logs older than this duration will be cleaned up when the archival is completed.<br />It is not set by default, meaning that old binary logs will not be cleaned up.<br />This field is immutable, it cannot be updated after creation. |  |  |


#### PointInTimeRecoveryStorage



PointInTimeRecoveryStorage stores the different storage options for PITR



_Appears in:_
- [PointInTimeRecoverySpec](#pointintimerecoveryspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `s3` _[S3](#s3)_ | S3 is the S3-compatible storage where the binary logs will be kept. |  |  |
| `azureBlob` _[AzureBlob](#azureblob)_ | AzureBlob is the Azure Blob Storage where the binary logs will be kept. |  |  |


#### PreferredSchedulingTerm

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#preferredschedulingterm-v1-core

_Appears in:_

* [NodeAffinity](api-reference.md#nodeaffinity)

| Field                                                                | Description | Default | Validation |
| -------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `weight` _integer_                                                   |             |         |            |
| `preference` [_NodeSelectorTerm_](api-reference.md#nodeselectorterm) |             |         |            |

#### PrimaryGalera

PrimaryGalera is the Galera configuration for the primary node.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field                    | Description                                                                                                                | Default | Validation |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `podIndex` _integer_     | PodIndex is the StatefulSet index of the primary node. The user may change this field to perform a manual switchover.      |         |            |
| `autoFailover` _boolean_ | AutoFailover indicates whether the operator should automatically update PodIndex to perform an automatic primary failover. |         |            |

#### PrimaryReplication

PrimaryReplication is the replication configuration and operation parameters for the primary.

_Appears in:_

* [Replication](api-reference.md#replication)
* [ReplicationSpec](api-reference.md#replicationspec)

| Field                                                                                                                   | Description                                                                                                                                                    | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `podIndex` _integer_                                                                                                    | PodIndex is the StatefulSet index of the primary node. The user may change this field to perform a manual switchover.                                          |         |            |
| `autoFailover` _boolean_                                                                                                | <p>AutoFailover indicates whether the operator should automatically update PodIndex to perform an automatic primary failover.<br>It is enabled by default.</p> |         |            |
| `autoFailoverDelay` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | <p>AutoFailoverDelay indicates the duration before performing an automatic primary failover.<br>By default, no extra delay is added.</p>                       |         |            |

#### Probe

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#probe-v1-core.

_Appears in:_

* [Agent](api-reference.md#agent)
* [ContainerTemplate](api-reference.md#containertemplate)
* [InitContainer](api-reference.md#initcontainer)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                             | Description | Default | Validation |
| ----------------------------------------------------------------- | ----------- | ------- | ---------- |
| `exec` [_ExecAction_](api-reference.md#execaction)                |             |         |            |
| `httpGet` [_HTTPGetAction_](api-reference.md#httpgetaction)       |             |         |            |
| `tcpSocket` [_TCPSocketAction_](api-reference.md#tcpsocketaction) |             |         |            |
| `initialDelaySeconds` _integer_                                   |             |         |            |
| `timeoutSeconds` _integer_                                        |             |         |            |
| `periodSeconds` _integer_                                         |             |         |            |
| `successThreshold` _integer_                                      |             |         |            |
| `failureThreshold` _integer_                                      |             |         |            |

#### ProbeHandler

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#probe-v1-core.

_Appears in:_

* [Probe](api-reference.md#probe)

| Field                                                             | Description | Default | Validation |
| ----------------------------------------------------------------- | ----------- | ------- | ---------- |
| `exec` [_ExecAction_](api-reference.md#execaction)                |             |         |            |
| `httpGet` [_HTTPGetAction_](api-reference.md#httpgetaction)       |             |         |            |
| `tcpSocket` [_TCPSocketAction_](api-reference.md#tcpsocketaction) |             |         |            |

#### ReplicaBootstrapFrom

ReplicaBootstrapFrom defines the sources for bootstrapping new relicas.

_Appears in:_

* [ReplicaReplication](api-reference.md#replicareplication)

| Field                                                                                       | Description                                                                                                                                                                                                                                   | Default | Validation              |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------- |
| `physicalBackupTemplateRef` [_LocalObjectReference_](api-reference.md#localobjectreference) | <p>PhysicalBackupTemplateRef is a reference to a PhysicalBackup object that will be used as template to create a new PhysicalBackup object<br>used synchronize the data from an up to date replica to the new replica to be bootstrapped.</p> |         | <p>Required: {}<br></p> |
| `restoreJob` [_Job_](api-reference.md#job)                                                  | RestoreJob defines additional properties for the Job used to perform the restoration.                                                                                                                                                         |         |                         |

#### ReplicaRecovery

ReplicaRecovery defines how the replicas should be recovered after they enter an error state.

_Appears in:_

* [ReplicaReplication](api-reference.md#replicareplication)

| Field                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                     | Default | Validation              |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------- |
| `enabled` _boolean_                                                                                                          | Enabled is a flag to enable replica recovery.                                                                                                                                                                                                                                                                                                                                                   |         | <p>Required: {}<br></p> |
| `errorDurationThreshold` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | <p>ErrorDurationThreshold defines the time duration after which, if a replica continues to report errors,<br>the operator will initiate the recovery process for that replica.<br>This threshold applies only to error codes not identified as recoverable by the operator.<br>Errors identified as recoverable will trigger the recovery process immediately.<br>It defaults to 5 minutes.</p> |         |                         |

#### ReplicaReplication

ReplicaReplication is the replication configuration and operation parameters for the replicas.

_Appears in:_

* [Replication](api-reference.md#replication)
* [ReplicationSpec](api-reference.md#replicationspec)

| Field                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Default | Validation                             |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------- |
| `replPasswordSecretKeyRef` [_GeneratedSecretKeyRef_](api-reference.md#generatedsecretkeyref)                      | <p>ReplPasswordSecretKeyRef provides a reference to the Secret to use as password for the replication user.<br>By default, a random password will be generated.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |         |                                        |
| `gtid` [_Gtid_](api-reference.md#gtid)                                                                            | <p>Gtid indicates which Global Transaction ID (GTID) position mode should be used when connecting a replica to the master.<br>By default, CurrentPos is used.<br>See: https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_use_gtid.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                           |         | <p>Enum: [CurrentPos SlavePos]<br></p> |
| `connectionRetrySeconds` _integer_                                                                                | <p>ConnectionRetrySeconds is the number of seconds that the replica will wait between connection retries.<br>See: https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_connect_retry.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |         |                                        |
| `maxLagSeconds` _integer_                                                                                         | <p>MaxLagSeconds is the maximum number of seconds that replicas are allowed to lag behind the primary.<br>If a replica exceeds this threshold, it is marked as not ready and read queries will no longer be forwarded to it.<br>If not provided, it defaults to 0, which means that replicas are not allowed to lag behind the primary (recommended).<br>Lagged replicas will not be taken into account as candidates for the new primary during failover,<br>and they will block other operations, such as switchover and upgrade.<br>This field is not taken into account by MaxScale, you can define the maximum lag as router parameters.<br>See: https://mariadb.com/docs/maxscale/reference/maxscale-routers/maxscale-readwritesplit#max_replication_lag.</p> |         |                                        |
| `syncTimeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | <p>SyncTimeout defines the timeout for the synchronization phase during switchover and failover operations.<br>During switchover, all replicas must be synced with the current primary before promoting the new primary.<br>During failover, the new primary must be synced before being promoted as primary. This implies processing all the events in the relay log.<br>When the timeout is reached, the operator restarts the operation from the beginning.<br>It defaults to 10s.<br>See: https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/miscellaneous-functions/master_gtid_wait</p>                                                                                                                                              |         |                                        |
| `bootstrapFrom` [_ReplicaBootstrapFrom_](api-reference.md#replicabootstrapfrom)                                   | <p>ReplicaBootstrapFrom defines the data sources used to bootstrap new replicas.<br>This will be used as part of the scaling out and recovery operations, when new replicas are created.<br>If not provided, scale out and recovery operations will return an error.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |         |                                        |
| `recovery` [_ReplicaRecovery_](api-reference.md#replicarecovery)                                                  | <p>ReplicaRecovery defines how the replicas should be recovered after they enter an error state.<br>This process deletes data from faulty replicas and recreates them using the source defined in the bootstrapFrom field.<br>It is disabled by default, and it requires the bootstrapFrom field to be set.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                     |         |                                        |

#### Replication

Replication defines replication configuration for a MariaDB cluster.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                        | Default | Validation                               |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------- |
| `primary` [_PrimaryReplication_](api-reference.md#primaryreplication)                                                    | Primary is the replication configuration for the primary node.                                                                                                                                                                                                                                                                                                                                     |         |                                          |
| `replica` [_ReplicaReplication_](api-reference.md#replicareplication)                                                    | ReplicaReplication is the replication configuration for the replica nodes.                                                                                                                                                                                                                                                                                                                         |         |                                          |
| `gtidStrictMode` _boolean_                                                                                               | <p>GtidStrictMode determines whether the GTID strict mode is enabled.<br>See: https://mariadb.com/docs/server/ha-and-performance/standard-replication/gtid#gtid_strict_mode.<br>It is enabled by default.</p>                                                                                                                                                                                      |         |                                          |
| `semiSyncEnabled` _boolean_                                                                                              | <p>SemiSyncEnabled determines whether semi-synchronous replication is enabled.<br>Semi-synchronous replication requires that at least one replica should have sent an ACK to the primary node<br>before committing the transaction back to the client.<br>See: https://mariadb.com/docs/server/ha-and-performance/standard-replication/semisynchronous-replication<br>It is enabled by default</p> |         |                                          |
| `semiSyncAckTimeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | <p>SemiSyncAckTimeout for the replica to acknowledge transactions to the primary.<br>It requires semi-synchronous replication to be enabled.<br>See: https://mariadb.com/docs/server/ha-and-performance/standard-replication/semisynchronous-replication#rpl_semi_sync_master_timeout</p>                                                                                                          |         |                                          |
| `semiSyncWaitPoint` [_WaitPoint_](api-reference.md#waitpoint)                                                            | <p>SemiSyncWaitPoint determines whether the transaction should wait for an ACK after having synced the binlog (AfterSync)<br>or after having committed to the storage engine (AfterCommit, the default).<br>It requires semi-synchronous replication to be enabled.<br>See: https://mariadb.com/kb/en/semisynchronous-replication/#rpl_semi_sync_master_wait_point.</p>                            |         | <p>Enum: [AfterSync AfterCommit]<br></p> |
| `syncBinlog` _integer_                                                                                                   | <p>SyncBinlog indicates after how many events the binary log is synchronized to the disk.<br>See: https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#sync_binlog</p>                                                                                                                                                              |         |                                          |
| `initContainer` [_InitContainer_](api-reference.md#initcontainer)                                                        | InitContainer is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.                                                                                                                                                                                                                                                                                  |         |                                          |
| `agent` [_Agent_](api-reference.md#agent)                                                                                | Agent is a sidecar agent that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.                                                                                                                                                                                                                                                                                            |         |                                          |
| `standaloneProbes` _boolean_                                                                                             | <p>StandaloneProbes indicates whether to use the default non-HA startup and liveness probes.<br>It is disabled by default</p>                                                                                                                                                                                                                                                                      |         |                                          |
| `enabled` _boolean_                                                                                                      | Enabled is a flag to enable replication.                                                                                                                                                                                                                                                                                                                                                           |         |                                          |

#### ReplicationSpec

ReplicationSpec is the replication desired state.

_Appears in:_

* [Replication](api-reference.md#replication)

| Field                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                        | Default | Validation                               |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------- |
| `primary` [_PrimaryReplication_](api-reference.md#primaryreplication)                                                    | Primary is the replication configuration for the primary node.                                                                                                                                                                                                                                                                                                                                     |         |                                          |
| `replica` [_ReplicaReplication_](api-reference.md#replicareplication)                                                    | ReplicaReplication is the replication configuration for the replica nodes.                                                                                                                                                                                                                                                                                                                         |         |                                          |
| `gtidStrictMode` _boolean_                                                                                               | <p>GtidStrictMode determines whether the GTID strict mode is enabled.<br>See: https://mariadb.com/docs/server/ha-and-performance/standard-replication/gtid#gtid_strict_mode.<br>It is enabled by default.</p>                                                                                                                                                                                      |         |                                          |
| `semiSyncEnabled` _boolean_                                                                                              | <p>SemiSyncEnabled determines whether semi-synchronous replication is enabled.<br>Semi-synchronous replication requires that at least one replica should have sent an ACK to the primary node<br>before committing the transaction back to the client.<br>See: https://mariadb.com/docs/server/ha-and-performance/standard-replication/semisynchronous-replication<br>It is enabled by default</p> |         |                                          |
| `semiSyncAckTimeout` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | <p>SemiSyncAckTimeout for the replica to acknowledge transactions to the primary.<br>It requires semi-synchronous replication to be enabled.<br>See: https://mariadb.com/docs/server/ha-and-performance/standard-replication/semisynchronous-replication#rpl_semi_sync_master_timeout</p>                                                                                                          |         |                                          |
| `semiSyncWaitPoint` [_WaitPoint_](api-reference.md#waitpoint)                                                            | <p>SemiSyncWaitPoint determines whether the transaction should wait for an ACK after having synced the binlog (AfterSync)<br>or after having committed to the storage engine (AfterCommit, the default).<br>It requires semi-synchronous replication to be enabled.<br>See: https://mariadb.com/kb/en/semisynchronous-replication/#rpl_semi_sync_master_wait_point.</p>                            |         | <p>Enum: [AfterSync AfterCommit]<br></p> |
| `syncBinlog` _integer_                                                                                                   | <p>SyncBinlog indicates after how many events the binary log is synchronized to the disk.<br>See: https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#sync_binlog</p>                                                                                                                                                              |         |                                          |
| `initContainer` [_InitContainer_](api-reference.md#initcontainer)                                                        | InitContainer is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.                                                                                                                                                                                                                                                                                  |         |                                          |
| `agent` [_Agent_](api-reference.md#agent)                                                                                | Agent is a sidecar agent that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.                                                                                                                                                                                                                                                                                            |         |                                          |
| `standaloneProbes` _boolean_                                                                                             | <p>StandaloneProbes indicates whether to use the default non-HA startup and liveness probes.<br>It is disabled by default</p>                                                                                                                                                                                                                                                                      |         |                                          |

#### ResourceRequirements

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#resourcerequirements-v1-core.

_Appears in:_

* [Agent](api-reference.md#agent)
* [BackupSpec](api-reference.md#backupspec)
* [Container](api-reference.md#container)
* [ContainerTemplate](api-reference.md#containertemplate)
* [Exporter](api-reference.md#exporter)
* [GaleraInitJob](api-reference.md#galerainitjob)
* [GaleraRecoveryJob](api-reference.md#galerarecoveryjob)
* [InitContainer](api-reference.md#initcontainer)
* [Job](api-reference.md#job)
* [JobContainerTemplate](api-reference.md#jobcontainertemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

#### Restore

Restore is the Schema for the restores API. It is used to define restore jobs and its restoration source.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `Restore`                                                       |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_RestoreSpec_](api-reference.md#restorespec)                                                               |                                                                 |         |            |

#### RestoreSource

RestoreSource defines a source for restoring a logical backup.

_Appears in:_

* [RestoreSpec](api-reference.md#restorespec)

| Field                                                                                                            | Description                                                                                                                                                                                                                                                           | Default | Validation |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `backupRef` [_LocalObjectReference_](api-reference.md#localobjectreference)                                      | BackupRef is a reference to a Backup object. It has priority over S3 and Volume.                                                                                                                                                                                      |         |            |
| `s3` [_S3_](api-reference.md#s3)                                                                                 | S3 defines the configuration to restore backups from a S3 compatible storage. It has priority over Volume.                                                                                                                                                            |         |            |
| `volume` [_StorageVolumeSource_](api-reference.md#storagevolumesource)                                           | Volume is a Kubernetes Volume object that contains a backup.                                                                                                                                                                                                          |         |            |
| `targetRecoveryTime` [_Time_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#time-v1-meta) | <p>TargetRecoveryTime is a RFC3339 (1970-01-01T00:00:00Z) date and time that defines the point in time recovery objective.<br>It is used to determine the closest restoration source in time.</p>                                                                     |         |            |
| `stagingStorage` [_BackupStagingStorage_](api-reference.md#backupstagingstorage)                                 | <p>StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.<br>It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Restore Job is scheduled.</p> |         |            |

#### RestoreSpec

RestoreSpec defines the desired state of restore

_Appears in:_

* [Restore](api-reference.md#restore)

| Field                                                                                                                         | Description                                                                                                                                                                                                                                                           | Default   | Validation                                                  |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------- |
| `args` _string array_                                                                                                         | Args to be used in the Container.                                                                                                                                                                                                                                     |           |                                                             |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                                   | Resources describes the compute resource requirements.                                                                                                                                                                                                                |           |                                                             |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)                                                       | SecurityContext holds security configuration that will be applied to a container.                                                                                                                                                                                     |           |                                                             |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                                                                                                                                                                                                       |           |                                                             |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                                                                            |           |                                                             |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                                                                                    |           |                                                             |
| `serviceAccountName` _string_                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                                                                                          |           |                                                             |
| `affinity` [_AffinityConfig_](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                                                                                                                                                                                                       |           |                                                             |
| `nodeSelector` _object (keys:string, values:string)_                                                                          | NodeSelector to be used in the Pod.                                                                                                                                                                                                                                   |           |                                                             |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                                                                                                                                                                                                                                    |           |                                                             |
| `priorityClassName` _string_                                                                                                  | PriorityClassName to be used in the Pod.                                                                                                                                                                                                                              |           |                                                             |
| `backupRef` [_LocalObjectReference_](api-reference.md#localobjectreference)                                                   | BackupRef is a reference to a Backup object. It has priority over S3 and Volume.                                                                                                                                                                                      |           |                                                             |
| `s3` [_S3_](api-reference.md#s3)                                                                                              | S3 defines the configuration to restore backups from a S3 compatible storage. It has priority over Volume.                                                                                                                                                            |           |                                                             |
| `volume` [_StorageVolumeSource_](api-reference.md#storagevolumesource)                                                        | Volume is a Kubernetes Volume object that contains a backup.                                                                                                                                                                                                          |           |                                                             |
| `targetRecoveryTime` [_Time_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#time-v1-meta)              | <p>TargetRecoveryTime is a RFC3339 (1970-01-01T00:00:00Z) date and time that defines the point in time recovery objective.<br>It is used to determine the closest restoration source in time.</p>                                                                     |           |                                                             |
| `stagingStorage` [_BackupStagingStorage_](api-reference.md#backupstagingstorage)                                              | <p>StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.<br>It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Restore Job is scheduled.</p> |           |                                                             |
| `mariaDbRef` [_MariaDBRef_](api-reference.md#mariadbref)                                                                      | MariaDBRef is a reference to a MariaDB object.                                                                                                                                                                                                                        |           | <p>Required: {}<br></p>                                     |
| `database` _string_                                                                                                           | <p>Database defines the logical database to be restored. If not provided, all databases available in the backup are restored.<br>IMPORTANT: The database must previously exist.</p>                                                                                   |           |                                                             |
| `logLevel` _string_                                                                                                           | LogLevel to be used n the Backup Job. It defaults to 'info'.                                                                                                                                                                                                          | info      | <p>Enum: [debug info warn error dpanic panic fatal]<br></p> |
| `backoffLimit` _integer_                                                                                                      | BackoffLimit defines the maximum number of attempts to successfully perform a Backup.                                                                                                                                                                                 | 5         |                                                             |
| `restartPolicy` [_RestartPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#restartpolicy-v1-core) | RestartPolicy to be added to the Backup Job.                                                                                                                                                                                                                          | OnFailure | <p>Enum: [Always OnFailure Never]<br></p>                   |
| `inheritMetadata` [_Metadata_](api-reference.md#metadata)                                                                     | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                                                                           |           |                                                             |

#### S3

_Appears in:_

* [BackupStorage](api-reference.md#backupstorage)
* [BootstrapFrom](api-reference.md#bootstrapfrom)
* [PhysicalBackupStorage](api-reference.md#physicalbackupstorage)
* [RestoreSource](api-reference.md#restoresource)
* [RestoreSpec](api-reference.md#restorespec)

| Field                                                                                   | Description                                                                                                                                                                                                                                                                             | Default | Validation              |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------- |
| `bucket` _string_                                                                       | Bucket is the name Name of the bucket to store backups.                                                                                                                                                                                                                                 |         | <p>Required: {}<br></p> |
| `endpoint` _string_                                                                     | Endpoint is the S3 API endpoint without scheme.                                                                                                                                                                                                                                         |         | <p>Required: {}<br></p> |
| `region` _string_                                                                       | Region is the S3 region name to use.                                                                                                                                                                                                                                                    |         |                         |
| `prefix` _string_                                                                       | Prefix indicates a folder/subfolder in the bucket. For example: mariadb/ or mariadb/backups. A trailing slash '/' is added if not provided.                                                                                                                                             |         |                         |
| `accessKeyIdSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector)     | AccessKeyIdSecretKeyRef is a reference to a Secret key containing the S3 access key id.                                                                                                                                                                                                 |         |                         |
| `secretAccessKeySecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector) | AccessKeyIdSecretKeyRef is a reference to a Secret key containing the S3 secret key.                                                                                                                                                                                                    |         |                         |
| `sessionTokenSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector)    | SessionTokenSecretKeyRef is a reference to a Secret key containing the S3 session token.                                                                                                                                                                                                |         |                         |
| `tls` [_TLSS3_](api-reference.md#tlss3)                                                 | TLS provides the configuration required to establish TLS connections with S3.                                                                                                                                                                                                           |         |                         |
| `ssec` [_SSECConfig_](api-reference.md#ssecconfig)                                      | <p>SSEC is a reference to a Secret containing the SSE-C (Server-Side Encryption with Customer-Provided Keys) key.<br>The secret must contain a 32-byte key (256 bits) in the specified key.<br>This enables server-side encryption where you provide and manage the encryption key.</p> |         |                         |

#### SQLTemplate

SQLTemplate defines a template to customize SQL objects.

_Appears in:_

* [DatabaseSpec](api-reference.md#databasespec)
* [GrantSpec](api-reference.md#grantspec)
* [UserSpec](api-reference.md#userspec)

| Field                                                                                                                 | Description                                                        | Default | Validation                     |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------- | ------------------------------ |
| `requeueInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations.        |         |                                |
| `retryInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)   | RetryInterval is the interval used to perform retries.             |         |                                |
| `cleanupPolicy` [_CleanupPolicy_](api-reference.md#cleanuppolicy)                                                     | CleanupPolicy defines the behavior for cleaning up a SQL resource. |         | <p>Enum: [Skip Delete]<br></p> |

#### SSECConfig

SSECConfig defines the configuration for SSE-C (Server-Side Encryption with Customer-Provided Keys).

_Appears in:_

* [S3](api-reference.md#s3)

| Field                                                                               | Description                                                                                                                                                                        | Default | Validation              |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------- |
| `customerKeySecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector) | <p>CustomerKeySecretKeyRef is a reference to a Secret key containing the SSE-C customer-provided encryption key.<br>The key must be a 32-byte (256-bit) key encoded in base64.</p> |         | <p>Required: {}<br></p> |

#### SST

_Underlying type:_ _string_

SST is the Snapshot State Transfer used when new Pods join the cluster. More info: https://galeracluster.com/library/documentation/sst.html.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field         | Description                                                                          |
| ------------- | ------------------------------------------------------------------------------------ |
| `rsync`       | <p>SSTRsync is an SST based on rsync.<br></p>                                        |
| `mariabackup` | <p>SSTMariaBackup is an SST based on mariabackup. It is the recommended SST.<br></p> |
| `mysqldump`   | <p>SSTMysqldump is an SST based on mysqldump.<br></p>                                |

#### Schedule

Schedule contains parameters to define a schedule

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field               | Description                                            | Default | Validation              |
| ------------------- | ------------------------------------------------------ | ------- | ----------------------- |
| `cron` _string_     | Cron is a cron expression that defines the schedule.   |         | <p>Required: {}<br></p> |
| `suspend` _boolean_ | Suspend defines whether the schedule is active or not. | false   |                         |

#### SecretKeySelector

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#secretkeyselector-v1-core.

_Appears in:_

* [ConnectionSpec](api-reference.md#connectionspec)
* [EnvVarSource](api-reference.md#envvarsource)
* [ExternalMariaDBSpec](api-reference.md#externalmariadbspec)
* [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [PasswordPlugin](api-reference.md#passwordplugin)
* [S3](api-reference.md#s3)
* [SSECConfig](api-reference.md#ssecconfig)
* [SqlJobSpec](api-reference.md#sqljobspec)
* [TLSS3](api-reference.md#tlss3)
* [UserSpec](api-reference.md#userspec)

| Field           | Description | Default | Validation |
| --------------- | ----------- | ------- | ---------- |
| `name` _string_ |             |         |            |
| `key` _string_  |             |         |            |

#### SecretTemplate

SecretTemplate defines a template to customize Secret objects.

_Appears in:_

* [ConnectionSpec](api-reference.md#connectionspec)
* [ConnectionTemplate](api-reference.md#connectiontemplate)

| Field                                              | Description                                                     | Default | Validation |
| -------------------------------------------------- | --------------------------------------------------------------- | ------- | ---------- |
| `metadata` [_Metadata_](api-reference.md#metadata) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `key` _string_                                     | Key to be used in the Secret.                                   |         |            |
| `format` _string_                                  | Format to be used in the Secret.                                |         |            |
| `usernameKey` _string_                             | UsernameKey to be used in the Secret.                           |         |            |
| `passwordKey` _string_                             | PasswordKey to be used in the Secret.                           |         |            |
| `hostKey` _string_                                 | HostKey to be used in the Secret.                               |         |            |
| `portKey` _string_                                 | PortKey to be used in the Secret.                               |         |            |
| `databaseKey` _string_                             | DatabaseKey to be used in the Secret.                           |         |            |

#### SecretVolumeSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#secretvolumesource-v1-core.

_Appears in:_

* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field                   | Description | Default | Validation |
| ----------------------- | ----------- | ------- | ---------- |
| `secretName` _string_   |             |         |            |
| `defaultMode` _integer_ |             |         |            |

#### SecurityContext

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#securitycontext-v1-core.

_Appears in:_

* [Agent](api-reference.md#agent)
* [BackupSpec](api-reference.md#backupspec)
* [ContainerTemplate](api-reference.md#containertemplate)
* [Exporter](api-reference.md#exporter)
* [InitContainer](api-reference.md#initcontainer)
* [JobContainerTemplate](api-reference.md#jobcontainertemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PhysicalBackupSpec](api-reference.md#physicalbackupspec)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                                                                                                      | Description | Default | Validation |
| -------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `capabilities` [_Capabilities_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#capabilities-v1-core) |             |         |            |
| `privileged` _boolean_                                                                                                     |             |         |            |
| `runAsUser` _integer_                                                                                                      |             |         |            |
| `runAsGroup` _integer_                                                                                                     |             |         |            |
| `runAsNonRoot` _boolean_                                                                                                   |             |         |            |
| `readOnlyRootFilesystem` _boolean_                                                                                         |             |         |            |
| `allowPrivilegeEscalation` _boolean_                                                                                       |             |         |            |

#### ServiceMonitor

ServiceMonitor defines a prometheus ServiceMonitor object.

_Appears in:_

* [MariadbMetrics](api-reference.md#mariadbmetrics)
* [MaxScaleMetrics](api-reference.md#maxscalemetrics)

| Field                        | Description                                                                 | Default | Validation |
| ---------------------------- | --------------------------------------------------------------------------- | ------- | ---------- |
| `prometheusRelease` _string_ | PrometheusRelease is the release label to add to the ServiceMonitor object. |         |            |
| `jobLabel` _string_          | JobLabel to add to the ServiceMonitor object.                               |         |            |
| `interval` _string_          | Interval for scraping metrics.                                              |         |            |
| `scrapeTimeout` _string_     | ScrapeTimeout defines the timeout for scraping metrics.                     |         |            |

#### ServicePort

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#serviceport-v1-core

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field            | Description | Default | Validation |
| ---------------- | ----------- | ------- | ---------- |
| `name` _string_  |             |         |            |
| `port` _integer_ |             |         |            |

#### ServiceRouter

_Underlying type:_ _string_

ServiceRouter defines the type of service router.

_Appears in:_

* [MaxScaleService](api-reference.md#maxscaleservice)

| Field            | Description                                                                                                                                          |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `readwritesplit` | <p>ServiceRouterReadWriteSplit splits the load based on the queries. Write queries are performed on master and read queries on the replicas.<br></p> |
| `readconnroute`  | <p>ServiceRouterReadConnRoute splits the load based on the connections. Each connection is assigned to a server.<br></p>                             |

#### ServiceTemplate

ServiceTemplate defines a template to customize Service objects.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                                                                                               | Description                                                                                                             | Default   | Validation                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------- | -------------------------------------------------- |
| `type` [_ServiceType_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#servicetype-v1-core)                                                    | Type is the Service type. One of `ClusterIP`, `NodePort` or `LoadBalancer`. If not defined, it defaults to `ClusterIP`. | ClusterIP | <p>Enum: [ClusterIP NodePort LoadBalancer]<br></p> |
| `metadata` [_Metadata_](api-reference.md#metadata)                                                                                                                  | Refer to Kubernetes API documentation for fields of `metadata`.                                                         |           |                                                    |
| `loadBalancerIP` _string_                                                                                                                                           | LoadBalancerIP Service field.                                                                                           |           |                                                    |
| `loadBalancerSourceRanges` _string array_                                                                                                                           | LoadBalancerSourceRanges Service field.                                                                                 |           |                                                    |
| `externalTrafficPolicy` [_ServiceExternalTrafficPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#serviceexternaltrafficpolicy-v1-core) | ExternalTrafficPolicy Service field.                                                                                    |           |                                                    |
| `sessionAffinity` [_ServiceAffinity_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#serviceaffinity-v1-core)                                 | SessionAffinity Service field.                                                                                          |           |                                                    |
| `allocateLoadBalancerNodePorts` _boolean_                                                                                                                           | AllocateLoadBalancerNodePorts Service field.                                                                            |           |                                                    |

#### SqlJob

SqlJob is the Schema for the sqljobs API. It is used to run sql scripts as jobs.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `SqlJob`                                                        |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_SqlJobSpec_](api-reference.md#sqljobspec)                                                                 |                                                                 |         |            |

#### SqlJobSpec

SqlJobSpec defines the desired state of SqlJob

_Appears in:_

* [SqlJob](api-reference.md#sqljob)

| Field                                                                                                                         | Description                                                                                                                                                                                                    | Default   | Validation                                |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------- |
| `args` _string array_                                                                                                         | Args to be used in the Container.                                                                                                                                                                              |           |                                           |
| `resources` [_ResourceRequirements_](api-reference.md#resourcerequirements)                                                   | Resources describes the compute resource requirements.                                                                                                                                                         |           |                                           |
| `securityContext` [_SecurityContext_](api-reference.md#securitycontext)                                                       | SecurityContext holds security configuration that will be applied to a container.                                                                                                                              |           |                                           |
| `podMetadata` [_Metadata_](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                                                                                                                                                |           |                                           |
| `imagePullSecrets` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                     |           |                                           |
| `podSecurityContext` [_PodSecurityContext_](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                             |           |                                           |
| `serviceAccountName` _string_                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                                   |           |                                           |
| `affinity` [_AffinityConfig_](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                                                                                                                                                |           |                                           |
| `nodeSelector` _object (keys:string, values:string)_                                                                          | NodeSelector to be used in the Pod.                                                                                                                                                                            |           |                                           |
| `tolerations` [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) _array_ | Tolerations to be used in the Pod.                                                                                                                                                                             |           |                                           |
| `priorityClassName` _string_                                                                                                  | PriorityClassName to be used in the Pod.                                                                                                                                                                       |           |                                           |
| `successfulJobsHistoryLimit` _integer_                                                                                        | SuccessfulJobsHistoryLimit defines the maximum number of successful Jobs to be displayed.                                                                                                                      |           | <p>Minimum: 0<br></p>                     |
| `failedJobsHistoryLimit` _integer_                                                                                            | FailedJobsHistoryLimit defines the maximum number of failed Jobs to be displayed.                                                                                                                              |           | <p>Minimum: 0<br></p>                     |
| `timeZone` _string_                                                                                                           | TimeZone defines the timezone associated with the cron expression.                                                                                                                                             |           |                                           |
| `mariaDbRef` [_MariaDBRef_](api-reference.md#mariadbref)                                                                      | MariaDBRef is a reference to a MariaDB object.                                                                                                                                                                 |           | <p>Required: {}<br></p>                   |
| `schedule` [_Schedule_](api-reference.md#schedule)                                                                            | Schedule defines when the SqlJob will be executed.                                                                                                                                                             |           |                                           |
| `username` _string_                                                                                                           | Username to be impersonated when executing the SqlJob.                                                                                                                                                         |           | <p>Required: {}<br></p>                   |
| `passwordSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector)                                              | UserPasswordSecretKeyRef is a reference to the impersonated user's password to be used when executing the SqlJob.                                                                                              |           | <p>Required: {}<br></p>                   |
| `tlsCASecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)                                              | <p>TLSCACertSecretRef is a reference toa CA Secret used to establish trust when executing the SqlJob.<br>If not provided, the CA bundle provided by the referred MariaDB is used.</p>                          |           |                                           |
| `tlsClientCertSecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)                                      | <p>TLSClientCertSecretRef is a reference to a Kubernetes TLS Secret used as authentication when executing the SqlJob.<br>If not provided, the client certificate provided by the referred MariaDB is used.</p> |           |                                           |
| `database` _string_                                                                                                           | Username to be used when executing the SqlJob.                                                                                                                                                                 |           |                                           |
| `dependsOn` [_LocalObjectReference_](api-reference.md#localobjectreference) _array_                                           | DependsOn defines dependencies with other SqlJob objectecs.                                                                                                                                                    |           |                                           |
| `sql` _string_                                                                                                                | Sql is the script to be executed by the SqlJob.                                                                                                                                                                |           |                                           |
| `sqlConfigMapKeyRef` [_ConfigMapKeySelector_](api-reference.md#configmapkeyselector)                                          | <p>SqlConfigMapKeyRef is a reference to a ConfigMap containing the Sql script.<br>It is defaulted to a ConfigMap with the contents of the Sql field.</p>                                                       |           |                                           |
| `backoffLimit` _integer_                                                                                                      | BackoffLimit defines the maximum number of attempts to successfully execute a SqlJob.                                                                                                                          | 5         |                                           |
| `restartPolicy` [_RestartPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#restartpolicy-v1-core) | RestartPolicy to be added to the SqlJob Pod.                                                                                                                                                                   | OnFailure | <p>Enum: [Always OnFailure Never]<br></p> |
| `inheritMetadata` [_Metadata_](api-reference.md#metadata)                                                                     | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                    |           |                                           |

#### StagingStorage



StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.



_Appears in:_
- [BackupSpec](#backupspec)
- [BootstrapFrom](#bootstrapfrom)
- [PhysicalBackupSpec](#physicalbackupspec)
- [RestoreSource](#restoresource)
- [RestoreSpec](#restorespec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `persistentVolumeClaim` _[PersistentVolumeClaimSpec](#persistentvolumeclaimspec)_ | PersistentVolumeClaim is a Kubernetes PVC specification. |  |  |
| `volume` _[StorageVolumeSource](#storagevolumesource)_ | Volume is a Kubernetes volume specification. |  |  |


#### StatefulSetPersistentVolumeClaimRetentionPolicy

StatefulSetPersistentVolumeClaimRetentionPolicy describes the lifecycle of PVCs created from volumeClaimTemplates. Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#statefulsetpersistentvolumeclaimretentionpolicy-v1-apps.

_Appears in:_

* [Storage](api-reference.md#storage)

| Field                                                                                                                 | Description | Default | Validation |
| --------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `whenDeleted` [_PersistentVolumeClaimRetentionPolicyType_](api-reference.md#persistentvolumeclaimretentionpolicytype) |             |         |            |
| `whenScaled` [_PersistentVolumeClaimRetentionPolicyType_](api-reference.md#persistentvolumeclaimretentionpolicytype)  |             |         |            |

#### Storage

Storage defines the storage options to be used for provisioning the PVCs mounted by MariaDB.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                   | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `ephemeral` _boolean_                                                                                                                      | Ephemeral indicates whether to use ephemeral storage in the PVCs. It is only compatible with non HA MariaDBs.                                                                                                                                                                                                                                                                 |         |            |
| `size` [_Quantity_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#quantity-resource-api)                            | Size of the PVCs to be mounted by MariaDB. Required if not provided in 'VolumeClaimTemplate'. It supersedes the storage size specified in 'VolumeClaimTemplate'.                                                                                                                                                                                                              |         |            |
| `storageClassName` _string_                                                                                                                | <p>StorageClassName to be used to provision the PVCS. It supersedes the 'StorageClassName' specified in 'VolumeClaimTemplate'.<br>If not provided, the default 'StorageClass' configured in the cluster is used.</p>                                                                                                                                                          |         |            |
| `resizeInUseVolumes` _boolean_                                                                                                             | <p>ResizeInUseVolumes indicates whether the PVCs can be resized. The 'StorageClassName' used should have 'allowVolumeExpansion' set to 'true' to allow resizing.<br>It defaults to true.</p>                                                                                                                                                                                  |         |            |
| `waitForVolumeResize` _boolean_                                                                                                            | <p>WaitForVolumeResize indicates whether to wait for the PVCs to be resized before marking the MariaDB object as ready. This will block other operations such as cluster recovery while the resize is in progress.<br>It defaults to true.</p>                                                                                                                                |         |            |
| `volumeClaimTemplate` [_VolumeClaimTemplate_](api-reference.md#volumeclaimtemplate)                                                        | VolumeClaimTemplate provides a template to define the PVCs.                                                                                                                                                                                                                                                                                                                   |         |            |
| `pvcRetentionPolicy` [_StatefulSetPersistentVolumeClaimRetentionPolicy_](api-reference.md#statefulsetpersistentvolumeclaimretentionpolicy) | <p>PersistentVolumeClaimRetentionPolicy describes the lifecycle of PVCs created from volumeClaimTemplates.<br>By default, all persistent volume claims are created as needed and retained until manually deleted.<br>This policy allows the lifecycle to be altered, for example by deleting PVCs when their statefulset is deleted,<br>or when their pod is scaled down.</p> |         |            |

#### StorageVolumeSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#volume-v1-core.

_Appears in:_

* [BackupStagingStorage](api-reference.md#backupstagingstorage)
* [BackupStorage](api-reference.md#backupstorage)
* [BootstrapFrom](api-reference.md#bootstrapfrom)
* [PhysicalBackupStorage](api-reference.md#physicalbackupstorage)
* [RestoreSource](api-reference.md#restoresource)
* [RestoreSpec](api-reference.md#restorespec)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field                                                                                                             | Description | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `emptyDir` [_EmptyDirVolumeSource_](api-reference.md#emptydirvolumesource)                                        |             |         |            |
| `nfs` [_NFSVolumeSource_](api-reference.md#nfsvolumesource)                                                       |             |         |            |
| `csi` [_CSIVolumeSource_](api-reference.md#csivolumesource)                                                       |             |         |            |
| `hostPath` [_HostPathVolumeSource_](api-reference.md#hostpathvolumesource)                                        |             |         |            |
| `persistentVolumeClaim` [_PersistentVolumeClaimVolumeSource_](api-reference.md#persistentvolumeclaimvolumesource) |             |         |            |

#### SuspendTemplate

SuspendTemplate indicates whether the current resource should be suspended or not.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleListener](api-reference.md#maxscalelistener)
* [MaxScaleMonitor](api-reference.md#maxscalemonitor)
* [MaxScaleService](api-reference.md#maxscaleservice)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field               | Description                                                                                                                                                                                                                                         | Default | Validation |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `suspend` _boolean_ | <p>Suspend indicates whether the current resource should be suspended or not.<br>This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities.</p> | false   |            |

#### TCPSocketAction

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#tcpsocketaction-v1-core.

_Appears in:_

* [Probe](api-reference.md#probe)
* [ProbeHandler](api-reference.md#probehandler)

| Field                                                                                                                | Description | Default | Validation |
| -------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `port` [_IntOrString_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#intorstring-intstr-util) |             |         |            |
| `host` _string_                                                                                                      |             |         |            |

#### TLS

TLS defines the PKI to be used with MariaDB.

_Appears in:_

* [ExternalTLS](api-reference.md#externaltls)
* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Default | Validation                                                     |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------- |
| `enabled` _boolean_                                                                   | <p>Enabled indicates whether TLS is enabled, determining if certificates should be issued and mounted to the MariaDB instance.<br>It is enabled by default.</p>                                                                                                                                                                                                                                                                                                                                                                                                                 |         |                                                                |
| `required` _boolean_                                                                  | <p>Required specifies whether TLS must be enforced for all connections.<br>User TLS requirements take precedence over this.<br>It disabled by default.</p>                                                                                                                                                                                                                                                                                                                                                                                                                      |         |                                                                |
| `versions` _string array_                                                             | <p>Versions specifies the supported TLS versions for this MariaDB instance.<br>By default, the MariaDB's default supported versions are used. See: https://mariadb.com/kb/en/ssltls-system-variables/#tls_version.</p>                                                                                                                                                                                                                                                                                                                                                          |         | <p>items:Enum: [TLSv1.0 TLSv1.1 TLSv1.2 TLSv1.3]<br></p>       |
| `serverCASecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)   | <p>ServerCASecretRef is a reference to a Secret containing the server certificate authority keypair. It is used to establish trust and issue server certificates.<br>One of:<br>- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.<br>- Secret containing only the 'ca.crt' in order to establish trust. In this case, either serverCertSecretRef or serverCertIssuerRef must be provided.<br>If not provided, a self-signed CA will be provisioned to issue the server certificate.</p>        |         |                                                                |
| `serverCertSecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference) | <p>ServerCertSecretRef is a reference to a TLS Secret containing the server certificate.<br>It is mutually exclusive with serverCertIssuerRef.</p>                                                                                                                                                                                                                                                                                                                                                                                                                              |         |                                                                |
| `serverCertIssuerRef` [_ObjectReference_](api-reference.md#objectreference)           | <p>ServerCertIssuerRef is a reference to a cert-manager issuer object used to issue the server certificate. cert-manager must be installed previously in the cluster.<br>It is mutually exclusive with serverCertSecretRef.<br>By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via serverCASecretRef.</p>                                                                                                                                                                            |         |                                                                |
| `serverCertConfig` [_TLSConfig_](api-reference.md#tlsconfig)                          | <p>ServerCertConfig allows configuring the server certificates, either issued by the operator or cert-manager.<br>If not set, the default settings will be used.</p>                                                                                                                                                                                                                                                                                                                                                                                                            |         |                                                                |
| `clientCASecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference)   | <p>ClientCASecretRef is a reference to a Secret containing the client certificate authority keypair. It is used to establish trust and issue client certificates.<br>One of:<br>- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.<br>- Secret containing only the 'ca.crt' in order to establish trust. In this case, either clientCertSecretRef or clientCertIssuerRef fields must be provided.<br>If not provided, a self-signed CA will be provisioned to issue the client certificate.</p> |         |                                                                |
| `clientCertSecretRef` [_LocalObjectReference_](api-reference.md#localobjectreference) | <p>ClientCertSecretRef is a reference to a TLS Secret containing the client certificate.<br>It is mutually exclusive with clientCertIssuerRef.</p>                                                                                                                                                                                                                                                                                                                                                                                                                              |         |                                                                |
| `clientCertIssuerRef` [_ObjectReference_](api-reference.md#objectreference)           | <p>ClientCertIssuerRef is a reference to a cert-manager issuer object used to issue the client certificate. cert-manager must be installed previously in the cluster.<br>It is mutually exclusive with clientCertSecretRef.<br>By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via clientCASecretRef.</p>                                                                                                                                                                            |         |                                                                |
| `clientCertConfig` [_TLSConfig_](api-reference.md#tlsconfig)                          | <p>ClientCertConfig allows configuring the client certificates, either issued by the operator or cert-manager.<br>If not set, the default settings will be used.</p>                                                                                                                                                                                                                                                                                                                                                                                                            |         |                                                                |
| `galeraSSTEnabled` _boolean_                                                          | <p>GaleraSSTEnabled determines whether Galera SST connections should use TLS.<br>It disabled by default.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |         |                                                                |
| `galeraServerSSLMode` _string_                                                        | <p>GaleraServerSSLMode defines the server SSL mode for a Galera Enterprise cluster.<br>This field is only supported and applicable for Galera Enterprise >= 10.6 instances.<br>Refer to the MariaDB Enterprise docs for more detail: https://mariadb.com/docs/galera-cluster/galera-security/mariadb-enterprise-cluster-security#wsrep-tls-modes</p>                                                                                                                                                                                                                            |         | <p>Enum: [PROVIDER SERVER SERVER_X509]<br></p>                 |
| `galeraClientSSLMode` _string_                                                        | <p>GaleraClientSSLMode defines the client SSL mode for a Galera Enterprise cluster.<br>This field is only supported and applicable for Galera Enterprise >= 10.6 instances.<br>Refer to the MariaDB Enterprise docs for more detail: https://mariadb.com/docs/galera-cluster/galera-security/mariadb-enterprise-cluster-security#sst-tls-modes</p>                                                                                                                                                                                                                              |         | <p>Enum: [DISABLED REQUIRED VERIFY_CA VERIFY_IDENTITY]<br></p> |

#### TLSConfig

TLSConfig defines parameters to configure a certificate.

_Appears in:_

* [ExternalTLS](api-reference.md#externaltls)
* [MaxScaleTLS](api-reference.md#maxscaletls)
* [TLS](api-reference.md#tls)

| Field                                                                                                              | Description                                                                                                                                                          | Default | Validation                   |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------- |
| `caLifetime` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)   | CALifetime defines the CA certificate validity.                                                                                                                      |         |                              |
| `certLifetime` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | CertLifetime defines the certificate validity.                                                                                                                       |         |                              |
| `privateKeyAlgorithm` _string_                                                                                     | <p>PrivateKeyAlgorithm is the algorithm to be used for the CA and leaf certificate private keys.<br>One of: ECDSA or RSA</p>                                         |         | <p>Enum: [ECDSA RSA]<br></p> |
| `privateKeySize` _integer_                                                                                         | <p>PrivateKeyAlgorithm is the key size to be used for the CA and leaf certificate private keys.<br>Supported values: ECDSA(256, 384, 521), RSA(2048, 3072, 4096)</p> |         |                              |

#### TLSRequirements

TLSRequirements specifies TLS requirements for the user to connect. See: https://mariadb.com/kb/en/securing-connections-for-client-and-server/#requiring-tls.

_Appears in:_

* [UserSpec](api-reference.md#userspec)

| Field              | Description                                                                                         | Default | Validation |
| ------------------ | --------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `ssl` _boolean_    | SSL indicates that the user must connect via TLS.                                                   |         |            |
| `x509` _boolean_   | X509 indicates that the user must provide a valid x509 certificate to connect.                      |         |            |
| `issuer` _string_  | Issuer indicates that the TLS certificate provided by the user must be issued by a specific issuer. |         |            |
| `subject` _string_ | Subject indicates that the TLS certificate provided by the user must have a specific subject.       |         |            |

#### TLSS3

_Appears in:_

* [S3](api-reference.md#s3)

| Field                                                                      | Description                                                                                                                                                                                                                                        | Default | Validation |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| `enabled` _boolean_                                                        | Enabled is a flag to enable TLS.                                                                                                                                                                                                                   |         |            |
| `caSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector) | <p>CASecretKeyRef is a reference to a Secret key containing a CA bundle in PEM format used to establish TLS connections with S3.<br>By default, the system trust chain will be used, but you can use this field to add more CAs to the bundle.</p> |         |            |

#### TopologySpreadConstraint

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#topologyspreadconstraint-v1-core.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScalePodTemplate](api-reference.md#maxscalepodtemplate)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PodTemplate](api-reference.md#podtemplate)

| Field                                                                                                                                                             | Description | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `maxSkew` _integer_                                                                                                                                               |             |         |            |
| `topologyKey` _string_                                                                                                                                            |             |         |            |
| `whenUnsatisfiable` [_UnsatisfiableConstraintAction_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#unsatisfiableconstraintaction-v1-core) |             |         |            |
| `labelSelector` [_LabelSelector_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#labelselector-v1-meta)                                     |             |         |            |
| `minDomains` _integer_                                                                                                                                            |             |         |            |
| `nodeAffinityPolicy` [_NodeInclusionPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#nodeinclusionpolicy-v1-core)                    |             |         |            |
| `nodeTaintsPolicy` [_NodeInclusionPolicy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#nodeinclusionpolicy-v1-core)                      |             |         |            |
| `matchLabelKeys` _string array_                                                                                                                                   |             |         |            |

#### TypedLocalObjectReference

TypedLocalObjectReference is a reference to a specific object type.

_Appears in:_

* [BootstrapFrom](api-reference.md#bootstrapfrom)

| Field           | Description           | Default | Validation |
| --------------- | --------------------- | ------- | ---------- |
| `name` _string_ | Name of the referent. |         |            |
| `kind` _string_ | Kind of the referent. |         |            |

#### UpdateStrategy

UpdateStrategy defines how a MariaDB resource is updated.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                       | Default                  | Validation                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------ |
| `type` [_UpdateType_](api-reference.md#updatetype)                                                                                                                  | Type defines the type of updates. One of `ReplicasFirstPrimaryLast`, `RollingUpdate` or `OnDelete`. If not defined, it defaults to `ReplicasFirstPrimaryLast`.                                                                                                                                                                                                                                    | ReplicasFirstPrimaryLast | <p>Enum: [ReplicasFirstPrimaryLast RollingUpdate OnDelete Never]<br></p> |
| `rollingUpdate` [_RollingUpdateStatefulSetStrategy_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#rollingupdatestatefulsetstrategy-v1-apps) | RollingUpdate defines parameters for the RollingUpdate type.                                                                                                                                                                                                                                                                                                                                      |                          |                                                                          |
| `autoUpdateDataPlane` _boolean_                                                                                                                                     | <p>AutoUpdateDataPlane indicates whether the Galera data-plane version (agent and init containers) should be automatically updated based on the operator version. It defaults to false.<br>Updating the operator will trigger updates on all the MariaDB instances that have this flag set to true. Thus, it is recommended to progressively set this flag after having updated the operator.</p> |                          |                                                                          |

#### UpdateType

_Underlying type:_ _string_

UpdateType defines the type of update for a MariaDB resource.

_Appears in:_

* [UpdateStrategy](api-reference.md#updatestrategy)

| Field                      | Description                                                                                                                                                                                                                                                                                                             |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ReplicasFirstPrimaryLast` | <p>ReplicasFirstPrimaryLastUpdateType indicates that the update will be applied to all replica Pods first and later on to the primary Pod.<br>The updates are applied one by one waiting until each Pod passes the readiness probe<br>i.e. the Pod gets synced and it is ready to receive traffic.<br></p>              |
| `RollingUpdate`            | <p>RollingUpdateUpdateType indicates that the update will be applied by the StatefulSet controller using the RollingUpdate strategy.<br>This strategy is unaware of the roles that the Pod have (primary or replica) and it will<br>perform the update following the StatefulSet ordinal, from higher to lower.<br></p> |
| `OnDelete`                 | <p>OnDeleteUpdateType indicates that the update will be applied by the StatefulSet controller using the OnDelete strategy.<br>The update will be done when the Pods get manually deleted by the user.<br></p>                                                                                                           |
| `Never`                    | <p>NeverUpdateType indicates that the StatefulSet will never be updated.<br>This can be used to roll out updates progressively to a fleet of instances.<br></p>                                                                                                                                                         |

#### User

User is the Schema for the users API. It is used to define grants as if you were running a 'CREATE USER' statement.

| Field                                                                                                              | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------- | ---------- |
| `apiVersion` _string_                                                                                              | `enterprise.mariadb.com/v1alpha1`                               |         |            |
| `kind` _string_                                                                                                    | `User`                                                          |         |            |
| `metadata` [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |
| `spec` [_UserSpec_](api-reference.md#userspec)                                                                     |                                                                 |         |            |

#### UserSpec

UserSpec defines the desired state of User

_Appears in:_

* [User](api-reference.md#user)

| Field                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               | Default | Validation                     |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------ |
| `requeueInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations.                                                                                                                                                                                                                                                                                                                                                                                               |         |                                |
| `retryInterval` [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#duration-v1-meta)   | RetryInterval is the interval used to perform retries.                                                                                                                                                                                                                                                                                                                                                                                                    |         |                                |
| `cleanupPolicy` [_CleanupPolicy_](api-reference.md#cleanuppolicy)                                                     | CleanupPolicy defines the behavior for cleaning up a SQL resource.                                                                                                                                                                                                                                                                                                                                                                                        |         | <p>Enum: [Skip Delete]<br></p> |
| `mariaDbRef` [_MariaDBRef_](api-reference.md#mariadbref)                                                              | MariaDBRef is a reference to a MariaDB object.                                                                                                                                                                                                                                                                                                                                                                                                            |         | <p>Required: {}<br></p>        |
| `passwordSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector)                                      | <p>PasswordSecretKeyRef is a reference to the password to be used by the User.<br>If not provided, the account will be locked and the password will expire.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.</p>                                                                                                                                         |         |                                |
| `passwordHashSecretKeyRef` [_SecretKeySelector_](api-reference.md#secretkeyselector)                                  | <p>PasswordHashSecretKeyRef is a reference to the password hash to be used by the User.<br>If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password hash.<br>It requires the 'strict-password-validation=false' option to be set. See: https://mariadb.com/docs/server/server-management/variables-and-modes/server-system-variables#strict_password_validation.</p> |         |                                |
| `passwordPlugin` [_PasswordPlugin_](api-reference.md#passwordplugin)                                                  | <p>PasswordPlugin is a reference to the password plugin and arguments to be used by the User.<br>It requires the 'strict-password-validation=false' option to be set. See: https://mariadb.com/docs/server/server-management/variables-and-modes/server-system-variables#strict_password_validation.</p>                                                                                                                                                  |         |                                |
| `require` [_TLSRequirements_](api-reference.md#tlsrequirements)                                                       | Require specifies TLS requirements for the user to connect. See: https://mariadb.com/kb/en/securing-connections-for-client-and-server/#requiring-tls.                                                                                                                                                                                                                                                                                                     |         |                                |
| `maxUserConnections` _integer_                                                                                        | MaxUserConnections defines the maximum number of simultaneous connections that the User can establish.                                                                                                                                                                                                                                                                                                                                                    | 10      |                                |
| `name` _string_                                                                                                       | Name overrides the default name provided by metadata.name.                                                                                                                                                                                                                                                                                                                                                                                                |         | <p>MaxLength: 80<br></p>       |
| `host` _string_                                                                                                       | Host related to the User.                                                                                                                                                                                                                                                                                                                                                                                                                                 |         | <p>MaxLength: 255<br></p>      |

#### Volume

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#volume-v1-core.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)
* [PodTemplate](api-reference.md#podtemplate)

| Field                                                                                                             | Description | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `name` _string_                                                                                                   |             |         |            |
| `emptyDir` [_EmptyDirVolumeSource_](api-reference.md#emptydirvolumesource)                                        |             |         |            |
| `nfs` [_NFSVolumeSource_](api-reference.md#nfsvolumesource)                                                       |             |         |            |
| `csi` [_CSIVolumeSource_](api-reference.md#csivolumesource)                                                       |             |         |            |
| `hostPath` [_HostPathVolumeSource_](api-reference.md#hostpathvolumesource)                                        |             |         |            |
| `persistentVolumeClaim` [_PersistentVolumeClaimVolumeSource_](api-reference.md#persistentvolumeclaimvolumesource) |             |         |            |
| `secret` [_SecretVolumeSource_](api-reference.md#secretvolumesource)                                              |             |         |            |
| `configMap` [_ConfigMapVolumeSource_](api-reference.md#configmapvolumesource)                                     |             |         |            |

#### VolumeClaimTemplate

VolumeClaimTemplate defines a template to customize PVC objects.

_Appears in:_

* [GaleraConfig](api-reference.md#galeraconfig)
* [MaxScaleConfig](api-reference.md#maxscaleconfig)
* [Storage](api-reference.md#storage)

| Field                                                                                                                                                         | Description                                                     | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------- | ---------- |
| `accessModes` [_PersistentVolumeAccessMode_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#persistentvolumeaccessmode-v1-core) _array_ |                                                                 |         |            |
| `selector` [_LabelSelector_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#labelselector-v1-meta)                                      |                                                                 |         |            |
| `resources` [_VolumeResourceRequirements_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#volumeresourcerequirements-v1-core)           |                                                                 |         |            |
| `storageClassName` _string_                                                                                                                                   |                                                                 |         |            |
| `metadata` [_Metadata_](api-reference.md#metadata)                                                                                                            | Refer to Kubernetes API documentation for fields of `metadata`. |         |            |

#### VolumeMount

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#volumemount-v1-core.

_Appears in:_

* [Agent](api-reference.md#agent)
* [Container](api-reference.md#container)
* [ContainerTemplate](api-reference.md#containertemplate)
* [InitContainer](api-reference.md#initcontainer)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                | Description                           | Default | Validation |
| -------------------- | ------------------------------------- | ------- | ---------- |
| `name` _string_      | This must match the Name of a Volume. |         |            |
| `readOnly` _boolean_ |                                       |         |            |
| `mountPath` _string_ |                                       |         |            |
| `subPath` _string_   |                                       |         |            |

#### VolumeSource

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#volume-v1-core.

_Appears in:_

* [Volume](api-reference.md#volume)

| Field                                                                                                             | Description | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `emptyDir` [_EmptyDirVolumeSource_](api-reference.md#emptydirvolumesource)                                        |             |         |            |
| `nfs` [_NFSVolumeSource_](api-reference.md#nfsvolumesource)                                                       |             |         |            |
| `csi` [_CSIVolumeSource_](api-reference.md#csivolumesource)                                                       |             |         |            |
| `hostPath` [_HostPathVolumeSource_](api-reference.md#hostpathvolumesource)                                        |             |         |            |
| `persistentVolumeClaim` [_PersistentVolumeClaimVolumeSource_](api-reference.md#persistentvolumeclaimvolumesource) |             |         |            |
| `secret` [_SecretVolumeSource_](api-reference.md#secretvolumesource)                                              |             |         |            |
| `configMap` [_ConfigMapVolumeSource_](api-reference.md#configmapvolumesource)                                     |             |         |            |

#### WaitPoint

_Underlying type:_ _string_

WaitPoint defines whether the transaction should wait for ACK before committing to the storage engine. More info: https://mariadb.com/kb/en/semisynchronous-replication/#rpl\_semi\_sync\_master\_wait\_point.

_Appears in:_

* [Replication](api-reference.md#replication)
* [ReplicationSpec](api-reference.md#replicationspec)

| Field         | Description                                                                                                                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AfterSync`   | <p>WaitPointAfterSync indicates that the primary waits for the replica ACK before committing the transaction to the storage engine.<br>It trades off performance for consistency.<br></p>        |
| `AfterCommit` | <p>WaitPointAfterCommit indicates that the primary commits the transaction to the storage engine and waits for the replica ACK afterwards.<br>It trades off consistency for performance.<br></p> |

#### WeightedPodAffinityTerm

Refer to the Kubernetes docs: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#weightedpodaffinityterm-v1-core.

_Appears in:_

* [PodAntiAffinity](api-reference.md#podantiaffinity)

| Field                                                                   | Description | Default | Validation |
| ----------------------------------------------------------------------- | ----------- | ------- | ---------- |
| `weight` _integer_                                                      |             |         |            |
| `podAffinityTerm` [_PodAffinityTerm_](api-reference.md#podaffinityterm) |             |         |            |
