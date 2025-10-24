# Enabling TLS in existing instances

In this guide, we will be migrating existing `MariaDB` Galera and `MaxScale` instances to [TLS](../tls.md) without downtime.

**1.** Ensure that `MariaDB` has TLS enabled and not enforced. Set the following options if needed:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  tls:
+   enabled: true
+   required: false
+   galeraSSTEnabled: false
+   galeraServerSSLMode: PROVIDER
+   galeraClientSSLMode: DISABLED
```

By setting these options, the operator will issue and configure certificates for `MariaDB`, but TLS will not be enforced in the connections i.e. both TLS and non-TLS connections will be accepted. TLS enforcement will be optionally configured at the end of the migration process.

This will trigger a rolling upgrade, make sure it finishes successfully before proceeding with the next step. Refer to the [updates documentation](../updates.md) for further information about update strategies.

**2.** If you are currently using `MaxScale`, it is important to note that, unlike `MariaDB`, it does not support TLS and non-TLS connections simultaneously (see [limitations](../tls.md)). For this reason, you must temporarily point your applications to `MariaDB` during the migration process. You can achieve this by configuring your application to use the [MariaDB Services](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability#kubernetes-services). At the end of the `MariaDB` migration process, the `MaxScale` instance will need to be recreated in order to use TLS, and then you will be able to point your application back to `MaxScale`. Ensure that all applications are pointing to `MariaDB` before moving on to the next step.

**3.** `MariaDB` is now accepting TLS connections. The next step is [migrating your applications to use TLS](../tls.md) by pointing them to `MariaDB` securely. Ensure that all applications are connecting to `MariaDB` via TLS before proceeding to the next step.

**4.** If you are currently using `MaxScale`, and you are planning to connect via TLS through it, you should now delete your `MaxScale` instance. If needed, keep a copy of the `MaxScale` manifest, as we will need to recreate it with TLS enabled in further steps:

```sh
kubectl get mxs maxscale-galera -o yaml > maxscale-galera.yaml
kubectl delete mxs maxscale-galera
```

It is very important that you wait until your old `MaxScale` instance is fully terminated to make sure that the old configuration is cleaned up by the operator.

**5.** For enhanced security, it is recommended to enforce TLS in all `MariaDB` connections by setting the following options. This will trigger a rolling upgrade, make sure it finishes successfully before proceeding with the next step:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  tls:
+   required: true
+   galeraServerSSLMode: SERVER_X509
```

**6.** For improved security, you can optionally configure TLS for Galera SSTs by following the steps below:

* Get the [migration script](https://operator.mariadb.com/scripts/migrate_galera_ssl.sh) and grant execute permissions:

```sh
curl -sLO https://operator.mariadb.com/scripts/migrate_galera_ssl.sh
chmod +x migrate_galera_ssl.sh
```

* Run the migration script. Make sure you set `<mariadb-name>` with the name of the `MariaDB` resource:

```sh
./migrate_galera_ssl.sh <mariadb-name>
```

* Set the following option to enable TLS for Galera SSTs:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  tls:
+   galeraSSTEnabled: true
+   galeraClientSSLMode: VERIFY_IDENTITY
```

This will trigger a rolling upgrade, make sure it finishes successfully before proceeding with the next step

**7.** As mentioned in step 4, recreate your `MaxScale` instance with `tls.enabled=true` if needed:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
+ tls:
+   enabled: true
```

**8.** `MaxScale` is now accepting TLS connections. Next, you need to [migrate your applications to use TLS](../tls.md) by pointing them back to `MaxScale` securely. You have done this previously for `MariaDB`, you just need to update your application configuration to use the [MaxScale Service](../topologies/maxscale.md#kubernetes-services) and its CA bundle.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
