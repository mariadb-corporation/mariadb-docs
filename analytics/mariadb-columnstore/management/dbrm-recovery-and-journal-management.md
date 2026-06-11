# DBRM Recovery and Journal Management

The procedure outlines steps for bringing ColumnStore back online when a failed rollback blocks startup, as well as managing timeout configurations for large extent maps. In general, rollback fragments usually exist within `vss` and `vbbm` files.

## Resolving Stuck `load_brm` and Failed Rollbacks

If a system is stuck due to a failed transaction rollback, you must manually clear the problematic files. The procedures differ depending on your deployment type.

### Local Storage Deployments

For local storage deployments, you can refer to `columnstore_review.sh --clearrollback`. To perform the recovery manually, follow these steps:

1. Verify Master State: On the master node, shut down the cluster and check the BRM saves.

```bash
mcsShutdown
cat /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_current
```

* The output should be `"BRM_saves"`.
* If it is not, you will need to reload a backup extent map.

2. Terminate Leftover Processes: On each node, check for and kill any remaining ColumnStore processes (aside from `mariadbd`).

{% code overflow="wrap" %}
```bash
ps -ef | grep ^mysql
ps -ef | grep -E '(PrimProc|ExeMgr|DMLProc|DDLProc|WriteEngineServer|StorageManager|controllernode|workernode)' | grep -v "grep" | awk '{print $2}' | xargs kill
```
{% endcode %}

3. Verify Configuration and Restart CMAPI: On each node, verify the configuration files match and restart the CMAPI service.

```bash
ll /etc/columnstore/Columnstore.xml
clearShm
systemctl restart mariadb-columnstore-cmapi
```

4. Backup DBRM Files: On the master node, back up the system dbrm files before proceeding.

```bash
cd /var/lib/columnstore/data1/systemFiles/dbrm
tar cvf ~/dbrm.`date +'%m%dT%H%M%S'`.tar BRM_saves_current BRM_saves_em BRM_saves_journal BRM_saves_vbbm BRM_saves_vss SMTxnID oidbitmap tablelocks
```

5. Clear VSS and VBBM files: On the master node, truncate the `vss` and `vbbm` files. This sends a NULL value to clear them out, allowing a fresh copy upon restart.

```bash
truncate -s 0 BRM_saves_vss
truncate -s 0 BRM_saves_vbbm
```

{% hint style="info" %}
You may need to address `tablelocks` (e.g., `rm -rf tablelocks`, `touch tablelocks`, `chmod 755 tablelocks`, `chown mysql:mysql tablelocks`).

You may need to truncate `/var/lib/columnstore/data1/versionbuffer.cdf` or `BRM_saves_journal`.
{% endhint %}

6. Restart System: In a separate session, monitor the logs while starting the system.

```bash
tail -100f /var/log/messages | egrep " python3|mcs-"
mcsStart
```

#### **Advanced Local Troubleshooting**

If, during startup, `/var/log/messages` indicates a rollback is still trying to process after clearing `BRM_saves_vss` and `BRM_saves_vbbm` (e.g., showing `DMLProc starts rollbackAll` or `DMLProc is rolling back transaction`), follow these steps:

*   Delete version buffer and journal: Truncate both files.

    ```bash
    > /var/lib/columnstore/data1/versionbuffer.cdf
    > BRM_saves_journal
    ```
*   Force clear table locks: If issues persist, clear any table locks in addition to the prior truncations.

    ```bash
    cleartablelock -l <lockid>
    ```
* Reload extent map: If the system is still unable to start, try reloading a backup extent map from prior to the lock or rollback occurrence.

### S3 Deployments

For deployments utilizing S3, follow this modified procedure:

1. Verify Master State: Shut down the cluster and check `BRM_saves_current` (should return "BRM\_saves", otherwise reload a backup extent map).

```bash
mcsShutdown
smcat /data1/systemFiles/dbrm/BRM_saves_current 2>/dev/null
```

2. Terminate Leftover Processes & Restart CMAPI: Kill hanging processes on each node, clear shared memory, and restart CMAPI.

```bash
ps -ef | grep -E '(PrimProc|ExeMgr|DMLProc|DDLProc|WriteEngineServer|StorageManager|controllernode|workernode)' | grep -v "grep" | awk '{print $2}' | xargs kill
clearShm
systemctl restart mariadb-columnstore-cmapi
```

3. Backup Metadata: On the master node, back up the storage manager metadata.

```bash
cd /var/lib/columnstore/storagemanager/metadata/data1/systemFiles/dbrm/
mkdir /tmp/dbrm-before-clearing-$(date +'%m%d')
cp * /tmp/dbrm-before-clearing-$(date +'%m%d')
```

4. Clear Meta Files and Cache: Remove and recreate the `vss` and `vbbm` metadata files, then purge the storage manager cache.

```bash
rm -rf BRM_saves_vss.meta BRM_saves_vbbm.meta
sudo -su mysql touch BRM_saves_vss.meta
sudo -su mysql touch BRM_saves_vbbm.meta
rm -rf /var/lib/columnstore/storagemanager/cache/data1/*;
mkdir /var/lib/columnstore/storagemanager/cache/data1/downloading; chown mysql:mysql -R /var/lib/columnstore/storagemanager/cache ;
```

5. Restart System: Tail the logs and start the system.

```bash
tail -100f /var/log/messages | egrep " python3|mcs-"
mcsStart
```

## Managing Timeouts for Large Extent Maps

When processing extremely large extent maps (e.g., massive cpimports exceeding 5 billion records) or experiencing long shutdowns for `brm_save`, adjusting default timeouts may be necessary.

### Systemd Service Timeouts

You can raise the standard systemd timeouts for worker and controller nodes:

*   Worker Nodes: Raise `TimeoutStopSec` and `TimeoutStartSec` to `1800`.

    ```bash
    systemctl cat mcs-workernode@1.service
    systemctl cat mcs-workernode@2.service
    ```
*   Controller Node: Raise `TimeoutStopSec` to `900` for massive cpimports.

    ```bash
    systemctl cat mcs-controllernode.service
    ```
* After modifying these values, apply them via `systemctl daemon-reload`.

### Long Shutdowns for BRM Save

To adjust timeout variables for DML processing and DBRM loading:

* DMLProc: Open `/usr/lib/systemd/system/mcs-dmlproc.service` and set `TimeoutStopSec=15min` and `TimeoutStartSec=15min`.
* LoadBRM: Open `mcs-loadbrm.service` and set `TimeoutStopSec=1800` and `TimeoutStartSec=1800`.
*   mcsShutdown Alias: Update the timeout for the shutdown command in the alias script to `900`.

    ```bash
    vi /etc/profile.d/columnstoreAlias.sh
    # Update to: '{"timeout":900}'
    ```

### CMAPI Timeouts

Occasionally, CMAPI may force a restart of all processes every few seconds if operations exceed its default thresholds. To increase the CMAPI timeout:

1.  Stop the service and clear shared memory.

    ```bash
    mcsShutdown
    systemctl stop mariadb-columnstore-cmapi
    clearShm
    ```
2.  Edit the CMAPI helpers file.

    ```bash
    sudo vi /usr/share/columnstore/cmapi/cmapi_server/helpers.py
    ```
3. On line 290, raise the timeout to a higher number (e.g., higher than 120 or 300).
4.  Restart the service.

    ```bash
    systemctl start mariadb-columnstore-cmapi
    ```
