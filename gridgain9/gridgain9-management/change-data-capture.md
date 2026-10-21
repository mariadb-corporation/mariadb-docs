---
description: >-
  Use GridGain 9 Change Data Capture (CDC) to replicate table changes to
  external systems such as Apache Iceberg, and from Microsoft SQL Server.
---

# Change Data Capture

GridGain provides Change Data Capture (CDC) implementation that can be used to integrate with external databases and propagate changes between them.

## Preparing CDC

Before starting replication, you need to configure a CDC source and sink. These will be used to start replication later.

## Prepare Data Schemas

For the replication to be successful, you need to make sure table schemas in source and sink are the same. If you do not yet have tables in the sink, GridGain will automatically create tables with matching schemas when replication starts.

## Configuring CDC Source

```
cdc source create --name <source_name> --type <source_type>  --tables <table_name1>[,<table_name2>,...] [--parameters <property_name1>=<property_value1>] [--parameters <property_name2>=<property_value2>]... [--experimental]
```

Command arguments:

| Property | Default | Description |
|---|---|---|
| name |  | The name the CDC source. This name will be used to reference it. |
| type |  | Data source type. Supported values: `gridgain`, `mariadb`, `mssql`. |
| tables |  | Comma-separated list of tables that will be replicated. |
| parameters |  | Optional additional parameters. The following parameters are supported:<br>- page-size - the size of each page sent via replication.<br>- poll-interval - the interval at which GridGain checks for updates in source tables. |
| experimental | false | Optional. Enables experimental source types. Creating or updating a source with an experimental type fails unless this flag is set. |

Below is an example of a CDC data source:

```
cdc source create --name gridgain_source --type gridgain --tables PUBLIC.MY_TABLE1 --parameters "poll-interval-ms"=1000 --parameters "page-size"=1024
```

### Updating CDC Source

You can update the CDC source when the relevant replication is not running by using the `cdc source update` command. The command uses the same arguments as the `cdc source create` command, including `--experimental`. For example:

```
cdc source update --name gridgain_source --type gridgain --parameters "poll-interval-ms"=1000 --tables=PUBLIC.MY_TABLE1
```

### Removing CDC Source

When you no longer need the CDC source, you can delete it with the `cdc source delete` command:

```
cdc source delete --name gridgain_source
```

## Configuring CDC Sink

```
cdc sink create --name <sink_name> --type <sink_type> [--parameters <property_name1>=<property_value1>] [--parameters <property_name2>=<property_value2>]... [--experimental]
```

Command parameters:

| Property | Default | Description |
|---|---|---|
| name |  | The name the CDC sink. This name will be used to reference it. |
| type |  | Data sink type. Supported values: `iceberg`; `gridgain_9`. |
| parameters |  | Optional additional parameters. Specific list of parameters depends on the type of the data sink. For Iceberg data sink, [Iceberg](https://iceberg.apache.org/docs/latest/configuration/#table-properties) configuration properties are supported. |
| create-table-if-not-exists | true | Optional. If `true`, missing tables are automatically created in the sink before replication starts. Has no effect for the `gridgain_9` sink, which requires the destination table to already exist. |
| experimental | false | Optional. Enables experimental sink types. Creating or updating a sink with an experimental type fails unless this flag is set. No sink type currently requires it. |

Below is an example of a CDC data sink:

```
cdc sink create --name iceberg_sink --type iceberg --parameters "catalog.type"="iceberg" --parameters "catalog.warehouse"="s3://my-bucket/my/key/prefix" --parameters "catalog-impl"="org.apache.iceberg.aws.glue.GlueCatalog" --parameters "io-impl"="org.apache.iceberg.aws.s3.S3FileIO" --parameters "s3.access-key-id"="my-secret-key-id" --parameters "s3.secret-access-key"="my-secret-access-key"
```

### Updating CDC Sink

You can update the CDC sink when the relevant replication is not running by using the `cdc sink update` command. The command uses the same arguments as the `cdc sink create` command, including `--experimental`: updating a sink that uses an experimental type also requires the `--experimental` flag. For example:

```
cdc sink update --name iceberg_sink --type iceberg --parameters "catalog.type"="iceberg"
```

### Removing CDC Sink

When you no longer need the CDC sink, you can delete it with the `cdc sink delete` command:

```
cdc sink delete --name gridgain_source
```

## Running CDC

### Creating Replication

To run CDC, you need to prepare the replication that connects the previously connected CDC source with the CDC sink. When created, replication will not start automatically, but can be used to review the involved tables by using the `cdc replication status`.

The example below shows how you can create a replication:

```
cdc replication create --name <replication_name> --source <gridgain_source> --sink <target_sink> --mode (ALL|NEW_DATA) [--execution-nodes <node_id1>[,<node_id2>,...]]
```

Command parameters:

| Property | Default | Description |
|---|---|---|
| name |  | The name the replication. This name will be used to reference it. |
| source |  | Data source to use in replication. |
| sink |  | Data sink to use in replication. |
| send-existing-data |  | Determines if historic data will be transferred. Possible values:<br>- `ALL` - all existing data will be replicated first, then updates will be transferred.<br>- `NEW_DATA` - only new data will be transferred. Previously existing data will remain in the source. |
| execution-nodes | any node | The list of nodes allowed to run the replication. If not specified, the replication can run on any node of the cluster and fails over to any live node. The list can be changed later with `cdc replication update`. |

{% hint style="info" %}
A `gridgain` source supports only `NEW_DATA` mode. `ALL` mode, which first replicates existing data and then switches to new changes, is available only for external sources such as `mariadb` and `mssql`. Starting a replication that uses a `gridgain` source in `ALL` mode fails.
{% endhint %}

### Starting Replication

To start the replication process, use the `cdc replication start` command. This will initiate the transfer process.

{% hint style="warning" %}
Once the replication is started, the sink and source involved in it can no longer be changed until the replication is stopped.
{% endhint %}

The example below shows how you can start a replication created on a previous step:

```
cdc replication start --name <replication_name>
```

### Monitoring Replication

You can get the list of existing replications with the `cdc replication list` command:

```
cdc replication list
```

You can also get detailed information about a replication by using the `cdc replication status` command. The command will return the replication status and progress for each table involved in the replication.

For example, the following command will

```
cdc replication status --name gg_to_iceberg
```

### Replication Failover

A replication runs on one node at a time. The `cdc replication status` command reports that node (`running on <node>`), and `cdc replication list` returns it as `runningOnNode`.

If the node executing a replication leaves the cluster, the replication is transferred to another node and resumes from the last saved position:

- When the replication was created without `--execution-nodes`, any live node of the cluster is a candidate. The remaining nodes agree on the new node without coordination, so each replication moves to exactly one node, and different replications spread across the cluster.
- When `--execution-nodes` names specific nodes, the new node is chosen from the live nodes in that list. If none of them is in the cluster, the replication becomes `FAILED` and is restarted when one of the listed nodes joins the cluster again.

The transfer starts the replication from the last position saved by the previous node, so the changes between that position and the moment the node left are delivered again. Sinks apply changes by primary key, so the repeated delivery does not create duplicate rows.

Failover needs the replication metadata to stay available while a node is down. GridGain 9 keeps it in system tables that the first CDC command creates, such as the first `cdc source create`, on the nodes that are in the cluster at that moment. Create the first CDC source, sink or replication after every node has joined the cluster.

In a mixed-version cluster, create replications without `--execution-nodes` only after every node is upgraded. An older node treats an empty node list as having no eligible node and marks such a replication `FAILED` when the node running it leaves.

#### Changing Execution Nodes

The list of nodes allowed to run a replication can be changed without deleting the replication, for example when nodes are added to the cluster or come back under new names:

```
cdc replication update --name gg_to_iceberg --execution-nodes node2,node3
cdc replication update --name gg_to_iceberg --any-node
```

A running replication keeps running where it is. The new list applies the next time the replication is started or fails over.

#### Node Restart

When a node that runs a replication is restarted, the replication is picked up by another node as described above. If no other node takes it over before the node is back, for example after a restart of the whole cluster, the restarted node resumes its own replications of `mariadb` and `mssql` sources from the last saved position. A `gridgain` source replication in that situation must be started again with `cdc replication start`.

The resume position must still be available in the source. For a `mssql` source it must be within the SQL Server CDC retention period of the capture instance, which is 3 days by default (`sys.sp_cdc_change_job` with `@job_type = 'cleanup'`, `@retention` in minutes). A replication whose position has been cleaned up becomes `FAILED` and has to be deleted and created again.

A SQL Server capture instance has no position until it captures its first change. If a `mssql` replication is restarted before the source table has had any captured change since CDC was enabled on it, there is no saved position to resume from, and the replication continues from the current position of the database.

### Stopping Replication

To stop replication, use the `cdc replication stop` command:

```
cdc replication stop --name gg_to_iceberg
```

Once the replication is stopped, the data will no longer be transferred.

## Configuring CDC with Iceberg

This section describes how to configure Change Data Capture with Apache Iceberg as the data sink.

### Overview

CDC with Iceberg allows you to replicate data from GridGain tables to Iceberg tables stored in various backends (S3, HDFS, local filesystem). The configuration involves creating a CDC source, an Iceberg sink, and a replication between them.

### Configuration Steps

#### Create CDC Source

Configure the GridGain source that will be monitored for changes:

```
cdc source create --name gridgain_source --type gridgain --tables PUBLIC.MY_TABLE1 --parameters "poll-interval-ms"=1000 --parameters "page-size"=1024
```

#### Create Iceberg Sink

Configure the Iceberg sink with the target storage backend:

```
cdc sink create --name iceberg_sink --type iceberg --parameters "catalog.type"="iceberg" --parameters "catalog.warehouse"="s3://my-bucket/my/key/prefix" --parameters "catalog-impl"="org.apache.iceberg.aws.glue.GlueCatalog" --parameters "io-impl"="org.apache.iceberg.aws.s3.S3FileIO" --parameters "s3.access-key-id"="my-secret-key-id" --parameters "s3.secret-access-key"="my-secret-access-key"
```

Configuration parameters:

| Parameter | Description |
|---|---|
| catalog.type | Type of Iceberg catalog (usually `iceberg`). |
| catalog.warehouse | Storage location. |
| catalog-impl | Iceberg catalog implementation class. |
| io-impl | File I/O implementation for the storage backend. |

Additional parameters support [Iceberg table properties](https://iceberg.apache.org/docs/latest/configuration/#table-properties).

#### Create and Start Replication

Create the replication connecting source and sink:

```
cdc replication create --name gg_to_iceberg --source gridgain_source --sink iceberg_sink --mode NEW_DATA
```

Start the replication process:

```
cdc replication start --name gg_to_iceberg
```

## Replicating from Microsoft SQL Server

This section describes how to replicate changes from a Microsoft SQL Server database into GridGain 9 tables. SQL Server acts as the CDC source, and a GridGain 9 sink lands the changes in local tables: inserts and updates are applied as upserts, and deletes remove the corresponding rows.

### Prerequisites and Required Permissions

Prepare SQL Server in this order:

1. Enable CDC on the database with `EXEC sys.sp_cdc_enable_db`. This requires the `sysadmin` role. The SQL Server Agent must be running, because the CDC capture and cleanup jobs run in it.
2. Enable CDC on each replicated table with `sys.sp_cdc_enable_table`. The captured column list (`@captured_column_list`) must include every primary-key column, or the source refuses to start. If `@role_name` is not `NULL`, the replication login must be a member of that role. You can enable CDC on a table after the replication starts: the source waits for the capture instance before it takes the snapshot.
3. Grant the replication login these permissions in the source database:
   * `SELECT` on each source table, for the snapshot and the primary-key metadata.
   * `SELECT` on `cdc.captured_columns` and `cdc.change_tables`, for the column and type checks at start.
   * `SELECT` on the function `cdc.fn_cdc_get_all_changes_<capture_instance>`, for the change reads. The `sys.fn_cdc_*` functions are public.
4. In `msdb`, create a user for the login and grant it `SELECT ON msdb.dbo.cdc_jobs`. The source reads the cleanup job's retention from this table to tell changes that the retention cleanup discarded (data loss) apart from a capture instance whose start position only moved. Without this grant the source runs in a degraded mode and logs a warning that names the grant. In that mode, a replication on a table that had no changes yet can end as expired after a restart, although no change was lost.
5. Create the destination GridGain 9 table with a schema compatible with the source rows (matching column names and types). Schema changes are not propagated automatically.

For example:

```sql
USE testdb;
EXEC sys.sp_cdc_enable_db;
EXEC sys.sp_cdc_enable_table @source_schema = N'dbo', @source_name = N'ACCOUNTS',
    @role_name = NULL, @supports_net_changes = 0;
GRANT SELECT ON dbo.ACCOUNTS TO replicator;
GRANT SELECT ON cdc.captured_columns TO replicator;
GRANT SELECT ON cdc.change_tables TO replicator;
GRANT SELECT ON cdc.fn_cdc_get_all_changes_dbo_ACCOUNTS TO replicator;

USE msdb;
CREATE USER replicator FOR LOGIN replicator;
GRANT SELECT ON dbo.cdc_jobs TO replicator;
```

### Create the SQL Server Source

```
cdc source create --name mssql_source --type mssql --tables dbo.ACCOUNTS \
  --parameters jdbcUrl="jdbc:sqlserver://localhost:1433;databaseName=testdb;encrypt=true;trustServerCertificate=true" \
  --parameters user=replicator --parameters password=<password>
```

Source parameters:

| Parameter | Default | Description |
|---|---|---|
| jdbcUrl |  | JDBC connection URL for SQL Server. Provide this, or supply `host` and `database` (and optionally `port`) instead. |
| host |  | SQL Server host. Used to build the JDBC URL when `jdbcUrl` is not set. |
| database |  | Database name. Used to build the JDBC URL when `jdbcUrl` is not set. |
| port | 1433 | SQL Server port. Used to build the JDBC URL when `jdbcUrl` is not set. |
| user |  | SQL Server user. |
| password |  | SQL Server password. |
| pollIntervalMs | 1000 | Interval, in milliseconds, at which GridGain polls SQL Server for changes. |
| fetchSize | 0 | JDBC fetch size. `0` uses the driver default. |
| reconnectAttempts | 30 | How many times in a row the source reconnects after a lost connection before it fails the replication. `0` disables reconnecting. |
| reconnectBackoffMs | 1000 | Delay, in milliseconds, before the first reconnect attempt. The delay doubles after each consecutive failure. |
| reconnectMaxBackoffMs | 60000 | Upper bound, in milliseconds, of the reconnect delay. It is at least `reconnectBackoffMs`. With the defaults, the source keeps trying for about 25 minutes. |
| watermarkFlushIntervalMs | 60000 | How often, in milliseconds, an idle table still records its position, so that a table without changes does not look expired after the retention period. |

{% hint style="info" %}
When the JDBC URL is built from `host`, `database`, and `port`, GridGain sets `encrypt=true;trustServerCertificate=true`. This encrypts the connection but does not validate the SQL Server certificate. To control the TLS behavior, pass an explicit `jdbcUrl` instead.
{% endhint %}

{% hint style="info" %}
The `password` is stored in plain text as part of the source definition; treat source definitions as sensitive.
{% endhint %}

### Create the GridGain 9 Sink

The `gridgain_9` sink writes changes into an existing local GridGain 9 table.

{% hint style="warning" %}
The `gridgain_9` sink does not create the destination table. The `--create-table-if-not-exists` sink option has no effect for this sink: the target table must already exist with a compatible schema before replication starts.
{% endhint %}

{% hint style="info" %}
Set `targetTable` to the qualified name of the destination table. It must differ from the source table's qualified name. If `targetTable` is omitted, it defaults to the source table name, and replication fails to start with a self-replication error.
{% endhint %}

```
cdc sink create --name gg9_sink --type gridgain_9 --parameters targetTable=PUBLIC.ACCOUNTS
```

Sink parameters:

| Parameter | Default | Description |
|---|---|---|
| targetTable | Source table name | Required in practice. Qualified name of the destination GridGain 9 table, which must differ from the source table's qualified name. If omitted, it defaults to the source table name and replication fails to start with a self-replication error. Use it to map the source table onto a differently named table, for example `dbo.ACCOUNTS` to `PUBLIC.ACCOUNTS`. |

### Create and Start Replication

```
cdc replication create --name mssql_to_gg9 --source mssql_source --sink gg9_sink --mode NEW_DATA
cdc replication start --name mssql_to_gg9
```

Both `NEW_DATA` and `ALL` modes are supported.

### Retention and Recovery

- The SQL Server CDC cleanup retention (`sys.sp_cdc_change_job @job_type = N'cleanup', @retention = <minutes>`, 3 days by default) limits how long a stopped replication can be resumed. A replication whose saved position is older than the oldest retained change fails with `GG-CDC-15`: the changes in between are lost. Delete and recreate the replication. In `ALL` mode it starts from a fresh snapshot, in `NEW_DATA` mode from the current position.
- A lost connection is re-established with an exponential backoff (see the `reconnect*` parameters). When the attempts are used up, the replication fails with `GG-CDC-16`.
- A restart during the initial `ALL`-mode snapshot starts the snapshot again. If the connection is lost after snapshot rows have already been replicated, the replication stops instead of delivering those rows twice; delete and recreate it.

### Schema Changes

The source reads the capture instance named `<schema>_<table>`, which is the SQL Server default name; a different name cannot be configured. SQL Server keeps a capture instance's column list fixed, so a schema change needs a new capture instance:

1. Stop the replication.
2. Change the source table.
3. Re-create the capture instance: run `sys.sp_cdc_disable_table` with `@capture_instance = N'<schema>_<table>'`, then `sys.sp_cdc_enable_table` with the default capture instance name.
4. Apply the same change to the destination GridGain 9 table.
5. Delete and recreate the replication. The saved position belongs to the old capture instance, so a resume fails with `GG-CDC-15`. Recreate it in `ALL` mode to copy the table again, or in `NEW_DATA` mode to continue from the current position without the changes made while it was stopped.

### Limitations

- Supported SQL Server types: `bit`, `tinyint`, `smallint`, `int`, `bigint`, `decimal`, `numeric`, `money`, `smallmoney`, `float`, `real`, `char`, `varchar`, `nchar`, `nvarchar`, `text`, `ntext`, `binary`, `varbinary`, `image`, `uniqueidentifier`, `date`, `time`, `datetime`, `datetime2`, `smalldatetime`, `datetimeoffset`, `rowversion`. A captured column of another type (for example `sql_variant` or `xml`) fails the replication at start. GridGain 9 stores time with microsecond precision: map `time(7)` and `datetime2(7)` to `TIME(6)` and `TIMESTAMP(6)` columns. A `datetimeoffset` value arrives as an instant in UTC (`TIMESTAMP WITH LOCAL TIME ZONE`).
- No metrics: lag, throughput and errors are visible only in the node logs.
- No backpressure: the source reads the next changes only after the sink has written the previous ones. A slow sink makes the lag grow; it does not fail the replication. Changes are read in chunks of up to 12288 rows or 16 MiB of row data, whichever comes first, and each chunk records its own position, so the memory a backlog needs does not grow with the backlog. One source transaction is never split: a transaction larger than both limits is held in memory whole. The initial snapshot is read in chunks of 1024 rows.
- One thread and one JDBC connection per replicated table. 100 tables per source were tested on one node.
- End-to-end lag has a floor set by the SQL Server capture job: about 4 to 8 seconds with the default job settings (`pollinginterval` of 5 seconds), about 2 to 3 seconds with a shorter `pollinginterval`. A `pollIntervalMs` below 1000 does not lower it.
- The source checks only that the connection parameters are present when it is created. A wrong host, database or table shows up when the replication starts.
- In `ALL` mode, the initial snapshot is not transactionally consistent with the start position for rows changed during the snapshot. Such rows converge when the incremental phase replays their changes.
- A paused or unresponsive SQL Server is not detected until its connection returns.
- Schema and DDL changes are not propagated; the destination table must exist with a compatible schema.
- In a mixed-version cluster, create `mssql` sources and `gridgain_9` sinks only after every node is upgraded. Older nodes cannot read the new source and sink types.

## Replicating from MariaDB

This section describes how to replicate changes from MariaDB tables into GridGain 9 tables. MariaDB acts as the CDC source: GridGain reads the row-based binary log, optionally after a consistent initial snapshot, and a GridGain 9 sink applies the changes to local tables. Inserts and updates are applied as upserts, and deletes remove the corresponding rows.

### Supported Configurations

| Area | Supported |
|---|---|
| MariaDB server | Validated with MariaDB 11.4.4. Other server versions are not validated. |
| Tables | InnoDB tables with a primary key. |
| Column types | Signed `INT` and `VARCHAR` with the `utf8mb3` or `utf8mb4` character set. Create the matching GridGain 9 columns as `INT` and `VARCHAR`. A table with any other column type, including unsigned integers, cannot be replicated. |
| Replication modes | `NEW_DATA` and `ALL`. |
| Delivery | At least once. After a failure, the last batch can be applied again; because changes are applied as upserts and deletes, the target table converges. |

### Prerequisites

Configure MariaDB with a row-based binary log and restart the server:

```ini
[mariadb]
server_id=1
log_bin=mysql-bin
binlog_format=ROW
binlog_row_image=FULL
binlog_expire_logs_seconds=604800
```

Keep binary logs longer than the longest planned outage of the replication plus its lag. If MariaDB purges the binary log file that holds the saved position, the replication fails and must be recreated.

Create an account for GridGain. `RELOAD` is needed only for the short global read lock that makes an `ALL` snapshot consistent with the start of streaming. `REPLICATION CLIENT` is accepted instead of `BINLOG MONITOR`.

```sql
CREATE USER 'gg_cdc'@'%' IDENTIFIED BY '<password>';
GRANT SELECT, RELOAD, REPLICATION SLAVE, BINLOG MONITOR ON *.* TO 'gg_cdc'@'%';
```

Creating a source does not connect to MariaDB, and starting a replication does not check these prerequisites. Before starting a replication, run `cdc source status --name <source_name>`: it checks the parameters, the connection, `binlog_format`, `binlog_row_image`, the account privileges, and the storage engine, column types and character sets of every table, and explains how to fix each failed check.

### Create the MariaDB Source

```
cdc source create --name mariadb_source --type mariadb --tables sales.orders \
  --parameters host=db.example.com --parameters database=sales \
  --parameters user=gg_cdc --parameters password=<password>
```

Specify each table as `<database>.<table>`. If the database part is omitted, the `database` parameter is used.

Source parameters:

| Parameter | Default | Description |
|---|---|---|
| host | localhost | MariaDB host. The binary log is always read from `host` and `port`. |
| port | 3306 | MariaDB port. |
| database |  | Required. Default database for tables listed without a database name. |
| user |  | Required. MariaDB account with the privileges listed above. |
| password |  | Required. Password of the MariaDB account. |
| jdbcUrl |  | Optional JDBC URL for metadata and snapshot reads, for example to set TLS options. It does not change the binary log connection. |
| batchSize | 1000 | Maximum number of rows in a batch. A single MariaDB transaction that changes more rows than this fails the replication; raise the value for larger transactions. |
| reconnectAttempts | 30 | Number of reconnect attempts after the binary log connection drops. When they are exhausted, the replication fails. |
| reconnectBackoffMs | 1000 | Initial delay between reconnect attempts, in milliseconds. The delay doubles after each attempt. |
| reconnectMaxBackoffMs | 60000 | Maximum delay between reconnect attempts, in milliseconds. |
| serverId | Random value between 1000000 and 3999999999 | Replica server ID used for the binary log connection. Each replicated table uses its own connection with the next consecutive ID. The IDs must not clash with other replicas of the same MariaDB server. |

{% hint style="info" %}
The `password` is stored in plain text as part of the source definition; treat source definitions as sensitive.
{% endhint %}

### Create the Sink and Start Replication

Create a `gridgain_9` sink as described in [Create the GridGain 9 Sink](#create-the-gridgain-9-sink), then create and start the replication:

```
cdc sink create --name gg9_sink --type gridgain_9 --parameters targetTable=PUBLIC.ORDERS
cdc replication create --name mariadb_to_gg9 --source mariadb_source --sink gg9_sink --mode ALL
cdc replication start --name mariadb_to_gg9
```

In `ALL` mode, GridGain holds a global read lock only while it starts a repeatable-read transaction and records the binary log position, then scans the table in primary key order without the lock, and streams changes from the recorded position. Changes committed during the scan are therefore neither lost nor missed. In `NEW_DATA` mode, streaming starts at the current binary log position.

### Recovery

GridGain saves the binary log position after the sink applies each batch. After a lost connection, a MariaDB restart, or a GridGain node restart, the replication resumes from the last saved position, so changes made while it was stopped are replicated. If an `ALL` snapshot is interrupted, it is restarted, and changes are replayed from the position of the first snapshot attempt. Rolled-back transactions are not replicated.

The replication never skips to the current binary log position. If the saved file has been purged, the replication fails; restore the binary logs or recreate the replication.

### Limitations

- Schema and DDL changes are not propagated. Do not change the schema of a replicated table while its replication is running.
- Recovery uses binary log file positions of the original MariaDB server. GTID-based failover to another server is not supported.
- Each replicated table uses its own binary log connection.
- In a mixed-version cluster, create `mariadb` sources only after every node is upgraded. Older nodes cannot read the new source type.
