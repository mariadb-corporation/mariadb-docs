---
description: >-
  Run vector similarity queries in GridGain with VectorQuery, including
  similarity scores, query parameters, field filters, PARTITIONED caches, and limits.
---

# Vector Queries

To perform a vector query, you would need a search vector provided by the same model as the one used to create the original vectors for the database objects. In this example, we will assume that you have procured the required vector already. Once the vector is available, you can use the `VectorQuery` object to create a query and send it to the cluster with the `query` method:

```java
float[] searchVector = // get from model
VectorQuery<Long, Article> myQuery =
    new VectorQuery<>(Article.class, "contentVector", searchVector, 5);
cache.query(myQuery).getAll();
```

The `VectorQuery` constructor accepts the following parameters:

- The first parameter specifies the Article object representing the cache entry type.
- The second parameter specifies the name of the vector field that will be searched.
- The third parameter specifies the previously obtained search vector.
- The fourth parameter specifies the maximum number of results to return. This parameter, often referred to as `k` in nearest neighbor searches, determines how many nearest neighbors the query will retrieve.
- You can also specify an optional fifth threshold parameter to control the quality of results returned, for example:

  ```java
  float[] searchVector = // get from model
  // Using the overloaded constructor with threshold parameter
  VectorQuery<Long, Article> myQuery =
      new VectorQuery<>(Article.class, "contentVector", searchVector, 5, 0.75f);
  cache.query(myQuery).getAll();
  ```

  The threshold is a minimum similarity score: the query returns only results with a score of at least this value. Higher values mean the results must be more similar to the search vector. A value of 0 or less, which is the default, turns the threshold off. The score range depends on the similarity function: for `MAXIMUM_INNER_PRODUCT`, scores can be greater than 1.0. This example returns up to 5 nearest neighbors, but only those that have a similarity score of at least 0.75. GridGain applies the threshold after it finds the nearest neighbors, so if fewer than 5 neighbors meet this threshold, fewer results are returned.
  Using a threshold can help ensure that your search only returns relevant results and filters out vectors that are too dissimilar from the search vector.

## Reading Similarity Scores

Since 8.10, every row a vector query returns implements `ScoredCacheEntry`. Its `score()` method returns the similarity between the search vector and the entry's vector, computed by the similarity function of the vector index. For every similarity function, a higher score means a more similar entry.

To read the score, cast the entry or unwrap it:

```java
for (Cache.Entry<Long, Article> e : cache.query(myQuery)) {
    float score = ((ScoredCacheEntry<Long, Article>)e).score();

    // The same value, without the cast:
    float same = e.unwrap(ScoredCacheEntry.class).score();
}
```

## Query Parameters

Since 8.10, `VectorQuery` has the following optional setters. Each returns the query, so you can chain them.

| Setter | Default | Description |
|---|---|---|
| `setEfSearch(int)` | `0` (engine default) | Search beam width, often called `efSearch` or `ef`: how many candidate vectors the engine keeps while it walks the index graph. The query returns the best `k` of those candidates. A beam wider than `k` improves recall and increases latency. A value below `k` is treated as `k`, and `0` or a negative value uses a beam of `k`. A wide beam is never rejected: the engine limits it to the number of indexed vectors. |
| `setOversample(int)` | `0` (engine default 3) | Applies only to an index that stores `BINARY` codes. The engine searches with at least `k` × `oversample` candidates and then re-scores them on the full-precision vectors. This is a minimum, so setting `setEfSearch` does not turn it off. It has no effect on `NONE` or `INT8` storage. For details, see [Vector Index Storage](vector-index-configuration.md#vector-index-storage). |
| `setFieldFilter(Map<String, Object>)` | `null` (whole index) | Field values that every result must have. For details, see [Filtering by Field Value](#filtering-by-field-value). |
| `setKeysOnly(boolean)` | `false` | Returns keys without values: `getValue()` of each row returns `null`. Use it only when you don't need the values. An engine that cannot leave out values returns full rows instead. This setting never changes which keys the query finds. |

```java
VectorQuery<Long, Article> qry = new VectorQuery<Long, Article>(Article.class, "contentVector", searchVector, 10)
    .setEfSearch(100)
    .setKeysOnly(true);
```

## Filtering by Field Value

Since 8.10, you can restrict a vector query to entries with given field values by calling `setFieldFilter`. GridGain applies the filter while it searches the index, so the query returns `k` matching entries, not the `k` nearest entries of which only some match. For example, one index can serve several tenants, with one filter for each tenant.

A filter can only name a field of the type's text index, for example, a field annotated with `@QueryTextField`. A filter that names any other field fails when the query runs. Field names are not case-sensitive.

```java
public class Article {
    @QueryTextField
    private String tenant;

    @QueryVectorField
    private float[] contentVector;
}

VectorQuery<Long, Article> qry = new VectorQuery<Long, Article>(Article.class, "contentVector", searchVector, 5)
    .setFieldFilter(Map.of("tenant", "acme"));
```

The filter works as follows:

- Each map entry is an exact-value test, and a result must pass every test. Range tests are not supported.
- A value matches when its text form equals the text form of the stored value. For an integer field, the integer type does not matter: `7`, `7L` and `(short)7` all match a stored `7`. A decimal value does not match an integer: `7.0d` matches nothing in a `long` field, and the query returns no error. Give a decimal field a value of the type it has in the schema.
- A stored value longer than 32766 bytes in UTF-8 cannot be filtered on. A filter on that field matches nothing for that entry, and the query returns no error. Filter on short values such as keys and labels.
- Keys and values in the map must not be `null`. A `null` or empty map searches the whole index.

## Vector Search on PARTITIONED Caches

Since 8.10, you can run vector queries on PARTITIONED caches. You use the same `VectorQuery` API as for a REPLICATED cache. GridGain distributes the query for you.

### How a Query Runs

When you run a vector query on a PARTITIONED cache, GridGain does the following:

1. Sends the query to every server node that holds data for the cache.
2. Each node searches only the partitions it is primary for and returns its own top `k` results with their similarity scores.
3. The node that started the query merges the results by score and returns the best `k`.

Each node answers for a different set of partitions, so the result contains no duplicate entries. Each node's search is approximate, as on a REPLICATED cache, but the merge does not lose any results.

You can run the query from a server node, a client node, or a thin client. A thin client query is distributed by the server node the client connects to.

On a REPLICATED cache, a server node answers the query from its own copy of the data. A client node usually sends the query to one server node.

### Local Queries

If you set `setLocal(true)` on a vector query for a PARTITIONED cache, the query searches only the partitions that the local node is primary for, and returns only entries from those partitions. Run local queries only on nodes that hold the cache's data. On a client node, or on a server node outside the cache's node filter, a local query fails.

### Topology Changes and Lost Partitions

While the query runs, each node reserves its primary partitions, so rebalancing cannot move them during the search. If a partition moves to another node, or a node leaves the cluster, GridGain repeats the whole query on the new topology. If the topology does not settle within about 30 seconds or 50 retries, the query fails.

If a partition is lost, the cache's [partition loss policy](../../architecture/rebalancing/partition-loss-policy.md) determines the result:

- With a `*_SAFE` policy, the query fails with `CacheInvalidStateException`.
- With a `*_ALL` policy, the query searches the remaining partitions. The `*_ALL` policies are deprecated.
- With `IGNORE`, lost partitions are treated as empty, so the query succeeds without their entries.

With a `*_SAFE` policy, a query never returns results that are missing a partition.

### Memory Planning

On a PARTITIONED cache, each node indexes every copy of the data it holds, both primary and [backup](../../architecture/data-modeling/data-partitioning.md#backup-partitions). A query skips backup copies, but they still use index memory. With one backup, each node's vector index holds about twice as many vectors as the node has primary entries. Take backups into account when you size memory for a PARTITIONED cache with a vector index.

### Requirements for PARTITIONED Caches

- All nodes must use the same vector index storage format. For details, see [Vector Index Storage](vector-index-configuration.md#vector-index-storage).
- During a rolling upgrade to 8.10, any vector query except a local query on a server node fails until the rolling upgrade is complete. Until then, run the query on a server node with `setLocal(true)`. On a PARTITIONED cache, such a query returns only the entries from that node's primary partitions.

## Vector Search Limits

GridGain limits the size of vectors and vector queries. To change the limits, set the following system properties. Set `GRIDGAIN_VECTOR_MAX_DIMENSIONS` on every server node. Set `GRIDGAIN_VECTOR_MAX_K` on every server node and on every client node that runs vector queries. A thin client query uses the limit set on the server node the client connects to.

| Property | Default | Description |
|---|---|---|
| `GRIDGAIN_VECTOR_MAX_DIMENSIONS` | 4096 | The maximum number of dimensions a vector index accepts. The property applies to indexes created after it is set. If the value is 0 or less, vector indexes cannot be created. |
| `GRIDGAIN_VECTOR_MAX_K` | 10000 | The maximum number of nearest neighbors (`k`) a single vector query can request. A query with a larger `k` is rejected. A value of 0 or less is ignored, and the default is used. |

{% hint style="info" %}
The memory usage and search time of a vector index grow with the number of dimensions. Vectors with more than 8192 dimensions exceed the 32 KB read buffer of the index storage, so each vector read takes several buffer reads.
{% endhint %}
