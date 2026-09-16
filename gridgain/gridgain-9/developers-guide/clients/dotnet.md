---
description: >-
  Connect to a GridGain 9 cluster with the .NET client, covering configuration,
  authentication, the SQL and table APIs, transactions, data streaming, metrics,
  logging, and object mapping.
---

# .NET Client

GridGain 9 clients connect to the cluster via a standard socket connection. Unlike GridGain 2.x, there is no separate Thin and Thick clients in GridGain 9. All clients are 'thin'.

Clients do not become a part of the cluster topology, never hold any data, and are not used as a destination for compute calculations.

## Getting Started

### Prerequisites

To use C# client, .NET 8.0 or newer is required.

### Installation

C# client is available via NuGet. To add it, use the `add package` command:

```bash
dotnet add package GridGain.Ignite --version 9.1
```

## Connecting to Cluster

To initialize a client, use the `IgniteClient` class, and provide it with the configuration:

{% code title=".NET" %}
```csharp
var clientCfg = new IgniteClientConfiguration
{
  Endpoints = { "127.0.0.1" }
};
using var client = await IgniteClient.StartAsync(clientCfg);
```
{% endcode %}

## Cluster API

The cluster API lets you inspect the cluster topology, access it through the `IIgnite.Cluster` property:

- `Cluster.GetNodesAsync()` returns all nodes that are part of the [logical topology](../../administrators-guide/lifecycle.md#logical-and-physical-topology).
- `Cluster.LocalNode` returns the local cluster node. On the client side it is `null`; it is populated only when accessed from server-side code inside a [compute job](../compute/compute.md) (`IJobExecutionContext.Ignite`) or a [data streamer receiver](../data-streamer.md) (`IDataStreamerReceiverContext.Ignite`),  where it identifies the node executing that code.

Each `IClusterNode` exposes its `Id` (a `Guid` that changes after a node restart), `Name` (the consistent ID, stable across restarts), and `Address`.

```csharp
using var client = await IgniteClient.StartAsync(clientCfg);

// Get all nodes in the logical topology.
IList<IClusterNode> nodes = await client.Cluster.GetNodesAsync();

foreach (IClusterNode node in nodes)
{
    Console.WriteLine($"{node.Name} @ {node.Address}");
}
```

{% hint style="info" %}
The older `IIgnite.GetClusterNodesAsync()` method is obsolete. Use `Cluster.GetNodesAsync()` instead.
{% endhint %}

## Client Configuration

### SQL Partition Awareness

The .NET client supports SQL partition awareness, which improves query performance by routing requests directly to the nodes that hold the relevant data. This feature is controlled by the `SqlPartitionAwarenessMetadataCacheSize` configuration property.

{% code title=".NET" %}
```csharp
var cfg = new IgniteClientConfiguration
{
    Endpoints = { "127.0.0.1" },
    SqlPartitionAwarenessMetadataCacheSize = 1024 // Default value
};
using var client = await IgniteClient.StartAsync(cfg);
```
{% endcode %}

| Property | Description |
| --- | --- |
| SqlPartitionAwarenessMetadataCacheSize | Maximum number of SQL partition awareness metadata entries to cache. Default is `1024`. Set to `0` to disable SQL partition awareness. |

The client builds a metadata cache during the initial query execution and uses this cache to optimize subsequent queries. Metadata is available for queries with equality predicates over all colocation columns.

## Authentication

To pass authentication information, pass it to `IgniteClient` builder:

{% code title=".NET" %}
```csharp
var cfg = new IgniteClientConfiguration("127.0.0.1:10800")
{
	Authenticator = new BasicAuthenticator
	{
		Username = "myUser",
		Password = "myPassword"
	}
};
IIgniteClient client = await IgniteClient.StartAsync(cfg);
```
{% endcode %}

### Limitations

There are limitations to user types that can be used for such a mapping. Some limitations are common, and others are platform-specific due to the programming language used.

- Only flat field structure is supported, meaning no nesting user objects. This is because Ignite tables, and therefore tuples have flat structure themselves;
- Fields should be mapped to Ignite types;
- All fields in user type should either be mapped to Table column or explicitly excluded;
- All columns from Table should be mapped to some field in the user type;
- **.NET only**: Any type (class, struct, record) is supported as long as all fields can be mapped to Ignite types;

### Usage Examples

{% code title=".NET" %}
```csharp
public class Account
{
  public long Id { get; set; }
  public long Balance { get; set; }

  [NotMapped]
  public Guid UnmappedId { get; set; }
}
```
{% endcode %}

## SQL API

GridGain 9 is focused on SQL, and SQL API is the primary way to work with the data. You can read more about supported SQL statements in the [SQL Reference](../../sql-reference/ddl.md) section. Here is how you can send SQL requests:

{% code title=".NET" %}
```csharp
IResultSet<IIgniteTuple> resultSet = await client.Sql.ExecuteAsync(transaction: null, "select name from tbl where id = ?", 42);
List<IIgniteTuple> rows = await resultSet.ToListAsync();
IIgniteTuple row = rows.Single();
Debug.Assert(row["name"] as string == "John Doe");
```
{% endcode %}

You can also use an explicit `IMapper<T>` interface to enable strongly typed SQL results without relying on tuple-based or reflection-based mapping:

{% code title=".NET" %}
```csharp
public sealed class MyRecordMapper : IMapper<Record> {}

IResultSet<MyRow> resultSet = await client.Sql.ExecuteAsync(
    transaction: null,
    mapper: new MyRecordMapper(),
    statement: "select name from tbl where id = ?",
    CancellationToken.None,
    42);

List<MyRecord> rows = await resultSet.ToListAsync();
```
{% endcode %}

### Batch SQL Execution

You can execute the specified DML statement once for each set of arguments and return the number of affected rows for each execution.

{% hint style="info" %}
Only `INSERT`, `UPDATE`, `DELETE` statements are supported.
{% endhint %}

To run a batch execution, you need to implement `ExecuteBatchAsync()` method with the following parameters:

```csharp
Task<long[]> ExecuteBatchAsync(
    ITransaction? transaction,
    SqlStatement statement,
    IEnumerable<IEnumerable<object?>> args,
    CancellationToken cancellationToken = default
);
```

#### Parameters

- `transaction` - The optional transaction in which to execute the batch.
- `statement` -  The SQL statement to execute for each entry in `args`.
- `args` - A collection of argument lists. The statement will be executed once per inner collection. Must not be empty or contain empty rows.
- `cancellationToken` - Token for cancelling the operation.

#### Example

In this example we return an array of update counts.
Each element corresponds to the number of rows affected by the statement execution for the matching entry in `args`. The length of the returned array equals the number of argument sets.

```csharp
long[] res = await sql.ExecuteBatchAsync(
    transaction: null,
    statement: "INSERT INTO Person (Id, Name) VALUES (?, ?)",
    args:
    [
        [1, "Alice"],
        [2, "Bob" ],
        [3, "Charlie"]
    ]
);
// res => [1, 1, 1]
```

#### Error Handling

If a batch execution fails, a `SqlBatchException` is thrown. The `UpdateCounters` property contains the number of rows affected by each statement that executed successfully before the failure, in the same order as the batch commands. Use it to determine which operations completed before the error occurred.

```csharp
try
{
    await Client.Sql.ExecuteBatchAsync(null, sql, args);
}
catch (SqlBatchException ex)
{
    // Check which operations succeeded before the error
    Console.WriteLine($"Succeeded: {ex.UpdateCounters.Count} operations");
    foreach (var count in ex.UpdateCounters)
    {
        Console.WriteLine($"Rows affected: {count}");
    }
}
```

### SQL Scripts

The default API executes SQL statements one at a time. If you want to execute large SQL statements, pass them to the `executeScript()` method. These statements will be executed in order.

{% code title=".NET" %}
```csharp
string script =
    "CREATE TABLE IF NOT EXISTS Person (id int primary key, city_id int, name varchar, age int, company varchar);" +
    "INSERT INTO Person (1,3, 'John', 43, 'Sample')";

await Client.Sql.ExecuteScriptAsync(script);
```
{% endcode %}

{% hint style="info" %}
Execution of each statement is considered complete when the first page is ready to be returned. As a result, when working with large data sets, `SELECT` statement may be affected by later statements in the same script.
{% endhint %}

### SQL Partition Awareness Configuration

SQL partition awareness optimizes query performance by routing SQL queries directly to the server nodes that hold the relevant data. This feature is enabled by default and can be configured using the `SqlPartitionAwarenessMetadataCacheSize` property.

To configure the partition awareness cache size:

{% code title=".NET" %}
```csharp
var cfg = new IgniteClientConfiguration
{
    Endpoints = { "127.0.0.1" },
    // Cache up to 2048 unique query patterns
    SqlPartitionAwarenessMetadataCacheSize = 2048
};

using var client = await IgniteClient.StartAsync(cfg);

// Queries are automatically routed when possible
await using var resultSet = await client.Sql.ExecuteAsync(
    transaction: null,
    statement: "SELECT * FROM Reservations WHERE floor_no = ?",
    args: 5);
```
{% endcode %}

To disable SQL partition awareness, set the cache size to zero:

```csharp
var cfg = new IgniteClientConfiguration
{
    SqlPartitionAwarenessMetadataCacheSize = 0 // Disable
};
```

{% hint style="info" %}
The cache is keyed by `(schema, query)` pairs. Each unique query pattern requires a separate cache entry. Queries with different parameter values but the same structure share the same cache entry.
{% endhint %}

## Transactions

All table operations in GridGain 9 are transactional. You can provide an explicit transaction as a first argument of any Table and SQL API call. If you do not provide an explicit transaction, an implicit one will be created for every call.

Here is how you  can provide a transaction explicitly:

{% code title=".NET" %}
```csharp
var accounts = table.GetKeyValueView<long, Account>();
await accounts.PutAsync(transaction: null, 42, new Account(16_000));

await using ITransaction tx = await client.Transactions.BeginAsync();

(Account account, bool hasValue) = await accounts.GetAsync(tx, 42);
account = account with { Balance = account.Balance + 500 };

await accounts.PutAsync(tx, 42, account);

Debug.Assert((await accounts.GetAsync(tx, 42)).Value.Balance == 16_500);

await tx.RollbackAsync();

Debug.Assert((await accounts.GetAsync(null, 42)).Value.Balance == 16_000);

public record Account(decimal Balance);
```
{% endcode %}

## Table API

To execute table operations on a specific table, you need to get a specific view of the table and use one of its methods. You can only create new tables by using SQL API.

When working with tables, you can use built-in IgniteTuple type, which is a set of key-value pairs underneath, or map the data to your own types for a strongly-typed access. Here is how you can work with tables:

### Getting a Table Instance

To obtain an instance of a table, use the `ITables.GetTableAsync(string name)` You can also use `ITables.GetTablesAsync` method to list all existing tables.

{% code title=".NET" %}
```csharp
var existingTables = await Client.Tables.GetTablesAsync();
var firstTable = existingTables[0];

var myTable = await Client.Tables.GetTableAsync("MY_TABLE");
```
{% endcode %}

### Basic Table Operations

Once you've got a table you need to get a specific view to choose how you want to operate table records.

#### Tuple Record View

A tuple record view. It can be used to operate table tuples directly.

{% code title=".NET" %}
```csharp
IRecordView<IIgniteTuple> view = table.RecordBinaryView;

IIgniteTuple fullRecord = new IgniteTuple
{
  ["id"] = 42,
  ["name"] = "John Doe"
};

await view.UpsertAsync(transaction: null, fullRecord);

IIgniteTuple keyRecord = new IgniteTuple { ["id"] = 42 };
(IIgniteTuple value, bool hasValue) = await view.GetAsync(transaction: null, keyRecord);

Debug.Assert(hasValue);
Debug.Assert(value.FieldCount == 2);
Debug.Assert(value["id"] as int? == 42);
Debug.Assert(value["name"] as string == "John Doe");
```
{% endcode %}

#### Record View

A record view mapped to a user type. It can be used to operate table using user objects which are mapped to table tuples.

{% code title=".NET" %}
```csharp
var pocoView = table.GetRecordView<Poco>();

await pocoView.UpsertAsync(transaction: null, new Poco(42, "John Doe"));
var (value, hasValue) = await pocoView.GetAsync(transaction: null, new Poco(42));

Debug.Assert(hasValue);
Debug.Assert(value.Name == "John Doe");

public record Poco(long Id, string? Name = null);
```
{% endcode %}

#### Key-Value Tuple View

A tuple key-value view. It can be used to operate table using key and value tuples separately.

{% code title=".NET" %}
```csharp
IKeyValueView<IIgniteTuple, IIgniteTuple> kvView = table.KeyValueBinaryView;

IIgniteTuple key = new IgniteTuple { ["id"] = 42 };
IIgniteTuple val = new IgniteTuple { ["name"] = "John Doe" };

await kvView.PutAsync(transaction: null, key, val);
(IIgniteTuple? value, bool hasValue) = await kvView.GetAsync(transaction: null, key);

Debug.Assert(hasValue);
Debug.Assert(value.FieldCount == 1);
Debug.Assert(value["name"] as string == "John Doe");
```
{% endcode %}

#### Key-Value View

A key-value view with user objects. It can be used to operate table using key and value user objects mapped to table tuples.

{% code title=".NET" %}
```csharp
IKeyValueView<long, Poco> kvView = table.GetKeyValueView<long, Poco>();

await kvView.PutAsync(transaction: null, 42, new Poco(Id: 0, Name: "John Doe"));
(Poco? value, bool hasValue) = await kvView.GetAsync(transaction: null, 42);

Debug.Assert(hasValue);
Debug.Assert(value.Name == "John Doe");

public record Poco(long Id, string? Name = null);
```
{% endcode %}

### Partition Management

Using an `IMapper<T>` to get partitions allows the client to compute the partition deterministically without reflection and is required for POCO keys in AOT and other no-reflection scenarios.

```csharp
public sealed class Poco
{
    public long Key { get; set; }
}

public sealed class PocoMapper : IMapper<Poco>
{
    public void Write(Poco obj, ref RowWriter rowWriter, IMapperSchema schema) =>
        rowWriter.WriteLong(obj.Key);

    public Poco Read(ref RowReader rowReader, IMapperSchema schema) =>
        new() { Key = rowReader.ReadLong()!.Value };
}

ITable table = (await client.Tables.GetTableAsync("PUBLIC.MY_TABLE"))!;
IPartitionManager pm = table.PartitionManager;

var partition = await pm.GetPartitionAsync(null, new Poco { Key = 42L }, new PocoMapper());
```

## Streaming Data

To stream a large amount of data, use the data streamer. Data streaming provides a quicker and more efficient way to load, organize and optimally distribute your data. Data streamer accepts a stream of data and distributes data entries across the cluster, where the processing takes place. Data streaming is available in all table views.

![](../../../.gitbook/assets/gg9-developers-guide-data_streaming.png)

Data streaming provides at-least-once delivery guarantee.

### Using Data Streamer API

{% code title=".NET" %}
```csharp
    var options = DataStreamerOptions.Default with { PageSize = 10 };
    var data = Enumerable.Range(0, Count).Select(x => new IgniteTuple { ["id"] = 1L, ["name"] = "foo" }).ToList();

    await TupleView.StreamDataAsync(data.ToAsyncEnumerable(), options);
```
{% endcode %}

## Client Metrics

Metrics are exposed by the .NET client through the `System.Diagnostics.Metrics` API with the `Apache.Ignite` meter name. For example, here is how you can access GridGain metrics by using the [dotnet-counters](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/dotnet-counters) tool:

```bash
dotnet-counters monitor --counters Apache.Ignite,System.Runtime --process-id PID
```

You can also get metrics in your code by creating a listener:

```csharp
var listener = new MeterListener();
listener.InstrumentPublished = (instrument, meterListener) =>
{
    if (instrument.Meter.Name == "Apache.Ignite")
    {
        meterListener.EnableMeasurementEvents(instrument);
    }
};
listener.SetMeasurementEventCallback<int>(
    (instrument, measurement, tags, state) => Console.WriteLine($"{instrument.Name}: {measurement}"));

listener.Start();
```

### Available .NET Metrics

| Metric name | Description |
| --- | --- |
| connections-active | The number of currently active connections. |
| connections-established | The number of established connections. |
| connections-lost | The number of connections lost. |
| connections-lost-timeout | The number of connections lost due to a timeout. |
| handshakes-failed | The number of failed handshakes. |
| handshakes-failed-timeout | The number of handshakes that failed due to a timeout. |
| requests-active | The number of currently active requests. |
| requests-sent | The number of requests sent. |
| requests-completed | The number of completed requests. Requests are completed once a response is received. |
| requests-retried | The number of request retries. |
| requests-failed | The number of failed requests. |
| bytes-sent | The amount of bytes sent. |
| bytes-received | The amount of bytes received. |
| streamer-batches-sent | The number of data streamer batches sent. |
| streamer-items-sent | The number of data streamer items sent. |
| streamer-batches-active | The number of existing data streamer batches. |
| streamer-items-queued | The number of queued data streamer items. |

## Logging

To enable logging, set the `IgniteClientConfiguration.LoggerFactory` property to an instance of the `Microsoft.Extensions.Logging.ILoggerFactory` standard API.
See [Standard logging in .NET](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging) to learn more.

### Examples

The example below shows how you can configure logging to console with the `Microsoft.Extensions.Logging.Console` package:

{% code title=".NET" %}
```csharp
var cfg = new IgniteClientConfiguration
{
    LoggerFactory = LoggerFactory.Create(builder => builder.AddConsole().SetMinimumLevel(LogLevel.Debug))
};
```
{% endcode %}

Alternatively, here is how to configure logging with [Serilog](https://serilog.net/) by using `Serilog.Extensions.Logging` and `Serilog.Sinks.Console` packages:

{% code title=".NET" %}
```csharp
var cfg = new IgniteClientConfiguration
{
    LoggerFactory = LoggerFactory.Create(builder =>
        builder.AddSerilog(new LoggerConfiguration()
            .MinimumLevel.Debug()
            .WriteTo.Console()
            .CreateLogger()))
};
```
{% endcode %}

## Custom Object Mapping

Ignite provides basic object mapping for table rows and SQL query results in the following APIs:

- `ITable.GetRecordView<T>`
- `ITable.GetKeyValueView<TK, TV>()`
- `ISql.ExecuteAsync<T>`
- `IJobTarget<TKey>.Colocated<TKey>()`
- `IPartitionManager.GetPartitionAsync();`

Mappers are generated at runtime with the use of reflection and IL emit. Mapped properties and fields can be customized with [ColumnAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.schema.columnattribute?view=net-10.0) and excluded with [NotMappedAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.schema.notmappedattribute?view=net-10.0).

For advanced mapping scenarios and environments where reflection is limited (such as NativeAOT), you can implement the `IMapper<T>` interface.

### Record View Mapper

For record views, implement the `IMapper<T>` interface:

```csharp
public class PocoMapper : IMapper<Poco>
{
    public void Write(Poco obj, ref RowWriter rowWriter, IMapperSchema schema)
    {
        rowWriter.WriteLong(obj.Key);
        if (schema.Columns.Count > 1)
        {
            rowWriter.WriteString(obj.Val);
        }
    }

    public Poco Read(ref RowReader rowReader, IMapperSchema schema)
    {
        return new Poco
        {
            Key = rowReader.ReadLong()!.Value,
            Val = schema.Columns.Count > 1 ? rowReader.ReadString() : null
        };
    }
}
```

Then use the mapper when creating a record view:

```csharp
IRecordView<Poco> recordView = table.GetRecordView(new PocoMapper());
```

### Key-Value View Mapper

For key-value views, implement a mapper for `KeyValuePair<TK, TV>`:

```csharp
public class KeyValPocoMapper : IMapper<KeyValuePair<KeyPoco, ValPoco>>
{
    public void Write(KeyValuePair<KeyPoco, ValPoco> obj, ref RowWriter rowWriter, IMapperSchema schema)
    {
        rowWriter.WriteLong(obj.Key.Key);

        if (schema.Columns.Count > 1)
        {
            rowWriter.WriteString(obj.Value.Val);
        }
    }

    public KeyValuePair<KeyPoco, ValPoco> Read(ref RowReader rowReader, IMapperSchema schema)
    {
        var key = new KeyPoco
        {
            Key = rowReader.ReadLong()!.Value
        };

        var val = schema.Columns.Count > 1
            ? new ValPoco
            {
                Val = rowReader.ReadString()
            }
            : null;

        return new KeyValuePair<KeyPoco, ValPoco>(key, val!);
    }
}
```

Then use the mapper when creating a key-value view:

```csharp
IKeyValueView<KeyPoco, ValPoco> kvView = table.GetKeyValueView(new KeyValPocoMapper());
```

### Schema-Aware Mapping

The `IMapper<T>` interface provides two approaches for mapping objects to rows, depending on whether the schema is known at compile time.

#### Static Schema Mapping

When the exact table schema is known at compile time, you can write columns directly in the correct order. This approach provides the best performance by avoiding column name lookups:

```csharp
public class DirectMapper : IMapper<MyObject>
{
    public void Write(MyObject obj, ref RowWriter rowWriter, IMapperSchema schema)
    {
        // Write columns in schema order
        rowWriter.WriteInt(obj.Id);
        rowWriter.WriteString(obj.Name);
        rowWriter.WriteDateTime(obj.CreatedAt);
    }

    public MyObject Read(ref RowReader rowReader, IMapperSchema schema)
    {
        // Read columns in schema order
        return new MyObject
        {
            Id = rowReader.ReadInt()!.Value,
            Name = rowReader.ReadString(),
            CreatedAt = rowReader.ReadDateTime()!.Value
        };
    }
}
```

#### Dynamic Schema Mapping

When the schema may vary or is not known at compile time, you can load the schema at runtime. The compiler optimizes switch statements with hash codes for fast lookups:

```csharp
public class DynamicMapper : IMapper<MyObject>
{
    public void Write(MyObject obj, ref RowWriter rowWriter, IMapperSchema schema)
    {
        foreach (var column in schema.Columns)
        {
            switch (column.Name)
            {
                case "ID":
                    rowWriter.WriteInt(obj.Id);
                    break;
                case "NAME":
                    rowWriter.WriteString(obj.Name);
                    break;
                case "CREATED_AT":
                    rowWriter.WriteDateTime(obj.CreatedAt);
                    break;
                default:
                    rowWriter.Skip(); // Unmapped column
                    break;
            }
        }
    }

    public MyObject Read(ref RowReader rowReader, IMapperSchema schema)
    {
        var obj = new MyObject();

        foreach (var column in schema.Columns)
        {
            switch (column.Name)
            {
                case "ID":
                    obj.Id = rowReader.ReadInt()!.Value;
                    break;
                case "NAME":
                    obj.Name = rowReader.ReadString();
                    break;
                case "CREATED_AT":
                    obj.CreatedAt = rowReader.ReadDateTime()!.Value;
                    break;
                default:
                    rowReader.Skip(); // Unmapped column
                    break;
            }
        }

        return obj;
    }
}
```

## Native Ahead-Of-Time Mode Support

GridGain 9 .NET client supports running in Native AOT mode for most public APIs. A small subset of APIs is not compatible with AOT due to reliance on reflection.

The following APIs are not supported in Native AOT mode:

- Automatic object mapping without `IMapper<T>`

**Workaround**: use overloads that explicitly accept IMapper<T>.

- LINQ-based APIs (`IRecordView.AsQueryable`, `IKeyValueView.AsQueryable`)

**Workaround**: use the SQL API, which supports `IMapper<T>` and is compatible with AOT.

When compiling an application in Native AOT mode, unsupported APIs produce trimming warnings that indicate the issue and suggest compatible alternatives.

For more details refer to the official Microsoft [documentation](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/?utm_source=chatgpt.com&tabs=windows%2Cnet8#publish-native-aot-using-the-cli).
