# 25.08 migration guide

This guide illustrates, step by step, how to migrate to `25.8.0` from previous versions. 

- Uninstall you current `mariadb-enterprise-operator` for preventing conflicts:
```bash
helm uninstall mariadb-enterprise-operator
```
Alternatively, you may only downscale and delete the webhook configurations:
```bash
kubectl scale deployment mariadb-enterprise-operator --replicas=0
kubectl scale deployment mariadb-enterprise-operator-webhook --replicas=0
kubectl delete validatingwebhookconfiguration mariadb-enterprise-operator-webhook
kubectl delete mutatingwebhookconfiguration mariadb-enterprise-operator-webhook
```

- Upgrade `mariadb-enterprise-operator-crds` to `25.8.0`:

```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds  mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 25.8.0
```

- The Galera data-plane must be updated to the `25.8.0` version. 


If you want the operator to automatically update the data-plane (i.e. init and agent containers), you can set `updateStrategy.autoUpdateDataPlane=true` in your `MariaDB` resources:
```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  updateStrategy:
+   autoUpdateDataPlane: true
```

Alternatively, you can also do this manually:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  galera:
    agent:
-      image: docker.mariadb.com/mariadb-enterprise-operator:1.0.0
+      image: docker.mariadb.com/mariadb-enterprise-operator:25.8.0
    initContainer:
-      image: docker.mariadb.com/mariadb-enterprise-operator:1.0.0
+      image: docker.mariadb.com/mariadb-enterprise-operator:25.8.0
```

-  Upgrade `mariadb-enterprise-operator` to `25.8.0`:
```bash 
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 25.8.0 
```

- If you previously decided to downscale the operator, make sure you upscale it back:
```bash
kubectl scale deployment mariadb-enterprise-operator --replicas=1
kubectl scale deployment mariadb-enterprise-operator-webhook --replicas=1
```

- If you previously set `updateStratety.autoUpdateDataPlane=true`, you may consider reverting the changes once the upgrades have finished:

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  updateStrategy:
+   autoUpdateDataPlane: false
-   autoUpdateDataPlane: true
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}


{% @marketo/form formId="4316" %}