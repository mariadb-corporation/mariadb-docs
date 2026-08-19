---
description: >-
  How to adapt existing installations to the MaxScale reference requirement
  introduced in MariaDB Enterprise Kubernetes Operator 26.06.2.
---

# Migrate to the MaxScale Reference Requirement

Starting from `26.6.2`, the validation webhook **rejects** `MariaDB` resources that have `spec.replication` or `spec.galera` configured and no `spec.maxScaleRef`. This guide describes how to adapt existing installations.

{% hint style="danger" %}
This is a **backwards incompatible** change. Existing `MariaDB` resources that do not set `spec.maxScaleRef` keep running, but they are rejected on their next update. Read this guide **before** updating the operator.
{% endhint %}

## Why

`spec.maxScaleRef` determines who owns topology decisions:

* **With** `spec.maxScaleRef`, switchover and failover are delegated to [MaxScale](../topologies/maxscale.md).
* **Without** it, the operator performs switchover and failover itself.

When a `MaxScale` proxies a `MariaDB` that does not reference it back, both the operator and MaxScale drive the topology independently and clash, which leads to failed switchovers, inconsistent primaries and, in the worst case, replicas that need a full rebuild. The reference is also the gate for several MaxScale-aware behaviors in the operator, which silently do not apply when it is missing.

## Which resources are affected

| `MariaDB` | Affected |
| --- | --- |
| `spec.replication.enabled=true` without `spec.maxScaleRef` | Yes |
| `spec.galera.enabled=true` without `spec.maxScaleRef` | Yes |
| [Standalone](../topologies/standalone.md), with neither `spec.replication` nor `spec.galera` | No |
| Any topology with `spec.maxScaleRef` already set | No |


## Option 1: Reference a MaxScale (recommended)

If a `MaxScale` already proxies the `MariaDB`, add the reference to it. This is also the configuration that avoids the operator and MaxScale clashing:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  # [...]
  maxScaleRef:
    name: maxscale-galera
  galera:
    enabled: true
  # [...]
```

You can achieve this imperatively using `kubectl patch`:

```bash
kubectl patch mariadb mariadb-galera \
  --type='merge' \
  -p '{"spec":{"maxScaleRef":{"name":"maxscale-galera"}}}'
```

If you do not have a `MaxScale` yet, refer to the [MaxScale documentation](../topologies/maxscale.md) to provision one.

{% hint style="warning" %}
Setting `spec.maxScaleRef` on an existing `MariaDB` hands over switchover and failover to MaxScale. Plan it as you would any other topology change, and verify that MaxScale reports the expected primary afterwards.
{% endhint %}

## Option 2: Opt out of the validation

If you intentionally run a highly available `MariaDB` without MaxScale, you can keep the previous behavior by disabling the validation in the operator. With the [helm chart](../installation/helm.md):

```yaml
# values.yaml
requireMaxScaleRef: false
```

```bash
helm upgrade --install mariadb-enterprise-operator \
  mariadb-enterprise-operator/mariadb-enterprise-operator \
  -f values.yaml
```

This renders the `--require-maxscale-ref=false` flag in the webhook `Deployment`. If you do not deploy with helm, set the flag directly, or the `MARIADB_ENTERPRISE_OPERATOR_REQUIRE_MAXSCALE_REF=false` environment variable, wherever the webhook server runs.

{% hint style="info" %}
The validation is enforced by the webhook, so the flag has no effect if it is only set in the controller `Deployment` while the webhook runs separately.
{% endhint %}

## More Information

For more details, please refer to the [Requiring a MaxScale reference](../topologies/maxscale.md#requiring-a-maxscale-reference) section in the MaxScale documentation.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>