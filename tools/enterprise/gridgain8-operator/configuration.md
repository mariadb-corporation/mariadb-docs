---
description: >-
  GridGainCluster settings, defaults, feature gates, and how generated
  configuration differs from a customer XML file.
---

# Configuration

The API reference lists every field. This page explains the defaults you hit first and the feature gates that keep some fields off until you opt in.

See [API Reference](api-reference.md) for types, validation, and defaults.

## Generated Configuration

By default the operator writes `default-config.xml`: discovery through the headless Service DNS, data regions, probes, and optional hooks for metrics or TLS when those gates are on.

Workload pods do **not** call the Kubernetes API to find peers. Do not expect the operator to create a Role for that.

`spec.caches` names are `PARTITIONED` with `backups=0`. A node restart drops entries whose only copy was on that node. Create backups in SQL or in your own XML. `spec.caches` cannot set the backup count.

## Customer XML

To mount your own Ignite XML, set `spec.mainConfigFrom` and `spec.allowUnsafeCustomConfig: true`. The operator mounts that ConfigMap as-is. Point `CONFIG_URI` (`spec.extraEnvVars`) at the mounted file.

The customer XML owns Ignite configuration, including authentication and TLS. `spec.auth.enabled` and `spec.tls.enabled` are refused together with `mainConfigFrom`. Beans that exist only in generated XML are not applied (`spec.caches`, data-region sizes from `status.memoryBudget`, and similar). Drain REST sends no credentials; if the XML enables authentication, drain fails unless unauthenticated REST is allowed.

## Feature Gates

Uncommitted capabilities are Alpha and **off by default**. Enable them with Helm:

```yaml
manager:
  featureGates:
    Auth: true
    CRDTLS: true
    ControlCenter: true
    Metrics: true
    NamedCaches: true
    Persistence: true
```

| Gate | Default | Spec that fills it |
| ---- | ------- | ------------------ |
| `Auth` | off | `spec.auth` is present |
| `CRDTLS` | off | `tls.enabled: true` or any TLS store field |
| `ControlCenter` | off | non-empty `controlCenterUrl` |
| `Metrics` | off | `metricsEnabled: true` |
| `NamedCaches` | off | `spec.caches` has at least one name |
| `Persistence` | off | an enabled volume, `persistenceEnabled`, volume permissions, or PVC retention |

Upgrade, drain, PDB, NetworkPolicy, and `defaultCacheConfiguration` are available without a gate.

While a gate is off, the webhook refuses a **create** that fills the field. Updates ratchet: a field already stored stays admitted if you later turn the gate off. The controller still will not reconcile a live object that fills a disabled gate (`FeatureGateDisabled` event). That matters in single-namespace mode, where the webhook is off.

Native persistence is not fully supported. `persistenceEnabled` stays false unless you opt in through the Persistence gate.

## Resources and JVM

When `spec.jvmOptions` is empty, the operator sizes heap from `spec.heapRamPercentage` (default `20`) of `spec.resources.limits.memory`. Computed values appear in `status.memoryBudget`.

## Probes

Default probes are HTTP GET on port `8080`:

* Liveness: `/ignite?cmd=probe&kind=liveness`
* Readiness: `/ignite?cmd=probe&kind=readiness`
* Startup: `/ignite?cmd=probe&kind=liveness`

They require GridGain **8.9.37** or newer. Setting any probe field replaces the whole probe.

## Examples

See [Quickstart](quickstart.md) for a copy-this cluster and the [examples catalog](examples-catalog.md) for OpenShift, upgrade, NetworkPolicy, scheduling, logging, and Alpha manifests.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
