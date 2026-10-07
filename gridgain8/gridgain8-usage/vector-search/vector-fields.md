---
description: >-
  Define vector fields in GridGain with the QueryVectorField annotation and set
  the similarity function per field, in Java and Python.
---

# Vector Fields

When creating the field for a vector, mark the field that will hold the vector with the `QueryVectorField` annotation. This field must have the `float[]` type. GridGain will create a vector index based on the provided embedding.

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

## Setting the Similarity Function

You can choose which [similarity function](similarity-functions.md) a vector field uses through the `similarityFunction` parameter of the `QueryVectorField` annotation. The example below shows a class with a vector field configured with a similarity function:

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
