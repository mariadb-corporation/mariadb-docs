---
description: >-
  Extend the GridGain SQL function set with custom SQL functions written in Java and annotated with @QuerySqlFunction.
---

# Custom SQL Functions

The SQL Engine can extend the SQL functions' set, defined by the ANSI-99 specification, via the addition of custom SQL functions written in Java.

A custom SQL function is just a public static method marked by the `@QuerySqlFunction` annotation.

```java
@QuerySqlFunction
public static int sqr(int x) {
    return x * x;
}
```

The class that owns the custom SQL function has to be registered in the `CacheConfiguration`.
To do that, use the `setSqlFunctionClasses(...)` method.

```java
// Preparing a cache configuration.
CacheConfiguration cfg = new CacheConfiguration("myCache");

// Registering the class that contains custom SQL functions.
cfg.setSqlFunctionClasses(SQLFunctions.class);

IgniteCache cache = ignite.createCache(cfg);
```

Once you have deployed a cache with the above configuration, you can call the custom function from within SQL queries:

```java
// Preparing the query that uses the custom defined 'sqr' function.
SqlFieldsQuery query = new SqlFieldsQuery("SELECT name FROM myCache WHERE sqr(size) > 100");

// Executing the query.
cache.query(query).getAll();
```

{% hint style="info" %}
Classes registered with `CacheConfiguration.setSqlFunctionClasses(...)` must be added to the classpath of all the nodes where the defined custom functions might be executed. Otherwise, you will get a `ClassNotFoundException` error when trying to execute the custom function.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
