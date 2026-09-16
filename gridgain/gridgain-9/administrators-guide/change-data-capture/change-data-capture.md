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
| type |  | Data source type. Supported values: `gridgain`; `mssql` (experimental, requires `--experimental`). |
| tables |  | Comma-separated list of tables that will be replicated. |
| parameters |  | Optional additional parameters. Currently, the following parameters are supported:<br>- page-size - the size of each page sent via replication.<br>- poll-interval - the interval at which GridGain checks for updates in source tables. |
| experimental | false | Optional. Enables experimental source types, such as `mssql`. Creating or updating a source with an experimental type fails unless this flag is set. |

Below is an example of a CDC data source:

```
cdc source create --name gridgain_source --type gridgain --tables PUBLIC.MY_TABLE1 --parameters "poll-interval-ms"=1000 --parameters "page-size"=1024
```

### Updating CDC Source

You can update the CDC source when the relevant replication is not running by using the `cdc source update` command. The command uses the same arguments as the `cdc source create` command, including `--experimental`: updating a source that uses an experimental type, such as `mssql`, also requires the `--experimental` flag. For example:

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

## Replicating from Microsoft SQL Server (Experimental)

{% hint style="warning" %}
The Microsoft SQL Server CDC source and the GridGain 9 CDC sink are experimental features. They may change significantly in later releases.
{% endhint %}

This section describes how to replicate changes from a Microsoft SQL Server database into GridGain 9 tables. SQL Server acts as the CDC source, and a GridGain 9 sink lands the changes in local tables: inserts and updates are applied as upserts, and deletes remove the corresponding rows.

### Prerequisites

- Native CDC must be enabled on the SQL Server database and on each replicated table (capture instances).
- The destination GridGain 9 table must already exist with a schema compatible with the source rows (matching column names and types). Schema changes are not propagated automatically.

### Create the SQL Server Source

Because the `mssql` source type is experimental, you must pass the `--experimental` flag. Without it, the command is rejected with `MSSQL source is experimental; pass the --experimental flag to enable it.`

```
cdc source create --name mssql_source --type mssql --tables dbo.ACCOUNTS \
  --parameters jdbcUrl="jdbc:sqlserver://localhost:1433;databaseName=testdb;encrypt=true;trustServerCertificate=true" \
  --parameters user=sa --parameters password=<password> \
  --experimental
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

### Create and Start Replication

```
cdc replication create --name mssql_to_gg9 --source mssql_source --sink gg9_sink --mode NEW_DATA
cdc replication start --name mssql_to_gg9
```

Both `NEW_DATA` and `ALL` modes are supported.

### Limitations

- Type mapping covers common SQL Server types (integers, strings, decimals, booleans, dates and times). Other types are not yet mapped.
- In `ALL` mode, the initial snapshot is not transactionally consistent with the start position for rows changed during the snapshot.
- Connectivity and CDC-enablement are not deeply validated when the source is created.
- Schema and DDL changes are not propagated; the destination table must exist with a compatible schema.
- In a mixed-version cluster, create `mssql` sources and `gridgain_9` sinks only after every node is upgraded. Older nodes cannot read the new source and sink types.
