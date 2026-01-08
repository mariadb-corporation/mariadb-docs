---
description: >-
  Instructions on how to extend the official MariaDB Docker image by installing
  additional plugins and dependencies using a custom Dockerfile.
---

# Adding Plugins to the MariaDB Docker Official Image

MariaDB has many plugins. Most are not enabled by default, some are in the `mariadb` container, while others need to be installed from additional packages.

The following methods summarize [Installing plugins in the MariaDB Docker Library Container](https://mariadb.org/installing-plugins-in-the-mariadb-docker-library-container/) (mariadb.org blog post) on this topic.

### Which Plugins Does the Container Contain?

To see which plugins are available in the mariadb:

```bash
$ docker run --rm mariadb:latest ls -C /usr/lib/mysql/plugin
```

### Enabling a Plugin Using Flags

Using the `--plugin-load-add` flag with the plugin name (can be repeated), the plugins will be loaded and ready when the container is started:

For example, to enable the `simple\_password\_check` plugin:

```bash
$ docker run --name some-%%REPO%% -e MARIADB_ROOT_PASSWORD=my-secret-pw --network=host -d mariadb:latest --plugin-load-add=simple_password_check
```

### Enabling a Plugin in the Configuration Files

plugin-load-add\` can be used as a configuration option to load plugins. The example below loads the [FederatedX Storage Engine](../../../server-usage/storage-engines/federatedx-storage-engine/).

```bash
$ printf "[mariadb]\nplugin-load-add=ha_federatedx\n" > /my/custom/federatedx.conf
$ docker run --name some-mariadb -v /my/custom:/etc/mysql/conf.d -e MARIADB_ROOT_PASSWORD=my-secret-pw -d mariadb:latest
```

### Install a Plugin Using SQL in /docker-entrypoint-initdb.d

[INSTALL SONAME](../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) can be used to install a plugin as part of the database initialization.

Create the SQL file used in initialization:

```bash
$ echo 'INSTALL SONAME "disks";' > my_initdb/disks.sql
```

In this case, the `my\_initdb` is a `/docker-entrypoint-initdb.d` directory per "Initializing a fresh instance" section above.

### Identifying Additional Plugins in Additional Packages

A number of plugins are in separate packages to reduce their installation size. The package names of MariaDB-created plugins can be determined using the following command:

```bash
$ docker run --rm mariadb:latest sh -c 'apt-get update -qq && apt-cache search mariadb-plugin'
```

### Creating an Image With Plugins From Additional Packages

A new image needs to be created when using additional packages. The `mariadb` image can however be used as a base:

In the following, the [CONNECT Storage Engine](../../../server-usage/storage-engines/connect/) is installed:

```docker
FROM mariadb:latest
RUN apt-get update && \
    apt-get install mariadb-plugin-connect -y && \
    rm -rf /var/lib/apt/lists/*
```

Installing plugins from packages creates a configuration file in the directory `/etc/mysql/mariadb.conf.d/` that loads the plugin on startup.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
