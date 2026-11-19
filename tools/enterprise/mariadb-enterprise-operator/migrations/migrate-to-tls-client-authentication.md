---
description: >-
  Migrate a password-based MariaDB to a new instance with TLS client
  certificate authentication, using a logical backup.
---

# Migrate a password-based MariaDB to TLS client authentication

`spec.tls.clientAuth` is immutable: it cannot be enabled on an existing `MariaDB`. This guide migrates the data of a password-based `MariaDB` into a **new** `MariaDB` that has [TLS client certificate authentication](../security/tls-client-authentication.md) enabled, using a [logical backup](../backup-and-restore/logical_backup.md) and [`bootstrapFrom`](../backup-and-restore/logical_backup.md#bootstrap-new-mariadb-instances). The new instance is created next to the old one, so you can verify it before switching your applications and keep the old one as a rollback.

{% hint style="warning" %}
This is a migration with downtime: writes performed on the old instance after the backup is taken are not copied. Stop your writers before taking the backup, and switch them to the new instance once it has been verified.
{% endhint %}

## Before you start

- The new `MariaDB` must have TLS enabled (`spec.tls.enabled: true`) and **no** `spec.rootPasswordSecretKeyRef`. Root will authenticate with the client certificate only.
- **The backup must set `ignoreGlobalPriv: true`.** The default is `false` for non-Galera instances, which includes `mysql.global_priv` in the dump. Restoring it overwrites the `root` account of the new instance with the one of the old instance (password, no certificate requirement). Once the server reloads its privileges (e.g. after a Pod restart), the operator can no longer connect and the `MariaDB` never becomes ready. Galera backups already ignore this table by default.
- Because `mysql.global_priv` is not restored, **accounts are not migrated**. Accounts managed by `User` and `Grant` resources, and the one declared in `spec.username`, are created again by the operator. Any account created manually with SQL must be recreated.
- Accounts that keep a password (your applications) are not affected by `clientAuth`: it only changes how the operator, `root` and the operator-managed users (replication, metrics, MaxScale) authenticate.

## Step 1: Take a backup of the old instance

Stop your writers and create a `Backup` that ignores the privilege table:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Backup
metadata:
  name: backup-migration
spec:
  mariaDbRef:
    name: mariadb
  ignoreGlobalPriv: true
  storage:
    persistentVolumeClaim:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
```

Wait for it to complete:

```bash
kubectl wait --for=condition=complete backup/backup-migration --timeout=10m
```

Any [storage type](../backup-and-restore/logical_backup.md#storage-types) is valid, such as S3. The new `MariaDB` must be able to read it.

## Step 2: Create the new MariaDB

Use a new name for the `MariaDB`. If you reuse the name of the old instance, delete the old `MariaDB` **and its data PVC** (`storage-<name>-0`, and one per replica) first: a reused PVC keeps the old password-based data and the new instance never initializes `clientAuth`.

Create a `MariaDB` with `clientAuth` enabled that bootstraps from the backup. Keep the rest of the spec equivalent to the old instance (replication, Galera, MaxScale, storage, resources...), but drop `rootPasswordSecretKeyRef`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-clientauth
spec:
  storage:
    size: 1Gi
  tls:
    enabled: true
    clientAuth:
      enabled: true
  bootstrapFrom:
    backupRef:
      name: backup-migration
```

For a replication topology, add `replicas` and `replication.enabled` as usual. The operator restores the backup in the primary, and the replicas catch up through replication.

```bash
kubectl wait --for=condition=ready mariadb/mariadb-clientauth --timeout=10m
```

## Step 3: Recreate your accounts

Declare every account of your old instance as a `User` and a `Grant` pointing to the new `MariaDB` (`spec.mariaDbRef.name`), reusing the same password `Secrets` so your applications keep their credentials. This includes the account of `spec.username`, if you used it in the old instance: define it as a `User` and `Grant` instead.

`mariaDbRef` is immutable. If the new instance is in the same namespace as the old one, create the resources with a new `metadata.name` and keep the account name with `spec.name`. For an `app` account with all the privileges on the `shop` database:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: mariadb-clientauth-app
spec:
  mariaDbRef:
    name: mariadb-clientauth
  name: app
  passwordSecretKeyRef:
    name: app
    key: password
  maxUserConnections: 20
  host: "%"
---
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Grant
metadata:
  name: mariadb-clientauth-app
spec:
  mariaDbRef:
    name: mariadb-clientauth
  privileges:
    - ALL PRIVILEGES
  database: shop
  table: "*"
  username: app
  host: "%"
```

The databases, tables, views and routines come with the backup, so no `Database` resource is needed.

Accounts created manually with SQL in the old instance must be recreated by hand, or adopted as `User` and `Grant` resources.

{% hint style="warning" %}
Views, routines, triggers and events keep the account that created them as their `DEFINER`. Querying a view whose definer does not exist fails with `ERROR 1446 (HY000): The user specified as a definer ('app'@'%') does not exist`. Recreate those accounts before using the objects. To list the definers, run in the new instance:

`SELECT table_schema, table_name, definer FROM information_schema.views WHERE definer NOT IN (SELECT CONCAT(user, '@', host) FROM mysql.user)`

and the same with `information_schema.routines`, `information_schema.triggers` and `information_schema.events`.
{% endhint %}

### Remove orphaned grants

The restore brings back the `mysql.db`, `mysql.tables_priv` and similar grant tables, even if the accounts they refer to were not restored. A grant row whose account no longer exists is applied again if an account with the same name is created later. List them using the client certificate, from the `mariadb` container of the new instance:

```bash
kubectl exec mariadb-clientauth-0 -c mariadb -- mariadb -u root -h 127.0.0.1 \
  --ssl-cert=/etc/pki/client.crt --ssl-key=/etc/pki/client.key --ssl-ca=/etc/pki/ca.crt \
  -e "SELECT d.host, d.db, d.user FROM mysql.db d LEFT JOIN mysql.user u ON u.user = d.user AND u.host = d.host WHERE u.user IS NULL"
```

Delete the rows that are not expected, then run `FLUSH PRIVILEGES`. Check `mysql.tables_priv`, `mysql.columns_priv` and `mysql.procs_priv` in the same way.

## Step 4: Verify

- The `MariaDB` is ready and survives a Pod restart, as the privileges are loaded again from the restored data:

  ```bash
  kubectl delete pod mariadb-clientauth-0
  kubectl wait --for=condition=ready mariadb/mariadb-clientauth --timeout=5m
  ```

- Your data is there. Compare row counts, views and routines with the old instance.
- `root` requires the certificate: `SELECT user, host, ssl_type, x509_subject FROM mysql.user WHERE user = 'root'` returns `SPECIFIED` and `/CN=<mariadb-name>-client` for `root@%`.
- Your applications can connect with their password over TLS.

## Step 5: Switch your applications

Point your applications to the new instance (for example, through the `Connection` resources or the new `Services`), start your writers, and keep the old instance until you are confident, so you can roll back. Then delete it and its backup:

```bash
kubectl delete mariadb mariadb
kubectl delete backup backup-migration
```

## Alternative: replicate from the old instance

The logical backup of this guide is the official way to migrate. If the downtime of the backup and the restore is too long for your data size, you can load a consistent snapshot in the new instance and replicate from the old one until the cutover, which only needs a short window in which the writes are stopped.

This is not a feature of the operator: it is a reference script that you can adapt to your own environment and requirements. Have a look at the `migrate-to-client-auth-replication` folder of the [examples catalog](../examples-catalog.md), which contains the manifests of an old password-based `MariaDB` and a new `clientAuth` one, and a script that loads the snapshot, replicates from the old instance with a dedicated `REPLICATION SLAVE` user, and performs the cutover.

Consider the following before adapting it:

- The old instance needs the binary log enabled and a `server_id` different to the new one, which requires a restart of the old instance.
- Account statements of the old instance (`CREATE USER`, `GRANT`...) must not be replicated, as they would overwrite `root` in the new instance. The script filters them for the replication connection.
- Accounts are not migrated: declare them as `User` and `Grant` resources in the new instance, as in [Step 3](#step-3-recreate-your-accounts).
- It has been tried with a standalone `MariaDB`. Replication and Galera topologies, and the number of writes during the cutover of a production workload, need to be validated in your environment.

## Troubleshooting

If the new instance's Pod keeps restarting with `Startup probe failed: ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)` before any restore starts, it reused the data PVC of the old instance (for example, when the new `MariaDB` has the same name and `storage-<name>-0` was not deleted). The old data directory already has a root password, so the `clientAuth` initialization is skipped. Delete the new `MariaDB` and its PVCs, make sure `kubectl get pvc` no longer lists them, and apply it again.

If the new instance never becomes ready after the restore and the operator logs `Access denied for user 'root'@... (using password: NO)`, the backup included `mysql.global_priv` (`ignoreGlobalPriv` was not `true`). The instance cannot be repaired from the operator: delete the `MariaDB` and its PVCs, take a new backup with `ignoreGlobalPriv: true`, and start again from Step 2.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
