---
description: >-
  MariaDB Enterprise Kubernetes Operator 26.10.0 is a Stable (GA) release of
  the 26.10 (LTS) line, released on 2026-11-03
---

# MariaDB Enterprise Kubernetes Operator 26.10.0 (LTS) Release Notes

MariaDB Enterprise Kubernetes Operator 26.10.0 is a Stable (GA) release of the 26.10 (LTS) line, released on 2026-11-03.

**Release Date**: 03 November 2026

Release 26.10.0 is a GA release.

Release 26.10 is a Long-Term Support (LTS) release. To start using LTS releases, refer to the [OpenShift](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/installation/openshift#release-channels) and [Helm](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/installation/helm#long-term-support-versions) documentation.

If you are updating from a previous version, **please follow the** [**UPDATE GUIDE**](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/updates/update-26.10) to ensure a safe transition.

## New Features

### Two-node semi-synchronous replication with an arbitrator (Public Preview)

Two-node replication clusters can now add an operator-managed arbitrator. The arbitrator is a lightweight MariaDB instance that holds no data and serves no traffic, and it gives MaxScale the third vote needed for a majority. This protects the cluster against split-brain while keeping automatic failover available when one data node is down, without the cost of a third database node. Requires MaxScale 26.10. [Learn more](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/topologies/replication#two-node-clusters)

### Semi-sync stall detection for replication primaries

When semi-synchronous replication is configured never to fall back to asynchronous mode, losing the replica can leave the primary unable to complete writes while still reporting healthy. A new opt-in setting lets the operator detect this condition, restart the affected server, and surface it through events, conditions and metrics. [Learn more](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/topologies/replication#asynchronous-vs-semi-synchronous-replication)

### Certificate-based authentication for FIPS deployments

MariaDB Enterprise Server, MaxScale and the metrics exporters can now authenticate with TLS client certificates instead of passwords. This keeps authentication within the FIPS-validated cryptographic module and supports FedRAMP High requirements. [Learn more](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/security/tls-client-authentication)

### Support for MariaDB Enterprise Server 12.3 and MaxScale 26.10

The operator supports the GA releases of MariaDB Enterprise Server 12.3 and MaxScale 26.10 as part of the 2026 Enterprise Platform launch, and now defaults to them for new `MariaDB` and `MaxScale` resources. Existing resources keep the image they already use. MaxScale 26.10 requires a license key, which is set per `MaxScale` or as an operator-wide default. When upgrading `spec.image` across a major Enterprise Server version, enable `spec.updateStrategy.mariadbAutoUpgradeEnabled` so that `mariadb-upgrade` runs on startup. [Learn more](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/topologies/maxscale#licensing)

## Bug Fixes

* [K8SDKR-280](https://jira.mariadb.org/browse/K8SDKR-280): Physical backup restores of large Galera clusters are no longer interrupted by big restores.
* [K8SDKR-285](https://jira.mariadb.org/browse/K8SDKR-285): The liveness probe no longer restarts a Galera Pod that is receiving a long SST, which restarted the transfer from scratch. This requires the [data-plane](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/topologies/data-plane) to be updated to 26.10.
* [K8SDKR-331](https://jira.mariadb.org/browse/K8SDKR-331): A node that rejoins as a replica after being a primary no longer fails with `Error 4191` when it replicates using `Current_Pos`.

## Known Issues and Limitations

* The arbitrator is only available for replication. It is not supported with TLS client certificate authentication.
* TLS client certificate authentication is not supported with multi-cluster and `ExternalMariaDB`.
* With TLS client certificate authentication, Galera requires `spec.tls.galeraSSTEnabled: true` and does not support the `mysqldump` SST.

## Platform and component versions

The current release has been tested with the following versions:

| Platform/Component        | Version          |
| ------------------------- | ---------------- |
| Kubernetes                | 1.36             |
| OpenShift                 | 4.18, 4.20, 4.22 |
| MariaDB Enterprise Server | 12.3.3-1         |
| MaxScale                  | 26.10.0          |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}