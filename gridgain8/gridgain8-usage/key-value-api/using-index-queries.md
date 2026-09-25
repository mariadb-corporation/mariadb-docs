---
description: >-
  Use IndexQuery to retrieve cache entries that match query criteria over distributed indexes.
---

# Executing Index Queries

{% hint style="warning" %}
Experimental API. Introduced in GridGain 8.9.2. Only Java API is supported.
{% endhint %}

Index queries work over distributed indexes and retrieve cache entries that match the specified query.  `IndexQuery` can be used if a low amount of data
matches filtering criteria. For these cases, [`ScanQuery`](using-scan-queries.md) usage is not optimal.

```java
// Create index by 2 fields (orgId, salary).
LinkedHashMap<String,String> fields = new LinkedHashMap<>();
  fields.put("orgId", Integer.class.getName());
  fields.put("salary", Integer.class.getName());

QueryEntity personEntity = new QueryEntity(Integer.class, Person.class)
  .setFields(fields)
  .setIndexes(Collections.singletonList(
      new QueryIndex(Arrays.asList("orgId", "salary"), QueryIndexType.SORTED)
          .setName("ORG_SALARY_IDX")
  ));

CacheConfiguration<Integer, Person> ccfg = new CacheConfiguration<Integer, Person>("entityCache")
  .setQueryEntities(Collections.singletonList(personEntity));

IgniteCache<Integer, Person> cache = ignite.getOrCreateCache(ccfg);

// Find the persons who work in Organization 1.
QueryCursor<Cache.Entry<Integer, Person>> cursor = cache.query(
  new IndexQuery<Integer, Person>(Person.class, "ORG_SALARY_IDX")
      .setCriteria(eq("orgId", 1))
);
```

Index query criteria are defined in the `IndexQueryCriteriaBuilder`. Criteria fields have to match the specified index.
For example, if there is an index defined with (A, B) set, then valid criteria sets are (A) and (A, B).
Criteria with the single (B) field will be executed without using an index because the field (B) is not a prefix set of the specified index fields,
and it's impossible to build a narrow index range with it.

{% hint style="info" %}
Criteria are joined by the AND operator. It is also possible to use multiple criteria for the same field.
{% endhint %}

```java
// Find the persons who work in Organization 1 and have salary more than 1,000.
QueryCursor<Cache.Entry<Integer, Person>> cursor = cache.query(
    new IndexQuery<Integer, Person>(Person.class, "ORG_SALARY_IDX")
        .setCriteria(eq("orgId", 1), gt("salary", 1000))
);
```

The index name is an optional parameter. In this case, GridGain tries to figure out the index by itself using specified criteria fields.

```java
// GridGain finds suitable index "ORG_SALARY_IDX" by specified criterion field "orgId".
QueryCursor<Cache.Entry<Integer, Person>> cursor = cache.query(
    new IndexQuery<Integer, Person>(Person.class)
        .setCriteria(eq("orgId", 1))
);
```

For the empty criteria list, a full table scan is performed.

## Additional filtering

`IndexQuery` also supports an optional predicate, the same as `ScanQuery` has. It's suitable for additional cache entry
filtering. For example, it may contain some logic or the "OR" operations.

```java
// Find the persons who work in Organization 1 and whose name contains 'Vasya'.
QueryCursor<Cache.Entry<Integer, Person>> cursor = cache.query(
    new IndexQuery<Integer, Person>(Person.class)
        .setCriteria(eq("orgId", 1))
        .setFilter((k, v) -> v.getName().contains("Vasya"))
);
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
