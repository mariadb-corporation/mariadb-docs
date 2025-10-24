---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Introduction

MariaDB Enterprise Kubernetes Operator provides a seamless way to run and operate containerized versions of MariaDB Enterprise Server and MaxScale on Kubernetes, allowing you to leverage Kubernetes orchestration and automation capabilities. This document outlines the features and advantages of using Kubernetes and the MariaDB Enterprise Kubernetes Operator to streamline the deployment and management of MariaDB and MaxScale instances.

## What is Kubernetes?

Kubernetes is more than just a container orchestrator; it is a comprehensive platform that provides APIs for managing both applications and the underlying infrastructure. It automates key aspects of container management, including deployment, scaling, and monitoring, while also handling essential infrastructure needs such as networking and storage. By unifying the management of applications and infrastructure, Kubernetes simplifies operations and improves efficiency in cloud-native environments.

## Why Kubernetes?

Kubernetes brings several key benefits to the table when managing applications in a containerized environment:

* Standardization: Kubernetes relies on standard APIs for managing applications and infrastructure, making it easier to ensure uniformity across various environments. It acts as a common denominator across cloud providers and on-premises.
* Automation: Kubernetes APIs encapsulate operational best practises, minimizing the need for manual intervention and improving the efficiency of operations.
* Cost Effectiveness: Having an standarized way to manage infrastructure across cloud providers and automation to streamline operations, Kubernetes helps reducing the infrastructure and operational costs.

## What is a Kubernetes Operator?

Kubernetes has been designed with flexibility in mind, allowing developers to extend its capabilities through custom resources and operators.

<figure><img src="../.gitbook/assets/operator-overview.png" alt=""><figcaption></figcaption></figure>

In particular, MariaDB Enterprise Kubernetes Operator, watches the desired state defined by users via `MariaDB` and `MaxScale` resources, and takes actions to ensure that the actual state of the system matches the desired state. This includes managing compute, storage and network resources, as well as the full lifecycle of the MariaDB and MaxScale instances. Whenever the desired state changes or the underlying infrastructure is modified, the Operator takes the necessary actions to reconcile the actual state with the desired state.

Operational expertise is baked into the `MariaDB` and `MaxScale` APIs and seamlessly managed by the Operator. This includes automated backups, restores, upgrades, monitoring, and other critical lifecycle tasks, ensuring reliability in Day 2 operations.

## MariaDB Enterprise Kubernetes Operator Features

* Provision and Configure MariaDB and MaxScale Declaratively: Define MariaDB Enterprise Server and MaxScale clusters in YAML manifests and deploy them with ease in Kubernetes.
* High Availability with Galera: Ensure availability with MariaDB Enterprise Cluster, providing synchronous multi-master replication.
* Query and Connection-Based Routing with MaxScale: MaxScale provides query routing and connection load balancing for improved application performance.
* Cluster-Aware Rolling Updates: Perform rolling updates on MariaDB and MaxScale clusters, ensuring zero-downtime upgrades with no disruptions to your applications.
* Flexible Storage Configuration and Volume Expansion: Easily configure storage for MariaDB instances, including the ability to expand volumes as needed.
* Physical Backups based on [mariadb-backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup) and [Kubernetes VolumeSnapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/). By leveraging the [BACKUP STAGE](https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage) feature, backups are taken without long read locks or service interruptions.
* Logical Backups based on [mariadb-dump](https://mariadb.com/docs/server/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump).
* Backup Management: Take, restore, and schedule backups with multiple storage types supported: S3, PVCs, Kubernetes volumes and VolumeSnapshots..
* Policy-Driven Backup Retention: Implement backup retention policies with bzip2 and gzip compression.
* Target Recovery Time: Restore your database to the closest available backup based on a specified recovery time.
* Bootstrap New Instances: Initialize new MariaDB instances from backups, S3, PVCs or VolumeSnapshots to quickly spin up new clusters.
* TLS Certificate Management: Issue, configure, and rotate TLS certificates and Certificate Authorities (CAs) for secure connections.
* Advanced TLS Support: customize certificate lifetime, private key algorithm and TLS version.
* Native Integration with cert-manager: Leverage [cert-manager](https://cert-manager.io/docs/), the de-facto standard for managing certificates in Kubernetes, to enable issuance with private CAs, public CAs and HashiCorp Vault.
* Prometheus Metrics: Expose metrics using the MariaDB and MaxScale Prometheus exporters.
* Native Integration with prometheus-operator: Leverage [prometheus-operator](https://github.com/prometheus-operator/prometheus-operator) to scrape metrics from MariaDB and MaxScale instances.
* Declarative User and Database Management: Manage users, grants, and logical databases in a declarative manner using Kubernetes resources.
* Secure, immutable and lightweight images based on Red Hat UBI, available for multiple architectires (amd64, arm64 and ppc64le).
* [Operator certified ](https://catalog.redhat.com/en/software/container-stacks/detail/65789bcbe17f1b31944acb1d#overview) by Red Hat.
* Manual Update Strategies: Supplementing our automated methods, you can choose `OnDelete` or `Never` to retain full manual control over Galera data plane updates.
* Automated Data Plane Updates: The operator automatically handles updates for the Galera data plane, ensuring consistency and reducing administrative burden.
* Automatic Updates On my.cnf changes: The operator automatically detects and acts on configuration changes, performing a database restart when a change in my.cnf is observed.
* Maintenance Mode: Provides the ability to suspend operator reconciliation, enabling you to perform maintenance operations without interference.
* Prometheus Integration: Native integration with the [prometheus-operator](https://github.com/prometheus-operator/prometheus-operator). Automatic creation of `ServiceMonitor` resources.
* External MariaDB Instances: Declarative management of external MariaDB instances with the operator.
* Connections: Ability to configure connections for your applications.
* SQL job scheduling: Declaratively schedule SQL scripts.
* Validation: Utilizes validation webhooks to enforce CRD immutability, ensuring configuration stability and preventing unintended changes.
* Multiple Deployment Modes: Supports flexible installation across cluster-wide and single-namespace modes.
* Asynchronous Replication: Supports asynchronous primary-replica replication for improved reading performance and high availability configurations.
* Automatic Replica Recovery: The operator includes mechanisms for the automatic recovery and re-synchronization of replica nodes following an unexpected halt or failure.
* Scale Out: Enables seamless scaling of read capacity by adding and managing new replica nodes declaratively.
* Installation: Easily deployable using Helm or through the certified operators catalog on OpenShift.
* GitOps Friendly: Designed to integrate smoothly with GitOps workflows and tools for declarative infrastructure management.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
