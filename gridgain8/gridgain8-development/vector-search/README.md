---
description: >-
  Index and search vectors stored in cache fields in GridGain — vector fields,
  vector queries, and configurable similarity functions.
---

# Vector Search

GridGain can index vectors stored in a field and then search the cache based on the provided vector. This enables similarity search over embeddings — for use cases such as semantic search, recommendations, and retrieval-augmented generation (RAG) — directly against data held in GridGain caches.

## Requirements

- GridGain must be running on Java 11 or later.
- GridGain license must provide access to vector search feature.
- Vector search can only be implemented for [REPLICATED](../../architecture/data-modeling/data-partitioning.md#replicated) caches.
- Vectors for the field must be acquired by using a separate model, as no model is provided with GridGain.

## Installation

To start using vector store, enable the optional `gridgain-vector-query` [module](../project-setup.md#enabling-modules).

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
Run vector similarity queries with VectorQuery, controlling the number of nearest neighbors and an optional similarity threshold.
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
