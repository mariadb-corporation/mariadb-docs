---
description: >-
  Step-by-step guide for updating MariaDB Enterprise Kubernetes Operator to
  26.10.2 from a previous version.
---

# 26.10.2 update guide

This guide illustrates, step by step, how to update to `26.10.2` from `26.10.1`. If you are updating from a version prior to `26.10.1`, follow the [26.10.1 update guide](update-26.10.1.md) first, and apply the changes described there before continuing with this one.

{% hint style="warning" %}
**`26.10.2` only updates the operator container image.** It fixes Critical and High CVEs and has no functional or breaking changes. Unlike other releases, there are no `26.10.2` Helm charts: the `mariadb-enterprise-operator-crds` and `mariadb-enterprise-operator` charts stay at version `26.10.1`, and the operator image is overridden to `26.10.2` via Helm values. The CRDs do not change, so they don't need to be updated.
{% endhint %}

{% hint style="info" %}
**Updating the** [**data-plane**](../topologies/data-plane.md) **to `26.10.2` is optional.** It has no functional or breaking changes, and it fixes the same CVEs in the data-plane containers, as they run the operator image. You may leave `updateStrategy.autoUpdateDataPlane` set to `false` (the default) and keep your current data-plane version, avoiding a rolling update of your `MariaDB` instances.
{% endhint %}

- If you want to update the data-plane to `26.10.2` to fix the CVEs in the data-plane containers, set `updateStrategy.autoUpdateDataPlane=true` in your `MariaDB` resources before updating the operator. Then, once updated, the operator will also update the data-plane based on its image. Bear in mind that this triggers a rolling update of your `MariaDB` instances:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
  updateStrategy:
+   autoUpdateDataPlane: true
```

- Make sure that the CRDs and the operator are running version `26.10.1`, as described in the [26.10.1 update guide](update-26.10.1.md).

- Override the image of the operator, the webhook and the cert-controller to `26.10.2` in the values of the `mariadb-enterprise-operator` chart, keeping the rest of your values as they are:

```yaml
image:
  tag: 26.10.2
webhook:
  image:
    tag: 26.10.2
certController:
  image:
    tag: 26.10.2
```

- At this point, the operator can be updated to `26.10.2` using the `26.10.1` chart and the values above:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.10.1 -f values.yaml
```

- Check that the operator, webhook and cert-controller Pods are running the `docker.mariadb.com/mariadb-enterprise-operator:26.10.2` image.

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

{% hint style="info" %}
When updating to a later release, remove the `26.10.2` image overrides from your values, so that the operator image defaults to the version of the chart again.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
