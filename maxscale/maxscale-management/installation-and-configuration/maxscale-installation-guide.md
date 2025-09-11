# MaxScale Installation Guide

## MariaDB MaxScale Installation Guide

We recommend to install MaxScale on a separate server, to ensure that there can be no competition of resources between MaxScale and a MariaDB Server that it manages.

### Install MariaDB MaxScale From MariaDB Repositories

The recommended approach is to use [the MariaDB package repository](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) to install MaxScale. After enabling the repository by following the instructions, MaxScale can be installed with the following commands.

* For RHEL/Rocky Linux/Alma Linux, use `dnf install maxscale`.
* For Debian and Ubuntu, run `apt update` followed by `apt install maxscale`.
* For SLES, use `zypper install maxscale`.

### Install MariaDB MaxScale From a RPM/DEB Package

Download the correct MaxScale package for your CPU architecture and operating system from [the MariaDB Downloads page](https://mariadb.com/downloads/community/maxscale/). MaxScale can be installed with the following commands.

* For RHEL/Rocky Linux/Alma Linux, use `dnf install /path/to/maxscale-*.rpm`
* For Debian and Ubuntu, use `apt install /path/to/maxscale-*.deb`.
* For SLES, use `zypper install /path/to/maxscale-*.rpm`.

### Install MariaDB MaxScale Using a Tarball

MaxScale can also be installed using a tarball. This may be required if you are using a Linux distribution for which there exist no installation package or if you want to install many different MaxScale versions side by side. For instructions on how to do that, please refer to [Install MariaDB MaxScale using a Tarball](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-installing-mariadb-maxscale-using-a-tarball.md).

### Building MariaDB MaxScale From Source Code

Alternatively, you may download the MariaDB MaxScale source and build your own binaries. To do this, refer to the separate document [Building MariaDB MaxScale from Source Code](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-building-mariadb-maxscale-from-source-code.md).

### Assumptions

#### Memory allocation behavior

MaxScale assumes that memory allocations always succeed and in general does not check for memory allocation failures. This assumption is compatible with the Linux kernel parameter [vm.overcommit\_memory](https://www.kernel.org/doc/Documentation/vm/overcommit-accounting) having the value `0`, which is also the default on most systems.

With `vm.overcommit_memory` being `0`, memory _allocations_ made by an application never fail, but instead the application may be killed by the so-called OOM (out-of-memory) killer if, by the time the application\
actually attempts to _use_ the allocated memory, there is not available free memory on the system.

If the value is `2`, then a memory allocation made by an application may fail and unless the application is prepared for that possibility, it will likely crash with a SIGSEGV. As MaxScale is not prepared to handle memory allocation failures, it will crash in this situation.

The current value of `vm.overcommit_memory` can be checked with this command:

```bash
sysctl vm.overcommit_memory
```

Alternatively, use this command:

```bash
cat /proc/sys/vm/overcommit_memory
```

### Configuring MariaDB MaxScale

[The MaxScale Tutorial](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-setting-up-mariadb-maxscale.md) covers the first steps in configuring your MariaDB MaxScale installation. Follow this tutorial to learn how to configure and start using MaxScale.

For a detailed list of all configuration parameters, refer to the [Configuration Guide](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md) and the module specific documents listed in the [Documentation Contents](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-2501-contents.md).

### Encrypting Passwords

Read the [Encrypting Passwords](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md) section of the configuration guide to set up password encryption for the\
configuration file.

### Administration Of MariaDB MaxScale

There are various administration tasks that may be done with MariaDB MaxScale. A command line tools is available, [maxctrl](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-reference/mariadb-maxscale-2501-maxscale-2501-maxctrl.md), that interacts with a running MariaDB MaxScale and allows the status of MariaDB MaxScale to be monitored and give some control of the MariaDB MaxScale functionality.

[The administration tutorial](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-administration-tutorial.md) covers the common administration tasks that need to be done with MariaDB MaxScale.

### Copying or Backing Up MaxScale

The main configuration file for MaxScale is in `/etc/maxscale.cnf` and additional user-created configuration files are in`/etc/maxscale.cnf.d/`. Objects created or modified at runtime are stored in`/var/lib/maxscale/maxscale.cnf.d/`. Some modules also store internal data in`/var/lib/maxscale/` named after the module or the configuration object.

The simplest way to back up the configuration and runtime data of a MaxScale installation is to create an archive from the following files and directories:

* `/etc/maxscale.cnf`
* `/etc/maxscale.cnf.d/`
* `/var/lib/maxscale/`

This can be done with the following command:

```bash
tar -caf maxscale-backup.tar.gz /etc/maxscale.cnf /etc/maxscale.cnf.d/ /var/lib/maxscale/
```

If MaxScale is configured to store data in custom locations, these should be included in the backup as well.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
