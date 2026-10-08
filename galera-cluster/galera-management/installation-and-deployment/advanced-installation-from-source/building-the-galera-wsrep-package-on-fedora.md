---
description: >-
  Build the galera wsrep provider RPM package on Fedora and other RPM-based
  distributions using the build.sh script.
---

# Building the Galera wsrep Package on Fedora

The instructions on this page were used to create the _galera_ package on the Fedora Linux distribution. This package contains the wsrep provider for [MariaDB Galera Cluster](../../../readme/mariadb-galera-cluster-usage-guide.md).

For the list of Galera wsrep provider versions and the MariaDB release each one first shipped in, see:

{% content-ref url="../../../reference/galera-wsrep-provider-versions.md" %}
[galera-wsrep-provider-versions.md](../../../reference/galera-wsrep-provider-versions.md)
{% endcontent-ref %}

1. Install the prerequisites:

```
sudo yum update
sudo yum -y install boost-devel check-devel glibc-devel openssl-devel scons
```

2. Clone [galera.git](https://github.com/mariadb/galera) from [github.com/mariadb](https://github.com/mariadb) and checkout the mariadb-3.x branch:

```
git init repo
cd repo
git clone -b mariadb-3.x https://github.com/MariaDB/galera.git
```

3. Build the packages by executing under the`build.sh` scripts/ directory with the`-p` switch:

```
cd galera
./scripts/build.sh -p
```

When finished, you will have an RPM package containing the Galera library, arbitrator, and related files in the current directory. Note: The same set of instructions can be applied to other RPM-based platforms to generate the Galera package.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
