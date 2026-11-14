# Migrate Embedded MaxScale to MaxScale Resource

In this guide, we will be migrating a `MaxScale` embedded in a `MariaDB` resource to its own resource.

{% hint style="warning" %}
The embedded `spec.maxScale` field was removed from the `MariaDB` CRD in Enterprise Operator 26.03. The last release series that supports it is 25.10. Complete this migration while you are still on 25.10, before you update the operator to 26.03 or later. With the newer CRDs, the `spec.maxScale` field no longer exists, so the operator no longer acts on it.
{% endhint %}

```diff
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
+  maxScaleRef:
+     name: mariadb-maxscale
-  # Provision a MaxScale instance and set 'spec.maxScaleRef' automatically.
-  maxScale:
-    enabled: true
-    connection:
-      secretName: mxs-repl-conn
-      port: 3306
-    metrics:
-      enabled: true
```

{% hint style="info" %}
Note that if you've been using the embedded `maxScale` property, the operator will already have created a `MaxScale` resource to go along with it, named `<mariadb-name>-maxscale`. The migration script sets `spec.maxScaleRef` to that name.
{% endhint %}

**1.** Get the [migration script](https://operator.mariadb.com/scripts/migrate_maxscale_to_resource.sh) and grant execute permissions:

```sh
curl -sLO https://operator.mariadb.com/scripts/migrate_maxscale_to_resource.sh
chmod +x migrate_maxscale_to_resource.sh
```

**2.** Migrate all of your existing `MariaDB` resources where `MaxScale` is embedded.

```sh
./migrate_maxscale_to_resource.sh <mariadb_manifest.yaml>
```

This will have created new `<migrated.mariadb_manifest.yaml>` manifests.

**3.** Inspect the newly created manifests and overwrite the source manifests if satisfied with the changes.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
