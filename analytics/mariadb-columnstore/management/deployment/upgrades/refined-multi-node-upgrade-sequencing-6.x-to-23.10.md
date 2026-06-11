# Refined Multi-Node Upgrade Sequencing: 6.x to 23.10

These instructions detail the comprehensive upgrade path from MariaDB ColumnStore 6 to MariaDB ColumnStore 23.10 in a Multi-Node topology. To ensure a successful upgrade, it is highly critical to execute package updates simultaneously across all nodes and ensure strict CMAPI synchronization.

### 1. Pre-Upgrade Preparation

Before making any modifications, prepare your cluster and secure backups of your current state.

* Perform Backups: Consider taking a full production backup using `bash mcs_backup_manager.sh backup` (note that this will lock out writes during the backup). Determine the primary node by running `mcs cluster status` and take a DBRM backup using `bash mcs_backup_manager.sh dbrm_backup -bl <path> -nb before-shutdown-before-upgrade`.
* Save Configurations: On every node, create a timestamped directory and save backups of `Columnstore.xml`, `storagemanager.cnf`, `cmapi_server.conf`, and `server.cnf`.
* Set Maintenance Mode: On the MaxScale node, set each replica server to maintenance mode to prevent traffic routing during the upgrade. You can do this using MaxCtrl (e.g., `maxctrl set server mcs2 maintenance`). Verify this by running `maxctrl list servers`; the state should reflect `Maintenance`.
* Disable GTID Strict Mode: Temporarily disable the `gtid_strict_mode` system variable on each replica server to reduce the chance of replication issues. Comment out `gtid_strict_mode=1` in your configuration files (e.g., `/etc/my.cnf.d/server.cnf`).

### 2. Coordinated Service Shutdown

Services must be completely shut down across the cluster prior to upgrading packages.

1. Stop Cluster: On the primary node, stop the ColumnStore cluster by executing `mcs cluster stop`.
2.  Stop Node Services: On _every_ node, stop the MariaDB Enterprise Server, MariaDB ColumnStore, and CMAPI services.

    ```bash
    sudo systemctl stop mariadb-columnstore-cmapi
    sudo systemctl stop mariadb-columnstore
    sudo systemctl stop mariadb
    ```
3. Terminate Orphaned Processes: On every node, forcefully kill any remaining ColumnStore processes if needed. Check for processes like `PrimProc`, `ExeMgr`, `DMLProc`, `DDLProc`, `WriteEngineServer`, `StorageManager`, `controllernode`, `workernode`, `load_brm`, or `save_brm`, and execute `kill -9` on their PIDs. Stop all individual `mcs-*` systemctl services.
4. Final Pre-Upgrade Backup: Take one more DBRM backup on the primary node before proceeding with the installation.

### 3. Simultaneous Package Upgrades

{% hint style="danger" %}
To prevent version mismatch issues within the cluster configuration, package updates must be executed at the exact same time across all nodes.
{% endhint %}

1. Configure Package Manager: On every node, configure the package repository using the MariaDB Enterprise Release Helper script. Pass the target version using the `--mariadb-server-version="11.4"` flag (as Enterprise ColumnStore 23.10 is included with MariaDB Enterprise Server 11.4).
2. Execute Update: On _every_ node at the same time, execute the package update.
   * For YUM (RHEL/CentOS): `sudo yum update "MariaDB-*" "MariaDB-columnstore-engine" "MariaDB-columnstore-cmapi"`.
   * For APT (Debian/Ubuntu, version 2.0+): `sudo apt install --only-upgrade '?upgradable ?name(mariadb.*)'`.
3.  Disable Standalone Service: After the packages are updated, the standalone `mariadb-columnstore` service must be disabled on each node, as it will now be controlled directly by CMAPI.

    ```bash
    sudo systemctl stop mariadb-columnstore
    sudo systemctl disable mariadb-columnstore
    ```

### 4. CMAPI Synchronization and Service Startup

With packages updated, services must be brought back online in a specific order to allow CMAPI to synchronize the cluster state.

1.  Start Services: On every node, start and enable the MariaDB server and CMAPI services.

    ```bash
    sudo systemctl start mariadb-columnstore-cmapi
    sudo systemctl enable mariadb-columnstore-cmapi
    sudo systemctl start mariadb
    sudo systemctl enable mariadb
    ```
2. Verify Status: On the primary node, check the status using `mariadb -e "show status like '%Columnstore%';"` and `mcs cluster status`. Ensure all nodes and dbroots are present. (If there are issues, you may need to restore the `Columnstore.xml`backed up earlier and run `clearShm` ).
3. Start Cluster: On the primary node, start the cluster using `mcs cluster start`.

### 5. Post-Upgrade Finalization

1. Write Binary Log: On the primary server, run `mariadb-upgrade --write-binlog` to upgrade the data directory with binary logging enabled to update system tables.
2. Verify Versions: On each node, query `SHOW GLOBAL STATUS LIKE 'Columnstore_version';` to confirm the version reads `23.10.0`, and `SHOW GLOBAL VARIABLES LIKE 'version';` to check the ES version.
3. Data Validation: Run data checks (e.g., `sudo bash table_checker.sh -c 6 -m 1`) and compare output counts from before the upgrade. Confirm replication users are connected via `show processlist`.
4. Restore Configurations: Re-enable the `gtid_strict_mode` system variable on each replica server. Restart MariaDB to apply the changes.
5. Clear Maintenance Mode: Finally, on the MaxScale node, clear the maintenance mode for each replica using MaxCtrl (e.g., `maxctrl clear server mcs2 maintenance`). Confirm the mode is cleared by checking that the state no longer says `Maintenance` in `maxctrl list servers`.
