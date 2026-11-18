---
description: >-
  Install MariaDB on Kubernetes with the independent, Apache-2.0-licensed
  HelmForge community Helm chart and the official MariaDB container image.
---

# HelmForge Community Helm Chart for MariaDB

[HelmForge](https://helmforge.dev/) maintains an Apache-2.0-licensed community Helm chart for deploying MariaDB on Kubernetes. The chart uses the official [`mariadb` container image](https://hub.docker.com/_/mariadb) and supports standalone deployments and asynchronous, GTID-based replication with one source and read replicas.

HelmForge is an independent community project. It is not developed or supported by MariaDB plc or the MariaDB Foundation. Report chart issues in the [HelmForge charts repository](https://github.com/helmforgedev/charts/issues).

## Install the Chart

Add the HelmForge repository and install the chart:

```bash
helm repo add helmforge https://repo.helmforge.dev
helm repo update
helm install mariadb helmforge/mariadb
```

The default installation creates a standalone MariaDB instance with persistent storage. To install a source with read replicas, set `architecture: replication`. The chart creates two read replicas by default. To change the number, set `replication.readReplicas.replicaCount` in a values file such as:

```yaml
architecture: replication

replication:
  readReplicas:
    replicaCount: 3
```

```bash
helm install mariadb helmforge/mariadb --values values.yaml
```

## Before Using the Chart in Production

Review the chart values and test the configuration in an environment that matches the target cluster. In particular, plan and validate persistent storage, backup and restore, upgrades, credentials, network access, and disruption behavior. Replication improves availability for some failure scenarios, but it does not replace backups.

See the [HelmForge MariaDB chart documentation](https://helmforge.dev/docs/charts/mariadb) for configuration details. The [chart source](https://github.com/helmforgedev/charts/tree/main/charts/mariadb) includes its templates, default values, and tests. Chart versions are published as [GitHub releases](https://github.com/helmforgedev/charts/releases).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
