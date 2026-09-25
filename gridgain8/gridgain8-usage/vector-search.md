---
description: >-
  How to index and search vectors stored in cache fields in GridGain, including
  vector fields, vector queries, and similarity functions.
---

# Vector Search

GridGain can index vectors stored in a field and then search the cache based on the provided vector.

## Requirements

- GridGain must be running on Java 11 or later.
- GridGain license must provide access to vector search feature.
- Vector search can only be implemented for [REPLICATED](../architecture/data-modeling/data-partitioning.md#replicated) caches.
- Vectors for the field must be acquired by using a separate model, as no model is provided with GridGain.

## Installation

To start using vector store, enable the optional  `gridgain-vector-query` [module](setup.md#enabling-modules).

## Vector Fields

When creating the field for vector, mark the field that will hold the vector with the `QueryVectorField` annotation. This field must have the `float[]` type. GridGain will create a vector index based on the provided embedding.

The example below shows a class that uses a text field and a vector field:

```java
public class Article {
    /**
     * Content (indexed).
     */
    @QueryTextField
    private String content;

    @QueryVectorField
    private float[] contentVector;

    /**
     * Required for binary deserialization.
     */
    public Article() {
        // No-op.
    }

    public Article(String contentVector, float[] contentVec) {
        this.contentVector = contentVector;
        this.vec = contentVec;
    }
}
```

Objects with vector fields can be stored as normal. GridGain will build an additional index for the vector column that can be queried.

## Performing a Vector Query

To perform a vector query, you would need a search vector provided by the same model as the one used to create the original vectors for the database objects. In this example, we will assume that you have procured the required vector already. Once the vector is available, you can use the `VectorQuery` object to create a query and send it to the cluster with the `query` method:

```java
float[] searchVector = // get from model
VectorQuery myQuery = new VectorQuery(Article.class, "myField", searchVector, 5)
cache.query(myQuery).getAll());
```

The `VectorQuery` constructor accepts the following parameters:

- The first parameter specifies the Article object representing the cache entry type.
- The second parameter specifies the name of the vector field that will be searched.
- The third parameter specifies the previously obtained search vector.
- The fourth parameter specifies the maximum number of results to return. This parameter, often referred to as `k` in nearest neighbor searches, determines how many nearest neighbors the query will retrieve.
- You can also specify an optional fifth threshold parameter to control the quality of results returned, for example:

  ```java
  float[] searchVector = // get from model
  // Using the overloaded constructor with threshold parameter
  VectorQuery myQuery = new VectorQuery(Article.class, "myField", searchVector, 5, 0.75)
  cache.query(myQuery).getAll());
  ```

  The threshold must be a float value between 0.0 and 1.0, where higher values mean the results must be more similar to the search vector. This example returns up to 5 nearest neighbors, but only those that have a similarity score of at least 0.75. If fewer than 5 neighbors meet this threshold, fewer results will be returned.
  Using a threshold can help ensure that your search only returns relevant results and filters out vectors that are too dissimilar from the search vector.

## Similarity Functions

GridGain supports **COSINE**, **EUCLIDEAN**, **DOT_PRODUCT** and **MAXIMUM_INNER_PRODUCT** similarity functions for vector search. Simililarity function is configurable at the query index level.

### Compatibility

When updating to 8.9.23, similarity function for all indexes without it will default to COSINE. If a newer version of the server is used with the older version of the client, the client will always default to COSINE function regardless of the function used.

### Function Comparison

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

### Similarity Vector Field

When creating the field for vector, mark the field that will hold the vector with the QueryVectorField annotation. This field must have the `float[]` type. GridGain will create a vector index based on the provided embedding.

The example below shows a class that uses a vector field with Similarity function:

{% tabs %}
{% tab title="Java" %}
```java
public class Article {
    /**
     * Content (indexed).
     */
    private String content;

    // Set the similarity function to use. Possible values:
    //COSINE | DOT_PRODUCT | EUCLIDEAN | MAXIMUM_INNER_PRODUCT
    @QueryVectorField(similarityFunction = COSINE)
    private float[] vec;

    /**
     * Required for binary deserialization.
     */
    public Article() {
        // No-op.
    }

    public Article(String content, float[] contentVec) {
        this.content = content;
        this.vec = contentVec;
    }

    /** {@inheritDoc} */
    @Override public String toString() {
        return "Article [content=" + content +
                ", vec=" + vec + ']';
    }

    public String getContent(){
        return content;
    }
}
```
{% endtab %}

{% tab title="Python" %}
```python
def cache_config(cache_name):
    return {
        PROP_NAME: cache_name,
        PROP_CACHE_MODE: CacheMode.REPLICATED,
        PROP_CACHE_ATOMICITY_MODE: CacheAtomicityMode.TRANSACTIONAL,
        PROP_WRITE_SYNCHRONIZATION_MODE: WriteSynchronizationMode.FULL_SYNC,
        PROP_QUERY_ENTITIES: [{
            'table_name': cache_name,
            'key_field_name': 'id',
            'key_type_name': 'java.lang.Long',
            'value_field_name': None,
            'value_type_name': Article.type_name,
            'field_name_aliases': [],
            'query_fields': [
                {
                    'name': 'id',
                    'type_name': 'java.lang.Long'
                },
                {
                    'name': 'title',
                    'type_name': 'java.lang.String'
                },
                {
                    'name': 'vec',
                    'type_name': '[F'
                }
            ],
            'query_indexes': [
                {
                    'index_name': 'vec',
                    'index_type': IndexType.VECTOR,
                    'inline_size': 1024,
                    #- Set `similarity_function: 0` for COSINE
                    #- Set `similarity_function: 1` for DOT_PRODUCT
                    #- Set `similarity_function: 2` for EUCLIDEAN
                    #- Set `similarity_function: 3` for MAXIMUM_INNER_PRODUCT

                    'similarity_function': 0,   # defaults to COSINE
                    'fields': [
                        {
                            'name': 'vec'
                        }
                    ]
                }
            ]
        }],
    }
```
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
