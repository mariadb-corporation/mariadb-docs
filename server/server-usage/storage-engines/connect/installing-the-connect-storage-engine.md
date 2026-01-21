---
description: The CONNECT storage engine has been deprecated.
---

# Installing CONNECT

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

The `CONNECT` storage engine enables MariaDB to access external local or remote data (MED). This is done by defining tables based on different data types, in particular files in various formats, data extracted from other DBMS or products (such as Excel or MongoDB) via ODBC or JDBC, or data retrieved from the environment (for example DIR, WMI, and MAC tables)

This storage engine supports table partitioning, MariaDB virtual columns and permits defining special columns such as ROWID, FILEID, and SERVID.

The storage engine must be installed before it can be used.

## Installing the Plugin's Package

The `CONNECT` storage engine's shared library is included in MariaDB packages as the `ha_connect.so` or `ha_connect.so` shared library on systems where it can be built.

### Installing on Linux

The `CONNECT` storage engine is included in [binary tarballs](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) on Linux.

#### Installing with a Package Manager

The `CONNECT` storage engine can also be installed via a package manager on Linux. In order to do so, your system needs to be configured to install from one of the MariaDB repositories.

You can configure your package manager to install it from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md).

You can also configure your package manager to install it from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).

**Installing with yum/dnf**

On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) from MariaDB's repository using [yum](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum.md) or [dnf](https://en.wikipedia.org/wiki/DNF_\(software\)). Starting with RHEL 8 and Fedora 22, `yum` has been replaced by `dnf`, which is the next major version of `yum`. However, `yum` commands still work on many systems that use `dnf`:

```bash
sudo yum install MariaDB-connect-engine
```

**Installing with apt-get**

On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant [DEB package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md) from MariaDB's repository using [apt-get](https://wiki.debian.org/apt-get):

```bash
sudo apt-get install mariadb-plugin-connect
```

**Installing with zypper**

On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) from MariaDB's repository using [zypper](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md):

```bash
sudo zypper install MariaDB-connect-engine
```

## Installing the Plugin

Once the shared library is in place, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md):

```sql
INSTALL SONAME 'ha_connect';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options. This can be specified as a command-line argument to [mysqld](../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[mariadb]
...
plugin_load_add = ha_connect
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md):

```sql
UNINSTALL SONAME 'ha_connect';
```

If you installed the plugin by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Installing Dependencies

The `CONNECT` storage engine has some external dependencies.

### Installing unixODBC

The `CONNECT` storage engine requires an ODBC library. On Unix-like systems, that usually means installing [unixODBC](https://www.unixodbc.org/). On some systems, this is installed as the `unixODBC` package:

```bash
sudo yum install unixODBC
```

On other systems, this is installed as the `libodbc1` package:

```bash
sudo apt-get install libodbc1
```

If you do not have the ODBC library installed, then you may get an error about a missing library when you attempt to install the plugin:

```sql
INSTALL SONAME 'ha_connect';
ERROR 1126 (HY000): Can't open shared library '/home/ian/MariaDB_Downloads/10.1.17/lib/plugin/ha_connect.so' 
  (errno: 2, libodbc.so.1: cannot open shared object file: No such file or directory)
```

## See Also

* [PLUGIN OVERVIEW](../../../reference/plugins/plugin-overview.md)

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
