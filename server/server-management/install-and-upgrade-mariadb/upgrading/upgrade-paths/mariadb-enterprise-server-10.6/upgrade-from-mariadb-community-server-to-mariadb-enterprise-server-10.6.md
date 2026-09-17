---
description: >-
  Upgrade from MariaDB Community Server 10.6 to MariaDB Enterprise Server 10.6,
  switching products on the same release series to keep a maintained and
  supported server.
hidden: true
---

# Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.6

These instructions detail the **upgrade** from **MariaDB Community Server 10.6** to **MariaDB Enterprise Server 10.6** on a range of [supported Operating Systems](https://mariadb.com/engineering-policies/).

{% hint style="warning" %}
MariaDB Community Server 10.6 reached its end of life in July 2026 and no longer receives maintenance or security releases. Upgrading to MariaDB Enterprise Server 10.6 lets you stay on the 10.6 release series while moving to a maintained and supported server.
{% endhint %}

{% hint style="info" %}
This page describes the minimal-change path: switching products while staying on the 10.6 release series. The recommended path is to upgrade directly to MariaDB Enterprise Server 11.8, the newest long-term release series, for a longer support runway — see [Upgrade from MariaDB Community Server 10.6 to MariaDB Enterprise Server 11.8](../mariadb-enterprise-server-11.8/upgrade-from-mariadb-community-server-10.6-to-mariadb-enterprise-server-11.8.md).
{% endhint %}

When switching from MariaDB Community Server to [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/), the old version needs to be uninstalled, and the new version needs to be installed.

MariaDB Enterprise Server 10.6 is not identical to MariaDB Community Server 10.6:

* MariaDB Enterprise Server includes features and fixes backported from later MariaDB versions. For details, see [What's New in MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/10.6/whats-new).
* MariaDB Enterprise Server does not include plugins that are not supported for enterprise use. Before upgrading, review [Differences in Available Plugins for Enterprise Server](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/about/mariadb-enterprise-server-differences/differences-in-available-plugins-for-enterprise-server) to confirm that the plugins you rely on are available.

### Data Backup

Occasionally, issues can be encountered during upgrades. These issues can even potentially corrupt the database's data files, preventing you from easily reverting to the old installation. Therefore, it is generally best to perform a backup prior to upgrading. If an issue is encountered during the upgrade, you can use the backup to restore your MariaDB Server database to the old version. If the upgrade finishes without issue, then the backup can be deleted.

The instructions below show how to perform a backup using [MariaDB Backup](../../../../../server-usage/backup-and-restore/mariadb-backup/). For more information about backing up and restoring the database, please see the [Recovery Guide](../../../../../server-usage/backup-and-restore/).

1.  Take a full backup:

    ```bash
    $ sudo mariadb-backup --backup \
          --user=mariadb-backup_user \
          --password=mariadb-backup_passwd \
          --target-dir=/data/backup/preupgrade_backup
    ```

    Confirm successful completion of the backup operation.
2.  Prepare the backup so that it is ready for immediate restoration if required:

    ```bash
    $ sudo mariadb-backup --prepare \
          --target-dir=/data/backup/preupgrade_backup
    ```

    Confirm successful completion of the prepare operation.
3. Verify that the backup is recoverable by restoring it to a non-production environment before proceeding with the upgrade.

### Audit Plugin Considerations

If you have the [MariaDB Audit Plugin](../../../../../reference/plugins/mariadb-audit-plugin/) installed, then the audit plugin should be removed prior to the upgrade to prevent conflict with the [MariaDB Enterprise Audit Plugin](../../../../../reference/plugins/mariadb-enterprise-audit.md) that is included in MariaDB Enterprise Server 10.6.

The two plugins differ mainly in how audit logging can be filtered:

| Capability | MariaDB Audit Plugin | MariaDB Enterprise Audit |
| ---------------------- | ------------------------------------------ | ------------------------------------------------ |
| Event selection | Global event types (connect, query, table) | Event filters defined per audit filter |
| Per-user control | Include/exclude user lists | Default and named per-user audit filters |
| Per-object control | Not available | Object filters for specific databases and tables |
| Configuration auditing | Not available | Changes to the audit configuration are logged |

It can be removed by using the [UNINSTALL SONAME](../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) statement:

```sql
UNINSTALL SONAME 'server_audit';
```

And if you load the plugin in a configuration file using the [plugin\_load\_add](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) option — a [mariadbd](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) startup option that loads a plugin library when the server starts — then the option should also be removed.

The MariaDB Enterprise Audit Plugin will automatically be installed after installing MariaDB Enterprise Server 10.6.

### Uninstall the Old Version

When upgrading to MariaDB Enterprise Server, it is necessary to remove the existing installation of MariaDB Community Server, before installing MariaDB Enterprise Server. Otherwise, the package manager will refuse to install MariaDB Enterprise Server.

#### Stop the MariaDB Server Process

Before the old version can be uninstalled, we first need to stop the current MariaDB Server process.

1.  Set the [innodb\_fast\_shutdown](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) system variable to `1`:

    ```sql
    SET GLOBAL innodb_fast_shutdown = 1;
    ```
2.  Use [XA RECOVER](../../../../../reference/sql-statements/transactions/xa-transactions.md#xa-recover) to confirm that there are no external XA transactions in a prepared state:

    ```sql
    XA RECOVER;
    ```

    Commit or rollback any open XA transactions before stopping the node for upgrade.
3.  Stop the server process:

    For distributions that use systemd (most supported OSes), you can manage the Server process using the `systemctl` command:

    ```bash
    $ sudo systemctl stop mariadb
    ```

{% tabs %}
{% tab title="Uninstall via YUM" %}
**Uninstall via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux)**

1.  Uninstall all of the MariaDB Community Server packages. Note that a wildcard character is used to ensure that all MariaDB Community Server packages are uninstalled:

    ```bash
    $ sudo yum remove "MariaDB-*"
    ```

    Be sure to check that this wildcard does not unintentionally refer to any of your custom applications:
2.  Uninstall the Galera package as well.

    For MariaDB Community Server 10.6, the package is called `galera-4`:

    ```bash
    $ sudo yum remove galera-4
    ```
3.  Before proceeding, verify that all MariaDB Community Server packages are uninstalled. The following command should not return any results:

    ```bash
    $ rpm --query --all | grep -i -E "mariadb|galera"
    ```
{% endtab %}

{% tab title="Uninstall via APT" %}
**Uninstall via APT (Debian, Ubuntu)**

1.  Uninstall all of the MariaDB Community Server packages. Note that a wildcard character is used to ensure that all MariaDB Community Server packages are uninstalled:

    ```bash
    $ sudo apt-get remove "mariadb-*"
    ```

    Be sure to check that this wildcard does not unintentionally refer to any of your custom applications.
2.  Uninstall the Galera package as well.

    For MariaDB Community Server 10.6, the package is called `galera-4`:

    ```bash
    $ sudo apt remove galera-4
    ```
3.  Before proceeding, verify that all MariaDB Community Server packages are uninstalled. The following command should not return any results:

    ```bash
    $ apt list --installed | grep -i -E "mariadb|galera"
    ```
{% endtab %}

{% tab title="Uninstall via ZYpp" %}
**Uninstall via ZYpp (SLES)**

1.  Uninstall all of the MariaDB Community Server packages. Note that a wildcard character is used to ensure that all MariaDB Community Server packages are uninstalled:

    ```bash
    $ sudo zypper remove "MariaDB-*"
    ```

    Be sure to check that this wildcard does not unintentionally refer to any of your custom applications.
2.  Uninstall the Galera package as well.

    For MariaDB Community Server 10.6, the package is called `galera-4`:

    ```bash
    $ sudo zypper remove galera-4
    ```
3.  Before proceeding, verify that all MariaDB Community Server packages are uninstalled. The following command should not return any results:

    ```bash
    $ rpm --query --all | grep -i -E "mariadb|galera"
    ```
{% endtab %}
{% endtabs %}

### Install the New Version

MariaDB Corporation provides package repositories for YUM (RHEL, AlmaLinux, CentOS, Rocky Linux), APT (Debian, Ubuntu), and ZYpp (SLES).

{% hint style="info" %}
If the server is a node in a Galera Cluster, also install the Enterprise Galera provider package, `galera-enterprise-4`, which replaces MariaDB Community Server's `galera-4` package. Cluster nodes are also upgraded one node at a time — see [Upgrading Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster) for the cluster-specific procedure.
{% endhint %}

{% tabs %}
{% tab title="Install via YUM" %}
**Install via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux)**

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the YUM package repository. Installable versions of MariaDB Enterprise Server are `10.6`, `11.4`, and `11.8`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](../../../mariadb-package-repository-setup-and-usage.md#using-mariadb-corporations-repository-setup-scripts). The following directions reference `10.6`.

    To configure YUM package repositories:

    ```
    $ sudo yum install curl
    ```

    ```bash
    $ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```bash
    $ echo "${checksum}  mariadb_es_repo_setup" \
        | sha256sum -c -
    ```

    ```bash
    $ chmod +x mariadb_es_repo_setup
    ```

    ```bash
    $ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="10.6"
    ```

    1. _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
3.  Install MariaDB Enterprise Server and package dependencies:

    ```
    $ sudo yum install MariaDB-server MariaDB-backup
    ```

    Installation of additional packages may be required for some plugins.
4.  Configure MariaDB.

    Installation only loads MariaDB Enterprise Server to the system. MariaDB Enterprise Server requires configuration before the database server is ready for use.
{% endtab %}

{% tab title="Install via APT" %}
**Install via APT (Debian, Ubuntu)**

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the APT package repository.

    Installable versions of MariaDB Enterprise Server are `10.6`, `11.4`, and `11.8`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](../../../mariadb-package-repository-setup-and-usage.md#using-mariadb-corporations-repository-setup-scripts). The following directions reference `10.6`.

    To configure APT package repositories:

    ```bash
    $ sudo apt install curl
    ```

    ```bash
    $ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```bash
    $ echo "${checksum}  mariadb_es_repo_setup" \
        | sha256sum -c -
    ```

    ```bash
    $ chmod +x mariadb_es_repo_setup
    ```

    ```bash
    $ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="10.6"
    ```

    ```bash
    $ sudo apt update
    ```

    1. _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
3.  Install MariaDB Enterprise Server and package dependencies:

    ```bash
    $ sudo apt install mariadb-server mariadb-backup
    ```

    Installation of additional packages may be required for some plugins.
4.  Configure MariaDB.

    Installation only loads MariaDB Enterprise Server to the system. MariaDB Enterprise Server requires configuration before the database server is ready for use.
{% endtab %}

{% tab title="Install via ZYpp" %}
**Install via ZYpp (SLES)**

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the ZYpp package repository.

    Installable versions of MariaDB Enterprise Server are `10.6`, `11.4`, and `11.8`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](../../../mariadb-package-repository-setup-and-usage.md#using-mariadb-corporations-repository-setup-scripts). The following directions reference `10.6`.

    To configure ZYpp package repositories:

    ```bash
    $ sudo zypper install curl
    ```

    ```bash
    $ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```bash
    $ echo "${checksum}  mariadb_es_repo_setup" \
        | sha256sum -c -
    ```

    ```bash
    $ chmod +x mariadb_es_repo_setup
    ```

    ```bash
    $ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="10.6"
    ```

    1. _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
3.  Install MariaDB Enterprise Server and package dependencies:

    ```bash
    $ sudo zypper install MariaDB-server MariaDB-backup
    ```

    Installation of additional packages may be required for some plugins.
4.  Configure MariaDB.

    Installation only loads MariaDB Enterprise Server to the system. MariaDB Enterprise Server requires configuration before the database server is ready for use.
{% endtab %}
{% endtabs %}

### Configuration

For platforms that use YUM or ZYpp as a package manager:

MariaDB Community Server's packages bundle several configuration files:

* `/etc/my.cnf`
* `/etc/my.cnf.d/client.cnf`
* `/etc/my.cnf.d/mysql-clients.cnf`
* `/etc/my.cnf.d/server.cnf`

If your version of any of these configuration files contained any custom edits, then the package manager may save your edited version with the `.rpmsave` extension during the upgrade process. If you want to continue using your version with the custom edits, then you may need to move it back. For example, to move `server.cnf` back in place:

```
$ sudo mv /etc/my.cnf.d/server.cnf /etc/my.cnf.d/server.cnf.original
```

```
$ sudo mv /etc/my.cnf.d/server.cnf.rpmsave /etc/my.cnf.d/server.cnf
```

In addition to the configuration files listed above, MariaDB Enterprise Server installs its own configuration file:

* On platforms that use YUM or ZYpp: `/etc/my.cnf.d/mariadb-enterprise.cnf`
* On platforms that use APT: `/etc/mysql/mariadb.conf.d/mariadb-enterprise.cnf`

This file provides MariaDB Enterprise Server defaults, some of which change behavior compared to a default MariaDB Community Server configuration:

* Only plugins of stable maturity are loaded (`plugin-maturity=stable`).
* The MariaDB Enterprise Audit Plugin is preloaded (with audit logging off by default).
* The [simple\_password\_check](../../../../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md) plugin is enabled, so new passwords must be at least 8 characters and include a digit, a special character, and both upper- and lowercase letters.
* The [InnoDB adaptive hash index](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) is kept disabled (also the default in MariaDB Community Server 10.6).

Do not edit this file directly. To override its settings, add your own options in a separate configuration file whose name sorts later than `mariadb-enterprise.cnf`.

### Starting the Server

MariaDB Enterprise Server includes configuration to start, stop, restart, enable/disable on boot, and check the status of the Server using the operating system default process management system.

For distributions that use systemd, you can manage the Server process using the `systemctl` command:

| **Operation**          | **Command**                      |
| ---------------------- | -------------------------------- |
| Start                  | `sudo systemctl start mariadb`   |
| Stop                   | `sudo systemctl stop mariadb`    |
| Restart                | `sudo systemctl restart mariadb` |
| Enable during startup  | `sudo systemctl enable mariadb`  |
| Disable during startup | `sudo systemctl disable mariadb` |
| Status                 | `sudo systemctl status mariadb`  |

### Upgrading the Data Directory

MariaDB Enterprise Server ships with a utility that can be used to identify and correct compatibility issues in the new version. After you upgrade your Server and start the server process, run the [mariadb-upgrade](../../../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) utility to upgrade the data directory:

```bash
$ sudo mariadb-upgrade
```

### Testing

When MariaDB Enterprise Server is up and running on your system, you should test that it is working and there weren't any issues during startup.

1.  Connect to the server with [MariaDB Client](../../../../../clients-and-utilities/mariadb-client/) using the `root@localhost` user account:

    ```bash
    $ sudo mariadb
    ```

    ```
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 9
    Server version: 10.6.28-24-MariaDB-enterprise MariaDB Enterprise Server

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]>
    ```

    The `-enterprise` suffix in the version string confirms that you are connected to MariaDB Enterprise Server rather than MariaDB Community Server.
2.  You can also verify the server version by checking the value of the [version](../../../../../reference/sql-functions/secondary-functions/information-functions/version.md) system variable with the [SHOW GLOBAL VARIABLES](../../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

    ```sql
    SHOW GLOBAL VARIABLES LIKE 'version';
    ```

    ```
    +---------------+-------------------------------+
    | Variable_name | Value                         |
    +---------------+-------------------------------+
    | version       | 10.6.28-24-MariaDB-enterprise |
    +---------------+-------------------------------+
    ```
3.  You can also verify the server version by calling the [VERSION()](../../../../../reference/sql-functions/secondary-functions/information-functions/version.md) function:

    ```sql
    SELECT VERSION();
    ```

    ```
    +-------------------------------+
    | VERSION()                     |
    +-------------------------------+
    | 10.6.28-24-MariaDB-enterprise |
    +-------------------------------+
    ```

***

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
