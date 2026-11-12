---
description: >-
  Step-by-step guide for updating MariaDB Enterprise Kubernetes Operator to
  26.10.1 from a previous version.
---

# 26.10.1 update guide

This guide illustrates, step by step, how to update to `26.10.1` from `26.10.0`. If you are updating from a version prior to `26.10.0`, follow the [26.10 LTS update guide](update-26.10.md) first, and apply the changes described there before continuing with this one.

{% hint style="info" %}
**Updating the** [**data-plane**](../topologies/data-plane.md) **to `26.10.1` is optional.** All the fixes delivered in `26.10.1` live in the operator itself, so updating the operator is enough to get all of them. You may leave `updateStrategy.autoUpdateDataPlane` set to `false` (the default) and keep your current data-plane version, avoiding a rolling update of your `MariaDB` instances.
{% endhint %}

{% hint style="info" %}
**The SQL thread of stopped replicas may be started once after the operator is updated.** For every `MariaDB` with finished `PhysicalBackup` `Jobs`, the operator starts the SQL thread of the replicas where it is stopped without an error, which also recovers replicas left stopped by a previous `PhysicalBackup`. If you stopped the SQL thread of a replica on purpose, check it after updating the operator. No switchover and no rolling update are triggered.
{% endhint %}

- If you still prefer to keep the data-plane aligned with the operator version, set `updateStrategy.autoUpdateDataPlane=true` in your `MariaDB` resources before updating the operator. Then, once updated, the operator will also update the data-plane based on its version. Bear in mind that this triggers a rolling update of your `MariaDB` instances:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
  updateStrategy:
+   autoUpdateDataPlane: true
```

- Then, the CRDs must be updated to `26.10.1`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 26.10.1
```

- At this point, the operator can be updated to `26.10.1`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.10.1
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

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
