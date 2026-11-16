---
description: >-
  How MaxScale persists runtime configuration changes, how configuration
  synchronization keeps several MaxScale instances in step, and how to back up changes.
---

# MaxScale Runtime Configuration Changes

This page describes how MaxScale handles configuration changes made at runtime.

The [MaxCtrl](../../../../reference/maxscale-maxctrl.md) and [REST-API](../../../../reference/maxscale-rest-api/maxscale-rest-api.md) documents provide information about making runtime changes.

All changes to the configuration done via MaxCtrl are persisted as individual configuration files in `/var/lib/maxscale/maxscale.cnf.d/`. The content of these files will override any configurations found in the main configuration file or any auxiliary configuration files.

Refer to the [Dynamic Configuration](README.md#dynamic-configuration) section for more details on how this mechanism works and how to disable it.

## Configuration Synchronization

The configuration synchronization mechanism is intended for synchronizing configuration changes done on one MaxScale to all other MaxScales. This is done by propagating the changes via the database cluster used by Maxscale.

When configuring configuration synchronization for the first time, the same static configuration files should be used on all MaxScale instances that use the same cluster: the value of `config_sync_cluster` must be the same on all MaxScale instances and the cluster (i.e. the monitor) pointed by it and its servers must be the same in every configuration.

Whenever the MaxScale configuration is modified at runtime, the latest configuration is stored in the database cluster in the `mysql.maxscale_config` table. The table is created when the first modification to the configuration is done. A local copy of the configuration is stored in the data directory to allow MaxScale to function even if a connection to the cluster cannot be made. By default this file is stored at `/var/lib/maxscale/maxscale-config.json`.

Whenever MaxScale starts up, it checks if a local version of this configuration exists. If it does and it is a valid cached configuration, the static configuration file as well as any other generated configuration files are ignored. The exception is the `[maxscale]` section of the main static configuration file which is always read.

Each configuration has a version number with the initial configuration being version 0. Each time the configuration is modified, the version number is incremented. This version number is used to detect when MaxScale needs to update its configuration.

### Error Handling in Configuration Synchronization

When doing a configuration change on the local MaxScale, if the configuration change completes on MaxScale but fails to be committed to the database, MaxScale will attempt to revert the local configuration change. If this attempt fails, MaxScale will discard the cached configuration and abort the process.

When synchronizing with the cluster, if MaxScale fails to apply a configuration retrieved from the cluster, it attempts to revert the configuration to the previous version. If successful, the failed configuration update is ignored. If the configuration update that fails cannot be reverted, the MaxScale configuration will be in an indeterminate state. When this happens, MaxScale will discard the cached configuration and abort the process.

When loading a locally cached configuration during startup, if any errors are found in the cached configuration, it is discarded and the MaxScale process will attempt to restart by exiting with code 75 from the main process. If MaxScale is being used as a SystemD service, this will automatically trigger a restart of MaxScale and no further actions are needed.

The most common reason for a failed configuration update is missing files. For example, if a configuration update adds encrypted connections to a server and the TLS certificates it uses were not copied over to all MaxScale nodes before the change was done, the operation will fail on all nodes that do not have these files.

If the synchronization of the configuration change fails at the step when the database transaction is being committed, the new configuration can be momentarily visible to the local MaxScale. This means the changes are not guaranteed to be atomic on the local MaxScale but are atomic from the cluster's point of view.

### Synchronization of Encrypted Passwords

Starting with MaxScale 6.4.9, any passwords that are transmitted by the configuration synchronization are encrypted if password encryption has been enabled in MaxScale. This means that all MaxScale nodes in the same configuration cluster must be configured to use password encryption and they need to all use the same encryption keys that were created with `maxkeys`.

### Managing Configuration Synchronization

The output of `maxctrl show maxscale` contains the `Config Sync` field with information about the current configuration state of the local Maxscale as well as the state of any other nodes using this cluster.

```
├──────────────┼─────────────────────────────────────────────────────────────┤
│ Config Sync  │ {                                                           │
│              │     "checksum": "3dd6b467760d1d2023f2bc3871a60dd903a3341e", │
│              │     "nodes": {                                              │
│              │         "maxscale": "OK",                                   │
│              │         "maxscale2": "OK"                                   │
│              │     },                                                      │
│              │     "origin": "maxscale",                                   │
│              │     "status": "OK",                                         │
│              │     "version": 2                                            │
│              │ }                                                           │
├──────────────┼─────────────────────────────────────────────────────────────┤
```

The `version` field is the logical configuration version and the `origin` is the node that originates the latest configuration change. The `checksum` field is the checksum of the logical configuration and can be used to compare whether two Maxscale instances are in the same configuration state. The `nodes` field contains the status of each MaxScale instance mapped to the hostname of the server. This field is updated whenever MaxScale reads the configuration from the cluster and can thus be used to detect which MaxScales have updated their configuration.

The `mysql.maxscale_config` table where the configuration changes are stored must not be modified manually. The only case when the table should be modified is when resetting the configuration synchronization.

To reset the configuration synchronization:

1. Stop all MaxScale instances
2. Remove the cached configuration file stored at `/var/lib/maxscale/maxscale-config.json` on all MaxScale instances
3. Drop the `mysql.maxscale_config` table
4. Start all MaxScale instances

To disable configuration synchronization, remove `config_sync_cluster` from the configuration file or set it to an empty string: `config_sync_cluster=""`. This can be done at runtime with MaxCtrl by passing an empty string to `config_sync_cluster`:

```
maxctrl alter maxscale config_sync_cluster ""
```

If MaxScale cannot create a connection to the database cluster, configuration changes are not possible until communication with the database is possible. To override this behavior and force the changes to be done, use the `--skip-sync` option for maxctrl or the `sync=false` HTTP parameter for the REST API. Any updates done with `--skip-sync` will overwritten by changes coming from the cluster.

### Limitations in Configuration Synchronization

Only the MaxScale configuration is synchronized. Any external files (TLS certificates, configuration files for modules or data generated by MaxScale) are not synchronized. For example, the rule files for the cache filter must be synchronized separately if the filter itself is modified.

Starting with MaxScale 22.08, the `Maintenance` and `Draining` states of servers and modifications to the administrative users will be synchronized. In older versions servers had to be put into maintenance mode and users had to be modified separately on each MaxScale.

* ([MXS-3619](https://jira.mariadb.org/browse/MXS-3619)) External files are not synchronized.
* ([MXS-4276](https://jira.mariadb.org/browse/MXS-4276)) The `--export-config` option will not export the cluster configuration and instead exports only the static configuration files. To start a new MaxScale based off of a clustered configuration, copy the static configuration files as well as the JSON configuration in `/var/lib/maxscale/maxscale-config.json` to the new MaxScale instance.

## Backing Up Configuration Changes

The combination of configuration files can be done either manually (e.g. `rsync`) or with the `maxscale --export-config=FILE` command line option. See `maxscale --help` for more information about how to use the `--export-config` flag.

For example, to export the current runtime configuration, run the following command.

```
maxscale --export-config=/tmp/maxscale.cnf.combined
```

This will create the `/tmp/maxscale.cnf.combined` file and write the current configuration into the it. This allows new MaxScale instances to be easily set up without requiring copying of all runtime configuration files. The user executing the command must be able to read all MaxScale configuration files as well as create and write the provided filename.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
