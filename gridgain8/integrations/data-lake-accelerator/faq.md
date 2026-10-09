---
description: >-
  Answers to commonly asked questions about the recommended data lake acceleration architecture.
---

# FAQ

The section covers commonly asked questions related to the recommended data lakes acceleration architecture.

## Can GridGain be used as a data lake, a data warehouse, or an analytical database?

GridGain is not an analytical database or data lake solution. It's designed for speed and scale. In particular:

- GridGain's storage format is similar to a row-based format and is optimized for fast in-memory access and real-time workloads. GridGain will consume more memory and disk space providing ultra-low latencies in return (microseconds, milliseconds, second). With data lakes like Hadoop or analytical databases, it's the opposite — the storage format is more compact and latencies are high (dozens of seconds, minutes or hours).
- GridGain is not suited for ad-hoc queries. With GridGain's storage format, secondary indexes are used for performance optimizations. This contradicts to the primary purpose of ad-hoc operations — they can be easily added by end users without extra optimization efforts. These limitations will no longer apply once GridGain supports columnar store format.

## Can I use GridGain for BI reports?

Yes and no.

If you follow the suggested Data Lake Acceleration architecture by preselecting a list of reports that require a real-time response time and do the required tuning for them (secondary indexes, data colocation, etc.) then, yes, GridGan can be used as a storage for BI for those specific reports.

Otherwise, you might be tempted to use GridGain as an analytical database or data lake. However, that is not a supported GridGain use case. Please see the question above.

## Is SQL the only API for real-time analytics?

No, SQL is one of the most wide-spread and standardized APIs adopted for analytics but it's not the only one. With GridGain you can use a compute grid to do complex calculations with your custom Java, .NET, or C++ code in a map-reduce fashion which boosts performance by reducing data movement over the network. Next, GridGain Machine and Deep Learning APIs are good for custom calculations with generic ML/DL models.

## How do I decide what is stored in GridGain vs. Hadoop?

A simple, generic approach is best:

- If low-latency (microseconds, milliseconds, seconds) and high throughput (thousands and millions of operations per second) are required for a set of business operations then store a data set needed for such operations in GridGain and use GridGain APIs for the fastest data processing.
- If high-latency (dozens of seconds, minutes, hours) and batch processing are reasonable/required for another set of operations then continue using your data lake (Hadoop).

Consider Spark integrations for federated-queries (aka. cross-database queries).
