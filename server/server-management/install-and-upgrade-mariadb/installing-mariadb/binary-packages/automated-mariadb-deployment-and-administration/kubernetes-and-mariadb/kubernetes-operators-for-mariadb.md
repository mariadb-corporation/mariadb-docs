# Kubernetes Operators for MariaDB

Operators basically instruct Kubernetes about how to manage a certain technology. Kubernetes comes with some default operators, but it is possible to create custom operators. Operators created by the community can be found on [OperatorHub.io](https://operatorhub.io/).

## Custom Operators

Kubernetes provides a declarative API. To support a specific (i.e. MariaDB) technology or implement a desired behavior (i.e. provisioning a [replica](../../../../../../ha-and-performance/standard-replication/)), we extend Kubernetes API. This involves creating two main components:

* A custom resource.
* A custom controller.

A custom resource adds an API endpoint, so the resource can be managed via the API server. It includes functionality to get information about the resource, like a list of the existing servers.

A custom controller implements the checks that must be performed against the resource to check if its state should be corrected using the API. In the case of MariaDB, some reasonable checks would be verifying that it accepts connections, replication is running, and a server is (or is not) read only.

## MariaDB Enterprise Operator

MariaDB Enterprise Operator provides a seamless way to run and operate containerized versions of MariaDB Enterprise Server and MaxScale on Kubernetes, allowing you to leverage Kubernetes orchestration and automation capabilities. This document outlines the features and advantages of using Kubernetes and the MariaDB Enterprise Operator to streamline the deployment and management of MariaDB and MaxScale instances.

{% hint style="success" %}
Find the [documentation here](https://app.gitbook.com/s/kuTXWg0NDbRx6XUeYpGD/mariadb-enterprise-operator).
{% endhint %}

## MariaDB Community Operator

[mariadb-operator](https://github.com/mariadb-operator/mariadb-operator) is a Kubernetes operator that allows you to run and operate MariaDB in a cloud native way. It aims to declaratively manage MariaDB instances using Kubernetes CRDs instead of imperative commands.

It's available in both [Artifact Hub](https://artifacthub.io/packages/helm/mariadb-operator/mariadb-operator) and [Operator Hub](https://operatorhub.io/operator/mariadb-operator) and supports the following features:

* [Easily provision](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/mariadb_minimal.yaml) and [configure](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/mariadb_full.yaml) MariaDB servers in Kubernetes.
* Multiple [HA modes](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/high_availability.md): Galera Cluster or MariaDB Replication.
* Automated Galera [primary failover](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/high_availability.md) and [cluster recovery](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/galera.md#galera-cluster-recovery).
* Advanced HA with [MaxScale](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/maxscale.md): a sophisticated database proxy, router, and load balancer for MariaDB.
* Flexible [storage](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/storage.md) configuration. [Volume expansion](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/storage.md#volume-resize).
* [Physical backups](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/physical_backup.md) based on [mariadb-backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup) and [Kubernetes VolumeSnapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/).
* [Logical backups](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/logical_backup.md) based on [mariadb-dump](https://mariadb.com/docs/server/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump).
* Multiple [backup storage types](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/physical_backup.md#storage-types): S3 compatible, PVCs, Kubernetes volumes and `VolumeSnapshots`.
* Flexible backup configuration: [scheduling](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/physical_backup.md#scheduling), [compression](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/physical_backup.md#compression), [retention policy](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/physical_backup.md#retention-policy), [timeout](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/physical_backup.md#timeout), [staging area](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/physical_backup.md#staging-area)...
* [Target recovery time](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/physical_backup.md#target-recovery-time): restore the closest available backup to the specified time.
* [Bootstrap new instances](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/physical_backup.md#restoration) from: Physical backups, logical backups, S3, PVCs, `VolumeSnapshots`...
* [Cluster-aware rolling update](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/updates.md#replicasfirstprimarylast): roll out replica Pods one by one, wait for each of them to become ready, and then proceed with the primary Pod, using `ReplicasFirstPrimaryLast`.
* Manual [update strategies](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/updates.md#update-strategies): `OnDelete` and `Never`.
* Automated [data-plane updates](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/updates.md#auto-update-data-plane).
* [my.cnf change detection](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/configuration.md#mycnf). Automatically trigger [updates](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/updates.md) when my.cnf changes.
* [Suspend](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/suspend.md) operator reconciliation for maintenance operations.
* Issue, configure and rotate [TLS certificates](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/tls.md) and CAs.
* Native integration with [cert-manager](https://github.com/cert-manager/cert-manager). Automatically create `Certificate` resources.
* [Prometheus metrics](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/metrics.md) via [mysqld-exporter](https://github.com/prometheus/mysqld_exporter) and maxscale-exporter.
* Native integration with [prometheus-operator](https://github.com/prometheus-operator/prometheus-operator). Automatically create `ServiceMonitor` resources.
* Declaratively manage [SQL resources](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/sql_resources.md): [users](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/user.yaml), [grants](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/grant.yaml) and logical [databases](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/database.yaml).
* Declaratively manage resources in [external MariaDB instances](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/external_mariadb.md).
* Configure [connections](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/connection.yaml) for your applications.
* Orchestrate and schedule [sql scripts](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/sqljobs).
* Validation webhooks to provide CRD immutability.
* Additional printer columns to report the current CRD status.
* CRDs designed according to the Kubernetes [API conventions](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md).
* Install it using [helm](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/helm.md), [OLM](https://operatorhub.io/operator/mariadb-operator) or [static manifests](https://github.com/mariadb-operator/mariadb-operator/blob/main/deploy/manifests).
* Multiple [deployment modes](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/helm.md#deployment-modes): cluster-wide and single namespace.
* Helm chart to deploy [MariaDB clusters](https://github.com/mariadb-operator/mariadb-operator/blob/main/docs/helm.md#mariadb-cluster-helm-chart) and its associated CRs.
* Multi-arch distroless [image](https://github.com/orgs/mariadb-operator/packages/container/package/mariadb-operator).
* GitOps friendly.

Please, refer to the [documentation](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/README.md), the [API reference](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/api_reference.md) and the [example suite](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests) for further detail.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
