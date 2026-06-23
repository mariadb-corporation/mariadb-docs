---
description: >-
  Step-by-step guide for updating MariaDB Enterprise Kubernetes Operator to
  26.06 from a previous version.
---

# 26.06 update guide

This guide illustrates, step by step, how to update to `26.6.0` from previous versions. This guide only applies if you are updating from a version prior to `26.6.x`, otherwise you may upgrade directly (see [Helm](https://mariadb.com/docs/tools/mariadb-enterprise-operator/installation/helm#updates) docs).

- The [data-plane](../topologies/data-plane.md) must be updated to the `26.6.0` version. You must set `updateStrategy.autoUpdateDataPlane=true` in your `MariaDB` resources before updating the operator. Then, once updated, the operator will also update the data-plane based on its version:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
  updateStrategy:
+   autoUpdateDataPlane: true
```

- First of all, the CRDs must be updated to `26.6.0`:
```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 26.6.0
```

- **Switchover on Graceful Shutdown** is enabled by default in `26.6.0` If you do not want primary switchovers to happen automatically when a primary Pod is gracefully terminated, you must disable the feature on your `MariaDB` resources before updating the operator. Refer to [this migration guide](../migrations/migrate-graceful-shutdown-switchover.md) for instructions.

- **Helm values changes**: Some changes have been introduced to facilitate and standarize how the default images used by the operator are configured. In particular, `config` has been split into `repository` and `tag` to facilitate overriding the image registry. If you are setting the `config` field explicitely, you must update your `values.yaml` from:

```yaml
config:
  mariadbImageName: docker.mariadb.com/enterprise-server:11.8.6-3.2
  maxscaleImage: docker.mariadb.com/maxscale:25.10.1
  exporterImage: mariadb/mariadb-prometheus-exporter-ubi:1.2.0
  exporterMaxscaleImage: mariadb/maxscale-prometheus-exporter-ubi:1.2.0
 ```

to the following format:

```yaml
config:
  mariadbImage:
    repository: docker.mariadb.com/enterprise-server
    tag: 11.8.6-3.2
  maxscaleImage:
    repository: docker.mariadb.com/maxscale
    tag: 25.10.1
  exporterImage:
    repository: mariadb/mariadb-prometheus-exporter-ubi
    tag: 1.2.0
  exporterMaxscaleImage:
    repository: mariadb/maxscale-prometheus-exporter-ubi
    tag: 1.2.0
```

- At this point, the operator can be updated to  `26.6.0`:
```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.6.0
```

- Consider reverting `updateStrategy.autoUpdateDataPlane` back to `false` in your `MariaDB` object to avoid unexpected updates:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
  updateStrategy:
+   autoUpdateDataPlane: false
-   autoUpdateDataPlane: true
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
