---
name: mariadb-vector-functions
description: "MariaDB vector functions — VEC_Distance, VEC_Distance_Euclidean, VEC_Distance_Cosine, VEC_FromText, VEC_ToText, and the VECTOR data type / MHNSW vector index context. Use when writing SQL that stores, queries, or computes distances over vector embeddings in MariaDB."
---

# MariaDB Vector Functions

*Last updated: 2026-07-20*

Catalog of every built-in vector function in MariaDB, with signature and a one-line semantic summary per entry. For a function not listed here, fall back to the canonical reference at
<https://mariadb.com/docs/server/reference/sql-functions/vector-functions>.

> **Default context:** Assume MariaDB **11.8 LTS** unless the user specifies another version. Functions with a `*(since X.Y)*` annotation are only available from that version onward; everything else is in every current LTS branch (10.6, 10.11, 11.4, 11.8).

The entire vector feature — the `VECTOR` data type, `VECTOR INDEX`, and every function in this catalog — is newer than that baseline: it landed as a preview in the **11.7** rolling release (`VEC_FromText`/`VEC_ToText`/`VEC_Distance*` since **11.7.1**), and **11.8 is the first LTS release to include it (GA/Stable)**. It does **not** exist in 10.6, 10.11, or 11.4 — code targeting those branches must not use it.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
| --- | --- |
| pgvector-style `<->` (Euclidean) or `<=>` (cosine) operators, or a `<#>` dot-product operator, in `ORDER BY` | MariaDB has no distance operators. Use the functions `VEC_DISTANCE_EUCLIDEAN(v, s)`, `VEC_DISTANCE_COSINE(v, s)`, or the index-aware `VEC_DISTANCE(v, s)` |
| Assuming vector search works on any current LTS | The whole feature is *(since 11.7.1, preview)* / *(since 11.8, GA)* — absent from 10.6/10.11/11.4. Check the target version before emitting any of this syntax |
| Inserting a bare JSON array string (e.g. `'[1,2,3]'`) into a `VECTOR` column and expecting it to convert automatically | Wrap it in `VEC_FromText('[1,2,3]')` explicitly. A `VECTOR` column stores little-endian IEEE-754 float32 bytes (4 bytes per dimension), not JSON text |
| Calling `VEC_DISTANCE_COSINE`/`VEC_DISTANCE_EUCLIDEAN` and expecting a normalized `[0,1]` similarity score | These return a raw distance (Euclidean L2, or `1 - cosine_similarity`-scaled cosine distance) — smaller means closer. There's no built-in dot-product/inner-product distance function; convert to a similarity score yourself if needed |
| Reaching for a dot-product/inner-product distance function to match another vector database's default metric | MariaDB deliberately has none — dot product isn't a proper distance metric there (a vector's nearest match need not be itself) and offers no speed advantage in MariaDB's implementation. Use `euclidean` or `cosine` instead; they're equally fast for normalized vectors |
| Expecting `ORDER BY VEC_DISTANCE_EUCLIDEAN(col, x) LIMIT k` to always use the `VECTOR INDEX` | The index is only used when the query's `ORDER BY` is the literal distance call (ascending) combined with a `LIMIT`, **and** that distance function matches the metric the index was built with (`DISTANCE=euclidean` by default, or `DISTANCE=cosine`). A mismatched metric, a bare `WHERE ... < threshold` with no `LIMIT`, or wrapping the distance in an outer expression all fall back to a full table scan |
| Using the generic `VEC_DISTANCE(v, s)` and assuming it always computes Euclidean distance | It's metric-agnostic: it resolves to whichever metric the column's `VECTOR INDEX` was built with (euclidean or cosine), and raises error 4206 if no such index can be found. Use `VEC_DISTANCE_EUCLIDEAN`/`VEC_DISTANCE_COSINE` directly when the metric must be pinned regardless of indexing |
| Assuming a table can have multiple `VECTOR INDEX` definitions, one per metric | MariaDB allows only **one** vector index per table, and the indexed column must be `NOT NULL`. Picking `DISTANCE` at `CREATE TABLE` time locks in the metric queries must match to use the index |

## Functions

<!-- BEGIN GENERATED -->
<!-- Extracted from server/reference/sql-functions/vector-functions -->
<!-- 3 functions, 2 pages skipped on extraction failure -->

### VEC_DISTANCE
`VEC_DISTANCE(v, s)`  
`VEC_DISTANCE` is a generic function that behaves either as VEC_DISTANCE_EUCLIDEAN, calculating the Euclidean (L2) distance between two points.

### VEC_DISTANCE_COSINE
`VEC_DISTANCE_COSINE(v, s)`  
`VEC_Distance_Cosine` is an SQL function that calculates the Cosine distance between two (not necessarily normalized) vectors.

### VEC_DISTANCE_EUCLIDEAN
`VEC_DISTANCE_EUCLIDEAN(v, s)`  
`VEC_Distance_Euclidean` is an SQL function that calculates a Euclidean (L2) distance between two points.
<!-- END GENERATED -->

## See Also
- **`mariadb-create-table`** — the `VECTOR(N)` column type, `VECTOR INDEX (col) [M=n] [DISTANCE=euclidean|cosine]` syntax, and the one-index-per-table / `NOT NULL` constraints
- Canonical reference on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-functions/vector-functions>
  - <https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-overview>
  - <https://mariadb.com/docs/server/reference/sql-structure/vectors/create-table-with-vectors>
  - <https://mariadb.com/docs/server/reference/sql-structure/vectors/vector>
  - <https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-system-variables>
