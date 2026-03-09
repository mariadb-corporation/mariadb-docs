# Migrate Community operator to Enterprise operator

In this guide, we will be migrating from the [MariaDB Community Operator](https://github.com/mariadb-operator/mariadb-operator) to the [MariaDB Enterprise Kubernetes Operator](../README.md) without downtime. This guide assumes:

* [0.37.1](https://github.com/mariadb-operator/mariadb-operator/releases/tag/0.37.1) version of the MariaDB Community Operator is installed in the cluster.
* `MariaDB` community resources will be migrated to its counterpart `MariaDB` enterprise resource. In this case, we will be using `11.4.4` version, which is supported in both community and enterprise versions. Check the supported [MariaDB Enterprise images](../docker-images.md) and migrate to a counterpart community version first if needed.
* `MaxScale` resources cannot be migrated in a similar way, they need to be recreated. To avoid downtime, temporarily point your applications to `MariaDB` directly during the migration.

**1.** Install the Enterprise CRDs as described in the [Helm documentation](../installation/helm.md#installing-crds).

**2.** Get the [migration script](https://operator.mariadb.com/scripts/migrate_enterprise.sh) and grant execute permissions:

```sh
curl -sLO https://operator.mariadb.com/scripts/migrate_enterprise.sh
chmod +x migrate_enterprise.sh
```

**3.** Migrate `MariaDB` resources using the migration script. Make sure you set `<mariadb-name>` with the name of the `MariaDB` resource to be migrated and `<operator-version>` with the version of the Enterprise operator you will be installing:

```sh
RESOURCE="<mariadb-name>" \
OLD_API_GROUP="k8s.mariadb.com" \
NEW_API_GROUP="enterprise.mariadb.com" \
NEW_MARIADB_IMAGE="docker.mariadb.com/enterprise-server:11.4.4-2" \
NEW_MARIADB_OPERATOR_IMAGE="docker.mariadb.com/mariadb-enterprise-operator:<operator-version>" \
./migrate_enterprise.sh
```

**4.** Update the `apiVersion` of the rest of CRs to `enterprise.mariadb.com/v1alpha1`.

**5.** Uninstall the Community operator:

```sh
helm uninstall mariadb-operator
```

**6.** If your `MariaDB` Community had Galera enabled, delete the `<mariadb-name>` `Role`, as it will be specifying the Community CRDs:

```sh
kubectl delete role <mariadb-name>
```

**7.** Install the Enterprise operator as described in the [Helm documentation](../installation/helm.md#installing-the-operator). This will trigger a rolling upgrade, make sure it finishes successfully before proceeding with the next step.

**8.** Delete the finalizers and uninstall the Community CRDs:

```sh
for crd in $(kubectl get crds -o json | jq -r '.items[] | select(.spec.group=="k8s.mariadb.com") | .metadata.name'); do
  kubectl get "$crd" -A -o json | jq -r '.items[] | "\(.metadata.namespace)/\(.metadata.name)"' | while read cr; do
    ns=$(echo "$cr" | cut -d'/' -f1)
    name=$(echo "$cr" | cut -d'/' -f2)
    echo "Removing finalizers from $crd: $name in $ns..."
    kubectl patch "$crd" "$name" -n "$ns" --type merge -p '{"metadata":{"finalizers":[]}}'
  done
done
helm uninstall mariadb-operator-crds
```

**9.** Run `mariadb-upgrade` in all `Pods`. Make sure you set `<mariadb-name>` with the name of the `MariaDB` resource:

```sh
for pod in $(kubectl get pods -l app.kubernetes.io/instance=<mariadb-name> -o jsonpath='{.items[*].metadata.name}'); do
  kubectl exec "$pod" -- sh -c 'mariadb-upgrade -u root -p${MARIADB_ROOT_PASSWORD} -f'
done
```

**10.** Restart the Enterprise operator:

```sh
kubectl rollout restart deployment mariadb-enterprise-operator
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}


{% @marketo/form formId="4316" %}
