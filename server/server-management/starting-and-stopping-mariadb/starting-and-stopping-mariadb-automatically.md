---
description: >-
  An overview of methods to start and stop MariaDB, distinguishing between
  service managers (systemd, sysVinit, launchd) and manual commands (mariadbd,
  mariadbd-safe).
---

# Starting and Stopping Overview

There are several different methods to start or stop the MariaDB Server process. There are two primary categories that most of these methods fall into: starting the process with the help of a service manager, and starting the process manually.

## Service Managers

[sysVinit](sysvinit.md) and [systemd](systemd.md) are the most common Linux service managers. [launchd](launchd.md) is used in MacOS X. [Upstart](https://en.wikipedia.org/wiki/Upstart_\(software\)) is a less common service manager.

### Systemd

RHEL/CentOS 7 and above, Debian 8 Jessie and above, and Ubuntu 15.04 and above use [systemd](systemd.md) by default.

For information on how to start and stop MariaDB with this service manager, see [systemd: Interacting with the MariaDB Server Process](systemd.md#interacting-with-the-mariadb-server-process).

### SysVinit

RHEL/CentOS 6 and below, and Debian 7 Wheezy and below use [sysVinit](sysvinit.md) by default.

For information on how to start and stop MariaDB with this service manager, see [sysVinit: Interacting with the MariaDB Server Process](sysvinit.md#interacting-with-the-mariadb-server-process).

### launchd

[launchd](launchd.md) is used in MacOS X.

### Upstart

Ubuntu 14.10 and below use Upstart by default.

## Starting the Server Process Manually

### mariadbd

[mariadbd](mariadbd-options.md) is the actual MariaDB Server binary. It can be started manually on its own.

### mariadbd-safe

[mariadbd-safe](mariadbd-safe.md) is a wrapper that can be used to start the [mariadbd](mariadbd-options.md) server process. The script has some built-in safeguards, such as automatically restarting the server process if it dies. See [mariadbd-safe](mariadbd-safe.md) for more information.

### mariadbd-multi

[mariadbd-multi](mariadbd-multi.md) is a wrapper that can be used to start the [mariadbd](mariadbd-options.md) server process if you plan to run multiple server processes on the same host. See [mariadbd-multi](mariadbd-multi.md) for more information.

### mysql.server

[mysql.server](mysql-server.md) is a wrapper that works as a standard [sysVinit](sysvinit.md) script. However, it can be used independently of [sysVinit](sysvinit.md) as a regular `sh` script. The script starts the [mariadbd](mariadbd-options.md) server process by first changing its current working directory to the MariaDB install directory and then starting [mariadbd-safe](mariadbd-safe.md). The script requires the standard [sysVinit](sysvinit.md) arguments, such as `start`, `stop`, and `status`. See [mysql.server](mysql-server.md) for more information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
