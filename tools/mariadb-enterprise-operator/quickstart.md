
# Quickstart

This guide aims to provide a quick way to get started with the MariaDB Enterprise Operator for Kubernetes. It will walk you through the process of deploying a MariaDB Enterprise Cluster and MaxScale via the `MariaDB` and `MaxScale` CRs ([Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)) respectively.


Before you begin, ensure you meet the following prerequisites:


* Configure your [customer access for docker.mariadb.com](customer-access-to-docker-mariadb-com.md)
* [Install the MariaDB Enterprise Operator](mariadb-enterprise-operator-installation/README.md)


The first step will be configuring a `Secret` with the credentials used by the `MariaDB` CR:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mariadb
stringData:
  password: MariaDB11!
```

```sh
kubectl apply -f secret.yaml
```

Next, we will deploy a MariaDB Enterprise Cluster (Galera) using the following CR:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  rootPasswordSecretKeyRef:
    name: mariadb
    key: password
  imagePullSecrets:
  -  name: mariadb-enterprise
  maxScaleRef:
    name: maxscale-galera
  username: mariadb
  passwordSecretKeyRef:
    name: mariadb
    key: password
  database: mariadb
  storage:
    size: 1Gi
  replicas: 3
  galera:
    enabled: true
```

```sh
kubectl apply -f mariadb-galera.yaml
```

Let's break it down:
* `rootPasswordSecretKeyRef`: A reference to a `Secret` containing the root password.
* `imagePullSecrets`: The name of the `Secret` containing the customer credentials to pull the MariaDB Enterprise Server image.
* `maxScaleRef`: The name of the `MaxScale` CR that we will be creating right after.
* `username`, `passwordSecretKeyRef` and `database`: The initial user and database to create.
* `storage`: The size of the volume that will back the data directory.
* `replicas`: The number of MariaDB Enterprise Server instances to deploy.
* `galera`: Configuration for the Galera clustering.


After applying the CR, we can observe the MariaDB `Pods` being created:

```sh
❯ kubectl get pods
NAME                                                           READY   STATUS    RESTARTS      AGE
mariadb-galera-0                                               2/2     Running   0             101s
mariadb-galera-1                                               2/2     Running   0             101s
mariadb-galera-2                                               2/2     Running   0             101s
```

Now, let's deploy a `MaxScale` CR:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  imagePullSecrets:
   -  name: mariadb-enterprise
  mariaDbRef:
    name: mariadb-galera
  replicas: 2
```

```sh
kubectl apply -f maxscale-galera.yaml
```


Again, let's break it down:
* `imagePullSecrets`: The name of the `Secret` containing the customer credentials to pull the MaxScale image.
* `mariaDbRef`: A reference to the `MariaDB` CR that we want to connect to.
* `replicas`: The number of MaxScale instances to deploy.

After applying the CR, we can observe the MaxScale `Pods` being created, and that both the `MariaDB` and `MaxScale` CRs will become ready eventually:

```sh
❯ kubectl get pods
mariadb-galera-0                                               2/2     Running   0             10m
mariadb-galera-1                                               2/2     Running   0             10m
mariadb-galera-2                                               2/2     Running   0             10m
maxscale-galera-0                                              1/1     Running   0             81s
maxscale-galera-1                                              1/1     Running   0             81s

❯ kubectl get maxscale
NAME              READY   STATUS    PRIMARY            AGE
maxscale-galera   True    Running   mariadb-galera-0   65s

❯ kubectl get mariadb
NAME             READY   STATUS    PRIMARY            UPDATES                    AGE
mariadb-galera   True    Running   mariadb-galera-0   ReplicasFirstPrimaryLast   10m
```



To conclude, let's connect to the MariaDB Enterprise Cluster through MaxScale using the initial user and database we initially defined in the `MariaDB` CR:


```sh
❯ kubectl run mariadb-connect --rm -it --image=mariadb:11.4 -- bash -c "mariadb -u mariadb -p'MariaDB11!' --ssl=false -h maxscale-galera"
If you don't see a command prompt, try pressing enter.
MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mariadb            |
+--------------------+
2 rows in set (0.001 sec)
```

{% hint style="success" %}
You have successfully deployed a MariaDB Enterprise Cluster with MaxScale in Kubernetes using the MariaDB Enterprise Operator!
{% endhint %}

Refer to the [documentation](README.md), the [API reference](api-reference.md) and the [examples catalog](examples-catalog.md) for further detail.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}


{% @marketo/form formId="4316" %}
