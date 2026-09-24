---
description: >-
  Create full and incremental data snapshots in GridGain 9, restore them,
  manage snapshot storage, and follow snapshot best practices.
---

# Data Snapshots and Recovery

{% hint style="info" %}
This feature is only available as a part of GridGain 9 Ultimate edition.
{% endhint %}

GridGain provides the ability to create snapshots of data stored cluster-wide, that can later be used for cluster recovery purposes. Having snapshots at hand, they can be used to recover the cluster to a state recorded in a snapshot.

## Limitations

There are currently the following limitations on snapshots:

- Snapshots can only be created on [Native persistent](../../architecture/storage/engines/native-persistent-storage.md) and [rocksDB](../../architecture/storage/engines/rocksdb-persistent-storage.md) primary storages.
- Only one snapshot restore operation can run in the cluster at a time.
- A snapshot in progress is cancelled if rebalance starts on a table included in the snapshot.
- GridGain 9 has no built-in snapshot scheduler. Schedule snapshots with an external tool. See [Snapshot Frequency](#snapshot-frequency).

## Snapshot Scope

Since snapshots store all data, it may be preferable to only create a snapshot of data you need. You can use the following parameters to configure snapshot scope:

- `--all` - creates a snapshot of all tables and [distributed maps](../../gridgain9-usage/data-structures/distributed-maps.md) and [sequences](../../gridgain9-usage/sql/sql-api.md#using-sequences). This is a standalone flag that does not accept arguments, and is not compatible with other scope parameters.
- `--tables` - comma-separated list of tables that will be included in the snapshot. Any structures required for the specified tables will be included in the snapshot automatically. Incompatible with `--all`.
- `--structures` - comma-separated list of [distributed structures](../../gridgain9-usage/data-structures/distributed-maps.md) and [sequences](../../gridgain9-usage/sql/sql-api.md#using-sequences) that will be included in the snapshot. Any system tables required for the specified structures will be included in the snapshot automatically. Incompatible with `--all`.

## Snapshot Sizing

A snapshot stores the data of each included partition as binary tuples. It keeps only the version of the snapshot timestamp, so a snapshot does not include historical MVCC versions. As a result, a full snapshot is roughly the size of the live data set it covers, excluding version history.

An incremental snapshot stores only the tuples that changed relative to the previous snapshot in the chain. Its size depends on how much data changed since then, not on the total data set size.

## Snapshot Frequency

GridGain 9 does not include a built-in snapshot scheduler. Create snapshots on a schedule that suits your recovery requirements using an external scheduler, such as `cron`, that invokes the `cluster snapshot create` command.

Create snapshots periodically to reduce both recovery time and the volume of change between snapshots. A common approach is a daily full snapshot combined with more frequent incremental snapshots. Choose the cadence based on your workload and how much data loss is acceptable between snapshots.

Snapshot creation runs as a single long read-only transaction while writing snapshot data to the configured destination. The main performance cost is the write throughput to that destination, so storing snapshots on storage separate from the cluster data minimizes the impact on cluster operations.

## Creating Full Snapshots

To create a full snapshot, use the `cluster snapshot create` [CLI](../../reference/cli-tool.md#snapshot-commands) command. For example:

```bash
cluster snapshot create --type=full --tables=PERSON
```

The command above creates a full snapshot of a table Person at a specified destination path (see [Snapshot Location](#snapshot-location) for the latter).

## Creating Incremental Snapshots

When creating incremental snapshots, successive copies of the data contain only the changes since the last full or incremental snapshot. The base snapshot for incremental snapshots must be a full snapshot, but all subsequent ones can be incremental. The latest valid snapshot will be found for the tables you have specified, and an incremental snapshot based on it will be created.

Here is how you can create an incremental snapshot based on the full snapshot created above:

```bash
cluster snapshot create --type=incremental --tables=PERSON
```

You cannot add more tables to the snapshot when creating an incremental snapshot. You need to have the same tables in it as in the base snapshot created before.

## Creating Snapshots in the Past

You can also make a snapshot for the specific cluster state in the past, for example:

```bash
cluster snapshot create --type=full --timestamp=2024-09-10T10:53:00+01:00 --all
```

The timestamp must be specified in ISO format.

{% hint style="info" %}
The specified time cannot be below the [low watermark](../../architecture/storage/low-watermark-and-gc.md), as historic data would be unavailable.
{% endhint %}

## Snapshot Encryption

By default, if [data encryption](../../security/transparent-data-encryption.md) is disabled on the cluster, snapshots are also not encrypted. If data encryption is enabled, snapshots will be encrypted by using the same encryption as your data.

You can also manually specify the pre-configured encryption provider in the `encryption-provider` configuration to use the specific encryption. For more information on configuring encryption, see [data encryption](../../security/transparent-data-encryption.md).

```bash
cluster snapshot create --type=full --tables=PERSON --encryption-provider=keystore
```

Once the encrypted snapshot is created, it can only be restored by including the `decryption-provider` in the `restore` command.

## Restoring Snapshots

To restore snapshots, you can use the `cluster snapshot restore` command.

To make sure your snapshot is restored correctly, follow these guidelines:

- Make sure that the cluster topology is the same as the one snapshot was taken on.
- The distribution zones on the target cluster must have the same number of partitions as when the snapshot was taken. This applies to both `LOCAL` and `REMOTE` snapshots; restoring into a zone whose partition count has changed fails with a partition count mismatch error.
- Stop traffic to the cluster during restoration to avoid possible inconsistencies and failed operations.

{% hint style="info" %}
If any user schemas referenced by the snapshot do not currently exist on the target cluster (for example, because they were dropped after the snapshot was taken), they are recreated automatically as empty schemas during restore. Objects inside those schemas are then restored by the regular snapshot machinery. Schema-level privileges or grants are not part of the snapshot and may need to be re-applied after restore.
{% endhint %}

When you are prepared to restore data to the cluster, run the `restore` command. For example:

```bash
cluster snapshot restore --id=8eb10b48-6885-4922-a1af-c28d8473ba28
```

The command above restores all tables in the snapshot with the specified ID, from the specified source path (see [Snapshot Location](#snapshot-location) for the latter). You can also choose to only restore specific tables stored in the snapshot, instead of all of them. In this case, specify the fully qualified table names of the tables to restore, for example:

```bash
cluster snapshot restore --id=8eb10b48-6885-4922-a1af-c28d8473ba28 --tables=PERSON
```

When restoring encrypted snapshots, specify the same [encryption provider](../../security/transparent-data-encryption.md) you used earlier to decrypt the snapshot in the `decryption-provider` parameter:

```bash
cluster snapshot restore --id=8eb10b48-6885-4922-a1af-c28d8473ba28 --decryption-provider=keystore
```

### Heterogeneous Recovery

A `REMOTE` snapshot created on a GridGain 9 cluster can be restored on the same or on any other GridGain 9 cluster, granted it has enough disk space to accommodate the snapshot data. The target cluster can have a different number of nodes, but each distribution zone must keep the same number of partitions it had when the snapshot was taken. Changing a zone's partition count prevents the snapshot from being restored.

## Checking Snapshot Status

You can check the status of all snapshots by using the `cluster snapshot status` command. By default, this command provides information about all snapshots in the cluster.

```bash
cluster snapshot status
```

You can narrow information down by providing the snapshot ID. If you do, you can also use the `--all-nodes` option to see information about the snapshot on each specific node in the cluster. For example:

```bash
cluster snapshot status --id=8eb10b48-6885-4922-a1af-c28d8473ba28  --all-nodes
```

The command above returns information about all operations with the snapshots per node.

The following information is provided:

| Column | Description |
|---|---|
| Operation ID | The ID of the operation. For create operations, this is the snapshot ID. For delete operations, this is the ID of the delete operation. |
| Start time | Time when the operation was started in UNIX time. |
| Operation | The operation performed. `CREATE` for creating snapshots, `DELETE` for deleting snapshots. |
| Status | Current operation status. Possible values: `STARTED`, `COMPLETED`, `FAILED`. |
| Target Snapshot ID | The snapshot the operation was performed against. |
| Base Snapshot ID | For incremental snapshots, the id of the snapshot this snapshot is based on. |
| Description | Operation description. |
| Timestamp | Point in time that corresponds to the system state the snapshot reflects. |
| URI | The base URI used by the snapshot operation. |
| URI Type | The path definition type: LOCAL or REMOTE. |

## Listing Snapshots

You can list all available snapshots from configured snapshot paths (both `REMOTE` and `LOCAL`) using the `cluster snapshot list` command.

```bash
cluster snapshot list
```

By default, the command displays snapshots from all configured snapshot paths, plus the default snapshot path when no paths are configured (see [snapshot configuration](../../reference/configuration/cluster-configuration-parameters.md#snapshots-configuration) for path setup). The command displays basic information about each snapshot. You can use additional options to get more detailed information:

- `--show-nodes` - displays node names instead of just showing the count of nodes;
- `--show-tables` - displays table names instead of just showing the count of tables;
- `--show-source-uri` - displays the full URI path where the snapshot is stored;
- `--source` - lists snapshots only from a specific configured path (as defined in the [snapshot configuration](../../reference/configuration/cluster-configuration-parameters.md#snapshots-configuration)).

For example, to see all snapshots with full node and table details:

```bash
cluster snapshot list --show-nodes --show-tables
```

To list snapshots from a specific configured path, specify it explicitly:

```bash
cluster snapshot list --source=absolute-path-example
```

{% hint style="info" %}
When listing snapshots from a `LOCAL` path, every node in the cluster's logical topology is queried and the per-node results are aggregated by snapshot ID. The *Number of Actual Nodes* column reflects only nodes that are currently in the topology and responded to the scan, so snapshots whose source nodes have all left the topology will not appear in the listing.
{% endhint %}

The following information is provided for each snapshot:

| Column | Description |
|---|---|
| Snapshot ID | The unique identifier of the snapshot. |
| Parent Snapshot ID | For incremental snapshots, the ID of the parent snapshot this snapshot is based on. |
| Type | The type of snapshot: `FULL` or `INCREMENTAL`. |
| Creation Time | Time when the snapshot was created, in UNIX time. |
| Source | The name of the snapshot path used by the snapshot. |
| Path Type | The type of the snapshot path: `LOCAL` or `REMOTE`. |
| URI | The name of the configured snapshot path. Only shown if the `show-source-uri` option is used. |
| Number of Target Nodes | The number of nodes the snapshot was intended for. Shows node names instead if the `--show-nodes` option is used. |
| Number of Actual Nodes | The number of nodes where the snapshot is actually present. Shows node names instead if the `--show-nodes` option is used. |
| Number of Tables | The number of tables in the snapshot. Shows table names instead if the `--show-tables` is used. |

## Deleting Snapshots

You can delete a snapshot using the `delete` command.

```bash
cluster snapshot delete --id [--url] 
```

Where: `id` is the snapshot's ID and `url` (optional) is the cluster's URL.

For example:

```bash
cluster snapshot delete --id=8eb10b48-6885-4922-a1af-c28d8473ba28 --url=http://localhost:10300 
```

## Snapshot Location

To specify the snapshot location, you need to configure the snapshot "path" in the [cluster configuration](../../reference/configuration/cluster-configuration-parameters.md#snapshots-configuration), and then use it in your snapshots. If not specified, snapshots use the default directory (`{GRIDGAIN_HOME}/work/snapshots` if no other default is configured). For a full configuration example, see the [Example](#example) section below.

The same location must be used for subsequent snapshot operation, for example:

- Incremental snapshot destination must have the same URI and type as all parent snapshots.
- The snapshot restore operations must point to the same URI with the same type (`LOCAL` or `REMOTE`) that was used when creating that snapshot.

### Local Snapshots

`LOCAL` snapshots are not shared between nodes. Every node saves the snapshot metadata and all partition files hosted by the node. Local snapshots can only be restored on the node they were created on. You can list `LOCAL` snapshots from a specific path with `cluster snapshot list --source=<name>`, or omit `--source` to list snapshots from all configured paths.

Depending on how the path is specified, the exact path will be slightly different:

- For _absolute_ path, snapshot with ID 1 would be created in the `/absolute-path/node-1/snapshot-1` directory.
- For _relative_ path, the same snapshot would be created in the `{GRIDGAIN_HOME}/relative-path/snapshot-1` directory.

### Remote Snapshots

`REMOTE` snapshots save only one copy of snapshot metadata and partition files. The location where this copy is saved must be accessible by all nodes with the use of the same base URI. The snapshot saves cluster information and data. Remote snapshots can be restored on any node in the cluster, or on a different cluster.

Depending on how the path is specified, the exact storage path will be slightly different:

- For _absolute_ path, the same snapshot would be created in the `/absolute-path/snapshot-1` directory.
- For _relative_ path, the same snapshot would be created in the `{GRIDGAIN_HOME}/relative-path/snapshot-1` directory.

### Example

For this example, let's assume that the cluster configuration defines the path in the following way:

```
{
  "ignite": {
    "snapshot": {
      "paths": [
        {
          "default": false,
          "name": "absolute-path-example",
          "type": "REMOTE",
          "uri": "file:/shared/folder/path"
        }
      ]
    }
  }
}
```

You can specify the snapshot location by adding the `--destination` parameter:

```
cluster snapshot create --type=full --tables=PERSON --destination=absolute-path-example
```

Snapshots can then be restored from the specified location by specifying the `--source` parameter.

```
cluster snapshot restore --id=8eb10b48-6885-4922-a1af-c28d8473ba28 --source=absolute-path-example
```

## Best Practices

### Snapshot Cadence

- *Keep incremental snapshots within the tombstone retention window.* GridGain preserves the tombstones needed for an incremental snapshot only for `snapshotTombstonesTtlMinutes` (24 hours by default) after the previous snapshot. If more time passes, the incremental snapshot cannot be created. Take incremental snapshots well within this window. The tombstone retention can be tuned by using the `snapshotTombstonesTtlMinutes` property in [cluster configuration](../../reference/configuration/cluster-configuration-parameters.md#snapshots-configuration) and is applied without a restart.
- *Take a fresh full snapshot periodically to bound chain length.* Restoring an incremental snapshot replays the whole chain, from the base full snapshot to the target. The longer the chain, the longer the restore takes. A periodic full snapshot keeps restore times predictable.
- *Take a new snapshot after changing partition configuration.* If you change the number of partitions in a distribution zone, snapshots taken before the change can no longer be restored into that zone. Take a new full snapshot after any change to a zone's partition count so that you retain a restorable snapshot. See [Heterogeneous Recovery](#heterogeneous-recovery).

### Retention and Cleanup

- *Delete incremental chains from newest to oldest.* A snapshot that has dependent incremental snapshots cannot be deleted. Remove the most recent snapshot in a chain first, then work backwards.
- *Schedule regular cleanup.* GridGain 9 has no built-in scheduler, so use an external scheduler to run `cluster snapshot delete` and reclaim disk space according to your retention policy.

### Reliability

- *Monitor every operation to completion.* Use `cluster snapshot status` to confirm each operation reaches the `COMPLETED` state and to detect failures.
- *Avoid taking snapshots during rebalance.* An in-progress snapshot is cancelled if rebalance starts on a table it includes. Schedule snapshots outside cluster scaling and rebalancing windows.

### Storage and Recovery

- *Store snapshots separately from cluster data.* Snapshot creation writes heavily to the destination, so using a separate disk minimizes the impact on cluster operations.
- *Use `REMOTE` snapshots when possible.* A `LOCAL` snapshot can only be restored on the node that created it, while a `REMOTE` snapshot can be restored on any node or on a different cluster. See [Remote Snapshots](#remote-snapshots) for more information.
- *Plan disk capacity on the restore target.* The target needs space for the snapshot data, and point-in-time recovery temporarily keeps both data versions during recovery.

### Security

- *Only give snapshot privileges to administrators.* Grant the `CREATE_SNAPSHOT`, `RESTORE_SNAPSHOT`, `DELETE_SNAPSHOT`, and `CHECK_SNAPSHOT` [privileges](../../security/user-permissions-and-roles.md) only to the roles that need them.
- *Preserve encryption providers and keys.* An encrypted snapshot can only be restored when its encryption provider is configured on the target cluster. Retain the provider and its keys for as long as you keep the snapshot.
