---
description: >-
  The Disks plugin adds the DISKS table to the Information Schema, providing
  metadata about the system's disk storage and usage.
---

# Disks Plugin

The `DISKS` plugin creates the [DISKS](../../system-tables/information-schema/information-schema-tables/information-schema-disks-table.md) table in the [INFORMATION\_SCHEMA](../../system-tables/information-schema/) database. This table shows metadata about disks on the system, enabling monitoring of the disk space status. Accessing the `INFORMATION_SCHEMA.DISKS` table requires the [FILE privilege](../../sql-statements/account-management-sql-statements/grant.md).

{% hint style="info" %}
The plugin is supported on Linux systems only.
{% endhint %}

## Installing the Plugin

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB automatically. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md):

```sql
INSTALL SONAME 'disks';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options. This can be provided as a command-line argument to [mysqld](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
plugin_load_add = disks
```

## Example

After the plugin is installed, the `INFORMATION_SCHEMA.DISKS` table displays disk utilization information.

To view disk usage information, run the following query:

```
SELECT * FROM information_schema.DISKS;
```

### Example Output

```sql
  +-----------+-----------------------+-----------+----------+-----------+
  | Disk      | Path                  | Total     | Used     | Available |
  +-----------+-----------------------+-----------+----------+-----------+
  | /dev/sda3 | /                     |  47929956 | 30666304 |  14805864 |
  | /dev/sda1 | /boot/efi             |    191551 |     3461 |    188090 |
  | /dev/sda4 | /home                 | 174679768 | 80335392 |  85448120 |
  | /dev/sdb1 | /mnt/hdd              | 961301832 |    83764 | 912363644 |
  | /dev/sdb1 | /home/wikman/Music    | 961301832 |    83764 | 912363644 |
  | /dev/sdb1 | /home/wikman/Videos   | 961301832 |    83764 | 912363644 |
  | /dev/sdb1 | /home/wikman/hdd      | 961301832 |    83764 | 912363644 |
  | /dev/sdb1 | /home/wikman/Pictures | 961301832 |    83764 | 912363644 |
  | /dev/sda3 | /var/lib/docker/aufs  |  47929956 | 30666304 |  14805864 |
  +-----------+-----------------------+-----------+----------+-----------+
  9 rows in set (0.00 sec)
```

## Column Descriptions

The `INFORMATION_SCHEMA.DISKS` table contains the following columns:

* **Disk**: The name of the disk device or partition.
* **Path**: The mount point where the disk is mounted.
* **Total**: The total disk space available on the disk (in KiB).
* **Used**: The amount of disk space currently used (in KiB).
* **Available**: The amount of disk space available to non-root users (in KiB).&#x20;

> Note: As root users may have more available space than non-root users, `Available` + `Used` may be less than `Total`.
>
> Additionally, all paths to which a specific disk is mounted are reported, so a disk may appear multiple times in the output.

## Alternative: Mounts Table

As an alternative option, the plugin includes the `INFORMATION_SCHEMA.MOUNTS` table, which contains mount points and their respective disks.

For example:

```
SELECT * FROM information_schema.MOUNTS;
```

### Expected Output

```
  +-----------------------+-----------+
  | Path                  | Disk      |
  +-----------------------+-----------+
  | /                     | /dev/sda3 |
  | /boot/efi             | /dev/sda1 |
  | /home                 | /dev/sda4 |
  | /mnt/hdd              | /dev/sdb1 |
  | /home/wikman/Music    | /dev/sdb1 |
  +-----------------------+-----------+
```

## Versions

| Version | Status | Introduced                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1     | Stable | [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10226-release-notes), [MariaDB 10.1.41](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10141-release-notes) |
| 1.0     | Beta   | [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes), [MariaDB 10.2.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10214-release-notes), [MariaDB 10.1.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10132-release-notes)                                                                                                                                                                |

## Options

### `disks`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Command line: `--disks=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md):

```sql
UNINSTALL SONAME 'disks';
```

If you installed the plugin by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## See Also

* [Information Schema](../../system-tables/information-schema/)
* [Plugin Overview](../plugin-overview.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
