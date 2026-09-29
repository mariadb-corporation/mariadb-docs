---
description: >-
  Configure how GridGain persists cache data to external stores — third-party
  databases and custom cache store implementations.
---

# Persistence

Beyond GridGain's native persistence, you can back a cache with an external store — a third-party database such as an RDBMS — or implement your own cache store. This section covers those options. For the concept of GridGain's built-in native persistence, see [Storage](../../architecture/storage/README.md).

{% columns %}
{% column %}
{% content-ref url="custom-cache-store.md" %}
[Implementing Custom Cache Store](custom-cache-store.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Implementing a custom CacheStore in GridGain to use an external data store as the underlying storage for a cache, with a JDBC example.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="external-storage.md" %}
[External Storage](external-storage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Using GridGain as a caching layer on top of an external database, including read-through/write-through, write-behind caching, and RDBMS and NoSQL integration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../services/services.md" %}
[Services](../services/services.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to implement, deploy, access, and re-deploy GridGain services, including deployment strategies, interceptors, and the IgniteServices framework.
{% endcolumn %}
{% endcolumns %}
