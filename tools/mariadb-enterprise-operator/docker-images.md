# Docker Images

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/b36uzH0IlkzSr1zA7hGa/" %}

## Certified images

All the Docker images used by this operator are based on [Red Hat UBI](https://catalog.redhat.com/software/base-images) and have been [certified by Red Hat](https://connect.redhat.com/en/partner-with-us/red-hat-openshift-certification). The advantages of using UBI based images are:

* Immutability: UBI images are built to be secure and stable, reducing the risk of unintended changes or vulnerabilities due to mutable base layers.
* Small size: The UBI [minimal](https://catalog.redhat.com/software/containers/ubi8/ubi-minimal/5c359a62bed8bd75a2c3fba8) and [micro](https://catalog.redhat.com/software/containers/ubi8-micro/601a84aadd19c7786c47c8ea) variants used by this operator are designed to be lightweight, containing only the essential packages. This can lead to smaller container image sizes, resulting in faster build times, reduced storage requirements, and quicker image pulls.
* Security and compliance: Regular CVE scanning and vulnerability patching help maintain compliance with industry standards and security best practices.
* Enterprise-grade support: UBI images are maintained and supported by Red Hat, ensuring timely security updates and long-term stability.&#x20;

&#x20;

## List of compatible images

MariaDB Enterprise Operator is compatible with the following Docker images:

| Component | Image | Supported Tags | CPU Architecture |
|-----------|-------|----------------|------------------|
| MariaDB Enterprise Operator (ppc64le support) | docker.mariadb.com/mariadb-enterprise-operator |  25.8.0 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MariaDB Enterprise Operator | docker.mariadb.com/mariadb-enterprise-operator |  1.0.0 <br>  |  amd64 <br>  arm64 <br>  |
| MariaDB Enterprise Server (ppc64le support) | docker.mariadb.com/enterprise-server |  11.4.7-4.1 <br>  11.4 <br>  10.6.22-18.1 <br>  10.6 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MariaDB Enterprise Server | docker.mariadb.com/enterprise-server |  11.4.5-3 <br>  11.4.4-2 <br>  10.6.21-17 <br>  10.6.20-16.1 <br>  10.6.19-15.1 <br>  10.6.18-14.2 <br>  10.6.17-13.2 <br>  |  amd64 <br>  arm64 <br>  |
| MaxScale Enterprise (ppc64le support) | docker.mariadb.com/maxscale |  25.01.3-1.1 <br>  25.01 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MaxScale Enterprise | docker.mariadb.com/maxscale-enterprise |  25.01.2 <br>  25.01.1 <br>  |  amd64 <br>  arm64 <br>  |
| MaxScale | mariadb/maxscale |  24.02.5-ubi <br>  24.02-ubi <br>  23.08.9-ubi <br>  23.08-ubi <br>  |  amd64 <br>  arm64 <br>  |
| MariaDB Prometheus Exporter (ppc64le support) | mariadb/mariadb-prometheus-exporter-ubi |  1.1.0 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MariaDB Prometheus Exporter | mariadb/mariadb-prometheus-exporter-ubi |  1.0.0 <br>  |  amd64 <br>  arm64 <br>  |
| MaxScale Prometheus Exporter (ppc64le support) | mariadb/maxscale-prometheus-exporter-ubi |  1.1.0 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MaxScale Prometheus Exporter | mariadb/maxscale-prometheus-exporter-ubi |  1.0.0 <br>  |  amd64 <br>  arm64 <br>  |

Refer to the registry documentation to [access docker.mariadb.com with your customer credentials](customer-access-to-docker-mariadb-com.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
