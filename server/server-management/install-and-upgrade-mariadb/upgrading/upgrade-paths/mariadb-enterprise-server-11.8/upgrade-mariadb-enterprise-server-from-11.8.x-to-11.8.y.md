---
description: >-
  Instructions for performing a minor release upgrade of MariaDB Enterprise
  Server within the 11.8 series, from an earlier 11.8.x release to a later
  11.8.y release.
---

# Upgrade MariaDB Enterprise Server from 11.8.X to 11.8.Y

These instructions detail a **minor release upgrade** with **MariaDB Enterprise Server 11.8** on a range of [supported Operating Systems](https://mariadb.com/engineering-policies/).

A minor release upgrade is a change from an earlier release of MariaDB Enterprise Server 11.8 to a later release in the same release series.

For example, it would be a minor release upgrade to upgrade from MariaDB Enterprise Server 11.8.2-0 to MariaDB Enterprise Server 11.8.3-1.

## Data Backup <a href="#data-backup" id="data-backup"></a>

Occasionally, issues can be encountered during upgrades. These issues can even potentially corrupt the database's data files, preventing you from easily reverting to the old installation. Therefore, it is generally best to perform a backup before upgrading. If an issue is encountered during the upgrade, you can use the backup to restore your MariaDB Server database to the old version. If the upgrade finishes without issue, then the backup can be deleted.

The instructions below show how to perform a backup using [MariaDB Backup](../../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md). For more information about backing up and restoring the database, please see the [Recovery Guide](../../../../../server-usage/backup-and-restore/).

1\. Take a full backup:

```bash
sudo mariadb-backup --backup \
      --user=mariadb-backup_user \
      --password=mariadb-backup_passwd \
      --target-dir=/data/backup/preupgrade_backup
```

Confirm successful completion of the backup operation.

2\. The backup must be prepared:

```bash
sudo mariadb-backup --prepare \
      --target-dir=/data/backup/preupgrade_backup
```

Confirm successful completion of the prepare operation.

3\. Backups should be tested before they are trusted.

## Stop the MariaDB Server Process <a href="#stop-the-mariadb-server-process" id="stop-the-mariadb-server-process"></a>

Before the new version can be installed, we first need to stop the current MariaDB Server process.

1\. Set the [innodb\_fast\_shutdown](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) system variable to 1:

```sql
SET GLOBAL innodb_fast_shutdown = 1;
```

2\. Use [XA RECOVER](../../../../../reference/sql-statements/transactions/xa-transactions.md#xa-recover) to confirm that there are no external [XA transactions](../../../../../reference/sql-statements/transactions/xa-transactions.md) in a prepared state:

```sql
XA RECOVER;
```

Commit or roll back any open [XA transactions](../../../../../reference/sql-statements/transactions/xa-transactions.md) before stopping the node for upgrade.

3\. Stop the server process. For distributions that use `systemd` (most supported OSes), you can manage the server process using the `systemctl` command:

```bash
sudo systemctl stop mariadb
```

## Install the New Version <a href="#install-the-new-version" id="install-the-new-version"></a>

MariaDB Corporation provides package repositories for YUM (RHEL, AlmaLinux, CentOS, Rocky Linux), APT (Debian, Ubuntu), and ZYpp (SLES).

For a minor release upgrade, the existing MariaDB Enterprise Server packages do not need to be uninstalled. The packages are updated in place.

### Install via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux) <a href="#install-via-yum-rhel-almalinux-centos-rocky-linux" id="install-via-yum-rhel-almalinux-centos-rocky-linux"></a>

1\. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.

2\. Configure the YUM package repository. Installable versions of MariaDB Enterprise Server are `11.8, 11.4, 10.6, 10.5, 10.4, and 10.3`. Pass the version to install using the `--mariadb-server-version` flag to `mariadb_es_repo_setup`. The following directions reference 11.8.

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

{% include "../../../../../.gitbook/includes/checksums-mariadb_es_repo_setup.md" %}

```bash
chmod +x mariadb_es_repo_setup
```

```bash
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-server-version="11.8"
```

3\. Update MariaDB Enterprise Server and package dependencies:

```bash
sudo yum update "MariaDB-*" "galera*"
```

### Install via APT (Debian, Ubuntu) <a href="#install-via-apt-debian-ubuntu" id="install-via-apt-debian-ubuntu"></a>

1\. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.

2\. Configure the APT package repository. Installable versions of MariaDB Enterprise Server are `11.8, 11.4, 10.6, 10.5, 10.4, and 10.3`. Pass the version to install using the `--mariadb-server-version` flag to `mariadb_es_repo_setup`. The following directions reference 11.8.

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

{% include "../../../../../.gitbook/includes/checksums-mariadb_es_repo_setup.md" %}

```bash
chmod +x mariadb_es_repo_setup
```

```bash
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-server-version="11.8"
```

```bash
sudo apt update
```

3\. Update MariaDB Enterprise Server and package dependencies:

```bash
sudo apt install --only-upgrade "mariadb-*" "galera*"
```

### Install via ZYpp (SLES) <a href="#install-via-zypp-sles" id="install-via-zypp-sles"></a>

1\. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.

2\. Configure the ZYpp package repository. Installable versions of MariaDB Enterprise Server are `11.8, 11.4, 10.6, 10.5, 10.4, and 10.3`. Pass the version to install using the `--mariadb-server-version` flag to `mariadb_es_repo_setup`. The following directions reference 11.8.

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

{% include "../../../../../.gitbook/includes/checksums-mariadb_es_repo_setup.md" %}

```bash
chmod +x mariadb_es_repo_setup
```

```bash
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-server-version="11.8"
```

3\. Update MariaDB Enterprise Server and package dependencies:

```bash
sudo zypper update "MariaDB-*" "galera*"
```

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

MariaDB Enterprise Server includes configuration to start, stop, restart, enable/disable on boot, and check the status of the Server using the operating system's default process management system.

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

The utility is called `mariadb-upgrade`:

```bash
sudo mariadb-upgrade
```

## Testing <a href="#testing" id="testing"></a>

When MariaDB Enterprise Server is up and running on your system, you should test that it is working and there weren't any issues during startup.

1\. Connect to the server using MariaDB Client using the `root@localhost` user account. MariaDB Client is called `mariadb`:

```bash
sudo mariadb
```

```
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 9
Server version: 11.8.3-1-MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

2\. You can also verify the server version by checking the value of the [version](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#version) system variable with the [SHOW GLOBAL STATUS](../../../../../reference/sql-statements/administrative-sql-statements/show/show-status.md) statement:

```sql
SHOW GLOBAL VARIABLES LIKE 'version';
```

```
+---------------+-----------------------------+
| Variable_name | Value                       |
+---------------+-----------------------------+
| version       | 11.8.3-1-MariaDB-Enterprise |
+---------------+-----------------------------+
```

3\. You can also verify the server version by calling the [VERSION()](../../../../../reference/sql-functions/secondary-functions/information-functions/version.md) function:

```sql
SELECT VERSION();
```

```
+-----------------------------+
| VERSION()                   |
+-----------------------------+
| 11.8.3-1-MariaDB-Enterprise |
+-----------------------------+
```

{% include "../../../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
