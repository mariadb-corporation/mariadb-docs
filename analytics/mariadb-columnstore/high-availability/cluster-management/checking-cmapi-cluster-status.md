# Checking CMAPI Cluster Status

The cluster status can be queried using either the shorthand administrative status command or a direct REST API connection utility execution:

1\. Execute via the administrative utility command:

```bash
mcsStatus
```

2\. Execute via direct REST API connection call:

{% code overflow="wrap" %}
```bash
curl -s https://127.0.0.1:8640/cmapi/0.4.0/cluster/status --header 'Content-Type:application/json' --header 'x-api-key:xxxxxxxxxxxxxxxx' -k | jq .
```
{% endcode %}

{% hint style="info" %}
Operational Note: The `mcsStatus` command functions as an alias wrapper for an underlying HTTP `curl` request. Firewalls and network security utilities can block or interfere with this transmission channel.
{% endhint %}

## Operational Troubleshooting Checklist

If the status check command fails, encounters a connection break, or yields no console output, execute the following diagnostic verification steps in sequential order:

{% stepper %}
{% step %}
### Check for interfering security programs

* Try running the `curl` statement with elevated system access prefixes (e.g., `sudo curl`), as local operating system controls can disrupt and abruptly terminate the active network connection thread.
* Use system activity monitoring utilities such as `htop`, `top`, or `ps` to search the runtime process tables for active endpoint security or access management utilities.
* Examples of security systems to inspect for include: `falcon-senor`, `falcond`, `falcon-sensor`, `AppArmor`, or `selinux`.
* If these applications are found to be blocking tracking loops, turn them off, recycle the active ColumnStore cluster instances, and retry the status command.
{% endstep %}

{% step %}
### Verify active port bindings between cluster nodes

* Ensure that port `8640` is fully open for communication to maintain valid TCP connections between the servers in the cluster topology.
*   Execute socket listing diagnostic tools on your server to verify exactly which system processes are bound to specific network ports:

    ```bash
    ss -ntlp
    ```
{% endstep %}

{% step %}
### Validate uniform authorization keys

* The security parameter `x-api-key` acts as an authentication credential for the API call.
* This specific key string must match exactly across all participating nodes in the deployment cluster pool.
* Inspect the local configuration file properties to confirm alignment:
  * File Path: `/etc/columnstore/cmapi_server.conf`
  * Section Header: `[Authentication]`
  * Target Variable: `x-api-key=xxxxxxx`
{% endstep %}

{% step %}
### Verify address targeting loops and XML pathing consistency

* Manually execute the `curl` connection block targeting the local loopback address (`127.0.0.1`) directly, and compare the console string behavior against the response from the known designated cluster master instance.
* If a discrepancies occur between these outputs, it indicates that the configuration routing definition file `/etc/columnstore/Columnstore.xml` has gone out of sync across the nodes.
* Remediation Action: Manually copy and redistribute an identical master copy of `Columnstore.xml` to all participating nodes, restart the underlying `cmapi` services, and test execution again.
{% endstep %}

{% step %}
### Reload terminal environment settings

*   If the system displays errors indicating that the baseline wrapper commands are untracked strings, source the configuration alias scripts again:

    ```bash
    source /etc/profile.d/columnstoreAlias.sh
    ```
*   Alternatively, source the fallback shared terminal file path:

    ```bash
    source /usr/share/columnstore/columnstoreAlias
    ```
{% endstep %}
{% endstepper %}

## Status Output Metric Guide

When evaluated successfully, the JSON telemetry stream outputs process metadata maps from each independent host node. Below is a standard sample tracking payload recorded from a operational 3-node cluster topology layout:

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
  "172.31.20.34": {
    "timestamp": "2021-12-21 19:01:50.958150",
    "uptime": 361172,
    "dbrm_mode": "slave",
    "cluster_mode": "readonly",
    "dbroots": [ "2" ],
    "module_id": 2,
    "services": [
      { "name": "workernode", "pid": 10492 },
      { "name": "PrimProc", "pid": 10513 },
      { "name": "ExeMgr", "pid": 10570 },
      { "name": "WriteEngine", "pid": 10588 }
    ]
  },
  "172.31.26.62": {
    "timestamp": "2021-12-21 19:01:51.013945",
    "uptime": 361174,
    "dbrm_mode": "slave",
    "cluster_mode": "readonly",
    "dbroots": [ "3" ],
    "module_id": 3,
    "services": [
      { "name": "workernode", "pid": 10198 },
      { "name": "PrimProc", "pid": 10219 },
      { "name": "ExeMgr", "pid": 10276 },
      { "name": "WriteEngine", "pid": 10291 }
    ]
  },
  "num_nodes": 3
}
```

## Metric Analysis Interpretations

Evaluating specific telemetry variables inside this payload returns diagnostic insights into cluster health:

#### 1. Node Cluster Counts (`num_nodes`)

* Analysis Context: Verify if the calculated `num_nodes` property reflects the expected server headcount. If one or more servers have failed, they will fall completely out of this cluster tracking block.
* Impact: When an active machine goes missing, the system configuration topologies defined inside `Columnstore.xml` are often shuffled as the engine automatically tags the failed target node as an inactive resource.

#### 2. Service Balances and Daemon Presence

* Validation Principle: The engine polls process listings across each node to verify matching binary application names. However, the output block cannot inherently flag whether a process is orphaned or not working as expected internally.
* Master Node Process Allocation: The host node flagged with a `dbrm_mode` of `master` must register exactly 7 active services inside its configuration array. If fewer services appear, components are failing to start or are trapped in a boot-restart loop. Database administrators must examine operating logs or inspect the specific paths `/var/log/mariadb/columnstore/trace/` and `/var/log/mariadb/columnstore/corefiles/` to isolate core dumps or trace data recorded immediately before segmentation faults occurred.
* Replica Node Process Allocation: Replica nodes assigned as a `slave` must register exactly 4 active services inside their tracking block. If missing, inspect node system logs for error sequences detailing why the daemons are failing to start.

#### 3. Master Operational Sockets (`cluster_mode`)

* Validation Principle: Locate the node entry where `dbrm_mode` reads `master`, and evaluate its current `cluster_mode` text string.
* Analysis Context: On a stable deployment, the master node's `cluster_mode` must read `readwrite`. Replica slave engines are permanently locked into `readonly` mode.
* If the primary master drops into a `readonly` status, a critical system error has occurred, and the cluster has placed itself into a restrictive safe mode to prevent modifications until manual intervention repairs the underlying fault. Historically, this safe-mode transition occurs due to:
  * Stuck version rollbacks originating from crashed or aborted query transactions and bulk `cpimport` tasks.
  * Disk Block Resource Manager (`BRM`) metadata structure files failing to receive updates, becoming un-writable, missing completely, or suffering data corruption.
  * Core backend service dependencies failing to initialize—such as `storagemanager` components failing to establish an external network path to connect to Amazon S3 storage buckets.

#### 4. Master Node Resolution Mechanics

* Validation Principle: To isolate and track which component node maintains the role of active master, CMAPI relies on the specialized internal `CEJ` system user profile. The `CEJ` user scans the active database processlist tables to verify the availability of background replication lines. If the database grants, authorization rules, or connection credentials for this `CEJ` user profile are broken, CMAPI cannot resolve the master context, breaking cluster status monitoring completely.
* Analysis Context: Under ideal operational layouts, the assigned `dbroots` values match the corresponding `module_id` tags, indicating that no node failovers have occurred. The master tracking node typically claims initial ownership mapping of `DBroot 1`. If a master node role change occurs, the structural database root execution responsibilities are shuffled across the surviving nodes.
