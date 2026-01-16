# Migrate Embedded MaxScale to MaxScale Resource

In this guide, we will be migrating a `MaxScale` embedded in a `MariaDB` resource to it's own resource.

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
Note that if you've been using the embedded `maxScale` property, the operator will already have created a `MaxScale` resource to go along with it. 
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

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
