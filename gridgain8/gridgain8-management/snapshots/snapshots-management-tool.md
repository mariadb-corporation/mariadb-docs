---
description: >-
  Reference for the GridGain snapshot-utility command-line tool — its commands,
  connection/output/SSL parameters, exit codes, command arguments, and error codes.
---

# Snapshots Management Tool

GridGain Ultimate Edition includes a command line tool that simplifies snapshot creation, recovery, and the management of related tasks.

The script that starts the tool is called `snapshot-utility` and is located in the `{GRIDGAIN_HOME}/bin/` folder. The script is available for Unix-based systems (`snapshot-utility.sh`) and for Windows (`snapshot-utility.bat`).

You can define the `snapshot-utility.sh|bat` log directory via an environment variable:

{% tabs %}
{% tab title="Linux/Unix" %}
```shell
$ SNAP_UTIL_LOG_CONFIG=-Dlog4j.configurationFile=<PATH_TO_CONFIG>  ./snapshot-utility.sh
```
{% endtab %}
{% tab title="Windows" %}
```shell
$ SNAP_UTIL_LOG_CONFIG=-Dlog4j.configurationFile=<PATH_TO_CONFIG>  ./snapshot-utility.bat
```
{% endtab %}
{% endtabs %}

The tool supports the following commands:

- HELP
- LIST
- INFO
- SNAPSHOT
- RESTORE
- CHECK
- DELETE
- MOVE
- STATUS
- CANCEL
- SCHEDULE
- COPY
- METADATA
- ANALYZE
- CLEANUP_RESTARTING_CACHES
- SECURITY_LEVEL

To call a specific command, use the following format:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh [command] <command arguments> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat <command> <args> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

- `<command arguments>` – command-specific parameters.
- <ssl parameters> - the parameters that are used to configure SSL.
- `<connection parameters>` – connection parameters the tool uses to connect to a cluster node. These parameters are required for the commands that are executed on the cluster's nodes (`list`, `info`, `snapshot`, `restore`, `check`, `delete`, `move`, `status`, `cancel`, `schedule`). If the connection options are not given, the tool tries to connect to a local node with default parameters.
- `<output parameters>` – the parameters that specify the output format and output file.

## Parameters

### Connection Parameters

Connection parameters allow you to specify the node on which commands will be executed. The following command require connection parameters: `list`, `info`, `snapshot`, `restore`, `check`, `delete`, `move`, `status`, `cancel`, `schedule`.

| Parameter | Description | Default |
|---|---|---|
| `-host=IP_OR_HOST` | The IP address or the host name of the node where the command will be executed. The tool connects to this node in order to issue snapshot related requests. | `127.0.0.1` |
| `-port=PORT` | The port on the cluster's node the snapshot tool will connect to. The port number is defined by org.apache.ignite.configuration.ConnectorConfiguration and defaults to 11211. | `11211` |
| `-ping_interval={time in ms}` | The time interval between heartbeats that are sent from the tool to the cluster's node, in milliseconds. | `5000` |
| `-ping_timeout={time in ms}` | Node response timeout. | `30000` |
| `-user=name` | The user name for connecting to a cluster that requires authentication. | - |
| `-password=password` | The password for connecting to a cluster that requires authentication. | - |

### Output Parameters

All commands support the following output parameters.

| Parameter | Description | Default |
|---|---|---|
| `-output=FILE_NAME` | The file to which the tool will save the output or error code. | snapshot-utility.out |
| `-format=text\|json` | The output format: text or JSON. | text |
| `-compression_level=N` | The compression level for snapshot files. The value depends on the codec type [min, max, default]: ZIP [1, 9, 1], ZSTD [1, 22, 1], LZ4 [0, 17, 0], or SNAPPY [0, 0, 0]. | Codec-dependent |

### SSL Parameters

SSL parameters allow you to configure how your SSL configuration

| Parameter | Description |
|---|---|
| -key_alias=alias | Alias for JKS key for working with SFTP server. |
| -ssl_enabled | Enables connection via SSL |
| -ssl_protocol=SSL_PROTOCOL[, SSL_PROTOCOL_2, ...] | SSL protocols, by default TLS will be used. |
| -ssl_algorithm=SSL_ALGORITHM | SSL algorithm, by default SunX509 will be used. |
| -ssl_key_store_type=SSL_KEY_STORE_TYPE | Type of key store, by default JKS will be used. |
| -ssl_key_store_path=PATH_TO_KEY_STORE | Path to key store. |
| -ssl_key_store_password=PASSWORD | Password for key store. |
| -ssl_truststore_type=SSL_TRUST_STORE_TYPE | Type of trust store, by default JKS will be used. |
| -ssl_truststore_path=PATH_TO_TRUST_STORE | Path to trust store. |
| -ssl_truststore_password=PASSWORD | Password for trust store. |
| -ssl_cipher_suites=SSL_CIPHER_1[, SSL_CIPHER_2, ...] | List of cipher suites. |

### Exit Codes

The snapshot tool returns a code as a result of an operation performed on the cluster. These codes are listed below:

| Exit Code | Description |
|---|---|
| 0 | Successful execution. |
| 1 | Unexpected error. |
| 2 | Unknown command. |
| 3 | Invalid arguments. |
| 4 | Connection failed. |
| 5 | Command failed with known error code. |
| 6 | Command executed successfully, but the tool failed to write the result to the output file. |
| 7 | Command failed and the tool failed to write error code to the output file. |

## HELP

The command prints out the list of all commands supported by the tool.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh help
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat help
```
{% endtab %}
{% endtabs %}

To get more details about a specific command, pass the command name as an argument to the `help` command.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh help snapshot
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat help snapshot
```
{% endtab %}
{% endtabs %}

## LIST

This command lists all locally stored snapshots.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh list [-src=path1,...,pathN] [-verbose] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat list [-src=path1[,path2,...,pathN]] [-verbose] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -src=path1[,path2,...,pathN] | A list of folders to search for snapshot files. The tool will search for snapshots in the default snapshot folder and the folders given in this argument. |
| -verbose | The output will additionally contain the names of the caches included in the snapshot. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 2000 | Failed to execute the `list` command. | This error means that something unexpected happened. Check cluster logs for errors. |
| 2110 | Unknown or unsupported arguments. | Check if the arguments are correct. |
| 2120 | Invalid argument value. | Check if the argument values are correct. |
| 2200 | Snapshots tool failed to authenticate in the cluster. | Make sure that the username and password are correct. |
| 2210 | Snapshots tool failed to authorize in the cluster. | Make sure that the username and password are correct. |
| 2220 | Snapshot utility failed to get secure console for password input. | Make sure the console has elevated permissions. |
| 2300 | Snapshots tool failed to connect to the cluster. | Check the following:<br>- the node defined by `-host` and `-port` arguments is reachable.<br>- the port number defined by `-port` is not blocked by firewalls.<br>- check the cluster logs for further information. |
| 2400 | Snapshots are not configured. The command can't be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 2410 | Cluster is not active, the command cannot be executed. | Activate the cluster. |
| 2730 | Storage device is full. | Empty enough space on the storage device. |
| 2760 | Invalid parallelism level. | Use a positive parallelism level. |
| 2800 | Command executed successfully, but the snapshot tool failed to write result to the output file. | Check the output file name and permissions. |
| 2810 | Command failed and the snapshot tool failed to write error code to the output file. | Check the output file name and permissions. |
| 2910 | Snapshot utility failed to find directory. | Specify a valid directory. |

## INFO

This command prints detailed information about a specific snapshot.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh info -id=SNAPSHOT_ID <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat info -id=SNAPSHOT_ID <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -id=SNAPSHOT_ID | The ID of the snapshot. Use the list command to obtain snapshot IDs and other details. |
| -src=path1,...,pathN | A list of folders to search for snapshot files. The tool will search for snapshots in the default snapshot folder and the folders given in this argument. |
| -verbose | The output will additionally contain the names of the caches included in the snapshot. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 3000 | Failed to execute the `info` command. | This error means that something unexpected happened. Check cluster logs for errors. |
| 3110 | Unknown or unsupported arguments. | Check that the arguments are correct. |
| 3120 | An invalid argument value. | Check that the arguments values are correct. |
| 3200 | Snapshots tool failed to authenticate in the cluster. | Check that the username and password are correct. |
| 3210 | Snapshots tool failed to authorize in the cluster. | Check that the username and password are correct. |
| 3220 | Snapshot utility failed to get secure console for password input. | Make sure the console has elevated permissions. |
| 3300 | Snapshots tool failed to connect to the cluster. | Check the following:<br>- the node defined by `-host` and `-port` arguments is reachable.<br>- the port number defined by `-port` is not blocked by firewalls.<br>- check the cluster logs for further information. |
| 3400 | Snapshots are not configured. The command can't be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 3410 | Cluster is not active, the command cannot be executed. | Activate the cluster. |
| 3500 | A snapshot with the specified ID does not exist. | Check that the snapshot ID is correct. Use the `list` command to get the ID of the required snapshot. |
| 3730 | Storage device is full. | Empty enough space on the storage device. |
| 3760 | Invalid parallelism level. | Use a positive parallelism level. |
| 3800 | Command executed successfully, but the snapshot tool failed to write result to the output file. | Check the output file name and permissions. |
| 3810 | Command failed and the snapshot tool failed to write error code to the output file. | Check the output file name and permissions. |

## SNAPSHOT

The command creates a snapshot of the cluster's data. You can specify a list of caches you want to include in the snapshots.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh snapshot [-type=full|inc] [-caches=cache1,cache2…] [-dest=EXTERNAL_FOLDER] [-verbose] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat snapshot  [-type=full|inc] [-caches=cache1,cache2,...,cacheN] [-dest=EXTERNAL_FOLDER] [-verbose] [-needexchange] [-parallelism=4] [-archive=NONE|ZIP] [-compression_level=5] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

After successful execution, the command will output the snapshot details to console and the file specified by the `-output` argument.

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -type=full\|inc | The type of snapshot: full or incremental. If this argument is not specified, an incremental snapshot is created. |
| -caches={cache1,…,cacheN,group1,...,groupK} | Include specific caches or cache groups in the snapshots. If this argument is specified, only the given caches are included in the snapshot. If the argument is not specified, the snapshot will include all caches.<br><br>If a cache is included in a cache group, then the entire cache group will be included in the snapshot.<br><br>When Point-in-Time Recovery is enabled, the command will return 4000 error code when executed with this parameter. With PITR, you can only create snapshot with all the caches stored in the cluster. |
| -excluded_caches={cache1,...,cacheN,group1,...groupK} | List of cache or group names excluded from processing. |
| -dest=EXTERNAL_FOLDER | The folder where the snapshot will be saved. If not specified, the default snapshot folder will be used. |
| -noprogress | Do not print progress bar. |
| -progress=DELAY | Delay in seconds for progress bar update, default is 5 seconds. |
| -verbose | The output will additionally contain the names of the caches included in the snapshot. |
| -needexchange | If this parameter is specified, the cluster waits for all ongoing cache updates to mark all data to be included in the snapshot and this step requires partition map exchange (PME). For detailed information about PME, see [Data Partitioning](../../architecture/data-modeling/data-partitioning.md). By default, this flag is not specified and creating a snapshot does not require PME.<br><br>When point-in-time recovery is enabled, the PME is still required to create snapshots, even though this parameter is not specified. |
| -parallelism=N | Determines parallel execution (threads) of snapshot operation, 1 to N. |
| -archive=NONE\|ZIP\|ZSTD\|LZ4\|SNAPPY | This argument enable compression for snapshot files. |
| -compression_level=N | This argument sets compression level for snapshot files, value dependent on codec type[min, max, default]: ZIP[1, 9, 1], ZSTD[1, 22, 1], LZ4[0, 17, 0], SNAPPY[0, 0, 0] |
| -write_throttling=N | Enables write throttling. Snapshots write speed will be limited when it reaches N bytes per second. This parameter is applied per node.<br><br>Only non-negative values are supported. Default value is 0 - no throttling. |
| -encryption_key=MASTER_KEY_NAME | This argument specifies a master key that will be used for snapshot encryption. If you want to use a key different from the [TDE master key](../../security/tde.md), you need to add that key to the JKS file. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 4000 | Failed to execute the `snapshot` command. | This error means that something unexpected happened. Check cluster logs for errors. |
| 4110 | Unknown or unsupported arguments. | Check that the arguments are correct. |
| 4120 | Invalid argument. | Check that the arguments values are correct. |
| 4200 | Failed to authenticate in the cluster. | Check that the username and password are correct. |
| 4210 | Failed to authorize in the cluster. | Check that the username and password are correct. |
| 4220 | Snapshot utility failed to get secure console for password input. | Make sure the console has elevated permissions. |
| 4300 | Failed to connect to the cluster. | Check the following:<br>- the node defined by the `-host` and `-port` arguments is reachable.<br>- the port number defined by `-port` is not blocked by firewalls.<br>- check cluster logs for further information. |
| 4400 | Snapshots are not configured. The command can't be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 4410 | Cluster is not active, the command cannot be executed. | Activate the cluster. |
| 4520 | An attempt to start snapshot creation while the previous snapshot creation operation is still in progress. | Wait for the previous snapshot to finish. Use the `status` command to monitor snapshot operations. |
| 4530 | Cannot create an incremental snapshot because the last full snapshot was not found. | Create a full snapshot first. |
| 4600 | Failed to find a cache with the specified name. | Check that the caches specified in the `-caches` argument exist in the cluster. |
| 4710 | Failed to create a snapshot in the destination folder. | Check if the destination folder has proper permissions. |
| 4730 | Storage device is full. | Empty enough space on the storage device. |
| 4760 | Invalid parallelism level. | Use a positive parallelism level. |
| 4800 | Command executed successfully, but the snapshot tool failed to write result to the output file. | Check the output file name and permissions. |
| 4810 | Command failed, and the snapshot tool failed to write error code to the output file. | Check the output file name and permissions. |

## RESTORE

The command restores the cluster data to the state preserved in a specific snapshot or to a given past point in time (if [Point-in-Time Recovery](point-in-time-recovery.md) is enabled).

To restore a specific snapshot:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh restore -id=snapshot_id [-nocheck] [-src=path1,...,pathN] [-config=config.xml] [-force] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat restore -id=snapshot_id [-nocheck] [-caches=cache1,cache2…] [-nocheck] [-src=path1[,path2,...,pathN]] [-config=config.xml] [-force] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

To restore to a point in time:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh restore -to=yyyy-MM-dd-HH:mm:ss.SSS [-caches=cache1,cache2,...] [-nocheck] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat restore -to=yyyy-MM-dd-HH:mm:ss.SSS [-caches=cache1,cache2,...] [-nocheck] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -id=SNAPSHOT_ID | The ID of the snapshot to be restored. Use the `list` command to obtain snapshot IDs and other details. |
| -to=yyyy-MM-dd-HH:mm:ss.SSS | The time you want to recover to. For this argument to work, point-in-time recovery must be enabled. See [Point-in-Time Recovery](point-in-time-recovery.md) for details. |
| -caches=[cache1,…,cacheN,group1,…,groupK] | The list of caches and cache groups to be restored from the snapshot. The data of the specified caches in the running cluster will be replaced with the content from the snapshot.<br><br>If this argument is not specified, all caches will be restored.<br><br>If a cache is included in a cache group, the entire group will be restored. This argument has no effect when recovering to a point of time. When using PITR, all caches will be restored. |
| -nocheck | Disables snapshot verification. If the argument is not specified, the snapshot will be checked for consistency before being restored (default behavior). |
| -src=path1,...,pathN | A list of folders to look for snapshot files. The tool will search for snapshots in the default snapshot folder and the folders given in this argument. If the argument is not specified, the default snapshot folder is used. |
| -config=config.xml | The file containing cache configurations to be used instead of the configuration stored in the snapshot metadata.<br><br>Note: Only the cache configuration from the specified `config` file will be used; the remaining information in this file will be ignored. The cache configuration from the `config` file will completely replace the pre-restore configuration (rather than being appended to it). The caches not mentioned in the `config` file will be restored as they would have been without the -config parameter. |
| -archive=NONE/ZIP/ZSTD/LZ4/SNAPPY | The compression codec to use for the snapshot. Default is NONE, meaning no compression. |
| -compression_level=1..9 | This argument sets compression level for snapshot files, 1 is the fastest. Default is 1. |
| -force | If you add new caches to the cache group after a snapshot was created, the tool will return an error when restoring that group. Specify this option to replace the entire group, deleting the new caches from the cluster. |
| -comment=TEXT | Add a custom message to the history record of this operation. |
| -progress=DELAY | Delay (sec) for progress bar update, default is 5 sec. |
| -parallelism=N | Determines parallel execution (threads) of snapshot operation, 1 to N. |
| -excluded_caches=[cache1,…,cacheN] | The list of caches or cache groups to not restore during the operation. Overrides `-caches`. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 5000 | Failed to execute the `restore` command. | This error means that something unexpected happened. Check cluster logs for errors. |
| 5110 | Unknown or unsupported arguments. | Check that the arguments are correct. |
| 5120 | An invalid argument. | Check that the arguments values are correct. |
| 5200 | Failed to authenticate in the cluster. | Check that the username and password are correct. |
| 5210 | Failed to authorize in the cluster. | Check that the username and password are correct. |
| 5220 | Snapshot utility failed to get secure console for password input. | Make sure the console has elevated permissions. |
| 5300 | Failed to connect to the cluster. | Check the following:<br>- the node defined by the `-host` and `-port` arguments is reachable.<br>- the port number defined by the `-port` argument is not blocked by firewalls.<br>- check the cluster logs for further information. |
| 5400 | Snapshots are not configured. The command can't be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 5410 | Cluster is not active, the command cannot be executed. | Activate the cluster. |
| 5500 | A snapshot with the specified ID doesn't exist. | Check that the snapshot ID is correct. Use the `list` command to get the ID of the required snapshot. |
| 5510 | The snapshot is corrupt. | Replace corrupt snapshot files with correct ones. |
| 5600 | Failed to find a cache with the specified name. | Check if -caches argument is specified correctly. |
| 5610 | Failed to read the cache configuration file. | Check if the file has correct permissions. |
| 5700 | The number of caches in the cache groups to be restored has changed, i.e. you have added new caches to the cache groups after the snapshot was taken. | Use the `-force` argument to restore cache groups from the snapshot, deleting the caches that have been added following snapshot creation. |
| 5730 | Storage device is full. | Empty enough space on the storage device. |
| 5760 | Invalid parallelism level. | Use a positive parallelism level. |
| 5800 | Command executed successfully, but the snapshot tool failed to write result to output file. | Check the output file name and permissions. |
| 5810 | Command failed and the snapshot tool failed to write error code to output file. | Check the output file name and permissions. |

## CHECK

This command checks if the specified snapshot is not broken and can be restored on this cluster.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh check -id=[snapshot_id] [-src=path1,...,pathN] [-caches=cache1,cache2,...] [-force] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat check -id=[snapshot_id] [-src=path1,...,pathN] [-caches=cache1,cache2,...] [-force] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -id=SNAPSHOT_ID | The ID of the snapshot to be checked. Use the list command to obtain snapshot IDs and other details. |
| -src=path1,...,pathN | A list of folders to search for snapshot files. The tool will search for snapshots in the default snapshot folder and the folders given in this argument. |
| -caches=[cache1,…,cacheN,group1,…,groupK] | A list of caches and cache groups to be checked. |
| -force | For each cache specified in the `-caches` argument, the command will check the entire cache group to which that cache belongs. |
| -progress=DELAY | Delay in seconds for progress bar update, default is 5 sec. |
| -parallelism=N | Determines parallel execution (threads) of snapshot operation, 1 to N. |
| -excluded_caches=[cache1,...,cacheN] | The list of caches or cache groups to not check. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 6000 | Failed to execute the `check` command. | This error means that something unexpected happened. Check cluster logs for errors. |
| 6110 | Unknown or unsupported arguments. | Check that the arguments are correct. |
| 6120 | Invalid argument. | Check that the arguments values are correct. |
| 6200 | Failed to authenticate in the cluster. | Check that the username and password are correct. |
| 6210 | Failed to authorize in the cluster. | Check that the username and password are correct. |
| 6300 | Failed to connect to the cluster. | Check the following:<br>- the node defined by the `-host` and `-port` arguments is reachable.<br>- the port number defined by the `-port` argument is not blocked by firewalls.<br>- check GridGain cluster logs for further information. |
| 6400 | Snapshots are not configured. The command can't be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 6410 | Cluster is not active, command cannot be executed. | Activate the cluster. |
| 6500 | The snapshot with the specified ID doesn't exist. | Check that the snapshot ID is correct. Use the `list` command to get the ID of the required snapshot. |
| 6510 | The snapshot is corrupt. | Check log files for errors. Check if you have had any hardware problems. Restore broken or missing files from a backup copy. |
| 6600 | The cache with the specified name is not found. | Check value of `-caches` argument. |
| 6700 | The number of caches in the cache groups to be restored has changed, i.e. you have added new caches to the cache groups after the snapshot was taken. | Use the `-force` argument to restore cache groups from the snapshot, deleting the caches that have been added following snapshot creation. |
| 6730 | Storage device is full. | Empty enough space on the storage device. |
| 6760 | Invalid parallelism level. | Use a positive parallelism level. |
| 6800 | Command executed successfully, but snapshot tool failed to write result to output file. | Check output file name and permissions. |
| 6810 | Command failed and snapshot tool failed to write error code to output file. | Check output file name and permissions. |

## DELETE

This command deletes a snapshot.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh delete -id=snapshot_id [-force] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat delete -id=snapshot_id [-force] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -id=SNAPSHOT_ID | The ID of the snapshot to be deleted. Use the `list` command to obtain snapshot IDs and other details. |
| -force | Note: This argument has been deprecated. It might be still valid in older versions of GridGain.<br><br>If this option is not specified and if there are dependent snapshots for the given snapshot, the tool will return an error. A dependent snapshot is a snapshot that requires the given snapshots for successful restoration. For example, an incremental snapshot depends on the last full snapshot and all incremental snapshots taken in-between.<br><br>Use this option to delete the specified snapshot and all dependent snapshots. |
| -chain=SINGLE\|FROM | This parameter defines how to work with snapshot chains, for example FULL-INC-INC-INC snapshot chain. Possible options:<br>- SINGLE - manipulate only with the defined snapshot (default);<br>- FROM - manipulate with snapshot chain (FULL-INC-INC-INC...) from the defined snapshot to the last one; |
| -noprogress | Do not print progress bar. |
| -comment=TEXT | Add a custom message to the history record of this operation. |

### Repeating a Failed Deletion

Deleting a snapshot removes parts of the snapshot on every node of the cluster that holds them. If the command
fails, run the same command again.
Deletion is repeatable: it continues from the state the previous attempt left behind.

A part of a snapshot that a failed deletion left behind is marked as incomplete. Such a part is no longer a snapshot.
It is not shown by the `list` command, and it can be neither restored from nor checked. Incomplete parts are removed
automatically:

* every node removes its own incomplete parts shortly after the node starts;
* every subsequent deletion, including a scheduled one, removes them as well.

{% hint style="info" %}
GridGain marks incomplete parts starting from 8.9.37. Previous releases did not mark incomplete parts. A part left
behind by a deletion that was interrupted under one of those versions is not shown by the `list` command and cannot be
restored from. Remove such a part from the snapshot folder manually.
{% endhint %}

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 7000 | Failed to execute the `delete` command. | Check cluster logs for errors. This error means that something unexpected happened. |
| 7110 | Unknown or unsupported arguments. | Check that the arguments are correct. |
| 7120 | Invalid argument. | Check that the arguments values are correct. |
| 7200 | Failed to authenticate in the cluster. | Check that username and password are correct. |
| 7210 | Failed to authorize in the cluster. | Check that the username and password are correct. |
| 7220 | Snapshot utility failed to get secure console for password input. | Make sure the console has elevated permissions. |
| 7300 | Failed to connect to the cluster. | Check the following:<br>- the node defined by the -host and -port arguments is reachable.<br>- the port number defined by the -port argument is not blocked by firewalls.<br>- check the cluster logs for further information. |
| 7400 | Snapshots are not configured. The command can't be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 7410 | Cluster is not active, the command cannot be executed. | Activate the cluster. |
| 7500 | The snapshot with the specified ID doesn't exist. | Check that the snapshot ID is correct. Use the `list` command to get the ID of the required snapshot. |
| 7520 | Concurrent snapshot operations are not allowed cluster-wide. | Wait for the previous snapshot operation to finish. Use the `status` command to monitor snapshot operations. |
| 7720 | Failed to delete the specified snapshot because the file operations were denied. | Check if the snapshot files exist and have correct permissions. |
| 7730 | Storage device is full. | Empty enough space on the storage device. |
| 7750 | Snapshot has dependent snapshots and could not be removed in default mode. Use '-chain=SINGLE\|FROM' to define how to work with snapshot and his dependent snapshots. |  |
| 7760 | Invalid parallelism level. | Use a positive parallelism level. |
| 7800 | Command executed successfully, but the snapshot tool failed to write result to the output file. | Check the output file name and permissions. |
| 7810 | Command failed and the snapshot tool failed to write error code to the output file. | Check the output file name and permissions. |

## MOVE

This command moves a specific node's snapshot and all related files from the node-specific default folder to a specified folder. Consolidation of all node snapshots in a single location helps you restore the entire cluster in another environment. 

The default snapshot folder is `IGNITE_HOME\work\snapshot` and can be changed in the snapshot configuration. See [Full and Incremental Snapshots](full-incremental-snapshots.md) for details.

If you create a snapshot using the snapshot management tool with the `-dest` argument specified, you won't be able to move the snapshot using the tool. However, you can move it manually by moving the snapshot files on the file system.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh move -id=snapshot_id -dest=EXTERNAL_FOLDER [-force] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat move -id=snapshot_id -dest=EXTERNAL_FOLDER [-force] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -id=SNAPSHOT_ID | The ID of the snapshot to move. Use the `list` command to obtain snapshot IDs and other details. |
| -dest=EXTERNAL_FOLDER | The name of the folder where the snapshot will be moved. |
| -force | If this option is not specified and for the given snapshot there are dependent snapshots, the tool will return an error. A dependent snapshot is a snapshot that requires the given snapshots for successful restoration. For example, an incremental snapshot depends on the last full snapshot and all incremental snapshots taken in-between.<br><br>Use this option to move the specified snapshot and all dependent snapshots. |
| -noprogress | Do not print progress bar. |
| -progress=DELAY | Delay in seconds for progress bar update, default is 5 sec. |
| -skip_wal | Move snapshot without dependent WAL. |
| -chain=SINGLE\|FROM | This parameter defines how to work with snapshot chains, for example FULL-INC-INC-INC snapshot chain. Possible options:<br>- SINGLE - manipulate only with the defined snapshot (default);<br>- FROM - manipulate with snapshot chain (FULL-INC-INC-INC...) from the defined snasphot to the last one; |
| -single_copy | Will synchronize node to copy partition files exactly once. |
| -comment=COMMENT | Add a custom message to the history record of this operation. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 8000 | Failed to execute the `move` command. | This error means that something unexpected happened. Check cluster logs for errors. |
| 8110 | Unknown or unsupported arguments. | Check that the arguments are correct. |
| 8120 | An invalid argument value. | Check that the argument values are correct. |
| 8200 | Failed to authenticate in the cluster. | Check that the username and password are correct. |
| 8210 | Failed to authorize in the cluster. | Check that the username and password are correct. |
| 8300 | Failed to connect to the cluster. | Check the following:<br>- the node defined by the `-host` and `-port` arguments is reachable.<br>- the port number defined by the `-port` argument is not blocked by firewalls.<br>- check GridGain cluster logs for further information. |
| 8400 | Snapshots are not configured. The command can't be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 8410 | Cluster is not active, command cannot be executed. | Activate the cluster. |
| 8500 | The snapshot with the specified ID doesn't exist. | Check that the snapshot ID is correct. Use the `list` command to get the ID of the required snapshot. |
| 8700 | Failed to move the specified snapshot because there are dependent snapshots. See the description of the `-force` option. | Use the `-force` argument to forcibly move the snapshot and the dependent snapshots. |
| 8710 | Failed to move snapshot to the destination folder. | Check if the destination folder has correct permissions. |
| 8720 | Failed to delete the specified snapshot. File operations are denied. | Check if the snapshot files have correct permissions. |
| 8730 | Storage device is full. | Empty enough space on the storage device. |
| 8760 | Invalid parallelism level. | Use a positive parallelism level. |
| 8800 | Command executed successfully, but the snapshot tool failed to write result to the output file. | Check the output file name and permissions. |
| 8810 | Command failed and the snapshot tool failed to write error code to the output file. | Check the output file name and permissions. |

## STATUS

This command will print a list of the currently running snapshot operations, such as `snapshot`, `restore`, `delete`, or `move`.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh status <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat status <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports ssl parameters, connection parameters and output parameters.

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 9000 | Failed to execute the `status` command. | This error means that something unexpected happened. Check cluster logs for errors. |
| 9110 | Unknown or unsupported arguments. | Check that the arguments are correct. |
| 9120 | An invalid argument value. | Check that the arguments values are correct. |
| 9200 | Failed to authenticate in the cluster. | Check that the username and password are correct. |
| 9210 | Failed to authorize in the cluster. | Check that the username and password are correct. |
| 9300 | Failed to connect to the cluster. | Check the following:<br>- the node defined by the `-host` and `-port` arguments is reachable.<br>- the port number defined by the `-port` argument is not blocked by firewalls.<br>- check the cluster logs for further information. |
| 9400 | Snapshots are not configured. The command can't be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 9410 | Cluster is not active, the command cannot be executed. | Activate the cluster. |
| 9730 | Storage device is full. | Empty enough space on the storage device. |
| 9760 | Invalid parallelism level. | Use a positive parallelism level. |
| 9800 | Command executed successfully, but the snapshot tool failed to write result to the output file. | Check the output file name and permissions. |
| 9810 | Command failed and the snapshot tool failed to write error code to the output file. | Check the output file name and permissions. |

## CANCEL

This command cancels a specified ongoing operation.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh cancel -id=operationId [-force] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat cancel -id=operationId [-force] [-comment=text] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -id=OPERATION_ID | The ID of the operation to be cancelled. |
| -force | Some operations cannot be cancelled during execution, for example, because of an ongoing file system operation. In such cases, if this argument is not specified, the command will return an error. If the argument is specified, the command will forcibly interrupt any operations, possibly leaving behind inconsistent or corrupt files. |
| -comment=TEXT | Add a custom message to the history record of this operation. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 11000 | Failed to execute the `cancel` command. | This error means that something unexpected happened. Check cluster logs for errors. |
| 11110 | Unknown or unsupported arguments. | Check that the arguments are correct. |
| 11120 | Invalid argument value. | Check that the arguments values are correct. |
| 11200 | Failed to authenticate in the cluster. | Check that the username and password are correct. |
| 11210 | Failed to authorize in the cluster. | Check that the username and password are correct. |
| 11220 | Snapshot utility failed to get secure console for password input. | Make sure the console has elevated permissions. |
| 11300 | Failed to connect to the cluster. | Check the following:<br>- the node defined by the -host and -port arguments is reachable.<br>- the port number defined by the -port argument is not blocked by firewalls.<br>- check GridGain cluster logs for further information. |
| 11400 | The persistent store is not configured. The command can't be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 11410 | Cluster is not active, the command cannot be executed. | Activate the cluster. |
| 11730 | Storage device is full. | Empty enough space on the storage device. |
| 11760 | Invalid parallelism level. | Use a positive parallelism level. |
| 11800 | Command executed successfully, but the snapshot tool failed to write result to the output file. | Check the output file name and permissions. |
| 11810 | Command failed and the snapshot tool failed to write error code to the output file. | Check the output file name and permissions. |
| 11960 | The operation for specified ID not found. | Make sure to specify the correct operation ID. |

## SCHEDULE

This command allows you to create schedules of snapshot operations. Each schedule has a name and can be enabled or disabled as necessary.

For this command to work, the Ignite-schedule module must be installed on the node where the command is to be executed.

List all registered schedules:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh schedule -list [-verbose] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat schedule -list [-verbose] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

Create a snapshot creation schedule:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh schedule -command=create -name=CREATE_SCHEDULE_NAME  [-caches=cache1,cache2,…] -full_frequency=FREQUENCY [-incremental_frequency=FREQUENCY] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat schedule -command=create -name=CREATE_SCHEDULE_NAME  [-caches=cache1,cache2,…] -full_frequency=FREQUENCY [-incremental_frequency=FREQUENCY] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

Create a snapshot deletion schedule:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh schedule -command=delete -name=SCHEDULE_NAME [-ttl=TTL] [-frequency=hourly] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat schedule -command=delete -name=SCHEDULE_NAME [-ttl=TTL] [-frequency=hourly] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh schedule -command=delete -name=SCHEDULE_NAME [-for-oldest=NUMBER_OF_SNAPSHOTS] [-frequency=hourly] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat schedule -command=delete -name=SCHEDULE_NAME [-for-oldest=NUMBER_OF_SNAPSHOTS] [-frequency=hourly] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

Create a schedule for the `move` operation:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh schedule -command=move -name=MOVE_SCHEDULE_NAME -dest=DEST_FOLDER [-ttl=TTL] [-frequency=hourly] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat schedule -command=move -name=MOVE_SCHEDULE_NAME -dest=DEST_FOLDER [-ttl=TTL] [-frequency=hourly] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

Create a schedule for the `check` operation:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh schedule -command=check -name=CHECK_SCHEDULE_NAME [-for-latest=NUMBER_OF_SNAPSHOTS] [-frequency=hourly] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat schedule -command=check -name=CHECK_SCHEDULE_NAME [-for-latest=NUMBER_OF_SNAPSHOTS] [-frequency=hourly] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

Create a task for the `check` operation that should be executed after the corresponding `create` operation:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh schedule -command=check -name=CHECK_TASK_NAME [-for-latest=NUMBER_OF_SNAPSHOTS] [-exec-after=CREATE_SCHEDULE_NAME] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat schedule -command=check -name=CHECK_TASK_NAME [-for-latest=NUMBER_OF_SNAPSHOTS] [-exec-after=CREATE_SCHEDULE_NAME] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

Enable a schedule:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh  schedule -name=SCHEDULE_NAME -enable <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat  schedule -name=SCHEDULE_NAME -enable <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

Disable a schedule:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh schedule -name=SCHEDULE_NAME -disable <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat schedule -name=SCHEDULE_NAME -disable <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

Delete a schedule:

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh schedule -name=SCHEDULE_NAME -delete <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat schedule -name=SCHEDULE_NAME -delete <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -list | Show all registered schedules. |
| -verbose | Enable verbose mode. |
| -name=SCHEDULE_NAME | Specify a schedule name. |
| -command=COMMAND | Specify the command to be scheduled ("create", "delete", "check" or "move").<br>- The `create` command requires either the `-full_frequency` or `-incremental_frequency` argument to be set.<br>- The `move` and `delete` commands require the `-frequency` argument to be set. |
| -caches=cache1,…,cacheN,group1,…,groupK | Specify the names of the caches to be included in the snapshot. |
| -full_frequency=FREQUENCY | Set a full snapshot creation frequency. |
| -incremental_frequency=FREQUENCY | Set an incremental snapshot creation frequency. |
| -frequency=FREQUENCY | Set the frequency for the delete, move, or check command. The default frequency is set to the rate of once every one hour.<br><br>FREQUENCY could be one of the following:<br>- "15mins" - execute every 15 minutes<br>- "30mins" - execute every 30 minutes<br>- "hourly" - execute every hour<br>- "daily" - execute every day at 00:00<br>- "weekly" - execute every Sunday at 00:00<br>- any valid CRON expression, for example: `0 0 * * *` |
| -exec-after=SCHEDULE_NAME | Execute the task after a successful completion of the SCHEDULE_NAME schedule. If you specify this argument, `-frequency` is not needed. It's possible to build a chain of multiple tasks, executing one after another, e.g. create snapshot, then check, then move (see also `-for-latest` and `-for-oldest` options). |
| -ttl=TTL | The time period for the maintenance of snapshots before they could be moved or deleted. Only one of parameters `-ttl`, `-for-oldest` or `-for-latest` should be specified. The default value is TTL=3 days.<br><br>TTL could be one of the following:<br>- NNd - NN days, for example: 3d<br>- NNh - NN hours, for example: 12h<br>- NNm - NN minutes, for example: 90m<br>- NN - NN milliseconds, for example: 100000 |
| -for-oldest=NUMBER_OF_SNAPSHOTS | Select NUMBER_OF_SNAPSHOTS oldest snapshots to check, move or delete. Only one of parameters `-ttl`, `-for-oldest` or `-for-latest` should be specified. The default value is TTL=3 days. |
| -for-latest=NUMBER_OF_SNAPSHOTS | Select NUMBER_OF_SNAPSHOTS latest snapshots to check, move or delete. Only one of parameters `-ttl`, `-for-oldest` or `-for-latest` should be specified. The default value is TTL=3 days. |
| -dest=DESTINATION_FOLDER | The snapshot destination folder. |
| -enable | Enable a schedule. |
| -disable | Disable a schedule. |
| -delete | Delete a schedule. If a specified schedule was created with `-exec-after` parameter, it is removed from the task chain. If it is the first task in the chain, all tasks in chain are deleted cascadely. |
| -keep | Only supported for delete subcommand. If specified, a specified number of snapshots are kept after deletion. Default value is 1. |
| -archive=NONE\|ZIP\|ZSTD\|LZ4\|SNAPPY | This argument enable compression for snapshot files. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 12000 | Failed to execute the `schedule` command. | This error means that something unexpected happened. Check cluster logs for errors. |
| 12110 | Unknown or unsupported arguments. | Check that the arguments are correct. |
| 12120 | Invalid argument value. | Check that the arguments values are correct. |
| 12200 | Failed to authenticate in the cluster. | Check that the username and password are correct. |
| 12210 | Failed to authorize in the cluster. | Check that the username and password are correct. |
| 12220 | Snapshot utility failed to get secure console for password input. | Make sure the console has elevated permissions. |
| 12300 | Failed to connect to the cluster. | Check the following:<br>- the node defined by the `-host` and `-port` arguments is reachable.<br>- the port number defined by the `-port` argument is not blocked by firewalls.<br>- check the cluster logs for further information. |
| 12400 | The persistent store is not configured. The command can't be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 12410 | Cluster is not active, the command cannot be executed. | Activate the cluster. |
| 12420 | Could not find the `Ignite-schedule` module in the cluster's class path. | Copy the `{GRIDGAIN_HOME}/libs/optional/ignite-schedule` folder to `{GRIDGAIN_HOME}/libs`. |
| 12430 | Schedule with the specified name not found. | Check if the specified schedule name is correct. |
| 12440 | Schedule with the specified name already exists. | Enter another name. |
| 12730 | Storage device is full. | Empty enough space on the storage device. |
| 12760 | Invalid parallelism level. | Use a positive parallelism level. |
| 12770 | Invalid compression level, should be between 1 and 9. | Specify a valid compression level. |
| 12780 | Compression level couldn't be applied, cause compression is off. | Enable compression. |
| 12800 | Command executed successfully, but snapshot tool failed to write result to output file. | Check the output file name and permissions. |
| 12810 | Command failed and snapshot tool failed to write error code to output file. | Check the output file name and permissions. |

## COPY

The COPY command copies the specified cache to the specified location.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh copy -id=SNAPSHOT_ID -dest=EXTERNAL_FOLDER -key_alias=ALIAS [-noprogress] [-skip_wal] [-chain=SINGLE|FROM] [-delete_source] [-verbose] [-single_copy] <ssl parameters> <connection parameters> <output parameters>

```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat copy -id=SNAPSHOT_ID -dest=EXTERNAL_FOLDER -key_alias=ALIAS [-noprogress] [-skip_wal] [-chain=SINGLE|FROM] [-delete_source] [-verbose] [-single_copy] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -id=SNAPSHOT_ID | Snapshot identifier to use. |
| -dest=EXTERNAL_FOLDER | Folder name where snapshot files should be moved. |
| -skip_wal | Move snapshot without dependent WAL. |
| -chain=SINGLE/FROM | Defines how to work with snapshot chains  (FULL-INC-INC-INC...):<br>- SINGLE - manipulate only with the defined snapshot (default);<br>- FROM - manipulate with snapshot chain (FULL-INC-INC-INC...) from the defined snasphot to the last one; |
| -delete_source | COPY will remove original snapshot if copy phase finished successfully cluster-wide. |
| -single_copy | Will synchronize node to copy partition files exactly once. |
| -noprogress | Do not print progress bar. |
| -comment=text | This argument allows to specify optional comment for command. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 16000 | Command failed. | This error means that something unexpected happened. Check cluster logs for errors. |
| 16110 | Unknown or unsupported arguments specified for command. | Check that the arguments are correct. |
| 16120 | Invalid arguments specified for command. | Check that the arguments values are correct. |
| 16200 | Snapshot utility failed to authenticate in cluster. | Check that the username and password are correct. |
| 16210 | Snapshot utility failed to authorize in cluster. | Check that the username and password are correct. |
| 16220 | Snapshot utility failed to get secure console for password input. | Make sure the console has elevated permissions. |
| 16300 | Snapshot utility failed to connect to cluster. | Check the following:<br>- the node defined by the -host and -port arguments is reachable.<br>- the port number defined by the -port argument is not blocked by firewalls.<br>- check GridGain cluster logs for further information. |
| 16400 | Snapshot is not configured, command cannot be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 16410 | Cluster is inactive, command cannot be executed. | Activate the cluster. |
| 16500 | Snapshot utility failed to find snapshot with specified ID. | Check that the snapshot ID is correct. Use the `list` command to get the ID of the required snapshot. |
| 16710 | Snapshot utility failed to move snapshot to destination folder. | Check if the destination folder has correct permissions. |
| 16720 | Snapshot utility failed to delete snapshots with specified IDs. | Check if the snapshot files have correct permissions. |
| 16730 | Storage device is full. | Empty enough space on the storage device. |
| 16740 | (When PITR is enabled) WAL files have been deleted manually after snapshot was created. | Use `-SKIP_WAL` flag to copy this snapshot. |
| 16760 | Invalid parallelism level. | Use a positive parallelism level. |
| 16800 | Command executed successfully, but snapshot utility failed to write result to output file. | Check the output file name and permissions. |
| 16810 | Command failed and snapshot utility failed to write error code to output file. | Check the output file name and permissions. |

## METADATA

Configures snapshot metadata.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh metadata -action=merge -src=SNAPSHOT_FOLDER1[,SNAPSHOT_FOLDER2,...] -id=SNAPSHOT_ID -dest=DEST_FILE [-template=snapshot-meta.bin] <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat metadata -action=merge -src=SNAPSHOT_FOLDER1[,SNAPSHOT_FOLDER2,...] -id=SNAPSHOT_ID -dest=DEST_FILE [-template=snapshot-meta.bin] <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -action=print/merge | Snapshot metadata operation type. |
| -src=SNAPSHOT_FOLDER1 [,SNAPSHOT_FOLDER2,...] | Paths to folders with snapshots. |
| -id=SNAPSHOT_ID | Snapshot identifier to use. |
| -file=METADATA_FILE | Metadata file path to process. |
| -verbose | Enable print information about partitions to console. |
| -dest=dest.file | Path to file with merged metadata. |
| -template=snapshot-meta.bin | Part of metadata file name for filter. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 14000 | Command failed. | This error means that something unexpected happened. Check cluster logs for errors. |
| 14110 | Unknown or unsupported arguments specified for command. | Check that the arguments are correct. |
| 14120 | Invalid arguments specified for command. | Check that the argument values are correct. |
| 14800 | Command executed successfully, but snapshot utility failed to write result to output file. | Check the output file name and permissions. |
| 14810 | Command failed and snapshot utility failed to write error code to output file. | Check the output file name and permissions. |

## ANALYZE

Analyzes the snapshot.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh analyze -src=SNAPSHOT_FOLDER -id=SNAPSHOT_ID [-page_size=4096] [-verbose] <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat analyze  -src=SNAPSHOT_FOLDER -id=SNAPSHOT_ID [-page_size=4096] [-verbose] <output parameters>
```
{% endtab %}
{% endtabs %}

### Command Arguments

| Arguments | Description |
|---|---|
| -src=SNAPSHOT_FOLDER | Path to folder with snapshot. |
| -id=SNAPSHOT_ID | Snapshot identifier to use. |
| -page_size=number | Snapshot page size. Default is 4096. |
| -verbose | Enable operation progress showing. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 15000 | Command failed. | This error means that something unexpected happened. Check cluster logs for errors. |
| 15110 | Unknown or unsupported arguments specified for command. | Check if the arguments are correct. |
| 15120 | Invalid arguments specified for command. | Check if the argument values are correct. |
| 15800 | Command executed successfully, but snapshot utility failed to write result to output file. | Check the output file name and permissions. |
| 15810 | Command failed and snapshot utility failed to write error code to output file. | Check the output file name and permissions. |

## CLEANUP_RESTARTING_CACHES

Cleans restarting caches.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh cleanup_restarting_caches [-verbose] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat cleanup_restarting_caches [-verbose] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 17000 | Command failed. | This error means that something unexpected happened. Check cluster logs for errors. |
| 17110 | Unknown or unsupported arguments specified for command. | Check if the arguments are correct. |
| 17120 | Invalid arguments specified for command. | Check if the argument values are correct. |
| 17200 | Snapshot utility failed to authenticate in cluster. | Make sure that the username and password are correct. |
| 17210 | Snapshot utility failed to authorize in cluster. | Make sure that the username and password are correct. |
| 17220 | Snapshot utility failed to get secure console for password input. | Make sure the console has elevated permissions. |
| 17300 | Snapshot utility failed to connect to cluster. | Check the following:<br>- the node defined by -host and -port arguments is reachable.<br>- the port number defined by -port is not blocked by firewalls.<br>- check the cluster logs for further information. |
| 17400 | Snapshot is not configured, command cannot be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 17410 | Cluster is inactive, command cannot be executed. | Activate the cluster. |
| 17730 | Storage device is full. | Empty enough space on the storage device. |
| 17760 | Invalid parallelism level. | Use a positive parallelism level. |
| 17800 | Command executed successfully, but snapshot utility failed to write result to output file. | Check the output file name and permissions. |
| 17810 | Command failed and snapshot utility failed to write error code to output file. | Check the output file name and permissions. |

## SECURITY_LEVEL

Sets the security level of the snapshot.

{% tabs %}
{% tab title="Unix" %}
```shell
snapshot-utility.sh security_level  [-level=<DISABLED|IGNORE_EXISTING|IGNORE_MISSING|REQUIRE>] [-verbose] <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% tab title="Windows" %}
```shell
snapshot-utility.bat security_level [-level=<DISABLED|IGNORE_EXISTING|IGNORE_MISSING|REQUIRE>] [-verbose]  <ssl parameters> <connection parameters> <output parameters>
```
{% endtab %}
{% endtabs %}

This command supports [connection parameters and output parameters](#parameters).

### Command Arguments

| Arguments | Description |
|---|---|
| -level=<DISABLED/IGNORE_EXISTING/IGNORE_MISSING/REQUIRE> | Snapshot security level to set. If this argument is omitted, current level will be displayed. |

### Error Codes

| Code | Description | Solution |
|---|---|---|
| 18000 | Command failed. | This error means that something unexpected happened. Check cluster logs for errors. |
| 18110 | Unknown or unsupported arguments specified for command. | Check if the arguments are correct. |
| 18120 | Invalid arguments specified for command. | Check if the argument values are correct. |
| 18200 | Snapshot utility failed to authenticate in cluster. | Make sure that the username and password are correct. |
| 18210 | Snapshot utility failed to authorize in cluster. | Make sure that the username and password are correct. |
| 18220 | Snapshot utility failed to get secure console for password input. | Make sure the console has elevated permissions. |
| 18300 | Snapshot utility failed to connect to cluster. | Check the following:<br>- the node defined by -host and -port arguments is reachable.<br>- the port number defined by -port is not blocked by firewalls.<br>- check the cluster logs for further information. |
| 18400 | Snapshot is not configured, command cannot be executed. | Refer to [Enabling Snapshots](full-incremental-snapshots.md#enabling-snapshots) for more details. |
| 18410 | Cluster is inactive, command cannot be executed. | Activate the cluster. |
| 18730 | Storage device is full. | Empty enough space on the storage device. |
| 18760 | Invalid parallelism level. | Use a positive parallelism level. |
| 18800 | Command executed successfully, but snapshot utility failed to write result to output file. | Check the output file name and permissions. |
| 18810 | Command failed and snapshot utility failed to write error code to output file. | Check the output file name and permissions. |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
