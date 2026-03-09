# General Upgrade Information

While specific guides exist for upgrading between individual versions, it is important to understand the general policies regarding skipping versions and upgrading clusters.

### Direct Upgrade Policy

Historically, upgrading MariaDB Community Server required stepping through each major version individually. However, for modern versions, **you can upgrade directly from your current version to the latest target version** in most scenarios.

* **Skip Intermediate Versions:** Skipping intermediate major or LTS versions is fully supported and tested for standalone servers.
* **Check Incompatible Changes:** Even when skipping versions, you **must** review the "Incompatible Changes" section for _every_ major version between your current version and your target version. This ensures your application does not rely on functionality, configuration, or reserved keywords that have been deprecated or modified in the interim.
* **Troubleshooting:** If you are unsure about your application's compatibility, upgrading one major/LTS version at a time is recommended. This incremental approach makes it easier to isolate the specific version that introduces a breaking change or application issue.

### Galera Cluster Upgrades

The upgrade strategy for Galera Clusters differs depending on whether you require zero downtime.

#### Rolling Upgrades

If you are performing a rolling upgrade to keep the cluster online:

* You **must upgrade one major/LTS version at a time**.
* Due to the complexity of intra-node communication, skipping versions during a rolling upgrade is not supported.
* This process requires multiple upgrade cycles, but the cluster remains available to applications throughout.

#### Full Cluster Shutdown

If you can schedule downtime for the entire cluster:

* You may shut down all nodes, upgrade them all to the target version, and then bring the cluster back up.
* In this scenario, a **direct upgrade** (skipping intermediate versions) is supported, similar to a standalone server.
