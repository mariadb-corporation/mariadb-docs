---
description: >-
  Configure GridGain vector indexes: quantized storage, HNSW build parameters,
  segment and query-thread tuning, and node-wide vector system properties.
---

# Vector Index Configuration

## Vector Index Storage

Since 8.10, a vector index can also store _quantized_ codes and traverse the search graph on those codes. This trades some recall for a smaller working set per search. It does not make the index smaller: the raw vectors stay in the index, so total index memory grows slightly. Storage is configured per index through the `quantization` attribute of `@QueryVectorField` (or `QueryIndex`):

| Value | Behavior |
| --- | --- |
| `ENGINE_DEFAULT` | The default. Leaves the choice to the node, which falls back to full precision unless `GRIDGAIN_VECTOR_BINARY_QUANTIZATION` is set node-wide. |
| `NONE` | Full precision. No quantization, largest working set, best recall. |
| `INT8` | One byte per dimension. The graph is traversed on codes about four times smaller than the raw vectors, and no re-score step is needed. The middle setting: less recall lost than `BINARY`, but a larger working set per search. |
| `BINARY` | One bit per dimension. The graph is traversed on codes about 32 times smaller than the raw vectors, and the retained raw vectors re-score the candidates at full precision. The smallest working set per search, and the most recall lost. Requires the Lucene 10.4 line. |

```java
// Store the index as int8-quantized codes.
@QueryVectorField(quantization = INT8)
private float[] vec;
```

{% hint style="info" %}
`INT8` is carried by both Lucene lines GridGain ships, so it works on any node. `BINARY` requires the Lucene 10.4 line (the `gridgain-vector-query-lucene-10` module). On a Lucene 9 node, a REPLICATED cache logs a warning and indexes at full precision instead. A PARTITIONED cache fails to create the vector index, because every node must use the same vector format. The same applies when `GRIDGAIN_VECTOR_BINARY_QUANTIZATION` selects `BINARY` for an index left at `ENGINE_DEFAULT`.

Recall for `INT8` can differ slightly between a Lucene 9 node and a Lucene 10 node, because the two lines do not quantize to identical bytes. A vector index is memory-resident and per node, so no node reads what another wrote - but keep this in mind when comparing recall across a mixed-version cluster.
{% endhint %}

## Tuning the Vector Index

The following attributes on `@QueryVectorField` (and `QueryIndex`), available since 8.10, control how a vector index is built and served. All are optional; leaving them unset uses the engine default.

| Attribute | Range (default) | Effect |
| --- | --- | --- |
| `hnswM` | 1-512 (engine default 16) | Number of graph connections for each vector in the HNSW graph. A higher value improves recall and costs graph memory and build time. Changing it requires an index rebuild. |
| `hnswEfConstruction` | 1-3200 (engine default 100) | Build-time beam width: how many candidates the engine keeps while it chooses each vector's connections. A higher value costs build time but no extra index memory. A value below `hnswM` wastes the higher connection count. Changing it requires an index rebuild. |
| `maxSegments` | 1-1024 (engine default 8) | Target maximum number of Lucene segments. A KNN query searches one graph per segment, so query cost tracks the segment count more than the corpus size. When a query finds more segments than this, the engine merges the index down in the background. After the first merge, the next one does not start before the index reaches twice the target. Fewer segments answer faster but the merge to reach them is expensive, and every write reopens the gap. |
| `queryThreads` | 1-64 (engine default 1) | How many threads search an index's segments concurrently. This _spreads_ one query's work rather than reducing it: it lowers latency only where cores are spare, and does nothing for an index of a single segment. |

```java
@QueryVectorField(maxSegments = 4, queryThreads = 8)
private float[] vec;
```

{% hint style="warning" %}
`queryThreads` is _per index_, and it multiplies. One vector index exists per vector-indexed type, so a node commits this many threads for _each_ of them. Size the value against the node, not the index.

Consolidating to a low `maxSegments` is not a one-off cost. A vector index is rebuilt when a node starts, so a cache that outlives its node re-pays the consolidation on every start, and the first queries after each start run against an index that is still merging. Prefer a read-mostly index for aggressive consolidation. As a reference point, consolidating a 50,000 x 1536-dimension index to 4 segments took about 153 seconds, and a full merge of a 1M-vector index to one segment took over 30 minutes.

To keep an index effectively unconsolidated, set `maxSegments` to 1024 - a target no index reaches.
{% endhint %}

Out-of-range values are rejected when the index is created (they are not silently clamped), and all of these attributes apply to `VECTOR` indexes only.

## Vector Index System Properties

These node-wide system properties, available since 8.10, set defaults for vector indexes that configure none of their own. For a property with a per-index twin, the per-index attribute wins, then the system property, then the engine default.

| Property | Accepts (default) | Description |
| --- | --- | --- |
| `GRIDGAIN_VECTOR_INDEX_MAX_SEGMENTS` | 1-1024 (0) | Node-wide `maxSegments` default. `0` defers to the per-index setting and then to the engine default of 8. A value outside 1-1024 fails the vector index at creation. |
| `GRIDGAIN_VECTOR_QUERY_THREADS` | 1-64 (0) | Node-wide `queryThreads` default. `0` defers to the per-index setting and then to the engine default of 1 (the query is answered on the calling thread). A value outside 1-64 fails the vector index at creation. |
| `GRIDGAIN_VECTOR_INDEX_DELETES_PCT` | 5-50 (20) | Largest share of deleted vectors an index holds before a merge reclaims their memory. When a cache entry expires or is removed, its vector is only _marked_ deleted - it keeps its memory and stays in the search graph until a merge rewrites the segment. A lower value reclaims memory sooner but merges more often. A value outside 5-50 fails the vector index at creation. |
| `GRIDGAIN_VECTOR_BINARY_QUANTIZATION` | `true` or `false` (`false`) | Stores `BINARY` codes for every vector index left at `ENGINE_DEFAULT`. Applies only to indexes built after it is set. An index that names its own storage keeps it. Set it the same on every node, or nodes answer the same query with different recall. |
| `GRIDGAIN_VECTOR_NOCOPY_SCORER` | `true` or `false` (`false`) | Turns on the no-copy vector scorer. Takes effect only with the `ignite-lucene-10-java22` module on Java 22 to 25, with the JVM started with `--add-modules jdk.incubator.vector`. Read once at node startup. For details, see [Enabling the No-Copy Vector Scorer](README.md#enabling-the-no-copy-vector-scorer). |
| `GRIDGAIN_VECTOR_INDEX_RAM_BUFFER_MB` | 1 or more (16) | Size in megabytes of the on-heap buffer a vector index fills before it flushes a segment. A larger buffer uses more heap but makes fewer segments. Each vector index has its own buffer, so the node needs this much heap for each vector-indexed type. A value of 0 or less fails the vector index at creation. |
