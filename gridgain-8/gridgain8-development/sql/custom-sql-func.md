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
// The 'sqr' function is registered on the "myCache" cache, so it belongs to
// the "myCache" SQL schema. This schema name is case-sensitive by default,
// so it must be quoted and used to qualify the function.
SqlFieldsQuery query = new SqlFieldsQuery("SELECT name FROM Person WHERE \"myCache\".sqr(age) > 100");

// Executing the query.
cache.query(query).getAll();
```

{% hint style="info" %}
Classes registered with `CacheConfiguration.setSqlFunctionClasses(...)` must be added to the classpath of all the nodes where the defined custom functions might be executed. Otherwise, you will get a `ClassNotFoundException` error when trying to execute the custom function.
{% endhint %}

## Function Scope and SQL Schema

A custom SQL function is registered in the SQL schema of the cache it is defined on. You can call the function against a table in any schema, or on its own, as long as you address it through its schema.

By default, the schema of a cache has the same name as the cache and is case-sensitive. To use it, you must enclose the schema name in double quotes:

```sql
SELECT name FROM Person WHERE "myCache".sqr(age) > 100;

SELECT "myCache".sqr(42);
```

To avoid quoting, assign the cache an explicit, case-insensitive schema with the `CacheConfiguration.setSqlSchema(...)` method. If you set the schema to `PUBLIC`, the function is registered in the default schema and can be called without a qualifier:

{% tabs %}
{% tab title="Java" %}
```java
CacheConfiguration cfg = new CacheConfiguration("myCache");
cfg.setSqlFunctionClasses(SQLFunctions.class);

// Register the functions in the PUBLIC schema so no qualifier is needed.
cfg.setSqlSchema("PUBLIC");

IgniteCache cache = ignite.createCache(cfg);
```
{% endtab %}

{% tab title="SQL" %}
```sql
SELECT name FROM Person WHERE sqr(age) > 100;
SELECT sqr(42);
```
{% endtab %}
{% endtabs %}

For more information about how cache and schema names relate, see the [Understanding Schemas](schemas.md) page.
