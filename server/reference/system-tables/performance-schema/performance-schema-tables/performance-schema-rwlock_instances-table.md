---
description: >-
  The rwlock_instances table lists all active read-write lock instances, showing
  the write-lock owner and the number of waiting readers or writers.
---

# Performance Schema rwlock\_instances Table

The `rwlock_instances` table lists all read write lock (rwlock) instances that the Performance Schema sees while the server is executing. A read write is a mechanism for ensuring threads can either share access to common resources, or have exclusive access.

The [performance\_schema\_max\_rwlock\_instances](../performance-schema-system-variables.md#performance_schema_max_rwlock_instances) system variable specifies the maximum number of instrumented rwlock objects.

The `rwlock_instances` table contains the following columns:

| Column                        | Description                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------- |
| NAME                          | Instrument name associated with the read write lock                                   |
| OBJECT\_INSTANCE\_BEGIN       | Address in memory of the instrumented lock                                            |
| WRITE\_LOCKED\_BY\_THREAD\_ID | THREAD\_ID of the locking thread if locked in write (exclusive) mode, otherwise NULL. |
| READ\_LOCKED\_BY\_COUNT       | Count of current read locks held                                                      |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
