---
description: >-
  MariaDB Enterprise Operator 26.10 is a Stable (GA) release of MariaDB
  Enterprise Operator, released on 2026-11-03
---

# MariaDB Enterprise Kubernetes Operator 26.10

**Release date**: 3 November 2026

Release 26.10 is a GA release.

This document describes the changes in release 26.10, when compared to release 26.06.

If you are updating from a previous version, **please follow the** [**UPDATE GUIDE**](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/updates/update-26.10) to ensure a safe transition.

For any problems you encounter, please consider submitting a bug report on [our Jira](https://jira.mariadb.org/projects/K8SDKR).

## Long-Term Support (LTS) Release

Release 26.10 is an annual Long-Term Support (LTS) release of the Enterprise Kubernetes Operator, which provides long-term stability and a predictable upgrade path. LTS releases focus on security updates and critical bug fixes and maintain CRD compatibility within the LTS release. New features continue to ship in the rolling releases between LTS cycles.

Please refer to the [OpenShift](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/installation/openshift#release-channels) and [Helm](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/installation/helm#long-term-support-versions) documentation to start using LTS releases.

## Changed Features

### [K8SDKR-257](https://jira.mariadb.org/browse/K8SDKR-257) / [K8SDKR-259](https://jira.mariadb.org/browse/K8SDKR-259) New default images

The operator now defaults to MariaDB Enterprise Server `12.3` (`config.mariadbDefaultVersion`, image `12.3.3-0`) and to MaxScale `26.10.0`. Existing `MariaDB` and `MaxScale` resources keep the image they already use.

### [K8SDKR-341](https://jira.mariadb.org/browse/K8SDKR-341) Updated license terms

The license terms bundled with the operator have been updated to the version dated 16 October 2026.

## New Features

### [K8SDKR-257](https://jira.mariadb.org/browse/K8SDKR-257) Support for MariaDB Enterprise Server 12.3

MariaDB Enterprise Server 12.3 is now supported. Three changes in the operator are tied to it:

* `spec.updateStrategy.mariadbAutoUpgradeEnabled` runs `mariadb-upgrade` when the Pods start, so the system schema is migrated when `spec.image` crosses a major version. It defaults to `false`: set it to `true` before bumping `spec.image` to a new major version.
* The multi-cluster switchover no longer fails on 12.3 with `Error 4243`: the replicas are stopped and their `Binlog Dump` threads killed on the promoted primary before `RESET MASTER` is issued.
* A replica that was stopped on purpose, with no replication error, is no longer restarted by the agent liveness probe.

### [K8SDKR-259](https://jira.mariadb.org/browse/K8SDKR-259) Support for MaxScale 26.10 and MaxScale licensing

MaxScale 26.10 requires a license key (`license_key`) to start. The license is resolved from `spec.licenseSecretKeyRef` of the `MaxScale` and, when it is not set, from the operator-level default configured with the `config.enterpriseLicenseKeyRef` Helm value (a Secret named `enterprise-license-key` with a `license` key, in the operator namespace). When a `MaxScale` that needs a license cannot resolve one, the operator emits a `MaxScaleLicenseNotFound` event and sets the `Ready` condition to `False`, instead of letting MaxScale fail to start. An event is also emitted when the license is expired.

The license is part of the static MaxScale configuration, so rotating it rolls the `MaxScale` Pods following `spec.updateStrategy`. Only the Secret referenced by `spec.licenseSecretKeyRef` is watched: the change in the default license Secret is picked up on the next reconciliation of each `MaxScale`.

Refer to the [MaxScale licensing documentation](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/topologies/maxscale#licensing) for more details.

### [K8SDKR-240](https://jira.mariadb.org/browse/K8SDKR-240) TLS client certificate authentication (FIPS 140-3, phase 2)

The operator and the components it manages can now authenticate with TLS client certificates instead of passwords, which is required in environments that enforce strict FIPS 140-3 (`GODEBUG=fips140=only`) and rules out password-based authentication. It is enabled with `spec.tls.clientAuth.enabled` on the `MariaDB` and is disabled by default.

When it is enabled:

* The `root` user is bootstrapped without a password, with a `REQUIRE SUBJECT` / `ISSUER` requirement that can be set in `spec.tls.clientAuth.rootTLSRequirements`. The other operator users take `spec.tls.clientAuth.tlsRequirements`.
* Replication, logical and physical backups, point-in-time recovery, `bootstrapFrom`, the metrics exporter, Galera, including its SST, and MaxScale authenticate with the client certificate, so no password is needed.
* `User` resources can get their own client certificate, issued by the operator, with `spec.clientCertificate`.
* The operator itself can run in FIPS mode with the new `fips.enabled` and `fips.strict` Helm values.

`spec.tls.clientAuth` is immutable: to move an existing `MariaDB` to this mode, follow the [migration guide](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/migrations/migrate-to-tls-client-authentication). It is not supported with multi-cluster, `ExternalMariaDB` or the arbitrator, and it requires MaxScale 25.10.4 or later.

Refer to the [TLS client certificate authentication documentation](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/security/tls-client-authentication) for more details.

### [K8SDKR-287](https://jira.mariadb.org/browse/K8SDKR-287) Arbitrator for two node replication clusters (Public Preview)

{% hint style="info" %}
The arbitrator is available as a **Public Preview**.
{% endhint %}

A replication cluster with one primary and one replica can now keep both split-brain safety and failover liveness. Enabling `spec.arbitrator` provisions a third, dataless MariaDB instance that holds a cooperative monitoring lock, so MaxScale needs 2 of 3 locks to fail over. The arbitrator takes no part in replication, serves no traffic and is never a failover target, backup source or bootstrap donor.

Refer to the [arbitrator documentation](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/topologies/arbitrator) for more details.

### [K8SDKR-285](https://jira.mariadb.org/browse/K8SDKR-285) Galera Pods are not restarted during long SSTs

While a Galera Pod receives an SST, `mysqld` does not accept connections, so the liveness probe failed and the kubelet restarted the Pod, which restarted the transfer from scratch. The agent liveness probe now succeeds for as long as an SST is in progress in the Pod. The readiness probe is unchanged: the Pod stays out of the `Services` until it is `Synced`. This requires the [data-plane](https://mariadb.com/docs/tools/enterprise/mariadb-enterprise-operator/topologies/data-plane) to be updated to 26.10.

New examples cover physical backups and restores of large Galera datasets, from a PVC, S3 or a `VolumeSnapshot`.

## Bug fixes

* [K8SDKR-331](https://jira.mariadb.org/browse/K8SDKR-331) A node that rejoins as a replica after being a primary no longer fails with `Error 4191` when it replicates using `Current_Pos`: `MASTER_USE_GTID=slave_pos` is now set together with `MASTER_DEMOTE_TO_SLAVE=1`.

## Known Issues and Limitations

* The arbitrator is only available for replication. It is not supported with TLS client certificate authentication.
* TLS client certificate authentication is not supported with multi-cluster and `ExternalMariaDB`.
* With TLS client certificate authentication, Galera requires `spec.tls.galeraSSTEnabled: true` and does not support the `mysqldump` SST.

## Platform and component versions

The current release has been tested with the following versions:

| Platform/Component        | Version    |
| ------------------------- | ---------- |
| Kubernetes                | 1.36       |
| OpenShift                 | 4.20       |
| MariaDB Enterprise Server | 12.3.3-0   |
| MaxScale                  | 26.10.0    |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
