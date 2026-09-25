---
description: >-
  How GridGain resolves cache update conflicts, including automatic resolution
  and the CacheConflictResolver interface for custom conflict handling.
---

# Conflict Resolution

When the cache is updated from some external sources such as a remote data center or a persistent local store, there is a chance you would like to decide whether to proceed with the update, keep the old value, or produce some other value merging the old and new values. To achieve this, GridGain offers the `CacheConflictResovler` interface.

By default, GridGain attempts to resolve conflicts automatically. This is achieved by comparing the topology version and the order of old and new entries. In case the conflict is between entries from different data centers, GridGain will invoke the user-provided conflict resolver to let the user decide what to do in that case.

If you want to control all the cache updates with a custom conflict resolver, then you should set `GridGainCacheConfiugration.setConflictMode()` to `CacheConflictMode.AUTO`.

When a conflict is detected and the user-provided implementation of `CacheConflictResolver` is invoked, a special object `CacheConflictContext` is passed to it. This object has all the necessary data to make a decision regarding the conflict. Conflict resolution can have one of the following outcomes:

- *Use new* - Incoming update must overwrite existing entry (`CacheConflictContext.useNew()`).
- *Use old* - Incoming update must be ignored and the existing entry remains untouched (`CacheConflictContext.useOld()`).
- *Merge* - Neither old nor new entry should be used; user provides new value for cache entry manually; such update is considered as an update in the local data center (`CacheConflictContext.merge()`).

If a conflict is detected and a conflict resolver is not set, then the incoming update will overwrite the existing value.

## Configuration

`GridGainCacheConfiguration` has the following optional configuration properties:

| Setter Method | Description | Default Value |
|---|---|---|
| `setConflictResolverMode(CacheConflictMode)` | Conflict resolution mode. | `AUTO` |
| `setConflictResolver(CacheConflictResolver)` | Conflict resolver. |  |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
