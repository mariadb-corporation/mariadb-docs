---
description: >-
  Reference for every cache filter setting, in alphabetical order: storage,
  time-to-live, size limits, rules, invalidation, and transactions.
---

# MaxScale Cache Settings

These settings go in the cache filter section of the MaxScale configuration file and are listed in alphabetical order. For how to configure the filter, see [Configuration](README.md#configuration).

The cache filter has no mandatory parameters but a range of optional ones. Note that it is advisable to specify `max_size` to prevent the cache from using up all memory there is, in case there is very little overlap among the queries.

## `cache_in_transactions`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `never`, `read_only_transactions`, `all_transactions`
* Default: `all_transactions`
* Description: Manages how the cache is used and updated during transactions.

An enumeration option specifying how the cache should behave when there are active transactions:

* `never`: When there is an active transaction, no data will be returned from the cache, but all requests will always be sent to the backend. The cache will be populated inside explicitly read-only transactions. Inside transactions that are not explicitly read-only, the cache will be populated until the first non-SELECT statement.
* `read_only_transactions`: The cache will be used and populated inside explicitly read-only transactions. Inside transactions that are not explicitly read-only, the cache will be populated, but not used until the first non-SELECT statement.
* `all_transactions`: The cache will be used and populated inside explicitly read-only transactions. Inside transactions that are not explicitly read-only, the cache will be used and populated until the first non-SELECT statement.

```
cache_in_transactions=never
```

Default is `all_transactions`.

The values `read_only_transactions` and `all_transactions` have roughly the same effect as changing the isolation level of the backend to `read_committed`.

## `cached_data`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `shared`, `thread_specific`
* Default: `thread_specific`
* Description: Determines whether cached data remains thread-specific or shared across threads.

An enumeration option specifying how data is shared between threads. The allowed values are:

* `shared`: The cached data is shared between threads. On the one hand it implies that there will be synchronization between threads, on the other hand that all threads will use data fetched by any thread.
* `thread_specific`: The cached data is specific to a thread. On the one hand it implies that no synchronization is needed between threads, on the other hand that the very same data may be fetched and stored multiple times.

The above applies to `storage_inmemory`. With a shared storage
(`storage_redis`, `storage_gridgain`) the cached data is held by the
storage server and is the same for all threads, irrespective of the value
of `cached_data`; data stored by one thread is used by all. The value only
affects the bookkeeping MaxScale itself does. With `thread_specific`:

* the queries known to be faster than
  [min\_query\_duration](#min_query_duration) are
  remembered by each thread separately, so each thread must learn them, and
* an entry that has become stale may be refreshed once per thread, instead
  of once.

The number of connections to the storage server does not depend on
`cached_data`: `storage_redis` uses one connection per client session and
`storage_gridgain` one per thread. `storage_gridgain` can only be used with
`cached_data=thread_specific`.

```
cached_data=shared
```

Default is `thread_specific`. See `max_count` and `max_size` what implication changing this setting to `shared` has.

## `clear_cache_on_parse_errors`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`
* Description: Controls whether the cache is cleared when modifying statements are not parsed correctly.

This boolean option specifies how the cache should behave in case of parsing errors when invalidation has been enabled.

* `true`: If the cache fails to parse an UPDATE/INSERT/DELETE statement then all cached data will be cleared.
* `false`: A failure to parse an UPDATE/INSERT/DELETE statement is ignored and no invalidation will take place due that statement.

The default value is `true`.

Changing the value to `false` may mean that stale data is returned from the cache, if an UPDATE/INSERT/DELETE cannot be parsed and the statement affects entries in the cache.

## `debug`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`
* Description: Uses a bitmask value to control the cache's debug logging level.

An integer value, using which the level of debug logging made by the cache can be controlled. The value is actually a bitfield with different bits denoting different logging.

* `0` (`0b00000`) No logging is made.
* `1` (`0b00001`) A matching rule is logged.
* `2` (`0b00010`) A non-matching rule is logged.
* `4` (`0b00100`) A decision to use data from the cache is logged.
* `8` (`0b01000`) A decision not to use data from the cache is logged.
* `16` (`0b10000`) Higher level decisions are logged.

Default is `0`. To log everything, give `debug` a value of `31`.

```
debug=31
```

## `enabled`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`
* Description: Manages whether the cache is enabled or disabled at startup.

Specifies whether the cache is initially enabled or disabled.

```
enabled=false
```

The value affects the initial state of the MaxScale user variables using which the behaviour of the cache can be modified at runtime. Please see [Runtime Configuration](README.md#runtime-configuration) for details.

## `hard_ttl`

* Type: [duration](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)
* Description: Specifies how long cached data can last before being deleted and reloaded.

_Hard time to live_; the maximum amount of time the cached result is used before it is discarded and the result is fetched from the backend (and cached). See also [soft\_ttl](#soft_ttl).

```
hard_ttl=60s
```

## `invalidate`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `never`, `current`
* Default: `never`
* Description: Manages how cached data is invalidated when changes occur.

An enumeration option specifying how the cache should invalidate cache entries.

```
* `never`: No invalidation is performed. This is the default.
* `current`: When a modification is made, entries in the cache used by
  the current session are invalidated. Other sessions that use the same
  cache will also be affected, but sessions that use another cache will
  not.
```

The effect of `current` depends upon the value of `cached_data`. If the value is `shared`, that is, all threads share the same cache, then the effect of an invalidation is immediately visible to all sessions, as there is just one cache. However, if the value is `thread_specific`, then an invalidation will affect only the cache that the session happens to be using.

This applies to `storage_inmemory`. With `storage_redis` the invalidation
is performed in the storage server, so it is immediately visible to all
sessions, irrespective of the value of `cached_data`.

If it is important and _sufficient_ that an application immediately sees a change that it itself has caused, then a combination of `invalidate=current` and `cached_data=thread_specific` can be used.

If it is important that an application _immediately_ sees all changes, irrespective of who has caused them, then a combination of `invalidate=current` and `cached_data=shared` _must_ be used.

## `max_count`

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)
* Description: Specifies the maximum amount of data that cache can store.

The maximum number of items the cache may contain. If the limit has been reached and a new item should be stored, then an older item will be evicted.

Note that if `cached_data` is `thread_specific` then this limit will be applied to each cache _separately_. That is, if a thread specific cache is used, then the total number of cached items is #threads \* the value of `max_count`.

```
max_count=1000
```

## `max_resultset_rows`

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)
* Description: Defines the maximum number of rows in a result set that can be cached.

Specifies the maximum number of rows a resultset can have in order to be stored in the cache. A resultset larger than this, will not be stored.

```
max_resultset_rows=1000
```

## `max_resultset_size`

* Type: [size](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)
* Description: Specifies the maximum result set size that can be cached.

Specifies the maximum size of a resultset, for it to be stored in the cache. A resultset larger than this, will not be stored.

```
max_resultset_size=128Ki
```

Note that the value of `max_resultset_size` should not be larger than the value of `max_size`.

## `max_size`

* Type: [size](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)
* Description: Defines the maximum total size of the cache.

The maximum size the cache may occupy. If the limit has been reached and a new item should be stored, then some older item(s) will be evicted to make space.

Note that if `cached_data` is `thread_specific` then this limit will be applied to each cache _separately_. That is, if a thread specific cache is used, then the total size is #threads \* the value of `max_size`.

```
max_size=100Mi
```

## `max_uncached_query_count`

Available since MaxScale 25.10.4.

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `10000`
* Description: Defines the maximum number of queries faster than `min_query_duration` that are remembered so that their cache lookups can be skipped.

The maximum number of queries — observed to be faster than
[min\_query\_duration](#min_query_duration) — that
MaxScale remembers in order to skip a cache lookup that would in any case
miss. When the limit has been reached and a new such query is seen, the
least recently used one is forgotten; the only consequence is that a lookup
will be attempted, and the query's duration measured, once more.

A value of `0` disables this bookkeeping, in which case a lookup is always
attempted even for queries known to be fast. The setting has no effect if
`min_query_duration` is `0`.

Note that if `cached_data` is `thread_specific` then this limit will be
applied to each cache _separately_. That is, if a thread specific cache is
used, then the total number of remembered queries is #threads \* the value
of `max_uncached_query_count`.

Tuning: the value need only be large enough to hold the set of _recurring_
fast queries; a query seen just once gains nothing from being remembered.
Because the cache key is a hash of the exact query text (literal values
included), queries that differ only in a literal are distinct keys, so a
point-lookup workload can have a very large distinct fast-query space; if
many distinct fast queries recur, a larger value increases how often the
lookup is skipped. Setting it too low is not harmful — an evicted entry
merely causes its lookup to be attempted, and its duration re-measured, once
more.

The `uncached_queries` diagnostics shown by `maxctrl show filter` report
`hits` (lookups skipped) and `misses` (below-threshold queries that were not
skipped); a persistently low `hits / (hits + misses)` ratio means the value
is delivering little. Raise it and check whether the ratio improves; if it
does not, the fast queries are mostly one-offs and the value can be set to 0.

The benefit is greatest with a networked storage (`storage_redis`,
`storage_gridgain`), where a skipped lookup avoids a server round-trip. With
`storage_inmemory` the skipped lookup is only a local hash probe, so this
setting has little effect and a small value — or `0` — is appropriate. The
memory cost is roughly 90 bytes per remembered query, per storage instance.

```
max_uncached_query_count=10000
```

## `min_query_duration`

Available since MaxScale 25.10.4.

* Type: [duration](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)
* Description: Defines the minimum time a query must take on the backend for its result to be stored in the cache.

Specifies the minimum duration a query must take on the backend for its
result to be stored in the cache. If a query executes faster than this, its
result is _not_ cached.

The rationale is that the result of a fast query is cheap to fetch from the
backend, so caching it saves little while still consuming cache space and
being subject to the same consistency caveats as any other cached value
(see [Best Efforts](README.md#best-efforts)). What counts as "fast"
depends on the deployment; for instance, a cache reached over the network
has a higher break-even point than a local one.

By default the value is `0s`, which means the duration of a query is not
considered and all cacheable results are stored.

The duration is measured by MaxScale as the time between the query being
sent to the backend and its complete result having been received, and so
includes both the network round-trip and the execution time. As the
measurement is taken with the granularity of the event loop, a threshold
smaller than a few milliseconds is not meaningful.

To avoid repeatedly attempting a cache lookup that is bound to miss for a
query whose result is not stored, MaxScale remembers the queries observed
to be faster than `min_query_duration` and skips the lookup for them. The
size of that bookkeeping is bounded by
[max\_uncached\_query\_count](#max_uncached_query_count).

```
min_query_duration=10ms
```

## `rules`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""` (no rules)
* Description: Specifies the file path containing caching rules.

Specifies the path of the file where the caching rules are stored. A relative path is interpreted relative to the _data directory_ of MariaDB MaxScale.

```
rules=/path/to/rules-file
```

Note that the rules will be reloaded, and applied if different, every time a dynamic configuration change is made. Thus, to cause a reloading of the rules, alter the rules parameter to the same value it has.

```
maxctrl alter filter MyCache rules='/path/to/rules-file'
```

## `selects`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `assume_cacheable`, `verify_cacheable`
* Default: `assume_cacheable`
* Description: Controls whether SELECT statements are considered to be cacheable or validated before caching.

An enumeration option specifying what approach the cache should take with respect to `SELECT` statements. The allowed values are:

* `assume_cacheable`: The cache can assume that all `SELECT` statements, without exceptions, are cacheable.
* `verify_cacheable`: The cache can not assume that all `SELECT` statements are cacheable, but must verify that.

```
selects=verify_cacheable
```

Default is `assume_cacheable`. In this case, all `SELECT` statements are assumed to be cacheable and will be parsed _only_ if some specific rule requires that.

If `verify_cacheable` is specified, then all `SELECT` statements will be parsed and only those that are safe for caching - e.g. do _not_ call any non-cacheable functions or access any non-cacheable variables - will be subject to caching.

If `verify_cacheable` has been specified, the cache will not be used in the following circumstances:

* The `SELECT` uses any of the following functions: `BENCHMARK`,`CONNECTION_ID`, `CONVERT_TZ`, `CURDATE`, `CURRENT_DATE`, `CURRENT_TIMESTAMP`,`CURTIME`, `DATABASE`, `ENCRYPT`, `FOUND_ROWS`, `GET_LOCK`, `IS_FREE_LOCK`,`IS_USED_LOCK`, `LAST_INSERT_ID`, `LOAD_FILE`, `LOCALTIME`, `LOCALTIMESTAMP`,`MASTER_POS_WAIT`, `NOW`, `RAND`, `RELEASE_LOCK`, `SESSION_USER`, `SLEEP`,`SYSDATE`, `SYSTEM_USER`, `UNIX_TIMESTAMP`, `USER`, `UUID`, `UUID_SHORT`.
* The `SELECT` accesses any of the following fields: `CURRENT_DATE`,`CURRENT_TIMESTAMP`, `LOCALTIME`, `LOCALTIMESTAMP`
* The `SELECT` uses system or user variables.

Note that parsing all `SELECT` statements carries a performance cost. Please read [performance](README.md#performance) for more details.

## `soft_ttl`

* Type: [duration](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)
* Description: Determines how long cached data is used before being refreshed from the backend.

_Soft time to live_; the amount of time - in seconds - the cached result is used before it is refreshed from the server. When `soft_ttl` has passed, the result will be refreshed when the _first_ client requests the value.

However, as long as [hard\_ttl](#hard_ttl) has not passed, _all_ other clients requesting the same value will use the result from the cache while it is being fetched from the backend. That is, as long as `soft_ttl` but not `hard_ttl` has passed, even if several clients request the same value at the same time, there will be just one request to the backend.

```
soft_ttl=60s
```

If the value of `soft_ttl` is larger than `hard_ttl` it will be adjusted down to the same value.

## `storage`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `storage_inmemory`
* Description: Defines the storage module used by the cache.

The name of the module that provides the storage for the cache. That module will be loaded and provided with the value of `storage_options` as argument. For instance:

```
storage=storage_redis
```

See [Storage](README.md#storage) for what storage modules are available.

## `storage_options`

* Type: string
* Mandatory: No
* Dynamic: No
* Default:
* Description: Deprecated. Previously used to pass configuration options to the storage module.

**NOTE** Deprecated in 23.02.

A string that is provided verbatim to the storage module specified in `storage`, when the module is loaded. Note that the needed arguments and their format depend upon the specific module.

From 23.02 onwards, the storage module configuration should be provided using nested parameters.

## `timeout`

* Type: [duration](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `5s`
* Description: Specifies the timeout for processes involving external storage backends.

The _timeout_ used when performing operations to distributed storages such as _redis_ or _memcached_.

```
timeout=7000ms
```

## `users`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `mixed`, `isolated`
* Default: `mixed`
* Description: Manages whether cached data is stored separately for each user or shared between users.

An enumeration option specifying how the cache should cache data for different users.

```
* `mixed`: The data of different users is stored in the same
  cache. This is the default and may cause that a user can
  access data he should not have access to.
* `isolated`: Each user has a unique cache and there can be
  no unintended sharing.
```

Note that if `isolated` has been specified, then each user will conceptually have a cache of his own, which is populated independently from each other. That is, if two users make the same query, then the data will be fetched twice and also stored twice. So, a `isolated` cache will in general use more memory and cause more traffic to the backend compared to a `mixed` cache.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
