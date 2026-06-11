# Emergency S3 Data Reset Procedure

This document outlines emergency recovery workflows for cases where local metadata becomes terminally out of sync with S3 storage or when cluster master and DBroot ownership configurations become corrupted.

## 1. Resetting ColumnStore S3 Storage Data

In some scenarios, you may need to completely reset your database data by deleting all contents within your S3 bucket. This procedure clears local caches, wipes the bucket, and resets the MariaDB server databases.

1. Shutdown ColumnStore Stop the ColumnStore cluster:

```bash
mcsShutdown
```

2. Remove On-Disk Caches & Metadata On each node in the cluster, remove the local caches and metadata that act as pointers to the S3 bucket. If your cluster uses a shared `/var/lib/columnstore/storagemanager/` directory for high availability (HA), you may only need to run these commands once:

```bash
rm -rf /var/lib/columnstore/storagemanager/cache
rm -rf /var/lib/columnstore/storagemanager/metadata
rm -rf /var/lib/columnstore/storagemanager/journal
```

3. Delete Everything from the S3 Bucket Depending on your access, delete all contents within the bucket. This can often be done via a GUI, or using the AWS CLI:

```bash
aws s3 sync . s3://bucket-name --delete
```

4. Start ColumnStore Bring the cluster back online:

```bash
mcsStart
```

5. Clean Up MariaDB Databases Delete the relevant databases or ColumnStore tables from the MariaDB server.

```sql
mariadb
SHOW DATABASES;
DROP DATABASE test;
```

6. Validate Table Creation Confirm the reset was successful by creating a new test database and table:

```sql
CREATE DATABASE test;
USE test;
CREATE TABLE t1 (a int) ENGINE=Columnstore;
```

## 2. Fixing Mixed DBroot Ownership and Master Node Issues

If node DBroot ownership becomes mixed (e.g., node 2 owns DBroot 4 but its `data4` directory has no data), or if the master node shifts unexpectedly, users may encounter `ERROR 1815 (HY000): Internal error: IDB-2039`. Use one of the following methods to reset the cluster configuration.

### Method A: Restoration via `Columnstore.xml.restore`

_Note: This method requires approximately 30 minutes of downtime and relies on having a `Columnstore.xml.restore` file created during the initial cluster setup_.

1. Set Maintenance Mode: Put replica servers into maintenance mode via MaxScale.

{% code overflow="wrap" expandable="true" %}
```bash
maxctrl set server server2 maintenance
maxctrl set server server3 maintenance
```
{% endcode %}

2. **Shutdown Cluster**: Run \`mcsShutdown\` on the master node.
3. **Stop Services:** On each node (starting with replicas), stop the services and clear shared memory.

```bash
   sudo systemctl stop mariadb
   sudo systemctl stop mariadb-columnstore-cmapi
   clearShm
```

4.  **Kill Zombie Processes**: Ensure no ColumnStore processes remain active.

    ```bash
    ps -ef | grep mysql**Backup DBRM:** On the master node, back up the DBRM files.
    ```
5. **Backup DBRM:** On the master node, back up the DBRM files.

```bash
   # For S3 deployments
   cp -R /var/lib/columnstore/storagemanager/* /tmp/DBRMbackup-$(date +"%d-%m-%Y-%s")
```

6. **Restore Configuration**: On each node, back up the current XML and restore the original.

{% code overflow="wrap" expandable="true" %}
```
cp /etc/columnstore/Columnstore.xml /tmp/Columnstore.xml.backup 
cp /etc/columnstore/Columnstore.xml.restore Columnstore.xml 
```
{% endcode %}

7. **Restart Services:** On each node (starting with the master), clear shared memory and restart services.

```bash
clearShm
sudo systemctl start mariadb-columnstore-cmapi
sudo systemctl start mariadb
```

8. Start Cluster: Run `mcsStart` on the master and wait 30 seconds. Verify cluster health using `mcsStatus`.
9. Clear Maintenance Mode: Remove the MaxScale maintenance blocks.

{% code overflow="wrap" expandable="true" %}
```bash
maxctrl clear server server2 maintenance 
maxctrl clear server server3 maintenance
```
{% endcode %}

### Method B: Manual Cluster Reset

{% hint style="info" %}
_This method requires approximately 2 hours of downtime and completely declusterizes the nodes before rebuilding them_.
{% endhint %}

1. **Gather IPs and Backup:** Run `ifconfig` to note all server IP addresses\[cite: 4]. Copy `/etc/columnstore/Columnstore.xml` to `/etc/columnstore/Columnstore.xml.beforeResetBackup` on all nodes\[cite: 4].
2. **Prepare Master and MaxScale:** Put replicas in maintenance mode via `maxctrl`\[cite: 4]. On the master, note your CMAPI key from `/etc/columnstore/cmapi_server.conf`, run `mcsShutdown`, and back up your DBRM files\[cite: 4].
3.  **Declusterize Nodes:** On each node, stop MariaDB and CMAPI\[cite: 4]. Copy the default XML to reset the node\[cite: 4].

    ```bash
    systemctl stop mariadb
    systemctl stop mariadb-columnstore-cmapi
    cp /etc/columnstore/Columnstore.xml.new /etc/columnstore/Columnstore.xml
    clearShm
    systemctl start mariadb 
    systemctl start mariadb-columnstore-cmapi
    ```

{% hint style="info" %}
Ensure `Columnstore.xml` only references `127.0.0.1` or `0.0.0.0`\[cite: 4]. You can verify the decluster was successful if `mcsStatus` shows `"num_nodes": 0`\[cite: 4].
{% endhint %}

4. **Rebuild Cluster**: On the master node, add the nodes back in the exact order of desired DBroot ownership (starting with the master as DBroot 1).

{% code overflow="wrap" %}
```bash
curl -k -s -X PUT https://127.0.0.1:8640/cmapi/0.4.0/cluster/node --header 'Content-Type:application/json' --header 'x-api-key:xxxxxx' --data '{"timeout":120, "node": "yyyyy"}' | jq .
```
{% endcode %}

5.  Restore Customizations: Compare your `Columnstore.xml.beforeResetBackup` with the new configuration and reapply customizations using `mcsSetConfig`.

    ```bash
    mcsSetConfig CrossEngineSupport User <username>
    mcsSetConfig CrossEngineSupport Password <password>
    ```
6. **Finalize:** Save the working configuration as `Columnstore.xml.restore`, bounce the cluster (`mcsShutdown` followed by `mcsStart`), and clear MaxScale maintenance mode.
