---
description: >-
  Step-by-step minor version upgrade (e.g., 11.4.4 to 11.4.5) for MariaDB
  Community Server on Linux using YUM, APT, or ZYpp — backup, stop, upgrade
  packages, restart, and run mariadb-upgrade.
---

# Upgrading Between Minor MariaDB Versions

These instructions detail a **minor release upgrade** of **MariaDB Community Server** on Linux. A minor release upgrade refers to upgrading within the same release series. For example, upgrading from MariaDB 11.4.4 to MariaDB 11.4.5 without changing the major version. Minor releases typically deliver bug fixes, security patches, and stability improvements.

For Windows, see [Upgrading MariaDB on Windows](upgrading-mariadb-on-windows.md). For major version upgrades (for example, MariaDB 10.11 to MariaDB 11.4), see [Upgrading Between Major MariaDB Versions](upgrading-between-major-mariadb-versions.md) and the per-version guides listed in [See Also](#see-also).

{% hint style="info" %}
The examples in this page use MariaDB Community Server 11.4.4 → 11.4.5 as the worked scenario. The same procedure applies to any supported minor-version upgrade within a release series.
{% endhint %}

## Data Backup

Occasionally, issues can be encountered during an upgrade. These issues can even potentially corrupt the database's data files, making it difficult to revert to the previous installation. It is strongly recommended to create a backup before upgrading. 
* If the upgrade fails, the backup can be used to restore the database to the previous version of MariaDB Server. 
* If the upgrade finishes successfully, then the backup can be deleted.

The instructions below show how to perform a backup using [MariaDB Backup](../../../server-usage/backup-and-restore/mariadb-backup/). For more information about backing up and restoring the database, see the [Recovery Guide](../../../server-usage/backup-and-restore/).

1.  Take a full backup:

    ```bash
    sudo mariadb-backup --backup \
          --user=mariadb-backup_user \
          --password=mariadb-backup_passwd \
          --target-dir=/data/backup/preupgrade_backup
    ```

    Replace `mariadb-backup_user` and `mariadb-backup_passwd` with your actual backup user credentials.
    Confirm successful completion of the backup operation.
2.  Prepare the backup so it is ready for immediate restoration if required:

    ```bash
    sudo mariadb-backup --prepare \
          --target-dir=/data/backup/preupgrade_backup
    ```

    Confirm successful completion of the prepare operation.
3. Backups should be tested before they are trusted. Restore the backup to a non-production instance and verify it before proceeding with the upgrade.

## Stop the MariaDB Server Process

Before the new packages are installed, stop the running server.

1.  Set the [innodb\_fast\_shutdown](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) system variable to `1` so InnoDB flushes all dirty pages and closes cleanly:

    ```sql
    SET GLOBAL innodb_fast_shutdown = 1;
    ```
2.  Use [XA RECOVER](../../../reference/sql-statements/transactions/xa-transactions.md#xa-recover) to confirm that there are no external XA transactions in a prepared state:

    ```sql
    XA RECOVER;
    ```

    Commit or roll back any open XA transactions before stopping the server.
3.  Stop the server process. On distributions that use `systemd` (most supported OSes), manage the server with `systemctl`:

    ```bash
    sudo systemctl stop mariadb
    ```

## Install the New Version

Unlike a major-version upgrade, a minor-version upgrade does **not** require uninstalling the old packages first. The distribution's package manager upgrades the packages in place, while keeping the data directory and configuration files unchanged.

MariaDB Community Server provides a setup script, [`mariadb_repo_setup`](../mariadb-package-repository-setup-and-usage.md), that configures the package repository for your distribution. To pin to a specific minor release, pass the full version number to `--mariadb-server-version`, prefixed with `mariadb-`. For example, to install MariaDB 11.4.5 instead of the latest 11.4.x release:

```
--mariadb-server-version="mariadb-11.4.5"
```

To track the latest release in a series rather than pinning to a specific minor, pass only the series:

```
--mariadb-server-version="mariadb-11.4"
```

{% tabs %}
{% tab title="Upgrade via YUM" %}
**Upgrade via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux)**

1.  Configure the YUM package repository for the target release. The following example uses MariaDB 11.4.5; adjust the version number for your target release:

    ```bash
    sudo yum install curl
    ```

    ```bash
    curl -LsSO https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
    ```

    ```bash
    chmod +x mariadb_repo_setup
    ```

    ```bash
    sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-11.4.5"
    ```

    See [Pinning the Repository to a Specific Minor Release](../mariadb-package-repository-setup-and-usage.md#mariadb-community-server-2) for more on minor-release pinning.
2.  Update MariaDB Community Server and package dependencies:

    ```bash
    sudo yum update "MariaDB-*" "galera*"
    ```

    Check that the wildcards do not unintentionally match any custom applications.
{% endtab %}

{% tab title="Upgrade via APT" %}
**Upgrade via APT (Debian, Ubuntu)**

1.  Configure the APT package repository for the target release. The following example uses MariaDB 11.4.5; adjust the version number for your target release:

    ```bash
    sudo apt install curl
    ```

    ```bash
    curl -LsSO https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
    ```

    ```bash
    chmod +x mariadb_repo_setup
    ```

    ```bash
    sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-11.4.5"
    ```

    ```bash
    sudo apt update
    ```
2.  Upgrade MariaDB Community Server and package dependencies. The `--only-upgrade` flag ensures `apt` does not install new packages, only updates existing ones:

    ```bash
    sudo apt install --only-upgrade "mariadb-*" "galera*"
    ```

    Check that the wildcards do not unintentionally match any custom applications.
{% endtab %}

{% tab title="Upgrade via ZYpp" %}
**Upgrade via ZYpp (SLES, openSUSE)**

1.  Configure the ZYpp package repository for the target release. The following example uses MariaDB 11.4.5; adjust the version number for your target release:

    ```bash
    sudo zypper install curl
    ```

    ```bash
    curl -LsSO https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
    ```

    ```bash
    chmod +x mariadb_repo_setup
    ```

    ```bash
    sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-11.4.5"
    ```
2.  Update MariaDB Community Server and package dependencies:

    ```bash
    sudo zypper update "MariaDB-*" "galera*"
    ```

    Check that the wildcards do not unintentionally match any custom applications.
{% endtab %}
{% endtabs %}

## Configuration

For platforms that use YUM or ZYpp as a package manager, MariaDB Community Server's packages bundle several configuration files:

* `/etc/my.cnf`
* `/etc/my.cnf.d/client.cnf`
* `/etc/my.cnf.d/mysql-clients.cnf`
* `/etc/my.cnf.d/server.cnf`

If your version of any of these configuration files contained custom edits, then the package manager may save your edited version with the `.rpmsave` extension during the upgrade. To continue using your customized version, restore it before starting the server. For example, to restore `server.cnf`:

```bash
sudo mv /etc/my.cnf.d/server.cnf /etc/my.cnf.d/server.cnf.original
```

```bash
sudo mv /etc/my.cnf.d/server.cnf.rpmsave /etc/my.cnf.d/server.cnf
```

On APT-based systems (Debian, Ubuntu), preserved configuration files use the `.dpkg-old` extension instead. The principle is the same: rename and restore as needed.

Now is also the time to make any desired changes to [option files](../configuring-mariadb/configuring-mariadb-with-option-files.md) such as `my.cnf`, before starting the new server.

## Starting the Server

MariaDB Community Server includes configuration to start, stop, restart, enable/disable on boot, and check the status of the server using the operating system's default process management system.

For distributions that use `systemd`, manage the server process using `systemctl`:

| Operation              | Command                          |
| ---------------------- | -------------------------------- |
| Start                  | `sudo systemctl start mariadb`   |
| Stop                   | `sudo systemctl stop mariadb`    |
| Restart                | `sudo systemctl restart mariadb` |
| Enable during startup  | `sudo systemctl enable mariadb`  |
| Disable during startup | `sudo systemctl disable mariadb` |
| Status                 | `sudo systemctl status mariadb`  |

## Upgrading the Data Directory

MariaDB ships with a utility that checks for and corrects any compatibility issues introduced by the upgrade. After the server is upgraded and running, run [mariadb-upgrade](../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) to upgrade the data directory:

```bash
sudo mariadb-upgrade
```

{% hint style="info" %}
Minor-version upgrades do not change the data dictionary. On mariadb-upgrade 2.0 and later, `mariadb-upgrade` detects this automatically and exits immediately with a message confirming no upgrade is needed and this is expected behaviour. Running `mariadb-upgrade` after a minor upgrade is still recommended as a safety check, and is harmless when no work is needed. Use `--force` to run the full check regardless. 
{% endhint %}

## Testing

When the upgraded server is up and running, verify it is working and there were no issues during startup.

1.  Connect to the server using the [mariadb](../../../clients-and-utilities/mariadb-client/) client as the `root@localhost` user:

    ```bash
    sudo mariadb
    ```

    ```
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 9
    Server version: 11.4.5-MariaDB MariaDB Server

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]>
    ```
2.  Verify the server version by checking the [version](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#version) system variable:

    ```sql
    SHOW GLOBAL VARIABLES LIKE 'version';
    ```

    ```
    +---------------+-----------------+
    | Variable_name | Value           |
    +---------------+-----------------+
    | version       | 11.4.5-MariaDB  |
    +---------------+-----------------+
    ```
3.  Verify by calling the [VERSION()](../../../reference/sql-functions/secondary-functions/information-functions/version.md) function:

    ```sql
    SELECT VERSION();
    ```

    ```
    +-----------------+
    | VERSION()       |
    +-----------------+
    | 11.4.5-MariaDB  |
    +-----------------+
    ```

## See Also

For major version upgrades (between release series), see:

* [Upgrading Between Major MariaDB Versions](upgrading-between-major-mariadb-versions.md)
* [Upgrading from MariaDB 11.4 to MariaDB 11.8](upgrading-from-to-specific-versions/upgrading-from-mariadb-11-4-to-mariadb-11-8.md)
* [Upgrading from MariaDB 10.11 to MariaDB 11.4](upgrading-from-to-specific-versions/upgrading-from-mariadb-10-11-to-mariadb-11-4.md)
* [Upgrading from MariaDB 10.6 to MariaDB 10.11](upgrading-from-to-specific-versions/upgrading-from-mariadb-10-6-to-mariadb-10-11.md)

For the equivalent Enterprise Server minor-upgrade guides, see:

* [Upgrade MariaDB Enterprise Server from 11.4.X to 11.4.Y](upgrade-paths/mariadb-enterprise-server-11.4/upgrade-mariadb-enterprise-server-from-11.4.x-to-11.4.y.md)
* [Upgrade MariaDB Enterprise Server from 10.6.X to 10.6.Y](upgrade-paths/mariadb-enterprise-server-10.6/upgrade-mariadb-enterprise-server-from-10.6.x-to-10.6.y.md)

Related references:

* [MariaDB Package Repository Setup and Usage](../mariadb-package-repository-setup-and-usage.md) — full reference for `mariadb_repo_setup` options, including `--mariadb-server-version` and minor-release pinning.
* [Installing MariaDB Packages with YUM](../installing-mariadb/binary-packages/rpm/yum.md)
* [Installing MariaDB .deb Files (APT)](../installing-mariadb/binary-packages/installing-mariadb-deb-files.md)
* [Installing MariaDB with Zypper](../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md)
* [mariadb-upgrade](../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) — the post-upgrade data-directory utility.
* [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/) — the recommended pre-upgrade backup tool.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
