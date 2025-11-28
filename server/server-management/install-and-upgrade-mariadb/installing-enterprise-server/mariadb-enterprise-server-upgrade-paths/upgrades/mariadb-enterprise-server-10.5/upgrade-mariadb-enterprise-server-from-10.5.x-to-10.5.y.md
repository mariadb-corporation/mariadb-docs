# Upgrade MariaDB Enterprise Server from 10.5.X to 10.5.Y

These instructions detail a **minor release upgrade** with **MariaDB Enterprise Server 10.5** on a range of supported Operating Systems.

A minor release upgrade is a change from an earlier release of MariaDB Enterprise Server 10.5 to a later release in the same release series.

For example, it would be a minor release upgrade to upgrade from MariaDB Enterprise Server 10.5.27-21 to MariaDB Enterprise Server 10.5.28-22.

### Data Backup

Occasionally, issues can be encountered during upgrades. These issues can even potentially corrupt the database's data files, preventing you from easily reverting to the old installation. Therefore, it is generally best to perform a backup prior to upgrading. If an issue is encountered during the upgrade, you can use the backup to restore your MariaDB Server database to the old version. If the upgrade finishes without issue, then the backup can be deleted.

The instructions below show how to perform a backup using [MariaDB Backup](../../../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md). For more information about backing up and restoring the database, please see the [Recovery Guide](../../../../../../server-usage/backup-and-restore/).

1.  Take a full backup.

    On MariaDB Enterprise Server 10.4 and later:

    ```bash
    $ sudo mariadb-backup --backup \
          --user=mariadb-backup_user \
          --password=mariadb-backup_passwd \
          --target-dir=/data/backup/preupgrade_backup
    ```

    On MariaDB Enterprise Server 10.3 and earlier:

    ```
    $ sudo mariadb-backup --backup \
          --user=mariadb-backup_user \
          --password=mariadb-backup_passwd \
          --target-dir=/data/backup/preupgrade_backup
    ```

    Confirm successful completion of the backup operation.
2.  The backup must be prepared.

    On MariaDB Enterprise Server 10.4 and later:

    ```bash
    $ sudo mariadb-backup --prepare \
          --target-dir=/data/backup/preupgrade_backup
    ```

    On MariaDB Enterprise Server 10.3 and earlier:

    ```bash
    $ sudo mariadb-backup --prepare \
          --target-dir=/data/backup/preupgrade_backup
    ```

    Confirm successful completion of the prepare operation.
3. Backups should be tested before they are trusted.

### Stop the MariaDB Server Process

Before the new version can be installed, we first need to stop the current MariaDB Server process.

1.  Set the [innodb\_fast\_shutdown](../../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) system variable to `1`:

    ```sql
    SET GLOBAL innodb_fast_shutdown = 1;
    ```
2.  Use [XA RECOVER](../../../../../../reference/sql-statements/transactions/xa-transactions.md#xa-recover) to confirm that there are no external XA transactions in a prepared state:

    ```sql
    XA RECOVER;
    ```

    Commit or rollback any open XA transactions before stopping the node for upgrade.
3.  Stop the server process:

    For distributions that use systemd (most supported OSes), you can manage the Server process using the `systemctl` command:

    ```bash
    $ sudo systemctl stop mariadb
    ```

### Install the New Version

MariaDB Corporation provides package repositories for YUM (RHEL, AlmaLinux, CentOS, Rocky Linux), APT (Debian, Ubuntu), and ZYpp (SLES).

{% tabs %}
{% tab title="Install via YUM" %}
**Install via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux)**

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the YUM package repository. Installable versions of MariaDB Enterprise Server are `11.4`, `10.6`, `10.5`, `10.4`, and `10.3`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#mariadb_es_repo_setup). The following directions reference `11.4`.

    To configure YUM package repositories:

    ```bash
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
       --mariadb-server-version="10.5"
    ```

    1. _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
3.  Update MariaDB Enterprise Server and package dependencies:

    ```bash
    $ sudo yum update "MariaDB-*" "galera*"
    ```
{% endtab %}

{% tab title="Install via APT" %}
**Install via APT (Debian, Ubuntu)**

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the APT package repository.

    Installable versions of MariaDB Enterprise Server are `11.4`, `10.6`, `10.5`, `10.4`, and `10.3`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#mariadb_es_repo_setup). The following directions reference `11.4`.

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
       --mariadb-server-version="10.5"
    ```

    ```bash
    $ sudo apt update
    ```

    1. _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
3.  Update MariaDB Enterprise Server and package dependencies:

    ```
    $ sudo apt install --only-upgrade "mariadb-*" "galera*"
    ```
{% endtab %}

{% tab title="Install via ZYpp" %}
**Install via ZYpp (SLES)**

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the ZYpp package repository.

    Installable versions of MariaDB Enterprise Server are `11.4`, `10.6`, `10.5`, `10.4`, and `10.3`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#mariadb_es_repo_setup). The following directions reference `10.5`.

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
       --mariadb-server-version="10.5"
    ```

    1. _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
3.  Update MariaDB Enterprise Server and package dependencies:

    ```
    $ sudo zypper update "MariaDB-*" "galera*"
    ```
{% endtab %}
{% endtabs %}

### Configuration

For platforms that use YUM or ZYpp as a package manager:

MariaDB Enterprise Server's packages bundle several configuration files:

* `/etc/my.cnf`
* `/etc/my.cnf.d/client.cnf`
* `/etc/my.cnf.d/mariadb-enterprise.cnf`
* `/etc/my.cnf.d/mysql-clients.cnf`
* `/etc/my.cnf.d/server.cnf`

If your version of any of these configuration files contained any custom edits, then the package manager may save your edited version with the `.rpmsave` extension during the upgrade process. If you want to continue using your version with the custom edits, then you may need to move it back. For example, to move `server.cnf` back in place:

```bash
$ sudo mv /etc/my.cnf.d/server.cnf /etc/my.cnf.d/server.cnf.original
```

```bash
$ sudo mv /etc/my.cnf.d/server.cnf.rpmsave /etc/my.cnf.d/server.cnf
```

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

MariaDB Enterprise Server ships with a utility that can be used to identify and correct compatibility issues in the new version. After you upgrade your Server and start the server process, run this utility to upgrade the data directory.

The utility is called [mariadb-upgrade](../../../../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) in MariaDB Enterprise Server 10.4 and later:

```bash
$ sudo mariadb-upgrade
```

And the utility is called [mysql\_upgrade](../../../../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) in MariaDB Enterprise Server 10.3 and 10.2:

```bash
$ sudo mysql_upgrade
```

### Testing

When MariaDB Enterprise Server is up and running on your system, you should test that it is working and there weren't any issues during startup.

1.  Connect to the server using MariaDB Client using the `root@localhost` user account.

    MariaDB Client is called [mariadb](../../../../../../clients-and-utilities/mariadb-client/) (ES10.4 and later) or `mysql` (ES10.3, ES10.2):

    ```bash
    $ sudo mariadb
    ```

    ```
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 9
    Server version: 10.5.28-22-MariaDB-Enterprise MariaDB Enterprise Server

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]>
    ```
2.  You can also verify the server version by checking the value of the [version](../../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables) system variable with the [SHOW GLOBAL STATUS](../../../../../../reference/sql-statements/administrative-sql-statements/show/show-status.md) statement:

    ```
    SHOW GLOBAL VARIABLES LIKE 'version';
    ```

    ```
    +---------------+-------------------------------+
    | Variable_name | Value                         |
    +---------------+-------------------------------+
    | version       | 10.5.28-22-MariaDB-Enterprise |
    +---------------+-------------------------------+
    ```
3.  You can also verify the server version by calling the [VERSION()](../../../../../../reference/sql-functions/secondary-functions/information-functions/version.md) function:

    ```sql
    SELECT VERSION();
    ```

    ```
    +-------------------------------+
    | VERSION()                     |
    +-------------------------------+
    | 10.5.28-22-MariaDB-Enterprise |
    +-------------------------------+
    ```

***

{% include "../../../../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
