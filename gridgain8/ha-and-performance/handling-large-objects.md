---
description: >-
  Considerations for storing and processing large objects in GridGain, including
  multipage objects, concurrency, field counts, and schemas.
---

# Handling Large Objects

Working with larger objects requires specific considerations. If you handle them incorrectly, it may lead to worsened performance.

## Multipage Objects

If the object is large enough to occupy multiple pages in the database, it causes multiple page reads each time it is called, which may mean reduced performance. By default, each page is 4KB, but you can adjust it up to 16KB by using the [DataStorageConfiguration.pageSize](performance-tuning/persistence-tuning.md#adjusting-page-size) parameter.

Objects that take multiple pages may also lead to wasted space and fragmentation - for example, if your objects are 5KB, but page is only 4KB, 3KB will be allocated to other data or wasted. Use the `pageFillFactor` metric to see how well pages in your database are filled.

When you use in-memory clusters to store large objects and have [eviction policies](../gridgain8-usage/memory-configuration/eviction-policies.md) configured, make sure that there is always enough memory to store new objects. When memory is almost full, eviction mechanism kicks in and removes old objects according to eviction policy.

To give Ignite an idea of how much memory has to be freed use the `setEmptyPagesPoolSize` setting. It should reflect how much memory is occupied by the biggest object expected to appear.

## Large Object Concurrency

When running concurrent operations of large objects, make sure you have sufficient heap memory available. Each thread will load objects in memory separately. For example, one 1MB object processed in 1000 threads will require over 1GB of heap memory.

Make sure to have sufficient memory prepared, of throttle the number of threads working with larger objects.

## Large Number of Fields

When GridGain interacts with objects, it reads all fields in them, including null fields.  This may lead to unexpected performance issues when the object has a large number of irrelevant or null fields.

To improve performance of your application, use smaller objects with relevant fields when possible, and avoid excessive reads of larger objects when not.

## Different Schemas

When GridGain stores your object, it also creates a schema based on filled object fields to speed up interactions. If a schema already exists, it will be used for all objects that match the schema. When a new object is stored with a different filled object fields, a new schema is created. Large number of different objects causes slower object interactions compared to storing more uniform objects.

To reduce memory use for schemas and improve performance, fill your object fields in the same way when you store them. Storing multiple smaller uniform objects is generally preferred to having large objects with empty fields.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
