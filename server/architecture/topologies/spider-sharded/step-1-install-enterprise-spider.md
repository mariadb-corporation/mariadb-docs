# Step 1: Install Enterprise Spider

## Overview

This page details step 1 of the 3-step procedure "[Deploy Spider Sharded Topology](./)".

This step installs the [Enterprise Spider storage engine](../../../server-usage/storage-engines/spider/) plugin on the Spider Node.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Allow Interconnect

MariaDB Enterprise Spider depends on interconnect between the Spider Node and all Data Nodes. This may require adjustment to firewall and security settings.

## Install Spider Package

The [Enterprise Spider storage engine](../../../server-usage/storage-engines/spider/) plugin is not installed with MariaDB Enterprise Server by default. An additional package must be installed.

### Install via YUM (CentOS, RHEL)

On the Spider Node, install MariaDB Enterprise Spider:

```bash
$ sudo yum install MariaDB-spider-engine
```

Install via APT (Debian, Ubuntu)

On the Spider Node, install MariaDB Enterprise Spider:

```bash
$ sudo apt install mariadb-plugin-spider
```

### Install via ZYpp (SLES)

On the Spider Node, install MariaDB Enterprise Spider:

```bash
$ sudo zypper install MariaDB-spider-engine
```

## Load the Spider Plugin

The [Enterprise Spider storage engine](../../../server-usage/storage-engines/spider/) plugin must be loaded by MariaDB Enterprise Server

**On the Spider Node**, use one of the following methods to configure MariaDB Enterprise Server to load the Enterprise Spider storage engine plugin:

<table><thead><tr><th width="113.88885498046875">Interface</th><th width="260.1112060546875">Method</th><th>Benefits</th></tr></thead><tbody><tr><td>Shell</td><td><a href="step-1-install-enterprise-spider.md#load-spider-with-configuration-file">Configuration File</a></td><td><ul><li>SQL access is not required</li><li>SUPER privilege is not required</li><li>Configuration file can be version controlled</li></ul></td></tr><tr><td>SQL</td><td><a href="step-1-install-enterprise-spider.md#load-spider-with-install-soname">INSTALL SONAME Statement</a></td><td><ul><li>Shell access is not required</li><li>File system privileges on configuration file are not required</li><li>Plugin is included in backup of mysql.plugin system table</li><li>Spider Node restart is not required</li></ul></td></tr></tbody></table>

## Load Spider with Configuration File

On the Spider Node, set the `plugin_load_add` option to `ha_spider` in a configuration file. The plugin\_load\_add option configures MariaDB Enterprise Server to load the Enterprise Spider storage engine plugin. The Spider Node must be restarted to detect the configuration change.

1. Choose a configuration file for custom changes to system variables and options.\
   It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.\
   \
   Ensure that your custom changes will be read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the z- prefix in the file name.\
   \
   Some example configuration file paths for different distributions are shown in the following table:

<table><thead><tr><th width="180.81475830078125" valign="top">Distributions</th><th valign="top">Example configuration file path</th></tr></thead><tbody><tr><td valign="top"><ul><li>CentOS</li><li>RHEL</li><li>Rocky Linux</li><li>SLES</li></ul></td><td valign="top"><code>/etc/my.cnf.d/z-custom-mariadb.cnf</code></td></tr><tr><td valign="top"><ul><li>Debian</li><li>Ubuntu</li></ul></td><td valign="top"><code>/etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf</code></td></tr></tbody></table>

2. Set the plugin\_load\_add option in the configuration file.\
   \
   It must be set in a group that will be read by MariaDB Server, such as `[mariadb]` or `[server]`.\
   \
   For example:

```
[mariadb]
...
plugin_load_add = "ha_spider"
```

3. Restart MariaDB Enterprise Server:

```bash
$ sudo systemctl restart mariadb
```

## Load Spider with INSTALL SONAME

**On the Spider Node**, execute the [INSTALL SONAME](../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) statement with the library name `ha_spider`. The `INSTALL SONAME` statement configures MariaDB Enterprise Server to load the Enterprise Spider storage engine plugin. The `INSTALL SONAME` statement requires the SUPER privilege.

The `INSTALL SONAME` statement adds the Enterprise Spider storage engine to the [mysql.plugin](../../../reference/system-tables/the-mysql-database-tables/mysql-plugin-table.md) system table. When the Spider Node is restarted, MariaDB Enterprise Server reads the system table and reloads the plugin, so the statement only needs to be executed once.

1. Connect to the Spider Node using MariaDB Client:

```bash
$ sudo mariadb
```

2. Use the INSTALL SONAME statement to install the Enterprise Spider storage engine plugin:

```sql
INSTALL SONAME "ha_spider";
```

## Test Plugin Installation

**On the Spider Node**, confirm that the Enterprise Spider storage engine plugin is loaded by querying the information\_schema.PLUGINS table:

```sql
SELECT PLUGIN_NAME, PLUGIN_STATUS
FROM information_schema.PLUGINS
WHERE PLUGIN_LIBRARY LIKE "ha_spider%";

+--------------------------+---------------+
| PLUGIN_NAME              | PLUGIN_STATUS |
+--------------------------+---------------+
| SPIDER                   | ACTIVE        |
| SPIDER_ALLOC_MEM         | ACTIVE        |
| SPIDER_WRAPPER_PROTOCOLS | ACTIVE        |
+--------------------------+---------------+
```

When the Enterprise Spider storage engine is loaded, the `PLUGIN_NAME` column contains the value `SPIDER` and the `PLUGIN_STATUS` column contains the value `ACTIVE`.

## Next Step

Navigation in the procedure "Deploy Spider Sharded Topology":

This page was step 1 of 3.

Next: Step 2: Configure Spider Node and Data Nodes.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
