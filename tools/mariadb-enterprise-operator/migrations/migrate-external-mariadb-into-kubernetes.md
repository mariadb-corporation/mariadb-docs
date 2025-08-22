
# Migrate external MariaDB into Kubernetes

In this guide, we will be migrating an external MariaDB into a new `MariaDB` instance running in Kubernetes and managed by MariaDB Enterprise Operator. We will be using [logical backups](../backup-and-restore/logical_backup.md) for achieving this migration.

{% hint style="info" %}
Ensure you understand the [key considerations and limitations of the Backup and Restore resources](../backup-and-restore/logical_backup.md#important-considerations-and-limitations) in the MariaDB Enterprise Operator.
{% endhint %}

**1.** Take a logical backup of your external MariaDB using one of the commands below:

```sh
mariadb-dump --user=${MARIADB_USER} --password=${MARIADB_PASSWORD} --host=${MARIADB_HOST} --single-transaction --events --routines --all-databases > backup.2024-08-26T12:24:34Z.sql
```

If you are currently using or migrating to a Galera instance, use the following command instead:

```sh
mariadb-dump --user=${MARIADB_USER} --password=${MARIADB_PASSWORD} --host=${MARIADB_HOST} --single-transaction --events --routines --all-databases --skip-add-locks --ignore-table=mysql.global_priv > backup.2024-08-26T12:24:34Z.sql
```

**2.** Ensure that your backup file matches the following format: `backup.2024-08-26T12:24:34Z.sql`. If the file name does not follow this format, it will be ignored by the operator.

**3.** Upload the backup file to one of the supported [storage types](../backup-and-restore/logical_backup.md#storage-types). We recommend using S3.

**4.** Create your `MariaDB` resource declaring that you want to [bootstrap from the previous backup](../backup-and-restore/logical_backup.md#bootstrap-new-mariadb-instances) and providing a [root password Secret](../backup-and-restore/logical_backup.md#root-credentials) that matches the backup:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  rootPasswordSecretKeyRef:
    name: mariadb
    key: root-password
  replicas: 3
  galera:
    enabled: true
  storage:
    size: 1Gi
  bootstrapFrom:
    s3:
      bucket: backups
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
          key: tls.crt
    targetRecoveryTime: 2024-08-26T12:24:34Z
```

**5.** If you are using Galera in your new instance, migrate your previous users and grants to use the `User` and `Grant` CRs. Refer to the [SQL resource documentation](../sql-resources.md) for further detail.


{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}


{% @marketo/form formId="4316" %}
