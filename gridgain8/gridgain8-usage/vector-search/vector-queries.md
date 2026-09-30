---
description: >-
  Run vector similarity queries in GridGain with VectorQuery, controlling the
  number of nearest neighbors and an optional similarity threshold.
---

# Vector Queries

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
