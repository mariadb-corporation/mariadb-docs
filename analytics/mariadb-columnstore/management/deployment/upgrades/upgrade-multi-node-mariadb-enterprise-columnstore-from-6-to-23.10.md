---
description: >-
  Upgrade a multi-node MariaDB Enterprise ColumnStore cluster from 6 to 23.10,
  with MaxScale-based replica maintenance mode, controlled service stops, and
  per-node upgrade steps.
---

# Upgrade Multi-Node MariaDB Enterprise ColumnStore from 6 to 23.10

These instructions detail the upgrade from **MariaDB Enterprise ColumnStore 6** to **MariaDB Enterprise ColumnStore 23.10** in a **Multi-Node** topology on a range of [supported Operating Systems](https://mariadb.com/engineering-policies/).

## Set Replicas to Maintenance Mode

This action is performed for each replica server **on the MaxScale node**.

Prior to upgrading, the replica servers must be [set to maintenance mode](../../node-maintenance-for-mariadb-enterprise-columnstore/set-a-node-to-maintenance-mode.md) in MaxScale. The replicas can be set to maintenance mode in MaxScale using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api). If you are using [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/administrative-tools-for-mariadb-maxscale-maxctrl), the replicas can be set to maintenance mode using the `set server` command:

```bash
maxctrl set server \
   mcs2 \
   maintenance
```

* As the first argument, provide the name for the server
* As the second argument, provide `maintenance` as the state

## Confirm Maintenance Mode is Set for Replicas

This action is performed **on the MaxScale node**.

Confirm that the replicas are set to maintenance mode in MaxScale using [MaxScale's REST API](http://localhost:8000/docs/server/service-management/admin-tools/maxscale/rest-api/). If you are using [MaxCtrl](http://localhost:8000/docs/server/ref/mxs/maxctrl/), the state of the replicas can be viewed using the [list servers](http://localhost:8000/docs/server/ref/mxs/maxctrl/list_servers/) command:

```bash
maxctrl list servers
```

```
┌────────┬───────────────┬──────┬─────────────┬──────────────────────┬────────┐
│ Server │ Address       │ Port │ Connections │ State                │ GTID   │
├────────┼───────────────┼──────┼─────────────┼──────────────────────┼────────┤
│ mcs3   │ 192.0.2.3     │ 3306 │ 0           │ Maintenance, Running │ 0-1-17 │
├────────┼───────────────┼──────┼─────────────┼──────────────────────┼────────┤
│ mcs2   │ 192.0.2.2     │ 3306 │ 0           │ Maintenance, Running │ 0-1-17 │
├────────┼───────────────┼──────┼─────────────┼──────────────────────┼────────┤
│ mcs1   │ 192.0.2.1     │ 3306 │ 0           │ Master, Running      │ 0-1-17 │
└────────┴───────────────┴──────┴─────────────┴──────────────────────┴────────┘
```

If the node is properly in maintenance mode, then the `State` column will show `Maintenance` as one of the states.

## Disable GTID Strict Mode

This action is performed **on each replica server**.

The [gtid\_strict\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_strict_mode) system variable must be disabled for this upgrade procedure. If the `gtid_strict_mode` system variable is enabled in any configuration files, disable it temporarily until the upgrade procedure is complete.

You can check if the `gtid_strict_mode` system variable is set in a configuration file by executing `my_print_defaults` command with the `mysqld` option:

```bash
my_print_defaults --mysqld \
   | grep "gtid[-_]strict[-_]mode"
```

```bash
--gtid_strict_mode=1
```

If the `gtid_strict_mode` system variable is set, you can temporarily disable it by adding `#` in front of it in the configuration file, so that it will be treated as a comment and ignored:

```ini
[mariadb]
...
# temporarily commented out for upgrade
# gtid_strict_mode=1
```

## Shutdown ColumnStore

Prior to upgrading, MariaDB Enterprise ColumnStore must be shutdown.

```bash
mcs cluster stop
```

## Stop Services

This action is performed **on each ColumnStore node**.

Prior to upgrading, several services must be stopped on each ColumnStore node:

1.  Stop the [CMAPI](../../../reference/cmapi/) service:

    ```bash
    sudo systemctl stop mariadb-columnstore-cmapi
    ```
2.  Stop the MariaDB Enterprise ColumnStore service:

    ```bash
    sudo systemctl stop mariadb-columnstore
    ```
3.  Stop the MariaDB Enterprise Server service:

    ```bash
    sudo systemctl stop mariadb
    ```

## Upgrade to the New Version

MariaDB Corporation provides package repositories for YUM (RHEL, CentOS, Rocky Linux) and APT (Debian, Ubuntu).

### Upgrade via YUM (RHEL, CentOS, Rocky Linux)

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the YUM package repository.

    Enterprise ColumnStore 23.10 is included with MariaDB Enterprise Server 11.4. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage).

    To configure YUM package repositories:

    ```bash
    sudo yum install curl
    ```

    ```
    curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```bash
    echo "${checksum} mariadb_es_repo_setup" | sha256sum -c -
    ```

    ```
    chmod +x mariadb_es_repo_setup
    ```

    ```bash
    sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="11.4"
    ```

    1. Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the [Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage#versions) section at the bottom of the [MariaDB Package Repository Setup and Usage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) page. Substitute `${checksum}` in the example above with the latest checksum.
3.  Update MariaDB Enterprise Server and package dependencies:

    ```bash
    sudo yum update "MariaDB-*" "MariaDB-columnstore-engine" "MariaDB-columnstore-cmapi"
    ```

### Upgrade via APT (Debian, Ubuntu)

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the APT package repository.

    Enterprise ColumnStore 23.10 is included with MariaDB Enterprise Server 11.4. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](http://localhost:8000/docs/server/ref/mariadb_es_repo_setup/).

    To configure APT package repositories:

    ```bash
    sudo apt install curl
    ```

    ```bash
    curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```bash
    echo "${checksum}  mariadb_es_repo_setup" sha256sum -c -
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

    1. Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the [Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage#versions) section at the bottom of the [MariaDB Package Repository Setup and Usage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) page. Substitute `${checksum}` in the example above with the latest checksum.
3.  Update MariaDB Enterprise Server and package dependencies.

    The update command depends on the installed APT version, which can be determined by executing the following command:

    ```bash
    apt --version
    ```

    ```
    apt 2.0.9 (amd64)
    ```

    For versions prior to APT 2.0, execute the following command:

    ```bash
    sudo apt install --only-upgrade "mariadb*"
    ```

    For APT 2.0 and later, execute the following command:

    ```bash
    sudo apt install --only-upgrade '?upgradable ?name(mariadb.*)'
    ```

## Disable ColumnStore Service

This action is performed **on each ColumnStore node**.

After upgrading, the MariaDB Enterprise ColumnStore service should be stopped, since it will be controlled by [CMAPI](../../../reference/cmapi/):

```bash
sudo systemctl stop mariadb-columnstore
sudo systemctl disable mariadb-columnstore
```

CMAPI disables the Enterprise ColumnStore service in a multi-node deployment. The Enterprise ColumnStore service will be started as-needed by the CMAPI service, so it does not need to start automatically upon reboot.

## Start Services

This action is performed **on each ColumnStore node**.

After upgrading, the [CMAPI](../../../reference/cmapi/) service and the MariaDB Enterprise Server service must be started on each ColumnStore node:

1.  Start the CMAPI service:

    ```bash
    sudo systemctl start mariadb-columnstore-cmapi
    ```
2.  Start the MariaDB Enterprise Server service:

    ```bash
    sudo systemctl start mariadb
    ```

## Write Binary Log

On the primary server, run [mariadb-upgrade](http://localhost:8000/docs/server/ref/mdb/cli/mariadb-upgrade/) to upgrade the data directory with binary logging enabled to update the system tables:

```bash
mariadb-upgrade --write-binlog
```

## Start ColumnStore

After upgrading, MariaDB Enterprise ColumnStore must be started.

```bash
mcs cluster start
```

## Enable GTID Strict Mode

This action is performed **on each replica server**.

If you temporarily disabled the [gtid\_strict\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_strict_mode) system variable in the [Disable GTID Strict Mode](upgrade-multi-node-mariadb-enterprise-columnstore-from-6-to-23.10.md#disable-gtid-strict-mode) step, it can be re-enabled. If the `gtid_strict_mode` system variable was temporarily disabled in any configuration files, re-enable it.

## Confirm ColumnStore Version

This action is performed **on each ColumnStore node**.

After upgrading, it is recommended to confirm the Enterprise ColumnStore version on each ColumnStore node. Connect to the node using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) and query the `Columnstore_version` status variable with [SHOW GLOBAL STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-status):

```sql
SHOW GLOBAL STATUS LIKE 'Columnstore_version';
```

```
+---------------------+---------+
| Variable_name       | Value   |
+---------------------+---------+
| Columnstore_version | 23.10.0 |
+---------------------+---------+
```

## Confirm ES Version

This action is performed **on each ColumnStore node**.

After upgrading, it is recommended to confirm the ES version on each ColumnStore node. Connect to the node using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) and query the [version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#version) system variable with [SHOW GLOBAL VARIABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-variables):

```sql
SHOW GLOBAL VARIABLES LIKE 'version';
```

```
+---------------+----------------------------------+
| Variable_name | Value                            |
+---------------+----------------------------------+
| version       | 10.6.9-5-MariaDB-enterprise-log  |
+---------------+----------------------------------+
```

## Clear Maintenance Mode for Replicas

This action is performed for each replica server **on the MaxScale node**.

After the upgrade, maintenance mode for each replica has been cleared in MaxScale using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api). If you are using [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/administrative-tools-for-mariadb-maxscale-maxctrl), maintenance mode can be cleared using the `clear server` command:

```bash
maxctrl clear server \
   mcs2 \
   maintenance
```

* As the first argument, provide the name for the server
* As the second argument, provide `maintenance` as the state

## Confirm Maintenance Mode is Cleared for Replicas

This action is performed for each replica server **on the MaxScale node**.

Confirm that maintenance mode in MaxScale has been cleared for each replica using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api). If you are using [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/administrative-tools-for-mariadb-maxscale-maxctrl), the state of the replicas can be viewed using the `list servers` command:

```bash
maxctrl list servers
```

```
┌────────┬───────────────┬──────┬─────────────┬─────────────────┬─────────┐
│ Server │ Address       │ Port │ Connections │ State           │ GTID    │
├────────┼───────────────┼──────┼─────────────┼─────────────────┼─────────┤
│ mcs3   │ 192.0.2.3     │ 3306 │ 0           │ Slave, Running  │ 0-3-159 │
├────────┼───────────────┼──────┼─────────────┼─────────────────┼─────────┤
│ mcs2   │ 192.0.2.2     │ 3306 │ 0           │ Slave, Running  │ 0-1-88  │
├────────┼───────────────┼──────┼─────────────┼─────────────────┼─────────┤
│ mcs1   │ 192.0.2.1     │ 3306 │ 0           │ Master, Running │ 0-1-88  │
└────────┴───────────────┴──────┴─────────────┴─────────────────┴─────────┘
```

If the node is no longer in maintenance mode, then the `State` column will no longer show `Maintenance` as one of the states.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
