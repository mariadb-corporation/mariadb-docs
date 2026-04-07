# 26.03 update guide

This guide illustrates, step by step, how to update to `26.3.2` from previous versions. This guide only applies if you are updating from a version prior to `26.3.x`, otherwise you may upgrade directly (see [Helm](https://mariadb.com/docs/tools/mariadb-enterprise-operator/installation/helm#updates) and [OpenShift](https://mariadb.com/docs/tools/mariadb-enterprise-operator/installation/openshift#updates) docs)

- The [data-plane](../topologies/data-plane.md) must be updated to the `26.3.2` version. You must set `updateStrategy.autoUpdateDataPlane=true` in your `MariaDB` resources before updating the operator. Then, once updated, the operator will also be updating the data-plane based on its version:
```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  updateStrategy:
+   autoUpdateDataPlane: true
```

- `MaxScale` embedded definition inside the `MariaDB` has been deprecated, please refer to the [migration guide.](https://mariadb.com/docs/tools/mariadb-enterprise-operator/migrations/migrate-embedded-maxscale-to-maxscale-resource) to perform the migration.

- At this point, you may proceed to update the operator. If you are using __Helm__:

Upgrade the `mariadb-enterprise-operator-crds` helm chart to `26.3.2`:
```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds  mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 26.3.2
```

Upgrade the `mariadb-enterprise-operator` helm chart to `26.3.2`:
```bash 
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 26.3.2
```

- If you are on __OpenShift__:

If you are on the `stable` channel using `installPlanApproval=Automatic` in your `Subscription` object, then the operator will be automatically updated. If you use `installPlanApproval=Manual`, you should have a new `InstallPlan` which needs to be approved to update the operator:

```bash
oc get installplan
NAME            CSV                                     APPROVAL   APPROVED
install-sjgcs   mariadb-enterprise-operator.v25.10.4    Manual     false

oc patch installplan install-sjgcs --type merge -p '{"spec":{"approved":true}}'

installplan.operators.coreos.com/install-sjgcs patched
```

- Consider reverting `updateStrategy.autoUpdateDataPlane` back to `false` in your `MariaDB` object to avoid unexpected updates:

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