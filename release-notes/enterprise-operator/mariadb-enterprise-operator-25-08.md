# MariaDB Enterprise Operator 25.08

**Release date**: 26 August 2025

We are excited to announce release of **MariaDB Enterprise Operator 25.08** - delivering enterprise-grade automation for managing MariaDB Enterprise workloads on Kubernetes and Red Hat OpenShift.

This enterprise version is based on the [25.8.3 Community release](https://github.com/mariadb-operator/mariadb-operator/releases/tag/25.8.3), adding support for non-blocking Physical Backups and the IBM Power (ppc64le) architecture among other enterprise-focused enhancements.

### Non-Blocking Physical Backups

 With the Enterprise Operator, we extend physical backups via mariadb-backup and Volume Snapshots available in Community version with support for non-blocking physical backups. By leveraging [MariaDB’s BACKUP STAGE](https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage) feature, backups are taken without long read locks or service interruptions. This enables consistent, production-grade backups with minimal impact on running workloads, ideal for high-availability and performance-sensitive environments.


### IBM Power (ppc64le) architecture support

We’ve added support for the ppc64le architecture for Enterprise Operator, enabling deployment and management of containerized MariaDB Enterprise Server and MaxScale on IBM Power systems, including certified images with Red Hat OpenShift for ppc64le. This enhancement allows teams to standardize Kubernetes-based database operations across diverse infrastructures, including amd64, arm64, and ppc64le environments.

### Compatibility with CNCF-Certified Kubernetes Distributions

We are extending our engineering policy to support the three latest Kubernetes versions across all [CNCF-certified Kubernetes distributions](https://www.cncf.io/training/certification/software-conformance/). While validation is performed on upstream Kubernetes, support extends to certified container platforms based on CNCF conformance, including Amazon EKS, Google Kubernetes Engine (GKE), Azure Kubernetes Service (AKS), VMware Tanzu Kubernetes Grid, and other CNCF-certified distributions. Infrastructure-related issues, such as misconfigured Kubernetes clusters or problems with CSI (storage) or CNI (network) drivers, remain outside the scope of support.

### Validation with OpenShift 4.16 EUS version

The Enterprise Operator is now validated with OpenShift 4.16, in addition to the currently available 4.18 version. This update ensures compatibility with the two most recent OpenShift Extended Update Support (EUS) versions, allowing platform teams to deploy and manage MariaDB Enterprise Server and MaxScale while staying aligned with Red Hat’s recommended upgrade path.

### Platform and component versions

The current release has been tested with the following versions:

| Platform/Component        | Version  |
| ------------------------- | -------- |
| Kubernetes                | 1.33     |
| OpenShift                 | 4.18.6, 4.16.4 |
| MariaDB Enterprise Server | 11.4.7-4 |
| MaxScale                  | 25.01.3-1 |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
