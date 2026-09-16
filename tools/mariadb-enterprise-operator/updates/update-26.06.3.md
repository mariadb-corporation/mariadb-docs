---
description: >-
  Step-by-step guide for updating MariaDB Enterprise Kubernetes Operator to
  26.06.3 from a previous version.
---

# 26.06.3 update guide

This guide illustrates, step by step, how to update to `26.6.3` from `26.6.2`. If you are updating from a version prior to `26.6.x`, follow the [26.06 update guide](update-26.06.md), the [26.06.1 update guide](update-26.06.1.md) and the [26.06.2 update guide](update-26.06.2.md) first, and apply the changes described there before continuing with this one.

{% hint style="info" %}
**Updating the** [**data-plane**](../topologies/data-plane.md) **to `26.6.3` is mandatory if you want to use the new** [**`replication.semiSyncBootAsReplica`**](../topologies/replication.md#configuration) **field.** It is rendered into the server configuration by the data-plane containers, so an older data-plane silently ignores it and the setting has no effect. Updating it implies a rolling update of the affected `MariaDB` instances. Unlike other replication settings, this one has no `spec.myCnf` equivalent, because the data-plane renders `rpl_semi_sync_master_enabled` itself.

The per-role handling of `rpl_semi_sync_master_enabled` described below lives in the operator itself, so updating the operator is enough to get it. If you do not intend to use the new field, you may leave `updateStrategy.autoUpdateDataPlane` set to `false` (the default) and keep your current data-plane version, avoiding a rolling update of your `MariaDB` instances.
{% endhint %}

{% hint style="warning" %}
Once the operator is updated, [`rpl_semi_sync_master_enabled`](https://mariadb.com/docs/server/ha-and-performance/standard-replication/semisynchronous-replication#rpl_semi_sync_master_enabled) is converged to the role of each node on every reconciliation: enabled in the current primary, disabled in the replicas. The configuration file still renders it as `ON`, so a node boots armed and the operator disarms it once it reconciles it as a replica. Setting `replication.semiSyncBootAsReplica` to `true` is what removes that window, and it requires the data-plane update described above.

If you worked around stalled replicas by setting `replication.semiSyncWaitNoSlave: false`, or `rpl_semi_sync_master_wait_no_slave=OFF` through `spec.myCnf`, that workaround is no longer needed and you may revert it to regain a primary that never commits a transaction without a replica acknowledgement.
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

- Then, the CRDs must be updated to `26.6.3`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 26.6.3
```

- At this point, the operator can be updated to `26.6.3`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.6.3
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