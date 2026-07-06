---
description: >-
  Start and stop MariaDB Server. This section covers service managers like
  systemd, the mariadbd and mariadbd-safe programs, startup options, and
  troubleshooting when the server won't start.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
---

# Starting & Stopping

{% columns %}
{% column %}
{% content-ref url="starting-and-stopping-mariadb-automatically.md" %}
[starting-and-stopping-mariadb-automatically.md](starting-and-stopping-mariadb-automatically.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete Starting and Stopping Overview guide for MariaDB. Complete reference documentation for implementation, configuration, and usage for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="launchd.md" %}
[launchd.md](launchd.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for configuring MariaDB to start automatically on macOS using a launchd plist file in /Library/LaunchDaemons.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="systemd/" %}
[systemd](systemd/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB on systemd (Linux): overview, supported distributions, and links to operational and configuration guidance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sysvinit.md" %}
[sysvinit.md](sysvinit.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes how to manage MariaDB using SysVinit scripts (mysql.server), common on older Linux distributions, using commands like `service` and `chkconfig`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadbd-safe.md" %}
[mariadbd-safe.md](mariadbd-safe.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details the `mariadbd-safe` wrapper script, which adds safety features like auto-restart upon crash and error logging to syslog.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadbd-multi.md" %}
[mariadbd-multi.md](mariadbd-multi.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to use `mariadbd-multi` to manage multiple MariaDB server processes on a single host using GNR groups in the configuration file.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadbd-options.md" %}
[mariadbd-options.md](mariadbd-options.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A reference list of command-line options available for the `mariadbd` server binary, covering configuration, replication, and service installation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadbd.md" %}
[mariadbd.md](mariadbd.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes the `mariadbd` binary (formerly `mysqld`), which is the core database server executable.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-server.md" %}
[mysql-server.md](mysql-server.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documentation for the `mysql.server` script, a SysVinit-style wrapper used to start and stop `mariadbd-safe`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="running-mariadb-from-the-build-directory.md" %}
[running-mariadb-from-the-build-directory.md](running-mariadb-from-the-build-directory.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for developers on how to run MariaDB directly from the source build directory without installing it to system paths.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="running-multiple-mariadb-server-processes.md" %}
[running-multiple-mariadb-server-processes.md](running-multiple-mariadb-server-processes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide on configuring and running multiple independent MariaDB instances on the same machine by isolating data directories, ports, and sockets.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="specifying-permissions-for-schema-data-directories-and-tables.md" %}
[specifying-permissions-for-schema-data-directories-and-tables.md](specifying-permissions-for-schema-data-directories-and-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains default file permissions for data directories and how to customize them using `UMASK` and `UMASK_DIR` environment variables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="switching-between-different-installed-mariadb-versions.md" %}
[switching-between-different-installed-mariadb-versions.md](switching-between-different-installed-mariadb-versions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for managing parallel installations of different MariaDB versions, typically using symlinks and separate data directories for testing.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="what-to-do-if-mariadb-doesnt-start.md" %}
[what-to-do-if-mariadb-doesnt-start.md](what-to-do-if-mariadb-doesnt-start.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete What to Do if MariaDB Doesn't Start guide for MariaDB. Complete reference documentation for implementation, configuration, and usage.
{% endcolumn %}
{% endcolumns %}
