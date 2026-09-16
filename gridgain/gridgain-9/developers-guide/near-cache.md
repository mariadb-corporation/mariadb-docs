---
description: >-
  Configure a near cache in GridGain 9 to store frequently accessed data locally,
  eliminating network latency for a specific data subset.
---

# Near Caches

A near cache is a local cache that stores the most recently or most frequently accessed data locally.

{% hint style="info" %}
The Java examples on this page use the thin client, which requires the `ignite-client` module. For repository and dependency configuration, see [Project Setup and Required Modules](project-setup.md).
{% endhint %}

## Benefits

GridGain can access data stored in near cache locally without additional network requests to the cluster. As a result, you can get significantly improved performance with a specific regularly accessed data subset, completely eliminating network latency and cluster load associated with these requests.

## Limitations

There are currently the following limitations on near caches:

- Near caches are available on Java clients and in embedded mode;
- Near caches only work for tables, not caches;
- The `getAll()` and `containsAll()` methods always read data from the cluster;
- Only the basic key-value and record view operations are currently available. The more complicated operations are not supported, including:
  - SQL with NearCache is not supported;
  - Criterion API  not supported;
  - Data streaming  is not supported;
  - Continuous queries are not supported;
  - Explicit transactions are not supported;
- Near caches can contain outdated data, if updates happened on cluster after the last read operation from it. Update frequency is controlled with the `expireAfterUpdate` parameter.

## Configuring Near Cache

In GridGain 9, you configure near caches for individual key-value or record views. As you access data, GridGain will store it locally for later access. GridGain stores the value stored for a certain duration, and uses it in read operations instead of accessing the cluster. The value eventually expires and is re-read from the cluster.

To configure the near cache, set the cache parameters in `NearCacheOptions` object, and then pass this object to the [table view](table-api.md#basic-table-operations) object through `TableViewOptions` parameter.

{% tabs %}
{% tab title="Client" %}
```java
public static void demonstrateNearCacheClient() throws Exception {
    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build()) {

        // Configure near cache options.
        NearCacheOptions nearCacheOptions = NearCacheOptions
                .builder()
                .expireAfterAccess(5000)
                .expireAfterUpdate(100000)
                .maxEntries(100)
                .build();

        // Create table view configuration.
        TableViewOptions tableViewOptions = TableViewOptions
                .builder()
                .nearCacheOptions(nearCacheOptions)
                .build();

        // Create a qualified table name object.
        QualifiedName myTable = QualifiedName.parse("PUBLIC.accounts");

        // Get a view that will also create a near cache on the client.
        try (KeyValueView<Tuple, Tuple> kvView = client.tables().table(myTable).keyValueView(tableViewOptions)) {

            // Get a value from the view.
            Tuple key = Tuple.create().set("id", 0);
            Tuple value = kvView.get(null, key);
            System.out.println("Retrieved value:" + value.intValue("id"));
        }
    }
}
```
{% endtab %}

{% tab title="Embedded" %}
The example below assumes that the node is started and initialized as described in the [Embedded mode](../quick-start/embedded-mode.md) documentation.

```java
public static void demonstrateNearCacheEmbedded() throws Exception {

    // Path to your configuration file
    Path myConfig = Path.of("conf/gridgain-config.conf");
    //Work directory
    Path myWorkDir = Path.of("/home/gridgain");

    IgniteServer node = IgniteServer.start("node", myConfig, myWorkDir);
    // Get the Ignite instance.
    // This example assumes that the node is running
    Ignite ignite = node.api();

    // Configure near cache options.
    NearCacheOptions nearCacheOptions = NearCacheOptions
            .builder()
            .expireAfterAccess(5000)
            .expireAfterUpdate(100000)
            .maxEntries(100)
            .updatePollInterval(1000)
            .build();

    // Create table view configuration.
    TableViewOptions tableViewOptions = TableViewOptions
            .builder()
            .nearCacheOptions(nearCacheOptions)
            .build();

    // Create a qualified table name object.
    QualifiedName myTable = QualifiedName.parse("PUBLIC.accounts");

    // Get a view that will also create a near cache on the client.
    try (KeyValueView<Tuple, Tuple> kvView = ignite.tables().table(myTable).keyValueView(tableViewOptions)) {

        // Get a value from the view.
        Tuple key = Tuple.create().set("id", 0);
        Tuple value = kvView.get(null, key);
        System.out.println("Retrieved value:" + value.intValue("id"));
    }
}
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
The example above uses the `KeyValueView` to access data. You can use any supported table view in your code instead.
{% endhint %}

Below are the available options for near cache configuration:

| Option | Description | Default value |
| --- | --- | --- |
| `maxEntries` | Maximum number of entries in the near cache. Once the maximum cache size is reached, the oldest entry is replaced. Negative values are not allowed. Zero means no limit. | 0 (no limit) |
| `expireAfterRead` | The period of time since the last time data was accessed by the client after which the entry expires and is removed from the near cache, in milliseconds. Negative values are not allowed. Zero means data does not expire. | 0 |
| `expireAfterUpdate` | The period of time since the latest update from cluster after which the entry expires and is removed from the near cache, in milliseconds.  Zero means no expiration. Negative values are not allowed. | 0 |
| `updatePollInterval` | The period of time with which updates are requested from the server, in milliseconds. If 0, update polling is disabled. | 0 (disabled) |
| `updateLongPollingWaitTimeMs` | The period of time each polling request waits on the server for updates, in milliseconds. Only used if `updatePollInterval` is greater than 0. 0 means polling requests return immediately. Negative values are not supported. | 10000 |
