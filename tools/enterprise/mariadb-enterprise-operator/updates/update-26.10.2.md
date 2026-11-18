---
description: >-
  Step-by-step guide for updating MariaDB Enterprise Kubernetes Operator to
  26.10.2 from a previous version.
---

# 26.10.2 update guide

This guide illustrates, step by step, how to update to `26.10.2` from `26.10.1`. If you are updating from a version prior to `26.10.1`, follow the [26.10.1 update guide](update-26.10.1.md) first, and apply the changes described there before continuing with this one.

{% hint style="info" %}
**`26.10.2` only contains security fixes.** It fixes Critical and High CVEs in the operator image, and has no functional or breaking changes.
{% endhint %}

{% hint style="info" %}
**Updating the** [**data-plane**](../topologies/data-plane.md) **to `26.10.2` is optional.** It has no functional or breaking changes, and it fixes the same CVEs in the data-plane containers, as they run the operator image. You may leave `updateStrategy.autoUpdateDataPlane` set to `false` (the default) and keep your current data-plane version, avoiding a rolling update of your `MariaDB` instances.
{% endhint %}

- If you want to update the data-plane to `26.10.2` to fix the CVEs in the data-plane containers, set `updateStrategy.autoUpdateDataPlane=true` in your `MariaDB` resources before updating the operator. Then, once updated, the operator will also update the data-plane based on its version. Bear in mind that this triggers a rolling update of your `MariaDB` instances:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
  updateStrategy:
+   autoUpdateDataPlane: true
```

- Then, the CRDs must be updated to `26.10.2`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 26.10.2
```

- At this point, the operator can be updated to `26.10.2`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.10.2
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
