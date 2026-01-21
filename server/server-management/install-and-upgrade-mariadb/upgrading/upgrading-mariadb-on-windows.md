---
description: >-
  Guide to upgrading MariaDB on Windows using the MSI installer, supporting both
  minor upgrades and major version migrations using the upgrade wizard.
---

# Upgrading MariaDB on Windows

For incompatibilities such as removed features, and changes to variables, see the pages describing changes by version on [Upgrading MariaDB](./).

## Minor Upgrades

To install a minor upgrade with MSI, just download the MSI and install it. It will do everything that needs to be done for minor upgrade automatically - shutdown MariaDB service(s), replace executables and DLLs, and start service(s) again.

The rest of the article is dedicated to _major_ upgrades, e.g 10.1.x to 10.2.y.

## General Information on Upgrade and Version Coexistence

This section assumes MSI installations.

First, check everything listed in the Incompatibilities section of the article relating to the version you are upgrading, for example, [Upgrading from MariaDB 10.1 to MariaDB 10.2](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-101-to-mariadb-102.md), to make sure you are prepared for the upgrade.

MariaDB (and also MySQL) allows different versions of the product to co-exist\
on the same machine, as long as these versions are different either in major or\
minor version numbers. For example, it is possible to have say [MariaDB 5.1.51](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5151-release-notes)\
and 5.2.6 to be installed on the same machine.

However only a single instance of 5.2 can exist. If for example 5.2.7 is\
installed on a machine where 5.2.6 is already installed, the installer will\
just replace 5.2.6 executables with 5.2.7 ones.

Now imagine, that both 5.1 and 5.2 are installed on the same machine and we\
want to upgrade the database instance running on 5.1 to the new version. In\
this case special tools are requied. Traditionally, [mysql\_upgrade](../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md) is used\
to accomplish this. On Windows, the[MySQL\
upgrade](https://dev.mysql.com/doc/refman/5.5/en/windows-upgrading.html) is a complicated multiple-step manual process.

Since [MariaDB 5.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-2-series/mariadb-526-release-notes), the Windows distribution includes tools that simplify\
migration between different versions and also allow migration between MySQL and\
MariaDB.

**Note**. Automatic upgrades are only possible for DB instances that run as a\
Windows service.

## General Recommendations

**Important:** Ignore any statement that tells you to _"just uninstall MySQL and install MariaDB"_. This does not work on Windows, never has, and never will. Keep your MySQL installed until after the database had been converted.

The following install/upgrade sequence is recommended in case of "major" upgrades, like going from 5.3 to 5.5

* Install new version, while still retaining the old one
* Upgrade services one by one, like described later in the document (e.g with mysql\_upgrade\_service). It is recommeded to have services cleanly shut down before the upgrade.
* Uninstall old version when previous step is done.

**Note**. This recommendation differs from the procedure on Unixes, where the upgrade sequence is "uninstall old version, install new version"

## Upgrade Wizard

This is a GUI tool that is typically invoked at the end of a MariaDB\
installation if upgradable services are found. The UI allows you to select\
instances you want to upgrade.

![UpgradeWizard](../../../.gitbook/assets/UpgradeWizard.png)

## `mysql_upgrade_service`

This is a command line tool that performs upgrades. The tool requires full\
administrative privileges (it has to start and stop services).

Example usage:

```
mysql_upgrade_service --service=MySQL
```

`mysql_upgrade_service` accepts a single parameter —\
the name of the MySQL or MariaDB service. It performs all the steps to convert\
a MariaDB/MySQL instance running as the service to the current version.

## Migration to 64 bit MariaDB from 32 bit

Earlier we said that only single instance of "MariaDB ." version\
can be installed on the same machine. This was almost correct, because MariaDB\
MSI installations allow 32 and 64-bit versions to be installed on the same\
machine, and in this case it is possible to have two instances of say 5.2\
installed at the same time, an x86 one and an x64 one. One can use the x64\
Upgrade wizard to upgrade an instance running as a 32-bit process to run as\
64-bit.

## Upgrading ZIP-based Installations.

Both UpgradeWizard and mysql\_upgrade\_service can also be used to upgrade\
database instances that were installed with the [ZIP installation](../installing-mariadb/binary-packages/installing-mariadb-windows-zip-packages.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
