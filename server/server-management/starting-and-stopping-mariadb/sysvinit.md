---
description: >-
  Describes how to manage MariaDB using SysVinit scripts (mysql.server), common
  on older Linux distributions, using commands like `service` and `chkconfig`.
---

# sysVinit

[sysVinit](https://en.wikipedia.org/wiki/Init#SysV-style) is one of the most common service managers. On systems that use [sysVinit](https://en.wikipedia.org/wiki/Init#SysV-style), the [mysql.server](mysql-server.md) script is normally installed to `/etc/init.d/mysql`.

## Interacting with the MariaDB Server Process

The service can be interacted with by using the [service](https://linux.die.net/man/8/service) command.

### Starting the MariaDB Server Process on Boot

On RHEL/CentOS and other similar distributions, the [chkconfig](https://linux.die.net/man/8/chkconfig) command can be used to enable the MariaDB Server process at boot:

```
chkconfig --add mysql
chkconfig --level 345 mysql on
```

On Debian and Ubuntu and other similar distributions, the [update-rc.d](https://manpages.debian.org/wheezy/sysv-rc/update-rc.d.8.en.html) command can be used:

```
update-rc.d mysql defaults
```

### Starting the MariaDB Server Process

```
service mysql start
```

### Stopping the MariaDB Server Process

```
service mysql stop
```

### Restarting the MariaDB Server Process

```
service mysql restart
```

### Checking the Status of the MariaDB Server Process

```
service mysql status
```

## Manually Installing mysql.server with SysVinit

If you install MariaDB from [source](../install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/) or from a [binary tarball](../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) that does not install [mysql.server](mysql-server.md)\
automatically, and if you are on a system that uses [sysVinit](sysvinit.md), then you can manually install `mysql.server` with [sysVinit](sysvinit.md). See [mysql.server: Manually Installing with SysVinit](mysql-server.md) for more information.

## SysVinit and Galera Cluster

### Bootstrapping a New Cluster

When using [Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide) with sysVinit, the first node in a cluster has to be started with `service mysql bootstrap`. See [Getting Started with MariaDB Galera Cluster: Bootstrapping a New Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster#bootstrapping-a-new-cluster) for more information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
