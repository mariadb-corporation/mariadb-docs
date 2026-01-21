---
description: >-
  Calculate Cosine distance. This function computes the Cosine distance between
  two vectors, measuring the cosine of the angle between them.
---

# VEC\_DISTANCE\_COSINE

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/pBQsCgBA6SJpi0m3pZuk/" %}

{% include "../../../.gitbook/includes/vectors-are-available-from-....md" %}

## Syntax

```sql
VEC_DISTANCE_COSINE(v, s)
```

## Description

`VEC_Distance_Cosine` is an SQL function that calculates the [Cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity#Cosine_distance) between two (not necessarily normalized) vectors.

Vectors must be of the same length. A distance between two vectors of different lengths is not defined, and `VEC_Distance_Cosine` will return `NULL` in such cases.

If the vector index was not built for the cosine function (see [CREATE TABLE with Vectors](../../sql-structure/vectors/create-table-with-vectors.md)), the index is not used — a full table scan is performed instead. The [VEC\_DISTANCE](vector-functions-vec_distance.md) function is a generic function that behaves either as [VEC\_DISTANCE\_EUCLIDEAN](vec_distance_euclidean.md) or `VEC_DISTANCE_COSINE`, depending on the underlying index type.

## Example

```sql
SELECT VEC_DISTANCE_COSINE(vec_fromtext('[1,2,3]'), vec_fromtext('[3,5,7]'));
+-----------------------------------------------------------------------+
| VEC_DISTANCE_COSINE(vec_fromtext('[1,2,3]'), vec_fromtext('[3,5,7]')) |
+-----------------------------------------------------------------------+
|                                                   0.00258509695694209 |
+-----------------------------------------------------------------------+
```

## See Also

* [VEC\_DISTANCE](vector-functions-vec_distance.md)
* [VEC\_DISTANCE\_EUCLIDEAN](vec_distance_euclidean.md)
* [Vector Overview](../../sql-structure/vectors/vector-overview.md)
* [CREATE TABLE with Vectors](../../sql-structure/vectors/create-table-with-vectors.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
