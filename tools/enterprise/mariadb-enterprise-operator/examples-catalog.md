---
description: >-
  A collection of YAML manifests and configuration examples for various common
  deployment scenarios and resource management tasks.
---

# Examples Catalog

The [examples catalog](https://operator.mariadb.com/examples/manifests.tar.gz) contains a number of sample manifests that aim to show the operator functionality in a practical way. Follow these instructions for getting started:

* Download the [examples catalog](https://operator.mariadb.com/examples/manifests.tar.gz):

```sh
curl -sLO https://operator.mariadb.com/examples/manifests.tar.gz
mkdir -p examples
tar -xzf manifests.tar.gz -C examples
```

* Install the configuration shared by all the examples:

```sh
kubectl apply -f examples/config
```

* Start deploying examples:

```sh
kubectl apply -f examples/mariadb.yaml
```

Some examples rely on external dependencies for specific tasks, make sure to install them when it applies:

* [prometheus-operator](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) for metrics
* [cert-manager](https://cert-manager.io/docs/installation/helm/) for TLS certificates
* [minio](https://github.com/minio/minio/tree/master/helm/minio) for S3 object storage

It is recommended to complement the examples with the [API reference](api-reference.md) documentation to understand the full range of configuration options available.

If you are looking for production-grade examples, you can check the following manifests:

* `mariadb_replication_production.yaml` and `maxscale_replication_production.yaml` for [asynchronous replication](topologies/replication.md)
* `mariadb_galera_production.yaml` and `maxscale_galera_production.yaml` for [Galera](topologies/galera.md)

For [TLS client certificate authentication](security/tls-client-authentication.md), you can check the following manifests:

* `mariadb_replication_client_tls.yaml` and `maxscale_replication_client_tls.yaml`: a replication `MariaDB` and its `MaxScale` that authenticate with TLS client certificates instead of passwords.
* `mariadb_galera_client_tls.yaml`: a Galera `MariaDB` with TLS client certificate authentication, including the SST settings it requires.
* `user_client_certificate.yaml`: a `User` with a dedicated TLS client certificate issued by the operator.
* `migrate-to-client-auth/`: step-by-step manifests to migrate a password-based `MariaDB` to TLS client certificate authentication through a logical backup, as described in the [migration guide](migrations/migrate-to-tls-client-authentication.md).
* `migrate-to-client-auth-replication/`: manifests and a script to migrate with a shorter downtime, by replicating from the old instance until the cutover.

For restoring and backing up large datasets, check the following manifests, which use long timeouts and large volumes:

* `physicalbackup_pvc_large.yaml` and `physicalbackup_volumesnapshot_large.yaml`: [physical backups](backup-and-restore/physical_backup.md) to a PVC and to a `VolumeSnapshot`, with long timeouts.
* `mariadb_galera_from_physicalbackup_large.yaml` and `mariadb_galera_from_volumesnapshot_large.yaml`: Galera clusters bootstrapped from a physical backup and from a `VolumeSnapshot`.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}