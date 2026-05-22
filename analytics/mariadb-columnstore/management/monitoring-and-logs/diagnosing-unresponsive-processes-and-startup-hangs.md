# Diagnosing Unresponsive Processes and Startup Hangs

During system startup, configuration procedures (`postConfigure`), or multi-node cluster initialization, the system may occasionally reach a state where processes appear to hang or fail to return control. This page outlines the systematic administrative steps required to diagnose unresponsive states and verify process health across the cluster nodes.

## Initial Assessment for Installation or Process Startup Hangs

If the system reached the stage indicating "Starting system processes" but appears to hang or does not return, use the following checklist to evaluate cluster communication and alignment:

1. Verify Locale Configurations: Check the locale settings on all configured servers and ensure that they are completely identical across every node in the cluster.
2.  Define ColumnStore Aliases: Ensure that the default ColumnStore administrative alias pathing is loaded in your current shell session on Performance Module 1 (`pm1`):

    ```bash
    . /usr/local/mariadb/columnstore/bin/columnstoreAlias
    ```
3.  Inspect Process Status via Admin Console: Execute the system information utility to check the current status of core daemons:

    ```bash
    mcsadmin getsysteminfo
    ```
4. Evaluate Process Monitors: Check if the Process Monitor daemon (`ProcMon`) is reported as `ACTIVE` across all configured servers in the topology. Concurrently, ensure that the Process Manager daemon (`ProcMgr`) is verified as `ACTIVE` on `pm1`.

### Common Root Causes for Process Monitor Unresponsiveness

If `ProcMon` or `ProcMgr` fails to transition to an active state, it is typically driven by one of the following underlying issues:

* External Storage Mount Restrictions: If utilizing external storage configurations, verify that the `/etc/fstab` layout is correctly defined and mounted on the respective performance module.
* Inter-Server Messaging Failures: Communication blocks between servers prevent `ProcMon` and `ProcMgr` from exchanging state messages. Ensure that all server-level network firewalls are temporarily disabled and that `SELinux`constraints are not blocking process sockets.

## Troubleshooting Hangs During `postConfigure` Initialization

The final stage of the `postConfigure` routine entails running the automated `columnstore` service startup script across all nodes. If the installation process hangs or flags an initialization failure during this timeframe, execute the following diagnostic steps:

1.  Initialize the Console Utility Alias: Load the proper command shortcut context:

    ```bash
    . ./usr/local/mariadb/columnstore/bin/aliasColumnstore
    ```
2.  Collect Cluster Statuses: Check system process lists explicitly:

    ```bash
    mcsadmin getsystemi
    ```
3. Verify Target Nodes and Engine Output Logs:
   * Confirm if a firewall on the installation coordinator (`pm1`) is actively restricting outbound commands.
   * If a particular module shows a status of `FAILED`, inspect the local engine system logs on that specific module. All system logging outputs reside in `/var/log/mariadb/columnstore`.
   * Cross-reference findings with the local log reports residing on the coordinator node (`pm1`).

## Troubleshooting Hangs During `startSystem` Invocations

When recovering from maintenance windows using the `startSystem` administrative command, the cluster may fail to achieve full consensus. Follow this structured diagnostic layout to determine the blocking factor:

```bash
mcsadmin getsystemi
```

### Analysis Matrix for `startSystem` Blockers

| Observed IndicatorText                                                 | Root Cause AnalysisText                                                      | Action ItemText                                                                                                    |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `ProcMon` inactive on remote nodes                                     | Firewall restriction or external storage mounting issues.                    | Check remote storage definitions and confirm network firewall rules are flushed.                                   |
| OAM DBRM Components(`ControllerNode` / `WorkerNode`) in `FAILED` state | Disk-to-shared-memory loading failure of the Extent Map or versioning files. | Inspect the structural integrity of the active DBRM files on disk storage.                                         |
| Module status listed explicitly as `FAILED`                            | Process crash, configuration mismatch, or local binary initialization error. | Check logs located under `/var/log/mariadb/columnstore`on both the affected module and the local `pm1`coordinator. |

## Operational Logs to Monitor During a Hang

To inspect active execution blocks, check the system logs in real time:

* `info.log`: Captures high-level service transitions and actions. Review this log during cluster stops and starts to isolate which module or process failed to initialize.
* `err.log` / `crit.log`: Captures critical software constraints and failure events logged by independent ColumnStore processes.
