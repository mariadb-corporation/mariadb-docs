---
title: backported-features-11.4.5-3
---

### Vector Search

The vector search capability has now been added to the MariaDB Enterprise Server 11.4 release. The linked [blog post](https://mariadb.com/resources/blog/mariadb-vector-preview-is-out/) explains the idea of the new vector search feature in detail. ([MENT-2233](https://jira.mariadb.org/browse/MENT-2233))

### Vector Embeddings

Vector embeddings are numerical representations `[0.2, -0.5, 0.8, 0.1, ...]` that capture semantic meaning or features of data in a multi-dimensional space. The embedding transforms simple to complex data such as text, images, audio, or video into a series of numbers (a vector) where similar items are positioned together in the multi-dimensional vector space.

For example, a word embedding of the word "dog" would be close in a vector embedding space to the word "puppy", whereas "dog" would not be close to the word "airplane". The embedding representation can be used in similarity search, recommendation systems, or more generally in traditional AI/ML systems and GenAI systems.

### New Data Type VECTOR(N)

A new data type `VECTOR(N)` has been added to represent the vector column, where N is the number of dimensions.\
Example:

```sql
CREATE TABLE myVectorSearch (
    id INT PRIMARY KEY,
    v VECTOR(5) NOT NULL,
    VECTOR INDEX (v)
);
```

### Conversion Functions

`VEC_FromText()` converts a text representation of the vector (a json array of numbers) to a vector (little-endian IEEE float sequence of bytes, 4 bytes per float).

Example:

```sql
SELECT hex(vec_fromtext('[1,2,3]'));
```

```
+------------------------------+
| hex(vec_fromtext('[1,2,3]')) |
+------------------------------+
| 0000803F0000004000004040     |
+------------------------------+
```

`VEC_ToText()` converts a binary vector into a json array of numbers (floats).\
Example:

```sql
SELECT VEC_ToText(x'e360d63ebe554f3fcdbc523f4522193f5236083d');
```

```
+---------------------------------------------------------+
| VEC_ToText(x'e360d63ebe554f3fcdbc523f4522193f5236083d') |
+---------------------------------------------------------+
| [0.418708,0.809902,0.823193,0.598179,0.033255]          |
+---------------------------------------------------------+
```

### Comparison Functions

Comparing vectors, calculating how close they are, is the key functionality needed by an application working with vector search. Two functions exist for calculating the distance between vectors. Which one to use depends on the application and on how the vectors were generated.

`VEC_DISTANCE_EUCLIDEAN()` takes two vectors and computes the straight line (L2) Euclidean distance between two multi-dimensional points in the vector space

Example:

```sql
INSERT INTO v VALUES
    (1, x'e360d63ebe554f3fcdbc523f4522193f5236083d'),
    (2, x'f511303f72224a3fdd05fe3eb22a133ffae86a3f'),
    (3,x'f09baa3ea172763f123def3e0c7fe53e288bf33e'),
    (4,x'b97a523f2a193e3eb4f62e3f2d23583e9dd60d3f'),
    (5,x'f7c5df3e984b2b3e65e59d3d7376db3eac63773e'),
    (6,x'de01453ffa486d3f10aa4d3fdd66813c71cb163f'),
    (7,x'76edfc3e4b57243f10f8423fb158713f020bda3e'),
    (8,x'56926c3fdf098d3e2c8c5e3d1ad4953daa9d0b3e'),
    (9,x'7b713f3e5258323f80d1113d673b2b3f66e3583f'),
    (10,x'6ca1d43e9df91b3fe580da3e1c247d3f147cf33e');
```

```sql
SELECT id FROM v
    ORDER BY VEC_DISTANCE_EUCLIDEAN(v, x'6ca1d43e9df91b3fe580da3e1c247d3f147cf33e');
```

```
+----+
| id |
+----+
| 10 |
|  7 |
|  3 |
|  9 |
|  2 |
|  1 |
|  5 |
|  4 |
|  6 |
|  8 |
+----+
```

`VEC_DISTANCE_COSINE()` measures the cosine distance between two vectors in a multi-dimensional vector space

Example:

```sql
SELECT VEC_DISTANCE_COSINE(VEC_FROMTEXT('[1,2,3]'), VEC_FROMTEXT('[3,5,7]'));
```

```
+-----------------------------------------------------------------------+
| VEC_DISTANCE_COSINE(VEC_FROMTEXT('[1,2,3]'), VEC_FROMTEXT('[3,5,7]')) |
+-----------------------------------------------------------------------+
|                                                   0.00258509695694209 |
+-----------------------------------------------------------------------+
```

### Configuration Options

The vector search feature requires some [new system variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors/vector-system-variables) for controlling the general behavior. Four new system variables have been added:

* `mhnsw_max_cache_size` - Upper limit for one MHNSW vector index cache
* `mhnsw_default_distance` - Default value for the DISTANCE vector index option
* `mhnsw_default_m` - Default value for the M vector index option
* `mhnsw_ef_search` - Minimal number of result candidates to look for in the vector index for ORDER BY ... LIMIT N queries.
