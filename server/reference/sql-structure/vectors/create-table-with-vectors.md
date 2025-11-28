---
description: >-
  Create tables optimized for vector storage. Learn to define columns with the
  VECTOR data type and configure vector indexes for similarity search.
---

# CREATE TABLE with Vectors

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/pBQsCgBA6SJpi0m3pZuk/" %}

{% include "../../../.gitbook/includes/vectors-are-available-from-....md" %}

MariaDB has a dedicated [VECTOR(N)](../../data-types/numeric-data-types/vector.md) data type with a built-in data validation. `N` is the number of dimensions that all vector values in the column have.

{% hint style="info" %}
* Vector indexes are dimensionality-specific.
* All vectors inserted into an indexed column must match the index's target dimensionality.
* Inserting vectors with different dimensionalities will result in an error.
{% endhint %}

Consider the following table:

```sql
CREATE TABLE embeddings (
        doc_id BIGINT UNSIGNED PRIMARY KEY,
        embedding VECTOR(1536)
);
```

To have a fast vector search, you have to index the vector column, creating a `VECTOR` index:

```sql
CREATE TABLE embeddings (
        doc_id BIGINT UNSIGNED PRIMARY KEY,
        embedding VECTOR(1536) NOT NULL,
        VECTOR INDEX (embedding)
);
```

{% hint style="warning" %}
Note that there can be only one vector index in the table, and the indexed vector column must be `NOT NULL`.
{% endhint %}

There are two options that can be used to configure the vector index:

* `M` — Larger values mean slower `SELECT` and `INSERT` statements, larger index size and higher memory consumption, but more accurate results. The valid range is from `3` to `200`.
* `DISTANCE` — Distance function to build the vector index for. Searches using a different distance function will not be able to use a vector index. Valid values are `cosine` and `euclidean` (the default).

```sql
CREATE TABLE embeddings (
        doc_id BIGINT UNSIGNED PRIMARY KEY,
        embedding VECTOR(1536) NOT NULL,
        VECTOR INDEX (embedding) M=8 DISTANCE=cosine
);
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
