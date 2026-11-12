---
description: >-
  Improve query performance by caching SELECT statement results. This filter
  stores result sets in memory, serving identical subsequent queries directly
  from MaxScale.
---

# MaxScale Cache

## Overview

The cache filter is a simple cache that is capable of caching the result of SELECTs, so that subsequent identical SELECTs are served directly by MaxScale, without the queries being routed to any server.

By _default_ the cache will be used and populated in the following circumstances:

* There is no explicit transaction active, that is, autocommit is used,
* there is an explicitly read-only transaction (that is,`START TRANSACTION READ ONLY`) active, or
* there is a transaction active and no statement that modifies the database has been performed.

In practice, the last bullet point basically means that if a transaction has been started with `BEGIN`, `START TRANSACTION` or `START TRANSACTION READ WRITE`, then the cache will be used and populated until the first `UPDATE`, `INSERT` or `DELETE` statement is encountered.

That is, in default mode the cache effectively causes the system to behave as if the _isolation level_ would be `READ COMMITTED`, irrespective of what the isolation level of the backends actually is.

The default behaviour can be altered using the configuration parameter [cache\_in\_transactions](cache-settings.md#cache_in_transactions).

By default it is assumed that all `SELECT` statements are cacheable, which means that also statements like `SELECT LOCALTIME` are cached. Please check [selects](cache-settings.md#selects) for how to change the default behaviour.

## Limitations

All of these limitations may be addressed in forthcoming releases.

### Prepared Statements

Resultsets of prepared statements are **not** cached.

### Multi-statements

Multi-statements are always sent to the backend and their result is **not** cached.

### Security

The cache is **not** aware of grants.

The implication is that unless the cache has been explicitly configured who the caching should apply to, the presence of the cache may provide a user with access to data he should not have access to.

Please read the section [Security](#security-1) for more detailed information.

However, it is possible to configure the cache to cache the data of each user separately, which effectively means that there can be no unintended sharing. Please see [users](cache-settings.md#users) for how to change the default behaviour.

### `information_schema`

When [invalidation](#invalidation) is enabled, SELECTs targeting tables in `information_schema` are not cached. The reason is that as the content of the tables changes as the side-effect of something else, the cache would not know when to invalidate the cache-entries.

## Invalidation

The cache is capable of invalidating entries in the cache when a
modification (UPDATE, INSERT or DELETE) that may affect those entries is made. However,
the invalidation depends upon the used storage also supporting invalidation.

| Storage                                 | Invalidation |
| ----------------------------------------| ------------ |
| [storage_gridgain](cache-storage.md#storage_gridgain)   | No           |
| [storage_inmemory](cache-storage.md#storage_inmemory)   | Yes          |
| [storage_memcached](cache-storage.md#storage_memcached) | No           |
| [storage_redis](cache-storage.md#storage_redis)         | Yes          |

The cache invalidation works on the table-level, that is, a modification made
to a particular table will cause all cache entries that refer to that table to
be invalidated, irrespective of whether the modification actually has an impact
on the cache entries or not. In practice this means that updates should occur
relatively rarely, as otherwise the cache will never have time to become warm,
before it is made cold again.

For instance, suppose the result of the following SELECT has been cached

```
SELECT * FROM t WHERE a=1;
```

An insert like

```
INSERT INTO t SET a=42;
```

will cause the cache entry containing the result of that SELECT to be invalidated even if the INSERT actually does not affect it. Please see [invalidate](cache-settings.md#invalidate) for how to enable the invalidation.

When invalidation has been enabled MaxScale must be able to completely parse a SELECT statement for its results to be stored in the cache. The reason is that in order to be able to invalidate cache entries, MaxScale must know what tables a SELECT statement depends upon. Consequently, if (and only if) invalidation has been enabled and MaxScale fails to parse a statement, the result of that particular statement will not be cached.

When invalidation has been enabled, MaxScale will also parse all UPDATE, INSERT and DELETE statements, in order to find out what tables are modified. If that parsing fails, MaxScale will _by default_ clear the entire cache. The reason is that unless MaxScale can completely parse the statement it cannot know what tables are modified and hence not what cache entries should be invalidated. Consequently, to prevent stale data from being returned, the entire cache is cleared. The default behaviour can be changed using the configuration parameter [clear\_cache\_on\_parse\_errors](cache-settings.md#clear_cache_on_parse_errors).

Note that what threading approach is used has a big impact on the invalidation. Please see [Threads, Users and Invalidation](#threads-users-and-invalidation) for how the threading approach affects the invalidation.

Note also that since the invalidation may not, depending on how the cache has been configured, be visible to all sessions of all users, it is still important to configure a reasonable [soft](cache-settings.md#soft_ttl) and [hard](cache-settings.md#hard_ttl) TTL.

### Best Efforts

The invalidation offered by the MaxScale cache can be said to be of _best efforts_ quality. The reason is that in order to ensure that the cache in all circumstances reflects the state in the actual database, would require that the operations involving the cache and the MariaDB server are synchronized, which would cause an unacceptable overhead.

What _best efforts_ means in this context is best illustrated using an example.

Suppose a client executes the statement `SELECT * FROM tbl` and that the result is cached. Next time that or any other client executes the same statement, the result is returned from the cache and the MariaDB server will not be accessed at all.

If a client now executes the statement `INSERT INTO tbl VALUES (...)`, the cached value for the `SELECT` statement above and all other statements that are dependent upon `tbl` will be invalidated. That is, the next time someone executes the statement `SELECT * FROM tbl` the result will again be fetched from the MariaDB server and stored to the cache.

However, suppose some client executes the statement `SELECT COUNT(*) FROM tbl` at the same time someone else executes the `INSERT ...` statement. A possible chain of events is as follows:

```
Timeline 1                 Timeline 2

Clients execute       INSERT ...                 SELECT COUNT(*) FROM tbl
MaxScale -> DB                                   SELECT COUNT(*) FROM tbl
MaxScale -> DB        INSERT ...
```

That is, the `SELECT` is performed in the database server _before_ the`INSERT`. However, since the timelines are proceeding independently of each other, the events may be re-ordered as far as the cache is concerned.

```
MaxScale -> Cache     Delete invalidated values
MaxScale -> Cache                                Store result and invalidation key
```

That is, the cached value for `SELECT COUNT(*) FROM tbl` will reflect the situation _before_ the insert and will thus not be correct.

The stale result will be returned until the value has reached its _time-to-live_ or its invalidation is caused by some update operation.

## Configuration

The cache is simple to add to any existing service. However, some experimentation may be required in order to find the configuration settings that provide the maximum benefit.

```
[Cache]
type=filter
module=cache
hard_ttl=30
soft_ttl=20
rules=...
...

[Cached-Routing-Service]
type=service
...
filters=Cache
```

Each configured cache filter uses a storage of its own. That is, if there are two services, each configured with a specific cache filter, then, even if queries target the very same servers the cached data will not be shared.

Two services can use the same cache filter, but then either the services should use the very same servers _or_ a completely different set of servers, where the used table names are different. Otherwise there can be unintended sharing.

## Settings

Every cache filter setting, with its type, default, and behavior, is described in [MaxScale Cache Settings](cache-settings.md), in alphabetical order.

## Runtime Configuration

The cache filter can be configured at runtime by executing SQL commands. If there is more than one cache filter in a service, only the first cache filter will be able to process the variables. The remaining filters will not see them and thus configuring them at runtime is not possible.

### `@maxscale.cache.populate`

Using the variable `@maxscale.cache.populate` it is possible to specify at runtime whether the cache should be populated or not. Its initial value is the value of the configuration parameter `enabled`. That is, by default the value is `true`.

The purpose of this variable is make it possible for an application to decide statement by statement whether the cache should be populated.

```
SET @maxscale.cache.populate=TRUE;
SELECT a, b FROM tbl;
SET @maxscale.cache.populate=FALSE;
SELECT a, b FROM tbl;
```

In the example above, the first `SELECT` will always be sent to the server and the result will be cached, provided the actual cache rules specifies that it should be. The second `SELECT` may be served from the cache, depending on the value of `@maxscale.cache.use` (and the cache rules).

The value of `@maxscale.cache.populate` can be queried

```
SELECT @maxscale.cache.populate;
```

but only _after_ it has been explicitly set once.

### `@maxscale.cache.use`

Using the variable `@maxscale.cache.use` it is possible to specify at runtime whether the cache should be used or not. Its initial value is the value of the configuration parameter `enabled`. That is, by default the value is `true`.

The purpose of this variable is make it possible for an application to decide statement by statement whether the cache should be used.

```
SET @maxscale.cache.use=TRUE;
SELECT a, b FROM tbl;
SET @maxscale.cache.use=FALSE;
SELECT a, b FROM tbl;
```

The first `SELECT` will be served from the cache, providing the rules specify that the statement should be cached, the cache indeed contains the result and the date is not stale (as specified by the _TTL_).

If the data is stale, the `SELECT` will be sent to the server **and** the cache entry will be updated, irrespective of the value of`@maxscale.cache.populate`.

If `@maxscale.cache.use` is `true` but the result is not found in the cache, and the result is subsequently fetched from the server, the result will **not** be added to the cache, unless`@maxscale.cache.populate` is also `true`.

The value of `@maxscale.cache.use` can be queried

```
SELECT @maxscale.cache.use;
```

but only after it has explicitly been set once.

### `@maxscale.cache.soft_ttl`

Using the variable `@maxscale.cache.soft_ttl` it is possible at runtime to specify _in seconds_ what _soft ttl_ should be applied. Its initial value is the value of the configuration parameter `soft_ttl`. That is, by default the value is 0.

The purpose of this variable is make it possible for an application to decide statement by statement what _soft ttl_ should be applied.

```
SET @maxscale.cache.soft_ttl=600;
SELECT a, b FROM unimportant;
SET @maxscale.cache.soft_ttl=60;
SELECT c, d FROM important;
```

When data is `SELECT`ed from the unimportant table `unimportant`, the data will be returned from the cache provided it is no older than 10 minutes, but when data is `SELECT`ed from the important table `important`, the data will be returned from the cache provided it is no older than 1 minute.

Note that `@maxscale.cache.hard_ttl` overrules `@maxscale.cache.soft_ttl` in the sense that if the former is less that the latter, then _soft ttl_ will, when used, be adjusted down to the value of _hard ttl_.

The value of `@maxscale.cache.soft_ttl` can be queried

```
SELECT @maxscale.cache.soft_ttl;
```

but only after it has explicitly been set once.

### `@maxscale.cache.hard_ttl`

Using the variable `@maxscale.cache.hard_ttl` it is possible at runtime to specify _in seconds_ what _hard ttl_ should be applied. Its initial value is the value of the configuration parameter `hard_ttl`. That is, by default the value is 0.

The purpose of this variable is make it possible for an application to decide statement by statement what _hard ttl_ should be applied.

Note that as `@maxscale.cache.hard_ttl` overrules `@maxscale.cache.soft_ttl`, is important to ensure that the former is at least as large as the latter and for best overall performance that it is larger.

```
SET @maxscale.cache.soft_ttl=600, @maxscale.cache.hard_ttl=610;
SELECT a, b FROM unimportant;
SET @maxscale.cache.soft_ttl=60, @maxscale.cache.hard_ttl=65;
SELECT c, d FROM important;
```

The value of `@maxscale.cache.hard_ttl` can be queried

```
SELECT @maxscale.cache.hard_ttl;
```

but only after it has explicitly been set once.

## Client Driven Caching

With `@maxscale.cache.populate` and `@maxscale.cache.use` is it possible to make the caching completely client driven.

Provide no `rules` file, which means that _all_ `SELECT` statements are subject to caching and that all users receive data from the cache. Set the startup mode of the cache to _disabled_.

```
[TheCache]
type=filter
module=cache
enabled=false
```

Now, in order to _mark_ statements that should be cached, set`@maxscale.cache.populate` to `true`, and perform those `SELECT`s.

```
SET @maxscale.cache.populate=TRUE;
SELECT a, b FROM tbl1;
SELECT c, d FROM tbl2;
SELECT e, f FROM tbl3;
SET @maxscale.cache.populate=FALSE;
```

Note that those `SELECT`s must return something in order for the statement to be _marked_ for caching.

After this, the value of `@maxscale.cache.use` will decide whether or not the cache is considered.

```
SET @maxscale.cache.use=TRUE;
SELECT a, b FROM tbl1;
SET @maxscale.cache.use=FALSE;
```

With `@maxscale.cache.use` being `true`, the cache is considered and the result returned from there, if not stale. If it is stale, the result is fetched from the server and the cached entry is updated.

By setting a very long _TTL_ it is possible to prevent the cache from ever considering an entry to be stale and instead manually cause the cache to be updated when needed.

```
UPDATE tbl1 SET a = ...;
SET @maxscale.cache.populate=TRUE;
SELECT a, b FROM tbl1;
SET @maxscale.cache.populate=FALSE;
```

## Threads, Users and Invalidation

What caching approach is used and how different users are treated has a significant impact on the behaviour of the cache. In the following the implication of different combinations is explained.

The table and the following subsections describe `storage_inmemory`. With a
shared storage the cached data is not duplicated across threads; see
[cached\_data](cache-settings.md#cached_data).

| cached\_data/users | mixed                                                                                                                          | isolated                                                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| thread\_specific   | No thread contention. Data/work duplicated across threads. May cause unintended sharing.                                       | No thread contention. Data/work duplicated across threads and users. No unintended sharing. Requires the most amount of memory. |
| shared             | Thread contention under high load. No duplicated data/work. May cause unintended sharing. Requires the least amount of memory. | Thread contention under high load. Data/work duplicated across users. No unintended sharing.                                    |

### Invalidation

Invalidation takes place only in the current cache, so how _visible_ the invalidation is, depends upon the configuration value of`cached_data`.

#### `cached_data=thread_specific`

The invalidation is visible only to the sessions that are handled by the same worker thread where the invalidation occurred. Sessions of the same or other users that are handled by different worker threads will not see the new value before the TTL causes the value to be refreshed.

#### `cached_data=shared`

The invalidation is immediately visible to all sessions of all users.

## Rules

The rules that decide what is cached and when a cached result is used are described in [MaxScale Cache Rules](cache-rules.md).

## Security

As the cache is not aware of grants, unless the cache has been explicitly configured who the caching should apply to, the presence of the cache may provide a user with access to data he should not have access to. Note that the following applies _only_ if `users=mixed` has been configured. If `users=isolated` has been configured, then there can never be any unintended sharing between users.

Suppose there is a table `access` that the user _alice_ has access to, but the user _bob_ does not. If _bob_ tries to access the table, he will get an error as reply:

```
MySQL [testdb]> select * from access;
ERROR 1142 (42000): SELECT command denied to user 'bob'@'localhost' for table 'access'
```

If we now setup caching for the table, using the simplest possible rules file, _bob_ will get access to data from the table, provided he executes a select identical with one _alice_ has executed.

For instance, suppose the rules look as follows:

```
{
    "store": [
        {
            "attribute": "table",
            "op": "=",
            "value": "access"
        }
    ]
}
```

If _alice_ now queries the table, she will get the result, which also will be cached:

```
MySQL [testdb]> select * from access;
+------+------+
| a    | b    |
+------+------+
|   47 |   11 |
+------+------+
```

If _bob_ now executes the very same query, and the result is still in the cache, it will be returned to him.

```
MySQL [testdb]> select current_user();
+----------------+
| current_user() |
+----------------+
| bob@127.0.0.1  |
+----------------+
1 row in set (0.00 sec)

MySQL [testdb]> select * from access;
+------+------+
| a    | b    |
+------+------+
|   47 |   11 |
+------+------+
```

That can be prevented, by explicitly declaring in the rules that the caching should be applied to _alice_ only.

```
{
    "store": [
        {
            "attribute": "table",
            "op": "=",
            "value": "access"
        }
    ],
    "use": [
        {
            "attribute": "user",
            "op": "=",
            "value": "'alice'@'%'"
        }
    ]
}
```

With these rules in place, _bob_ is again denied access, since queries targeting the table `access` will in his case not be served from the cache.

## Storage

The storage modules (in-memory, GridGain, memcached and Redis) and their settings are described in [MaxScale Cache Storage](cache-storage.md).

## Example

In the following we define a cache _MyCache_ that uses the cache storage module`storage_inmemory` and whose _soft ttl_ is `30` seconds and whose _hard ttl_ is`45` seconds. The cached data is shared between all threads and the maximum size of the cached data is `50` mebibytes. The rules for the cache are in the file`cache_rules.json`.

### Configuration

```
[MyCache]
type=filter
module=cache
storage=storage_inmemory
soft_ttl=30
hard_ttl=45
cached_data=shared
max_size=50Mi
rules=cache_rules.json

[MyService]
type=service
...
filters=MyCache
```

### `cache_rules.json`

The rules specify that the data of the table `sbtest` should be cached.

```
{
    "store": [
        {
            "attribute": "table",
            "op": "=",
            "value": "sbtest"
        }
    ]
}
```

## Performance

When the cache filter was introduced, the most significant factor affecting the performance of the cache was whether the statements needed to be parsed. Initially, all statements were parsed in order to exclude `SELECT` statements that use non-cacheable functions, access non-cacheable variables or refer to system or user variables. Later, the default value of the `selects` parameter was changed to `assume_cacheable`, to maximize the default performance.

With the default configuration, the cache itself will not cause the statements to be parsed. However, even with `assume_cacheable` configured, a rule referring specifically to a _database_, _table_ or _column_ will still cause the statement to be parsed.

For instance, a simple rule like

```
{
    "store": [
        {
            "attribute": "database",
            "op": "=",
            "value": "db1"
        }
    ]
}
```

cannot be fulfilled without parsing the statement.

If the rule is instead expressed using a regular expression

```
{
    "store": [
        {
            "attribute": "query",
            "op": "like",
            "value": "FROM db1\\..*"
        }
    ]
}
```

then the statement will not be parsed.

However, when the [query classifier cache](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#query_classifier_cache_size) was introduced, the parsing cost was significantly reduced and the cost for parsing and regular expression matching is roughly the same.

In the following is a table with numbers giving a rough picture of the relative cost of different approaches.

In the table, _regexp match_ means that the cacheable statements were picked out using a rule like

```
{
    "attribute": "query",
    "op": "unlike",
    "value": "FROM nomatch"
}
```

while _exact match_ means that the cacheable statements were picked out using a rule like

```
{
    "attribute": "database",
    "op": "!=",
    "value": "nomatch"
}
```

The exact match rule requires all statements to be parsed.

As the purpose of the test is to illustrate the overhead of different approaches, the rules were formulated so that all SELECT statements would match.

Note that these figures were obtained by running sysbench, MaxScale and the server in the same computer, so they are only indicative.

| selects           | Rule         | qps |
| ----------------- | ------------ | --- |
| assume\_cacheable | none         | 100 |
| assume\_cacheable | regexp match | 83  |
| assume\_cacheable | exact match  | 83  |
| verify\_cacheable | none         | 80  |
| verify\_cacheable | regexp match | 80  |
| verify\_cacheable | exact match  | 80  |

For comparison, without caching, the qps is `33`.

As can be seen, due to the query classifier cache there is no difference between exact and regex based matching.

### Summary

For maximum performance:

* Arrange the situation so that the default `selects=assume_cacheable` can be used, and use no rules.

Otherwise it is mostly a personal preference whether exact or regex based rules are used. However, one should always test with real data and real queries before choosing one over the other.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
