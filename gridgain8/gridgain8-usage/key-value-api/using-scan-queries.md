---
description: >-
  Use scan queries to retrieve cache entries in a distributed manner, with optional predicates, transformers, and local or asynchronous execution.
---

# Using Scan Queries

## Overview

`IgniteCache` has several query methods, all of which receive a subclass of the `Query` class and return a `QueryCursor`.

A `Query` represents an abstract paginated query to be executed on a cache.
The page size is configurable via the `Query.setPageSize(...)` method (default is 1024).

`QueryCursor` represents the query result set and allows for transparent page-by-page iteration.
When a user starts iterating over the last page, `QueryCursor` automatically requests the next page in the background.
For cases when pagination is not needed, you can use the `QueryCursor.getAll()` method, which fetches the entries and stores them in a collection.

{% hint style="info" %}
**Closing Cursors**

Cursors close automatically when you call the `QueryCursor.getAll()` method. If you are iterating over the cursor in a for loop or explicitly getting an `Iterator`, you must close the cursor explicitly or use a  try-with-resources statement.
{% endhint %}

## Executing Scan Queries

A scan query is a simple search query used to retrieve data from a cache in a distributed manner. When executed without parameters, a scan query returns all entries from the cache.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, Person> cache = ignite.getOrCreateCache("myCache");

QueryCursor<Cache.Entry<Integer, Person>> cursor = cache.query(new ScanQuery<>());
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cursor = cache.Query(new ScanQuery<int, Person>());
```
{% endtab %}
{% tab title="C++" %}
```cpp
Cache<int64_t, Person> cache = ignite.GetOrCreateCache<int64_t, ignite::Person>("personCache");

QueryCursor<int64_t, Person> cursor = cache.Query(ScanQuery());
```
{% endtab %}
{% endtabs %}

Scan queries return entries that match a predicate, if specified. The predicate is applied on the remote nodes.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, Person> cache = ignite.getOrCreateCache("myCache");

// Find the persons who earn more than 1,000.
IgniteBiPredicate<Integer, Person> filter = (key, p) -> p.getSalary() > 1000;

try (QueryCursor<Cache.Entry<Integer, Person>> qryCursor = cache.query(new ScanQuery<>(filter))) {
    qryCursor.forEach(
            entry -> System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue()));
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class SalaryFilter : ICacheEntryFilter<int, Person>
{
    public bool Invoke(ICacheEntry<int, Person> entry)
    {
        return entry.Value.Salary > 1000;
    }
}

public static void ScanQueryFilterDemo()
{
    var ignite = Ignition.Start();
    var cache = ignite.GetOrCreateCache<int, Person>("person_cache");

    cache.Put(1, new Person {Name = "person1", Salary = 1001});
    cache.Put(2, new Person {Name = "person2", Salary = 999});

    using (var cursor = cache.Query(new ScanQuery<int, Person>(new SalaryFilter())))
    {
        foreach (var entry in cursor)
        {
            Console.WriteLine("Key = " + entry.Key + ", Value = " + entry.Value);
        }
    }
}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Scan queries also support an optional transformer closure which lets you convert the entry on the server node before sending it back. This is useful, for example, when you want to fetch only several fields of a large object and want to minimize the network traffic. The example below shows how to fetch only the keys without sending the values.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, Person> cache = ignite.getOrCreateCache("myCache");

// Get only keys for persons earning more than 1,000.
List<Integer> keys = cache.query(new ScanQuery<>(
        // Remote filter
        (IgniteBiPredicate<Integer, Person>) (k, p) -> p.getSalary() > 1000),
        // Transformer
        (IgniteClosure<Cache.Entry<Integer, Person>, Integer>) Cache.Entry::getKey).getAll();
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Asynchronous Scan Queries

In .NET, a query cursor (`IQueryCursor`) implements `IAsyncEnumerable<T>` and `IAsyncDisposable` in addition to `IEnumerable<T>` and `IDisposable`. This lets you iterate the results with `await foreach` and release the cursor's server-side resources with `await using`, without blocking the calling thread on network I/O.

`Query` returns the cursor as usual; each page is then fetched without blocking the calling thread as you iterate:

{% code title="C#/.NET" %}
```csharp
// Query() returns the cursor; the cursor implements IAsyncEnumerable, so each page
// is fetched without blocking the calling thread as you iterate with await foreach.
await foreach (var entry in cache.Query(new ScanQuery<int, Person>()))
{
    Console.WriteLine("Key = " + entry.Key + ", Name = " + entry.Value.Name);
}
```
{% endcode %}

{% hint style="info" %}
A cursor can be enumerated only once. Calling `GetAll()` and then iterating the same cursor (or iterating it twice) throws an `InvalidOperationException`. Pass a `CancellationToken` with `.WithCancellation(token)` to stop iteration early.
{% endhint %}

To release the cursor asynchronously as well, wrap it in an `await using` block:

{% tabs %}
{% tab title="C#/.NET" %}
```csharp
await using (var cursor = cache.Query(new ScanQuery<int, Person>()))
{
    await foreach (var entry in cursor)
        Console.WriteLine($"{entry.Key} = {entry.Value.Name}");
}
// DisposeAsync releases the server-side query resources without blocking the
// calling thread; "await foreach" iterates the cursor asynchronously.
```
{% endtab %}
{% tab title="Java" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Local Scan Query

By default, a scan query is distributed to all nodes.
However, you can execute the query locally, in which case the query runs against the data stored on the local node (i.e. the node where the query is executed).

{% tabs %}
{% tab title="Java" %}
```java
QueryCursor<Cache.Entry<Integer, Person>> cursor = cache
        .query(new ScanQuery<Integer, Person>().setLocal(true));
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var query = new ScanQuery<int, Person> {Local = true};
var cursor = cache.Query(query);
```
{% endtab %}
{% tab title="C++" %}
```cpp
ScanQuery sq;
sq.SetLocal(true);

QueryCursor<int64_t, Person> cursor = cache.Query(sq);
```
{% endtab %}
{% endtabs %}

## Related Topics

- [Execute scan query via REST API](../../reference/rest-api/README.md#sql-scan-query-execute)
- [Cache Query Events](../events/events.md#cache-query-events)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
