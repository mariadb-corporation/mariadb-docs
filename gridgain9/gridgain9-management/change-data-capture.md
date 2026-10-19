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
| type |  | Data source type. Supported values: `gridgain`, `mssql`. |
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
| type |  | Data sink type. Supported values: `iceberg`; `gridgain_9` (experimental, requires `--experimental`). |
| parameters |  | Optional additional parameters. Specific list of parameters depends on the type of the data sink. For Iceberg data sink, [Iceberg](https://iceberg.apache.org/docs/latest/configuration/#table-properties) configuration properties are supported. |
| create-table-if-not-exists | true | Optional. If `true`, missing tables are automatically created in the sink before replication starts. Has no effect for the `gridgain_9` sink, which requires the destination table to already exist. |
| experimental | false | Optional. Enables experimental sink types, such as `gridgain_9`. Creating or updating a sink with an experimental type fails unless this flag is set. |

Below is an example of a CDC data sink:

```
cdc sink create --name iceberg_sink --type iceberg --parameters "catalog.type"="iceberg" --parameters "catalog.warehouse"="s3://my-bucket/my/key/prefix" --parameters "catalog-impl"="org.apache.iceberg.aws.glue.GlueCatalog" --parameters "io-impl"="org.apache.iceberg.aws.s3.S3FileIO" --parameters "s3.access-key-id"="my-secret-key-id" --parameters "s3.secret-access-key"="my-secret-access-key"
```

### Updating CDC Sink

You can update the CDC sink when the relevant replication is not running by using the `cdc sink update` command. The command uses the same arguments as the `cdc sink create` command, including `--experimental`: updating a sink that uses an experimental type, such as `gridgain_9`, also requires the `--experimental` flag. For example:

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
| execution-nodes |  | The list of nodes that will be used to run replication. If not specified, the node the command is executed on is used. |

{% hint style="info" %}
A `gridgain` source supports only `NEW_DATA` mode. `ALL` mode, which first replicates existing data and then switches to new changes, is available only for external sources such as `mssql`. Starting a replication that uses a `gridgain` source in `ALL` mode fails.
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

If at any point the node executing replication leaves the cluster, the replication process will automatically be transferred to a different node from the list specified in the `execution-nodes` parameter. If none of the specified nodes are available in the cluster, replication will fail.

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

{% hint style="warning" %}
The GridGain 9 CDC sink (`gridgain_9`) used in this section is an experimental feature. It may change significantly in later releases. The Microsoft SQL Server CDC source (`mssql`) is not experimental.
{% endhint %}

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
| captureInstance.&lt;schema&gt;.&lt;table&gt; | `<schema>_<table>` | The capture instance to read for the table, for example `captureInstance.dbo.ACCOUNTS=dbo_ACCOUNTS_v2`. The table is matched ignoring case and must be one of the source's tables. Used for the two-instance hand-over of a [schema change](#schema-changes). |

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

Because the `gridgain_9` sink type is experimental, you must pass the `--experimental` flag. Without it, the command is rejected with `GRIDGAIN_9 sink is experimental; pass the --experimental flag to enable it.`

```
cdc sink create --name gg9_sink --type gridgain_9 --parameters targetTable=PUBLIC.ACCOUNTS --experimental
```

Sink parameters:

| Parameter | Default | Description |
|---|---|---|
| targetTable | Source table name | Required in practice. Qualified name of the destination GridGain 9 table, which must differ from the source table's qualified name. If omitted, it defaults to the source table name and replication fails to start with a self-replication error. Use it to map the source table onto a differently named table, for example `dbo.ACCOUNTS` to `PUBLIC.ACCOUNTS`. |
| unmappedFieldPolicy | `FAIL` | What happens to a source column the destination table does not have. `FAIL` refuses to start the replication. `IGNORE` drops the column from every row and keeps it once the destination table gains the column. A primary-key column is never dropped. The same policy governs the GridGain Kafka Connect sink. |

When the replication starts, the sink compares the columns of the capture instance with the destination table and fails the start with a message naming every mismatch, rather than failing on the first row: a column the destination lacks (under `FAIL`), a primary key made of different columns, a type the destination column does not accept, a nullable source column going into a `NOT NULL` destination column, or a `NOT NULL` destination column the source does not deliver. Integer and floating-point source values are accepted by a wider destination column; a narrower one is a mismatch.

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

SQL Server keeps a capture instance's column list fixed, so a schema change needs a new capture instance. SQL Server supports two capture instances per table for exactly this: the DBA creates the second instance while the first still captures, and the consumer moves from one to the other. The replication follows the same hand-over, so the source table keeps taking writes throughout and the destination table is changed when you are ready. The saved position survives the switch, because it is kept per replication and table.

To add a column to `dbo.ACCOUNTS` replicated by the source `mssql_source` into `PUBLIC.ACCOUNTS`:

1. Create the sink with `unmappedFieldPolicy=IGNORE`, or update it to that value, so that the new column is dropped until the destination table has it. With the default `FAIL`, step 4 refuses to start the replication until step 5 is done; do step 5 first in that case.
2. Change the source table and create the second capture instance. Both instances capture from here on; the replication keeps reading the first one.
   ```sql
   ALTER TABLE dbo.ACCOUNTS ADD EMAIL NVARCHAR(64) NULL;
   EXEC sys.sp_cdc_enable_table @source_schema = N'dbo', @source_name = N'ACCOUNTS',
       @role_name = NULL, @supports_net_changes = 0, @capture_instance = N'dbo_ACCOUNTS_v2';
   GRANT SELECT ON cdc.fn_cdc_get_all_changes_dbo_ACCOUNTS_v2 TO replicator;
   ```
3. Wait until the replication has read the first instance past the second one's start: any change to the table after step 2, or one `watermarkFlushIntervalMs` on an idle table, is enough.
4. Move the replication to the second instance. `cdc source update` takes the same arguments as `cdc source create`, plus the capture instance:
   ```
   cdc replication stop --name mssql_to_gg9
   cdc source update --name mssql_source --type mssql --tables dbo.ACCOUNTS \
     --parameters jdbcUrl="jdbc:sqlserver://localhost:1433;databaseName=testdb;encrypt=true;trustServerCertificate=true" \
     --parameters user=replicator --parameters password=<password> \
     --parameters captureInstance.dbo.ACCOUNTS=dbo_ACCOUNTS_v2
   cdc replication start --name mssql_to_gg9
   ```
   The replication resumes from its saved position on the second instance. Rows written since the stop arrive with the new column, which the sink drops until step 5.
5. Add the column to the destination table. The sink keeps it from the next batch on; rows replicated before this step do not get the column.
   ```sql
   ALTER TABLE PUBLIC.ACCOUNTS ADD COLUMN EMAIL VARCHAR;
   ```
6. Drop the first capture instance once nothing reads it: `EXEC sys.sp_cdc_disable_table @source_schema = N'dbo', @source_name = N'ACCOUNTS', @capture_instance = N'dbo_ACCOUNTS';`.

If step 4 runs before the replication has read the first instance past the second one's start, the start fails with a message naming both instances and both positions: the changes in between exist on the first instance only. Set the parameter back to the first instance, start the replication, and switch again once its position has passed the start of the second instance. A switch to an instance SQL Server does not know fails naming the instance.

To drop or retype a column, use the same hand-over: the second capture instance is created after the source table change, and the destination table is changed when the replication has moved. A dropped source column leaves the destination column `NULL` in later rows if it is nullable; a `NOT NULL` destination column the source no longer delivers fails the start.

### Limitations

- Supported SQL Server types: `bit`, `tinyint`, `smallint`, `int`, `bigint`, `decimal`, `numeric`, `money`, `smallmoney`, `float`, `real`, `char`, `varchar`, `nchar`, `nvarchar`, `text`, `ntext`, `binary`, `varbinary`, `image`, `uniqueidentifier`, `date`, `time`, `datetime`, `datetime2`, `smalldatetime`, `datetimeoffset`, `rowversion`. A captured column of another type (for example `sql_variant` or `xml`) fails the replication at start. GridGain 9 stores time with microsecond precision: map `time(7)` and `datetime2(7)` to `TIME(6)` and `TIMESTAMP(6)` columns. A `datetimeoffset` value arrives as an instant in UTC (`TIMESTAMP WITH LOCAL TIME ZONE`).
- No metrics: lag, throughput and errors are visible only in the node logs.
- No backpressure: the source reads the next changes only after the sink has written the previous ones. A slow sink makes the lag grow; it does not fail the replication. Changes are read in chunks of up to 12288 rows or 16 MiB of row data, whichever comes first, and each chunk records its own position, so the memory a backlog needs does not grow with the backlog. One source transaction is never split: a transaction larger than both limits is held in memory whole. The initial snapshot is read in chunks of 1024 rows.
- One thread and one JDBC connection per replicated table. 100 tables per source were tested on one node.
- End-to-end lag has a floor set by the SQL Server capture job: about 4 to 8 seconds with the default job settings (`pollinginterval` of 5 seconds), about 2 to 3 seconds with a shorter `pollinginterval`. A `pollIntervalMs` below 1000 does not lower it.
- The source checks only that the connection parameters are present when it is created. A wrong host, database or table shows up when the replication starts.
- In `ALL` mode, the initial snapshot is not transactionally consistent with the start position for rows changed during the snapshot. Such rows converge when the incremental phase replays their changes.
- A paused or unresponsive SQL Server is not detected until its connection returns.
- Schema and DDL changes are not propagated; the destination table must exist with a compatible schema, and a schema change follows the capture-instance hand-over described above.
- In a mixed-version cluster, create `mssql` sources and `gridgain_9` sinks only after every node is upgraded. Older nodes cannot read the new source and sink types.
