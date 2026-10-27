---
description: >-
  The COSINE, EUCLIDEAN, DOT_PRODUCT, and MAXIMUM_INNER_PRODUCT similarity
  functions for GridGain vector search, with a comparison and compatibility notes.
---

# Similarity Functions

GridGain supports **COSINE**, **EUCLIDEAN**, **DOT_PRODUCT** and **MAXIMUM_INNER_PRODUCT** similarity functions for vector search. Simililarity function is configurable at the query index level. To set the function on a vector field, see [Vector Fields](vector-fields.md#setting-the-similarity-function).

## Compatibility

When updating to 8.9.23, similarity function for all indexes without it will default to COSINE. If a newer version of the server is used with the older version of the client, the client will always default to COSINE function regardless of the function used.

## Function Comparison

- **DOT_PRODUCT**: Optimized cosine similarity for pre-normalized vectors, for example, recommendation systems with normalized embeddings. Fastest performance when vectors can be normalized in advance. **DOT_PRODUCT** is the preferred method for cosine similarity when vectors can be normalized in advance.
  - **Speed**: Fastest, optimized similarity calculation.
  - **Memory**: Least usage - pre-normalized vectors, minimal runtime overhead.
  - **Storage**: Smallest footprint - pre-normalized vectors only.
- **MAXIMUM_INNER_PRODUCT**: Optimized for retrieval scenarios with unnormalized vectors,
for example, document search, image retrieval. Similar to **DOT_PRODUCT**, but preserves magnitude information for ranking.
  - **Speed**: Second fastest, DOT_PRODUCT performance without normalization requirement.
  - **Memory**: Moderate usage - original vectors with magnitude, no normalization calculations.
  - **Storage**: Standard footprint - original vectors with magnitude information preserved.
- **COSINE**: Measures angle between vectors, works well for low-medium dimensions, but suffers from convergence in high-dimensional spaces. Direction-focused, ignores magnitude. The COSINE function should be used when one cannot pre-normalize vectors.
  - **Speed**: Slower due to runtime normalization with square root operations.
  - **Memory**: More usage - original vectors + runtime magnitude calculations + temporary normalization storage.
  - **Storage**: Larger footprint - raw vectors + magnitude metadata.
- **EUCLIDEAN**: Works best for the high dimension vector, for example, embeddings with 1000+ dimensions from modern ML models. Accounts for both direction and magnitude. Less affected by dimensional convergence.
  - **Speed**: Slowest due to squared differences and square root operations.
  - **Memory**: Moderate usage - raw vectors + temporary storage for squared differences.
  - **Storage**: Standard footprint - raw vectors, no preprocessing required.
