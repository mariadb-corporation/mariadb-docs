---
description: >-
  Implementing a custom CacheStore in GridGain to use an external data store as
  the underlying storage for a cache, with a JDBC example.
---

# Implementing Custom Cache Store

You can implement your own custom `CacheStore` and use it as an underlying data storage for the cache. The methods of `IgniteCache` that read or modify the data will call the corresponding methods of the `CacheStore` implementation.

The following table describes the methods of the `CacheStore` interface.

| Method | Description |
|---|---|
| `loadCache()` | The `loadCache(...)` method is called whenever `IgniteCache.loadCache(...)` is called and is usually used to preload data from the underlying database into memory. This method loads data on all nodes on which the cache is present.<br><br>To load the data on a single node, call `IgniteCache.localLoadCache()` on that node. |
| `load()`, `write()`, `delete()` | The `load()`, `write()`, and `delete()` methods are called whenever the `get()`, `put()`, and `remove()` methods are called on the `IgniteCache` interface. These methods are used to enable the _read-through_ and _write-through_ behavior when working with individual cache entries. |
| `loadAll()`, `writeAll()`, `deleteAll()` | `loadAll()`, `writeAll()`, and `deleteAll()` in the `CacheStore` are called whenever methods `getAll()`, `putAll()`, and `removeAll()` are called on the `IgniteCache` interface. These methods are used to enable the read-through and write-through behavior when working with multiple cache entries and should generally be implemented using batch operations to provide better performance. |

## CacheStoreAdapter

`CacheStoreAdapter` is an extension of `CacheStore` that provides default implementations for bulk operations, such as `loadAll(Iterable)`, `writeAll(Collection)`, and `deleteAll(Collection)`, by iterating through all entries and calling corresponding `load()`, `write()`, and `delete()` operations on individual entries.

## CacheStoreSession

Cache store sessions are used to hold the context between multiple operations on the store and mainly employed to provide transactional support. The operations within one transaction are executed using the same database connection, and the connection is committed when the transaction commits.
Cache store session is represented by an object of the `CacheStoreSession` class, which can be injected into your `CacheStore` implementation via the `@GridCacheStoreSessionResource` annotation.

## Example

Below is an example of a non-transactional implementation of `CacheStore`.

{% code title="JDBC non-transactional" %}
```java
public class CacheJdbcPersonStore extends CacheStoreAdapter<Long, Person> {
    // This method is called whenever the "get(...)" methods are called on IgniteCache.
    @Override
    public Person load(Long key) {
        try (Connection conn = connection()) {
            try (PreparedStatement st = conn.prepareStatement("select * from PERSON where id=?")) {
                st.setLong(1, key);

                ResultSet rs = st.executeQuery();

                return rs.next() ? new Person(rs.getInt(1), rs.getString(2)) : null;
            }
        } catch (SQLException e) {
            throw new CacheLoaderException("Failed to load: " + key, e);
        }
    }

    @Override
    public void write(Entry<? extends Long, ? extends Person> entry) throws CacheWriterException {
        try (Connection conn = connection()) {
            // Syntax of MERGE statement is database specific and should be adopted for your database.
            // If your database does not support MERGE statement then use sequentially
            // update, insert statements.
            try (PreparedStatement st = conn.prepareStatement("merge into PERSON (id, name) key (id) VALUES (?, ?)")) {
                Person val = entry.getValue();

                st.setLong(1, entry.getKey());
                st.setString(2, val.getName());

                st.executeUpdate();
            }
        } catch (SQLException e) {
            throw new CacheWriterException("Failed to write entry (" + entry + ")", e);
        }
    }

    // This method is called whenever the "remove(...)" method are called on IgniteCache.
    @Override
    public void delete(Object key) {
        try (Connection conn = connection()) {
            try (PreparedStatement st = conn.prepareStatement("delete from PERSON where id=?")) {
                st.setLong(1, (Long) key);

                st.executeUpdate();
            }
        } catch (SQLException e) {
            throw new CacheWriterException("Failed to delete: " + key, e);
        }
    }

    // This method is called whenever the "loadCache()" and "localLoadCache()"
    // methods are called on IgniteCache. It is used for bulk-loading the cache.
    // If you don't need to bulk-load the cache, skip this method.
    @Override
    public void loadCache(IgniteBiInClosure<Long, Person> clo, Object... args) {
        if (args == null || args.length == 0 || args[0] == null)
            throw new CacheLoaderException("Expected entry count parameter is not provided.");

        final int entryCnt = (Integer) args[0];

        try (Connection conn = connection()) {
            try (PreparedStatement st = conn.prepareStatement("select * from PERSON")) {
                try (ResultSet rs = st.executeQuery()) {
                    int cnt = 0;

                    while (cnt < entryCnt && rs.next()) {
                        Person person = new Person(rs.getInt(1), rs.getString(2));
                        clo.apply(person.getId(), person);
                        cnt++;
                    }
                }
            }
        } catch (SQLException e) {
            throw new CacheLoaderException("Failed to load values from cache store.", e);
        }
    }

    // Open JDBC connection.
    private Connection connection() throws SQLException {
        // Open connection to your RDBMS systems (Oracle, MySQL, Postgres, DB2, Microsoft SQL, etc.)
        Connection conn = DriverManager.getConnection("jdbc:mysql://[host]:[port]/[database]", "YOUR_USER_NAME", "YOUR_PASSWORD");

        conn.setAutoCommit(true);

        return conn;
    }
}
```
{% endcode %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
