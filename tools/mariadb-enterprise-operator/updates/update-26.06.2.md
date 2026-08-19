---
description: >-
  Step-by-step guide for updating MariaDB Enterprise Kubernetes Operator to
  26.06.2 from a previous version.
---

# 26.06.2 update guide

This guide illustrates, step by step, how to update to `26.6.2` from `26.6.1`. If you are updating from a version prior to `26.6.x`, follow the [26.06 update guide](https://mariadb.com/docs/tools/mariadb-enterprise-operator/updates/update-26.06) first, and apply the changes described there before continuing with this one.

## `spec.maxScaleRef` is now required in highly available `MariaDB` resources

{% hint style="danger" %}
This is a **backwards incompatible** change. Complete this section **before** updating the operator.
{% endhint %}

Starting from `26.6.2`, the validation webhook rejects `MariaDB` resources that have `spec.replication` or `spec.galera` configured and no `spec.maxScaleRef`, so that switchover and failover are handled by MaxScale instead of by the operator. [Standalone](../topologies/standalone.md) `MariaDB` resources are not affected.

Already running `MariaDB` resources keep running, but their updates are rejected until either `spec.maxScaleRef` is set or the validation is disabled.

* For each of your `MariaDB` Custom Resources, either set `spec.maxScaleRef` to the `MaxScale` that proxies it:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
+ maxScaleRef:
+   name: maxscale-galera
  galera:
    enabled: true
```

* Or, if you intentionally run a highly available `MariaDB` without MaxScale, opt out of the validation when updating the operator:

```diff
# values.yaml
+requireMaxScaleRef: false
```

Refer to the [migration guide](../migrations/require-maxscale-ref.md) for the full detail on both options.

## Updating the operator

* First of all, the CRDs must be updated to `26.6.2`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 26.6.2
```

{% hint style="info" %}
If the CRDs are managed by Helm through a GitOps tool such as ArgoCD or Flux, temporarily pause the reconciliation of that Helm release before applying the CRDs, and resume it afterwards.
{% endhint %}

* At this point, the operator can be updated to `26.6.2`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.6.2 \
  -f values.yaml
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}