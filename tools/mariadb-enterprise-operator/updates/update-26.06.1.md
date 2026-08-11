---
description: >-
  Step-by-step guide for updating MariaDB Enterprise Kubernetes Operator to
  26.06.1 from a previous version.
---

# 26.06.1 update guide

This guide illustrates, step by step, how to update to `26.6.1` from `26.6.0`. If you are updating from a version prior to `26.6.x`, follow the [26.06 update guide](https://mariadb.com/docs/tools/mariadb-enterprise-operator/updates/update-26.06) first, and apply the changes described there before continuing with this one.

- The [data-plane](../topologies/data-plane.md) must be updated to the `26.6.1` version, as the liveness probe fix that prevents MariaDB Pods from being restarted during long-running backups is delivered there. You must set `updateStrategy.autoUpdateDataPlane=true` in your `MariaDB` resources before updating the operator. Then, once updated, the operator will also update the data-plane based on its version:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
  updateStrategy:
+   autoUpdateDataPlane: true
```

- First of all, the CRDs must be updated to `26.6.1`. They include the new `spec.config.ephemeral` field on the `MaxScale` resource:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 26.6.1
```

{% hint style="info" %}
If the CRDs are managed by Helm through a GitOps tool such as ArgoCD or Flux, temporarily pause the reconciliation of that Helm release before applying the CRDs, and resume it afterwards.
{% endhint %}

- At this point, the operator can be updated to `26.6.1`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.6.1
```

- Wait until the data-plane update has completed: all `MariaDB` Pods must be ready and the `MariaDB` resources must report the `Ready` condition before proceeding.

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

## Updating MaxScale to 25.10.3

This section only applies if you are also updating MaxScale from `25.01.x` to `25.10.3`. It relies on the `config.ephemeral` field introduced in `26.6.1`, so the steps above must be completed first.

- **Enable ephemeral MaxScale configuration.** By default, MaxScale persists its runtime configuration under `/var/lib/maxscale` and loads it again on startup. That persisted copy was written by the previous MaxScale version and may contain parameters the new version no longer recognizes, causing the new Pods to fail to apply it on startup. Enabling ephemeral configuration removes this conflict at the source: MaxScale no longer persists or loads runtime configuration from disk, and a restarting Pod bootstraps itself using MaxScale's config sync feature, pulling the runtime configuration from the MariaDB cluster without depending on the operator.

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale
spec:
  config:
+   ephemeral: true
```

{% hint style="warning" %}
This change triggers a rolling update of the MaxScale Pods. **Wait until this rolling update finishes** — all MaxScale Pods ready and the `MaxScale` resource reporting the `Ready` condition — before bumping the image.
{% endhint %}

- **Update the MaxScale image.** Bump `spec.image` to the `25.10.3` version:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale
spec:
- image: docker.mariadb.com/maxscale:25.01.6
+ image: docker.mariadb.com/maxscale:25.10.3
```

**Expect a restart of the new Pods on first startup — this is expected and safe.** The cached configuration (`/var/lib/maxscale/maxscale-config.json`) written by the previous version still contains the `session_trace` service parameter, an unused parameter that has been removed from MaxScale (see [MXS-5533](https://jira.mariadb.org/browse/MXS-5533)). When `25.10.3` starts and attempts to apply that cached configuration, it fails to create the services because `session_trace` is no longer recognized. MaxScale then renames the bad cached configuration — keeping a copy at `maxscale-config.json.bad-config` — restarts, and starts correctly using the static configuration. No manual intervention is required.

You will see logs similar to the following:

```
notice : (ConfigManager); Using cached configuration for cluster 'mariadbmon-monitor', version 11: /var/lib/maxscale/maxscale-config.json
warning: Discarding journal file '/var/lib/maxscale/mariadbmon-monitor_journal.json'. File is for MaxScale version 250106. Current MaxScale version is 251003.
error  : (ConfigManager); readconnroute: The parameter 'session_trace' is unrecognized.
error  : (ConfigManager); Could not create service 'rconn-master-router' with module 'readconnroute'
error  : (ConfigManager); Failed to apply cached configuration: Failed to create service 'rconn-master-router'
error  : (ConfigManager); Renamed cached configuration, using static configuration on next startup. A copy of the bad cached configuration is stored at: /var/lib/maxscale/maxscale-config.json.bad-config
notice : Attempting to restart MaxScale.
notice : MaxScale is shutting down.
notice : MaxScale shutdown completed.
```

After the automatic restart, MaxScale comes up correctly on `25.10.3`, recreating its services and listeners from the synchronized configuration:

```
warning: (ConfigManager); Successfully reverted the failed configuration change, ignoring configuration version 6.
notice : [mariadbmon] 'mariadbmon-monitor' acquired the exclusive lock on a majority of its servers.
notice : (ConfigManager); Updating to configuration version 13
notice : (ConfigManager); Created service 'rconn-master-router'
notice : (ConfigManager); Created service 'rconn-slave-router'
notice : (ConfigManager); Created service 'rw-router'
notice : (rw-router-listener); Listening for connections at [::]:3306
notice : (ConfigManager); Added 'mariadb-repl-0', 'mariadb-repl-1' to 'rw-router'
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}