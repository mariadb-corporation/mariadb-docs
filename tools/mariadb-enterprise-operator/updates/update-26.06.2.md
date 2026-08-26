---
description: >-
  Step-by-step guide for updating MariaDB Enterprise Kubernetes Operator to
  26.06.2 from a previous version.
---

# 26.06.2 update guide

This guide illustrates, step by step, how to update to `26.6.2` from `26.6.1`. If you are updating from a version prior to `26.6.x`, follow the [26.06 update guide](https://mariadb.com/docs/tools/mariadb-enterprise-operator/updates/update-26.06) and the [26.06.1 update guide](https://mariadb.com/docs/tools/mariadb-enterprise-operator/updates/update-26.06.1) first, and apply the changes described there before continuing with this one.

{% hint style="info" %}
**Unlike previous releases, updating the** [**data-plane**](../topologies/data-plane.md) **to `26.6.2` is optional.** All the fixes delivered in `26.6.2` live in the operator itself, so updating the operator is enough to get all of them. You may leave `updateStrategy.autoUpdateDataPlane` set to `false` (the default) and keep your current data-plane version, avoiding a rolling update of your `MariaDB` instances.
{% endhint %}

- If you still prefer to keep the data-plane aligned with the operator version, you must set `updateStrategy.autoUpdateDataPlane=true` in your `MariaDB` resources before updating the operator. Then, once updated, the operator will also update the data-plane based on its version. Bear in mind that this triggers a rolling update of your `MariaDB` instances:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
  updateStrategy:
+   autoUpdateDataPlane: true
```

- First of all, the CRDs must be updated to `26.6.2`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 26.6.2
```

- At this point, the operator can be updated to `26.6.2`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.6.2
```

{% hint style="warning" %}
`26.6.2` fixes the `copy-agent` init container image, which is injected in `MariaDB` resources that have replication enabled and `replication.primary.autoSwitchoverOnGracefulShutdown` set to `true` (the default). It is now taken from the pinned data-plane image (`spec.replication.initContainer.image`) instead of the running operator image, so that it honors `updateStrategy.autoUpdateDataPlane` like the rest of the data-plane containers.

If the pinned data-plane image of a given `MariaDB` differs from the operator version you are updating from, this results in a **one-off rolling update** of that instance in the first reconciliation after the operator has been updated. From that point on, updating the operator no longer restarts your `MariaDB` instances unless `updateStrategy.autoUpdateDataPlane` is enabled.
{% endhint %}

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

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
