---
description: >-
  Step-by-step guide for updating MariaDB Enterprise Kubernetes Operator to
  26.10 LTS from a previous version.
---

# 26.10 LTS update guide

This guide illustrates, step by step, how to update to `26.10.0` from `26.6.7`. If you are updating from a version prior to `26.6.x`, follow the [26.06 update guide](update-26.06.md) and the update guides of the `26.6.x` patch releases first, and apply the changes described there before continuing with this one.

{% hint style="warning" %}
**MaxScale 26.10 requires a license to start.** Before creating a `MaxScale` that uses the `26.10` image, or updating an existing one to it, make a license available: either set `spec.licenseSecretKeyRef` in the `MaxScale`, or create the default license Secret that the operator uses when it is not set. Refer to the [MaxScale licensing documentation](../topologies/maxscale.md#licensing).

Existing `MaxScale` resources keep the image they already use, so updating the operator does not require a license by itself.
{% endhint %}

{% hint style="info" %}
**Updating the** [**data-plane**](../topologies/data-plane.md) **to `26.10.0` is optional, except for the following features, which are ignored by an older data-plane:**

* **Galera pods are not restarted during long SSTs**: the agent liveness probe change only takes effect once the data-plane is updated.
* **TLS client certificate authentication** (`spec.tls.clientAuth`), which is only available for new `MariaDB` resources.

If you do not need them, you may leave `updateStrategy.autoUpdateDataPlane` set to `false` (the default) and keep your current data-plane version, avoiding a rolling update of your `MariaDB` instances.
{% endhint %}

{% hint style="info" %}
**If you are updating from a version prior to `26.6.7`, every `MaxScale` receives one monitor update when the operator is updated.** Automatic failover is paused for a few monitor ticks while it is applied. No switchover and no rolling update are triggered.
{% endhint %}

- If you prefer to keep the data-plane aligned with the operator version, set `updateStrategy.autoUpdateDataPlane=true` in your `MariaDB` resources before updating the operator. Then, once updated, the operator will also update the data-plane based on its version. Bear in mind that this triggers a rolling update of your `MariaDB` instances:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
  updateStrategy:
+   autoUpdateDataPlane: true
```

- Then, the CRDs must be updated to `26.10.0`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 26.10.0
```

- **Helm values changes**: the default images are now MariaDB Enterprise Server `12.3.3-1` (`config.mariadbDefaultVersion` is `12.3`) and MaxScale `26.10.0`. If you set `config.mariadbImage` or `config.maxscaleImage` explicitly in your `values.yaml`, your values are kept. The new `config.enterpriseLicenseKeyRef` value references the default MaxScale license Secret (`enterprise-license-key`, key `license`), and `fips.enabled` / `fips.strict` run the operator in FIPS mode.

- At this point, the operator can be updated to `26.10.0`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.10.0
```

- If you enabled `updateStrategy.autoUpdateDataPlane`, wait until the data-plane update has completed: all `MariaDB` Pods must be ready and the `MariaDB` resources must report the `Ready` condition before proceeding.

- Consider reverting `updateStrategy.autoUpdateDataPlane` back to `false` in your `MariaDB` objects to avoid unexpected updates:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
  updateStrategy:
-   autoUpdateDataPlane: true
+   autoUpdateDataPlane: false
```

## Updating to MariaDB Enterprise Server 12.3

Updating the operator does not change the image of your existing `MariaDB` resources. To move them to MariaDB Enterprise Server 12.3, set `updateStrategy.mariadbAutoUpgradeEnabled` to `true` **before** bumping `spec.image`, so that `mariadb-upgrade` runs when the Pods start and migrates the system schema:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
+ image: docker.mariadb.com/enterprise-server:12.3.3-1
  updateStrategy:
+   mariadbAutoUpgradeEnabled: true
```

Refer to the [MariaDB upgrade documentation](https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/upgrading/upgrading-from-to-specific-versions/upgrading-from-mariadb-11-8-to-mariadb-12-3) for the upgrade path from 11.8 to 12.3. A replica upgraded to 12.3 resets the `master_use_gtid` setting of its replication connection to the default ([MDEV-39788](https://jira.mariadb.org/browse/MDEV-39788)): check it after the upgrade if you rely on it.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
