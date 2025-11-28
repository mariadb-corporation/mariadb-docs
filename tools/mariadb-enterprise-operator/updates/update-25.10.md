# 25.10 LTS update guide

This guide illustrates, step by step, how to update to `25.10.2` from previous versions.

- The Galera data-plane must be updated to the `25.10.2` version. You must set `updateStrategy.autoUpdateDataPlane=true` in your `MariaDB` resources before updating the operator. Then, once updated, the operator will also be updating the data-plane based on its version:
```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  updateStrategy:
+   autoUpdateDataPlane: true
```

- Once set, you may proceed to update the operator. If you are using __Helm__:

Upgrade the `mariadb-enterprise-operator-crds` helm chart to `25.10.2`:
```bash
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds  mariadb-enterprise-operator/mariadb-enterprise-operator-crds --version 25.10.2
```

Upgrade the `mariadb-enterprise-operator` helm chart to `25.10.2`:
```bash 
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator --version 25.10.2
```

As part of the 25.10 LTS release, we have introduced support for LTS versions. Refer to the [Helm docs](https://mariadb.com/docs/tools/mariadb-enterprise-operator/installation/helm#long-term-support-versions) for sticking to LTS versions.

- If you are on __OpenShift__:

If you are on the `stable` channel using `installPlanApproval=Automatic` in your `Subscription` object, then the operator will be automatically updated. If you use `installPlanApproval=Manual`, you should have a new `InstallPlan` which needs to be approved to update the operator:

```bash
oc get installplan
NAME            CSV                                     APPROVAL   APPROVED
install-sjgcs   mariadb-enterprise-operator.v25.10.2    Manual     false

oc patch installplan install-sjgcs --type merge -p '{"spec":{"approved":true}}'

installplan.operators.coreos.com/install-sjgcs patched
```

As part of the 25.10 LTS release, we have introduced new [release channels](https://mariadb.com/docs/tools/mariadb-enterprise-operator/installation/openshift#release-channels). Consider switching to the `stable-v25.10` if you are willing to stay in the `25.10.x` version:

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: mariadb-enterprise-operator
  namespace: openshift-operators
spec:
  channel: stable-v25.10
  installPlanApproval: Automatic
  name: mariadb-enterprise-operator
  source: certified-operators
  sourceNamespace: openshift-marketplace
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
