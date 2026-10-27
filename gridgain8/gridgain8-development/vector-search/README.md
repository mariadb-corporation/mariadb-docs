---
description: >-
  Index and search vectors stored in cache fields in GridGain — vector fields,
  vector queries, and configurable similarity functions.
---

# Vector Search

GridGain can index vectors stored in a field and then search the cache based on the provided vector. This enables similarity search over embeddings — for use cases such as semantic search, recommendations, and retrieval-augmented generation (RAG) — directly against data held in GridGain caches.

## Requirements

- GridGain must be running on Java 17 or later.
- GridGain license must provide access to vector search feature.
- Vector search is supported for both [REPLICATED](../../architecture/data-modeling/data-partitioning.md#replicated) and [PARTITIONED](../../architecture/data-modeling/data-partitioning.md#partitioned) caches. PARTITIONED support was added in 8.10. For how a query runs on a PARTITIONED cache, see [Vector Search on PARTITIONED Caches](vector-queries.md#vector-search-on-partitioned-caches).
- Vectors for the field must be acquired by using a separate model, as no model is provided with GridGain.

## Installation

To start using vector store, enable the optional `gridgain-vector-query` [module](../project-setup.md#enabling-modules).

### Choosing a Lucene Line

Vector search and text search run on one of two Lucene lines. A node runs exactly one line. Choose the line by the node's Java version:

| Java version | Lucene modules | Where to get them |
|---|---|---|
| 17 or later | `ignite-lucene-9` (Lucene 9.10) and `gridgain-vector-query` | The `libs` directory of the binary distribution. `ignite-lucene-9` is enabled by default. |
| 21 or later | `ignite-lucene-10` (Lucene 10.4) and `gridgain-vector-query-lucene-10` | The `libs/optional` directory of the binary distribution. Disabled by default. |
| 22 or later | `ignite-lucene-10-java22` (Lucene 10.4) and `gridgain-vector-query-lucene-10` | The `libs/optional` directory of the binary distribution. Disabled by default. |

The Lucene 9 line is the default and needs no action. Java 17 nodes must use it, because Lucene 10 requires Java 21.

`ignite-lucene-10-java22` is an alternative to `ignite-lucene-10`, not an addition. It can also score vectors directly in off-heap memory instead of copying them to the heap. For details, see [Enabling the No-Copy Vector Scorer](#enabling-the-no-copy-vector-scorer).

To switch a node to the Lucene 10 line:

1. Stop the node.
2. Remove the `libs/ignite-lucene-9` folder from the GridGain installation.
3. Move one of the following folders from `libs/optional` to `libs`:
   - `ignite-lucene-10` for Java 21 or later.
   - `ignite-lucene-10-java22` for Java 22 or later.
4. For vector search, remove `libs/gridgain-vector-query` if it is present, and move `libs/optional/gridgain-vector-query-lucene-10` to `libs`.
5. Start the node.

To switch back to the Lucene 9 line, reverse these steps: move the Lucene 10 module folders back to `libs/optional`, and restore `libs/ignite-lucene-9` and `libs/gridgain-vector-query` from the binary distribution.

Use the same Lucene line on every node in the cluster. Otherwise, a vector query can return results with different recall depending on the node that serves it. Switching lines does not affect data on disk: Lucene indexes are held in memory and rebuilt from cache data.

If you add vector search as a Maven dependency, use either `gridgain-vector-query` or `gridgain-vector-query-lucene-10`, not both. Each one brings its matching Lucene module. To use `ignite-lucene-10-java22` instead, exclude `ignite-lucene-9` and `ignite-lucene-10` from every dependency that brings them, such as `ignite-indexing` and `gridgain-vector-query-lucene-10`, and add `ignite-lucene-10-java22`. `ignite-indexing` picks its Lucene module by the JDK your build runs on, not the JDK of the node. Run `mvn dependency:tree` to check that exactly one Lucene module is on the classpath.

### Enabling the No-Copy Vector Scorer

By default, a node copies each vector from off-heap index memory to the heap before it scores it. With the `ignite-lucene-10-java22` module, a node can score vectors directly in off-heap memory instead. This reduces allocation and garbage collection during vector search.

The no-copy scorer is off by default. To turn it on, install `ignite-lucene-10-java22` as described above, and start the node with the following JVM options:

```shell
-DGRIDGAIN_VECTOR_NOCOPY_SCORER=true
--add-modules jdk.incubator.vector
--enable-native-access=ALL-UNNAMED
```

- `-DGRIDGAIN_VECTOR_NOCOPY_SCORER=true` turns the scorer on. The node reads it once at startup, so you cannot change it on a running node.
- `--add-modules jdk.incubator.vector` is required. Without it, the node runs and returns correct results, but the scorer is not used.
- `--enable-native-access=ALL-UNNAMED` allows the native memory access the scorer uses. On Java 22 and 23, it only suppresses JVM warnings. On Java 24 and later, it is required if the JVM runs with `--illegal-native-access=deny`. Do not pass `--illegal-native-access` on Java 22 or 23: the option does not exist there, and the JVM does not start.

The scorer works on Java 22 to 25.

When the scorer is active, the node writes a message to the log. Check the log to confirm that the scorer is used.

## In This Section

{% columns %}
{% column %}
{% content-ref url="vector-fields.md" %}
[Vector Fields](vector-fields.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Define vector fields with the QueryVectorField annotation and set the similarity function per field, in Java and Python.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vector-queries.md" %}
[Vector Queries](vector-queries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Run vector similarity queries with VectorQuery: nearest neighbors, similarity threshold and scores, query parameters, field filters, PARTITIONED caches, and limits.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="similarity-functions.md" %}
[Similarity Functions](similarity-functions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The COSINE, EUCLIDEAN, DOT_PRODUCT, and MAXIMUM_INNER_PRODUCT similarity functions, with a comparison and compatibility notes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vector-index-configuration.md" %}
[Vector Index Configuration](vector-index-configuration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure quantized index storage, HNSW build parameters, segment and query-thread tuning, and node-wide vector system properties.
{% endcolumn %}
{% endcolumns %}
