---
description: >-
  PyGridGain 1.7.0 supports Python 3.11 to 3.15, adds vector query filters and
  tuning parameters, and uses TLS 1.3 by default. Also covers langchain-gridgain
  and langgraph-checkpoint-gridgain 3.0.0.
hidden: true
---

# PyGridGain 1.7.0 Release Notes

## New Features

PyGridGain 1.7.0 adds new vector search parameters, supports newer Python versions, and changes several defaults. This release also covers `langchain-gridgain` 3.0.0 and the new `langgraph-checkpoint-gridgain` 3.0.0 package.

### Python 3.11 to 3.15

The client now requires Python 3.11 or later, and pre-built binaries are available for Python 3.11 to 3.15. Python 3.9 and 3.10 are no longer supported. To use the client with these Python versions, install version 1.6.0 or earlier.

### Vector Query Filters

`Cache.vector()` and `AioCache.vector()` accept a `field_filter` parameter that restricts a query to entries with given field values. GridGain applies the filter while it searches the index, so the query returns `k` matching entries. The new `oversample` parameter controls re-scoring for indexes that store `BINARY` codes.

```python
cursor = cache.vector(
    type_name=Article.type_name,
    field='vector_field',
    clause_vector=query_vector,
    k=10,
    threshold=0,
    field_filter={'tenant': 'acme'},
)
```

### Vector Query and Index Parameters

`Cache.vector()` and `AioCache.vector()` accept the following new parameters:

- `ef_search` sets the search beam width.
- `with_scores` adds the similarity score to each result row.
- `no_content` returns keys without values.

Vector indexes accept the new `hnsw_m`, `hnsw_ef_construction`, `quantization` (including `INT8`), `max_segments`, and `query_threads` keys.

The new vector parameters require GridGain 8.10 or later. If the cluster does not support a parameter that you set, the client raises `NotSupportedByClusterError`.

For more information, see [Vector Queries](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/thin-clients/python-thin-client#vector-queries).

### LangChain and LangGraph Integration

`langchain-gridgain` 3.0.0 and the new `langgraph-checkpoint-gridgain` 3.0.0 package include the following changes, including the changes from `langchain-gridgain` 2.0.0:

- **New `langgraph-checkpoint-gridgain` package.** It provides the following LangGraph components, which do not require a license for vector search:
  - `GridGainCheckpointSaver`, a checkpointer.
  - `GridGainMemoryStore`, a store for long-term memory with structured filters and expiry enforced by the server.
  - `GridGainNodeCache`, a node cache.
- **`GridGainByteStore`.** A key-value store for binary values, such as embeddings cached with `CacheBackedEmbeddings`.
- **Entry expiry.** `GridGainStore`, `GridGainByteStore`, `GridGainCache`, `GridGainSemanticCache`, and `GridGainVectorStore` accept a `ttl` argument.
- **Vector store metadata filtering.** `GridGainVectorStore` filters searches by declared metadata keys on the server. Filtering requires PyGridGain 1.7.0 and GridGain 8.10 or later.
- **Vector store improvements.** `GridGainVectorStore` supports IDs, deleting and getting documents by ID, and maximal marginal relevance search, and returns real cosine distances as scores.

## Changes in Behavior

- **TLS 1.3 by default.** SSL connections now use TLS 1.3 or later by default. Before, the client used TLS 1.2. To connect to a cluster that supports only TLS 1.2, set `ssl_version=ssl.TLSVersion.TLSv1_2`. `ssl_version` now takes an `ssl.TLSVersion` value, which is the minimum version. The `ssl.PROTOCOL_TLSv1_2`, `ssl.PROTOCOL_TLSv1_1`, and `ssl.PROTOCOL_TLSv1` constants still work; other `ssl.PROTOCOL_*` values, such as `ssl.PROTOCOL_TLS_SERVER`, raise `ParameterError`.
- **Vector query page size.** `Cache.vector()` and `AioCache.vector()` use `k` as the default `page_size` instead of `1`, so the whole result arrives in one page. To keep a smaller page, set `page_size` explicitly.
- **Vector query `k` check.** The client raises `ValueError` for a `k` that is not positive, instead of sending the query to the server.
- **Vector query response shapes.** An asyncio `(key, value)` row is now a `tuple` instead of a `list`. The low-level `pygridgain.api.sql.vector()` function returns rows as a list of `(key, value)` tuples instead of a dictionary.
- **Feature bits of vector index parameters.** The client uses the same feature bits as GridGain 8.10 for Hierarchical Navigable Small World (HNSW) build parameters and vector quantization. It no longer uses these features with GridGain 8.9.38 or 8.9.39, which advertise the old bits but do not support the fields.
- **Dependencies.** `attrs` and `tzlocal` are no longer pinned to exact versions, and `contextvars` is no longer required.
- **Packaging.** The package metadata moved to `pyproject.toml`. The installed package no longer contains a top-level `tests` package. Building from a source distribution requires setuptools 77 or later.
- **License.** The client is licensed under the MariaDB Software License Terms.
- **LangGraph imports.** In `langchain-gridgain` 3.0.0, `GridGainCheckpointSaver` and `GridGainMemoryStore` moved to `langgraph-checkpoint-gridgain`. Import them from `langgraph.checkpoint.gridgain` and `langgraph.store.gridgain`.
- **LangChain dependencies and cache keys.** `langchain-gridgain` depends on `langchain-core` 1.4.7 or later instead of `langchain-community`, and `GridGainCache` keys now include the large language model (LLM). Clear LLM caches written by version 1.0.x once after the upgrade.

## Improvements and Fixed Issues

| Issue ID | Description |
|---|---|
| GG-38200 | A partition-aware client now registers the binary type of a complex key before it sends the key. Before, SQL and other clients could not read such keys. `AioClient` was affected by default. |
| GG-45279 | `langchain-gridgain`: `GridGainVectorStore.clear()` and `from_texts()` now work correctly. |
| GG-49286 | Added the `ef_search`, `with_scores`, and `no_content` vector query parameters. |
| GG-49543 | Added the `hnsw_m` and `hnsw_ef_construction` vector index parameters. |
| GG-49786 | `langchain-gridgain`: added `GridGainByteStore` and TTL support; fixed the LLM cache key, similarity scores, and clearing of the semantic cache. |
| GG-49787, GG-49788, GG-49789 | Added the LangGraph `GridGainCheckpointSaver` and `GridGainMemoryStore`. |
| GG-49932 | Vector queries use `k` as the default page size and decode responses faster. Strings that contain a NUL character (U+0000) are no longer truncated. |
| GG-50943 | Added the `quantization` (including `INT8`), `max_segments`, and `query_threads` vector index parameters. |
| GG-51543 | The client now sends its time zone ID, such as `Europe/Berlin`, in the handshake. In versions 1.5.0 and 1.6.0, the time zone was not sent for zones that use daylight saving time, so the server shifted timestamps. |
| GG-51569 | The LangGraph components moved to the new `langgraph-checkpoint-gridgain` package. |
| GG-51572 | Added the LangGraph `GridGainNodeCache`. |
| GG-51636 | Modernized the packaging and dependencies. The installation instructions now use `pip install "pygridgain<9"`, because a plain `pip install pygridgain` installs the GridGain 9 client. |
| GG-51637 | Added support for Python 3.11 to 3.15 and removed support for Python 3.9 and 3.10. SSL connections use TLS 1.3 by default. The client no longer emits `DeprecationWarning` on Python 3.14 and later. |
| GG-51945 | Added the `field_filter` and `oversample` vector query parameters. |
| GG-51946 | `langchain-gridgain`: `GridGainVectorStore` filters searches by metadata on the server. |
| GG-52701 | Fixed reading and writing vector index parameters with GridGain 8.9.38 and 8.9.39 clusters. |
| GG-52848 | The client is licensed under the MariaDB Software License Terms. |

## Installation and Upgrade Information

{% hint style="warning" %}
The `pygridgain` package on PyPI also contains the GridGain 9 client, which has version numbers 9.0 and higher. Always specify a version lower than 9.
{% endhint %}

To upgrade an existing package, use the following command:

```shell
pip install --upgrade "pygridgain<9"
```

To install the latest version of a package:

```shell
pip install "pygridgain<9"
```

To install a specific version:

```shell
pip install pygridgain==1.7.0
```

To install the LangChain and LangGraph packages:

```shell
pip install langchain-gridgain==3.0.0
pip install langgraph-checkpoint-gridgain==3.0.0
```

## Previous Releases

- [PyGridGain 1.6.0](release-notes_python-1.6.0.md)
- [PyGridGain 1.5.0](release-notes_python-1.5.0.md)
- [PyGridGain 1.4.0](release-notes_python-1.4.0.md)
- [PyGridGain 1.3.1](release-notes_python-1.3.1.md)
- [PyGridGain 1.2.0](release-notes_python-1.2.0.md)

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
