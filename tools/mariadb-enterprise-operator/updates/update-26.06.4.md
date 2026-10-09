---
description: >-
  Step-by-step guide for updating MariaDB Enterprise Kubernetes Operator to
  26.06.4 from a previous version.
---

# 26.06.4 update guide

This guide illustrates, step by step, how to update to `26.6.4` from `26.6.3`. If you are updating from a version prior to `26.6.x`, follow the [26.06 update guide](update-26.06.md), the [26.06.1 update guide](update-26.06.1.md), the [26.06.2 update guide](update-26.06.2.md) and the [26.06.3 update guide](update-26.06.3.md) first, and apply the changes described there before continuing with this one.

{% hint style="info" %}
**Updating the** [**data-plane**](../topologies/data-plane.md) **to `26.6.4` is optional.** All the fixes delivered in `26.6.4` live in the operator itself, so updating the operator is enough to get all of them. You may leave `updateStrategy.autoUpdateDataPlane` set to `false` (the default) and keep your current data-plane version, avoiding a rolling update of your `MariaDB` instances.
{% endhint %}

{% hint style="warning" %}
Once the operator is updated, every `MaxScale` resource re-patches its servers once, even if nothing has changed. This is expected: the operator now also tracks the server attributes derived from the `MariaDB` and from the `MaxScale` TLS settings. The patch is idempotent, and it is the same change MaxScale receives when `spec.servers` is updated.
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

- Then, the CRDs must be updated to `26.6.4`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 26.6.4
```

- At this point, the operator can be updated to `26.6.4`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.6.4
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
