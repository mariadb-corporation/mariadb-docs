# Upgrade to MariaDB Enterprise Server 11.4

## Overview <a href="#overview" id="overview"></a>

These instructions detail the **upgrade** from a previous version of **MariaDB Enterprise Server** to **MariaDB Enterprise Server 11.4** on a range of [supported Operating Systems](https://mariadb.com/engineering-policies/).

When MariaDB Enterprise Server is upgraded, the old version needs to be uninstalled, and the new version needs to be installed.

See [What's New in MariaDB Enterprise Server 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11-4/whats-new-in-mariadb-enterprise-server-11-4).

## Data Backup <a href="#data-backup" id="data-backup"></a>

Occasionally, issues can be encountered during upgrades. These issues can even potentially corrupt the database's data files, preventing you from easily reverting to the old installation. Therefore, it is generally best to perform a backup before upgrading. If an issue is encountered during the upgrade, you can use the backup to restore your MariaDB Server database to the old version. If the upgrade finishes without issue, then the backup can be deleted.

The instructions below show how to perform a backup using [MariaDB Backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/). For more information about backing up and restoring the database, please see the [Recovery Guide](../../../../server-usage/backing-up-and-restoring-databases/backup-and-restore-with-mariadb-enterprise-server/).

1\. Take a full backup. On MariaDB Enterprise Server 11.4 and later:

```bash
sudo mariadb-backup --backup \
      --user=mariadb-backup_user \
      --password=mariadb-backup_passwd \
      --target-dir=/data/backup/preupgrade_backup
```

Confirm successful completion of the backup operation.

2\. The backup must be prepared. On the MariaDB Enterprise Server 10.4 and later:

```bash
sudo mariadb-backup --prepare \
      --target-dir=/data/backup/preupgrade_backup
```

Confirm successful completion of the prepare operation.

3\. Backups should be tested before they are trusted.

## Audit Plugin Considerations <a href="#audit-plugin-considerations" id="audit-plugin-considerations"></a>

If you have the [MariaDB Audit Plugin](../../../../reference/plugins/mariadb-audit-plugin/) installed and if you are upgrading to MariaDB Enterprise Server 10.4 or later, then the audit plugin should be removed prior to the upgrade to prevent conflict with the [MariaDB Enterprise Audit Plugin](../../../../reference/plugins/mariadb-enterprise-audit.md) that is present in MariaDB Enterprise Server 10.4 or later. It can be removed by using the [UNINSTALL SONAME](../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) statement:

```sql
UNINSTALL SONAME 'server_audit';
```

And if you load the plugin in a configuration file using the `plugin\_load\_add` option, then the option should also be removed. The [MariaDB Enterprise Audit Plugin](../../../../reference/plugins/mariadb-enterprise-audit/) will automatically be installed after installing MariaDB Enterprise Server 10.4 or later.

## Uninstall the Old Version <a href="#uninstall-the-old-version" id="uninstall-the-old-version"></a>

When upgrading to a new major release of MariaDB Enterprise Server, it is necessary to remove the existing installation of MariaDB Enterprise Server before installing the new version of MariaDB Enterprise Server. Otherwise, the package manager will refuse to install the new version of MariaDB Enterprise Server.

### Stop the MariaDB Server Process <a href="#stop-the-mariadb-server-process" id="stop-the-mariadb-server-process"></a>

Before the old version can be uninstalled, we first need to stop the current MariaDB Server process.

1\. Set the [innodb\_fast\_shutdown](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) system variable to 1:

```sql
SET GLOBAL innodb_fast_shutdown = 1;
```

2\. Use [XA RECOVER](../../../../reference/sql-statements/transactions/xa-transactions.md#xa-recover) to confirm that there are no external [XA transactions](../../../../reference/sql-statements/transactions/xa-transactions.md) in a prepared state:

```sql
XA RECOVER;
```

Commit or roll back any open [XA transactions](../../../../reference/sql-statements/transactions/xa-transactions.md) before stopping the node for upgrade.

3\. Stop the server process: For distributions that use `systemd` (most supported OSes), you can manage the server process using the `systemctl` command:

```bash
sudo systemctl stop mariadb
```

### Uninstall via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux) <a href="#uninstall-via-yum-rhel-almalinux-centos-rocky-linux" id="uninstall-via-yum-rhel-almalinux-centos-rocky-linux"></a>

1\. Uninstall all of the MariaDB Enterprise Server packages. Note that a wildcard character is used to ensure that all MariaDB Enterprise Server packages are uninstalled:

```bash
sudo yum remove "MariaDB-*"
```

Be sure to check that this wildcard does not unintentionally refer to any of your custom applications:

2\. Uninstall the Galera package as well. The name of the package depends on the specific version of MariaDB Enterprise Server. When upgrading from MariaDB Enterprise Server 10.4 or later, the package is called `galera-enterprise-4`:

```bash
sudo yum remove galera-enterprise-4
```

3\. Before proceeding, verify that all MariaDB Enterprise Server packages are uninstalled. The following command should not return any results:

```bash
rpm --query --all | grep -i -E "mariadb|galera"
```

### Uninstall via APT (Debian, Ubuntu) <a href="#uninstall-via-apt-debian-ubuntu" id="uninstall-via-apt-debian-ubuntu"></a>

1\. Uninstall all of the MariaDB Enterprise Server packages. Note that a wildcard character is used to ensure that all MariaDB Enterprise Server packages are uninstalled:

```bash
sudo apt-get remove "mariadb-*"
```

Be sure to check that this wildcard does not unintentionally refer to any of your custom applications.

2\. Uninstall the Galera package as well. The name of the package depends on the specific version of MariaDB Enterprise Server. When upgrading from MariaDB Enterprise Server 10.4 or later, the package is called galera-enterprise-4:

```bash
sudo apt remove galera-enterprise-4
```

3\. Before proceeding, verify that all MariaDB Enterprise Server packages are uninstalled. The following command should not return any results:

```bash
apt list --installed | grep -i -E "mariadb|galera"
```

### Uninstall via ZYpp (SLES) <a href="#uninstall-via-zypp-sles" id="uninstall-via-zypp-sles"></a>

1\. Uninstall all of the MariaDB Enterprise Server packages. Note that a wildcard character is used to ensure that all MariaDB Enterprise Server packages are uninstalled:

```bash
sudo zypper remove "MariaDB-*"
```

Be sure to check that this wildcard does not unintentionally refer to any of your custom applications.

2\. Uninstall the Galera package as well. The name of the package depends on the specific version of MariaDB Enterprise Server. When upgrading from MariaDB Enterprise Server 10.4 or later, the package is called galera-enterprise-4:

```bash
sudo zypper remove galera-enterprise-4
```

3\. Before proceeding, verify that all MariaDB Enterprise Server packages are uninstalled. The following command should not return any results:

```bash
rpm --query --all | grep -i -E "mariadb|galera"
```

## Install the New Version <a href="#install-the-new-version" id="install-the-new-version"></a>

MariaDB Corporation provides package repositories for YUM (RHEL, AlmaLinux, CentOS, Rocky Linux), APT (Debian, Ubuntu), and ZYpp (SLES).

### Install via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux) <a href="#install-via-yum-rhel-almalinux-centos-rocky-linux" id="install-via-yum-rhel-almalinux-centos-rocky-linux"></a>

1. Retrieve your Customer Download Token atand substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.

2. Configure the YUM package repository. Installable versions of MariaDB Enterprise Server are `11.8, 11.4, 10.6, 10.5, 10.4, and 10.3.` Pass the version to install using the `--mariadb-server-version` flag to `mariadb_es_repo_setup`. The following directions reference 11.8.

    To configure YUM package repositories:

    ```bash
    sudo yum install curl 
    ```

    ```bash
    curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```bash
    echo "${checksum}  mariadb_es_repo_setup" \
        | sha256sum -c -
    ```

    ```bash
    chmod +x mariadb_es_repo_setup
    ```

    ```bash
    sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="11.4"
    ```
    * _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._

3. Install MariaDB Enterprise Server and package dependencies:

    ```bash
    sudo yum install MariaDB-server MariaDB-backup
    ```

4. Installation of additional packages may be required for some plugins.

5. Configure MariaDB. Installation only loads MariaDB Enterprise Server onto the system. MariaDB Enterprise Server requires configuration before the database server is ready for use.

### Install via APT (Debian, Ubuntu) <a href="#install-via-apt-debian-ubuntu" id="install-via-apt-debian-ubuntu"></a>

1. Retrieve your Customer Download Token atand substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.

2. Configure the APT package repository. Installable versions of MariaDB Enterprise Server are `11.8 11.4, 10.6, 10.5, 10.4, and 10.3.` Pass the version to install using the `--mariadb-server-version` flag to `mariadb_es_repo_setup`. The following directions reference 11.8.

    To configure APT package repositories:

    ```bash
    sudo apt install curl
    ```

    ```bash
    curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```bash
    echo "${checksum}  mariadb_es_repo_setup" \
        | sha256sum -c -
    ```

    ```bash
    chmod +x mariadb_es_repo_setup
    ```

    ```bash
    sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="11.4"
    ```

    ```bash
    sudo apt update
    ```
    * _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._

3. Install MariaDB Enterprise Server and package dependencies:

    ```
    $ sudo apt install mariadb-server mariadb-backup
    ```

4. Installation of additional packages may be required for some plugins

5. Configure MariaDB. Installation only loads MariaDB Enterprise Server to the system. MariaDB Enterprise Server requires configuration before the database server is ready for use.

### Install via ZYpp (SLES) <a href="#install-via-zypp-sles" id="install-via-zypp-sles"></a>

1. Retrieve your Customer Download Token atand substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.

2. Configure the ZYpp package repository. Installable versions of MariaDB Enterprise Server are `11.8, 11.4, 10.6, 10.5, 10.4, and 10.3.` Pass the version to install using the `--mariadb-server-version` flag to `mariadb_es_repo_setup`. The following directions reference 11.8.

    To configure ZYpp package repositories:

    ```bash
    sudo zypper install curl
    ```

    ```bash
    curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```bash
    echo "${checksum}  mariadb_es_repo_setup" \
        | sha256sum -c -
    ```

    ```bash
    chmod +x mariadb_es_repo_setup
    ```

    ```bash
    sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="11.4"
    ```
    * _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._

3. Install MariaDB Enterprise Server and package dependencies:

    ```bash
    sudo zypper install MariaDB-server MariaDB-backup
    ```

4. Installation of additional packages may be required for some plugins.

5. Configure MariaDB. Installation only loads MariaDB Enterprise Server onto the system. MariaDB Enterprise Server requires configuration before the database server is ready for use.

## Configuration <a href="#configuration" id="configuration"></a>

For platforms that use YUM or ZYpp as a package manager: MariaDB Enterprise Server's packages bundle several configuration files:

* `/etc/my.cnf`
* `/etc/my.cnf.d/client.cnf`
* `/etc/my.cnf.d/mariadb-enterprise.cnf`
* `/etc/my.cnf.d/mysql-clients.cnf`
* `/etc/my.cnf.d/server.cnf`

If your version of any of these configuration files contained any custom edits, then the package manager may save your edited version with the `.rpmsave` extension during the upgrade process. If you want to continue using your version with the custom edits, then you may need to move it back.

For example, to move `server.cnf` back in place:

```bash
sudo mv /etc/my.cnf.d/server.cnf /etc/my.cnf.d/server.cnf.original
```

```bash
sudo mv /etc/my.cnf.d/server.cnf.rpmsave /etc/my.cnf.d/server.cnf
```

## Starting the Server <a href="#starting-the-server" id="starting-the-server"></a>

MariaDB Enterprise Server includes configuration to `start, stop, restart, enable/disable` on boot, and check the status of the Server using the operating system's default process management system.

For distributions that use `systemd`, you can manage the Server process using the `systemctl` command:

| Operation              | Command                          |
| ---------------------- | -------------------------------- |
| Start                  | `sudo systemctl start mariadb`   |
| Stop                   | `sudo systemctl stop mariadb`    |
| Restart                | `sudo systemctl restart mariadb` |
| Enable during startup  | `sudo systemctl enable mariadb`  |
| Disable during startup | `sudo systemctl disable mariadb` |
| Status                 | `sudo systemctl status mariadb`  |

## Upgrading the Data Directory <a href="#upgrading-the-data-directory" id="upgrading-the-data-directory"></a>

MariaDB Enterprise Server ships with a utility that can be used to identify and correct compatibility issues in the new version. After you upgrade your Server and start the server process, run this utility to upgrade the data directory.

The utility is called `mariadb-upgrade` in MariaDB Enterprise Server 10.4 and later:

```bash
sudo mariadb-upgrade
```

## Testing <a href="#testing" id="testing"></a>

When MariaDB Enterprise Server is up and running on your system, you should test that it is working and there weren't any issues during startup.

1\. Connect to the server using MariaDB Client using the `root@localhost` user account. MariaDB Client is called `mariadb` (ES 10.4 and later):

```bash
sudo mariadb
```

```
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 9
Server version: 11.4.5-3-MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

2\. You can also verify the server version by checking the value of the [version](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#version) system variable with the [SHOW GLOBAL STATUS](../../../../reference/sql-statements/administrative-sql-statements/show/show-status.md) statement:

```sql
SHOW GLOBAL VARIABLES LIKE 'version';
```

```
+---------------+-----------------------------+
| Variable_name | Value                       |
+---------------+-----------------------------+
| version       | 11.4.5-3-MariaDB-Enterprise |
+---------------+-----------------------------+
```

3\. You can also verify the server version by calling the [VERSION()](../../../../reference/sql-functions/secondary-functions/information-functions/version.md) function:

```sql
SELECT VERSION();
```

```
+-----------------------------+
| VERSION()                   |
+-----------------------------+
| 11.4.5-3-MariaDB-Enterprise |
+-----------------------------+
```

{% @marketo/form formId="4316" %}
