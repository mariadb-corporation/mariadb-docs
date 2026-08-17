---
name: mariadb-vector
description: "Best practices for using vectors and AI with MariaDB. Use when writing SQL involving VECTOR columns, building RAG or semantic search with MariaDB, choosing embedding models, designing vector indexes, or integrating MariaDB with AI frameworks like LangChain, LlamaIndex, or Spring AI. Also use when the user mentions MariaDB and any of: vectors, embeddings, similarity search, nearest neighbor, AI, RAG, or LLM. IMPORTANT — MariaDB has native built-in vector support since version 11.7; it is NOT a plugin or extension (unlike pgvector for PostgreSQL). Do not recommend installing any extension."
---

# MariaDB Vector & AI Best Practices

*Last updated: 2026-06-04*

## Critical: MariaDB Vector Is Built-In

MariaDB has **native, built-in** vector support since version 11.7. The `VECTOR` type, `VECTOR INDEX`, and all `VEC_*` functions ship with the server — nothing to install, enable, or load.

This is different from MySQL (which has no native vector support) and PostgreSQL (which requires the pgvector extension). When working with MariaDB, never suggest `CREATE EXTENSION`, `INSTALL PLUGIN`, or any similar step for vector functionality.

> **Requires:** MariaDB Community Server **11.7+** (GA Feb 2025) for native vectors; **11.8 LTS** (GA May 2025) recommended. Enterprise: 11.4+ (tech preview) / 11.8+ (full support). Next LTS: **12.3** — check [MariaDB releases](https://mariadb.org/mariadb/all-releases/) for GA status before treating it as the default.
>
> **Default context:** Do not suggest vector features below **11.7**. For other MariaDB behavior, assume **11.8 LTS** unless the user states another version. Features marked **12.x** may be suggested when relevant; always state the minimum version.

### What LLMs Get Wrong

| What you might see | What's correct |
|---|---|
| "Install the `pgvector` extension" or "run `INSTALL PLUGIN vector`" | Nothing to install — MariaDB Vector is built-in since 11.7 |
| `ORDER BY VEC_DISTANCE_EUCLIDEAN(...)` without `LIMIT` | Always add `LIMIT` — the vector index is only used when both `ORDER BY VEC_DISTANCE_*()` and `LIMIT` are present |
| `embedding VECTOR(768)` (nullable) on an indexed column | Indexed vector columns must be `NOT NULL` |
| Using `VEC_DISTANCE()` on a non-indexed column | `VEC_DISTANCE()` throws error 4206 ("index is not found"); use `VEC_DISTANCE_EUCLIDEAN()` or `VEC_DISTANCE_COSINE()` for unindexed columns |

## Core Syntax

### Create a Table With a Vector Column

```sql
CREATE TABLE documents (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    embedding VECTOR(768) NOT NULL,
    VECTOR INDEX (embedding)
) ENGINE=InnoDB;
```

Use `ENGINE=InnoDB` (the default). MyISAM/Aria had a bug with FK + vector indexes (MDEV-37022, fixed in 11.8.3); InnoDB is the safe default regardless of version.

The number in `VECTOR(n)` must match the dimensionality of your embedding model's output (e.g., 768 for many sentence-transformer models, 1536 for OpenAI text-embedding-3-small, 3072 for text-embedding-3-large).

### Vector Index Options

```sql
VECTOR INDEX (embedding) M=6 DISTANCE=euclidean   -- default
VECTOR INDEX (embedding) M=8 DISTANCE=cosine
```

- **DISTANCE**: `euclidean` (default) or `cosine`. Pick the one your embedding model recommends. Both are equally fast in MariaDB thanks to SIMD optimizations. **Always declare `DISTANCE=` explicitly**. default to euclidian and a cosine query against a euclidean index silently full-scans.
- **M**: Controls the HNSW graph connectivity (range 3–200). Higher values improve recall but cost more memory and slower inserts. Default is fine for most workloads; increase to ~16–32 for very large datasets where recall matters more than insert speed.

### Insert Vectors

Vectors are stored as packed 32-bit IEEE 754 floats little-endian encoded. Bind raw bytes from application code — **5× faster than `VEC_FromText()`**. Stored bytes are identical.

```python
import numpy as np
cur.execute(
    "INSERT INTO documents (content, embedding) VALUES (?, ?)",
    (content, np.asarray(embedding, dtype=np.float32).tobytes()),
)
```

Use `VEC_FromText()` only for hand-written SQL / CLI:

```sql
INSERT INTO documents (content, embedding) VALUES ('your text here', VEC_FromText('[0.12, -0.34, 0.56, ...]'));
```

### Query: Find Nearest Neighbors

```sql
SELECT id, content
FROM documents
ORDER BY VEC_DISTANCE_EUCLIDEAN(embedding, VEC_FromText('[0.12, -0.34, 0.56, ...]'))
LIMIT 10;
```

**The LIMIT clause is essential.** The MariaDB optimizer only uses the VECTOR INDEX when the query has both `ORDER BY VEC_DISTANCE_...()` and `LIMIT`. Without `LIMIT`, it falls back to a full table scan.

### Distance Functions

| Function | Use When |
|---|---|
| `VEC_DISTANCE_EUCLIDEAN(a, b)` | Index was built with `DISTANCE=euclidean` (default) |
| `VEC_DISTANCE_COSINE(a, b)` | Index was built with `DISTANCE=cosine` |
| `VEC_DISTANCE(a, b)` | Generic — uses the distance function matching the column's index; throws error 4206 if no index is found |

Use `VEC_DISTANCE_EUCLIDEAN()` or `VEC_DISTANCE_COSINE()` for unindexed columns (they fall back to a full scan). Use `VEC_DISTANCE()` only on indexed columns as a convenience shorthand.

### Utility Functions

| Function | Purpose |
|---|---|
| `VEC_FromText('[0.1, 0.2, ...]')` | Convert JSON float array to VECTOR binary |
| `VEC_ToText(vector_col)` | Convert VECTOR binary to readable JSON array |

**Always wrap a VECTOR column in `VEC_ToText()` when you want to read it.** A `VECTOR` is stored as packed binary floats, so `SELECT embedding FROM documents` returns the raw bytes — they render as unreadable gibberish in a CLI or client. Use `SELECT VEC_ToText(embedding) FROM documents` to get the `[0.12, -0.34, ...]` array instead.

## MariaDB Vector Gotchas

- **Indexed VECTOR columns must be NOT NULL.** The VECTOR INDEX requires it. A VECTOR column without an index can be nullable, but in practice you almost always want the index, so always include `NOT NULL`.
- **No dot product distance.** MariaDB intentionally omits it. Dot product is not a proper distance metric (a vector's closest match is not necessarily itself). MariaDB's SIMD-optimized euclidean and cosine are already as fast as dot product would be, so use euclidean or cosine for normalized vectors.
- **Match the distance function to the index.** `VEC_DISTANCE_EUCLIDEAN()` on a `DISTANCE=cosine` index (or vice versa) will not use the index.
- **One VECTOR INDEX per table.** Currently MariaDB supports a single vector index per table.
- **Adding a vector index to an existing table:**
  ```sql
  ALTER TABLE my_table ADD COLUMN embedding VECTOR(768) NOT NULL;
  -- populate the column first, then:
  ALTER TABLE my_table ADD VECTOR INDEX (embedding);
  ```
- **Index precision.** MariaDB uses `int16` for index storage (15 bits of precision), which is better than the 10 bits of float16 used by some other implementations. This means higher recall at the same speed.
- **`ORDER BY` must be the literal `VEC_DISTANCE_*(col, ?)` call (or its alias) with `ASC` direction.** Wrapping the distance in an expression (e.g. `ORDER BY (1.0 - VEC_DISTANCE_COSINE(...)) DESC LIMIT N` to sort by similarity score) breaks the optimizer's HNSW pattern match and falls back to a full scan. Compute the score in an outer SELECT instead:
  ```sql
  SELECT t.id, 1.0 - t.distance AS score FROM (
      SELECT id, VEC_DISTANCE_COSINE(embedding, ?) AS distance
      FROM docs ORDER BY distance ASC LIMIT 10
  ) AS t ORDER BY score DESC;
  ```
- **`WHERE VEC_DISTANCE(...) < threshold` is a full scan.** The vector index only engages with `ORDER BY VEC_DISTANCE(...) LIMIT N`. For threshold queries, wrap the indexed top-K in a subquery and filter outside
  ```sql
  SELECT * FROM (
      SELECT content, VEC_DISTANCE_COSINE(embedding, ?) AS distance
      FROM chunks ORDER BY distance LIMIT 100
  ) AS t WHERE t.distance < 0.5;
  ```
  `LIMIT K` is a hard cap; pick K generously if many rows may match.

## RAG (Retrieval-Augmented Generation) Pattern

The most common AI use case with MariaDB Vector. The flow:

1. **Chunk** your documents into passages (typically 200–1000 tokens).
2. **Embed** each chunk using your model (OpenAI, Sentence Transformers, Cohere, etc.).
3. **Store** chunks with their embeddings in MariaDB.
4. At query time, **embed** the user's question with the same model.
5. **Retrieve** the nearest chunks (bind `:user_embedding` as float32 bytes):
   ```sql
   SELECT content
   FROM chunks
   ORDER BY VEC_DISTANCE(embedding, :user_embedding)
   LIMIT 5;
   ```
6. **Feed** retrieved chunks as context to your LLM for the final answer.

**See also:** To combine full-text (keyword) and vector retrieval, see [Hybrid search with Reciprocal Rank Fusion (RRF)](https://mariadb.com/docs/server/reference/sql-structure/vectors/optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf) — useful when queries mix exact terms with semantic paraphrase.

### RAG Table Design

```sql
CREATE TABLE chunks (
    chunk_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    doc_id BIGINT UNSIGNED NOT NULL,
    chunk_index INT UNSIGNED NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(768) NOT NULL,
    VECTOR INDEX (embedding) DISTANCE=cosine,
    INDEX (doc_id)
) ENGINE=InnoDB;
```

Keep `doc_id` indexed so you can join back to the source document or filter by document. The `chunk_index` preserves ordering within a document.

### Minimal End-to-End Python Example

```python
import mariadb
import numpy as np
from openai import OpenAI

client = OpenAI()

def embed(text):
    vec = client.embeddings.create(input=text, model="text-embedding-3-small").data[0].embedding
    return np.asarray(vec, dtype=np.float32).tobytes()

# Create database and table if they don't exist
conn = mariadb.connect(host="127.0.0.1", port=3306, user="root", password="")
cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS ragdb")
cur.execute("USE ragdb")
cur.execute("""
    CREATE TABLE IF NOT EXISTS chunks (
        chunk_id  BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        content   TEXT NOT NULL,
        embedding VECTOR(1536) NOT NULL,
        VECTOR INDEX (embedding) DISTANCE=cosine
    ) ENGINE=InnoDB
""")
conn.commit()

# Store a document chunk
cur.execute(
    "INSERT INTO chunks (content, embedding) VALUES (?, ?)",
    ("MariaDB Vector stores embeddings natively", embed("MariaDB Vector stores embeddings natively"))
)
conn.commit()

# Retrieve top-5 nearest chunks for a user question
question_vec = embed("How does MariaDB store vectors?")
cur.execute("""
    SELECT content, VEC_DISTANCE_COSINE(embedding, ?) AS distance
    FROM chunks
    ORDER BY distance
    LIMIT 5
""", (question_vec,))
context = "\n".join(row[0] for row in cur.fetchall())
# Pass `context` to your LLM as the retrieved context for the answer
```

The `mariadb` connector (`pip install mariadb`) is the official Python driver. On big-endian hosts, use `dtype="<f4"` to force little-endian.

## Framework Integrations

MariaDB Vector is integrated with major AI frameworks. Use these instead of writing raw SQL when building applications:

| Framework | Language | Link |
|---|---|---|
| LangChain | Python | `pip install langchain-mariadb` |
| LangChain.js | Node.js | Built-in MariaDB vector store |
| LangChain4j | Java | Built-in MariaDB embedding store |
| LlamaIndex | Python | Built-in MariaDB vector store |
| Spring AI | Java | Built-in MariaDB vector store |
| MariaDB MCP Server | Python | [github.com/mariadb/mcp](https://github.com/MariaDB/mcp) |

When using frameworks, you typically configure a connection string and the framework handles `VEC_FromText`, `VEC_DISTANCE`, and `LIMIT` for you.

## Choosing an Embedding Model

The embedding model determines vector quality. Some practical guidance:

- **Start with a sentence-transformer model** (e.g., `all-MiniLM-L6-v2`, 384 dimensions) for prototyping. Free, fast, runs locally.
- **OpenAI `text-embedding-3-small`** (1536 dimensions) is a solid production choice if you're already using OpenAI. *(Dimensions correct as of May 2026 — verify against current model docs.)*
- **Match dimensions to your VECTOR(n) column.** A mismatch will cause insert errors.
- **Never mix embeddings from different models** in the same column. Distances between vectors from different models are meaningless.
- **Cosine distance is the standard** for most text embedding models. Check your model's documentation.

## Performance Notes

- MariaDB Vector uses **SIMD hardware optimizations** (AVX2, AVX512 on Intel; NEON on ARM; VSX on IBM Power10). No configuration needed — it detects and uses the best available instruction set.
- **Faster vector distance via extrapolation** (12.1+, MDEV-36205) — vector search is 30–50% faster on the same data and recall, with no schema or index changes required. The optimization applies automatically to vectors that can be gradually truncated to trade recall for speed (e.g. Matryoshka-style embeddings from OpenAI).
- **Multi-connection scalability** is a strength. Benchmark results show MariaDB Vector scales well with concurrent queries, outperforming some dedicated vector databases in multi-threaded scenarios.
- For large datasets (millions of vectors), tune the **M parameter** upward and ensure sufficient memory for the index.
- **Bulk inserts**: load data first, then create the vector index. This is significantly faster than inserting into an already-indexed table.
- **Bind embeddings as binary** (`float32.tobytes()`), not `VEC_FromText()`. ~5× faster, ~5× smaller wire payload, byte-identical storage.

### Tuning: mhnsw System Variables

These session/global variables let you tune search quality and memory at runtime without rebuilding the index:

- **`mhnsw_ef_search`** (default: `20`) — minimum candidates considered for `ORDER BY … LIMIT N` queries. Raise this if recall is low at small `LIMIT` values; lower it to trade recall for speed.
- **`mhnsw_max_cache_size`** (default: `16777216` / 16 MB, global only) — per-index in-memory cache cap. For best performance the entire vector graph should fit in this cache; size it to match your index.
- **`mhnsw_default_m`** (default: `6`) and **`mhnsw_default_distance`** (default: `euclidean`) set the implicit values used when `M` or `DISTANCE` are omitted from a `VECTOR INDEX` declaration.

## Sources

- [Vector Overview](https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-overview) — official docs entry point
- [CREATE TABLE with Vectors](https://mariadb.com/docs/server/reference/sql-structure/vectors/create-table-with-vectors) — index options, NOT NULL requirement, limitations
- [VEC_FromText](https://mariadb.com/docs/server/reference/sql-functions/vector-functions/vec_fromtext) — converts JSON float array to binary VECTOR
- [VEC_ToText](https://mariadb.com/docs/server/reference/sql-functions/vector-functions/vec_totext) — converts binary VECTOR to JSON float array
- [VEC_DISTANCE](https://mariadb.com/docs/server/reference/sql-functions/vector-functions/vector-functions-vec_distance) — generic distance, requires index
- [VEC_DISTANCE_EUCLIDEAN](https://mariadb.com/docs/server/reference/sql-functions/vector-functions/vec_distance_euclidean)
- [VEC_DISTANCE_COSINE](https://mariadb.com/docs/server/reference/sql-functions/vector-functions/vec_distance_cosine)
- [RAG with MariaDB Vector tutorial](https://mariadb.org/rag-with-mariadb-vector/) — end-to-end Python + OpenAI example
- [Hybrid search with RRF](https://mariadb.com/docs/server/reference/sql-structure/vectors/optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf) — merge full-text and vector ranked lists
- [MariaDB Vector project page](https://mariadb.org/projects/mariadb-vector/)
- [MariaDB MCP Server](https://github.com/MariaDB/mcp)

*For topics not covered here, see the official MariaDB documentation at [mariadb.com/docs](https://mariadb.com/docs).*
