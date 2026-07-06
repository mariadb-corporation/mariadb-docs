# System Troubleshooting

## Verifying CMAPI Cluster Status

The `mcsStatus` command is an administrative alias for an HTTP `curl` request. Firewalls and security programs can block or interfere with this communication channel.

### Status Verification Commands

*   Execute via administrative alias:

    ```bash
    mcsStatus
    ```
*   Execute via explicit network request:

    <pre class="language-bash" data-overflow="wrap"><code class="lang-bash">curl -s https://127.0.0.1:8640/cmapi/0.4.0/cluster/status --header 'Content-Type:application/json' --header 'x-api-key:xxxxxxxxxxxxxxxx' -k | jq .
    </code></pre>

### Operational Troubleshooting Checklist

If the status check command fails, encounters a connection break, or returns empty results, execute the following diagnostic verification steps in sequence:

1. Check for security programs interfering: Try running the connection string with elevated permissions (`sudo curl`), as local system configurations can cut the connection. Use tracking utilities like `htop`, `top`, or `ps` to look for interfering security services.
   * _Examples to audit:_ `falcon-senor`, `falcond`, `falcon-sensor`, `AppArmor`, or `seliux`.
   * _Remediation:_ Turn these applications off, recycle the cluster instance, and attempt the status check again.
2. Verify node port connectivity: The remote nodes must have port `8640` open for communication via a TCP connection.
   *   Run the socket inspection utility to verify which processes are actively bound to system ports:

       ```bash
       ss -ntlp
       ```
3. Validate uniform authorization keys (`x-api-key`): The authentication header string must match across all nodes in the deployment.
   * Inspect the following configuration file path to verify key synchronization:
     * File Location: `/etc/columnstore/cmapi_server.conf`
     * Target Section: `[Authentication]`
     * Variable Line: `x-api-key=xxxxxxx`
4. Confirm JSON processor installation: The API outputs a JSON data stream that is piped directly into `jq`. If the server does not have this utility installed, the result is piped into nothing, returning blank terminal feedback.
   *   Install the prerequisite package dependency via the package manager:

       ```bash
       yum install jq
       ```
5. Check IP address targeting loops: Manually run the `curl` query against the local loopback address (`127.0.0.1`) and compare the output structure against a query run against the known master instance.
   * If the results do not match, it indicates that `/etc/columnstore/Columnstore.xml` is not identical across all cluster nodes.
   * _Remediation:_ Manually copy a uniform copy of `Columnstore.xml` to all nodes, restart the `cmapi` service, and try again.
6.  Reload default terminal environment settings: If the shell fails to recognize baseline commands, refresh the tracking aliases:

    ```bash
    source /etc/profile.d/columnstoreAlias.sh
    # Alternative file target to source: /usr/share/columnstore/columnstoreAlias
    ```

## Parsing CMAPI JSON Telemetry Output

When executed successfully, CMAPI generates a process status payload tracking metadata across the cluster topology:

```json
{
  "timestamp": "2021-12-21 19:01:50.866654",
  "172.31.22.252": {
    "timestamp": "2021-12-21 19:01:50.872922",
    "uptime": 361172,
    "dbrm_mode": "master",
    "cluster_mode": "readwrite",
    "dbroots": [ "1" ],
    "module_id": 1,
    "services": [
      { "name": "workernode", "pid": 12292 },
      { "name": "controllernode", "pid": 12370 },
      { "name": "PrimProc", "pid": 12387 },
      { "name": "ExeMgr", "pid": 12444 },
      { "name": "WriteEngine", "pid": 12465 },
      { "name": "DMLProc", "pid": 12474 },
      { "name": "DDLProc", "pid": 12504 }
    ]
  },
  "num_nodes": 3
}
```

### Key Output Interpretation Rules

* Node Headcount (`num_nodes`): Verify if the expected number of nodes are actively part of the cluster. If 1 or more nodes fail and drop out, deeper troubleshooting is required, and `Columnstore.xml` will likely be shuffled as the node is considered inactive.
* Service Presence Tracking: CMAPI evaluates the process list on each node against specific binary names, but it cannot identify if processes are orphaned or not working as expected.
  * Master Node Requirement: The server acting as master (`dbrm_mode="master"`) must have exactly 7 running processes. If fewer appear, some may be failing to start; inspect the system logs or check `/var/log/mariadb/columnstore/trace/` and `/var/log/mariadb/columnstore/corefiles/` for core dumps or stack traces before segmentation faults occurred.
  * Replica Node Requirement: Replica nodes (`dbrm_mode="slave"`) must have exactly 4 running processes. Check the logs if a service fails to initialize.
* Cluster Modes (`cluster_mode`): Find the node where `dbrm_mode=master` and check its `cluster_mode` flag. Replicas always remain locked into `readonly` mode. A healthy master should read `readwrite`. If the master node is in `readonly`, a severe issue has occurred, forcing the system into safe mode until manual intervention corrects the root cause. This state transition historically occurs because:
  * Stuck rollbacks originating from failed transactions or bulk `cpimport` tasks.
  * Disk Block Resource Manager (BRM) files cannot be updated/written to, or are missing/corrupted.
  * Certain services cannot start, such as `storagemanager` being unable to reach external S3 storage buckets.
* Master Resolution Dependencies: CMAPI determines which node is the master dynamically by utilizing the internal `CEJ` user profile to inspect the database process list for active replication threads. If `CEJ` user credentials or grant permissions are broken, CMAPI breaks completely.
* DBroot Mappings: The tracked `dbroots` values should match the `module_id` to confirm no failover states have transpired. The active master node traditionally owns `DBroot 1`. If a role change occurs, the database root responsibilities get shuffled across surviving instances.

## ColumnStore Engine Log Breakdown

### Parsing the `debug.log` Text String Layout

The primary diagnostic log file is located at `/var/log/mariadb/columnstore/debug.log`. Output entries are written according to a standardized layout format:

{% code overflow="wrap" %}
```
[Date Time] [Hostname] [Process Name][Process ID] [unknown timing] |[Internal Transaction ID]|0|0| [Message or SQL statement or transaction]|[Database]|
```
{% endcode %}

### Tracking Operational Timings via Internal Transaction IDs

1. Identify the transaction scope: Locate the numeric `Internal Transaction ID` that appears between the two pipe characters (`||`). For example: `|22|`.
2. Correlate matching execution markers: Map the corresponding `Start SQL statement` and `End SQL statement` rows that share the same transaction ID to find the rough timing of queries. For instance, a `LOAD DATA INFILE` operation spanning these markers reveals an exact execution window.
3. Trace long-running queries: For extended or heavy operations, these bounding lines will not appear back-to-back because other cluster nodes interleave separate log output statements. Search explicitly on the unique transaction ID (e.g., `|22|`) to compile a continuous timeline for that single query lifecycle.

### Administrative Log Investigation Patterns

Execute the following `grep` search strings to extract critical milestones from system logs:

*   Find executed SQL query strings:

    ```bash
    grep "Start SQL statement" /var/log/mariadb/columnstore/debug.log
    ```
*   Track the lifecycle of bulk `cpimport` tasks:

    <pre class="language-bash" data-overflow="wrap"><code class="lang-bash">grep 'cpimport.bin\[' /var/log/mariadb/columnstore/debug.log | grep -E 'Initiating BulkLoad:|finished loading table'
    </code></pre>
*   Locate cluster startup timestamps:

    ```bash
    grep "put_start starts" /var/log/messages
    ```
*   Verify successful `loadbrm` executions with the extent map:

    ```bash
    grep "mcs-loadbrm.py" /var/log/messages
    ```
*   Audit if `DMLProc` handles rollbacks correctly during initialization:

    ```bash
    grep -A 5 "DMLProc starts rollbackAll" /var/log/messages
    ```
*   Confirm successful system shutdowns via `save_brm` checkpoints:

    <pre class="language-bash" data-overflow="wrap"><code class="lang-bash">sudo grep -E "mcs-savebrm.py: Saved to /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves" /var/log/messages
    </code></pre>

## Common Startup Errors and Remediation Strategies

### 1. Object Mapping Failures (`IDB-2006: does not exist in Columnstore`)

```
writeenginesplit[4423]: ERROR : IDB-2006: 'test.flights' does not exist in Columnstore
writeenginesplit[4423]: Please make sure both schema and table exists!!
```

* Root Cause: The underlying MySQL definition metadata files match successfully at `/var/lib/mysql/{database}/{tablename}.frm`, but the internal object mappings linking those columns to lower-level ColumnStore elements have broken or are missing entirely.
*   Remediation Action (Single Affected Table): If the data records contained in the target table are not critical, recreate the structural definitions to instantiate brand new object identification tracking values within the columnar storage maps:

    ```sql
    SHOW CREATE TABLE flights;
    DROP TABLE flights;
    CREATE TABLE flights xxxx;
    ```
* Remediation Action (System-Wide Mismatch): If numerous database tables throw this same exception concurrently when queried, the wrong extent map file has likely been loaded into memory. Restore system operations by restoring a valid historical extent map backup and its matching transaction journal. If a functional backup map cannot be obtained, execute `mcsRebuildEM` to reconstruct the map properties, which may succeed if the raw data files still reside intact inside each independent `dbroot` workspace directory path. If those source data files are also missing, no further recovery paths exist.
*   Remediation Action (Front-End/Back-End Out of Sync): If the table information between the front end and back end is out of sync, a table can become impossible to either drop or create &mdash; `DROP TABLE` fails with `IDB-2006: ... does not exist in Columnstore`, while `CREATE TABLE` fails with `Table ... already exists`. Drop the table with the `RESTRICT` option to clear the mismatch, after which the table can be created again:

    ```sql
    DROP TABLE table1 RESTRICT;
    ```

### 2. Hanging Ingestion Rollbacks on Cluster Boot

```
DMLProc[4003]: I 20 CAL0002: DMLProc starts rollbackAll.
DMLProc[4003]: I 20 CAL0002: DMLProc will rollback 0 tables.
DMLProc[4003]: I 20 CAL0002: DMLProc finished rollbackAll
```

* Root Cause: These log sequences appear normally during system startup phases as `DMLProc` reviews the transaction layers to finalize outstanding changes or roll back bulk updates that were abruptly canceled or failed prior to the system restart.
* Mechanics: These tracking records are maintained inside the active `BRM_saves_journal` structure, with historical rollback fragments potentially existing inside corresponding `.vss` and `.vbbm` block files.
* Workaround: If cluster initialization operations become completely blocked or hang indefinitely while processing failed rollbacks, restoring an older version or backup copy of the transaction journal can bypass the loop. Note that pursuing this cleanup strategy will result in the permanent loss of any other distinct transaction writes recorded within that specific journal window.

### 3. Verification of System Catalog States

```
writeengine[7393]: I 19 CAL0060: dbbuilder system catalog status: System catalog appears to exist. It will remain intact for reuse. The database is not recreated.
```

* Root Cause: This represents a standard informational notification output during cluster boot procedures confirming that ColumnStore successfully detects a valid pre-existing installation and will load the data blocks normally without resetting or overwriting deployment configurations.

### 4. Table Lock File Permission Blockages

```
IDBFile[3928]: Failed to open file: /var/lib/columnstore/data1/systemFiles/dbrm/tablelocks, exception: unable to open Buffered file
controllernode[3928]: TableLockServer::load(): could not open the save file/var/lib/columnstore/data1/systemFiles/dbrm/tablelocks
```

* Root Cause: The database application layer cannot modify or access the metadata lock boundaries because of an operating system file write permission conflict on the physical file system tracking asset.
*   Remediation Action: Switch your active terminal shell context to the primary database service user profile (`mysql`) and initialize a clean instance of the lock tracking file path manually to clear the access conflict:

    ```bash
    sudo -su mysql touch var/lib/columnstore/data1/systemFiles/dbrm/tablelocks
    ```
