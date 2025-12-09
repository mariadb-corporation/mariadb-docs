---
description: >-
  A guide on configuring and running multiple independent MariaDB instances on
  the same machine by isolating data directories, ports, and sockets.
---

# Running Multiple MariaDB Server Processes

It is possible to run multiple MariaDB Server processes on the same server, but there are certain things that need to be kept in mind. This page will go over some of those things.

## Configuring Multiple MariaDB Server Processes

If multiple MariaDB Server process are running on the same server, then at minimum, you will need to ensure that the different instances do not use the same [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir), [port](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#port), and [socket](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#socket). The following example shows these options set in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[client]
# TCP port to use to connect to mariadbd server
port=3306
# Socket to use to connect to mariadbd server
socket=/tmp/mysql.sock
[mariadb]
# TCP port to make available for clients
port=3306
#  Socket to make available for clients
socket=/tmp/mysql.sock
# Where MariaDB should store all its data
datadir=/usr/local/mysql/data
```

The above values are the defaults. If you would like to run multiple MariaDB Server instances on the same server, then you will need to set unique values for each instance.

There may be additional options that also need to be changed for each instance. Take a look at the full list of options for [mariadbd](mariadbd-options.md).

To see the current values set for an instance, see [Checking Program Options](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#checking-program-options) for how to do so.

To list the default values, check the end of the output of this command:

```bash
mariadbd --help --verbose
```

## Starting Multiple MariaDB Server Processes

There are several different methods to start or stop the MariaDB Server process. There are two primary categories that most of these methods fall into: starting the process with the help of a service manager, and starting the process manually. See [Starting and Stopping MariaDB](starting-and-stopping-mariadb-automatically.md) for more information.

If you want to run different MariaDB versions on the same machine, using [binary tarballs](../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md), [Docker](../automated-mariadb-deployment-and-administration/docker-and-mariadb/installing-and-using-mariadb-via-docker.md) or using Virtual Machines (VMs) are the recommended ways. A binary tarball uses least resources, Docker a bit more and a VM uses most resources.

### Service Managers

[sysVinit](sysvinit.md) and [systemd](systemd.md) are the most common Linux service managers. [launchd](launchd.md) is used in MacOS X. [Upstart](https://en.wikipedia.org/wiki/Upstart_\(software\)) is a less common service manager.

#### Systemd

RHEL/CentOS 7 and above, Debian 8 Jessie and above, and Ubuntu 15.04 and above use [systemd](systemd.md) by default.

For information on how to start and stop multiple MariaDB Server processes on the same server with this service manager, see [systemd: Interacting with Multiple MariaDB Server Processes](systemd.md#interacting-with-multiple-mariadb-server-processes).

### Starting the Server Process Manually

#### mariadbd

[mariadbd](mariadbd-options.md) is the actual MariaDB Server binary. It can be started manually on its own.

If you want to force each instance to read only a single [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then you can use the [--defaults-file](mariadbd-options.md#-defaults-file) option:

```
mariadbd --defaults-file=/etc/my_instance1.cnf
```

#### mariadbd-safe

[mariadbd-safe](mariadbd-safe.md) is a wrapper that can be used to start the [mariadbd](mariadbd-options.md) server process. The script has some built-in safeguards, such as automatically restarting the server process if it dies. See [mariadbd-safe](mariadbd-safe.md) for more information.

If you want to force each instance to read only a single [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then you can use the [--defaults-file](mariadbd-options.md#-defaults-file) option:

```
mariadbd-safe --defaults-file=/etc/my_instance1.cnf
```

#### mariadbd-multi

[mariadbd-multi](mariadbd-multi.md) is a wrapper that can be used to start the [mariadbd](mariadbd-options.md) server process if you plan to run multiple server processes on the same host. See [mariadbd-multi](mariadbd-multi.md) for more information.

## Other Options

In some cases, there may be easier ways to run multiple MariaDB Server instances on the same server, such as:

* Starting multiple [Docker](../automated-mariadb-deployment-and-administration/docker-and-mariadb/installing-and-using-mariadb-via-docker.md) containers.
* Using [dbdeployer](../../clients-and-utilities/administrative-tools/dbdeployer.md) (no longer maintained).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
