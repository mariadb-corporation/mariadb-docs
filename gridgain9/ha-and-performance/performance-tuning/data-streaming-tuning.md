---
description: >-
  Tuning the GridGain 9 Data Streamer for stability and throughput under heavy
  load, including batching, timeout configuration, and streamer options.
---

# Data Streaming Performance Tuning

When loading large amounts of data using the [Data Streamer](../../gridgain9-usage/data-streaming.md), default settings may cause timeout failures or suboptimal throughput under heavy load. This page describes tuning options to improve stability and performance.

## Batch Records

Instead of submitting all records to a single publisher and calling `streamerFut.join()` once at the end, process data in smaller batches by creating a new publisher per batch. Submitting the entire dataset before joining increases the risk of transaction failures and memory pressure under heavy load.

```java
DataStreamerOptions options = DataStreamerOptions.builder()
        .pageSize(1000)
        .perPartitionParallelOperations(1)
        .build();

int batchSize = 100_000;

for (int batch = 0; batch < totalRecords; batch += batchSize) {
    CompletableFuture<Void> streamerFut;
    try (var publisher = new SubmissionPublisher<DataStreamerItem<Account>>()) {
        streamerFut = view.streamData(publisher, options);
        int end = Math.min(batch + batchSize, totalRecords);
        for (int i = batch; i < end; i++) {
            publisher.submit(DataStreamerItem.of(new Account(i)));
        }
    }
    streamerFut.join();
}
```

## Timeout Tuning

Under heavy Data Streamer load, the cluster may exhaust default timeouts, which can cause lease failures, primary replica changes, and eventually streamer failures. Increase the following timeouts in the node configuration:

| Property | Default | Recommended | Description |
|---|---|---|---|
| [leaseExpirationIntervalMillis](../../reference/configuration/cluster-configuration-parameters.md#replication-configuration) | 5000 | 10000 | Duration before a partition lease is considered expired. Increasing this gives heavily loaded nodes more time to renew their partition leases, reducing unnecessary primary replica changes under heavy I/O. |
| [retryTimeoutMillis](../../reference/configuration/node-configuration-parameters.md#raft-configuration) | 10000 | 30000 | Timeout for Raft operation retries to receive a successful response from a remote peer. Increasing this reduces the chance of Raft failures during prolonged streaming sessions. |

Example configuration:

```javascript
{
  "ignite" : {
    "replication" : {
      "leaseExpirationIntervalMillis" : 10000,
    }
    "raft" : {
      "retryTimeoutMillis" : 30000,
    }
  }
}
```

{% hint style="warning" %}
Verify these settings in a test environment before applying them to production. Higher timeout values reduce failure rates but may increase the time it takes to detect actual node failures.
{% endhint %}

## DataStreamer Options

The following DataStreamer options can be tuned to improve throughput and reduce latency:

| Option | Default | Description |
|---|---|---|
| [perPartitionParallelOperations](../../gridgain9-usage/data-streaming.md#configuring-data-streamer) | 1 | Number of parallel streaming operations per partition. Increasing this value can reduce latency and improve throughput on clusters with available CPU and network capacity. |
| [pageSize](../../gridgain9-usage/data-streaming.md#configuring-data-streamer) | 1000 | Number of records per streaming page. Larger values reduce the number of round trips, which can improve latency, but increase memory usage per operation. |

Start with moderate increases and benchmark each change, as optimal values depend on record size, cluster topology, and available resources.
