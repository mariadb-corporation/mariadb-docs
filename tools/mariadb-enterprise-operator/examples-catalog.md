
# Examples Catalog

The [examples catalog](https://operator.mariadb.com/examples/manifests.tar.gz) contains a number of sample manifests that aim to show the operator functionality in a practical way. Follow these instructions for getting started:


* Download the [examples catalog](https://operator.mariadb.com/examples/manifests.tar.gz):

```sh
curl -sLO https://operator.mariadb.com/examples/manifests.tar.gz
mkdir -p examples
tar -xzf manifests.tar.gz -C examples
```

* Install the configuration shared by all the examples:

```sh
kubectl apply -f examples/config
```

* Start deploying examples:

```sh
kubectl apply -f examples/mariadb.yaml
```



Some examples rely on external dependencies for specific tasks, make sure to install them when it applies:
* [prometheus-operator](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) for metrics
* [cert-manager](https://cert-manager.io/docs/installation/helm/) for TLS certificates
* [minio](https://github.com/minio/minio/tree/master/helm/minio) for S3 object storage


It is recommended to complement the examples with the [API reference](api-reference.md) documentation to understand the full range of configuration options available.


If you are looking for production-grade examples, you can check the `mariadb_galera_production.yaml` and `maxscale_galera_production.yaml` examples.


{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
