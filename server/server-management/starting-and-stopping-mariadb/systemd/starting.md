---
description: >-
  Starting, stopping, restarting, and inspecting the MariaDB systemd service,
  multi-instance setups, Galera Cluster integration, and the systemd journal.
---

# Starting MariaDB on systemd

This page covers the operational side of running MariaDB under [systemd](README.md). For drop-in configuration, limits, socket activation, and `mariadbd-safe`-to-systemd conversion, see [Configuring MariaDB for systemd](configuring.md).

## Installing & Starting MariaDB

When installing using the MariaDB server RPM or DEB package, it automatically runs the [mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md) script which creates the initial databases and users.

When MariaDB is started with the `systemd` unit file, it directly starts the [mariadbd](../mariadbd-options.md) process as the `mysql` user. Unlike with [sysVinit](../sysvinit.md), the [mariadbd](../mariadbd-options.md) process is not started with [mariadbd-safe](../mariadbd-safe.md). As a consequence, options are not read from the `[mariadbd-safe]` [option group](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

## Interacting with the MariaDB Server Process

The service can be interacted with by using the [systemctl](https://www.freedesktop.org/software/systemd/man/systemctl.html) command.

### Starting the MariaDB Server Process on Boot

MariaDB's `systemd` service can be configured to start at boot by executing the following:

```bash
sudo systemctl enable mariadb.service
```

### Starting the MariaDB Server Process

MariaDB's `systemd` service can be started by executing the following:

```bash
sudo systemctl start mariadb.service
```

MariaDB's `systemd` unit file has a default startup timeout of about 90 seconds on most systems. If certain startup tasks, such as crash recovery, take longer than this default startup timeout, then `systemd` assumes that `mariadbd` has failed to startup, which causes `systemd` to kill the `mariadbd` process. To work around this, you can reconfigure the MariaDB `systemd` unit to have an [infinite timeout](configuring.md#configuring-the-systemd-service-timeout).

Note that [systemd 236 added the EXTEND\_TIMEOUT\_USEC environment variable](https://lists.freedesktop.org/archives/systemd-devel/2017-December/039996.html) that allows services to extend the startup timeout during long-running processes. Starting with [MariaDB 10.1.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.33), [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), and [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.6), on systems with systemd versions that support it, MariaDB uses this feature to extend the startup timeout during certain startup processes that can run long. Therefore, if you are using `systemd` 236 or later, then you should not need to manually override `TimeoutStartSec`, even if your startup tasks, such as crash recovery, run for longer than the configured value. See [MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705) for more information.

### Stopping the MariaDB Server Process

MariaDB's `systemd` service can be stopped by executing the following:

```bash
sudo systemctl stop mariadb.service
```

### Restarting the MariaDB Server Process

MariaDB's `systemd` service can be restarted by executing the following:

```bash
sudo systemctl restart mariadb.service
```

### Checking the Status of the MariaDB Server Process

The status of MariaDB's `systemd` service can be obtained by executing the following:

```bash
sudo systemctl status mariadb.service
```

### Interacting with Multiple MariaDB Server Processes

On some operating systems, a `systemd` [template unit file](https://www.freedesktop.org/software/systemd/man/systemd.unit.html) called `mariadb@.service` is installed in `INSTALL_SYSTEMD_UNITDIR`. See [Contents of the MariaDB Service's Unit File](README.md#contents-of-the-mariadb-services-unit-file) for how to inspect the unit file on your system.

This template unit file allows you to interact with multiple MariaDB instances on the same system using the same template unit file. When you interact with a MariaDB instance using this template unit file, you have to provide an instance name as a suffix. For example, the following command tries to start a MariaDB instance with the name `node1`:

```bash
sudo systemctl start mariadb@node1.service
```

MariaDB's build system cannot include the `mariadb@.service` template unit file in [RPM](../../install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) packages on platforms that have [cmake](../../compiling-mariadb-from-source/generic-build-instructions.md#using-cmake) versions older than 3.3.0, because these `cmake` versions have a [bug](https://public.kitware.com/Bug/view.php?id=14782) that causes it to encounter errors when packaging a file in RPMs if the file name contains the `@` character. To use this functionality on a MariaDB version that does not have the file, you can copy the file from a package that contains the file.

#### Default Configuration of Multiple Instances

`systemd` also looks for an [option file](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) for a specific MariaDB instance based on the instance name.

It uses the `.%I` as the [custom option group suffix](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#custom-option-group-suffixes) that is appended to any [server option group](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#server-option-groups), in any configuration file included by default.

In all distributions, the `%I` is the MariaDB instance name. In the above `node1` case, it would use the [option file](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) at the path `/etc/mynode1.cnf`.

When using multiple instances, each instance also needs their own [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir), [socket](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#socket), and [port](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#port) (unless [`skip_networking`](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_networking) is specified). Because [mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md#option-groups) reads the same sections as the server, and `ExecStartPre=run mariadb-install-db` within the service, the instances are automatically created if there are sufficient privileges.

#### Custom Configuration of Multiple Instances

Because users may want to do many various things with their multiple instances, we've provided a way to let the user define how they wish their multiple instances to run. The systemd environment variable `MYSQLD_MULTI_INSTANCE` can be set to anything that [mariadbd](../mariadbd.md) and [mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md) recognize.

A hosting environment where each user has their own instance looks like this\
(with `sudo systemctl edit mariadb@.service`):

```ini
[Service]
ProtectHome=false
Environment='MYSQLD_MULTI_INSTANCE=--defaults-file=/home/%I/my.cnf \
                        --user=%I \
                        --socket=/home/%I.sock \ 
                        --datadir=/home/%I/mariadb_data \
                        --skip-networking'
```

Here the instance name is the unix user of the service.

## Systemd and Galera Cluster

### Bootstrapping a New Cluster

When using [Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide) with systemd, the first node in a cluster has to be started with `galera_new_cluster`. See [Getting Started with MariaDB Galera Cluster: Bootstrapping a New Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster#bootstrapping-a-new-cluster) for more information.

### Recovering a Node's Cluster Position

When using Galera Cluster with systemd, a node's position in the cluster can be recovered with `galera_recovery`. See [Getting Started with MariaDB Galera Cluster: Determining the Most Advanced Node](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster#determining-the-most-advanced-node) for more information.

### SSTs and Systemd

MariaDB's `systemd` unit file has a default startup timeout of about 90 seconds on most systems. If an SST takes longer than this default startup timeout on a joiner node, then `systemd` assumes that `mariadbd` has failed to startup, which causes `systemd` to kill the `mariadbd` process on the joiner node. To work around this, you can reconfigure the MariaDB `systemd` unit to have an [infinite timeout](configuring.md#configuring-the-systemd-service-timeout). See [Introduction to State Snapshot Transfers (SSTs): SSTs and Systemd](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts#ssts-and-systemd) for more information.

Note that [systemd 236 added the EXTEND\_TIMEOUT\_USEC environment variable](https://lists.freedesktop.org/archives/systemd-devel/2017-December/039996.html) that allows services to extend the startup timeout during long-running processes. On systems with `systemd` versions that support it, MariaDB uses this feature to extend the startup timeout during long SSTs. Therefore, if you are using `systemd` 236 or later, you do not need to manually override `TimeoutStartSec` even if your SSTs run for longer than the configured value. See [MDEV-15607](https://jira.mariadb.org/browse/MDEV-15607) for more information.

## Systemd Journal

`systemd` has its own logging system called the `systemd` journal. The `systemd` journal contains information about the service startup process. It is a good place to look when a failure has occurred.

The MariaDB `systemd` service's journal can be queried by using the [journalctl](https://www.freedesktop.org/software/systemd/man/journalctl.html) command:

```bash
$ sudo journalctl n 20 -u mariadb.service
-- Logs begin at Fri 2019-01-25 13:49:04 EST, end at Fri 2019-01-25 18:07:02 EST. --
Jan 25 13:49:15 ip-172-30-0-249.us-west-2.compute.internal systemd[1]: Starting MariaDB 10.1.37 database server...
Jan 25 13:49:16 ip-172-30-0-249.us-west-2.compute.internal mysqld[2364]: 2019-01-25 13:49:16 140547528317120 [Note] /usr/sbin/mysqld (mysqld 10.1.37-MariaDB) starting as process 2364 ...
Jan 25 13:49:17 ip-172-30-0-249.us-west-2.compute.internal systemd[1]: Started MariaDB 10.1.37 database server.
Jan 25 18:06:42 ip-172-30-0-249.us-west-2.compute.internal systemd[1]: Stopping MariaDB 10.1.37 database server...
Jan 25 18:06:44 ip-172-30-0-249.us-west-2.compute.internal systemd[1]: Stopped MariaDB 10.1.37 database server.
Jan 25 18:06:57 ip-172-30-0-249.us-west-2.compute.internal systemd[1]: Starting MariaDB 10.1.37 database server...
Jan 25 18:08:32 ip-172-30-0-249.us-west-2.compute.internal systemd[1]: mariadb.service start-pre operation timed out. Terminating.
Jan 25 18:08:32 ip-172-30-0-249.us-west-2.compute.internal systemd[1]: Failed to start MariaDB 10.1.37 database server.
Jan 25 18:08:32 ip-172-30-0-249.us-west-2.compute.internal systemd[1]: Unit mariadb.service entered failed state.
Jan 25 18:08:32 ip-172-30-0-249.us-west-2.compute.internal systemd[1]: mariadb.service failed.
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
