---
description: >-
  A comprehensive guide to managing MariaDB with systemd, including unit file
  customization, startup timeouts, and handling multiple instances.
---

# systemd (Linux)

`systemd` is a [sysVinit](sysvinit.md) replacement that is the default service manager on the following Linux distributions:

* RHEL 7 and above
* CentOS 7 and above
* Fedora 15 and above
* Debian 8 and above
* Ubuntu 15.04 and above
* SLES 12 and above
* OpenSUSE 12.2 and above

MariaDB's `systemd` unit file is included in the server packages for [RPMs](../install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) and [DEBs](../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md). It is also included in certain [binary tarballs](../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md).

The service name is `mariadb.service`.

## Installing & Starting MariaDB

When installing MariaDB server rpm / dep package, it will automatically run the [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md) script, that creates the initial databases and users.

When MariaDB is started with the `systemd` unit file, it directly starts the [mariadbd](mariadbd-options.md) process as the `mysql` user. Unlike with [sysVinit](sysvinit.md), the [mariadbd](mariadbd-options.md) process is not started with [mariadbd-safe](mariadbd-safe.md). As a consequence, options will not be read from the `[mariadbd-safe]` [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

## Contents of the MariaDB Service's Unit File

The contents of the `mariadb.service` file can be examined with `systemctl show mariadb.service`.

## Interacting with the MariaDB Server Process

The service can be interacted with by using the [systemctl](https://www.freedesktop.org/software/systemd/man/systemctl.html) command.

### Starting the MariaDB Server Process on Boot

MariaDB's `systemd` service can be configured to start at boot by executing the following:

```
sudo systemctl enable mariadb.service
```

### Starting the MariaDB Server Process

MariaDB's `systemd` service can be started by executing the following:

```
sudo systemctl start mariadb.service
```

MariaDB's `systemd` unit file has a default startup timeout of about 90 seconds on most systems. If certain startup tasks, such as crash recovery, take longer than this default startup timeout, then `systemd` will assume that `mariadbd` has failed to startup, which causes `systemd` to kill the `mariadbd` process. To work around this, you can reconfigure the MariaDB `systemd` unit to have an [infinite timeout](systemd.md#configuring-the-systemd-service-timeout).

Note that [systemd 236 added the EXTEND\_TIMEOUT\_USEC environment variable](https://lists.freedesktop.org/archives/systemd-devel/2017-December/039996.html) that allows services to extend the startup timeout during long-running processes. Starting with [MariaDB 10.1.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10133-release-notes), [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes), and [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes), on systems with systemd versions that support it, MariaDB uses this feature to extend the startup timeout during certain startup processes that can run long. Therefore, if you are using `systemd` 236 or later, then you should not need to manually override `TimeoutStartSec`, even if your startup tasks, such as crash recovery, run for longer than the configured value. See [MDEV-14705](https://jira.mariadb.org/browse/MDEV-14705) for more information.

### Stopping the MariaDB Server Process

MariaDB's `systemd` service can be stopped by executing the following:

```
sudo systemctl stop mariadb.service
```

### Restarting the MariaDB Server Process

MariaDB's `systemd` service can be restarted by executing the following:

```
sudo systemctl restart mariadb.service
```

### Checking the Status of the MariaDB Server Process

The status of MariaDB's `systemd` service can be obtained by executing the following:

```
sudo systemctl status mariadb.service
```

### Interacting with Multiple MariaDB Server Processes

A `systemd` [template unit file](https://www.freedesktop.org/software/systemd/man/systemd.unit.html) with the name `mariadb@.service` is installed in `INSTALL_SYSTEMD_UNITDIR` on some systems. See [Locating the MariaDB Service's Unit File](systemd.md#locating-the-mariadb-services-unit-file) to see what directory that refers to on each distribution.

This template unit file allows you to interact with multiple MariaDB instances on the same system using the same template unit file. When you interact with a MariaDB instance using this template unit file, you have to provide an instance name as a suffix. For example, the following command tries to start a MariaDB instance with the name `node1`:

```
sudo systemctl start mariadb@node1.service
```

MariaDB's build system cannot include the `mariadb@.service` template unit file in [RPM](../install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) packages on platforms that have [cmake](../compiling-mariadb-from-source/generic-build-instructions.md#using-cmake) versions older than 3.3.0, because these [cmake](../compiling-mariadb-from-source/generic-build-instructions.md#using-cmake) versions have a [bug](https://public.kitware.com/Bug/view.php?id=14782) that causes it to encounter errors when packaging a file in RPMs if the file name contains the `@` character. MariaDB's RHEL 7 and CentOS 7 RPM build hosts only got a new enough [cmake](../compiling-mariadb-from-source/generic-build-instructions.md#using-cmake) version starting with [MariaDB 10.1.39](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10139-release-notes), [MariaDB 10.2.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10223-release-notes), and [MariaDB 10.3.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10314-release-notes). To use this functionality on a MariaDB version that does not have the file, you can copy the file from a package that does have the file.

#### Default configuration of Multiple Instances in 10.4 and Later

`systemd` will also look for an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) for a specific MariaDB instance based on the instance name.

It will use the `.%I` as the [custom option group suffix](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#custom-option-group-suffixes) that is appended to any [server option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#server-option-groups), in any configuration file included by default.

In all distributions, the `%I` is the MariaDB instance name. In the above `node1` case, it would use the [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) at the path`/etc/mynode1.cnf`.

When using multiple instances, each instance will of course also need their own [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir), [socket](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#socket) and , [port](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#port) (unless `[skip_networking](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#skip_networking) is specified). As [mariadb-install-db#option-groups](../../../clients-and-utilities/mariadb-install-db.md#option-groups) reads the same sections as the server, and`ExecStartPre=`run [mariadb-install-db](../../../clients-and-utilities/mariadb-install-db.md) within the service, the instances are autocreated if there is sufficient priviledges.`

To use a 10.3 configuration in 10.4 or later and the following customisation in the editor after running `sudo systemctl edit mariadb@.service`:

```
[Unit]
ConditionPathExists=

[Service]
Environment='MYSQLD_MULTI_INSTANCE=--defaults-file=/etc/my%I.cnf'
```

#### Custom configuration of Multiple Instances in 10.4 and Later

Because users may want to do many various things with their multiple instances, we've provided a way to let the user define how they wish their multiple instances to run. The systemd environment variable `MYSQLD_MULTI_INSTANCE` can be set to anything that [mariadbd](mariadbd.md) and [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md) will recognise.

A hosting environment where each user has their own instance may look like\
(with `sudo systemctl edit mariadb@.service`):

```
[Service]
ProtectHome=false
Environment='MYSQLD_MULTI_INSTANCE=--defaults-file=/home/%I/my.cnf \
                        --user=%I \
                        --socket=/home/%I.sock \ 
                        --datadir=/home/%I/mariadb_data \
                        --skip-networking'
```

Here the instance name is the unix user of the service.

#### Configuring Multiple Instances in 10.3 and Earlier

`systemd` will also look for an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) for a specific MariaDB instance based on the instance name. By default, it will look for the option file in a directory defined at build time by the `INSTALL_SYSCONF2DIR` option provided to [cmake](../compiling-mariadb-from-source/generic-build-instructions.md#using-cmake).

For example, on RHEL, CentOS, Fedora, and other similar Linux distributions, `INSTALL_SYSCONF2DIR` is defined as `/etc/my.cnf.d/`, so it will look for an option file that matches the format:

* `/etc/my.cnf.d/my%I.cnf`

And on Debian, Ubuntu, and other similar Linux distributions, `INSTALL_SYSCONF2DIR` is defined as `/etc/mysql/conf.d//`, so it will look for an option file that matches the format:

* `/etc/mysql/conf.d/my%I.cnf`

In all distributions, the `%I` is the MariaDB instance name. In the above `node1` case, it would use the [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) at the path`/etc/my.cnf.d/mynode1.cnf` for RHEL-like distributions and `/etc/mysql/conf.d/mynode1.cnf` for Debian-like distributions.

When using multiple instances, each instance will of course also need their own [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir). See [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md) for information on how to initialize the [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir) for additional MariaDB instances.

## Systemd and Galera Cluster

### Bootstrapping a New Cluster

When using [Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide) with systemd, the first node in a cluster has to be started with `galera_new_cluster`. See [Getting Started with MariaDB Galera Cluster: Bootstrapping a New Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster#bootstrapping-a-new-cluster) for more information.

### Recovering a Node's Cluster Position

When using Galera Cluster with systemd, a node's position in the cluster can be recovered with `galera_recovery`. See [Getting Started with MariaDB Galera Cluster: Determining the Most Advanced Node](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster#determining-the-most-advanced-node) for more information.

### SSTs and Systemd

MariaDB's `systemd` unit file has a default startup timeout of about 90 seconds on most systems. If an SST takes longer than this default startup timeout on a joiner node, then `systemd` will assume that `mariadbd` has failed to startup, which causes `systemd` to kill the `mariadbd` process on the joiner node. To work around this, you can reconfigure the MariaDB `systemd` unit to have an [infinite timeout](systemd.md#configuring-the-systemd-service-timeout). See [Introduction to State Snapshot Transfers (SSTs): SSTs and Systemd](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts#ssts-and-systemd) for more information.

Note that [systemd 236 added the EXTEND\_TIMEOUT\_USEC environment variable](https://lists.freedesktop.org/archives/systemd-devel/2017-December/039996.html) that allows services to extend the startup timeout during long-running processes. Starting with [MariaDB 10.1.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10135-release-notes), [MariaDB 10.2.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10217-release-notes), and [MariaDB 10.3.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1038-release-notes), on systems with systemd versions that support it, MariaDB uses this feature to extend the startup timeout during long SSTs. Therefore, if you are using `systemd` 236 or later, then you should not need to manually override `TimeoutStartSec`, even if your SSTs run for longer than the configured value. See [MDEV-15607](https://jira.mariadb.org/browse/MDEV-15607) for more information.

## Configuring the Systemd Service

You can configure MariaDB's `systemd` service by creating a "drop-in" configuration file for the `systemd` service. On most systems, the `systemd` service's directory for "drop-in" configuration files is `/etc/systemd/system/mariadb.service.d/`. You can confirm the directory and see what "drop-in" configuration files are currently loaded by executing:

```
$ sudo systemctl status mariadb.service
● mariadb.service - MariaDB 10.1.37 database server
   Loaded: loaded (/usr/lib/systemd/system/mariadb.service; enabled; vendor preset: disabled)
  Drop-In: /etc/systemd/system/mariadb.service.d
           └─migrated-from-my.cnf-settings.conf, timeoutstartsec.conf
...
```

If you want to configure the `systemd` service, then you can create a file with the `.conf` extension in that directory. The configuration option(s) that you would like to change would need to be placed in an appropriate section within the file, usually `[Service]`. If a `systemd` option is a list, then you may need to set the option to empty before you set the replacement values. For example:

```
[Service]

ExecStart=
ExecStart=/usr/bin/numactl --interleave=all  /usr/sbin/mariadbd $MYSQLD_OPTS $_WSREP_NEW_CLUSTER $_WSREP_START_POSITION
```

After any configuration change, you will need to execute the following for the change to go into effect:

```
sudo systemctl daemon-reload
```

### Useful Systemd Options

Useful `systemd` options are listed below. If an option is equivalent to a common [mariadbd-safe](mariadbd-safe.md) option, then that is also listed. Use `systemctl edit mariadb.service` to create the systemd option under a `[Service]` section header.

| mariadbd-safe option                                                   | systemd option                                                                                                                    | Comments                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| no option                                                              | [ProtectHome=false](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#ProtectHome=)                              | If any MariaDB files are in /home/                                                                                                                                                                                                                      |
| no option                                                              | [PrivateDevices=false](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#PrivateDevices=)                        | If any MariaDB storage references raw block devices                                                                                                                                                                                                     |
| no option                                                              | [ProtectSystem=](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#ProtectSystem=)                               | If any MariaDB write any files to anywhere under /boot, /usr or /etc                                                                                                                                                                                    |
| no option                                                              | [TimeoutStartSec={time}](https://www.freedesktop.org/software/systemd/man/systemd.service.html#TimeoutStartSec=)                  | Service startup timeout. See [Configuring the Systemd Service Timeout](systemd.md#configuring-the-systemd-service-timeout).                                                                                                                             |
| no option (see [MDEV-9264](https://jira.mariadb.org/browse/MDEV-9264)) | [OOMScoreAdjust={priority}](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#OOMScoreAdjust=)                   | e.g. -600 to lower priority of OOM killer for mariadbd                                                                                                                                                                                                  |
| [open-files-limit](mariadbd-safe.md#options)                           | [LimitNOFILE={limit}](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#LimitCPU=)                               | Limit on number of open files. See [Configuring the Open Files Limit](systemd.md#configuring-the-open-files-limit).                                                                                                                                     |
| [core-file-size](mariadbd-safe.md#options)                             | [LimitCORE={size}](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#LimitCPU=)                                  | Limit on core file size. Useful when [enabling core dumps](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/enabling-core-dumps). See [Configuring the Core File Size](systemd.md#configuring-the-core-file-size). |
|                                                                        | [LimitMEMLOCK={size}](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#LimitCPU=) or infinity                   | Limit on how much can be locked in memory. Useful when [large-pages](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#large_pages) or [memlock](mariadbd-options.md#-memlock) is used                       |
| [nice](mariadbd-safe.md#options)                                       | [Nice={nice value}](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#Nice=)                                     |                                                                                                                                                                                                                                                         |
| [syslog](mariadbd-safe.md#options)                                     | [StandardOutput=syslog](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#StandardOutput=)                       | See [Configuring MariaDB to Write the Error Log to Syslog](systemd.md#configuring-mariadb-to-write-the-error-log-to-syslog).                                                                                                                            |
|                                                                        | [StandardError=syslog](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#StandardError=)                         |                                                                                                                                                                                                                                                         |
|                                                                        | [SyslogFacility=daemon](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#SyslogFacility=)                       |                                                                                                                                                                                                                                                         |
|                                                                        | [SyslogLevel=err](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#SyslogLevel=)                                |                                                                                                                                                                                                                                                         |
| [syslog-tag](mariadbd-safe.md#options)                                 | [SyslogIdentifier](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#SyslogIdentifier=)                          |                                                                                                                                                                                                                                                         |
| [flush-caches](mariadbd-safe.md#options)                               | ExecStartPre=/usr/bin/sync                                                                                                        |                                                                                                                                                                                                                                                         |
|                                                                        | ExecStartPre=/usr/sbin/sysctl -q -w vm.drop\_caches=3                                                                             |                                                                                                                                                                                                                                                         |
| [malloc-lib](mariadbd-safe.md#options)                                 | [Environment=LD\_PRELOAD=/path/to/library](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#Environment=)       |                                                                                                                                                                                                                                                         |
| [numa-interleave](mariadbd-safe.md#options)                            | [NUMAPolicy=interleave](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#NUMAPolicy=)                           | from systemd v243 onwards                                                                                                                                                                                                                               |
|                                                                        | or: ExecStart=/usr/bin/numactl --interleave=all /usr/sbin/mariadbd $MYSQLD\_OPTS $\_WSREP\_NEW\_CLUSTER $\_WSREP\_START\_POSITION | prepending ExecStart=/usr/bin/numactl --interleave=all to existing ExecStart setting                                                                                                                                                                    |
| [no-auto-restart](mariadbd-safe.md#options)                            | Restart={exit-status}                                                                                                             |                                                                                                                                                                                                                                                         |

Note: the [systemd](https://www.freedesktop.org/software/systemd/man/systemd.service.html) manual contains the official meanings for these options. The manual also lists considerably more options than the ones listed above.

There are other options and the `mariadb-service-convert` script will attempt to convert these as accurately as possible.

### Configuring the Systemd Service Timeout

MariaDB's [systemd](systemd.md) unit file has a default startup timeout of about 90 seconds on most systems. If a service startup takes longer than this default startup timeout, then `systemd` will assume that `mariadbd` has failed to startup, which causes `systemd` to kill the `mariadbd` process. To work around this, it can be changed by configuring the [TimeoutStartSec](https://www.freedesktop.org/software/systemd/man/systemd.service.html#TimeoutStartSec=) option for the `systemd` service.

A similar problem can happen when stopping the MariaDB service. Therefore, it may also be a good idea to set [TimeoutStopSec](https://www.freedesktop.org/software/systemd/man/systemd.service.html#TimeoutStopSec=).

For example, you can reconfigure the MariaDB `systemd` service to have an infinite timeout by executing one of the following commands:

If you are using `systemd` 228 or older, then you can execute the following to set an infinite timeout:

```
sudo systemctl edit mariadb.service

[Service]

TimeoutStartSec=0
TimeoutStopSec=0
```

[Systemd 229 added the infinity option](https://lists.freedesktop.org/archives/systemd-devel/2016-February/035748.html), so if you are using `systemd` 229 or later, then you can execute the following to set an infinite timeout:

```
sudo systemctl edit mariadb.service

[Service]

TimeoutStartSec=infinity
TimeoutStopSec=infinity
```

Note that [systemd 236 added the EXTEND\_TIMEOUT\_USEC environment variable](https://lists.freedesktop.org/archives/systemd-devel/2017-December/039996.html) that allows services to extend the startup timeout during long-running processes. On systems with systemd versions that support it, MariaDB uses this feature to extend the startup timeout during certain startup processes that can run long.

### Configuring the Open Files Limit

When using `systemd`, rather than setting the open files limit by setting the [open-files-limit](mariadbd-safe.md#mariadbd-safe-options) option for `mariadbd-safe` or the [open\_files\_limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#open_files_limit) system variable, the limit can be changed by configuring the [LimitNOFILE](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#LimitCPU=) option for the MariaDB `systemd` service. The default is set to `LimitNOFILE=16364` in `mariadb.service`.

For example, you can reconfigure the MariaDB `systemd` service to have a larger limit for open files by executing the following commands:

```
sudo systemctl edit mariadb.service

[Service]

LimitNOFILE=infinity
```

An important note is that setting `LimitNOFILE=infinity` doesn't actually set the open file limit to _infinite_.

In `systemd` 234 and later, setting `LimitNOFILE=infinity` actually sets the open file limit to the value of the kernel's `fs.nr_open` parameter. Therefore, in these `systemd` versions, you may have to change this parameter's value.

The value of the `fs.nr_open` parameter can be changed permanently by setting the value in [/etc/sysctl.conf](https://linux.die.net/man/5/sysctl.conf) and restarting the server.

The value of the `fs.nr_open` parameter can be changed temporarily by executing the [sysctl](https://linux.die.net/man/8/sysctl) utility. For example:

```
sudo sysctl -w fs.nr_open=1048576‬
```

In `systemd` 233 and before, setting `LimitNOFILE=infinity` actually sets the open file limit to `65536`. See [systemd issue #6559](https://github.com/systemd/systemd/issues/6559) for more information. Therefore, in these `systemd` versions, it is not generally recommended to set `LimitNOFILE=infinity`. Instead, it is generally better to set `LimitNOFILE` to a very large integer. For example:

```
sudo systemctl edit mariadb.service

[Service]
LimitNOFILE=1048576
```

### Configuring the Core File Size

When using `systemd`, if you would like to [enable core dumps](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/enabling-core-dumps), rather than setting the core file size by setting the [core-file-size](mariadbd-safe.md#mariadbd-safe-options) option for `mariadbd-safe`, the limit can be changed by configuring the [LimitCORE](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#LimitCPU=) option for the MariaDB `systemd` service. For example, you can reconfigure the MariaDB `systemd` service to have an infinite size for core files by executing the following commands:

```
sudo systemctl edit mariadb.service

[Service]
LimitCORE=infinity
```

### Configuring MariaDB to Write the Error Log to Syslog

When using `systemd`, if you would like to redirect the [error log](../server-monitoring-logs/error-log.md) to the [syslog](https://linux.die.net/man/8/rsyslogd), then that can easily be done by doing the following:

* Ensure that [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) system variable is not set.
* Set [StandardOutput=syslog](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#StandardOutput=).
* Set [StandardError=syslog](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#StandardError=).
* Set [SyslogFacility=daemon](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#SyslogFacility=).
* Set [SysLogLevel=err](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#SyslogLevel=).

For example:

```
sudo systemctl edit mariadb.service

[Service]

StandardOutput=syslog
StandardError=syslog
SyslogFacility=daemon
SysLogLevel=err
```

If you have multiple instances of MariaDB, then you may also want to set [SyslogIdentifier](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#SyslogIdentifier=) with a different tag for each instance.

### Configuring LimitMEMLOCK

If using [--memlock](mariadbd-options.md#-memlock), or the io\_uring asyncronious IO in InnoDB in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106) or above, with a Linux Kernel version < 5.12, you will need to raise the LimitMEMLOCK limit.

```
sudo systemctl edit mariadb.service

[Service]

LimitMEMLOCK=2M
```

Note: Prior to [MariaDB 10.1.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10110-release-notes), the [--memlock](mariadbd-options.md#-memlock) option could not be used with the MariaDB `systemd` service.

### Configuring Access to Home Directories

MariaDB's [systemd](systemd.md) unit file restricts access to `/home`, `/root`, and `/run/user` by default. This restriction can be overridden by setting the [ProtectHome](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#ProtectHome=) option to `false` for the MariaDB `systemd` service. This is done by creating a "drop-in" directory `/etc/systemd/system/mariadb.service.d/` and in it a file with a `.conf` suffix that contains the `ProtectHome=false` directive.

You can reconfigure the MariaDB `systemd` service to allow access to `/home` by executing the following commands:

```
sudo systemctl edit mariadb.service

[Service]

ProtectHome=false
```

### Configuring the umask

When using `systemd`, the default file permissions of `mariadbd` can be set by setting the `UMASK` and `UMASK_DIR` environment variables for the `systemd` service. For example, you can configure the MariaDB `systemd` service's umask by executing the following commands:

```
sudo systemctl edit mariadb.service

[Service]

Environment="UMASK=0750"
Environment="UMASK_DIR=0750"
```

These environment variables do not set the umask. They set the default file system permissions. See [MDEV-23058](https://jira.mariadb.org/browse/MDEV-23058) for more information.

Keep in mind that configuring the umask this way will only affect the permissions of files created by the `mariadbd` process that is managed by `systemd`. The permissions of files created by components that are not managed by `systemd`, such as [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md), will not be affected.

See [Specifying Permissions for Schema (Data) Directories and Tables](specifying-permissions-for-schema-data-directories-and-tables.md) for more information.

### Configuring the data directory

When doing a standard binary tarball install the datadir will be under /usr/local/data. The default systemd service file makes the whole /usr directory tree write protected however.

So when just copying the distributed service file a tarball install will not start up, complaining e.g. about

```
[Warning] Can't create test file /usr/local/.../data/ubuntu-focal.lower-test
[ERROR] mariadbd: File '/usr/local/.../data/aria_log_control' not found (Errcode: 30 "Read-only file system")
[ERROR] mariadbd: Got error 'Can't open file' when trying to use aria control file '/usr/local/.../data/aria_log_control'
```

So when using a data directory under /usr/local that specific directory needs to be made writable for the service using the ReadWritePaths setting:

```
sudo systemctl edit mariadb.service

[Service]
ReadWritePaths=/usr/local/mysql/data
```

## Systemd Socket Activation

**MariaDB starting with** [**10.6.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes)

MariaDB can use systemd's socket activation.

This is an on-demand service for MariaDB that will activate when required.

Systemd socket activation uses a `mariadb.socket` definition file to define a set of UNIX and TCP sockets. Systemd will listen on these sockets, and when they are connected to, systemd will start the `mariadb.service` and hand over the socket file descriptors for MariaDB to process the connection.

MariaDB remains running at this point and will have all sockets available and process connections exactly like it did before 10.6.

When MariaDB is shut down, the systemd `mariadb.socket` remains active, and a new connection will restart the `mariadb.service`.

### Using Systemd Socket Activation

To use MariaDB systemd socket activation, instead of enabling/starting `mariadb.service`, `mariadb.socket` is used instead.

So the following commands work exactly like the `mariadb.service` equivalents.

```
systemctl start mariadb.socket
systemctl enable mariadb.socket
```

These files alone only contain the UNIX and TCP sockets and basic network connection information to which will be listening for connections. `@mariadb` is a UNIX abstract socket, which means it doesn't appear on the filesystem. Connectors based on MariaDB Connector/C will be able to connect with these by using the socket name directly, provided the higher level implementation doesn't try to test for the file's existence first. Some connectors like PHP use mysqlnd that is a pure PHP implementation and as such will only be able to connect to on filesystem UNIX sockets.

With systemd activated sockets there is only a file descriptor limit on the number of listening sockets that can be created.

### When to Use Systemd Socket Activation

A common use case for systemd socket activated MariaDB is when there needs to be a quick boot up time. MariaDB needs to be ready to run, but it doesn't need to be running.

The ideal use case for systemd socket activation for MariaDB is for infrastructure providers running many multiple instances of MariaDB, where each instance is dedicated for a user.

### Downsides to Using Systemd Socket Activiation

From the time the connection occurs, the client is going to be waiting until MariaDB has fully initialized before MariaDB can process the awaiting connection. If MariaDB was previously hard shutdown and needs to perform an extensive InnoDB rollback, then the activation time may be larger than the desired wait time of the client connection.

### Configuring Systemd Socket Activation

When MariaDB is run under systemd socket activation, the usual [socket](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#socket) , [port](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#port), and [backlog](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#backlog) system variables are ignored, as these settings are contained within the systemd socket definition file.

There is no configuration required in MariaDB to use MariaDB under socket activation.

The systemd options available are from the [systemd documentation](https://www.freedesktop.org/software/systemd/man/systemd.socket.html), however [ListenStream](https://www.freedesktop.org/software/systemd/man/systemd.socket.html#ListenStream=) and [BackLog](https://www.freedesktop.org/software/systemd/man/systemd.socket.html#Backlog=) would be the most common configuration options.

As MariaDB isn't creating these sockets, the sockets don't need to be created with a `mysql` user. The sockets MariaDB may end up listening to under systemd socket activation, it may have not had the privileges to create itself.

Changes to the default `mariadb.socket` can be made in the same way as services, `systemctl edit mariadb.socket`, or using `/etc/systemd/system/mariadb.socket.d/someconfig.conf` files.

### Extra Port

A systemd socket can be configured as an [extra\_port](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#extra_port), by using the`[FileDescriptorName=extra](https://www.freedesktop.org/software/systemd/man/systemd.socket.html#FileDescriptorName=) in the`.socket`file.`

The `mariadb-extra.socket` is already packaged and ready for use.

### Multi-instance socket activation

`mariadb@.socket` is MariaDB's packaged multi-instance defination. It creates multiple UNIX sockets based on the socket file started.

Starting `mariadb@bob.socket` will use the `mariadb@.socket` defination with `%I` within the defination replaced with "bob".

When something connects to a socket defined there, the `mariadb@bob.service` will be started.

## Systemd Socket Activation for Hosting Service Providers

A systemd socket activation service with multi-instance can provide an on-demand per user access to a hosting service provider's dedicated database.

"User", in this case, refers to the customer of the hosting service provider.

### End User Benefits

This provides the following benefits for the user:

* Each user has their own dedicated instance with the following benefits:
  * The instance is free from the database contention of neighbors on MariaDB shared resources (table cache, connections, etc)
  * The user is free to change their own configuration of MariaDB, within the limits and permissions of the service provider.
  * Database service level backups, like mariadb-backup, are now directly available.
  * A user can install their own plugins.
  * The user can run a different database version to their neighbors.
  * If a user's neighbor triggers a fault in the server, the uder's instance isn't affected.
* The database runs as their unix user in the server facilitating:
  * User can directly migrate their MariaDB data directory to a different provider.
  * The user's data is protected from other users on a kernel level.

### Hosting Service Provider Benefits

In addition to providing user benefits as a sales item, the following are additional benefits for the hosting service provider compared to a monolith service:

* Without passwords for the database, while still having security, support may be easier.
* When a user's database isn't active, there is no resource usage, only listening file descriptors by systemd.
* The socket activation transparently, with a minor startup time, starts the service as required.
* When the user's database hasn't had any activity after a time, it will deactivate ([MDEV-25282](https://jira.mariadb.org/browse/MDEV-25282)).
* Planned enhancements in InnoDB provide:
  * an on-demand consumption of memory ([MDEV-25340](https://jira.mariadb.org/browse/MDEV-25340) .
  * a proactive reduction in memory ([MDEV-25341](https://jira.mariadb.org/browse/MDEV-25341)).
  * a memory resource pressure reduction in memory use ([MDEV-24670](https://jira.mariadb.org/browse/MDEV-24670)).
* The service provider can still cap the user's database memory usage in a ulimit way that a user cannot override in settings.
* The service provider may choose a CPU/memory/IO based billing to the user on Linux cgroup accounting rather than the available comprared to the rather limited options in [CREATE USER](../../reference/sql-statements/account-management-sql-statements/create-user.md).
* Because a user's database will shutdown when inactive, a database upgrade on the server will not take effect for the user until it passively shuts down, restarts, and then gets reactivated hence reducing user downtime..

### Downsides to the Hosting Service Provider

The extra memory used by more instances. This is mitigated by the on-demand activation. The deactivation when idle, and improved InnoDB memory management.

With plenty of medium size database servers running, the Linux OOM kill has the opportunity to kill off only a small number of database servers running rather than everyones.

### Example on configuration Items for a per user, systemd socket activitated multi-instance service

From a server pespective the operation would be as follows;

To make the socket ready to connect and systemd will be listening to the socket:

```
# systemctl start mariadb@username.socket
# systemctl start mariadb-extra@username.socket
```

To enable this on reboot (the same way as a systemd service):

```
# systemctl enable mariadb@username.socket
# systemctl enable mariadb-extra@username.socket
```

#### A MariaDB Template File

A global template file. Once installed as a user's `$HOME/.my.cnf` file, it will becomes the default for many applications, and the MariaDB server itself.

```
# cat /etc/my.cnf.templ
[client]
socket=/home/USER/mariadb.sock

[client-server]
user=USER

[mariadbd]
datadir=/home/USER/mariadb-datadir
```

#### Custom Configuration for the Multi-instance Service

This extends/modifies the MariaDB multi-instance service.

The feature of this extension are:

* that it will autocreate configuration file for user applications
* It will install the database on first service start
* `auth-root-*` in [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md) means that the user is their own privileged user with unix socket authentication active. This means non-that user cannot access another users service, even with\
  access to the unix socket(s). For more information see [unix socket authentication security](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md#security).
* If the MariaDB version was upgrade, the upgrade changes are made automatically
* `LimitData` places a hard upper limit so the user doesn't exceed a portion of the server resources

```
# cat /etc/systemd/system/mariadb@.service.d/user.conf
[Service]
User=%I
ProtectHome=false

Environment=MYSQLD_MULTI_INSTANCE="--defaults-file=/home/%I/.my.cnf"

ExecStartPre=
ExecStartPre=/bin/sh -c "[ -f /home/%I/.my.cnf ] || sed -e \"s/USER/%I/g\" /etc/my.cnf.templ > /home/%I/.my.cnf"
ExecStartPre=mkdir -p /home/%I/mariadb-datadir
ExecStartPre=/usr/bin/mariadb-install-db $MYSQLD_MULTI_INSTANCE --rpm \
   --auth-root-authentication-method=socket --auth-root-socket-user=%I
ExecStartPost=/usr/bin/mariadb-upgrade $MYSQLD_MULTI_INSTANCE

# To limit user based tuning
LimitData=768M
# For io_uring use by innodb on < 5.12 kernels
LimitMEMLOCK=1M
```

#### Custom Configuration for the Multi-instance Socket

This extends/modifies the MariaDB socket defination to be per user.

Create sockets based on the user of the istance (`%I`). Permissions are only necessary in the sense that the user can connect to them. It won't matter to the server. Access control is enforced within the server, however if the user web services are run as the user, `Mode=777` can be reduced. `@mariadb-%I` is a abstract unix socket not on the filesystem. It may help if a user is in a chroot. Not all applications can connect to abstract sockets.

```
# cat /etc/systemd/system/mariadb@.socket.d/user.conf
[Socket]
SocketUser=%I
SocketMode=777
ListenSteam=
ListenStream=@mariadb-%I
ListenStream=/home/%I/mariadb.sock
```

The extra socket provides the user the ability to access the server when all max-connections are used:

```
# cat /etc/systemd/system/mariadb-extra@.socket.d/user.conf
[Socket]
SocketUser=%I
SocketMode=777
ListenSteam=
ListenStream=@mariadb-extra-%I
ListenStream=/home/%I/mariadb-extra.sock
```

## Systemd Journal

`systemd` has its own logging system called the `systemd` journal. The `systemd` journal contains information about the service startup process. It is a good place to look when a failure has occurred.

The MariaDB `systemd` service's journal can be queried by using the [journalctl](https://www.freedesktop.org/software/systemd/man/journalctl.html) command. For example:

```
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

## Converting mariadbd-safe Options to Systemd Options

`mariadb-service-convert` is a script included in many MariaDB packages that is used by the package manager to convert [mariadbd-safe](mariadbd-safe.md#mariadbd-safe-options) options to `systemd` options. It reads any explicit settings in the `[mariadbd-safe]` [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), and its output is directed to `/etc/systemd/system/mariadb.service.d/migrated-from-my.cnf-settings.conf`. This helps to keep the configuration the same when upgrading from a version of MariaDB that does not use `systemd` to one that does.

Implicitly high defaults of [open-files-limit](mariadbd-safe.md#mariadbd-safe-options) may be missed by the conversion script and require explicit configuration. See [Configuring the Open Files Limit](systemd.md#configuring-the-open-files-limit).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
