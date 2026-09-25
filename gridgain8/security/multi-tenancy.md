---
description: >-
  Isolate tenant data in GridGain by creating per-tenant caches and assigning
  per-cache security permissions.
---

# Multi-Tenancy

In multi-tenant applications, data subsets that belong to different tenants are required to be isolated from each other. GridGain supports this by creating separate caches for different tenants and assigning proper per-cache security permissions.

Since caches can be created and destroyed dynamically on demand, you don't have to preconfigure caches for all tenants. Once a new tenant needs to be added to the system, a new cache (or caches) should be created for this tenant. Permissions for the tenant's users should be modified to allow access to these caches. Access to all other caches should be denied. This way you're guaranteed that other tenants will never read or update data of this new tenant.

As an example, suppose there are two tenants and each of them needs to have its own isolated set of data. To achieve this, we will create two independent caches:

{% tabs %}
{% tab title="Java" %}
```java
// Create two caches with default configuration.
ignite.createCache(new CacheConfiguration("dataCache_tenant1"));
ignite.createCache(new CacheConfiguration("dataCache_tenant2"));
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
ignite.CreateCache<int, int>(new CacheConfiguration("dataCache_tenant1"));
ignite.CreateCache<int, int>(new CacheConfiguration("dataCache_tenant2"));
```
{% endtab %}
{% endtabs %}

Each tenant will work with its own cache. Therefore, each tenant should receive the set of permissions that will give access only to the cache that belongs to this tenant.

Permissions for `tenant1` allows full access to cache `dataCache_tenant1` and denies access to other caches:

{% code title="JSON" %}
```json
{
    {
        "cache":"dataCache_tenant1",
        "permissions":["CACHE_READ", "CACHE_PUT", "CACHE_REMOVE"]
    },
    "defaultAllow":"false"
}
```
{% endcode %}

Permissions for `tenant2` are similar, but allows access to cache `dataCache_tenant2` instead:

{% code title="JSON" %}
```json
{
    {
        "cache":"dataCache_tenant2",
        "permissions":["CACHE_READ", "CACHE_PUT", "CACHE_REMOVE"]
    },
    "defaultAllow":"false"
}
```
{% endcode %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
