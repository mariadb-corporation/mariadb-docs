# Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.5

These instructions detail the **upgrade** from **MariaDB Community Server** to **MariaDB Enterprise Server 10.5** on a range of [supported Operating Systems](https://mariadb.com/engineering-policies/).

When [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/) is upgraded, the old version needs to be uninstalled, and the new version needs to be installed.

### Data Backup

Occasionally, issues can be encountered during upgrades. These issues can even potentially corrupt the database's data files, preventing you from easily reverting to the old installation. Therefore, it is generally best to perform a backup prior to upgrading. If an issue is encountered during the upgrade, you can use the backup to restore your MariaDB Server database to the old version. If the upgrade finishes without issue, then the backup can be deleted.

The instructions below show how to perform a backup using [MariaDB Backup](../../../../../../server-usage/backup-and-restore/mariadb-backup/). For more information about backing up and restoring the database, please see the [Recovery Guide](../../../../../../server-usage/backup-and-restore/).

1.  Take a full backup.

    On MariaDB Community Server 10.4 and later:

    ```bash
    $ sudo mariadb-backup --backup \
          --user=mariadb-backup_user \
          --password=mariadb-backup_passwd \
          --target-dir=/data/backup/preupgrade_backup
    ```

    On MariaDB Community Server 10.3 and earlier:

    ```bash
    $ sudo mariadb-backup --backup \
          --user=mariadb-backup_user \
          --password=mariadb-backup_passwd \
          --target-dir=/data/backup/preupgrade_backup
    ```

    Confirm successful completion of the backup operation.
2.  The backup must be prepared.

    On MariaDB Community Server 10.4 and later:

    ```bash
    $ sudo mariadb-backup --prepare \
          --target-dir=/data/backup/preupgrade_backup
    ```

    On MariaDB Community Server 10.3 and earlier:

    ```bash
    $ sudo mariadb-backup --prepare \
          --target-dir=/data/backup/preupgrade_backup
    ```

    Confirm successful completion of the prepare operation.
3. Backups should be tested before they are trusted.

### Audit Plugin Considerations

If you have the [MariaDB Audit Plugin](../../../../../../reference/plugins/mariadb-audit-plugin/) installed and if you are upgrading to MariaDB Enterprise Server 10.4 or later, then the audit plugin should be removed prior to the upgrade to prevent conflict with the MariaDB Enterprise Audit Plugin that is present in MariaDB Enterprise Server 10.4 or later.

It can be removed by using the [UNINSTALL SONAME](../../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) statement:

```sql
UNINSTALL SONAME 'server_audit';
```

And if you load the plugin in a configuration file using the `plugin_load_add` option, then the option should also be removed.

The MariaDB Enterprise Audit Plugin will automatically be installed after installing MariaDB Enterprise Server 10.4 or later.

### Uninstall the Old Version

When upgrading to MariaDB Enterprise Server, it is necessary to remove the existing installation of MariaDB Community Server, before installing MariaDB Enterprise Server. Otherwise, the package manager will refuse to install MariaDB Enterprise Server.

#### Stop the MariaDB Server Process

Before the old version can be uninstalled, we first need to stop the current MariaDB Server process.

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

{% tabs %}
{% tab title="Uninstall via YUM" %}
**Uninstall via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux)**

1.  Uninstall all of the MariaDB Community Server packages. Note that a wildcard character is used to ensure that all MariaDB Community Server packages are uninstalled:

    ```bash
    $ sudo yum remove "MariaDB-*"
    ```

    Be sure to check that this wildcard does not unintentionally refer to any of your custom applications:
2.  Uninstall the Galera package as well.

    The name of the package depends on the specific version of MariaDB Community Server.

    When upgrading from MariaDB Community Server 10.4 or later, the package is called `galera-4`:

    ```bash
    $ sudo yum remove galera-4
    ```

    When upgrading from MariaDB Community Server 10.3 or earlier, the package is called `galera`:

    ```bash
    $ sudo yum remove galera
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

    The name of the package depends on the specific version of MariaDB Community Server.

    When upgrading from MariaDB Community Server 10.4 or later, the package is called `galera-4`:

    ```bash
    $ sudo apt remove galera-4
    ```

    When upgrading from MariaDB Community Server 10.3 or earlier, the package is called `galera-3`:

    ```bash
    $ sudo apt remove galera-3
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

    The name of the package depends on the specific version of MariaDB Community Server.

    When upgrading from MariaDB Community Server 10.4 or later, the package is called `galera-4`:

    ```bash
    $ sudo zypper remove galera-4
    ```

    When upgrading from MariaDB Community Server 10.3 or earlier, the package is called `galera`:

    ```bash
    $ sudo zypper remove galera
    ```
3.  Before proceeding, verify that all MariaDB Community Server packages are uninstalled. The following command should not return any results:

    ```bash
    $ rpm --query --all | grep -i -E "mariadb|galera"
    ```
{% endtab %}
{% endtabs %}

### Install the New Version

MariaDB Corporation provides package repositories for YUM (RHEL, AlmaLinux, CentOS, Rocky Linux), APT (Debian, Ubuntu), and ZYpp (SLES).

{% tabs %}
{% tab title="Install via YUM" %}
**Install via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux)**

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the YUM package repository. Installable versions of MariaDB Enterprise Server are `11.4`, `10.6`, `10.5`, `10.4`, and `10.3`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#mariadb_es_repo_setup). The following directions reference `10.5`.

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
       --mariadb-server-version="10.5"
    ```

    1. _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
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

    Installable versions of MariaDB Enterprise Server are `11.4`, `10.6`, `10.5`, `10.4`, and `10.3`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](../../../../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#mariadb_es_repo_setup). The following directions reference `10.5`.

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

And the utility is called `mysql\_upgrade` in MariaDB Enterprise Server 10.3 and 10.2:

```bash
$ sudo mysql_upgrade
```

### Testing

When MariaDB Enterprise Server is up and running on your system, you should test that it is working and there weren't any issues during startup.

1.  Connect to the server using MariaDB Client using the `root@localhost` user account.

    MariaDB Client is called [mariadb](../../../../../../clients-and-utilities/mariadb-client/) (ES10.4 and later) or `mysql` (ES10.3 and earlier):

    ```bash
    $ sudo mariadb
    ```

    ```
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 9
    Server version: 10.5.28-MariaDB MariaDB Server

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]>
    ```
2.  You can also verify the server version by checking the value of the [version](../../../../../../reference/sql-functions/secondary-functions/information-functions/version.md) system variable with the [SHOW GLOBAL STATUS](../../../../../../reference/sql-statements/administrative-sql-statements/show/show-status.md) statement:

    ```sql
    SHOW GLOBAL VARIABLES LIKE 'version';
    ```

    ```
    +---------------+-----------------+
    | Variable_name | Value           |
    +---------------+-----------------+
    | version       | 10.5.28-MariaDB |
    +---------------+-----------------+
    ```
3.  You can also verify the server version by calling the [VERSION()](../../../../../../reference/sql-functions/secondary-functions/information-functions/version.md) function:

    ```sql
    SELECT VERSION();
    ```

    ```
    +-----------------+
    | VERSION()       |
    +-----------------+
    | 10.5.28-MariaDB |
    +-----------------+
    ```

***

{% include "../../../../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
