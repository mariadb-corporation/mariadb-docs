---
description: >-
  System variables that control MariaDB's vector storage and similarity-search
  features.
---

# Vector System Variables

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/pBQsCgBA6SJpi0m3pZuk/" %}

{% include "../../../.gitbook/includes/vectors-are-available-from-....md" %}

This page documents system variables related to [Vectors](./).

See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for instructions on setting them.

Also see the [Full list of MariaDB options, system and status variables](../../full-list-of-mariadb-options-system-and-status-variables.md).

#### `mhnsw_default_distance`

* Description: Specifies the default distance metric for MHNSW vector indexing. This is used when the `DISTANCE` option is not explicitly defined during index creation.
* Command line: `--mhnsw-default-distance=val`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `euclidean`
* Valid Values:
  * `euclidean` Calculates straight-line distance between vectors. Best for spatial data, images, etc, when absolute magnitude matters.
  * `cosine` Measures directional similarity between vectors. Ideal for text embeddings, semantic search, and when vector magnitude is less important.
* Introduced: MariaDB 11.7.1

#### `mhnsw_default_m`

* Description: Defines the default value for the M parameter in MHNSW vector indexing. The `M` parameter controls the number of connections per layer in the graph structure, influencing the balance between search performance and index size.
  * Larger `M` → Better search accuracy, but larger index size and slower updates and searches.
  * Smaller `M` → Faster updates and searches, smaller index, but potentially less accurate search.
* Command line: `--mhnsw-default-m=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `int unsigned`
* Default Value: `6`
* Range: `3` to `200`
* Introduced: MariaDB 11.7.1

#### `mhnsw_ef_search`

* Description: Defines the minimal number of result candidates to look for in the vector index for ORDER BY ... LIMIT N queries. The search will never search for less rows than that, even if LIMIT is smaller. This notably improves the search quality at low LIMIT values, at the expense of search time. Higher values may increase search quality but will also impact query performance.
* Command line: `--mhnsw-ef-search=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `int unsigned`
* Default Value: `20`
* Range: `1` to `10000`
* Introduced: MariaDB 11.7.1

#### `mhnsw_max_cache_size`

* Description: Upper limit for one MHNSW vector index cache. This limits the amount of memory that can be used for caching the index, ensuring efficient memory utilization.
* Command line: `--mhnsw-max-cache-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `bigint unsigned`
* Default Value: `16777216` (16 MB)
* Range: `1048576` to `18446744073709551615`
* Introduced: MariaDB 11.7.1

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
