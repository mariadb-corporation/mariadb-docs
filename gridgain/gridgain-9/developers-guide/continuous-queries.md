---
description: >-
  Monitor data modifications in a GridGain 9 table with continuous queries —
  subscribers, watermarks, dedicated executors, remote filters, and event types.
---

# Continuous Queries

Continuous queries monitors data modifications in a table. All update events are propagated to the local subscriber. Continuous query implementation guarantees exactly once delivery of an event to the subscriber.

{% hint style="info" %}
The Java examples on this page use the thin client, which requires the `ignite-client` module. For repository and dependency configuration, see [Project Setup and Required Modules](project-setup.md).
{% endhint %}

## Guarantees

Continuous queries provide the following guarantees:

- Exactly-once delivery.
- Order is preserved within a partition. For example, if a key gets updated multiple times, GridGain will always preserve the update order.
- Order is not preserved across multiple partitions. For example, if keys belonging to different partitions get updated, the order of events is not defined.
- Continuous queries only observe committed changes. Changes made within an explicit transaction are only observed after you commit it.
- It is not guaranteed that all changes from a single transaction are a part of a single `TableRowEventBatch` event. A transaction can affect more rows than `pageSize`.

## Starting a Continuous Query

When you modify a table (insert, update, or delete an entry), an event is sent to the continuous query’s local listener so that your application can react accordingly. The local listener is executed on the node that initiated the query.

Note that the continuous query throws an exception if started without a local listener.

Before you start a continuous query, you define a subscriber: the local listener that receives the update events and reacts to them. You then pass it to the query when you start it.

The example below defines a subscriber that prints every event it receives:

{% tabs %}
{% tab title="Java" %}
```java
public class SubscriberExample implements Flow.Subscriber<TableRowEventBatch<Tuple>> {

    private volatile Flow.Subscription subscription;

    @Override
    public void onSubscribe(Flow.Subscription subscription) {
        subscription.request(Long.MAX_VALUE);
    }

    @Override
    public void onNext(TableRowEventBatch<Tuple> batch) {
        List<TableRowEvent<Tuple>> items = batch.rows();
        for (TableRowEvent<Tuple> item : items) {
            System.out.println("onNext: " + item.type() + ", old=" + item.oldEntry() + ", new=" + item.entry());
        }
    }

    @Override
    public void onError(Throwable throwable) {
        System.out.println("onError: " + throwable);
    }

    @Override
    public void onComplete() {
        System.out.println("onComplete");
    }

    void cancel() {
        if (subscription != null) {
            subscription.cancel();
        }
    }
}
```
{% endtab %}

{% tab title=".NET" %}
```csharp
ITable? table = await Client.Tables.GetTableAsync("Person");
IRecordView<IIgniteTuple> view = table!.RecordBinaryView;
IAsyncEnumerable<ITableRowEventBatch<IIgniteTuple>> continuousQuery = view.QueryContinuouslyAsync();

// Add data after the query is started.
await view.UpsertAsync(null, new IgniteTuple { ["Id"] = 1, ["Name"] = "John" });
await view.UpsertAsync(null, new IgniteTuple { ["Id"] = 2, ["Name"] = "Jane" });
await foreach (ITableRowEventBatch<IIgniteTuple> batch in continuousQuery)
{
    foreach (ITableRowEvent<IIgniteTuple> rowEvent in batch.Events)
    {
        Console.WriteLine(rowEvent);
    }
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
using namespace ignite;

auto table = client.get_tables().get_table("Person");
auto view = table->get_record_binary_view();

continuous_query_options opts;
opts.set_poll_interval_ms(100);

auto cq = view.query_continuously(opts);

// Process events asynchronously
cq.get_next_async([](auto res) {
    if (res.has_error()) {
        std::cerr << "Error: " << res.error().what() << std::endl;
        return;
    }

    const auto& batch = res.value();
    for (const auto& event : batch.get_events()) {
        std::cout << "Event type: " << static_cast<int>(event.get_event_type()) << std::endl;
        std::cout << "New entry: " << event.get_new_entry().has_value() << std::endl;
    }
});
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
If the continuous query consumer is slow, it is possible that the query will eventually fail, as it tries to read data that was already cleaned up due to falling behind the [low watermark](../administrators-guide/storage/data-partitions.md#version-storage).
{% endhint %}

### Continuous Query Watermark

When starting a continuous query, GridGain creates a watermark object that represents the continuous query cursor position. This cursor object can be used in a variety of ways to make your work with continuous queries more consistent.

You can use `IContinuousQueryWatermark.AfterTransaction` to start a continuous query after the specified transaction finishes, so you see its changes first and then only newer updates.

```csharp
var watermark = IContinuousQueryWatermark.AfterTransaction(tx);
```

#### Resuming Continuous Queries

When you need to resume the continuous query, you can continue it at the current watermark position by passing the watermark. The watermark must be stored to guarantee the continuous query can be resumed and passed to the continuous query when it is restarted.

The example below shows how you can store the watermark every time data is updated on a subscriber.

```java
public ContinuousQueryWatermark latestWatermark;

@Override
public void onNext(TableRowEventBatch<Tuple> batch) {
    for (TableRowEvent<Tuple> event : batch.rows()) {
        latestWatermark = event.watermark();
    }
}
```

Then, when you need to resume a continuous query, pass the watermark to it.

```java
// Pass the watermark to continuous query.
ContinuousQueryOptions options = ContinuousQueryOptions.builder().watermark(latestWatermark).build();

// Start the continuous query.
accounts.queryContinuously(subscriber, options);
```

#### Starting Continuous Queries in the Past

By default, continuous queries start in present. By setting the watermark in the past, you can choose a specific time to start the continuous query at. All updates since the specified timestamp will be propagated automatically.

You need to pass the time with `Instant` data type to the `ContinuousQueryWatermark.ofInstant()` method.

The example below starts the continuous query 1 hour in the past.

```java
// Get the time one hour ago.
Instant startTime = Instant.now().minus(Duration.ofHours(1));

// Create a watermark object.
ContinuousQueryWatermark wm = ContinuousQueryWatermark.ofInstant(startTime);

// Pass the watermark to continuous query.
ContinuousQueryOptions options = ContinuousQueryOptions.builder().watermark(wm).build();

// Start the continuous query.
accounts.queryContinuously(subscriber, options);
```

#### Starting Continuous Queries From Transaction Timestamp

When starting a continuous query, you can get a timestamp of a *read-only* transaction and pass it to the query to start from exactly the timestamp of the transaction. This way, you can read data from your GridGain cluster with a transaction, apply this data as a snapshot, and then start the continuous query from exactly the point in time the transaction was executed at, without missing or duplicating any updates, ensuring exactly once delivery.

The continuous query started this way behaves the same way as a [query started in the past](continuous-queries.md#starting-continuous-queries-in-the-past), except instead of an `Instant` it starts at the specific point in time for which the transaction gathered data.

The example below shows how you can read data from a view with a read-only transaction:

```java
// This is a sample view that we will work with.
KeyValueView<Long, Account> accounts = table.keyValueView(Mapper.of(Long.class), Mapper.of(Account.class));

// Create transaction configuration that sets it to read-only mode.
var txOpts = new TransactionOptions().readOnly(true);

// Start a transaction.
Transaction tx = client.transactions().begin(txOpts);

// Read data from the view into a list.
List<Entry<Long, Account>> initialRows = new ArrayList<>();
try (Cursor<Entry<Long, Account>> initialQuery = accounts.query(tx, null)) {
    initialQuery.forEachRemaining(initialRows::add);
}

// Commit the transaction.
tx.commit();
```

After the transaction completes, you can apply this data in the appropriate way for your application.

Then, use the `ContinuousQueryWatermark.afterTransaction()` method to obtain the transaction timestamp, and start your continuous query from that point by setting a watermark to it.

The example below starts a simple continuous query starting from the watermark:

```java
// Create a watermark at the transaction timestamp.
ContinuousQueryWatermark wm = ContinuousQueryWatermark.afterTransaction(tx);

// Pass the watermark to continuous query.
ContinuousQueryOptions options = ContinuousQueryOptions.builder().watermark(wm).build();

// Start the continuous query.
accounts.queryContinuously(subscriber, options);
```

### Dedicated Executor Thread

When a continuous query is created, it accepts a Subscriber which gets invoked when the query receives data. By default, Subscriber's methods are executed on the Java's Common Thread Pool. You can fine-tune the thread pool used by creating a dedicated executor and passing it in the continuous query options. This guarantees that the Subscriber's methods will be handled in a dedicated thread pool, providing better control over resource allocation.

Below is the example of creating an executor and using it in your continuous query to the subscriber defined above:

```java
ExecutorService executor = Executors.newSingleThreadExecutor();

var options = ContinuousQueryOptions.builder()
        .executor(executor)
        .build();

view.queryContinuously(subscriber, options);
```

## Stopping a Continuous Query

A continuous query runs indefinitely, delivering events until you explicitly stop it. You can stop a running query using a cancellation token in Java and .NET, or a `cancel()` call in C++.

{% tabs %}
{% tab title="Java" %}
```java
// Create a cancel handle and take a token from it.
CancelHandle cancelHandle = CancelHandle.create();

// Start the continuous query, passing the token.
accounts.queryContinuously(subscriber, options, cancelHandle.token());

// Later, stop the continuous query.
cancelHandle.cancel();
```
{% endtab %}

{% tab title=".NET" %}
```csharp
using var cts = new CancellationTokenSource();

await foreach (ITableRowEventBatch<IIgniteTuple> batch in view.QueryContinuouslyAsync(
    cancellationToken: cts.Token))
{
    foreach (ITableRowEvent<IIgniteTuple> rowEvent in batch.Events)
    {
        Console.WriteLine(rowEvent);
    }
}

// From another thread, stop the continuous query.
cts.Cancel();
```
{% endtab %}

{% tab title="C++" %}
```cpp
auto cq = view.query_continuously(opts);

// Later, stop the continuous query.
cq.cancel();
```
{% endtab %}
{% endtabs %}

## Parameters

You can configure the following properties of continuous queries:

- `executor` - The [executor thread](continuous-queries.md) to use for continuous queries.
- `pageSize` - The number of entries returned from a single partition in one network call. Default value: `1000`.
- `partitions` - The list of table partitions that will be involved in the continuous query. By default, all partitions are included.
- `pollIntervalMs` - Poll interval, in milliseconds. Default value: `1000`.
- `longPollingWaitTimeMs` - Maximum time, in milliseconds, the server waits for new events when none are immediately available. If events arrive, the response is returned immediately; otherwise, an empty response is returned after the timeout. Zero or negative values disable long polling. Use together with pollIntervalMs to balance latency and throughput.
- `skipOldEntries` - When `true`, `TableRowEvent#oldEntry()` (Java/.NET) or `table_row_event::get_old_entry()` (C++) will return `null` or `std::nullopt` for `TableRowEventType#UPDATED` events. This reduces network traffic by avoiding transmission of old entry values to the subscriber.
- `startTimestampMillis` - Start timestamp in epoch time.
- `watermark` - The watermark transaction that will be applied before starting the continuous query.
- `remoteFilter` - Server-side filter (Java/.NET) that drops events before they are sent to the subscriber. See [Remote Filter](#remote-filter). In .NET, the same feature is exposed as overloads of `QueryContinuouslyAsync` rather than an option.

The example below shows how to configure and execute a continuous query:

{% tabs %}
{% tab title="Java" %}
```java
var options = ContinuousQueryOptions.builder()
        .pollIntervalMs(10)
        .longPollingWaitTimeMs(30)
        .pageSize(pageSize)
        .skipOldEntries(false)
        .build();

view.queryContinuously(subscriber, options);
```
{% endtab %}

{% tab title=".NET" %}
```csharp
var options = new ContinuousQueryOptions
{
    ColumnNames = ["id", "name"],
    EventTypes = [TableRowEventType.Created, TableRowEventType.Updated],
    PageSize = 42,
    PollInterval = TimeSpan.FromSeconds(0.5),
    LongPollingWaitTimeMs = TimeSpan.FromSeconds(3000),
    Watermark = IContinuousQueryWatermark.FromInstant(Instant.FromDateTimeUtc(
        DateTime.UtcNow.AddDays(-1))),
    EnableEmptyBatches = false,
    SkipOldEntries = false
};
```
{% endtab %}

{% tab title="C++" %}
```cpp
using namespace ignite;

continuous_query_options opts;
opts.set_page_size(42);
opts.set_poll_interval_ms(500);
opts.set_event_types({table_row_event_type::CREATED, table_row_event_type::UPDATED});
opts.set_column_names({"id", "name"});
opts.set_skip_old_entries(true);
opts.set_enable_empty_batches(false);

auto cq = view.query_continuously(opts);
```
{% endtab %}
{% endtabs %}

## Continuous Query Events

These event types describe the change delivered to `Subscriber` in `TableRowEvent` when continuous query is executing.

| Event Type | Description |
| --- | --- |
| `CREATED` | Row created. |
| `UPDATED` | Row updated. |
| `REMOVED` | Row removed. |
| `ARCHIVED` | Row archived. This event happens when you have a table with [`ARCHIVE AT`](../sql-reference/ddl.md#keywords-and-parameters) condition set and rows get archived according to this condition, meaning those rows are removed on a primary storage but will still be available on the secondary storage. |

## Event Generation

A continuous query observes only committed changes, and events are produced per committed transaction. How many events you receive for a given key therefore depends on the write API you use and on how those writes are grouped into transactions:

- *Single table operations* (such as `upsert`, `delete`, or their batch variants like `upsertAll`): each operation is applied in its own implicit transaction, so every operation that changes a row produces an event.
- *Explicit transactions*: changes are observed only after the transaction commits. If the same key is updated several times within one transaction, the updates are conflated, and the continuous query observes a single event reflecting the final state of that row at commit time.
- *Data streamer*: by default, a streamer batch is applied as a single implicit transaction, so multiple updates to the same key within one batch are conflated into a single event. This is the `SQUASH` mode of [`DataStreamerOptions.sameKeyUpdateMode`](data-streamer.md#same-key-update-mode). To make the streamer emit a separate event for every same-key update, set the mode to `PRESERVE`, which splits the batch so that each update is committed in its own transaction.

## Remote Filter

A remote filter is a predicate that runs on the server and drops non-matching events before they are sent to the subscriber. Use it to reduce network traffic when a continuous query is interested in only a subset of changes (for example, updates to a single status, rows whose price crossed a threshold, or events from specific partitions).

{% hint style="info" %}
The remote filter is experimental and currently available in the Java and .NET clients. It is not yet supported in C++.
{% endhint %}

### Column Reference Syntax

The filter is evaluated against three virtual tables that describe each event:

| Reference | Description |
| --- | --- |
| `CUR.<column>` | Current value of a column (after the operation). |
| `OLD.<column>` | Previous value of a column (before the operation). |
| `EVENT.PARTITION_ID` | Partition ID (`BIGINT`). |
| `EVENT.TYPE_ID` | Event type ID (`INT`): `0` = `CREATED`, `1` = `UPDATED`, `2` = `REMOVED`, `3` = `ARCHIVED`. |
| `EVENT.COMMIT_TIMESTAMP` | Physical commit timestamp, Unix time, in milliseconds (`BIGINT`). |

Quote column names that contain spaces or reserved words with double quotes (for example, `CUR."column with spaces"`).

The availability of `CUR` and `OLD` values depends on the event type:

- *CREATED:* `OLD` columns are `null`; `CUR` columns contain the inserted row.
- *UPDATED:* both `OLD` and `CUR` columns are available.
- *REMOVED:* `OLD` columns contain the deleted row; `CUR` columns are `null`.
- *ARCHIVED:* `OLD` columns contain the archived row; `CUR` columns are `null` (same as `REMOVED`).

### Configuring a Remote Filter

In Java, the filter is built with `Criteria.columnValue(tableName, columnName, condition)` and passed to `ContinuousQueryOptions.remoteFilter()`.

In .NET, two `QueryContinuouslyAsync` overloads accept the filter directly: one takes a SQL predicate string with positional `?` parameters, the other takes a LINQ expression that is translated to SQL on the client. The LINQ overload requires reflection and is not available in AOT builds; use the SQL-string overload there.

The example below filters for updated rows whose new price is greater than `300`:

{% tabs %}
{% tab title="Java" %}
```java
// Only deliver UPDATED events whose new price is greater than 300.
Criteria filter = Criteria.and(
        Criteria.columnValue("CUR", "PRICE", Criteria.greaterThan(300)),
        Criteria.columnValue("EVENT", "TYPE_ID", Criteria.equalTo(TableRowEventType.UPDATED.id()))
);

var options = ContinuousQueryOptions.builder()
        .remoteFilter(filter)
        .build();

view.queryContinuously(subscriber, options);
```
{% endtab %}

{% tab title=".NET (SQL)" %}
```csharp
await foreach (var batch in view.QueryContinuouslyAsync(
    "CUR.PRICE > ? AND EVENT.TYPE_ID = ?",
    [300, (int)TableRowEventType.Updated]))
{
    foreach (var rowEvent in batch.Events)
    {
        Console.WriteLine(rowEvent);
    }
}
```
{% endtab %}

{% tab title=".NET (LINQ)" %}
```csharp
await foreach (var batch in view.QueryContinuouslyAsync(
    e => e.Entry!.Price > 300 && e.Type == TableRowEventType.Updated))
{
    foreach (var rowEvent in batch.Events)
    {
        Console.WriteLine(rowEvent);
    }
}
```
{% endtab %}
{% endtabs %}

The LINQ expression maps to the SQL form as follows: `e.Entry.<column>` becomes `CUR.<column>`, `e.OldEntry.<column>` becomes `OLD.<column>`, and `e.Type` becomes `EVENT.TYPE_ID`. For key-value views, use `e.Entry.Key.<column>` or `e.Entry.Value.<column>`.
